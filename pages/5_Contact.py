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
st.markdown("""
<section class="section section-darker">
    <div class="contact-grid">
        <div>
            <h2 class="contact-left-title">Let's Grow Your <span class="gradient-text">Revenue</span></h2>
            <p class="contact-left-sub">
                Whether you're looking to generate more leads, close more deals, or find the right technology —
                we're ready to help. Fill out the form and our team will get back to you within 24 hours.
            </p>

            <div class="contact-info-item">
                <div class="contact-info-icon">📧</div>
                <div class="contact-info-text">hello@bytewavedigital.com</div>
            </div>
            <div class="contact-info-item">
                <div class="contact-info-icon">📞</div>
                <div class="contact-info-text">+91 98XXX XXXXX</div>
            </div>
            <div class="contact-info-item">
                <div class="contact-info-icon">📍</div>
                <div class="contact-info-text">India (Pan-India Coverage)</div>
            </div>
            <div class="contact-info-item">
                <div class="contact-info-icon">🕐</div>
                <div class="contact-info-text">Mon–Sat: 9:00 AM – 7:00 PM IST</div>
            </div>

            <div style="margin-top:40px;">
                <div style="font-size:13px; font-weight:700; letter-spacing:2px; text-transform:uppercase; color:#475569; margin-bottom:16px;">What happens next?</div>
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
        </div>

        <div class="contact-form-container">
""", unsafe_allow_html=True)

# Streamlit form (native)
with st.form("contact_form", clear_on_submit=True):
    st.markdown("""
    <div style="font-size:20px; font-weight:700; color:#F1F5F9; margin-bottom:24px;">
        Send Us a Message
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Your Name *", placeholder="Rahul Sharma")
    with col2:
        email = st.text_input("Work Email *", placeholder="rahul@company.com")

    col3, col4 = st.columns(2)
    with col3:
        company = st.text_input("Company Name *", placeholder="Your Company")
    with col4:
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

    submitted = st.form_submit_button("🚀 Send Message")

    if submitted:
        if name and email and company and requirement != "Select a service..." and message:
            st.success(f"✅ Thank you, **{name}**! We've received your message and will get back to you within 24 hours.")
            st.balloons()
        else:
            st.error("Please fill in all required fields marked with *")

st.markdown("""
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── QUICK OPTIONS ───────────────────────────────────────────────────────────
st.markdown("""
<section class="section section-dark">
    <div class="section-label">Quick Actions</div>
    <h2 class="section-title">Other Ways to <span class="gradient-text">Connect</span></h2>
    <div class="cards-grid" style="max-width:800px;">
        <div class="service-card" style="text-align:center; cursor:pointer;">
            <span class="card-icon">📅</span>
            <div class="card-title">Book a Consultation</div>
            <div class="card-desc">Schedule a free 30-minute strategy call with our revenue experts.</div>
            <div style="margin-top:16px;"><a href="#" class="btn-gradient" style="font-size:13px; padding:8px 20px;">Book Now</a></div>
        </div>
        <div class="service-card" style="text-align:center; cursor:pointer;">
            <span class="card-icon">🖥️</span>
            <div class="card-title">Get a Demo</div>
            <div class="card-desc">See how our lead generation system works with a live demonstration.</div>
            <div style="margin-top:16px;"><a href="#" class="btn-gradient" style="font-size:13px; padding:8px 20px;">Get Demo</a></div>
        </div>
        <div class="service-card" style="text-align:center; cursor:pointer;">
            <span class="card-icon">🚀</span>
            <div class="card-title">Start Generating Leads</div>
            <div class="card-desc">Ready to go? Let's launch your first lead generation campaign today.</div>
            <div style="margin-top:16px;"><a href="#" class="btn-gradient" style="font-size:13px; padding:8px 20px;">Get Started</a></div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

footer()
