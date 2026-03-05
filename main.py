from teams.myteam import get_interview_team
from autogen_agentchat.ui import Console
import asyncio

async def main():
    job_position = input("Enter the job position you are interviewing for: ")
    team = get_interview_team(job_position)
    return await Console(team.run_stream(task=f"Conduct an interview for the position of {job_position}."))
if __name__ == "__main__":
    asyncio.run(main())