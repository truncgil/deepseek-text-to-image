from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline
import base64
from io import BytesIO
from PIL import Image

app = FastAPI()

# Modeli önceden yükle
image_generator = pipeline("text-to-image", model="deepseek-ai/deepseek-moe-16b-base")

class GenerationRequest(BaseModel):
    prompt: str
    width: int = 512
    height: int = 512
    num_inference_steps: int = 50

@app.post("/generate")
async def generate_image(request: GenerationRequest):
    try:
        # Görsel oluşturma
        result = image_generator(
            request.prompt,
            width=request.width,
            height=request.height,
            num_inference_steps=request.num_inference_steps
        )
        
        # PIL Image'ı base64'e çevir
        buffered = BytesIO()
        result["image"].save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue())
        
        return {
            "image": img_str.decode("utf-8"),
            "metadata": {
                "model": "deepseek-moe-16b-base",
                "resolution": f"{request.width}x{request.height}"
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 