from typing import Literal
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
## from dotenv import load_dotenv

## load_dotenv()

class RouteQuery(BaseModel):
    """Route a user query to the most relevant datasource."""

    datasource: Literal["vectorstore", "websearch"] = Field(
        ...,
        description="Given a user question choose to route it to web search or a vectorstore.",
    )


llm = ChatOpenAI(temperature=0)
structured_llm_router = llm.with_structured_output(RouteQuery)

system = """You are an expert at routing a user question to a vectorstore or web search.
The vectorstore contains documents with detailed dream interpretations, symbolic meanings, and insights into subconscious thoughts.
Use the vectorstore for questions on these topics. For all else, use web-search."""
route_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)

question_router = route_prompt | structured_llm_router




#if __name__ == '__main__':
#    print(question_router.invoke(
#        {"question":"rüyada ağlamak ne anlama gelir?"}
#    ))

#   print(question_router.invoke(
#        {"question":"tarja turen mi şebnem ferah mı :D "}
#    ))