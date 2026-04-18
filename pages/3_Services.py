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
        From technology advisory and software procurement to lead generation and sales execution —
        we cover every step of your growth journey.
    </p>
</div>
""", unsafe_allow_html=True)

# ─── CORE: IT SOFTWARE RESELLING ─────────────────────────────────────────────
st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section section-dark">
    <div class="section-label">Core Service</div>
    <h2 class="section-title" style="text-align:center;">IT Software Reselling <span class="gradient-text">(Core Focus)</span></h2>
    <p class="section-subtitle">
        We help businesses identify, procure, and implement the right software solutions
        aligned to their operational and growth needs.
    </p>
    <div class="cards-grid">
        <div class="service-card">
            <span class="card-icon">🧭</span>
            <div class="card-title">Technology Advisory</div>
            <div class="card-desc">We help you evaluate and compare solutions based on your business needs, ensuring you choose the right fit — not just a popular option.</div>
        </div>
        <div class="service-card">
            <span class="card-icon">🛒</span>
            <div class="card-title">Software Procurement</div>
            <div class="card-desc">We simplify the purchasing process by connecting you with the right vendors and the most favorable commercial options.</div>
        </div>
        <div class="service-card">
            <span class="card-icon">⚖️</span>
            <div class="card-title">Vendor Selection &amp; Comparison</div>
            <div class="card-desc">We cut through the noise and present only the most relevant solutions tailored to your use case, budget, and scale.</div>
        </div>
        <div class="service-card">
            <span class="card-icon">💰</span>
            <div class="card-title">Commercial Optimization</div>
            <div class="card-desc">We help you get the best value — pricing, licensing, and packaging aligned to your specific needs and usage patterns.</div>
        </div>
        <div class="service-card">
            <span class="card-icon">🌐</span>
            <div class="card-title">Partner Ecosystem Access</div>
            <div class="card-desc">Leveraging insights built from Fundoo Data, we provide access to a wide network of leading global technology providers through a single point of contact.</div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── VALUE-ADDED: SALES & REVENUE ────────────────────────────────────────────
st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section section-darker">
    <div class="section-label">Value-Added Services</div>
    <h2 class="section-title">Sales &amp; <span class="gradient-text">Revenue Services</span></h2>
    <p class="section-subtitle">
        In addition to software reselling, we provide end-to-end sales execution support
        to help technology companies accelerate revenue growth.
    </p>
    <div class="cards-grid">
        <div class="service-card">
            <span class="card-icon">📈</span>
            <div class="card-title">Lead Generation</div>
            <div class="card-desc">Build a targeted, high-quality pipeline of prospects using data-driven strategies.</div>
            <ul class="card-bullets">
                <li>Target account identification</li>
                <li>Verified B2B data sourcing</li>
                <li>Account-based targeting</li>
            </ul>
        </div>
        <div class="service-card">
            <span class="card-icon">📞</span>
            <div class="card-title">SDR Services</div>
            <div class="card-desc">We act as your front-line sales engine, handling outreach and appointment setting at scale.</div>
            <ul class="card-bullets">
                <li>Cold outreach (Email, LinkedIn, Calls)</li>
                <li>Appointment setting</li>
                <li>Pipeline building</li>
            </ul>
        </div>
        <div class="service-card">
            <span class="card-icon">🔥</span>
            <div class="card-title">Sales Execution</div>
            <div class="card-desc">We help move opportunities forward and convert pipeline into closed deals.</div>
            <ul class="card-bullets">
                <li>Demo support</li>
                <li>Proposal creation</li>
                <li>Objection handling</li>
            </ul>
        </div>
        <div class="service-card">
            <span class="card-icon">🏆</span>
            <div class="card-title">Deal Closure Support</div>
            <div class="card-desc">We help convert pipeline into revenue through negotiation and closing strategy.</div>
            <ul class="card-bullets">
                <li>Negotiation support</li>
                <li>Closing strategy</li>
                <li>Revenue conversion</li>
            </ul>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── ENGAGEMENT MODELS ───────────────────────────────────────────────────────
st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section section-dark">
    <div class="section-label">Engagement Models</div>
    <h2 class="section-title">Flexible Models Built for <span class="gradient-text">Your Needs</span></h2>
    <p class="section-subtitle">We offer flexible engagement models based on your business goals and growth stage.</p>
    <div class="pricing-grid">
        <div class="pricing-card">
            <div class="pricing-card-icon">🟢</div>
            <div class="pricing-card-title">Reseller Model</div>
            <div class="pricing-card-subtitle">Primary engagement — technology first</div>
            <ul class="pricing-features">
                <li>Software procurement & licensing</li>
                <li>Implementation support</li>
                <li>Vendor selection & comparison</li>
                <li>Commercial optimization</li>
                <li>Partner ecosystem access</li>
            </ul>
            <a target="_self" href="/Contact" class="pricing-cta secondary">Get Started →</a>
        </div>
        <div class="pricing-card featured">
            <div class="pricing-card-icon">🔴</div>
            <div class="pricing-card-title">Hybrid Model</div>
            <div class="pricing-card-subtitle">Technology + Sales = End-to-End Growth</div>
            <ul class="pricing-features">
                <li>Everything in Reseller Model</li>
                <li>Lead generation</li>
                <li>SDR services</li>
                <li>Sales execution</li>
                <li>Deal closure support</li>
                <li>Revenue acceleration</li>
            </ul>
            <a target="_self" href="/Contact" class="pricing-cta primary">Get Started →</a>
        </div>
        <div class="pricing-card">
            <div class="pricing-card-icon">🔵</div>
            <div class="pricing-card-title">Service Model</div>
            <div class="pricing-card-subtitle">Sales execution focused</div>
            <ul class="pricing-features">
                <li>Lead generation campaigns</li>
                <li>SDR & outreach services</li>
                <li>Sales pipeline management</li>
                <li>Deal closure support</li>
                <li>Revenue conversion</li>
            </ul>
            <a target="_self" href="/Contact" class="pricing-cta secondary">Get Started →</a>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── CTA ─────────────────────────────────────────────────────────────────────
st.markdown("""
<section class="cta-banner">
    <h2 class="cta-title">Let's Build a Plan That <span class="gradient-text">Works for You</span></h2>
    <p class="cta-sub">Every business is different. Let's talk and design the right engagement model together.</p>
    <div class="cta-buttons">
        <a target="_self" href="/Contact" class="btn-gradient">📞 Book Strategy Call</a>
        <a target="_self" href="/Solutions" class="btn-outline">🔍 Explore Solutions</a>
    </div>
</section>
""", unsafe_allow_html=True)

footer()
