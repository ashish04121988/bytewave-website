import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import GLOBAL_CSS
from components import navbar, footer

st.set_page_config(
    page_title="Services — Bytewave Digital Solutions",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
navbar("Services")

# ─── PAGE HEADER ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <div class="page-header-watermark">SERVICES</div>
    <div class="section-label">What We Offer</div>
    <h1 class="section-title">Complete <span class="gradient-text">Revenue Services</span></h1>
    <p class="section-subtitle">
        From helping businesses choose the right technology to helping SaaS companies close more deals —
        we cover every step of the revenue cycle.
    </p>
</div>
""", unsafe_allow_html=True)

# ─── SERVICE 1: TECHNOLOGY RESELLING ─────────────────────────────────────────
st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)

st.markdown("""
<section class="section section-dark">
    <div class="service-detail">
        <div class="service-detail-icon-block">💻</div>
        <div class="service-detail-content">
            <div class="section-label" style="text-align:left;">Service 01</div>
            <h2 class="service-detail-title">Technology Reselling</h2>
            <p class="service-detail-desc">
                We help businesses identify and adopt the right software solutions based on their unique needs.
                We don't just sell — we advise, recommend, and enable full adoption to ensure real business value.
            </p>
            <ul class="service-detail-list">
                <li>CRM Solutions</li>
                <li>Marketing Automation Tools</li>
                <li>HR &amp; Finance Software</li>
                <li>Cloud &amp; IT Solutions</li>
                <li>Expert advisory included</li>
                <li>Post-adoption support</li>
            </ul>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── SERVICE 2: LEAD GENERATION ──────────────────────────────────────────────
st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)

st.markdown("""
<section class="section section-darker">
    <div class="service-detail reverse">
        <div class="service-detail-icon-block">📈</div>
        <div class="service-detail-content">
            <div class="section-label" style="text-align:left;">Service 02</div>
            <h2 class="service-detail-title">Lead Generation Services</h2>
            <p class="service-detail-desc">
                We help technology companies generate high-quality B2B leads using data-driven strategies.
                Our focus is always on quality leads that convert — not just volume.
            </p>
            <ul class="service-detail-list">
                <li>Targeted prospect lists</li>
                <li>Email campaigns</li>
                <li>LinkedIn outreach</li>
                <li>Appointment setting</li>
                <li>Quality over volume</li>
                <li>Detailed reporting</li>
            </ul>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── SERVICE 3: SALES EXECUTION ──────────────────────────────────────────────
st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)

st.markdown("""
<section class="section section-dark">
    <div class="service-detail">
        <div class="service-detail-icon-block">🔥</div>
        <div class="service-detail-content">
            <div class="section-label" style="text-align:left;">Service 03</div>
            <h2 class="service-detail-title">Sales Execution (Closing Support)</h2>
            <p class="service-detail-desc">
                We go beyond leads and help you close deals. Think of us as your extended sales team —
                focused entirely on revenue outcomes and faster deal closures.
            </p>
            <ul class="service-detail-list">
                <li>Sales pipeline management</li>
                <li>Demo coordination</li>
                <li>Deal follow-ups</li>
                <li>Revenue-focused execution</li>
                <li>Extended sales team model</li>
                <li>Performance tracking</li>
            </ul>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── SERVICE 4: DATA TARGETING ────────────────────────────────────────────────
st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)

st.markdown("""
<section class="section section-darker">
    <div class="service-detail reverse">
        <div class="service-detail-icon-block">📊</div>
        <div class="service-detail-content">
            <div class="section-label" style="text-align:left;">Service 04</div>
            <h2 class="service-detail-title">Data-Driven Targeting</h2>
            <p class="service-detail-desc">
                Using premium data sources like Fundoodata, we help you identify the exact decision-makers
                in your target market, build precision campaigns, and dramatically improve conversion rates.
            </p>
            <ul class="service-detail-list">
                <li>Decision-maker identification</li>
                <li>Targeted campaigns</li>
                <li>Improved conversion rates</li>
                <li>Premium data sources</li>
                <li>Market segmentation</li>
                <li>Campaign analytics</li>
            </ul>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── CTA ─────────────────────────────────────────────────────────────────────
st.markdown("""
<section class="cta-banner">
    <h2 class="cta-title">Ready to <span class="gradient-text">Get Started?</span></h2>
    <p class="cta-sub">Tell us about your business and we'll recommend the right service mix for maximum ROI.</p>
    <div class="cta-buttons">
        <a target="_self" href="/Contact" class="btn-gradient">🚀 Book a Free Consultation</a>
        <a target="_self" href="/Pricing" class="btn-outline">💰 View Pricing</a>
    </div>
</section>
""", unsafe_allow_html=True)

footer()
