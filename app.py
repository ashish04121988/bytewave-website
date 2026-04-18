import streamlit as st
from styles import GLOBAL_CSS
from components import navbar, footer

st.set_page_config(
    page_title="Bytewave Digital — Right Technology. No Noise.",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
navbar("Home")

# ─── HERO ────────────────────────────────────────────────────────────────────
st.markdown("""
<section class="hero-section" style="display:flex;">
    <div class="hero-left">
        <div class="hero-eyebrow">Vendor-Neutral IT Software Reseller</div>
        <h1 class="hero-h1">
            Simplifying Technology Buying<br>
            for <span class="gradient-text">Modern Businesses</span>
        </h1>
        <p class="hero-sub">
            Built on the legacy of Fundoo Data, Bytewave Digital helps you identify and procure
            the right technology — faster, smarter, and without the noise.
        </p>
        <div class="hero-cta-group">
            <a target="_self" href="/Solutions" class="btn-gradient">🔍 Explore Solutions</a>
            <a target="_self" href="/Contact" class="btn-outline">💬 Talk to an Expert</a>
        </div>
    </div>
    <div class="hero-right">
        <div class="logo-centerpiece">
            <div class="logo-wave-text">⚡</div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── TRUST BANNER ────────────────────────────────────────────────────────────
st.markdown("""
<div class="trust-strip">
    <div style="text-align:center; margin-bottom:14px; font-size:13px; color:#64748B; letter-spacing:1px;">
        Born from the legacy of <strong style="color:#93C5FD;">Fundoo Data</strong> — trusted by organizations for corporate intelligence and insights
    </div>
    <div class="trust-items">
        <div class="trust-item"><span class="trust-icon">💻</span> Software Reselling</div>
        <div class="trust-item"><span class="trust-icon">🎯</span> Lead Generation</div>
        <div class="trust-item"><span class="trust-icon">🔥</span> Sales Execution</div>
        <div class="trust-item"><span class="trust-icon">📈</span> Revenue Acceleration</div>
        <div class="trust-item"><span class="trust-icon">🤝</span> Vendor-Neutral Advisory</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─── ABOUT SNAPSHOT ──────────────────────────────────────────────────────────
st.markdown("""
<section class="about-section">
    <div class="about-content">
        <div class="about-icon">⚡</div>
        <div class="section-label">About Us</div>
        <h2 class="section-title">Your Technology &amp; <span class="gradient-text">Revenue Growth</span> Partner</h2>
        <p class="about-body">
            Bytewave Digital is a <strong style="color:#93C5FD;">technology reseller with a strong advisory approach</strong>,
            helping businesses choose, implement, and optimize the right software solutions.
        </p>
        <p class="about-body" style="margin-top:12px;">
            Born from the legacy of Fundoo Data, we gained deep insights into how organizations evaluate and invest in technology.
            After working with SME, mid-size, and enterprise customers, we identified a critical gap — organizations
            struggled to find the right technology solutions in a complex and crowded market.
            <strong style="color:#93C5FD;">Bytewave Digital was created to simplify that journey.</strong>
        </p>
        <div style="margin-top:28px;">
            <a target="_self" href="/About" class="btn-gradient" style="text-decoration:none;">Learn Our Story →</a>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── SOLUTIONS OVERVIEW ───────────────────────────────────────────────────────
st.markdown("""
<section class="section section-darker">
    <div class="section-label">What We Do</div>
    <h2 class="section-title">Our <span class="gradient-text">Solutions</span></h2>
    <p class="section-subtitle">We simplify complex technology choices so you can focus on outcomes.</p>
    <div class="cards-grid">
        <div class="service-card">
            <span class="card-icon">🤝</span>
            <div class="card-title">CRM Solutions</div>
            <div class="card-desc">Select the right CRM platform to streamline sales, improve customer engagement, and drive revenue growth.</div>
        </div>
        <div class="service-card">
            <span class="card-icon">📣</span>
            <div class="card-title">Marketing Automation</div>
            <div class="card-desc">Navigate the crowded martech landscape with confidence. Choose platforms that enhance lead generation and campaigns.</div>
        </div>
        <div class="service-card">
            <span class="card-icon">☁️</span>
            <div class="card-title">Cloud &amp; IT Solutions</div>
            <div class="card-desc">Choose the right cloud platforms and infrastructure tools to support scalability and performance.</div>
        </div>
        <div class="service-card">
            <span class="card-icon">🤖</span>
            <div class="card-title">Agentic AI Solutions</div>
            <div class="card-desc">Leverage next-generation AI tools that automate workflows, enhance productivity, and drive intelligent decision-making.</div>
        </div>
        <div class="service-card">
            <span class="card-icon">👥</span>
            <div class="card-title">HR &amp; Finance Software</div>
            <div class="card-desc">Enable smarter workforce and financial management. Identify solutions that improve efficiency and compliance.</div>
        </div>
        <div class="service-card">
            <span class="card-icon">🔭</span>
            <div class="card-title">Observability</div>
            <div class="card-desc">Gain complete visibility into your applications and infrastructure at cloud scale.</div>
        </div>
    </div>
    <div style="text-align:center; margin-top:40px;">
        <a target="_self" href="/Solutions" class="btn-gradient" style="text-decoration:none;">View All Solutions →</a>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── HOW WE WORK ─────────────────────────────────────────────────────────────
st.markdown("""
<section class="section section-dark">
    <div class="section-label">How We Work</div>
    <h2 class="section-title">Understand → Curate → <span class="gradient-text">Enable</span></h2>
    <p class="section-subtitle">A simple, proven approach to simplify your technology buying journey.</p>
    <div class="process-steps" style="max-width:700px; margin:0 auto;">
        <div class="process-step" style="width:200px;">
            <div class="step-number">1</div>
            <div class="step-title">Understand</div>
            <div class="step-desc">We analyze your business needs, challenges, and goals in depth.</div>
        </div>
        <div class="step-connector" style="width:80px;"></div>
        <div class="process-step" style="width:200px;">
            <div class="step-number">2</div>
            <div class="step-title">Curate</div>
            <div class="step-desc">We shortlist the most relevant, best-fit technology solutions for you.</div>
        </div>
        <div class="step-connector" style="width:80px;"></div>
        <div class="process-step" style="width:200px;">
            <div class="step-number">3</div>
            <div class="step-title">Enable</div>
            <div class="step-desc">We help you make informed decisions and connect with the right vendors.</div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── WHY CHOOSE US ───────────────────────────────────────────────────────────
st.markdown("""
<section class="section section-darker">
    <div class="section-label">Why Bytewave Digital</div>
    <h2 class="section-title">The <span class="gradient-text">Bytewave</span> Advantage</h2>
    <p class="section-subtitle">We recommend what's right for you — not what we need to sell.</p>
    <div class="why-grid">
        <div class="why-item">
            <span class="why-check">✔</span>
            <span class="why-text">Vendor-neutral technology advisory</span>
        </div>
        <div class="why-item">
            <span class="why-check">✔</span>
            <span class="why-text">Access to leading global software providers</span>
        </div>
        <div class="why-item">
            <span class="why-check">✔</span>
            <span class="why-text">Faster, simplified procurement process</span>
        </div>
        <div class="why-item">
            <span class="why-check">✔</span>
            <span class="why-text">Cost optimization &amp; right-fit solutions</span>
        </div>
        <div class="why-item">
            <span class="why-check">✔</span>
            <span class="why-text">Built on the trusted legacy of Fundoo Data</span>
        </div>
        <div class="why-item">
            <span class="why-check">✔</span>
            <span class="why-text">Outcome-driven, ROI-focused approach</span>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── CTA BANNER ──────────────────────────────────────────────────────────────
st.markdown("""
<section class="cta-banner">
    <h2 class="cta-title">Ready to Choose the <span class="gradient-text">Right Technology?</span></h2>
    <p class="cta-sub">Let's simplify your software buying journey. No noise. No guesswork. Just the right fit.</p>
    <div class="cta-buttons">
        <a target="_self" href="/Contact" class="btn-gradient">📅 Schedule a Consultation</a>
        <a target="_self" href="/Solutions" class="btn-outline">🔍 Explore Solutions</a>
    </div>
</section>
""", unsafe_allow_html=True)

footer()
