
from openai import OpenAI
from app.services.summarizer import SummarizerService, SummarizeResult

def init_extensions(app):
    client = OpenAI(api_key=app.config['API_SECRET_KEY'])
    app.extensions['summarizer'] = SummarizerService(client)