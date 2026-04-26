import os
from langfuse import Langfuse
from langfuse.decorators import observe, langfuse_context

langfuse = Langfuse(
    secret_key=os.environ["LANGFUSE_SECRET_KEY"],
    public_key=os.environ["LANGFUSE_PUBLIC_KEY"],
    host=os.environ.get("LANGFUSE_HOST", "https://cloud.langfuse.com"),
)

@observe()
def execute_tool(step):
    langfuse_context.update_current_observation(
        name=f"tool.{step.tool_name}",
        input=step.args,
        metadata={"tool_version": step.tool_version},
    )
    result = step.run()
    langfuse_context.update_current_observation(output=result)
    return result

@observe()
def agent_turn(user_input: str, user_id: str, session_id: str):
    langfuse_context.update_current_trace(user_id=user_id, session_id=session_id)
    plan = make_plan(user_input)
    tool_results = [execute_tool(step) for step in plan.steps]
    response = synthesize_response(plan, tool_results)
    return response

def shutdown():
    langfuse.flush()  # required for serverless / short-lived workers
