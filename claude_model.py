import anthropic
import os
from dotenv import load_dotenv

load_dotenv()


class ClaudeModel:
    def __init__(self):
        self.client = anthropic.Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )
        self.model = "claude-haiku-4-5-20251001"

    def generate(self, prompt, max_tokens=500):
        response = self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.content[0].text

    def get_name(self):
        return "Claude Haiku"