import base64
import json

from openai import OpenAI

from hemo_scan.api.schemas.analysis import Analysis
from hemo_scan.core.config import settings


def analyze(image: bytes, mime: str = "image/jpeg") -> Analysis:
    client = OpenAI(base_url=settings.llm_base_url, api_key=settings.llm_api_key)
    prompt = settings.prompt_file.read_text(encoding="utf-8")
    schema = json.dumps(Analysis.model_json_schema(), ensure_ascii=False)

    answer = client.chat.completions.create(
        model=settings.llm_model,
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": f"{prompt}\n\nAnswer in JSON matching this schema:\n{schema}"},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Assess this sample."},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:{mime};base64,{base64.b64encode(image).decode()}"},
                    },
                ],
            },
        ],
    )
    return Analysis.model_validate_json(answer.choices[0].message.content or "")
