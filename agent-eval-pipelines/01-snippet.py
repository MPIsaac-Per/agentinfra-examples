# Illustrative shape only. The companion repo's tests/test_langfuse_experiment.py
# carries the pinned langfuse and provider-SDK versions and the exact model ID
# used at the time of that commit. Verify against
# https://langfuse.com/docs/evaluation/dataset-runs/run-via-sdk before deploying.
from langfuse import Langfuse
from anthropic import Anthropic  # or the provider SDK of choice

langfuse = Langfuse()
client = Anthropic()

CANDIDATE_MODEL = "<provider-model-id-from-current-docs>"

def my_agent(*, item, **kwargs):
    response = client.messages.create(
        model=CANDIDATE_MODEL,
        max_tokens=1024,
        messages=[{"role": "user", "content": item.input["question"]}],
    )
    return response.content[0].text

def exact_match(*, output, expected_output, **kwargs):
    return {"name": "exact_match", "value": 1 if output.strip() == expected_output.strip() else 0}

dataset = langfuse.get_dataset(name="agent-regression-suite-v3")
dataset.run_experiment(
    name=f"baseline-{CANDIDATE_MODEL}-2026-04-26",
    task=my_agent,
    evaluators=[exact_match],
)
