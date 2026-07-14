"""Run a Langfuse dataset experiment with an Anthropic candidate model.

Required environment variables are read by the provider SDKs when
``run_experiment`` is called. Importing this module has no network side effects.
"""

from __future__ import annotations

from typing import Any

from anthropic import Anthropic
from langfuse import Evaluation, Langfuse


def exact_match(
    *,
    input: Any,
    output: Any,
    expected_output: Any,
    metadata: dict[str, Any] | None,
    **_: dict[str, Any],
) -> Evaluation:
    del input, metadata
    if expected_output is None:
        return Evaluation(
            name="exact_match",
            value=0,
            comment="expected output is missing",
        )
    if not isinstance(output, str) or not isinstance(expected_output, str):
        return Evaluation(
            name="exact_match",
            value=0,
            comment="exact_match requires string output and expected_output",
        )
    return Evaluation(
        name="exact_match",
        value=int(output.strip() == expected_output.strip()),
    )


def run_experiment(*, model: str, dataset_name: str, run_name: str) -> Any:
    if not model.strip():
        raise ValueError("model must be a non-empty provider model ID")

    langfuse = Langfuse()
    anthropic = Anthropic()

    def run_agent(*, item: Any, **_: Any) -> str:
        question = item.input.get("question") if isinstance(item.input, dict) else None
        if not isinstance(question, str) or not question.strip():
            raise ValueError("dataset item input.question must be a non-empty string")
        response = anthropic.messages.create(
            model=model,
            max_tokens=1024,
            messages=[{"role": "user", "content": question}],
        )
        text_blocks = [block.text for block in response.content if block.type == "text"]
        return "".join(text_blocks)

    dataset = langfuse.get_dataset(name=dataset_name)
    return dataset.run_experiment(
        name=run_name,
        task=run_agent,
        evaluators=[exact_match],
    )
