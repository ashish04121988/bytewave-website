import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import GLOBAL_CSS
from components import navbar, footer

st.set_page_config(
    page_title="Results — Bytewave Digital Solutions",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
navbar("Results")

# ─── PAGE HEADER ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <div class="page-header-watermark">RESULTS</div>
    <div class="section-label">Proven Impact</div>
    <h1 class="section-title">Results That <span class="gradient-text">Speak for Themselves</span></h1>
    <p class="section-subtitle">
        We measure our success by your revenue growth. Here's what clients can expect when working with Bytewave.
    </p>
</div>
""", unsafe_allow_html=True)

# ─── KEY METRICS ─────────────────────────────────────────────────────────────
st.markdown("""
<section class="section section-darker">
    <div class="section-label">Key Metrics</div>
    <h2 class="section-title">Numbers That <span class="gradient-text">Define Success</span></h2>
    <div class="metrics-grid" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));">
        <div class="metric-card">
            <div class="metric-number">3–4x</div>
            <div class="metric-label">Pipeline Growth</div>
        </div>
        <div class="metric-card">
            <div class="metric-number">2x</div>
            <div class="metric-label">Better Lead Quality</div>
        </div>
        <div class="metric-card">
            <div class="metric-number">50%</div>
            <div class="metric-label">Faster Closures</div>
        </div>
        <div class="metric-card">
            <div class="metric-number">40%</div>
            <div class="metric-label">Higher Conversion Rate</div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── WHAT CLIENTS SAY ─────────────────────────────────────────────────────────
st.markdown("""
<section class="section section-dark">
    <div class="section-label">Client Outcomes</div>
    <h2 class="section-title">What You Can <span class="gradient-text">Expect</span></h2>
    <p class="section-subtitle">Real outcomes our clients achieve after partnering with Bytewave.</p>
    <div class="cards-grid">
        <div class="service-card" style="background:rgba(13,35,71,0.9);">
            <span class="card-icon">🚀</span>
            <div class="card-title">Pipeline Growth</div>
            <div class="card-desc">Businesses typically see 3–4x pipeline growth within 90 days of engagement, driven by precision targeting and consistent outreach.</div>
        </div>
        <div class="service-card" style="background:rgba(13,35,71,0.9);">
            <span class="card-icon">🎯</span>
            <div class="card-title">Better Lead Quality</div>
            <div class="card-desc">Our data-driven targeting means leads that actually match your ICP — resulting in 2x better quality and higher engagement rates.</div>
        </div>
        <div class="service-card" style="background:rgba(13,35,71,0.9);">
            <span class="card-icon">⚡</span>
            <div class="card-title">Faster Deal Closures</div>
            <div class="card-desc">With active pipeline management and sales support, clients see up to 50% reduction in their average deal cycle time.</div>
        </div>
        <div class="service-card" style="background:rgba(13,35,71,0.9);">
            <span class="card-icon">📊</span>
            <div class="card-title">Higher Conversion Rates</div>
            <div class="card-desc">Better lead quality combined with structured follow-ups leads to significantly higher conversion rates across all funnel stages.</div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── TESTIMONIALS ────────────────────────────────────────────────────────────
st.markdown("""
<section class="section section-darker">
    <div class="section-label">Testimonials</div>
    <h2 class="section-title">What Our <span class="gradient-text">Clients Say</span></h2>
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:24px; max-width:1000px; margin:0 auto;">

        <div style="background:rgba(13,35,71,0.7); border:1px solid rgba(37,99,235,0.2); border-radius:16px; padding:32px; backdrop-filter:blur(10px); transition:all 0.3s;">
            <div style="color:#F97316; font-size:24px; margin-bottom:16px;">★★★★★</div>
            <p style="font-size:15px; color:#94A3B8; line-height:1.7; margin-bottom:24px; font-style:italic;">
                "Bytewave transformed our sales pipeline completely. Within 3 months, we had 4x more qualified leads flowing in and our conversion rates jumped significantly."
            </p>
            <div style="display:flex; align-items:center; gap:12px;">
                <div style="width:44px; height:44px; border-radius:50%; background:linear-gradient(135deg,#2563EB,#7C3AED); display:flex; align-items:center; justify-content:center; font-weight:700; color:white; font-size:16px;">R</div>
                <div>
                    <div style="font-size:14px; font-weight:700; color:#F1F5F9;">Rahul Sharma</div>
                    <div style="font-size:12px; color:#64748B;">CEO, TechVenture India</div>
                </div>
            </div>
        </div>

        <div style="background:rgba(13,35,71,0.7); border:1px solid rgba(124,58,237,0.2); border-radius:16px; padding:32px; backdrop-filter:blur(10px);">
            <div style="color:#F97316; font-size:24px; margin-bottom:16px;">★★★★★</div>
            <p style="font-size:15px; color:#94A3B8; line-height:1.7; margin-bottom:24px; font-style:italic;">
                "The quality of leads we get from Bytewave is unmatched. They truly understand B2B targeting and the data-driven approach makes all the difference."
            </p>
            <div style="display:flex; align-items:center; gap:12px;">
                <div style="width:44px; height:44px; border-radius:50%; background:linear-gradient(135deg,#7C3AED,#F97316); display:flex; align-items:center; justify-content:center; font-weight:700; color:white; font-size:16px;">P</div>
                <div>
                    <div style="font-size:14px; font-weight:700; color:#F1F5F9;">Priya Menon</div>
                    <div style="font-size:12px; color:#64748B;">VP Sales, CloudSoft Solutions</div>
                </div>
            </div>
        </div>

        <div style="background:rgba(13,35,71,0.7); border:1px solid rgba(249,115,22,0.2); border-radius:16px; padding:32px; backdrop-filter:blur(10px);">
            <div style="color:#F97316; font-size:24px; margin-bottom:16px;">★★★★★</div>
            <p style="font-size:15px; color:#94A3B8; line-height:1.7; margin-bottom:24px; font-style:italic;">
                "We chose Bytewave to help us enter the Indian market. Their local knowledge combined with systematic lead gen gave us a running start we couldn't have achieved alone."
            </p>
            <div style="display:flex; align-items:center; gap:12px;">
                <div style="width:44px; height:44px; border-radius:50%; background:linear-gradient(135deg,#F97316,#2563EB); display:flex; align-items:center; justify-content:center; font-weight:700; color:white; font-size:16px;">A</div>
                <div>
                    <div style="font-size:14px; font-weight:700; color:#F1F5F9;">Amit Desai</div>
                    <div style="font-size:12px; color:#64748B;">Director, FinTech Innovations</div>
                </div>
            </div>
        </div>

    </div>
</section>
""", unsafe_allow_html=True)

# ─── INDUSTRIES ──────────────────────────────────────────────────────────────
st.markdown("""
<section class="section section-dark">
    <div class="section-label">Industries Served</div>
    <h2 class="section-title">Delivering Results <span class="gradient-text">Across Sectors</span></h2>
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

# ─── CTA ─────────────────────────────────────────────────────────────────────
st.markdown("""
<section class="cta-banner">
    <h2 class="cta-title">Ready to See <span class="gradient-text">These Results?</span></h2>
    <p class="cta-sub">Join businesses growing their revenue with Bytewave's proven system.</p>
    <div class="cta-buttons">
        <a href="/Contact" class="btn-gradient">🚀 Start Growing Today</a>
        <a href="/Process" class="btn-outline">⚙️ See Our Process</a>
    </div>
</section>
""", unsafe_allow_html=True)

footer()
