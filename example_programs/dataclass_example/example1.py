from dataclasses import asdict, dataclass
@dataclass
class GeminiCallDetails:
    prompt: str
    max_tokens: int
    gemini_id: str
    gemini_api_url: str


def mock_gemini_call(params):
    print("hello world")
    print(params)


inp = GeminiCallDetails(
    prompt="what is Python?",
    max_tokens=1000,
    gemini_id="trdt5667",
    gemini_api_url="https://hello.com"
)


mock_gemini_call(asdict(inp))

print(asdict(inp))
