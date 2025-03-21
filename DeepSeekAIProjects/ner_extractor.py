import requests
import gradio as gr
OLLAMA_URL = "http://localhost:11434/api/generate"

def extract_named_entities(text):
    """

    Uses DeepSeek AI to summarize a given text
    """

    prompt = f"Extract all named entities (persons, organizations, locations, dates) from the following text:\n\n{text}"

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

#Test Named Entity Recognition
# if __name__ == "__main__":
#     sample_text = "Google was founded by Larry Page and Sergy Brin in September 1998 in at Stanford."
#     print("### Extracted Entities ###")
#     print(extract_named_entities(sample_text))


# Create Gradio Interface
interface = gr.Interface(
    fn = extract_named_entities,
    inputs=gr.Textbox(lines=5, placeholder="Enter text for entity recognition"),
    outputs=gr.Textbox(label="Extracted Entities"),
    title="AI-Powered Named Entity Recognition (NER)",
    description="Enter paragraph and DeepSeek AI will extract persons, organizations, locations, and dates"
)

#launching the web app
if __name__ == "__main__":
    interface.launch()