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

industries = [
    {
        "icon": "💻",
        "title": "Technology & SaaS",
        "desc": "Helping fast-growing tech companies choose scalable and flexible technology stacks that support rapid expansion without over-engineering.",
        "points": ["Scalable architecture selection", "SaaS tool stack evaluation", "Integration ecosystem mapping", "Growth-stage technology planning"],
        "reverse": False,
    },
    {
        "icon": "🏦",
        "title": "Financial Services",
        "desc": "Supporting secure, compliant, and efficient technology decision-making for banks, NBFCs, fintechs, and insurance companies.",
        "points": ["Compliance-aligned tools", "Data security evaluation", "Core banking integrations", "Regulatory reporting solutions"],
        "reverse": True,
    },
    {
        "icon": "🏥",
        "title": "Healthcare & Life Sciences",
        "desc": "Enabling better system selection for operational efficiency and compliance in hospitals, clinics, diagnostic labs, and pharma.",
        "points": ["EHR & HMS evaluation", "HIPAA-aligned platforms", "Lab management tools", "Clinical workflow automation"],
        "reverse": False,
    },
    {
        "icon": "🏭",
        "title": "Manufacturing & Logistics",
        "desc": "Driving efficiency through the right enterprise and automation tools for manufacturers, distributors, and logistics operators.",
        "points": ["ERP selection & comparison", "Supply chain tools", "Warehouse management systems", "IoT & automation platforms"],
        "reverse": True,
    },
    {
        "icon": "🛒",
        "title": "Retail & E-commerce",
        "desc": "Helping businesses choose platforms for customer engagement, inventory management, and omnichannel growth.",
        "points": ["E-commerce platform selection", "Customer engagement tools", "Inventory & order management", "Analytics & personalization"],
        "reverse": False,
    },
    {
        "icon": "🎓",
        "title": "Education & Public Sector",
        "desc": "Supporting institutions with cost-effective and scalable technology solutions aligned to tighter budgets and unique compliance needs.",
        "points": ["LMS & EdTech evaluation", "Cost-effective procurement", "Compliance-aligned solutions", "Scalable infrastructure choices"],
        "reverse": True,
    },
]

for i, ind in enumerate(industries):
    bg = "section-dark" if i % 2 == 0 else "section-darker"
    rev = "reverse" if ind["reverse"] else ""
    bullets_html = "".join([f"<li>{p}</li>" for p in ind["points"]])
    st.markdown(f'<div class="gradient-divider"></div>', unsafe_allow_html=True)
    st.markdown(f"""
<section class="section {bg}">
    <div class="service-detail {rev}">
        <div class="service-detail-icon-block" style="font-size:54px;">{ind["icon"]}</div>
        <div class="service-detail-content">
            <div class="section-label" style="text-align:left;">Industry</div>
            <h2 class="service-detail-title">{ind["title"]}</h2>
            <p class="service-detail-desc">{ind["desc"]}</p>
            <ul class="service-detail-list">{bullets_html}</ul>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── WHO WE WORK WITH ────────────────────────────────────────────────────────
st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section section-dark">
    <div class="section-label">Who We Work With</div>
    <h2 class="section-title">Built for <span class="gradient-text">Both Sides</span> of the Market</h2>
    <p class="section-subtitle">Whether you sell technology or need to buy it — we have the right approach for you.</p>
    <div class="split-cards">
        <div class="split-card">
            <div class="split-card-icon">🧩</div>
            <div class="split-card-title">Technology Companies</div>
            <p style="font-size:14px; color:#94A3B8; margin-bottom:16px;">SaaS Companies · IT & Technology Firms · Software Vendors</p>
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
