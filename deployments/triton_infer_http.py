import numpy as np
import tritonclient.http as httpclient
from transformers import AutoTokenizer

# Port should be replaced with the port returned by minikube service
client = httpclient.InferenceServerClient(url='localhost:49316')
print(client.is_server_ready())
print(client.get_model_repository_index())
print(client.get_model_metadata(model_name="emotion-classifier"))

tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
text = "I love this product, it's amazing!"
inputs = tokenizer(text, padding=True, truncation=True, max_length=128, return_tensors="np")

input_ids = httpclient.InferInput("input_ids", inputs["input_ids"].shape, "INT64")
attention_mask = httpclient.InferInput("attention_mask", inputs["attention_mask"].shape, "INT64")

input_ids.set_data_from_numpy(inputs["input_ids"])
attention_mask.set_data_from_numpy(inputs["attention_mask"])

output = httpclient.InferRequestedOutput("logits")

response = client.infer(
    model_name="emotion-classifier",
    inputs=[input_ids, attention_mask],
    outputs=[output]
)

result = response.as_numpy("logits")
print(result)

probabilities = np.exp(result) / np.sum(np.exp(result), axis=1, keepdims=True)
predicted_class = np.argmax(probabilities)

labels = ["negative", "neutral", "positive"]
print(f"Predicted sentiment: {labels[predicted_class]}")
print(f"Probabilities: {dict(zip(labels, probabilities[0]))}")
