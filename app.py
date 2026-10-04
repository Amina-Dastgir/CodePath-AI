import os
import streamlit as st

from settings import create_llm, MODEL_NAME
from agents.requirement_agent import run_requirement_analysis
from agents.roadmap_agent import run_roadmap_agent
from agents.code_agent import run_code_agent
from agents.reviewer_agent import run_reviewer_agent

st.set_page_config(
    page_title="CodePath AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');
:root { --cp-bg:#0a0f1e; --cp-card:#121a2d; --cp-border:rgba(160,174,210,.16); --cp-purple:#8b5cf6; --cp-cyan:#22d3ee; }
.stApp { background: radial-gradient(ellipse at 12% 0%, rgba(99,102,241,.18), transparent 36%), radial-gradient(ellipse at 90% 12%, rgba(34,211,238,.10), transparent 30%), #0a0f1e; }
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
h1,h2,h3 { font-family:'Space Grotesk',sans-serif !important; letter-spacing:-.03em; }
.block-container { max-width: 1380px; padding-top: 1.7rem; padding-bottom: 3rem; }
section[data-testid="stSidebar"] { background: rgba(13,19,36,.96); border-right:1px solid var(--cp-border); }
.hero { padding: 1.8rem 1.9rem; border:1px solid rgba(139,92,246,.30); border-radius:24px; background:linear-gradient(125deg,rgba(139,92,246,.17),rgba(34,211,238,.06) 60%,rgba(255,255,255,.02)); margin-bottom:1.2rem; }
.eyebrow { color:#a5b4fc; font-size:.78rem; font-weight:700; letter-spacing:.14em; text-transform:uppercase; }
.hero-title { font-family:'Space Grotesk',sans-serif; font-size:2.45rem; line-height:1.12; font-weight:700; margin:.45rem 0 .7rem; color:#f5f7ff; }
.hero-copy { color:#aab5cf; max-width:760px; font-size:1rem; line-height:1.65; }
.feature-card { border:1px solid var(--cp-border); border-radius:18px; padding:1rem 1.05rem; background:rgba(18,26,45,.78); min-height:125px; }
.feature-icon { font-size:1.35rem; margin-bottom:.45rem; }
.feature-title { font-weight:700; color:#eef2ff; margin-bottom:.3rem; }
.feature-copy { color:#9eabc7; font-size:.86rem; line-height:1.45; }
.section-label { color:#c7d2fe; font-size:.78rem; letter-spacing:.12em; font-weight:700; text-transform:uppercase; margin:.3rem 0 .65rem; }
div[data-testid="stForm"] { border:1px solid var(--cp-border); background:rgba(18,26,45,.72); border-radius:20px; padding:1.1rem 1.15rem; }
.stButton > button, div[data-testid="stFormSubmitButton"] > button { border-radius:12px; min-height:2.8rem; font-weight:700; border:1px solid rgba(167,139,250,.45); transition:all .2s ease; }
div[data-testid="stFormSubmitButton"] > button { background:linear-gradient(90deg,#7c3aed,#6366f1); color:white; }
.stButton > button:hover, div[data-testid="stFormSubmitButton"] > button:hover { border-color:#a5b4fc; transform:translateY(-1px); }
div[data-testid="stTextArea"] textarea, div[data-testid="stTextInput"] input { border-radius:12px; }
div[data-testid="stSelectbox"] > div > div { border-radius:12px; }
div[data-testid="stMetric"] { background:rgba(18,26,45,.75); border:1px solid var(--cp-border); border-radius:15px; padding: .8rem 1rem; }
div[data-testid="stStatusWidget"] { border:1px solid var(--cp-border); border-radius:14px; background:rgba(18,26,45,.75); }
.result-card { border:1px solid var(--cp-border); border-radius:18px; padding:1rem 1.2rem; background:rgba(18,26,45,.75); }
.muted { color:#9eabc7; }
footer { visibility:hidden; }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def get_api_key():
    """Read the Gemini key from Streamlit Cloud secrets, with an env-var fallback."""
    try:
        value = st.secrets.get("GEMINI_API_KEY", "")
        if value:
            return value
    except Exception:
        pass
    return os.getenv("GEMINI_API_KEY", "")


with st.sidebar:
    st.markdown("## ⚡ CodePath AI")
    st.caption("Your AI-powered programming companion")
    st.markdown("---")
    st.markdown("### Agent team")
    st.markdown("🧭 **Requirement Analyzer**")
    st.caption("Understands your goal and skill level.")
    st.markdown("🗺️ **Learning Planner**")
    st.caption("Creates a step-by-step roadmap.")
    st.markdown("💻 **Code Assistant**")
    st.caption("Explains concepts and generates code.")
    st.markdown("🛡️ **Quality Reviewer**")
    st.caption("Checks output structure and basic syntax.")
    st.markdown("---")
    st.markdown("**Model**")
    st.code(MODEL_NAME, language="text")
    st.caption("Gemini API · CrewAI · Streamlit")
    st.markdown("---")
    st.caption("Tip: start with one clear request. You can refine it in a new run.")

st.markdown(
    """
    <div class="hero">
      <div class="eyebrow">MULTI-AGENT LEARNING STUDIO</div>
      <div class="hero-title">Learn to code.<br>Build with confidence.</div>
      <div class="hero-copy">Turn a programming goal into a learning roadmap, clear explanations, practical code, and a review step — powered by a coordinated AI agent team.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

feature_cols = st.columns(3)
features = [
    ("🧭", "Personalized roadmaps", "Break a goal into manageable learning steps."),
    ("⚡", "Code on demand", "Generate examples for your language and level."),
    ("🛡️", "Review before you go", "Get basic validation and improvement notes."),
]
for col, (icon, title, copy) in zip(feature_cols, features):
    with col:
        st.markdown(
            f'<div class="feature-card"><div class="feature-icon">{icon}</div>'
            f'<div class="feature-title">{title}</div><div class="feature-copy">{copy}</div></div>',
            unsafe_allow_html=True,
        )

st.write("")
left, right = st.columns([1.18, 0.82], gap="large")

with left:
    st.markdown('<div class="section-label">01 / Tell us what you want to do</div>', unsafe_allow_html=True)
    with st.form("codepath_request_form", clear_on_submit=False):
        task_type = st.selectbox(
            "What do you need help with?",
            [
                "Learning roadmap",
                "Explain a concept",
                "Generate code",
                "Review my code",
            ],
        )
        c1, c2 = st.columns(2)
        with c1:
            language = st.selectbox(
                "Programming language",
                ["Python", "JavaScript", "Java", "C++", "C#", "HTML/CSS", "SQL", "Other"],
            )
        with c2:
            level = st.selectbox("Your experience level", ["Beginner", "Intermediate", "Advanced"])
        learning_days = st.slider(
            "Learning time (used for roadmap requests)",
            min_value=3,
            max_value=90,
            value=30,
            step=1,
        )
        prompt = st.text_area(
            "Describe your goal or paste your code",
            placeholder=(
                "Example: I am a beginner. Explain Python functions with a simple example and 3 practice questions.\n"
                "For code review, paste your code here and describe what it should do."
            ),
            height=155,
            help="Be specific about the result you want. Do not paste passwords, API keys, or private data.",
        )
        submitted = st.form_submit_button("✨ Build my result", use_container_width=True)

with right:
    st.markdown('<div class="section-label">02 / What happens next</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="result-card">
          <h3 style="margin-top:.15rem">Your request, coordinated</h3>
          <p class="muted">CodePath AI routes your request through a small team of specialist agents.</p>
          <hr style="border-color:rgba(160,174,210,.16)">
          <p>① <b>Analyze</b> — clarify the goal and constraints.</p>
          <p>② <b>Create</b> — generate the roadmap, explanation, or code.</p>
          <p>③ <b>Review</b> — check structure and run safe static checks where applicable.</p>
          <p class="muted" style="font-size:.82rem;margin-bottom:0">Generated code is not executed on the server. Always review and test code before using it.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    st.info("The active agent will appear below while your request is being processed.", icon="🤖")

if submitted:
    if not prompt.strip():
        st.warning("Please describe your goal or paste the code you want reviewed.")
    else:
        api_key = get_api_key()
        if not api_key:
            st.error(
                "Gemini API key not found. Open your Streamlit app settings → Secrets and add "
                '`GEMINI_API_KEY = "your_key_here"`.'
            )
        else:
            workflow = []
            analysis = ""
            draft = ""
            final_output = ""
            progress = st.progress(0, text="Preparing your agent team…")
            st.markdown('<div class="section-label">03 / Live agent workflow</div>', unsafe_allow_html=True)
            try:
                llm = create_llm()

                with st.status("🧭 Requirement Analyzer — working", expanded=True) as status:
                    status.write("Using the Request Analysis Tool to structure your goal.")
                    analysis = run_requirement_analysis(
                        llm=llm,
                        language=language,
                        level=level,
                        task_type=task_type,
                        prompt=prompt,
                        learning_days=learning_days,
                    )
                    status.update(label="✅ Requirement Analyzer — complete", state="complete", expanded=False)
                workflow.append(("Requirement Analyzer", "Request Analysis Tool", analysis))
                progress.progress(25, text="Request analyzed")

                if task_type == "Learning roadmap":
                    with st.status("🗺️ Learning Planner Agent — working", expanded=True) as status:
                        status.write("Using the Roadmap Structure Tool to organize learning stages.")
                        draft = run_roadmap_agent(
                            llm=llm,
                            language=language,
                            level=level,
                            prompt=prompt,
                            learning_days=learning_days,
                            analysis=analysis,
                        )
                        status.update(label="✅ Learning Planner Agent — complete", state="complete", expanded=False)
                    workflow.append(("Learning Planner Agent", "Roadmap Structure Tool", draft))
                    progress.progress(65, text="Roadmap created")
                elif task_type == "Review my code":
                    draft = prompt
                    progress.progress(55, text="Code submitted for review")
                else:
                    with st.status("💻 Code Assistant Agent — working", expanded=True) as status:
                        status.write("Using the Code Planning Tool to prepare language-specific guidance.")
                        draft = run_code_agent(
                            llm=llm,
                            language=language,
                            level=level,
                            task_type=task_type,
                            prompt=prompt,
                            analysis=analysis,
                        )
                        status.update(label="✅ Code Assistant Agent — complete", state="complete", expanded=False)
                    workflow.append(("Code Assistant Agent", "Code Planning Tool", draft))
                    progress.progress(65, text="Draft generated")

                with st.status("🛡️ Quality Reviewer Agent — working", expanded=True) as status:
                    status.write("Using the Output Validation Tool for structural checks and basic static review.")
                    final_output = run_reviewer_agent(
                        llm=llm,
                        language=language,
                        task_type=task_type,
                        draft=draft,
                    )
                    status.update(label="✅ Quality Reviewer Agent — complete", state="complete", expanded=False)
                workflow.append(("Quality Reviewer Agent", "Output Validation Tool", final_output))
                progress.progress(100, text="Workflow complete")

                st.session_state["last_result"] = final_output
                st.session_state["last_draft"] = draft
                st.session_state["last_analysis"] = analysis
                st.session_state["last_workflow"] = workflow
                st.session_state["last_request"] = {
                    "type": task_type,
                    "language": language,
                    "level": level,
                    "prompt": prompt,
                }
                st.success("Your result is ready.")
            except Exception as exc:
                progress.empty()
                st.error(
                    "The workflow could not finish. Check your Gemini API key, model availability, "
                    "API quota, and Streamlit app logs. Technical detail: "
                    + str(exc)[:700]
                )

if "last_result" in st.session_state:
    st.write("")
    st.markdown('<div class="section-label">04 / Your result</div>', unsafe_allow_html=True)
    result_tab, workflow_tab, draft_tab = st.tabs(["✨ Final result", "🤖 Agent workflow", "📝 Original draft"])
    with result_tab:
        st.markdown(st.session_state["last_result"])
        st.download_button(
            "⬇️ Download result as Markdown",
            data=st.session_state["last_result"],
            file_name="codepath_ai_result.md",
            mime="text/markdown",
            use_container_width=False,
        )
    with workflow_tab:
        request_info = st.session_state.get("last_request", {})
        st.caption(
            f"{request_info.get('type', '')} · {request_info.get('language', '')} · "
            f"{request_info.get('level', '')}"
        )
        for index, (agent_name, tool_name, output) in enumerate(st.session_state.get("last_workflow", []), start=1):
            with st.expander(f"{index}. {agent_name}  ·  Tool: {tool_name}", expanded=False):
                st.markdown(output)
    with draft_tab:
        st.markdown(st.session_state.get("last_draft", ""))

st.markdown(
    """
    <div style="text-align:center;color:#7784a4;font-size:.8rem;padding:2rem 0 0">
      CodePath AI · Built with Streamlit, CrewAI and Gemini · Review AI-generated code before running it.
    </div>
    """,
    unsafe_allow_html=True,
)
