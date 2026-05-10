import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import GLOBAL_CSS
from components import navbar, footer

st.set_page_config(
    page_title="Industries — Bytewave Digital",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
navbar("Industries")

# ─── PAGE HEADER ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <div class="page-header-watermark">INDUSTRIES</div>
    <div class="section-label">Who We Serve</div>
    <h1 class="section-title">Technology Advisory Across <span class="gradient-text">Every Sector</span></h1>
    <p class="section-subtitle">
        We bring vendor-neutral technology expertise to organizations across industries &#8212;
        helping each make smarter, faster, and more confident technology decisions.
    </p>
</div>
""", unsafe_allow_html=True)

# ─── INDUSTRY CARD GRID: ROW 1 ───────────────────────────────────────────────
st.markdown("""
<div style="padding: 80px 60px 0; background: #FAF8F4;">
    <div style="text-align:center; margin-bottom:48px;">
        <div class="section-label">Our Verticals</div>
        <h2 class="section-title">Industries We <span class="gradient-text">Specialize In</span></h2>
        <p class="section-subtitle">Deep domain expertise combined with strategic technology advisory tailored to each industry&#8217;s unique business and operational needs.</p>
    </div>
</div>
""", unsafe_allow_html=True)

with st.container():

    row1_c1, row1_c2, row1_c3 = st.columns(3)

    with row1_c1:
        st.markdown("""
        <div class="industry-img-card" style="margin-bottom:8px;">
            <img src="https://images.unsplash.com/photo-1611532736597-de2d4265fba3?auto=format&fit=crop&w=700&q=90" alt="BFSI" />
            <div class="industry-img-overlay">
                <div class="industry-img-title">&#127974; BFSI</div>
                <div class="industry-img-sub">Secure, compliant tech for banking &amp; financial services</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with row1_c2:
        st.markdown("""
        <div class="industry-img-card" style="margin-bottom:8px;">
            <img src="https://images.unsplash.com/photo-1486325212027-8081e485255e?auto=format&fit=crop&w=700&q=90" alt="PSUs" />
            <div class="industry-img-overlay">
                <div class="industry-img-title">&#127963; Public Sector Undertakings (PSUs)</div>
                <div class="industry-img-sub">IT modernization for public enterprises</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with row1_c3:
        st.markdown("""
        <div class="industry-img-card" style="margin-bottom:8px;">
            <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=700&q=90" alt="Government Digital Platforms" />
            <div class="industry-img-overlay">
                <div class="industry-img-title">&#128187; Government Digital Platforms</div>
                <div class="industry-img-sub">Digital transformation for government services</div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ─── ROW 1 DETAILS ───────────────────────────────────────────────────────────
with st.container():

    det1_c1, det1_c2, det1_c3 = st.columns(3)

    with det1_c1:
        st.markdown("""
        <div style="background:rgba(232,93,4,0.04); border:1px solid rgba(232,93,4,0.12); border-radius:0 0 12px 12px; padding:20px; margin-bottom:32px;">
            <ul style="list-style:none; display:flex; flex-direction:column; gap:8px;">
                <li style="font-size:13px; color:#4A3728; display:flex; align-items:center; gap:8px;"><span style="color:#E85D04; font-weight:700;">&#8594;</span> Cybersecurity &amp; compliance solutions</li>
                <li style="font-size:13px; color:#4A3728; display:flex; align-items:center; gap:8px;"><span style="color:#E85D04; font-weight:700;">&#8594;</span> Core banking &amp; fintech integrations</li>
                <li style="font-size:13px; color:#4A3728; display:flex; align-items:center; gap:8px;"><span style="color:#E85D04; font-weight:700;">&#8594;</span> Observability for financial platforms</li>
                <li style="font-size:13px; color:#4A3728; display:flex; align-items:center; gap:8px;"><span style="color:#E85D04; font-weight:700;">&#8594;</span> Regulatory reporting &amp; monitoring</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with det1_c2:
        st.markdown("""
        <div style="background:rgba(232,93,4,0.04); border:1px solid rgba(232,93,4,0.12); border-radius:0 0 12px 12px; padding:20px; margin-bottom:32px;">
            <ul style="list-style:none; display:flex; flex-direction:column; gap:8px;">
                <li style="font-size:13px; color:#4A3728; display:flex; align-items:center; gap:8px;"><span style="color:#E85D04; font-weight:700;">&#8594;</span> IT modernization advisory</li>
                <li style="font-size:13px; color:#4A3728; display:flex; align-items:center; gap:8px;"><span style="color:#E85D04; font-weight:700;">&#8594;</span> Government-grade security solutions</li>
                <li style="font-size:13px; color:#4A3728; display:flex; align-items:center; gap:8px;"><span style="color:#E85D04; font-weight:700;">&#8594;</span> Compliance-aligned platforms</li>
                <li style="font-size:13px; color:#4A3728; display:flex; align-items:center; gap:8px;"><span style="color:#E85D04; font-weight:700;">&#8594;</span> ERP &amp; operational tool evaluation</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with det1_c3:
        st.markdown("""
        <div style="background:rgba(232,93,4,0.04); border:1px solid rgba(232,93,4,0.12); border-radius:0 0 12px 12px; padding:20px; margin-bottom:32px;">
            <ul style="list-style:none; display:flex; flex-direction:column; gap:8px;">
                <li style="font-size:13px; color:#4A3728; display:flex; align-items:center; gap:8px;"><span style="color:#E85D04; font-weight:700;">&#8594;</span> Citizen services technology advisory</li>
                <li style="font-size:13px; color:#4A3728; display:flex; align-items:center; gap:8px;"><span style="color:#E85D04; font-weight:700;">&#8594;</span> Cloud &amp; infrastructure evaluation</li>
                <li style="font-size:13px; color:#4A3728; display:flex; align-items:center; gap:8px;"><span style="color:#E85D04; font-weight:700;">&#8594;</span> Data security &amp; governance tools</li>
                <li style="font-size:13px; color:#4A3728; display:flex; align-items:center; gap:8px;"><span style="color:#E85D04; font-weight:700;">&#8594;</span> Digital platform observability</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)


# ─── INDUSTRY CARD GRID: ROW 2 ───────────────────────────────────────────────
with st.container():

    row2_c1, row2_c2, row2_c3 = st.columns(3)

    with row2_c1:
        st.markdown("""
        <div class="industry-img-card" style="margin-bottom:8px;">
            <img src="https://images.unsplash.com/photo-1516116216624-53e697fedbea?auto=format&fit=crop&w=700&q=90" alt="Telecom" />
            <div class="industry-img-overlay">
                <div class="industry-img-title">&#128225; Telecom</div>
                <div class="industry-img-sub">Network, CRM &amp; automation for telecom operators</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with row2_c2:
        st.markdown("""
        <div class="industry-img-card" style="margin-bottom:8px;">
            <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=700&q=90" alt="Technology Companies" />
            <div class="industry-img-overlay">
                <div class="industry-img-title">&#9881;&#65039; Technology Companies</div>
                <div class="industry-img-sub">Scalable IT solutions for tech-driven businesses</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with row2_c3:
        st.markdown("""
        <div class="industry-img-card" style="margin-bottom:8px;">
            <img src="https://images.unsplash.com/photo-1551434678-e076c223a692?auto=format&fit=crop&w=700&q=90" alt="SaaS Companies" />
            <div class="industry-img-overlay">
                <div class="industry-img-title">&#9729;&#65039; SaaS Companies</div>
                <div class="industry-img-sub">Observability, security &amp; growth tools for SaaS</div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ─── ROW 2 DETAILS ───────────────────────────────────────────────────────────
with st.container():

    det2_c1, det2_c2, det2_c3 = st.columns(3)

    with det2_c1:
        st.markdown("""
        <div style="background:rgba(232,93,4,0.04); border:1px solid rgba(232,93,4,0.12); border-radius:0 0 12px 12px; padding:20px; margin-bottom:32px;">
            <ul style="list-style:none; display:flex; flex-direction:column; gap:8px;">
                <li style="font-size:13px; color:#4A3728; display:flex; align-items:center; gap:8px;"><span style="color:#E85D04; font-weight:700;">&#8594;</span> Network performance monitoring</li>
                <li style="font-size:13px; color:#4A3728; display:flex; align-items:center; gap:8px;"><span style="color:#E85D04; font-weight:700;">&#8594;</span> CRM &amp; customer experience platforms</li>
                <li style="font-size:13px; color:#4A3728; display:flex; align-items:center; gap:8px;"><span style="color:#E85D04; font-weight:700;">&#8594;</span> AI-driven automation tools</li>
                <li style="font-size:13px; color:#4A3728; display:flex; align-items:center; gap:8px;"><span style="color:#E85D04; font-weight:700;">&#8594;</span> BSS/OSS transformation advisory</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with det2_c2:
        st.markdown("""
        <div style="background:rgba(232,93,4,0.04); border:1px solid rgba(232,93,4,0.12); border-radius:0 0 12px 12px; padding:20px; margin-bottom:32px;">
            <ul style="list-style:none; display:flex; flex-direction:column; gap:8px;">
                <li style="font-size:13px; color:#4A3728; display:flex; align-items:center; gap:8px;"><span style="color:#E85D04; font-weight:700;">&#8594;</span> Scalable architecture &amp; tool selection</li>
                <li style="font-size:13px; color:#4A3728; display:flex; align-items:center; gap:8px;"><span style="color:#E85D04; font-weight:700;">&#8594;</span> Security posture assessment</li>
                <li style="font-size:13px; color:#4A3728; display:flex; align-items:center; gap:8px;"><span style="color:#E85D04; font-weight:700;">&#8594;</span> Observability &amp; APM platform advisory</li>
                <li style="font-size:13px; color:#4A3728; display:flex; align-items:center; gap:8px;"><span style="color:#E85D04; font-weight:700;">&#8594;</span> Growth-stage technology planning</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with det2_c3:
        st.markdown("""
        <div style="background:rgba(232,93,4,0.04); border:1px solid rgba(232,93,4,0.12); border-radius:0 0 12px 12px; padding:20px; margin-bottom:32px;">
            <ul style="list-style:none; display:flex; flex-direction:column; gap:8px;">
                <li style="font-size:13px; color:#4A3728; display:flex; align-items:center; gap:8px;"><span style="color:#E85D04; font-weight:700;">&#8594;</span> Observability &amp; APM tool evaluation</li>
                <li style="font-size:13px; color:#4A3728; display:flex; align-items:center; gap:8px;"><span style="color:#E85D04; font-weight:700;">&#8594;</span> Integration ecosystem mapping</li>
                <li style="font-size:13px; color:#4A3728; display:flex; align-items:center; gap:8px;"><span style="color:#E85D04; font-weight:700;">&#8594;</span> AI &amp; automation platform advisory</li>
                <li style="font-size:13px; color:#4A3728; display:flex; align-items:center; gap:8px;"><span style="color:#E85D04; font-weight:700;">&#8594;</span> Customer experience solutions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)


# ─── WHO WE WORK WITH ────────────────────────────────────────────────────────
st.markdown("""
<div class="gradient-divider"></div>
<section class="section section-white">
    <div class="section-label">Who We Work With</div>
    <h2 class="section-title">Built for <span class="gradient-text">Both Sides</span> of the Market</h2>
    <p class="section-subtitle">Whether you sell technology or need to buy it &#8212; we have the right approach for you.</p>
    <div class="split-cards">
        <div class="split-card">
            <div class="split-card-icon">&#129513;</div>
            <div class="split-card-title">Technology Companies</div>
            <p style="font-size:14px; color:#6B5E52; margin-bottom:16px;">SaaS Companies &#183; IT &amp; Technology Firms &#183; Software Vendors</p>
            <ul class="split-card-list">
                <li>Expand market reach</li>
                <li>Accelerate revenue through reselling</li>
                <li>Build pipeline with SDR support</li>
                <li>Close deals with sales execution</li>
            </ul>
        </div>
        <div class="split-card">
            <div class="split-card-icon">&#127962;</div>
            <div class="split-card-title">Businesses (Buyers)</div>
            <p style="font-size:14px; color:#6B5E52; margin-bottom:16px;">Startups &amp; Scaleups &#183; Enterprises &#183; Companies Expanding into New Markets</p>
            <ul class="split-card-list">
                <li>Identify the right technology fit</li>
                <li>Simplify complex buying decisions</li>
                <li>Maximize ROI from software investments</li>
                <li>Access global vendor ecosystem</li>
            </ul>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── CTA ─────────────────────────────────────────────────────────────────────
st.markdown("""
<section class="cta-banner">
    <h2 class="cta-title">Don't See Your Industry? <span class="gradient-text">Let's Talk.</span></h2>
    <p class="cta-sub">We work with organizations across sectors. Tell us about your business and we'll show you how we can help.</p>
    <div class="cta-buttons">
        <a target="_self" href="/Contact" class="btn-gradient">&#128172; Talk to an Expert</a>
        <a target="_self" href="/Solutions" class="btn-outline">&#128269; Explore Solutions</a>
    </div>
</section>
""", unsafe_allow_html=True)

footer()
