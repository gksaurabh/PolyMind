import os
import sys

from agno.team import Team
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.reasoning import ReasoningTools

# Add the project root to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))

from src.prompts.agent_prompts import AgentPrompts
from src.agents.forecaster.forecaster_agent import ForecasterAgent
from src.agents.historian.historian_agent import HistorianAgent 
from src.agents.optimist.optimist_agent import OptimistAgent
from src.agents.pessimist.pessimist_agent import PessimistAgent


class JudgeTeam():
    def __init__(self):
        optimist_agent = OptimistAgent()
        pessimist_agent = PessimistAgent()
        historian_agent = HistorianAgent()
        forecaster_agent = ForecasterAgent()
        self.team = Team(
            name="Judge Team",
            members=[optimist_agent.agent, pessimist_agent.agent, historian_agent.agent, forecaster_agent.agent],
            model=OpenAIChat(id="gpt-4o"),
            instructions=AgentPrompts.JUDGE_INSTRUCTIONS,
            tools=[ReasoningTools(add_instructions=True), DuckDuckGoTools()],
            reasoning=True,
            show_members_responses=True,
            share_member_interactions=True,
            delegate_task_to_all_members=True,
            get_member_information_tool=True,
            stream_intermediate_steps=True,
            store_member_responses=True,
            markdown=True
        )
    
    def run(self, topic: str, stream: bool = False):
        return self.team.run(f"Based on the reports from all agents, provide a comprehensive and balanced final assessment on the topic: {topic}", stream=stream)
    
if __name__ == "__main__":
    judge_team = JudgeTeam()
    try:
        # response = judge_team.run("The future of renewable energy", stream=False)
        # if response is not None:
        #     # Access the content attribute from the RunOutput object
        #     print(getattr(response, 'content', str(response)))
        
        judge_team.team.print_response("Will companies be open to using AI to prevent accidents in construction sites?", stream=True)

    except Exception as e:
        print(f"Error occurred in JudgeTeam: {e}")