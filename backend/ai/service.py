import json
import os
from ai.client import client
from ai.prompts import EMOTION_PROMPT


def analyze_text(text: str):

    try:
        response = client.chat.completions.create(
            model=os.getenv("AI_MODEL"),
            messages=[
                {
                    "role": "system",
                    "content": EMOTION_PROMPT
                },
                {
                    "role": "user",
                    "content": text
                }
            ],
            temperature=0.3,
        )

        content = response.choices[0].message.content
    

        return json.loads(content)
    except Exception as e:
        print(f"ai调用失败: {e}")
        raise