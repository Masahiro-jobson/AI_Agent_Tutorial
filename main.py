from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from pydantic import BaseModel

# load LLM API keys from .env file
load_dotenv()

# llm variable contains the LLM model to use for the agent.
llm = ChatOpenAI(model="gpt-3.5-turbo")
llm2 = ChatAnthropic(model="claude-3-opus-20241022")
