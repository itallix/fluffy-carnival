from pyovms import Tensor
from optimum.intel import OVModelForSequenceClassification
from transformers import AutoTokenizer, pipeline
import json

class OvmsPythonModel:
    def initialize(self, kwargs: dict):
        model_id = "cardiffnlp/twitter-roberta-base-sentiment"

        self.model = OVModelForSequenceClassification.from_pretrained(model_id)
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        
        self.pipe = pipeline(
            "sentiment-analysis",
            model=self.model,
            tokenizer=self.tokenizer
        )
        return True

    def execute(self, inputs: list):
        text = bytes(inputs[0]).decode()
        results = self.pipe(text)

        output = {
            "label": results[0]["label"],
            "score": float(results[0]["score"])
        }
        
        return [Tensor("sentiment", json.dumps(output).encode())]
