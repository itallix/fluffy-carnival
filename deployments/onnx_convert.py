from transformers import AutoModelForSequenceClassification, AutoTokenizer
from optimum.exporters.onnx import export
from optimum.exporters import TasksManager
from pathlib import Path

model_id = "cardiffnlp/twitter-roberta-base-sentiment"
onnx_output_path = Path("models/emotion-classifier/1/model.onnx")

model = AutoModelForSequenceClassification.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)

onnx_config_constructor = TasksManager.get_exporter_config_constructor(
    model=model,
    exporter="onnx",
    task="text-classification",
    library_name="transformers"
)
onnx_config = onnx_config_constructor(model.config)

dummy_text = ["This is a test sentence."]
encoded_inputs = tokenizer(dummy_text, padding="max_length", max_length=128, truncation=True, return_tensors="pt")
reference_model_inputs = {k: v for k, v in encoded_inputs.items()}

onnx_inputs = onnx_config.generate_dummy_inputs_for_validation(reference_model_inputs)

export(
    model=model,
    config=onnx_config,
    opset=14,  # ONNX opset version
    output=onnx_output_path
)

tokenizer.save_pretrained(onnx_output_path.parent)

print(f"ONNX model has been saved to: {onnx_output_path}")
