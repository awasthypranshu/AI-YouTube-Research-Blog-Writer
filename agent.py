import os
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from crewai import Agent
from tools import yt_tool

blog_research = Agent(
    role="Blog Research Agent",
    goal="get the relevant video transcription for the topic {topic} from the provided Yt channel",
    backstory="Expert in understanding videos in AI Data Science , MAchine Learning And GEN AI and providing suggestion",
    verbose=True,
    allow_delegation=True,
    memory=True,
    tools=[yt_tool],
    llm=ChatGroq(model_name="qwen/qwen3.6-27b", api_key=os.getenv("GROQ_API_KEY"))
)

blog_writer = Agent(
    role = 'Blog Writer Agent',
    goal = 'Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=False,
    llm=ChatGroq(model_name="qwen/qwen3.6-27b", api_key=os.getenv("GROQ_API_KEY"))
)