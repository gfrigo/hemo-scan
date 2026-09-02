from typing import Literal

from pydantic import BaseModel, Field

Quality = Literal["good", "poor", "unusable"]


class Analysis(BaseModel):
    quality: Quality
    approved: bool = Field(description="True only when quality is 'good'")
    reasons: list[str] = Field(description="Visual findings backing the label")
    confidence: float = Field(ge=0, le=1)
