# ⚡ CodePath AI

### Multi-Agent AI Programming & Learning Assistant

> **Learn smarter. Code better. Build your path.**

CodePath AI is a **multi-agent AI programming assistant** that helps learners understand programming concepts, generate code, create personalized learning roadmaps, and review programming outputs.

Instead of relying on a single AI response, CodePath AI uses a team of specialized AI agents coordinated through **CrewAI**, powered by **Google Gemini**, and presented through a modern **Streamlit** interface.

---

## 🌟 Why CodePath AI?

Learning programming can be overwhelming.

A learner may know **what** they want to build but not:

* What concepts they need to learn first
* Which topics are suitable for their current skill level
* How to turn an idea into working code
* Why a particular piece of code works
* Whether their generated code has obvious problems
* What they should learn next

CodePath AI brings these tasks together into one intelligent workflow.

The user provides:

**Programming Language + Experience Level + Goal + Request**

and the AI agent team works together to produce a structured result.

---

# 🚀 Key Features

### 🗺️ Personalized Learning Roadmaps

Generate a structured learning path based on:

* Programming language
* Experience level
* Learning goal
* Available time

The planner breaks a large goal into manageable stages, practice exercises, checkpoints, and mini-projects.

---

### 💡 Programming Concept Explanations

Ask CodePath AI to explain concepts such as:

* Variables
* Functions
* Loops
* Object-Oriented Programming
* APIs
* Data Structures
* File Handling
* Exception Handling
* And many more

Explanations are adapted to the learner's selected experience level.

---

### 💻 AI Code Generation

Describe what you want to build and select your programming language.

CodePath AI can generate:

* Beginner-friendly examples
* Small programming solutions
* Commented code
* Sample input/output
* Explanations of important logic
* Potential limitations and edge cases

---

### 🛡️ Code & Output Review

Generated output passes through a dedicated review stage.

The reviewer checks:

* Relevance to the user's request
* Output structure
* Obvious issues
* Python syntax when applicable
* Basic delimiter consistency for other languages
* Explanation/code consistency

> CodePath AI does **not** claim that generated code has been executed when it has not.

---

# 🤖 Multi-Agent Architecture

CodePath AI uses specialized agents instead of putting every responsibility into one large prompt.

```text
                    ┌─────────────────────┐
                    │     Streamlit UI     │
                    │   User Request       │
                    └──────────┬──────────┘
                               │
                               ▼
                 ┌─────────────────────────┐
                 │ Requirement Analyzer    │
                 │        Agent            │
                 └────────────┬────────────┘
                              │
                 ┌────────────┴────────────┐
                 │                         │
                 ▼                         ▼
       ┌──────────────────┐      ┌──────────────────┐
       │ Learning Planner │      │  Code Assistant  │
       │      Agent       │      │      Agent       │
       └────────┬─────────┘      └────────┬─────────┘
                │                         │
                └────────────┬────────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │  Quality Reviewer   │
                  │       Agent         │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │   Final Response    │
                  │   + Explanation     │
                  │   + Code/roadmap    │
                  └─────────────────────┘
```

---

# 🧠 Agent Team

## 1. 🧭 Requirement Analyzer Agent

### Responsibility

Understands and structures the user's request before another specialist works on it.

It identifies:

* User goal
* Programming language
* Experience level
* Request type
* Constraints
* Expected deliverable
* Missing information

### Tool

**Request Analysis Tool**

---

## 2. 🗺️ Learning Planner Agent

### Responsibility

Creates personalized learning roadmaps.

It considers:

* Current experience
* Programming language
* Learning goal
* Available time
* Required prerequisites

### Tool

**Roadmap Structure Tool**

---

## 3. 💻 Code Assistant Agent

### Responsibility

Handles programming-related learning and code generation.

It can:

* Explain concepts
* Generate code
* Explain code
* Provide examples
* Suggest practice exercises

### Tool

**Code Planning Tool**

---

## 4. 🛡️ Quality Reviewer Agent

### Responsibility

Reviews the generated result before it reaches the user.

It performs:

* Output validation
* Basic Python syntax checking
* Basic delimiter checking for other languages
* Structure review
* Quality improvement

### Tool

**Output Validation Tool**

---

# 🧰 Tool-Enabled Agents

A core design principle of CodePath AI is that the agents are **tool-enabled**.

