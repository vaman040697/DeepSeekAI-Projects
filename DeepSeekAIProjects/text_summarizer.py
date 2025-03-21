import requests
import gradio as gr

OLLAMA_URL = "http://localhost:11434/api/generate"

def summarize_text(text):
    """

    Uses DeepSeek AI to summarize a given text
    """
    payload = {
        "model": "deepseek-r1",
        "prompt": f"Summarize the following text:\n\n{text}",
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "no summary generated.")
    else:
        return f"Error: {response.text}"


# create a gradio interface
interface = gr.Interface(
    fn = summarize_text,
    inputs = gr.Textbox(lines=10, placeholder="Enter text to summarize"),
    outputs = gr.Textbox(label="Summarized Text"),
    title = "AI-Powered Text Summarizer",
    description = "Enter a long text and DeepDeek AI will generate a concise summary"
)

#launch the web app
if __name__ == "__main__":
    interface.launch()

# Test Summarization
# if __name__ == "__main__":
#     sample_text = """
#     The Evolution of Artificial Intelligence
#     Artificial Intelligence (AI) has transformed from a theoretical concept into a powerful force shaping modern technology. From early rule-based systems to advanced deep learning models, AI has demonstrated remarkable capabilities across various domains.
#     In recent years, breakthroughs in natural language processing (NLP) and computer vision have enabled AI to interact with humans more naturally and perceive the world with greater accuracy. Models like GPT and DALL·E generate human-like text and images, pushing the boundaries of creativity and automation. Meanwhile, reinforcement learning has allowed AI to master complex tasks, such as playing chess, controlling robots, and optimizing logistics.
#     However, AI also presents ethical challenges. Bias in training data, privacy concerns, and the impact on employment are critical issues that researchers and policymakers must address. As AI continues to evolve, ensuring its responsible development will be essential for harnessing its potential while mitigating risks.
#     Looking ahead, AI is expected to revolutionize fields like healthcare, quantum computing, and neuroscience. With the advent of AGI (Artificial General Intelligence) on the horizon, the future of AI promises both exciting advancements and significant responsibilities.
#         """
#     print("### Summary ###")
#     print(summarize_text(sample_text))