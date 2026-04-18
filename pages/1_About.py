import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import GLOBAL_CSS
from components import navbar, footer

st.set_page_config(
    page_title="About — Bytewave Digital",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
navbar("About")

# ─── PAGE HEADER ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <div class="page-header-watermark">ABOUT</div>
    <div class="section-label">Our Story</div>
    <h1 class="section-title">Born from the Legacy of <span class="gradient-text">Fundoo Data</span></h1>
    <p class="section-subtitle">
        A vendor-neutral IT software reseller and technology advisor, focused on helping organizations
        identify, evaluate, and procure the right technology solutions.
    </p>
</div>
""", unsafe_allow_html=True)

# ─── OUR STORY ───────────────────────────────────────────────────────────────
st.markdown("""
<section class="section section-darker">
    <div style="max-width:800px; margin:0 auto;">
        <div class="section-label" style="text-align:left;">Our Origin</div>
        <h2 class="section-title" style="text-align:left;">How <span class="gradient-text">Bytewave Digital</span> Came to Be</h2>
        <p style="font-size:17px; color:#94A3B8; line-height:1.85; margin-bottom:24px;">
            Bytewave Digital was born from the legacy of <strong style="color:#93C5FD;">Fundoo Data</strong> — where we helped
            organizations with deep corporate intelligence and business insights.
        </p>
        <p style="font-size:17px; color:#94A3B8; line-height:1.85; margin-bottom:24px;">
            Through these engagements, we worked closely with SMEs, mid-size companies, and large enterprises,
            gaining firsthand visibility into how technology decisions are made across industries.
        </p>
        <p style="font-size:17px; color:#94A3B8; line-height:1.85; margin-bottom:32px;">
            We identified a consistent gap — <strong style="color:#E2E8F0;">organizations were overwhelmed with choices and struggled to find
            the right-fit technology solutions aligned to their business needs.</strong>
            This insight led to the creation of Bytewave Digital.
        </p>
        <div style="background:rgba(37,99,235,0.08); border:1px solid rgba(37,99,235,0.2); border-left:4px solid #2563EB; border-radius:0 12px 12px 0; padding:24px 28px;">
            <p style="font-size:16px; color:#CBD5E1; line-height:1.7; margin:0; font-style:italic;">
                "We don't build or implement — we help you <strong style="color:#93C5FD;">choose and buy right</strong>."
            </p>
        </div>
    </div>
</section>

<div class="gradient-divider"></div>
""", unsafe_allow_html=True)

# ─── WHO WE ARE ──────────────────────────────────────────────────────────────
st.markdown("""
<section class="section section-dark">
    <div class="section-label">Who We Are</div>
    <h2 class="section-title">A <span class="gradient-text">Vendor-Neutral</span> Technology Advisor</h2>
    <div class="split-cards">
        <div class="split-card">
            <div class="split-card-icon">🎯</div>
            <div class="split-card-title">Our Mission</div>
            <p style="font-size:15px; color:#94A3B8; line-height:1.7;">
                To empower organizations to make smarter technology investments through clarity, choice, and confidence.
            </p>
        </div>
        <div class="split-card">
            <div class="split-card-icon">🌐</div>
            <div class="split-card-title">Our Vision</div>
            <p style="font-size:15px; color:#94A3B8; line-height:1.7;">
                To become a trusted global partner for technology buying decisions — helping businesses scale through the right software.
            </p>
        </div>
    </div>
</section>

<div class="gradient-divider"></div>
""", unsafe_allow_html=True)

# ─── OUR APPROACH ────────────────────────────────────────────────────────────
st.markdown("""
<section class="section section-darker">
    <div class="section-label">Our Approach</div>
    <h2 class="section-title">Understand → Curate → <span class="gradient-text">Enable</span></h2>
    <p class="section-subtitle">A simple, transparent process designed to deliver the right technology decision — every time.</p>
    <div class="process-steps" style="max-width:700px; margin:0 auto;">
        <div class="process-step" style="width:200px;">
            <div class="step-number">1</div>
            <div class="step-title">Understand</div>
            <div class="step-desc">We analyze your business goals, operational needs, and current technology landscape.</div>
        </div>
        <div class="step-connector" style="width:80px;"></div>
        <div class="process-step" style="width:200px;">
            <div class="step-number">2</div>
            <div class="step-title">Curate</div>
            <div class="step-desc">We shortlist the most relevant technology options from our global ecosystem.</div>
        </div>
        <div class="step-connector" style="width:80px;"></div>
        <div class="process-step" style="width:200px;">
            <div class="step-number">3</div>
            <div class="step-title">Enable</div>
            <div class="step-desc">We help you make an informed decision and connect you with the right vendors.</div>
        </div>
    </div>
</section>

<div class="gradient-divider"></div>
""", unsafe_allow_html=True)

# ─── WHY CHOOSE US ───────────────────────────────────────────────────────────
st.markdown("""
<section class="section section-dark">
    <div class="section-label">Why Us</div>
    <h2 class="section-title">What Makes Us <span class="gradient-text">Different</span></h2>
    <div class="why-grid">
        <div class="why-item">
            <span class="why-check">✔</span>
            <span class="why-text">Built on the trusted legacy of Fundoo Data</span>
        </div>
        <div class="why-item">
            <span class="why-check">✔</span>
            <span class="why-text">Vendor-neutral recommendations — we advise, not push</span>
        </div>
        <div class="why-item">
            <span class="why-check">✔</span>
            <span class="why-text">Strong global partner ecosystem across categories</span>
        </div>
        <div class="why-item">
            <span class="why-check">✔</span>
            <span class="why-text">Simplified technology buying experience</span>
        </div>
        <div class="why-item">
            <span class="why-check">✔</span>
            <span class="why-text">Faster decision-making, less noise</span>
        </div>
        <div class="why-item">
            <span class="why-check">✔</span>
            <span class="why-text">Outcome-driven approach aligned to your business goals</span>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── CTA ─────────────────────────────────────────────────────────────────────
st.markdown("""
<section class="cta-banner">
    <h2 class="cta-title">Ready to Simplify Your <span class="gradient-text">Technology Journey?</span></h2>
    <p class="cta-sub">Let's talk about your business needs and find the right technology fit for you.</p>
    <div class="cta-buttons">
        <a target="_self" href="/Contact" class="btn-gradient">📅 Schedule a Consultation</a>
        <a target="_self" href="/Solutions" class="btn-outline">🔍 Explore Solutions</a>
    </div>
</section>
""", unsafe_allow_html=True)

footer()
