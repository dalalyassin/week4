from llama_cpp import Llama
from base import LLMProvider


class LocalLlamaProvider(LLMProvider):
    def __init__(self, model_path: str):
        self.llm = Llama(
            model_path=model_path,
            n_ctx=4096,
            temperature=0,
            verbose=False
        )

    def generate(self, prompt: str) -> str:
        output = self.llm(
            prompt,
            max_tokens=512,
        )
        return output["choices"][0]["text"].strip()
