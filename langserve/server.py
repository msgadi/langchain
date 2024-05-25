from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv
from pathlib import Path

# Specify the path to the .env file
dotenv_path = Path('../.env')

load_dotenv(dotenv_path=dotenv_path)

if not os.getenv("OPENAI_API_KEY"):
    os.environ['OPENAI_API_KEY'] = "your_api_key_here"
else:
    os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    decsription="A simple API Server"

)

model = ChatOpenAI()
prompt=ChatPromptTemplate.from_template("provide me an essay about {topic}")
prompt1=ChatPromptTemplate.from_template("provide me a poem about {topic}")

add_routes(
    app,
    model,
    path="/openai"
)

add_routes(
    app,
    prompt|model,
    path="/essay"

)

add_routes(
    app,
    prompt1|model,
    path="/poem"

)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)