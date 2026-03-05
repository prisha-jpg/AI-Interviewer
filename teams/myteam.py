from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
def get_interview_team(job_position):
    from agents.candidate import get_candidate
    from agents.interviewer import get_interviewer
    from agents.careercoach import get_career_coach
    from models.model_client import get_model

    candidate = get_candidate(job_position)
    model_client = get_model()
    interviewer = get_interviewer(model_client, job_position)
    career_coach = get_career_coach(job_position)
    termination=TextMentionTermination(text="TERMINATE")
    team = RoundRobinGroupChat(
        participants=[interviewer, candidate, career_coach],
        max_turns=15,
        name="Interview Team",
        termination_condition=termination,
        )
    return team