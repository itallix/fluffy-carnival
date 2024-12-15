import requests
import json
import click

@click.command()
@click.option(
    '--port',
    default=8080,
    help='Port number for the emotion classifier service (default: 8080)'
)
@click.option(
    '--model',
    default="emotion_classifier",
    help='Requested model name (default: emotion_classifier)'
)
@click.argument('text')
def predict_text(port, model, text):
    url = f"http://localhost:{port}"
    payload = {
        "text": text,
    }

    try:
        response = requests.post(
            f"{url}/v1/models/{model}/infer",
            json=payload
        )
        response.raise_for_status()
        print(response.json())
    except requests.RequestException as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    predict_text()
