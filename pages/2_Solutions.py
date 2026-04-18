import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import GLOBAL_CSS
from components import navbar, footer

st.set_page_config(
    page_title="Solutions — Bytewave Digital",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
navbar("Solutions")

# ─── PAGE HEADER ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <div class="page-header-watermark">SOLUTIONS</div>
    <div class="section-label">Technology Solutions</div>
    <h1 class="section-title">The Right Technology, <span class="gradient-text">Curated for You</span></h1>
    <p class="section-subtitle">
        We help you navigate a complex technology landscape — evaluating and comparing solutions
        so you can make confident, informed buying decisions.
    </p>
</div>
""", unsafe_allow_html=True)

# ─── SOLUTION 1: CRM ─────────────────────────────────────────────────────────
st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section section-dark">
    <div class="service-detail">
        <div class="service-detail-icon-block">🤝</div>
        <div class="service-detail-content">
            <div class="section-label" style="text-align:left;">Solution 01</div>
            <h2 class="service-detail-title">CRM Solutions</h2>
            <p class="service-detail-desc">
                Select CRM platforms that align with your sales processes, improve customer engagement,
                and drive revenue growth. We help you evaluate scalability, integrations, and usability
                before making a decision.
            </p>
            <ul class="service-detail-list">
                <li>Scalability evaluation</li>
                <li>Integration compatibility</li>
                <li>User adoption assessment</li>
                <li>Commercial comparison</li>
                <li>Vendor shortlisting</li>
                <li>Right-fit recommendation</li>
            </ul>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── SOLUTION 2: MARKETING AUTOMATION ────────────────────────────────────────
st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section section-darker">
    <div class="service-detail reverse">
        <div class="service-detail-icon-block">📣</div>
        <div class="service-detail-content">
            <div class="section-label" style="text-align:left;">Solution 02</div>
            <h2 class="service-detail-title">Marketing Automation Tools</h2>
            <p class="service-detail-desc">
                Navigate the crowded martech landscape with confidence. We guide you in choosing platforms
                that enhance lead generation, campaign management, and customer journey orchestration
                aligned to your marketing strategy.
            </p>
            <ul class="service-detail-list">
                <li>Lead generation platforms</li>
                <li>Campaign management tools</li>
                <li>Customer journey orchestration</li>
                <li>Martech stack evaluation</li>
                <li>Integration mapping</li>
                <li>ROI-focused selection</li>
            </ul>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── SOLUTION 3: HR & FINANCE ─────────────────────────────────────────────────
st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section section-dark">
    <div class="service-detail">
        <div class="service-detail-icon-block">👥</div>
        <div class="service-detail-content">
            <div class="section-label" style="text-align:left;">Solution 03</div>
            <h2 class="service-detail-title">HR &amp; Finance Software</h2>
            <p class="service-detail-desc">
                Enable smarter workforce and financial management with the right tools. We help you
                identify solutions that improve operational efficiency, compliance, and decision-making
                across your HR and finance functions.
            </p>
            <ul class="service-detail-list">
                <li>Workforce management platforms</li>
                <li>Financial reporting tools</li>
                <li>Payroll & compliance solutions</li>
                <li>Operational efficiency evaluation</li>
                <li>Compliance alignment</li>
                <li>Decision-making improvement</li>
            </ul>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── SOLUTION 4: CLOUD & IT ───────────────────────────────────────────────────
st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section section-darker">
    <div class="service-detail reverse">
        <div class="service-detail-icon-block">☁️</div>
        <div class="service-detail-content">
            <div class="section-label" style="text-align:left;">Solution 04</div>
            <h2 class="service-detail-title">Cloud &amp; IT Solutions</h2>
            <p class="service-detail-desc">
                Choose the right cloud platforms and infrastructure tools to support scalability and performance.
                We help you evaluate options across public, private, and hybrid environments aligned
                to your business goals and budget.
            </p>
            <ul class="service-detail-list">
                <li>Public cloud evaluation</li>
                <li>Private & hybrid options</li>
                <li>Infrastructure comparison</li>
                <li>Cost optimization</li>
                <li>Scalability planning</li>
                <li>Vendor negotiation support</li>
            </ul>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── SOLUTION 5: AGENTIC AI ──────────────────────────────────────────────────
st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section section-dark">
    <div class="service-detail">
        <div class="service-detail-icon-block">🤖</div>
        <div class="service-detail-content">
            <div class="section-label" style="text-align:left;">Solution 05</div>
            <h2 class="service-detail-title">Agentic AI Solutions</h2>
            <p class="service-detail-desc">
                Leverage next-generation AI tools that automate workflows, enhance productivity, and drive
                intelligent decision-making. We help you identify AI platforms that align with your use
                cases and deliver measurable business value.
            </p>
            <ul class="service-detail-list">
                <li>Workflow automation AI</li>
                <li>Decision-making platforms</li>
                <li>Productivity enhancement tools</li>
                <li>Use-case alignment</li>
                <li>AI readiness assessment</li>
                <li>Business value mapping</li>
            </ul>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── SOLUTION 6: OBSERVABILITY ───────────────────────────────────────────────
st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section section-darker">
    <div class="service-detail reverse">
        <div class="service-detail-icon-block">🔭</div>
        <div class="service-detail-content">
            <div class="section-label" style="text-align:left;">Solution 06</div>
            <h2 class="service-detail-title">Observability for Cloud-Scale Applications</h2>
            <p class="service-detail-desc">
                Gain complete visibility into your applications and infrastructure. We help you choose
                observability platforms that ensure performance, reliability, and faster issue resolution
                at cloud scale — so your teams can act on insights, not guesses.
            </p>
            <ul class="service-detail-list">
                <li>Application monitoring</li>
                <li>Infrastructure visibility</li>
                <li>Performance analytics</li>
                <li>Reliability engineering tools</li>
                <li>Incident resolution speed</li>
                <li>Cloud-scale platform evaluation</li>
            </ul>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── CTA ─────────────────────────────────────────────────────────────────────
st.markdown("""
<section class="cta-banner">
    <h2 class="cta-title">Not Sure Which Solution <span class="gradient-text">You Need?</span></h2>
    <p class="cta-sub">Talk to our experts and we'll help you identify the right technology fit for your business.</p>
    <div class="cta-buttons">
        <a target="_self" href="/Contact" class="btn-gradient">💬 Talk to an Expert</a>
        <a target="_self" href="/Services" class="btn-outline">⚙️ See How We Help</a>
    </div>
</section>
""", unsafe_allow_html=True)

footer()
