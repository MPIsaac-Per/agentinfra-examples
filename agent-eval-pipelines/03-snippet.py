# Illustrative shape. Verify the v4 SDK call signatures against
# https://langfuse.com/docs/v4 and
# https://langfuse.com/docs/api-and-data-platform/features/query-via-sdk/
from langfuse import Langfuse

langfuse = Langfuse()

def promote_trace_to_dataset(
    trace_id: str,
    observation_id: str,
    dataset_name: str,
    expected_output: str,
):
    observation = langfuse.fetch_observation(observation_id)
    langfuse.create_dataset_item(
        dataset_name=dataset_name,
        input=observation.input,
        expected_output=expected_output,
        source_trace_id=trace_id,
    )
