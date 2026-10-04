import ast
import re
from crewai.tools import BaseTool


class RequestAnalysisTool(BaseTool):
    name: str = "Request Analysis Tool"
    description: str = (
        "Use this tool to structure a learner's request. Input should include the request type, "
        "programming language, experience level, and user goal. Returns a checklist of requirements to identify."
    )

    def _run(self, argument: str) -> str:
        return (
            "Request analysis checklist:\n"
            "1. Identify the user's actual goal and requested deliverable.\n"
            "2. Respect the chosen programming language and experience level.\n"
            "3. Separate required features from optional ideas.\n"
            "4. Identify missing information and state assumptions rather than inventing facts.\n"
            "5. Prefer a small, understandable result that matches the prompt.\n\n"
            f"Request supplied to the tool:\n{argument}"
        )


class RoadmapStructureTool(BaseTool):
    name: str = "Roadmap Structure Tool"
    description: str = (
        "Use this tool before creating a learning roadmap. Input should include the programming language, "
        "learner level, learning goal, and number of days. Returns a roadmap structure checklist."
    )

    def _run(self, argument: str) -> str:
        return (
            "Recommended roadmap structure:\n"
            "- Start with prerequisites and setup only when relevant.\n"
            "- Group related concepts into progressive stages.\n"
            "- Each day or stage should include: topic, objective, hands-on exercise, and a small checkpoint.\n"
            "- Include revision and a mini-project when time allows.\n"
            "- Keep the plan realistic for the learner's level and available time.\n"
            "- Avoid claiming that the learner will master a broad field in a few days.\n\n"
            f"Roadmap request:\n{argument}"
        )


class CodePlanningTool(BaseTool):
    name: str = "Code Planning Tool"
    description: str = (
        "Use this tool before explaining a programming concept or generating code. Input should include "
        "the language, skill level, and goal. Returns a checklist for readable, level-appropriate output."
    )

    def _run(self, argument: str) -> str:
        return (
            "Code and explanation checklist:\n"
            "- Match the requested language and the learner's level.\n"
            "- Prefer a minimal, readable example over unnecessary architecture.\n"
            "- Explain important variables, functions, and control flow.\n"
            "- Include expected output when useful.\n"
            "- Mention assumptions, edge cases, and likely limitations.\n"
            "- Do not claim code was executed unless a real execution tool was used.\n"
            "- Never recommend running untrusted code on a public application server.\n\n"
            f"Programming request:\n{argument}"
        )


class OutputValidationTool(BaseTool):
    name: str = "Output Validation Tool"
    description: str = (
        "Use this tool to perform a basic structural review of a draft. For Python code, provide the draft "
        "with a fenced Python code block so the tool can parse its syntax without executing it. "
        "For other languages, it performs only simple delimiter checks, not compilation."
    )

    def _run(self, argument: str) -> str:
        language_match = re.search(r"(?im)^LANGUAGE:\s*([^\n]+)", argument)
        fenced_language_match = re.search(r"```([a-zA-Z0-9_+#.-]+)\s*\n", argument)
        language = (
            language_match.group(1).strip().lower() if language_match
            else (fenced_language_match.group(1).strip().lower() if fenced_language_match else "")
        )
        code_blocks = re.findall(r"```(?:[a-zA-Z0-9_+#.-]+)?\s*\n(.*?)```", argument, flags=re.DOTALL)
        code = code_blocks[-1].strip() if code_blocks else ""

        if not code:
            checks = []
            if len(argument.strip()) < 80:
                checks.append("Draft is very short; verify that it answers the request.")
            if re.search(r"(?i)todo|placeholder|insert here", argument):
                checks.append("Potential placeholder text found.")
            if not checks:
                checks.append("No fenced code block found; code syntax check was not applicable.")
            return "Output validation results:\n- " + "\n- ".join(checks)

        if "python" in language:
            try:
                ast.parse(code)
                return (
                    "Static Python syntax check: PASSED (ast.parse accepted the code).\n"
                    "This does not prove the program runs correctly. Dependencies, runtime behavior, "
                    "inputs, and logic have not been tested."
                )
            except SyntaxError as exc:
                return (
                    "Static Python syntax check: FAILED.\n"
                    f"Line: {exc.lineno}\n"
                    f"Problem: {exc.msg}\n"
                    "Fix the syntax issue before presenting the code. This tool did not execute the program."
                )

        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}
        for char in code:
            if char in "([{":
                stack.append(char)
            elif char in ")]}":
                if not stack or stack[-1] != pairs[char]:
                    return (
                        "Basic delimiter check: FAILED (mismatched or unexpected closing delimiter).\n"
                        "This is a simple text check, not a language compiler."
                    )
                stack.pop()
        if stack:
            return (
                "Basic delimiter check: FAILED (one or more opening delimiters were not closed).\n"
                "This is a simple text check, not a language compiler."
            )
        return (
            "Basic delimiter check: PASSED.\n"
            "This is not a syntax or compilation check for the selected language. "
            "No code was executed."
        )
