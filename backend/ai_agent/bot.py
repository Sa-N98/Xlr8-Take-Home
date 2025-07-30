import json
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from dotenv import load_dotenv
import os


load_dotenv()

# --- LLM Setup (OpenRouter-compatible with streaming output) ---
llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL"),
    model="moonshotai/kimi-k2:free",
    streaming=True,
    callbacks=[]
)


def ai_call(report_template, variables):
    prompt_template = PromptTemplate(
        template=report_template,
        input_variables=list(variables.keys())
    )
    chain = prompt_template | llm
    full_response = ""
    for chunk in chain.stream(variables):
        print(chunk.content, end="", flush=True)
        full_response += chunk.content
    output = full_response.replace('```json', '').replace('```', '')
    return json.loads(output) if output else None