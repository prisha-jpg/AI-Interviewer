# AI-Interviewer

A multi-agent AI interview simulator built with [AutoGen](https://github.com/microsoft/autogen). It conducts realistic mock interviews for any job position using three collaborating AI agents — an **Interviewer**, a **Candidate** (you), and a **Career Coach** — powered by Google's Gemini 2.0 Flash model.

## Features

- **Interactive mock interviews** — practice for any job role by simply entering the position title.
- **Three-agent round-robin system** — the Interviewer asks questions, you (the Candidate) respond, and the Career Coach provides real-time feedback.
- **Automatic evaluation** — receive a hire/don't-hire recommendation and a score out of 10 at the end.
- **Career coaching** — get a summary of your strengths and areas for improvement after the interview.
- **Powered by Gemini 2.0 Flash** — uses Google's Generative AI via the OpenAI-compatible API.

## Architecture

```
main.py                  # Entry point — prompts for job position & runs the interview
agents/
  interviewer.py         # Interviewer agent — asks targeted questions
  candidate.py           # Candidate agent — proxies your terminal input
  careercoach.py         # Career Coach agent — provides feedback & evaluation
models/
  model_client.py        # Configures the Gemini 2.0 Flash model client
teams/
  myteam.py              # Assembles agents into a RoundRobinGroupChat team
config/
  constant.py            # Constants (reserved for future use)
utils/                   # Utilities (reserved for future use)
```

### How It Works

1. You enter a job position (e.g. "Backend Engineer").
2. A **RoundRobinGroupChat** team is created with three participants:
   - **Interviewer** — an `AssistantAgent` that asks technical, problem-solving, and cultural-fit questions.
   - **Candidate** — a `UserProxyAgent` that forwards your terminal input as responses.
   - **Career Coach** — an `AssistantAgent` that silently observes and provides coaching feedback.
3. The agents take turns in round-robin order for up to 15 turns (or until the Interviewer says "TERMINATE").
4. At the end, the Interviewer gives a **HIRE / DON'T HIRE** recommendation with a score, and the Career Coach summarises your performance.

## Prerequisites

- **Python 3.10+**
- A **Google Gemini API key** ([get one here](https://aistudio.google.com/apikey))

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/AI-Interviewer.git
   cd AI-Interviewer
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS / Linux
   # venv\Scripts\activate    # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install autogen-agentchat autogen-ext[openai] python-dotenv
   ```

4. **Set up your API key**

   Create a `.env` file in the project root:

   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

## Usage

```bash
python main.py
```

You'll be prompted to enter the job position, then the interview begins in your terminal. Answer each question as the Candidate — the Interviewer and Career Coach will handle the rest.

### Example

```
Enter the job position you are interviewing for: Backend Engineer

---------- Interviewer ----------
Question 1: Can you walk me through how you would design a RESTful API
for a simple e-commerce application?

---------- Candidate ----------
> I would start by identifying the core resources...

---------- career_coach ----------
Good start! Consider also mentioning authentication and pagination...
```

## Configuration

| Setting | Location | Default |
|---|---|---|
| AI Model | [models/model_client.py](models/model_client.py) | `gemini-2.0-flash` |
| Max turns | [teams/myteam.py](teams/myteam.py) | `15` |
| Termination keyword | [teams/myteam.py](teams/myteam.py) | `TERMINATE` |
| Number of questions | [agents/interviewer.py](agents/interviewer.py) | `1` |

To increase the number of interview questions, update the interviewer's system prompt in [agents/interviewer.py](agents/interviewer.py) and adjust `max_turns` in [teams/myteam.py](teams/myteam.py) accordingly.

## License

This project is open-source. Feel free to use and modify it as you see fit.