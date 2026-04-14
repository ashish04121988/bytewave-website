import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import GLOBAL_CSS
from components import navbar, footer

st.set_page_config(
    page_title="Contact — Bytewave Digital Solutions",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
navbar("Contact")

# ─── PAGE HEADER ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <div class="page-header-watermark">CONTACT</div>
    <div class="section-label">Get In Touch</div>
    <h1 class="section-title">Let's Grow Your <span class="gradient-text">Revenue Together</span></h1>
    <p class="section-subtitle">
        Book a free strategy call, get a demo, or just tell us about your business.
        We'll get back to you within 24 hours.
    </p>
</div>
""", unsafe_allow_html=True)

# ─── CONTACT SECTION ─────────────────────────────────────────────────────────
# Use st.columns for layout — no HTML wrapper across multiple st.markdown calls

col_left, col_right = st.columns([1, 1.4], gap="large")

with col_left:
    # Complete self-contained HTML block — no splits
    st.markdown("""
    <div style="padding:40px 20px 40px 40px;">
        <h2 style="font-size:34px; font-weight:800; letter-spacing:-1px; line-height:1.2; color:#F1F5F9; margin-bottom:14px;">
            Let's Grow Your <span style="background:linear-gradient(135deg,#2563EB,#7C3AED,#F97316);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">Revenue</span>
        </h2>
        <p style="font-size:15px; color:#94A3B8; line-height:1.7; margin-bottom:36px;">
            Whether you're looking to generate more leads, close more deals, or find the right technology —
            we're ready to help. Fill out the form and our team will get back to you within 24 hours.
        </p>
        <div style="display:flex; flex-direction:column; gap:16px; margin-bottom:40px;">
            <div style="display:flex; align-items:center; gap:14px;">
                <div style="width:40px; height:40px; background:rgba(37,99,235,0.15); border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:18px; flex-shrink:0;">📧</div>
                <span style="font-size:14px; color:#94A3B8;">hello@bytewavedigital.com</span>
            </div>
            <div style="display:flex; align-items:center; gap:14px;">
                <div style="width:40px; height:40px; background:rgba(37,99,235,0.15); border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:18px; flex-shrink:0;">📞</div>
                <span style="font-size:14px; color:#94A3B8;">+91 98XXX XXXXX</span>
            </div>
            <div style="display:flex; align-items:center; gap:14px;">
                <div style="width:40px; height:40px; background:rgba(37,99,235,0.15); border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:18px; flex-shrink:0;">📍</div>
                <span style="font-size:14px; color:#94A3B8;">India (Pan-India Coverage)</span>
            </div>
            <div style="display:flex; align-items:center; gap:14px;">
                <div style="width:40px; height:40px; background:rgba(37,99,235,0.15); border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:18px; flex-shrink:0;">🕐</div>
                <span style="font-size:14px; color:#94A3B8;">Mon–Sat: 9:00 AM – 7:00 PM IST</span>
            </div>
        </div>
        <div style="font-size:12px; font-weight:700; letter-spacing:2px; text-transform:uppercase; color:#475569; margin-bottom:16px;">What happens next?</div>
        <div style="display:flex; flex-direction:column; gap:12px;">
            <div style="display:flex; align-items:center; gap:12px; font-size:14px; color:#94A3B8;">
                <div style="width:28px; height:28px; border-radius:50%; background:linear-gradient(135deg,#2563EB,#7C3AED); display:flex; align-items:center; justify-content:center; font-size:12px; font-weight:700; color:white; flex-shrink:0;">1</div>
                We review your requirements within 24 hours
            </div>
            <div style="display:flex; align-items:center; gap:12px; font-size:14px; color:#94A3B8;">
                <div style="width:28px; height:28px; border-radius:50%; background:linear-gradient(135deg,#7C3AED,#F97316); display:flex; align-items:center; justify-content:center; font-size:12px; font-weight:700; color:white; flex-shrink:0;">2</div>
                We schedule a free 30-min strategy call
            </div>
            <div style="display:flex; align-items:center; gap:12px; font-size:14px; color:#94A3B8;">
                <div style="width:28px; height:28px; border-radius:50%; background:linear-gradient(135deg,#F97316,#2563EB); display:flex; align-items:center; justify-content:center; font-size:12px; font-weight:700; color:white; flex-shrink:0;">3</div>
                We build a custom growth plan for you
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    # Header card — complete self-contained HTML block
    st.markdown("""
    <div style="background:rgba(13,35,71,0.7); border:1px solid rgba(37,99,235,0.2); border-radius:20px 20px 0 0; padding:28px 32px 16px; position:relative; overflow:hidden; margin-top:40px;">
        <div style="position:absolute; top:0; left:0; right:0; height:3px; background:linear-gradient(135deg,#2563EB,#7C3AED,#F97316);"></div>
        <div style="font-size:20px; font-weight:700; color:#F1F5F9;">Send Us a Message</div>
    </div>
    """, unsafe_allow_html=True)

    # Form body — separate complete block, styled to attach visually below header
    st.markdown("""
    <div style="background:rgba(13,35,71,0.7); border:1px solid rgba(37,99,235,0.2); border-top:none; border-radius:0 0 20px 20px; padding:0 32px 28px;">
    </div>
    """, unsafe_allow_html=True)

    with st.form("contact_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Your Name *", placeholder="Rahul Sharma")
        with c2:
            email = st.text_input("Work Email *", placeholder="rahul@company.com")

        c3, c4 = st.columns(2)
        with c3:
            company = st.text_input("Company Name *", placeholder="Your Company")
        with c4:
            phone = st.text_input("Phone Number", placeholder="+91 98XXX XXXXX")

        requirement = st.selectbox(
            "I'm interested in *",
            [
                "Select a service...",
                "Lead Generation",
                "Sales Execution Support",
                "Technology Reselling Advisory",
                "End-to-End Revenue Partnership",
                "Book a Free Strategy Call",
                "Get a Demo",
                "Other",
            ]
        )

        message = st.text_area(
            "Tell us about your business *",
            placeholder="Briefly describe your business, target market, and what you're looking to achieve...",
            height=120,
        )

        submitted = st.form_submit_button("🚀 Send Message", use_container_width=True)

        if submitted:
            if name and email and company and requirement != "Select a service..." and message:
                st.success(f"✅ Thank you, **{name}**! We've received your message and will get back to you within 24 hours.")
                st.balloons()
            else:
                st.error("Please fill in all required fields marked with *")

# ─── QUICK OPTIONS ───────────────────────────────────────────────────────────
st.markdown("""
<section class="section section-dark">
    <div class="section-label">Quick Actions</div>
    <h2 class="section-title">Other Ways to <span class="gradient-text">Connect</span></h2>
    <div class="cards-grid" style="max-width:800px;">
        <div class="service-card" style="text-align:center;">
            <span class="card-icon">📅</span>
            <div class="card-title">Book a Consultation</div>
            <div class="card-desc">Schedule a free 30-minute strategy call with our revenue experts.</div>
        </div>
        <div class="service-card" style="text-align:center;">
            <span class="card-icon">🖥️</span>
            <div class="card-title">Get a Demo</div>
            <div class="card-desc">See how our lead generation system works with a live demonstration.</div>
        </div>
        <div class="service-card" style="text-align:center;">
            <span class="card-icon">🚀</span>
            <div class="card-title">Start Generating Leads</div>
            <div class="card-desc">Ready to go? Let's launch your first lead generation campaign today.</div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

footer()
