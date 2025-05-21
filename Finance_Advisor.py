import groq
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

client = groq.Client(api_key=api_key)


web_search_agent=Agent(
    name="Web Search Agnet",
    role="Search the web for the information",
    model=Groq(id="Llama-3.3-70b-Specdec"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,

)

finance_agent=Agent(
    nme="Finance Agent",
    model=Groq(id="Llama-3.3-70b-Specdec"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)
        ],
    instructions=["Use table to display data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent=Agent(
    team=[web_search_agent,finance_agent],
    model=Groq(id="Llama-3.3-70b-Specdec"),
    instructions=["Always include sources","Use table to display data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for OGDCL",stream=True)