from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    text: str


class AnalyzeResponse(BaseModel):
    text: str
    emotion: str
    summary: str
    keywords: list[str]
    confidence: float
    pinyin: str