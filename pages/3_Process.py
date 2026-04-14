import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import GLOBAL_CSS
from components import navbar, footer

st.set_page_config(
    page_title="Our Process — Bytewave Digital Solutions",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
navbar("Process")

# ─── PAGE HEADER ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <div class="page-header-watermark">PROCESS</div>
    <div class="section-label">How It Works</div>
    <h1 class="section-title">Our <span class="gradient-text">Revenue Blueprint</span></h1>
    <p class="section-subtitle">
        A proven 5-step process that takes your business from discovery to revenue —
        built on data, executed with precision.
    </p>
</div>
""", unsafe_allow_html=True)

# ─── PROCESS STEPS ───────────────────────────────────────────────────────────
st.markdown("""
<section class="section section-darker" style="padding-bottom:100px;">
    <div class="process-steps">
        <div class="process-step">
            <div class="step-number">1</div>
            <div class="step-title">Understand</div>
            <div class="step-desc">Deep-dive into your business, goals, and current revenue challenges.</div>
        </div>
        <div class="step-connector"></div>
        <div class="process-step">
            <div class="step-number">2</div>
            <div class="step-title">Target</div>
            <div class="step-desc">Identify your ideal customer profile and build precise targeting lists.</div>
        </div>
        <div class="step-connector"></div>
        <div class="process-step">
            <div class="step-number">3</div>
            <div class="step-title">Generate</div>
            <div class="step-desc">Execute multi-channel outreach and generate qualified leads at scale.</div>
        </div>
        <div class="step-connector"></div>
        <div class="process-step">
            <div class="step-number">4</div>
            <div class="step-title">Pipeline</div>
            <div class="step-desc">Build and manage a healthy sales pipeline with constant nurturing.</div>
        </div>
        <div class="step-connector"></div>
        <div class="process-step">
            <div class="step-number">5</div>
            <div class="step-title">Close</div>
            <div class="step-desc">Drive deals to closure with active sales support and follow-ups.</div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── STEP DETAILS ────────────────────────────────────────────────────────────
steps = [
    {
        "num": "01",
        "icon": "🔍",
        "title": "Understand Your Business",
        "desc": "We start by gaining a thorough understanding of your business model, revenue goals, current pain points, and competitive landscape. This discovery phase ensures every subsequent step is aligned with what actually matters to you.",
        "bullets": ["Business model analysis", "Revenue goal setting", "Pain point identification", "Competitive landscape review", "Stakeholder alignment"],
        "reverse": False,
    },
    {
        "num": "02",
        "icon": "🎯",
        "title": "Identify Target Market",
        "desc": "Using premium data sources and market intelligence, we build precise Ideal Customer Profiles (ICPs) and identify high-value decision-makers in your target segments. We map the entire addressable market before launching any outreach.",
        "bullets": ["ICP development", "Decision-maker mapping", "Market segmentation", "Geographic targeting", "Intent signal analysis"],
        "reverse": True,
    },
    {
        "num": "03",
        "icon": "📈",
        "title": "Generate Qualified Leads",
        "desc": "With a clear target in mind, we execute precision outreach across email, LinkedIn, and other channels. Every lead is qualified against your ICP criteria before it enters your pipeline — ensuring your team only talks to the right people.",
        "bullets": ["Multi-channel outreach", "Email campaigns", "LinkedIn prospecting", "Appointment setting", "Lead qualification scoring"],
        "reverse": False,
    },
    {
        "num": "04",
        "icon": "🔥",
        "title": "Build the Pipeline",
        "desc": "We don't just hand off leads. We actively manage and nurture your pipeline — ensuring prospects move through stages with the right messaging, follow-ups, and engagement tactics. Expect a healthy, growing pipeline at all times.",
        "bullets": ["CRM pipeline management", "Deal stage tracking", "Nurture sequences", "Stakeholder engagement", "Pipeline health reporting"],
        "reverse": True,
    },
    {
        "num": "05",
        "icon": "🏆",
        "title": "Close Deals & Drive Revenue",
        "desc": "The final step is where revenue happens. We support your closing process with demo coordination, proposal follow-ups, objection handling, and deal acceleration tactics. We act as your extended team until the contract is signed.",
        "bullets": ["Demo coordination", "Proposal support", "Objection handling", "Contract facilitation", "Post-close onboarding support"],
        "reverse": False,
    },
]

for i, step in enumerate(steps):
    bg = "section-dark" if i % 2 == 0 else "section-darker"
    rev = "reverse" if step["reverse"] else ""
    bullets_html = "".join([f"<li>{b}</li>" for b in step["bullets"]])
    st.markdown(f"""
<div class="gradient-divider"></div>
<section class="section {bg}">
    <div class="service-detail {rev}">
        <div class="service-detail-icon-block" style="font-size:54px;">{step["icon"]}</div>
        <div class="service-detail-content">
            <div class="section-label" style="text-align:left;">Step {step["num"]}</div>
            <h2 class="service-detail-title">{step["title"]}</h2>
            <p class="service-detail-desc">{step["desc"]}</p>
            <ul class="service-detail-list">{bullets_html}</ul>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── CTA ─────────────────────────────────────────────────────────────────────
st.markdown("""
<section class="cta-banner">
    <h2 class="cta-title">Ready to Start the <span class="gradient-text">Process?</span></h2>
    <p class="cta-sub">Book a free strategy call and let's map out a revenue plan for your business.</p>
    <div class="cta-buttons">
        <a href="/Contact" class="btn-gradient">🚀 Start the Journey</a>
        <a href="/Services" class="btn-outline">📋 Explore Services</a>
    </div>
</section>
""", unsafe_allow_html=True)

footer()
