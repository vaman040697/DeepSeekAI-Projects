import requests
import gradio as gr
OLLAMA_URL = "http://localhost:11434/api/generate"

def analyze_sentiment(text):
    """

    Uses DeepSeek AI to summarize a given text
    """

    prompt = f"Classify the sentiment of the following text as positive, negative, or neutral\n\n{text}"

    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "no entities detected.")
    else:
        return f"Error: {response.text}"

# Create Gradio Interface
interface = gr.Interface(
    fn = analyze_sentiment,
    inputs=gr.Textbox(lines=5, placeholder="Enter a sentence for sentiment analysis"),
    outputs=gr.Textbox(label="Sentiment Result"),
    title="AI-Powered Sentiment Analysis",
    description="Enter a sentence, and DeepSeek will classify its sentiment as Positive, Negative or Neutral"
)

#launching the web app
if __name__ == "__main__":
    interface.launch()

#Test Sentiment Analysis
# if __name__ == "__main__":
#     sample_text = "The Captain America Brave New World movie was fantastic! I enjoyed every minute of it."
#     print("### Sentiment Analysis Result ###")
#     print(analyze_sentiment(sample_text))