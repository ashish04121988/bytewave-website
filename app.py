import streamlit as st
from styles import GLOBAL_CSS
from components import navbar, footer

st.set_page_config(
    page_title="Bytewave Digital Solutions",
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
        <div class="hero-eyebrow">Your Growth Partner in Technology & Sales</div>
        <h1 class="hero-h1">
            We Don't Just Sell Technology —<br>
            We Help You <span class="gradient-text">Generate Revenue</span>
        </h1>
        <p class="hero-sub">
            Bytewave Digital Solutions helps businesses choose the right technology
            and helps tech companies grow faster through lead generation, pipeline
            building, and end-to-end sales execution.
        </p>
        <div class="hero-cta-group">
            <a target="_self" href="/Contact" class="btn-gradient">🚀 Get Qualified Leads</a>
            <a target="_self" href="/Contact" class="btn-outline">📞 Book Free Strategy Call</a>
        </div>
    </div>
    <div class="hero-right">
        <div class="logo-centerpiece">
            <div class="logo-wave-text">⚡</div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── TRUST STRIP ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="trust-strip">
    <div class="trust-items">
        <div class="trust-item"><span class="trust-icon">💻</span> Technology Reselling</div>
        <div class="trust-item"><span class="trust-icon">📈</span> Lead Generation</div>
        <div class="trust-item"><span class="trust-icon">🔥</span> Sales Execution</div>
        <div class="trust-item"><span class="trust-icon">📊</span> Data Targeting</div>
        <div class="trust-item"><span class="trust-icon">🎯</span> Pipeline Building</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─── ABOUT ───────────────────────────────────────────────────────────────────
st.markdown("""
<section class="about-section">
    <div class="about-content">
        <div class="about-icon">⚡</div>
        <div class="section-label">About Us</div>
        <h2 class="section-title">Your <span class="gradient-text">Revenue Growth</span> Partner</h2>
        <p class="about-body">
            Bytewave Digital Solutions is a <strong style="color:#93C5FD;">technology reseller and revenue acceleration partner</strong>.
            We bridge the gap between technology companies and businesses by not only recommending the right solutions
            but also ensuring they generate real business outcomes.
        </p>
        <div class="about-tags">
            <span class="about-tag">SaaS Companies</span>
            <span class="about-tag">IT Service Providers</span>
            <span class="about-tag">Enterprises</span>
            <span class="about-tag">B2B Businesses</span>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── SERVICES ────────────────────────────────────────────────────────────────
st.markdown("""
<section class="section section-darker">
    <div class="section-label">What We Do</div>
    <h2 class="section-title">End-to-End <span class="gradient-text">Revenue Services</span></h2>
    <p class="section-subtitle">From technology adoption to sales execution — we cover the full revenue cycle.</p>
    <div class="cards-grid">
        <div class="service-card">
            <span class="card-icon">💻</span>
            <div class="card-title">Technology Reselling</div>
            <div class="card-desc">We help businesses identify and adopt the right software solutions. We don't just sell — we advise, recommend, and enable adoption.</div>
            <ul class="card-bullets">
                <li>CRM Solutions</li>
                <li>Marketing Automation Tools</li>
                <li>HR &amp; Finance Software</li>
                <li>Cloud &amp; IT Solutions</li>
            </ul>
        </div>
        <div class="service-card">
            <span class="card-icon">📈</span>
            <div class="card-title">Lead Generation</div>
            <div class="card-desc">We help technology companies generate high-quality B2B leads using data-driven strategies. Focus on quality, not just volume.</div>
            <ul class="card-bullets">
                <li>Targeted Prospect Lists</li>
                <li>Email Campaigns</li>
                <li>LinkedIn Outreach</li>
                <li>Appointment Setting</li>
            </ul>
        </div>
        <div class="service-card">
            <span class="card-icon">🔥</span>
            <div class="card-title">Sales Execution</div>
            <div class="card-desc">We go beyond leads and help you close deals. We act as your extended sales team — revenue-focused execution every step.</div>
            <ul class="card-bullets">
                <li>Sales Pipeline Management</li>
                <li>Demo Coordination</li>
                <li>Deal Follow-ups</li>
                <li>Revenue Execution</li>
            </ul>
        </div>
        <div class="service-card">
            <span class="card-icon">📊</span>
            <div class="card-title">Data-Driven Targeting</div>
            <div class="card-desc">Using premium data sources, we help you identify decision-makers, build targeted campaigns, and improve conversion rates.</div>
            <ul class="card-bullets">
                <li>Decision-Maker Identification</li>
                <li>Targeted Campaigns</li>
                <li>Improved Conversion Rates</li>
                <li>Premium Data Sources</li>
            </ul>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── WHO WE WORK WITH ────────────────────────────────────────────────────────
st.markdown("""
<section class="section section-dark">
    <div class="section-label">Who We Work With</div>
    <h2 class="section-title">Built for <span class="gradient-text">Both Sides</span> of the Market</h2>
    <p class="section-subtitle">Whether you sell technology or buy it — we have a solution for you.</p>
    <div class="split-cards">
        <div class="split-card">
            <div class="split-card-icon">🧩</div>
            <div class="split-card-title">For Technology Companies</div>
            <ul class="split-card-list">
                <li>Increase pipeline significantly</li>
                <li>Enter new markets with confidence</li>
                <li>Close more deals, faster</li>
                <li>Outsource end-to-end sales</li>
            </ul>
        </div>
        <div class="split-card">
            <div class="split-card-icon">🏢</div>
            <div class="split-card-title">For Businesses (Buyers)</div>
            <ul class="split-card-list">
                <li>Get the right technology fit</li>
                <li>Save time on vendor research</li>
                <li>Improve operations efficiently</li>
                <li>Expert advisory at every step</li>
            </ul>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── WHY CHOOSE US ───────────────────────────────────────────────────────────
st.markdown("""
<section class="section section-darker">
    <div class="section-label">Why Choose Us</div>
    <h2 class="section-title">The <span class="gradient-text">Bytewave</span> Advantage</h2>
    <p class="section-subtitle">We combine technology expertise with proven sales execution to deliver measurable ROI.</p>
    <div class="why-grid">
        <div class="why-item">
            <span class="why-check">✔</span>
            <span class="why-text">End-to-end approach — Lead → Pipeline → Revenue</span>
        </div>
        <div class="why-item">
            <span class="why-check">✔</span>
            <span class="why-text">Strong B2B data targeting with premium sources</span>
        </div>
        <div class="why-item">
            <span class="why-check">✔</span>
            <span class="why-text">Technology + Sales expertise combined</span>
        </div>
        <div class="why-item">
            <span class="why-check">✔</span>
            <span class="why-text">Faster go-to-market execution</span>
        </div>
        <div class="why-item">
            <span class="why-check">✔</span>
            <span class="why-text">ROI-focused engagement model</span>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── INDUSTRIES ──────────────────────────────────────────────────────────────
st.markdown("""
<section class="section section-dark">
    <div class="section-label">Industries We Serve</div>
    <h2 class="section-title">Across <span class="gradient-text">Every Sector</span></h2>
    <p class="section-subtitle">We bring our revenue acceleration expertise to businesses across multiple industries.</p>
    <div class="industry-tags">
        <div class="industry-tag">🖥️ IT &amp; SaaS</div>
        <div class="industry-tag">🏭 Manufacturing</div>
        <div class="industry-tag">🏦 BFSI</div>
        <div class="industry-tag">🏥 Healthcare</div>
        <div class="industry-tag">🚀 Startups</div>
        <div class="industry-tag">🏢 Enterprises</div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── RESULTS SNAPSHOT ────────────────────────────────────────────────────────
st.markdown("""
<section class="section section-darker">
    <div class="section-label">Results You Can Expect</div>
    <h2 class="section-title">Numbers That <span class="gradient-text">Speak Louder</span></h2>
    <div class="metrics-grid">
        <div class="metric-card">
            <div class="metric-number">3–4x</div>
            <div class="metric-label">Pipeline Growth</div>
        </div>
        <div class="metric-card">
            <div class="metric-number">2x</div>
            <div class="metric-label">Conversion Rate</div>
        </div>
        <div class="metric-card">
            <div class="metric-number">50%</div>
            <div class="metric-label">Faster Deal Closures</div>
        </div>
        <div class="metric-card">
            <div class="metric-number">100%</div>
            <div class="metric-label">ROI-Focused</div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── CTA BANNER ──────────────────────────────────────────────────────────────
st.markdown("""
<section class="cta-banner">
    <h2 class="cta-title">Ready to Scale Your <span class="gradient-text">Revenue?</span></h2>
    <p class="cta-sub">Join businesses that are growing faster with Bytewave's proven revenue acceleration system.</p>
    <div class="cta-buttons">
        <a target="_self" href="/Contact" class="btn-gradient">🚀 Get Started Today</a>
        <a target="_self" href="/Contact" class="btn-outline">📞 Book a Strategy Call</a>
    </div>
</section>
""", unsafe_allow_html=True)

footer()
