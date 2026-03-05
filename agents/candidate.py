from autogen_agentchat.agents import UserProxyAgent
from models.model_client import get_model
model_client=get_model()
def get_candidate(job_position):
    return UserProxyAgent(
        name="Candidate",
        input_func=input,
        description=f""" 
You are a candidate interviewing for a {job_position} position."""
    )