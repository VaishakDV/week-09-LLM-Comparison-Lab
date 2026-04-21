import time


class Comparator:
    def __init__(self, model_a, model_b):
        self.model_a = model_a
        self.model_b = model_b

    def compare(self, prompt):
        print(f"\nPrompt: {prompt}")
        print("="*60)

        print(f"\n--- {self.model_a.get_name()} ---")
        start = time.time()
        response_a = self.model_a.generate(prompt)
        time_a = time.time() - start
        print(f"Response: {response_a}")
        print(f"Time: {time_a:.2f}s")

        print(f"\n--- {self.model_b.get_name()} ---")
        start = time.time()
        response_b = self.model_b.generate(prompt)
        time_b = time.time() - start
        print(f"Response: {response_b}")
        print(f"Time: {time_b:.2f}s")

        print("\n--- COMPARISON ---")
        print(f"{self.model_a.get_name()}: {time_a:.2f}s")
        print(f"{self.model_b.get_name()}: {time_b:.2f}s")

        if time_a < time_b:
            print(f"{self.model_a.get_name()} was faster")
        else:
            print(f"{self.model_b.get_name()} was faster")

        return {
            "prompt": prompt,
            "response_a": response_a,
            "response_b": response_b,
            "time_a": time_a,
            "time_b": time_b
        }