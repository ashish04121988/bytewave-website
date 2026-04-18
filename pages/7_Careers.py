import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import GLOBAL_CSS
from components import navbar, footer

st.set_page_config(
    page_title="Careers — Bytewave Digital",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
navbar("Careers")

# ─── PAGE HEADER ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <div class="page-header-watermark">CAREERS</div>
    <div class="section-label">Join Our Team</div>
    <h1 class="section-title">Build the Future of <span class="gradient-text">Technology Buying</span></h1>
    <p class="section-subtitle">
        We're a fast-growing team on a mission to simplify technology decisions for businesses worldwide.
        If you're passionate about technology, sales, or advisory &#8212; we'd love to meet you.
    </p>
</div>
""", unsafe_allow_html=True)

# ─── WHY JOIN US ─────────────────────────────────────────────────────────────
st.markdown("""
<section class="section section-white">
    <div class="section-label">Why Bytewave</div>
    <h2 class="section-title">Why You'll <span class="gradient-text">Love Working Here</span></h2>
    <p class="section-subtitle">We believe in a high-trust, high-ownership culture where great work is noticed and rewarded.</p>
</section>
""", unsafe_allow_html=True)

v_c1, v_c2, v_c3, v_c4 = st.columns(4)

with v_c1:
    st.markdown("""
    <div style="padding:0 10px 60px; background:#FFFFFF;">
        <div class="career-value-card">
            <div class="career-value-icon">&#128640;</div>
            <div class="career-value-title">High-Growth Environment</div>
            <div class="career-value-desc">We're scaling fast. Every team member has outsized impact and room to grow with the company &#8212; no red tape, no bureaucracy.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with v_c2:
    st.markdown("""
    <div style="padding:0 10px 60px; background:#FFFFFF;">
        <div class="career-value-card">
            <div class="career-value-icon">&#127760;</div>
            <div class="career-value-title">Global Exposure</div>
            <div class="career-value-desc">Work with leading global technology vendors &#8212; Microsoft, AWS, Salesforce, and more &#8212; serving clients across India and globally.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with v_c3:
    st.markdown("""
    <div style="padding:0 10px 60px; background:#FFFFFF;">
        <div class="career-value-card">
            <div class="career-value-icon">&#129513;</div>
            <div class="career-value-title">Learn Every Day</div>
            <div class="career-value-desc">Bytewave is built on knowledge. You'll gain deep expertise across technology categories, sales strategy, and business consulting.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with v_c4:
    st.markdown("""
    <div style="padding:0 10px 60px; background:#FFFFFF;">
        <div class="career-value-card">
            <div class="career-value-icon">&#129309;</div>
            <div class="career-value-title">People-First Culture</div>
            <div class="career-value-desc">We invest in people &#8212; through mentorship, flexible work, and an open-door leadership culture built on trust and transparency.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ─── TEAM SNAPSHOT ───────────────────────────────────────────────────────────
team_l, team_r = st.columns([0.9, 1.1])

with team_l:
    st.markdown("""
    <div style="padding:0 40px 60px 60px; background:#FAF8F4;">
        <div class="about-img" style="height:420px; position:relative;">
            <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1200&q=90"
                 style="width:100%; height:100%; object-fit:cover; border-radius:20px;" alt="Bytewave Team" />
            <div class="about-img-badge">
                <div class="about-img-badge-num">2024</div>
                <div class="about-img-badge-text">Founded in Noida, India</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with team_r:
    st.markdown("""
    <div style="padding:0 60px 60px 20px; background:#FAF8F4;">
        <div class="section-label" style="text-align:left;">Our Culture</div>
        <h2 style="font-size:clamp(26px,3vw,38px); font-weight:800; letter-spacing:-1px; color:#1C1107; margin-bottom:20px; line-height:1.2;">
            A Team Built on <span class="gradient-text">Curiosity &amp; Execution</span>
        </h2>
        <p style="font-size:15px; color:#6B5E52; line-height:1.85; margin-bottom:20px;">
            Bytewave Digital is built by people who care deeply about doing things right. We're a small but
            mighty team &#8212; former sales leaders, technology consultants, and data experts &#8212; united by a
            shared mission to simplify technology buying.
        </p>
        <p style="font-size:15px; color:#6B5E52; line-height:1.85; margin-bottom:28px;">
            We're not looking for people who fit a mold &#8212; we're looking for those who are driven to
            make an impact, hungry to learn, and excited by the intersection of technology and business.
        </p>
        <div style="display:flex; flex-direction:column; gap:12px; margin-bottom:32px;">
            <div style="display:flex; align-items:center; gap:12px; font-size:14px; color:#4A3728;">
                <span style="color:#E85D04; font-weight:700; font-size:16px;">&#10003;</span>
                Flat hierarchy &#8212; your ideas are heard from Day 1
            </div>
            <div style="display:flex; align-items:center; gap:12px; font-size:14px; color:#4A3728;">
                <span style="color:#E85D04; font-weight:700; font-size:16px;">&#10003;</span>
                Performance-linked incentives and career progression
            </div>
            <div style="display:flex; align-items:center; gap:12px; font-size:14px; color:#4A3728;">
                <span style="color:#E85D04; font-weight:700; font-size:16px;">&#10003;</span>
                Continuous learning through vendor certifications
            </div>
            <div style="display:flex; align-items:center; gap:12px; font-size:14px; color:#4A3728;">
                <span style="color:#E85D04; font-weight:700; font-size:16px;">&#10003;</span>
                Flexible, outcome-driven work environment
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ─── OPEN POSITIONS ──────────────────────────────────────────────────────────
st.markdown("""
<div style="padding:60px 60px 20px; background:#FFFFFF; border-top:1px solid rgba(232,93,4,0.1);">
    <div class="section-label">Open Roles</div>
    <h2 class="section-title" style="margin-bottom:8px;">Current <span class="gradient-text">Openings</span></h2>
    <p class="section-subtitle">We're hiring across sales, technology advisory, and marketing. Don't see a fit? Write to us anyway.</p>
</div>
""", unsafe_allow_html=True)

job_c1, job_c2 = st.columns(2)

with job_c1:
    st.markdown("""
    <div style="padding:12px 12px 8px 60px; background:#FFFFFF;">
        <div class="career-card">
            <div class="career-card-icon">&#128200;</div>
            <div>
                <div class="career-card-title">Business Development Manager</div>
                <div class="career-card-dept">Sales &amp; Revenue</div>
                <div class="career-card-desc">Drive new business by identifying and engaging mid-market enterprises. You'll manage the full sales cycle from prospecting to closure across our CRM and cloud solutions portfolio.</div>
                <div>
                    <span class="career-badge location">&#128205; Noida / Remote</span>
                    <span class="career-badge type">&#128197; Full-Time</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with job_c2:
    st.markdown("""
    <div style="padding:12px 60px 8px 12px; background:#FFFFFF;">
        <div class="career-card">
            <div class="career-card-icon">&#129302;</div>
            <div>
                <div class="career-card-title">Technology Advisory Consultant</div>
                <div class="career-card-dept">Advisory &amp; Pre-Sales</div>
                <div class="career-card-desc">Work closely with clients to understand their technology needs and recommend the right software solutions. Prior experience in IT solutions or SaaS presales preferred.</div>
                <div>
                    <span class="career-badge location">&#128205; Noida / Hybrid</span>
                    <span class="career-badge type">&#128197; Full-Time</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

job_c3, job_c4 = st.columns(2)

with job_c3:
    st.markdown("""
    <div style="padding:8px 12px 8px 60px; background:#FFFFFF;">
        <div class="career-card">
            <div class="career-card-icon">&#128222;</div>
            <div>
                <div class="career-card-title">SDR — Sales Development Representative</div>
                <div class="career-card-dept">Inside Sales</div>
                <div class="career-card-desc">Identify and qualify prospects through outbound calling, email, and LinkedIn outreach. Build a strong pipeline and set up qualified meetings for the senior sales team.</div>
                <div>
                    <span class="career-badge location">&#128205; Noida</span>
                    <span class="career-badge type">&#128197; Full-Time</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with job_c4:
    st.markdown("""
    <div style="padding:8px 60px 8px 12px; background:#FFFFFF;">
        <div class="career-card">
            <div class="career-card-icon">&#128226;</div>
            <div>
                <div class="career-card-title">Digital Marketing &amp; Content Specialist</div>
                <div class="career-card-dept">Marketing</div>
                <div class="career-card-desc">Own Bytewave's digital presence &#8212; from content marketing and SEO to LinkedIn campaigns and email outreach. Must have a strong understanding of B2B SaaS marketing.</div>
                <div>
                    <span class="career-badge location">&#128205; Remote / Hybrid</span>
                    <span class="career-badge type">&#128197; Full-Time</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

job_c5, job_c6 = st.columns(2)

with job_c5:
    st.markdown("""
    <div style="padding:8px 12px 32px 60px; background:#FFFFFF;">
        <div class="career-card">
            <div class="career-card-icon">&#128269;</div>
            <div>
                <div class="career-card-title">Research &amp; Intelligence Analyst</div>
                <div class="career-card-dept">Strategy &amp; Intelligence</div>
                <div class="career-card-desc">Leverage data and market intelligence to identify target accounts, map competitive landscapes, and support advisory engagements. Background in business research or data analytics preferred.</div>
                <div>
                    <span class="career-badge location">&#128205; Noida / Remote</span>
                    <span class="career-badge type">&#128197; Full-Time</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with job_c6:
    st.markdown("""
    <div style="padding:8px 60px 32px 12px; background:#FFFFFF;">
        <div class="career-card">
            <div class="career-card-icon">&#127942;</div>
            <div>
                <div class="career-card-title">Partnerships &amp; Alliances Manager</div>
                <div class="career-card-dept">Partnerships</div>
                <div class="career-card-desc">Build and manage relationships with our technology vendor partners &#8212; Microsoft, AWS, Salesforce, and others. Drive joint GTM programs and partner revenue targets.</div>
                <div>
                    <span class="career-badge location">&#128205; Noida / Remote</span>
                    <span class="career-badge type">&#128197; Full-Time</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ─── GENERAL APPLICATION ──────────────────────────────────────────────────────
st.markdown("""
<section class="section section-beige">
    <div class="section-label">Don't See Your Role?</div>
    <h2 class="section-title">We're Always Looking for <span class="gradient-text">Great People</span></h2>
    <p class="section-subtitle">
        If you're passionate about technology, sales, or advisory work and believe you'd thrive at Bytewave Digital &#8212;
        reach out. We'd love to hear from you.
    </p>
    <div style="display:flex; gap:16px; justify-content:center; flex-wrap:wrap; margin-top:16px;">
        <a target="_self" href="/Contact" class="btn-gradient" style="text-decoration:none;">&#128231; Send Your Profile</a>
        <a target="_self" href="/About" class="btn-outline" style="text-decoration:none;">&#128269; Learn About Us</a>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── CTA ─────────────────────────────────────────────────────────────────────
st.markdown("""
<section class="cta-banner">
    <h2 class="cta-title">Ready to Make an <span class="gradient-text">Impact?</span></h2>
    <p class="cta-sub">Join a team that's simplifying technology for businesses everywhere. Your next chapter starts here.</p>
    <div class="cta-buttons">
        <a target="_self" href="/Contact" class="btn-gradient">&#128231; Apply Now</a>
        <a target="_self" href="/Contact" class="btn-outline">&#128172; Talk to Us First</a>
    </div>
</section>
""", unsafe_allow_html=True)

footer()
