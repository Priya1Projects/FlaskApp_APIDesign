from dataclasses import dataclass
from openai import OpenAI

@dataclass
class SummarizeResult:
    original_text: str
    summary: str

class SummarizerService:
    def __init__(self, client: OpenAI):
        self.client = client

    def summarize_text(self,text: str, max_length: int = 350) -> SummarizeResult:
        # Placeholder for actual summarization logic
    summary = self.client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": text
            }
        ]
    )
    return SummarizeResult(original_text=text, summary=summary)