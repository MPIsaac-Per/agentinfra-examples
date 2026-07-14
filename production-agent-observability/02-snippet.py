"""Langfuse v4 tracing with injected planning and synthesis functions."""

from __future__ import annotations

from collections.abc import Callable
from typing import Any, Protocol

from langfuse import get_client, observe, propagate_attributes


class ToolStep(Protocol):
    tool_name: str
    tool_version: str
    args: Any

    def run(self) -> Any: ...


class Plan(Protocol):
    steps: list[ToolStep]


@observe(name="execute_tool", as_type="tool", capture_input=False)
def execute_tool(step: ToolStep) -> Any:
    client = get_client()
    client.update_current_span(
        name=f"tool.{step.tool_name}",
        input=step.args,
        metadata={"tool_version": step.tool_version},
    )
    try:
        result = step.run()
    except Exception as exc:
        client.update_current_span(
            level="ERROR",
            status_message=type(exc).__name__,
            output={"error_type": type(exc).__name__},
        )
        raise
    client.update_current_span(output=result)
    return result


@observe(name="agent.turn", as_type="agent")
def _observed_agent_turn(
    user_input: str,
    *,
    make_plan: Callable[[str], Plan],
    synthesize_response: Callable[[Plan, list[Any]], str],
) -> str:
    plan = make_plan(user_input)
    tool_results = [execute_tool(step) for step in plan.steps]
    return synthesize_response(plan, tool_results)


def agent_turn(
    user_input: str,
    *,
    user_id: str,
    session_id: str,
    make_plan: Callable[[str], Plan],
    synthesize_response: Callable[[Plan, list[Any]], str],
) -> str:
    with propagate_attributes(
        user_id=user_id,
        session_id=session_id,
        trace_name="agent.turn",
    ):
        return _observed_agent_turn(
            user_input,
            make_plan=make_plan,
            synthesize_response=synthesize_response,
        )


def shutdown() -> None:
    get_client().flush()
