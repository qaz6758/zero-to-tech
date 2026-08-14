from pypinyin import lazy_pinyin, Style

def to_pinyin(text: str):

    return " ".join(
        lazy_pinyin(
            text,
            style=Style.TONE
        )
    )