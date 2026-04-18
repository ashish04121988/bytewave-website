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
story_left, story_right = st.columns([1.2, 0.8])

with story_left:
    st.markdown("""
    <div style="padding: 80px 60px 60px 60px; background: #FAF8F4;">
        <div class="section-label" style="text-align:left;">Our Origin</div>
        <h2 style="font-size:clamp(28px,3.5vw,42px); font-weight:800; letter-spacing:-1px; color:#1C1107; margin-bottom:24px; line-height:1.15; text-align:left;">
            How <span class="gradient-text">Bytewave Digital</span> Came to Be
        </h2>
        <p style="font-size:16px; color:#6B5E52; line-height:1.85; margin-bottom:20px;">
            Bytewave Digital was born from the legacy of <strong style="color:#E85D04;">Fundoo Data</strong> &#8212; where we helped organizations with deep corporate intelligence and business insights. Through these engagements, we worked closely with SMEs, mid-size companies, and large enterprises, gaining firsthand visibility into how technology decisions are made.
        </p>
        <p style="font-size:16px; color:#6B5E52; line-height:1.85; margin-bottom:20px;">
            We identified a consistent gap &#8212; <strong style="color:#1C1107;">organizations were overwhelmed with choices and struggled to find the right-fit technology solutions aligned to their business needs.</strong> Too many vendors. Too many tools. Too much noise. This insight led to the creation of Bytewave Digital.
        </p>
        <p style="font-size:16px; color:#6B5E52; line-height:1.85; margin-bottom:28px;">
            At Bytewave Digital, we simplify that journey. We work with organizations to identify, evaluate, and procure the right technology solutions &#8212; aligned to their business goals, not vendor agendas. No implementation. No bias. Just the right decision.
        </p>
        <div style="background:rgba(232,93,4,0.06); border:1px solid rgba(232,93,4,0.2); border-left:4px solid #E85D04; border-radius:0 12px 12px 0; padding:24px 28px; margin-bottom:32px;">
            <p style="font-size:15px; color:#4A3728; line-height:1.7; margin:0; font-style:italic;">
                "We don't build or implement &#8212; we help you <strong style="color:#E85D04;">choose and buy right</strong>."
            </p>
        </div>
        <div style="display:flex; gap:16px; flex-wrap:wrap;">
            <a target="_self" href="/Contact" class="btn-gradient" style="text-decoration:none;">&#128197; Schedule a Consultation</a>
            <a target="_self" href="/Solutions" class="btn-outline" style="text-decoration:none;">&#128269; Explore Solutions</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with story_right:
    st.markdown("""
    <div style="padding: 80px 60px 60px 0; background: #FAF8F4;">
        <div class="about-img" style="height:480px; position:relative;">
            <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1200&q=90"
                 style="width:100%; height:100%; object-fit:cover; border-radius:20px;" alt="Bytewave Digital Team" />
            <div class="about-img-badge">
                <div class="about-img-badge-num">Est. 2024</div>
                <div class="about-img-badge-text">Noida, India</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ─── MISSION / VISION ────────────────────────────────────────────────────────
st.markdown("""
<div class="gradient-divider"></div>
<section class="section section-white">
    <div class="section-label">Who We Are</div>
    <h2 class="section-title">A <span class="gradient-text">Vendor-Neutral</span> Technology Advisor</h2>
    <div class="split-cards">
        <div class="split-card">
            <div class="split-card-icon">&#127919;</div>
            <div class="split-card-title">Our Mission</div>
            <p style="font-size:15px; color:#6B5E52; line-height:1.7;">
                To empower organizations to make smarter technology investments through clarity, choice, and confidence.
                We cut through vendor noise so our clients can focus on outcomes, not options.
            </p>
        </div>
        <div class="split-card">
            <div class="split-card-icon">&#127760;</div>
            <div class="split-card-title">Our Vision</div>
            <p style="font-size:15px; color:#6B5E52; line-height:1.7;">
                To become a trusted global partner for technology buying decisions &#8212; helping businesses at every
                stage scale through the right software without guesswork or noise.
            </p>
        </div>
    </div>
</section>
<div class="gradient-divider"></div>
""", unsafe_allow_html=True)

# ─── OUR APPROACH ────────────────────────────────────────────────────────────
st.markdown("""
<section class="section section-beige">
    <div class="section-label">Our Approach</div>
    <h2 class="section-title">Understand &#8594; Curate &#8594; <span class="gradient-text">Enable</span></h2>
    <p class="section-subtitle">A simple, transparent process designed to deliver the right technology decision &#8212; every time.</p>
</section>
""", unsafe_allow_html=True)

ap_c1, ap_c2, ap_c3 = st.columns(3)

with ap_c1:
    st.markdown("""
    <div style="padding: 0 20px 60px; background: #FAF8F4;">
        <div class="feature-card">
            <div class="feature-num">01</div>
            <div class="feature-icon">&#128269;</div>
            <div class="feature-title">Understand</div>
            <div class="feature-desc">We analyze your business goals, operational needs, and current technology landscape to build a comprehensive picture of what you truly need &#8212; without assumptions.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with ap_c2:
    st.markdown("""
    <div style="padding: 0 20px 60px; background: #FAF8F4;">
        <div class="feature-card">
            <div class="feature-num">02</div>
            <div class="feature-icon">&#129513;</div>
            <div class="feature-title">Curate</div>
            <div class="feature-desc">We shortlist the most relevant technology options from our global ecosystem &#8212; cutting through thousands of tools to present only the ones that truly fit your needs.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with ap_c3:
    st.markdown("""
    <div style="padding: 0 20px 60px; background: #FAF8F4;">
        <div class="feature-card">
            <div class="feature-num">03</div>
            <div class="feature-icon">&#128640;</div>
            <div class="feature-title">Enable</div>
            <div class="feature-desc">We help you make an informed decision and connect you with the right vendors &#8212; guiding procurement, negotiations, and onboarding so you buy right the first time.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ─── WHY CHOOSE US ───────────────────────────────────────────────────────────
st.markdown("""
<div class="gradient-divider"></div>
<section class="section section-white">
    <div class="section-label">Why Us</div>
    <h2 class="section-title">What Makes Us <span class="gradient-text">Different</span></h2>
    <div class="why-grid">
        <div class="why-item">
            <span class="why-check">&#10004;</span>
            <span class="why-text">Built on the trusted legacy of Fundoo Data</span>
        </div>
        <div class="why-item">
            <span class="why-check">&#10004;</span>
            <span class="why-text">Vendor-neutral recommendations &#8212; we advise, not push</span>
        </div>
        <div class="why-item">
            <span class="why-check">&#10004;</span>
            <span class="why-text">Strong global partner ecosystem across categories</span>
        </div>
        <div class="why-item">
            <span class="why-check">&#10004;</span>
            <span class="why-text">Simplified technology buying experience</span>
        </div>
        <div class="why-item">
            <span class="why-check">&#10004;</span>
            <span class="why-text">Faster decision-making, significantly less noise</span>
        </div>
        <div class="why-item">
            <span class="why-check">&#10004;</span>
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
        <a target="_self" href="/Contact" class="btn-gradient">&#128197; Schedule a Consultation</a>
        <a target="_self" href="/Solutions" class="btn-outline">&#128269; Explore Solutions</a>
    </div>
</section>
""", unsafe_allow_html=True)

footer()
