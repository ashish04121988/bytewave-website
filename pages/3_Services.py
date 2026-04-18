import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import GLOBAL_CSS
from components import navbar, footer

st.set_page_config(
    page_title="Services — Bytewave Digital",
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
    <div class="section-label">How We Help</div>
    <h1 class="section-title">Services Built Around <span class="gradient-text">Your Growth</span></h1>
    <p class="section-subtitle">
        From technology advisory and software procurement to lead generation and sales execution &#8212;
        we cover every step of your growth journey.
    </p>
</div>
""", unsafe_allow_html=True)

# ─── CORE: IT SOFTWARE RESELLING ─────────────────────────────────────────────
st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section section-beige">
    <div class="section-label">Core Service</div>
    <h2 class="section-title" style="text-align:center;">IT Software Reselling <span class="gradient-text">(Core Focus)</span></h2>
    <p class="section-subtitle">
        We help businesses identify, procure, and implement the right software solutions
        aligned to their operational and growth needs.
    </p>
    <div class="cards-grid">
        <div class="service-card">
            <span class="card-icon">&#129517;</span>
            <div class="card-title">Technology Advisory</div>
            <div class="card-desc">We help you evaluate and compare solutions based on your business needs, ensuring you choose the right fit &#8212; not just a popular option.</div>
        </div>
        <div class="service-card">
            <span class="card-icon">&#128722;</span>
            <div class="card-title">Software Procurement</div>
            <div class="card-desc">We simplify the purchasing process by connecting you with the right vendors and the most favorable commercial options.</div>
        </div>
        <div class="service-card">
            <span class="card-icon">&#9878;&#65039;</span>
            <div class="card-title">Vendor Selection &amp; Comparison</div>
            <div class="card-desc">We cut through the noise and present only the most relevant solutions tailored to your use case, budget, and scale.</div>
        </div>
        <div class="service-card">
            <span class="card-icon">&#128176;</span>
            <div class="card-title">Commercial Optimization</div>
            <div class="card-desc">We help you get the best value &#8212; pricing, licensing, and packaging aligned to your specific needs and usage patterns.</div>
        </div>
        <div class="service-card">
            <span class="card-icon">&#127760;</span>
            <div class="card-title">Partner Ecosystem Access</div>
            <div class="card-desc">Leveraging insights and networks built from Fundoo Data, we provide access to a wide ecosystem of global technology providers through a single point of contact.</div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── CTA ─────────────────────────────────────────────────────────────────────
st.markdown("""
<section class="cta-banner">
    <h2 class="cta-title">Let's Simplify Your <span class="gradient-text">Technology Journey</span></h2>
    <p class="cta-sub">Every business is different. Let's talk and find the right technology solutions together.</p>
    <div class="cta-buttons">
        <a target="_self" href="/Contact" class="btn-gradient">&#128222; Book Strategy Call</a>
        <a target="_self" href="/Solutions" class="btn-outline">&#128269; Explore Solutions</a>
    </div>
</section>
""", unsafe_allow_html=True)

footer()
