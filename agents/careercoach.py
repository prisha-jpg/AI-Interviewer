from autogen_agentchat.agents import AssistantAgent
from models.model_client import get_model
model_client=get_model()
def get_career_coach(job_position):
    return AssistantAgent(
        name="career_coach",
        model_client=model_client,
        description=f""" An AI career coach that provides personalized advice and guidance to individuals seeking to advance their careers.""",
        system_message=f""" 
You are a Professional Career Coach for {job_position} position.
Provide constructive feedback and actionable suggestions to help the candidate improve their interview skills and overall career prospects.
After the interview , summarise the candidate's strengths and areas for improvement in brief pointers.
After the final question , analyse the candidate's performance in all the questions asked by the interviewer and  make a decision whether is suitable for the {job_position} position or not.

"""
    )