The system contains custom tools designed for different stages of the workflow.

| Tool                       | Purpose                                 |
| -------------------------- | --------------------------------------- |
| 🔍 Request Analysis Tool   | Structures the user's request           |
| 🗺️ Roadmap Structure Tool | Provides learning-plan structure        |
| 💻 Code Planning Tool      | Provides language-aware coding guidance |
| 🛡️ Output Validation Tool | Performs basic output/static validation |

The tools provide deterministic guidance/checks around the LLM workflow instead of relying entirely on free-form generation.

---

# 🛠️ Technology Stack

| Technology           | Purpose                            |
| -------------------- | ---------------------------------- |
| 🐍 Python            | Core application                   |
| 🤖 CrewAI            | Multi-agent orchestration          |
| ✨ Google Gemini      | Large Language Model               |
| 🎨 Streamlit         | Web interface                      |
| 🔐 Streamlit Secrets | API key management                 |
| 🐙 GitHub            | Source control & deployment source |

---

# 🎨 User Interface

CodePath AI uses a modern dark-themed interface designed around a simple workflow:

```text
01 / Tell us what you want to do
            ↓
02 / Agent workflow
            ↓
03 / Live agent progress
            ↓
04 / Your result
```

The interface displays the active agent while the request is being processed.

For example:

```text
🧭 Requirement Analyzer — complete

🗺️ Learning Planner Agent — working

🛡️ Quality Reviewer Agent — pending
```

This makes the multi-agent architecture visible during the hackathon demonstration.

---

# 📁 Project Structure

```text
CodePath-AI/
│
├── app.py
├── settings.py
├── requirements.txt
├── README.md
│
├── agents/
│   ├── __init__.py
│   ├── requirement_agent.py
│   ├── roadmap_agent.py
│   ├── code_agent.py
│   └── reviewer_agent.py
│
├── tools/
│   ├── __init__.py
│   └── learning_tools.py
│
└── .streamlit/
    └── config.toml
```

### Why modular architecture?

Each agent has its own file.

This makes the project:

* Easier to understand
* Easier to debug
* Easier to modify
* Easier for a team to work on
* Easier to extend with new agents

For example, a future `Quiz Agent` can be added without rewriting the entire application.

---

# 🔄 How the System Works

### Step 1 — User Input

The user selects:

```text
Programming Language
        +
Experience Level
        +
Request Type
        +
Programming Goal
```

---

### Step 2 — Requirement Analysis

The Requirement Analyzer understands the request and creates a structured task.

---

### Step 3 — Specialist Agent

Depending on the request, CodePath AI routes the task to the appropriate specialist.

For example:

```text
Learning Roadmap
       ↓
Learning Planner Agent
```

or

```text
Code Generation
       ↓
Code Assistant Agent
```

---

### Step 4 — Review

The generated output goes through the Quality Reviewer.

---

### Step 5 — Final Result

The user receives:

* Roadmap
* Explanation
* Code
* Review feedback
* Practice suggestions

depending on the selected workflow.

---

# 💻 Example Use Cases

## Use Case 1 — Learning Roadmap

### User Input

```text
Language: Python

Experience: Beginner

Request:
I want to learn Python for AI development.

Time:
30 days
```

### CodePath AI

Generates:

```text
Phase 1
Python Fundamentals

Phase 2
Functions & Modules

Phase 3
Data Structures

Phase 4
Object-Oriented Programming

Phase 5
File Handling & APIs

Phase 6
Python for Data/AI

Final Mini Project
```

---

# 💻 Use Case 2 — Code Generation

### User Input

```text
Language: Python

Experience: Beginner

Request:
Create a program that calculates the average
of five student marks.
```

### Output

Code + explanation + sample input/output + review.

---

# 💡 Use Case 3 — Concept Explanation

### User Input

```text
Language: Python

Experience: Beginner

Concept:
Functions
```

### Output

The system can provide:

* Simple definition
* Syntax
* Example
* Explanation
* Expected output
* Common mistakes
* Practice questions

---

# 🛡️ Use Case 4 — Code Review

A learner can paste code and ask CodePath AI to review it.

The Quality Reviewer performs basic static checks and provides improvement suggestions.

For Python, the project uses Python's built-in AST parser for syntax parsing.

