"""Promote one Langfuse v4 observation into a regression dataset."""

from __future__ import annotations

import json
from typing import Any

from langfuse import Langfuse


def promote_observation_to_dataset(
    langfuse: Langfuse,
    *,
    trace_id: str,
    observation_id: str,
    dataset_name: str,
    expected_output: Any,
) -> Any:
    observation_filter = json.dumps(
        [
            {
                "type": "string",
                "column": "id",
                "operator": "=",
                "value": observation_id,
            }
        ]
    )
    response = langfuse.api.observations.get_many(
        fields="io",
        trace_id=trace_id,
        filter=observation_filter,
        limit=1,
    )
    if len(response.data) != 1 or response.data[0].id != observation_id:
        raise LookupError(f"observation {observation_id!r} was not found in trace {trace_id!r}")

    observation = response.data[0]
    return langfuse.create_dataset_item(
        dataset_name=dataset_name,
        input=observation.input,
        expected_output=expected_output,
        source_trace_id=trace_id,
        source_observation_id=observation_id,
    )
