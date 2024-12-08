from transformers import AutoModelForSequenceClassification, AutoTokenizer
from optimum.intel import OVModelForSequenceClassification
import os

MODEL_DIR = "models/emotion-classifier/1"
os.makedirs(MODEL_DIR, exist_ok=True)

# Загружаем модель
model_id = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)

# Конвертируем в OpenVINO
ov_model = OVModelForSequenceClassification.from_pretrained(
    model_id,
    export=True,
    compile=False
)

ov_model.save_pretrained(MODEL_DIR)
tokenizer.save_pretrained(MODEL_DIR)