> Static syntax validation does not guarantee that a program will run correctly.

---

# 🔐 Security

CodePath AI does **not** store API keys inside source code.

The Gemini API key should be provided through **Streamlit Secrets**.

Example:

```toml
GEMINI_API_KEY = "your-api-key"
```

### Never do this:

```python
GEMINI_API_KEY = "actual-secret-key"
```

Never commit API keys to GitHub.

If an API key is accidentally exposed publicly, revoke it and generate a new one.

---

# ⚙️ Deployment

CodePath AI is designed for a simple deployment workflow:

```text
ChatGPT
   ↓
Create / modify code
   ↓
GitHub
   ↓
Streamlit Community Cloud
   ↓
Live Web Application
```

No local Python environment is required for the intended deployment workflow.

---

# ☁️ Deploy to Streamlit Community Cloud

### 1. Create a GitHub repository

Create a repository named:

```text
CodePath-AI
```

### 2. Upload the project

Make sure the repository preserves this structure:

```text
app.py
settings.py
requirements.txt

agents/
tools/
.streamlit/
```

### 3. Connect GitHub to Streamlit

Open Streamlit Community Cloud and create a new app.

Select:

```text
Repository: CodePath-AI
Branch: main
Main file: app.py
```

### 4. Add the Gemini API key

In Streamlit app settings, add the secret:

```toml
GEMINI_API_KEY = "your-gemini-api-key"
```

### 5. Deploy

Streamlit will install the dependencies from:

```text
requirements.txt
```

and launch:

```text
app.py
```

---

# 📦 Installation Dependencies

The application uses the dependencies declared in:

```text
requirements.txt
```

Core libraries:

```text
streamlit
crewai
```

The project is intentionally kept lightweight for the hackathon MVP.

---

# 🧪 Testing Strategy

The project should be tested using representative requests.

### Roadmap Test

```text
Create a 7-day Python beginner roadmap.
```

### Concept Test

```text
Explain Python functions to a beginner.
```

### Code Test

```text
Create a Python student marks calculator.
```

### Review Test

Submit intentionally incorrect Python syntax and verify that the reviewer identifies the issue.

---

# ⚠️ Limitations

CodePath AI is an AI-assisted learning tool.

Generated responses may contain mistakes.

In particular:

* Generated code may contain logical errors.
* Static syntax checking does not prove runtime correctness.
* Non-Python validation is limited.
* The application does not execute arbitrary generated code.
* Gemini API availability and quotas depend on the configured account/service.
* The roadmap is guidance, not a guarantee of mastery.

Users should review and safely test generated code before using it in real projects.

---

# 🔮 Future Roadmap

The architecture is designed so additional agents and tools can be added later.

### Planned possibilities

* 🧠 Long-term learner memory
* 📊 Learning progress dashboard
* 📝 AI-generated quizzes
* 🎯 Skill assessment
* 🧪 Sandboxed code execution
* 🏆 Coding challenges
* 📚 RAG-based programming knowledge base
* 🔗 GitHub project analysis
* 👨‍🏫 Personalized AI tutor
* 🌐 Support for more programming languages
* 📥 Export roadmap as PDF
* 🔄 Adaptive roadmap based on learner performance

---

# 🏆 Hackathon Value

CodePath AI demonstrates several modern AI engineering concepts in a single application:

### Multi-Agent AI

Different agents have different responsibilities.

### Tool-Using Agents

Agents are equipped with specialized tools for analysis, planning, coding guidance, and validation.

### Personalized AI

The system adapts its output to the learner's programming language and experience level.

### Human-Centered Design

The application focuses on making AI output understandable and actionable for learners.

### Modular Architecture

Agents and tools are separated into independent modules for easier development and scaling.

---

# 👥 Team

Built as an AI Hackathon project.

### Team Contributions

* AI / Agent Architecture
* CrewAI Workflow
* Gemini Integration
* Streamlit UI/UX
* Custom Tools
* Testing & Deployment

---

# 📄 License

This project currently does not specify a license.

Add an appropriate open-source license if you plan to distribute the project publicly.

---

# ⭐ Acknowledgements

Built using:

* CrewAI
* Google Gemini
* Streamlit
* Python

---

## 🚀 CodePath AI

**From “I want to learn this” → to “I know what to build next.”**

> **Learn. Build. Review. Improve.**
