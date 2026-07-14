import os

from openai import OpenAI


def run_smoke_test(*, base_url: str, virtual_key: str) -> str | None:
    client = OpenAI(base_url=base_url, api_key=virtual_key)
    response = client.chat.completions.create(
        model="claude-sonnet",
        messages=[{"role": "user", "content": "What is 2+2? Reply with one word."}],
        extra_body={
            "metadata": {"generation_name": "smoke-test"},
            "user": "feature=test",
        },
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    print(
        run_smoke_test(
            base_url=os.environ.get("LITELLM_BASE_URL", "http://127.0.0.1:4000/v1"),
            virtual_key=os.environ["LITELLM_VIRTUAL_KEY"],
        )
    )
