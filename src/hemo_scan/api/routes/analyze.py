from fastapi import APIRouter, File, HTTPException, UploadFile
from pydantic import ValidationError

from hemo_scan.api.schemas.analysis import Analysis
from hemo_scan.services import llm

router = APIRouter()


@router.post("/analyze")
async def analyze(image: UploadFile = File(...)) -> Analysis:
    mime = image.content_type or ""
    if not mime.startswith("image/"):
        raise HTTPException(415, "Envie uma imagem")

    try:
        return llm.analyze(await image.read(), mime)
    except ValidationError as err:
        raise HTTPException(502, "Resposta invalida do modelo") from err
