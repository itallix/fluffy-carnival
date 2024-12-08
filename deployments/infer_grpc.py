import numpy as np
from ovmsclient import make_grpc_client
from scipy.special import softmax
from transformers import AutoTokenizer

port = 51473
address = "localhost:" + str(port)
model_name = "emotion_classifier"

# Bind the grpc address to the client object
client = make_grpc_client(address)
model_status = client.get_model_status(model_name=model_name)
print(model_status)
model_metadata = client.get_model_metadata(model_name=model_name)
print(model_metadata)

model_id = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_id)

text = "What a wonderful day!"
tokenized_input = tokenizer(
    text,
    padding=True,
    truncation=True,
    return_tensors="np"
)
print(tokenized_input)
input_ids = tokenized_input["input_ids"].astype(np.int64)
attention_mask = tokenized_input["attention_mask"].astype(np.int64)
inputs = {
    "input_ids": input_ids,
    "attention_mask": attention_mask
}
# inputs = {"text_input": ["What a wonderful day!"]}
logits = client.predict(inputs=inputs, model_name=model_name)

probabilities = softmax(np.array(logits))
print(probabilities)
