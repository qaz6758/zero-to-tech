from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from utils.pinyin import to_pinyin
from ai.service import analyze_text
from ai.schemas import AnalyzeRequest, AnalyzeResponse




app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)



profile = {
    "heroTitle": "关于我",
    "heroSubtitle": "项目，创意，灵感，心得，我的作品",
    "featuredWork": {
        "kicker": "作品",
        "title": "文字实验室",
        "copy": "拼音和情绪，挖掘中文里的细节",
        "linkLabel": "打开作品",
  },
  "identity": {
    "motto": "已识乾坤大，尤怜草木青",
    "learning": "零到全栈",
  },
}



@app.get("/api/profile")
def read_root():
    return profile



@app.post("/analyze", response_model=AnalyzeResponse)
def analyze_api(req: AnalyzeRequest):
    try:
        result = analyze_text(req.text)
        result["pinyin"] = to_pinyin(req.text)
        result["text"] = req.text

        return result
    except Exception:
        raise HTTPException(
            status_code=503,
            detail="AI 服务暂时不可用"
        )