from crewai_tools import YoutubeChannelSearchTool

yt_tool = YoutubeChannelSearchTool(
    youtube_channel_handle="@krishnaik06",
    config={
        "llm": {
            "provider": "groq",
            "config": {
                "model": "qwen/qwen3.6-27b",
            },
        },
        "embedder": {
            "provider": "huggingface",
            "config": {
                "model": "sentence-transformers/all-MiniLM-L6-v2",
            },
        },
    },
)