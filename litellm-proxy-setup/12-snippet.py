# pip install "openai>=1.55,<2"
from openai import OpenAI

client = OpenAI(
    base_url="http://litellm-proxy:4000/v1",
    api_key="sk-...the-issued-key...",
)

resp = client.chat.completions.create(
    model="claude-sonnet",
    messages=[{"role": "user", "content": "What's 2+2? One word."}],
    extra_body={
        "metadata": {"generation_name": "smoke-test"},
        "user": "feature=test",
    },
)
print(resp.choices[0].message.content)
