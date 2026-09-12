from crewai import Task
from tools import yt_tool
from agent import blog_research,blog_writer

research_task = Task(
    description="get the relevant video transcription for the topic {topic} from the provided Yt channel",
    expected_output="relevant video transcript",
    tools=[yt_tool],
    agent=blog_research,
    output_file="output/blog.md"
)

write_task = Task(
    description="write a blog post about the topic {topic} from the relevant video transcript",
    expected_output="blog post",
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    output_file="output/blog.md"
)