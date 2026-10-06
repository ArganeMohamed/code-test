from app.llm import create_llm


class ChatService:
    def __init__(self):
        self.llm = create_llm()

    def ask(self, message: str) -> str:
        prompt = (
            "You are a helpful assistant.\n"
            f"User question: {message}"
        )

        response = self.llm.invoke(prompt)

        return str(response.content)