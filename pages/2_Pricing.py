import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import GLOBAL_CSS
from components import navbar, footer

st.set_page_config(
    page_title="Pricing — Bytewave Digital Solutions",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
navbar("Pricing")

# ─── PAGE HEADER ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <div class="page-header-watermark">PRICING</div>
    <div style="font-size:44px; margin-bottom:16px; filter: drop-shadow(0 0 12px rgba(37,99,235,0.5));">⚡</div>
    <div class="section-label">Flexible Pricing</div>
    <h1 class="section-title">Built Around <span class="gradient-text">Your Growth</span></h1>
    <p class="section-subtitle">
        No one-size-fits-all pricing. We craft engagement models tailored to your business goals and growth stage.
    </p>
</div>
""", unsafe_allow_html=True)

# ─── CORE MESSAGE ────────────────────────────────────────────────────────────
st.markdown("""
<section class="section section-darker" style="text-align:center;">
    <div style="max-width:700px; margin:0 auto; background:rgba(13,35,71,0.6); border:1px solid rgba(37,99,235,0.2); border-radius:20px; padding:48px 40px; position:relative; overflow:hidden;">
        <div style="position:absolute; top:0; left:0; right:0; height:3px; background:linear-gradient(135deg,#2563EB,#7C3AED,#F97316);"></div>
        <div style="font-size:48px; margin-bottom:16px;">🎯</div>
        <h2 style="font-size:28px; font-weight:800; color:#F1F5F9; margin-bottom:16px; letter-spacing:-0.5px;">No One-Size-Fits-All Pricing</h2>
        <p style="font-size:16px; color:#94A3B8; line-height:1.7;">
            Every business has different revenue goals, market sizes, and sales cycles.
            That's why we build custom pricing plans based on what you actually need —
            not a package you have to squeeze into.
        </p>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── WHAT YOU GET ────────────────────────────────────────────────────────────
st.markdown("""
<section class="section section-dark">
    <div class="section-label">What You Get</div>
    <h2 class="section-title">Every Plan <span class="gradient-text">Includes</span></h2>
    <p class="section-subtitle">Core capabilities available across all our engagement models.</p>
    <div class="cards-grid">
        <div class="service-card">
            <span class="card-icon">💻</span>
            <div class="card-title">Technology Reselling</div>
            <div class="card-desc">Access to our curated technology stack with expert advisory and onboarding support.</div>
        </div>
        <div class="service-card">
            <span class="card-icon">📈</span>
            <div class="card-title">Lead Generation</div>
            <div class="card-desc">High-quality B2B leads using data-driven targeting from premium sources.</div>
        </div>
        <div class="service-card">
            <span class="card-icon">🔥</span>
            <div class="card-title">Sales Execution</div>
            <div class="card-desc">End-to-end sales support from pipeline building to deal closure.</div>
        </div>
        <div class="service-card">
            <span class="card-icon">📊</span>
            <div class="card-title">Data Targeting</div>
            <div class="card-desc">Precision targeting using Fundoodata and other premium data sources.</div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── ENGAGEMENT MODELS ───────────────────────────────────────────────────────
st.markdown("""
<section class="section section-darker">
    <div class="section-label">Engagement Models</div>
    <h2 class="section-title">Choose Your <span class="gradient-text">Growth Path</span></h2>
    <p class="section-subtitle">Select the engagement model that fits where you are today — upgrade anytime as you grow.</p>
    <div class="pricing-grid">

        <div class="pricing-card">
            <div class="pricing-card-icon">📈</div>
            <div class="pricing-card-title">Lead Generation Only</div>
            <div class="pricing-card-subtitle">For companies with an existing sales team</div>
            <ul class="pricing-features">
                <li>Targeted B2B prospect lists</li>
                <li>Email outreach campaigns</li>
                <li>LinkedIn lead generation</li>
                <li>Appointment setting</li>
                <li>Weekly lead reports</li>
                <li>Dedicated account manager</li>
            </ul>
            <a href="/Contact" class="pricing-cta secondary">Get Custom Quote →</a>
        </div>

        <div class="pricing-card featured">
            <div class="pricing-card-icon">🚀</div>
            <div class="pricing-card-title">Lead + Sales Support</div>
            <div class="pricing-card-subtitle">For companies wanting full pipeline support</div>
            <ul class="pricing-features">
                <li>Everything in Lead Generation</li>
                <li>Sales pipeline management</li>
                <li>Demo scheduling & coordination</li>
                <li>Deal follow-up sequences</li>
                <li>Bi-weekly strategy calls</li>
                <li>CRM integration support</li>
                <li>Performance analytics</li>
            </ul>
            <a href="/Contact" class="pricing-cta primary">Get Custom Quote →</a>
        </div>

        <div class="pricing-card">
            <div class="pricing-card-icon">🏆</div>
            <div class="pricing-card-title">End-to-End Revenue Partner</div>
            <div class="pricing-card-subtitle">For companies wanting complete revenue execution</div>
            <ul class="pricing-features">
                <li>Everything in Lead + Sales</li>
                <li>Technology reselling advisory</li>
                <li>Full sales team extension</li>
                <li>Market entry strategy</li>
                <li>Weekly executive reports</li>
                <li>Priority support</li>
                <li>Custom data targeting</li>
            </ul>
            <a href="/Contact" class="pricing-cta secondary">Get Custom Quote →</a>
        </div>

    </div>
</section>
""", unsafe_allow_html=True)

# ─── TRUST BADGES ────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; padding:40px 60px; background:#0B1F3A;">
    <div class="trust-badges">
        <div class="trust-badge">
            <span class="trust-badge-icon">✔</span>
            Transparent Pricing
        </div>
        <div class="trust-badge">
            <span class="trust-badge-icon">✔</span>
            ROI-Focused
        </div>
        <div class="trust-badge">
            <span class="trust-badge-icon">✔</span>
            Scalable Plans
        </div>
        <div class="trust-badge">
            <span class="trust-badge-icon">✔</span>
            No Lock-In Contracts
        </div>
        <div class="trust-badge">
            <span class="trust-badge-icon">✔</span>
            Flexible Engagement
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─── CTA ─────────────────────────────────────────────────────────────────────
st.markdown("""
<section class="cta-banner">
    <h2 class="cta-title">Let's Build a Plan That <span class="gradient-text">Works for You</span></h2>
    <p class="cta-sub">Every business is different. Let's talk and design a custom revenue acceleration plan together.</p>
    <div class="cta-buttons">
        <a href="/Contact" class="btn-gradient">📞 Book Strategy Call</a>
        <a href="/Contact" class="btn-outline">💬 Talk to Our Team</a>
    </div>
</section>
""", unsafe_allow_html=True)

footer()
