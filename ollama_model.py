import ollama


class OllamaModel:
    def __init__(self, model_name="llama3.2"):
        self.model_name = model_name

    def generate(self, prompt, max_tokens=500):
        response = ollama.chat(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}],
            options={"num_predict": max_tokens}
        )
        return response["message"]["content"]

    def get_name(self):
        return f"Llama 3.2 (local)"