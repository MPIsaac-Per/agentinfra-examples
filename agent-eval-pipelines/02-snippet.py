import json
import random
from statistics import mean
from anthropic import Anthropic

client = Anthropic()

JUDGE_PROMPT_TEMPLATE = """Score the agent response on a 1-5 rubric for factual accuracy.
Return JSON only, shaped as {{"score": <int>, "reason": <str>}}.
Question: {question}
Expected: {expected}
Response: {response}"""


def judge(question: str, expected: str, response: str, model: str) -> dict:
    msg = client.messages.create(
        model=model,
        max_tokens=256,
        messages=[{
            "role": "user",
            "content": JUDGE_PROMPT_TEMPLATE.format(
                question=question, expected=expected, response=response
            ),
        }],
    )
    return json.loads(msg.content[0].text)


def _bootstrap_ci(values: list[int], iters: int = 1000, alpha: float = 0.05) -> tuple[float, float]:
    n = len(values)
    if n == 0:
        return (float("nan"), float("nan"))
    rng = random.Random(0)
    means = []
    for _ in range(iters):
        sample = [values[rng.randrange(n)] for _ in range(n)]
        means.append(sum(sample) / n)
    means.sort()
    lo = means[int((alpha / 2) * iters)]
    hi = means[int((1 - alpha / 2) * iters) - 1]
    return (lo, hi)


def calibrate(rows: list[dict], cheap_model: str, reference_model: str) -> dict:
    """Compare a candidate cheap judge against a reference judge on a held-out set.

    Reference judge is treated as a relative anchor, not ground truth.
    Each row is shaped {"question": str, "expected": str, "response": str}.
    """
    if not rows:
        return {"n": 0, "agreement_within_1": float("nan"), "mean_bias": float("nan"), "ci_95": (float("nan"), float("nan"))}
    deltas = []
    agreements = []
    for row in rows:
        small = judge(row["question"], row["expected"], row["response"], cheap_model)
        large = judge(row["question"], row["expected"], row["response"], reference_model)
        delta = small["score"] - large["score"]
        deltas.append(delta)
        agreements.append(1 if abs(delta) <= 1 else 0)
    return {
        "n": len(rows),
        "agreement_within_1": mean(agreements),
        "mean_bias": mean(deltas),
        "ci_95": _bootstrap_ci(agreements),
    }
