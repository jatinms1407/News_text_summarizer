from google import genai


class TextSummarizer:
    """
    Text Summarizer using Gemini LLM API.
    """

    def __init__(self, model_name="models/gemini-flash-latest"):
        self.model_name = model_name

        # 👇 Put your key directly here for now
        API_KEY = "AIzaSyAsNmeDjDRpG04jqZeb8ZsnYSrx4CvOOV0"

        self.client = genai.Client(api_key=API_KEY)

    def preprocess(self, text: str) -> str:
        text = text.replace("\n", " ").strip()
        return text

    def summarize(self, text: str) -> str:
        text = self.preprocess(text)

        if len(text.split()) < 30:
            return "Text is too short to summarize."

        prompt = f"""
        You are a professional news editor.
        Summarize the following news article clearly and concisely:

        {text}
        """

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt
        )

        return response.text
