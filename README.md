# Truncgil DeepSeek Prompt-to-Image Generator

Docker-based image generation application using DeepSeek model

## Features

- 🖼️ Generate images from text prompts
- 🐳 Docker container support
- ⚡ FastAPI-based REST API
- 🌍 Simple web interface
- 🔧 Customizable parameters (resolution, inference steps)

## Installation

### Quick Start with Docker

1. Clone the repository:
```bash
git clone https://github.com/truncgil/deepseek-text-to-image.git
cd deepseek-image-generator
```

2. Build Docker container:
```bash
docker build -t deepseek-image-generator .
```

3. Start container:
```bash
docker run -p 8000:8000 deepseek-image-generator
```

### Manual Setup
```bash
python -m venv venv
source venv/bin/activate # Linux/MacOS
venv\Scripts\activate # Windows
pip install -r requirements.txt
uvicorn app.api:app --reload
```

4. Test API:
```bash
curl -X POST "http://localhost:8000/generate" \
-H "Content-Type: application/json" \
-d '{"prompt": "futuristic cityscape at sunset"}'
```

**Parameters:**
- `prompt` (required): Image description
- `width` (default 512): Image width
- `height` (default 512): Image height
- `num_inference_steps` (default 50): Number of inference steps for generation quality

## Frontend Usage

1. Open `frontend/index.html` in browser while API is running
2. Enter your description in the text box
3. Click "Generate" button

## Configuration

### Environment Variables
Configure via `.env` file:
```env
MODEL_NAME=deepseek-ai/deepseek-moe-16b-base
DEFAULT_WIDTH=512
DEFAULT_HEIGHT=512
```

### Model Settings
Modify parameters in `app/api.py`:
```python
image_generator = pipeline(
    "text-to-image",
    model=os.getenv("MODEL_NAME"),
    torch_dtype=torch.float16,
    device_map="auto"  # For GPU usage
)
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss.

## License
MIT License

---

**Important Notes:**
- Model files will be downloaded on first run (≈5-10GB)
- NVIDIA Container Toolkit required for GPU usage
- Remember to add CORS and rate limiting for production