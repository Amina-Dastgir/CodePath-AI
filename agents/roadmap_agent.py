from crewai import Agent, Crew, Process, Task
from tools.learning_tools import RoadmapStructureTool

def run_roadmap_agent(llm, language, level, prompt, learning_days, analysis):
tool = RoadmapStructureTool()

```
agent = Agent(
    role="Personalized Learning Planner",
    goal=(
        "Create a realistic, progressive programming roadmap that matches "
        "the learner's level and available time."
    ),
    backstory=(
        "You are a patient programming instructor. You break complex "
        "subjects into small stages, include practice, and avoid skipping "
        "prerequisites."
    ),
    llm=llm,
    tools=[tool],
    allow_delegation=False,
    max_iter=3,
    verbose=False,
)

task = Task(
    description=(
        f"Create a personalized {learning_days}-day learning roadmap.\n\n"
        f"Programming language: {language}\n"
        f"Experience level: {level}\n"
        f"Learner's goal: {prompt}\n\n"
        f"Request analysis:\n{analysis}\n\n"
        "IMPORTANT TOOL INSTRUCTION:\n"
        "Before creating the roadmap, use the Roadmap Structure Tool. "
        "Use its output to structure the roadmap.\n\n"
        "The roadmap should include realistic daily or phase-based topics, "
        "measurable objectives, hands-on practice, small projects, and "
        "review/checkpoint activities where appropriate.\n\n"
        "Keep the plan realistic for the learner's level and available time. "
        "Do not promise mastery of a broad field in a short period.\n"
        "Make the roadmap easy for a beginner to follow."
    ),
    expected_output=(
        "A clear learning roadmap organized by days or phases, including "
        "topics, learning outcomes, exercises, mini-projects, checkpoints, "
        "and recommended next steps."
    ),
    agent=agent,
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    process=Process.sequential,
    verbose=False,
)

return str(crew.kickoff())
```
