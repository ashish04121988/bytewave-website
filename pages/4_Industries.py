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
        We bring vendor-neutral technology expertise to organizations across industries —
        helping each make smarter, faster, and more confident technology decisions.
    </p>
</div>
""", unsafe_allow_html=True)

# ─── INDUSTRY CARD GRID: ROW 1 ───────────────────────────────────────────────
st.markdown("""
<div style="padding: 80px 60px 0; background: #081729;">
    <div style="text-align:center; margin-bottom:48px;">
        <div class="section-label">Our Verticals</div>
        <h2 class="section-title">Industries We <span class="gradient-text">Specialize In</span></h2>
        <p class="section-subtitle">Deep domain knowledge paired with vendor-neutral technology advisory — tailored for each sector.</p>
    </div>
</div>
""", unsafe_allow_html=True)

with st.container():

    row1_c1, row1_c2, row1_c3 = st.columns(3)

    with row1_c1:
        st.markdown("""
        <div class="industry-img-card" style="margin-bottom:8px;">
            <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=500&q=80" alt="Technology and SaaS" />
            <div class="industry-img-overlay">
                <div class="industry-img-title">💻 Technology &amp; SaaS</div>
                <div class="industry-img-sub">Scalable stacks for fast-growing tech companies</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with row1_c2:
        st.markdown("""
        <div class="industry-img-card" style="margin-bottom:8px;">
            <img src="https://images.unsplash.com/photo-1611532736597-de2d4265fba3?auto=format&fit=crop&w=500&q=80" alt="Financial Services" />
            <div class="industry-img-overlay">
                <div class="industry-img-title">🏦 Financial Services</div>
                <div class="industry-img-sub">Secure, compliant tech for BFSI organizations</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with row1_c3:
        st.markdown("""
        <div class="industry-img-card" style="margin-bottom:8px;">
            <img src="https://images.unsplash.com/photo-1559757148-5c350d0d3c56?auto=format&fit=crop&w=500&q=80" alt="Healthcare" />
            <div class="industry-img-overlay">
                <div class="industry-img-title">🏥 Healthcare &amp; Life Sciences</div>
                <div class="industry-img-sub">Compliance-first platforms for clinical operations</div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ─── ROW 1 DETAILS ───────────────────────────────────────────────────────────
with st.container():

    det1_c1, det1_c2, det1_c3 = st.columns(3)

    with det1_c1:
        st.markdown("""
        <div style="background:rgba(13,35,71,0.6); border:1px solid rgba(37,99,235,0.15); border-radius:0 0 12px 12px; padding:20px; margin-bottom:32px;">
            <ul style="list-style:none; display:flex; flex-direction:column; gap:8px;">
                <li style="font-size:13px; color:#CBD5E1; display:flex; align-items:center; gap:8px;"><span style="color:#2563EB; font-weight:700;">→</span> Scalable architecture selection</li>
                <li style="font-size:13px; color:#CBD5E1; display:flex; align-items:center; gap:8px;"><span style="color:#2563EB; font-weight:700;">→</span> SaaS tool stack evaluation</li>
                <li style="font-size:13px; color:#CBD5E1; display:flex; align-items:center; gap:8px;"><span style="color:#2563EB; font-weight:700;">→</span> Integration ecosystem mapping</li>
                <li style="font-size:13px; color:#CBD5E1; display:flex; align-items:center; gap:8px;"><span style="color:#2563EB; font-weight:700;">→</span> Growth-stage technology planning</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with det1_c2:
        st.markdown("""
        <div style="background:rgba(13,35,71,0.6); border:1px solid rgba(37,99,235,0.15); border-radius:0 0 12px 12px; padding:20px; margin-bottom:32px;">
            <ul style="list-style:none; display:flex; flex-direction:column; gap:8px;">
                <li style="font-size:13px; color:#CBD5E1; display:flex; align-items:center; gap:8px;"><span style="color:#2563EB; font-weight:700;">→</span> Compliance-aligned tools</li>
                <li style="font-size:13px; color:#CBD5E1; display:flex; align-items:center; gap:8px;"><span style="color:#2563EB; font-weight:700;">→</span> Data security evaluation</li>
                <li style="font-size:13px; color:#CBD5E1; display:flex; align-items:center; gap:8px;"><span style="color:#2563EB; font-weight:700;">→</span> Core banking integrations</li>
                <li style="font-size:13px; color:#CBD5E1; display:flex; align-items:center; gap:8px;"><span style="color:#2563EB; font-weight:700;">→</span> Regulatory reporting solutions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with det1_c3:
        st.markdown("""
        <div style="background:rgba(13,35,71,0.6); border:1px solid rgba(37,99,235,0.15); border-radius:0 0 12px 12px; padding:20px; margin-bottom:32px;">
            <ul style="list-style:none; display:flex; flex-direction:column; gap:8px;">
                <li style="font-size:13px; color:#CBD5E1; display:flex; align-items:center; gap:8px;"><span style="color:#2563EB; font-weight:700;">→</span> EHR &amp; HMS evaluation</li>
                <li style="font-size:13px; color:#CBD5E1; display:flex; align-items:center; gap:8px;"><span style="color:#2563EB; font-weight:700;">→</span> HIPAA-aligned platforms</li>
                <li style="font-size:13px; color:#CBD5E1; display:flex; align-items:center; gap:8px;"><span style="color:#2563EB; font-weight:700;">→</span> Lab management tools</li>
                <li style="font-size:13px; color:#CBD5E1; display:flex; align-items:center; gap:8px;"><span style="color:#2563EB; font-weight:700;">→</span> Clinical workflow automation</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)


# ─── INDUSTRY CARD GRID: ROW 2 ───────────────────────────────────────────────
with st.container():

    row2_c1, row2_c2, row2_c3 = st.columns(3)

    with row2_c1:
        st.markdown("""
        <div class="industry-img-card" style="margin-bottom:8px;">
            <img src="https://images.unsplash.com/photo-1565043589221-1a6fd9ae45c7?auto=format&fit=crop&w=500&q=80" alt="Manufacturing" />
            <div class="industry-img-overlay">
                <div class="industry-img-title">🏭 Manufacturing &amp; Logistics</div>
                <div class="industry-img-sub">Efficiency tools for manufacturers &amp; distributors</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with row2_c2:
        st.markdown("""
        <div class="industry-img-card" style="margin-bottom:8px;">
            <img src="https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=500&q=80" alt="Retail" />
            <div class="industry-img-overlay">
                <div class="industry-img-title">🛒 Retail &amp; E-commerce</div>
                <div class="industry-img-sub">Omnichannel platforms for customer growth</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with row2_c3:
        st.markdown("""
        <div class="industry-img-card" style="margin-bottom:8px;">
            <img src="https://images.unsplash.com/photo-1580582932707-520aed937b7b?auto=format&fit=crop&w=500&q=80" alt="Education" />
            <div class="industry-img-overlay">
                <div class="industry-img-title">🎓 Education &amp; Public Sector</div>
                <div class="industry-img-sub">Cost-effective, scalable solutions for institutions</div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ─── ROW 2 DETAILS ───────────────────────────────────────────────────────────
with st.container():

    det2_c1, det2_c2, det2_c3 = st.columns(3)

    with det2_c1:
        st.markdown("""
        <div style="background:rgba(13,35,71,0.6); border:1px solid rgba(37,99,235,0.15); border-radius:0 0 12px 12px; padding:20px; margin-bottom:32px;">
            <ul style="list-style:none; display:flex; flex-direction:column; gap:8px;">
                <li style="font-size:13px; color:#CBD5E1; display:flex; align-items:center; gap:8px;"><span style="color:#2563EB; font-weight:700;">→</span> ERP selection &amp; comparison</li>
                <li style="font-size:13px; color:#CBD5E1; display:flex; align-items:center; gap:8px;"><span style="color:#2563EB; font-weight:700;">→</span> Supply chain tools</li>
                <li style="font-size:13px; color:#CBD5E1; display:flex; align-items:center; gap:8px;"><span style="color:#2563EB; font-weight:700;">→</span> Warehouse management systems</li>
                <li style="font-size:13px; color:#CBD5E1; display:flex; align-items:center; gap:8px;"><span style="color:#2563EB; font-weight:700;">→</span> IoT &amp; automation platforms</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with det2_c2:
        st.markdown("""
        <div style="background:rgba(13,35,71,0.6); border:1px solid rgba(37,99,235,0.15); border-radius:0 0 12px 12px; padding:20px; margin-bottom:32px;">
            <ul style="list-style:none; display:flex; flex-direction:column; gap:8px;">
                <li style="font-size:13px; color:#CBD5E1; display:flex; align-items:center; gap:8px;"><span style="color:#2563EB; font-weight:700;">→</span> E-commerce platform selection</li>
                <li style="font-size:13px; color:#CBD5E1; display:flex; align-items:center; gap:8px;"><span style="color:#2563EB; font-weight:700;">→</span> Customer engagement tools</li>
                <li style="font-size:13px; color:#CBD5E1; display:flex; align-items:center; gap:8px;"><span style="color:#2563EB; font-weight:700;">→</span> Inventory &amp; order management</li>
                <li style="font-size:13px; color:#CBD5E1; display:flex; align-items:center; gap:8px;"><span style="color:#2563EB; font-weight:700;">→</span> Analytics &amp; personalization</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with det2_c3:
        st.markdown("""
        <div style="background:rgba(13,35,71,0.6); border:1px solid rgba(37,99,235,0.15); border-radius:0 0 12px 12px; padding:20px; margin-bottom:32px;">
            <ul style="list-style:none; display:flex; flex-direction:column; gap:8px;">
                <li style="font-size:13px; color:#CBD5E1; display:flex; align-items:center; gap:8px;"><span style="color:#2563EB; font-weight:700;">→</span> LMS &amp; EdTech evaluation</li>
                <li style="font-size:13px; color:#CBD5E1; display:flex; align-items:center; gap:8px;"><span style="color:#2563EB; font-weight:700;">→</span> Cost-effective procurement</li>
                <li style="font-size:13px; color:#CBD5E1; display:flex; align-items:center; gap:8px;"><span style="color:#2563EB; font-weight:700;">→</span> Compliance-aligned solutions</li>
                <li style="font-size:13px; color:#CBD5E1; display:flex; align-items:center; gap:8px;"><span style="color:#2563EB; font-weight:700;">→</span> Scalable infrastructure choices</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)


# ─── WHO WE WORK WITH ────────────────────────────────────────────────────────
st.markdown("""
<div class="gradient-divider"></div>
<section class="section section-dark">
    <div class="section-label">Who We Work With</div>
    <h2 class="section-title">Built for <span class="gradient-text">Both Sides</span> of the Market</h2>
    <p class="section-subtitle">Whether you sell technology or need to buy it — we have the right approach for you.</p>
    <div class="split-cards">
        <div class="split-card">
            <div class="split-card-icon">🧩</div>
            <div class="split-card-title">Technology Companies</div>
            <p style="font-size:14px; color:#94A3B8; margin-bottom:16px;">SaaS Companies · IT &amp; Technology Firms · Software Vendors</p>
            <ul class="split-card-list">
                <li>Expand market reach</li>
                <li>Accelerate revenue through reselling</li>
                <li>Build pipeline with SDR support</li>
                <li>Close deals with sales execution</li>
            </ul>
        </div>
        <div class="split-card">
            <div class="split-card-icon">🏢</div>
            <div class="split-card-title">Businesses (Buyers)</div>
            <p style="font-size:14px; color:#94A3B8; margin-bottom:16px;">Startups &amp; Scaleups · Enterprises · Companies Expanding into New Markets</p>
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
        <a target="_self" href="/Contact" class="btn-gradient">💬 Talk to an Expert</a>
        <a target="_self" href="/Solutions" class="btn-outline">🔍 Explore Solutions</a>
    </div>
</section>
""", unsafe_allow_html=True)

footer()
