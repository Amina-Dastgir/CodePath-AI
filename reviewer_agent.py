from crewai import Agent, Crew, Process, Task
from tools.learning_tools import OutputValidationTool


def run_reviewer_agent(llm, language, task_type, draft):
    tool = OutputValidationTool()
    validation_report = tool._run(f"LANGUAGE: {language}\nTASK TYPE: {task_type}\n\n{draft}")
    agent = Agent(
        role="Programming Output Quality Reviewer",
        goal="Review the draft for relevance, clarity, structure, and obvious code issues.",
        backstory=(
            "You are a careful reviewer. You distinguish between static checks and actual execution, "
            "avoid claiming that code was run, and preserve useful details while correcting obvious problems."
        ),
        llm=llm,
        tools=[tool],
        allow_delegation=False,
        max_iter=3,
        verbose=False,
    )
    task = Task(
        description=(
            f"Review the following {task_type} output for a learner using {language}.\n\n"
            f"DRAFT:\n{draft}\n\n"
            f"Preliminary tool report (from Output Validation Tool):\n{validation_report}\n\n"
            "Use the attached Output Validation Tool if another check is useful. "
            "Return the polished final deliverable, incorporating important corrections and noting any "
            "remaining limitations. If code is present, preserve it in a fenced code block. "
            "Do not claim that code has been executed. If the tool reports a syntax issue, fix it where possible."
        ),
        expected_output="A polished final answer with corrected content and honest limitations.",
        agent=agent,
    )
    crew = Crew(agents=[agent], tasks=[task], process=Process.sequential, verbose=False)
    return str(crew.kickoff())
