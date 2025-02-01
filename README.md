# Deepseek Prompt-to-Image Generator

Docker tabanlı, Deepseek modelini kullanan metinden görsel oluşturma uygulaması

## Özellikler

- 🖼️ Metin prompt'undan görsel oluşturma
- 🐳 Docker container desteği
- ⚡ FastAPI tabanlı REST API
- 🌍 Basit web arayüzü
- 🔧 Özelleştirilebilir parametreler (çözünürlük, inference adımları)

## Kurulum

### Docker ile Hızlı Başlangıç

1. Repository'yi klonlayın:
```bash
git clone https://github.com/sizin-repo-adresiniz.git
cd deepseek-image-generator
```
2. Docker container oluşturun:
```bash
docker build -t deepseek-image-generator .
```
3. Container'ı başlatın:
```bash
docker run -p 8000:8000 deepseek-image-generator
bash
python -m venv venv
source venv/bin/activate # Linux/MacOS
venv\Scripts\activate # Windows
pip install -r requirements.txt
uvicorn app.api:app --reload
```
4. API'yi test edin:
```bash
curl -X POST "http://localhost:8000/generate" \
-H "Content-Type: application/json" \
-d '{"prompt": "futuristic cityscape at sunset"}'
```

**Parametreler:**
- `prompt` (zorunlu): Görsel açıklaması
- `width` (varsayılan 512): Görsel genişliği
- `height` (varsayılan 512): Görsel yüksekliği
- `num_inference_steps` (varsayılan 50): Üretim kalitesi için inference adım sayısı

## Frontend Kullanımı

1. API çalışırken `frontend/index.html` dosyasını tarayıcıda açın
2. Metin kutusuna istediğiniz açıklamayı yazın
3. "Generate" düğmesine tıklayın

## Yapılandırma

### Ortam Değişkenleri
`.env` dosyası üzerinden ayarlanabilir:
```env
MODEL_NAME=deepseek-ai/deepseek-moe-16b-base
DEFAULT_WIDTH=512
DEFAULT_HEIGHT=512
```

### Model Ayarları
`app/api.py` dosyasında aşağıdaki parametreleri değiştirebilirsiniz:
```python
image_generator = pipeline(
    "text-to-image",
    model=os.getenv("MODEL_NAME"),
    torch_dtype=torch.float16,
    device_map="auto"  # GPU kullanımı için
)
```

## Katkıda Bulunma
Pull request'ler memnuniyetle karşılanır. Büyük değişiklikler için önce konuyu tartışmak için bir issue açın.

## Lisans
MIT Lisansı - Detaylar için [LICENSE](LICENSE) dosyasına bakın

---

**Önemli Notlar:**
- İlk çalıştırmada model dosyaları indirilecektir (≈5-10GB)
- GPU kullanımı için NVIDIA Container Toolkit kurulu olmalıdır
- Üretim ortamında CORS ve rate limiting eklemeyi unutmayın