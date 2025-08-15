"""
Level 4 & Level 5 Agno Multi-Agent Content Creation
===================================================

This example runs both:
- Level 4: Stateless coordinated team of agents
- Level 5: Stateful workflow with explicit tasks
And compares their outputs side-by-side in Markdown.
"""

from agno.agent import Agent
from agno.team import Team
from agno.models.mistral import MistralChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.reasoning import ReasoningTools
from agno.tools.file import FileTools
from agno.tools.python import PythonTools
from agno.workflow import Workflow
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
import os

# ===== Load env variables =====
load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# ===== Define Agents =====
research_agent = Agent(
    name="Research Agent",
    role="Conduct thorough research on given topics using web search",
    model=MistralChat(id="open-mistral-nemo", api_key=MISTRAL_API_KEY),
    tools=[DuckDuckGoTools(), ReasoningTools()],
    instructions=[
        "Gather comprehensive information from multiple recent and credible sources",
        "Include source URLs in APA format",
        "Organize findings in a clear, structured format",
        "Focus on key trends, facts, and insights"
    ],
    show_tool_calls=True,
    markdown=True,
)

writing_agent = Agent(
    name="Writing Agent", 
    role="Create engaging, well-structured content based on research findings",
    model=MistralChat(id="open-mistral-nemo", api_key=MISTRAL_API_KEY),
    tools=[ReasoningTools(), FileTools(), PythonTools()],
    show_tool_calls=True,
    markdown=True,
)

editor_agent = Agent(
    name="Editor Agent",
    role="Review and improve content for quality, accuracy, and engagement",
    model=MistralChat(id="open-mistral-nemo", api_key=MISTRAL_API_KEY),
    tools=[ReasoningTools(), FileTools(), PythonTools()],
    instructions=[
        "Review for clarity, grammar, and logical flow",
        "Ensure all claims are supported",
        "Make it engaging for the target audience",
        "Return ONLY the polished text, no explanations"
    ],
    show_tool_calls=True,
    markdown=True,
)

# ===== Level 4: Coordinated Team =====
content_creation_team = Team(
    name="Content Creation Team",
    mode="coordinate",
    members=[research_agent, writing_agent, editor_agent],
    model=MistralChat(id="open-mistral-nemo", api_key=MISTRAL_API_KEY),
    success_criteria=[
        "Comprehensive, credible research",
        "Well-structured and engaging content",
        "Reviewed for accuracy and readability"
    ],
    instructions=[
        "Work as a team to produce high-quality content ready for publication"
    ],
    show_tool_calls=True,
    markdown=True,
)

def run_level4(topic: str, target_audience: str, content_type: str) -> str:
    prompt = f"""
    Create a comprehensive {content_type} on: "{topic}"
    Target audience: {target_audience}

    Process:
    1. Research thoroughly using credible sources
    2. Write engaging, well-structured content
    3. Review and refine for quality and accuracy

    Return the final, publication-ready version with citations.
    """
    result = content_creation_team.run(prompt)
    return result.content

# ===== Level 5: Stateful Workflow =====
class ContentWorkflow(Workflow):
    def __init__(self):
        super().__init__()
        self.research_findings = None
        self.draft_content = None
        self.final_content = None

    def research_task(self, topic: str) -> str:
        result = research_agent.run(
            f"You are an expert researcher. Find the 5 most important facts about {topic}, "
            f"with credible sources (APA format). Output only the findings."
        )
        self.research_findings = result.content
        return result.content

    def writing_task(self, research_data: str, content_type: str) -> str:
        result = writing_agent.run(
            f"You are a professional {content_type} writer. Using this research:\n\n"
            f"{research_data}\n\n"
            f"Write a {content_type} (600-800 words) with a catchy title, engaging intro, "
            f"clear subheadings, and strong conclusion. Do NOT explain the process."
        )
        self.draft_content = result.content
        return result.content

    def editing_task(self, draft: str) -> str:
        result = editor_agent.run(
            f"You are a senior editor. Polish this:\n\n{draft}\n\n"
            f"Ensure clarity, flow, grammar, and engagement. Return ONLY the polished text."
        )
        self.final_content = result.content
        return result.content

    def run_workflow(self, topic: str, content_type: str) -> str:
        research = self.research_task(topic)
        draft = self.writing_task(research, content_type)
        final = self.editing_task(draft)
        return final

# ===== Run both and compare =====
if __name__ == "__main__":
    topic = "The Future of Artificial Intelligence in Healthcare"
    content_type = "technical report"
    target_audience = "healthcare professionals"

    # Run Level 4
    level4_result = run_level4(topic, target_audience, content_type)

    # Run Level 5
    workflow = ContentWorkflow()
    level5_result = workflow.run_workflow(topic, content_type)

    # Show side-by-side in Markdown
    console = Console()
    console.rule("[bold green]📊 Level 4 vs Level 5 Comparison")
    console.print(Markdown("## 📝 Level 4 Result\n" + level4_result))
    console.rule("[bold blue]⬇⬇⬇")
    console.print(Markdown("## 📝 Level 5 Result\n" + level5_result))