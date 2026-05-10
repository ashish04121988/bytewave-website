import streamlit as st
from styles import GLOBAL_CSS
from components import navbar, footer

st.set_page_config(
    page_title="Bytewave Digital — Right Technology. No Noise.",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
navbar("Home")

# ─── HERO ────────────────────────────────────────────────────────────────────
hero_left, hero_right = st.columns([1.4, 0.6])

with hero_left:
    st.markdown("""
    <div class="hero-bg">
        <div style="max-width:700px; z-index:2; position:relative;">
            <div class="hero-eyebrow">Enterprise AI, Cybersecurity &amp; Observability Solutions Partner</div>
            <h1 class="hero-h1">
                Simplifying Technology Decisions.<br>
                <span class="gradient-text">Maximizing Business Outcomes.</span>
            </h1>
            <p class="hero-sub">
                Helping organizations modernize IT operations, strengthen security posture, and improve operational visibility through scalable, business-aligned technology solutions.
            </p>
            <p class="hero-sub">
                Through its strategic partnership with Fundoodata and a strong industry network, Bytewave Digital helps organizations identify, evaluate, and adopt the right technology solutions &#8212; driven by business needs, not vendor agendas.
            </p>
            <div class="hero-cta-group">
                <a target="_self" href="/Solutions" class="btn-gradient">&#128269; Explore Solutions</a>
                <a target="_self" href="/Contact" class="btn-outline">&#128172; Talk to an Expert</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with hero_right:
    st.markdown("""
    <div style="background: #FAF8F4; min-height:92vh; display:flex; flex-direction:column; justify-content:center; align-items:center; gap:20px; padding:40px 24px;">
        <div class="stat-badge" style="width:200px;">
            <div class="stat-badge-number">3&#8211;4x</div>
            <div class="stat-badge-label">Pipeline Growth</div>
        </div>
        <div class="stat-badge" style="width:200px;">
            <div class="stat-badge-number">50%</div>
            <div class="stat-badge-label">Faster Deal Cycles</div>
        </div>
        <div class="stat-badge" style="width:200px;">
            <div class="stat-badge-number">1</div>
            <div class="stat-badge-label">Strategic Partner</div>
        </div>
        <div style="margin-top:8px; text-align:center;">
            <div style="font-size:11px; color:#A89888; letter-spacing:1px; text-transform:uppercase; margin-bottom:12px;">Trusted by</div>
            <div style="font-size:13px; color:#4A3728; font-weight:600;">SMEs &#183; Mid-Market &#183; Enterprise</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ─── PARTNER STRIP ────────────────────────────────────────────────────────────
st.markdown("""
<div class="partner-strip">
    <div style="text-align:center; margin-bottom:18px; font-size:12px; color:#A89888; letter-spacing:2px; text-transform:uppercase; font-weight:700;">
        Trusted Technology Ecosystem
    </div>
    <div class="partner-logos">
        <div class="partner-logo">Microsoft</div>
        <div class="partner-logo">AWS</div>
        <div class="partner-logo">Google Cloud</div>
        <div class="partner-logo">Salesforce</div>
        <div class="partner-logo">SAP</div>
        <div class="partner-logo">HubSpot</div>
        <div class="partner-logo">Freshworks</div>
        <div class="partner-logo">Zoho</div>
        <div class="partner-logo">ServiceNow</div>
        <div class="partner-logo">Oracle</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─── STATS SECTION ───────────────────────────────────────────────────────────
st.markdown("""
<div class="stats-section">
    <div class="stats-grid">
        <div class="stat-item">
            <div class="stat-number">3&#8211;4x</div>
            <div class="stat-label">Pipeline Growth</div>
            <div class="stat-sublabel">for technology vendors</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">50%</div>
            <div class="stat-label">Faster Deal Cycles</div>
            <div class="stat-sublabel">through curated advisory</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">4</div>
            <div class="stat-label">Core Focus Areas</div>
            <div class="stat-sublabel">AI, Cybersecurity, APM, CRM</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">1</div>
            <div class="stat-label">Strategic Partner</div>
            <div class="stat-sublabel">Fundoodata ecosystem</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─── ABOUT SNAPSHOT ──────────────────────────────────────────────────────────
st.markdown("""
<div style="padding: 60px 60px 0; background: #FAF8F4; text-align:center;">
    <div class="section-label">About Us</div>
</div>
""", unsafe_allow_html=True)

about_left, about_right = st.columns([1.1, 0.9])

with about_left:
    st.markdown("""
    <div style="padding: 0 40px 60px 60px; background: #FAF8F4;">
        <h2 style="font-size:clamp(32px,4vw,48px); font-weight:800; letter-spacing:-1px; color:#1C1107; margin-bottom:20px; line-height:1.15; text-align:left;">
            Your Technology &amp; <span class="gradient-text">Revenue Growth</span> Partner
        </h2>
        <p style="font-size:16px; color:#6B5E52; line-height:1.85; margin-bottom:16px;">
            At Bytewave Digital, we work with SMB, Mid-Market, and Enterprise businesses across industries such as Retail, Manufacturing, BFSI, Healthcare, Utilities, Technology, and Professional Services.
        </p>
        <p style="font-size:16px; color:#6B5E52; line-height:1.85; margin-bottom:16px;">
            As organizations scale, they often face fragmented tools, disconnected systems, and limited visibility across key business functions. The challenge is rarely a lack of technology &#8212; it&#8217;s choosing the right solutions from too many options.
        </p>
        <p style="font-size:16px; color:#6B5E52; line-height:1.85; margin-bottom:28px;">
            From CRM, marketing automation, cloud adoption, and Data &amp; AI to Digital Engineering, Quality Engineering, and application performance monitoring, we help businesses identify, evaluate, and adopt the right technology solutions aligned to their goals.
        </p>
        <div style="display:flex; flex-direction:column; gap:10px; margin-bottom:32px;">
            <div style="display:flex; align-items:center; gap:12px; font-size:14px; color:#4A3728;">
                <span style="color:#E85D04; font-weight:700;">&#10003;</span> Vendor-neutral technology advisory
            </div>
            <div style="display:flex; align-items:center; gap:12px; font-size:14px; color:#4A3728;">
                <span style="color:#E85D04; font-weight:700;">&#10003;</span> Access to a curated ecosystem of global software providers
            </div>
            <div style="display:flex; align-items:center; gap:12px; font-size:14px; color:#4A3728;">
                <span style="color:#E85D04; font-weight:700;">&#10003;</span> Faster, simplified procurement
            </div>
            <div style="display:flex; align-items:center; gap:12px; font-size:14px; color:#4A3728;">
                <span style="color:#E85D04; font-weight:700;">&#10003;</span> Cost optimization and right-fit solutions
            </div>
        </div>
        <a target="_self" href="/About" class="btn-gradient" style="text-decoration:none;">Learn Our Story &#8594;</a>
    </div>
    """, unsafe_allow_html=True)

with about_right:
    st.markdown("""
    <div style="padding: 0 60px 60px 0; background: #FAF8F4;">
        <div class="about-img" style="height:460px; position:relative;">
            <img src="https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1200&q=90"
                 style="width:100%; height:100%; object-fit:cover; border-radius:20px;" alt="Bytewave Digital Team" />
            <div class="about-img-badge">
                <div class="about-img-badge-num">Est. 2024</div>
                <div class="about-img-badge-text">Noida, India</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ─── SOLUTIONS (TABBED) ──────────────────────────────────────────────────────
st.markdown("""
<div style="padding: 80px 60px 40px; background: #FFFFFF;">
    <div style="text-align:center; margin-bottom:48px;">
        <div class="section-label">What We Do</div>
        <h2 class="section-title">Our <span class="gradient-text">Solutions</span></h2>
        <p class="section-subtitle">We simplify complex technology choices so you can focus on outcomes.</p>
    </div>
</div>
""", unsafe_allow_html=True)

with st.container():

    tab1, tab2, tab3, tab4 = st.tabs([
        "&#129302; AI &amp; Automation", "&#128274; Cybersecurity &amp; Cloud Security", "&#128301; Observability &amp; APM", "&#128187; CRM &amp; Customer Experience"
    ])

    with tab1:
        col_img, col_txt = st.columns([1, 1])
        with col_img:
            st.markdown("""
            <div class="sol-img-card">
                <img src="https://images.unsplash.com/photo-1485827404703-89b55fcc595e?auto=format&fit=crop&w=900&q=90" alt="AI and Automation" />
                <div class="sol-img-overlay">
                    <span class="sol-img-tag">SOLUTION 01</span>
                    <div class="sol-img-icon">&#129302;</div>
                    <div class="sol-img-title">AI &amp; Automation Solutions</div>
                    <div class="sol-img-desc">Intelligent automation for modern enterprises</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col_txt:
            st.markdown("""
            <div style="padding-left:24px;">
                <div class="section-label" style="text-align:left;">Solution 01</div>
                <h3 style="font-size:30px; font-weight:800; color:#1C1107; margin-bottom:16px; letter-spacing:-0.5px;">AI &amp; Automation Solutions</h3>
                <p style="font-size:15px; color:#6B5E52; line-height:1.8; margin-bottom:20px;">
                    Leverage next-generation AI and automation tools that streamline workflows, enhance
                    productivity, and drive intelligent decision-making. We help organizations identify
                    the right AI platforms aligned to real business use cases.
                </p>
                <ul style="list-style:none; display:flex; flex-direction:column; gap:10px; margin-bottom:28px;">
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> AI readiness assessment</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Workflow automation platform evaluation</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Agentic AI &amp; LLM tool advisory</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Use-case alignment &amp; business value mapping</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Vendor-neutral AI solution shortlisting</li>
                </ul>
                <a target="_self" href="/Contact" class="btn-gradient" style="text-decoration:none;">Get AI Advisory &#8594;</a>
            </div>
            """, unsafe_allow_html=True)

    with tab2:
        col_img, col_txt = st.columns([1, 1])
        with col_img:
            st.markdown("""
            <div class="sol-img-card">
                <img src="https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=900&q=90" alt="Cybersecurity" />
                <div class="sol-img-overlay">
                    <span class="sol-img-tag">SOLUTION 02</span>
                    <div class="sol-img-icon">&#128274;</div>
                    <div class="sol-img-title">Cybersecurity &amp; Cloud Security</div>
                    <div class="sol-img-desc">Strengthen your security posture end-to-end</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col_txt:
            st.markdown("""
            <div style="padding-left:24px;">
                <div class="section-label" style="text-align:left;">Solution 02</div>
                <h3 style="font-size:30px; font-weight:800; color:#1C1107; margin-bottom:16px; letter-spacing:-0.5px;">Cybersecurity &amp; Cloud Security</h3>
                <p style="font-size:15px; color:#6B5E52; line-height:1.8; margin-bottom:20px;">
                    Protect your organization with the right security tools and posture. We help you
                    evaluate and adopt cybersecurity and cloud security solutions aligned to your
                    risk profile, compliance requirements, and IT environment.
                </p>
                <ul style="list-style:none; display:flex; flex-direction:column; gap:10px; margin-bottom:28px;">
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Security posture assessment</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Cloud security platform evaluation</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Endpoint &amp; network security advisory</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Compliance &amp; risk management tools</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Vendor-neutral security shortlisting</li>
                </ul>
                <a target="_self" href="/Contact" class="btn-gradient" style="text-decoration:none;">Get Security Advisory &#8594;</a>
            </div>
            """, unsafe_allow_html=True)

    with tab3:
        col_img, col_txt = st.columns([1, 1])
        with col_img:
            st.markdown("""
            <div class="sol-img-card">
                <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=900&q=90" alt="Observability and APM" />
                <div class="sol-img-overlay">
                    <span class="sol-img-tag">SOLUTION 03</span>
                    <div class="sol-img-icon">&#128301;</div>
                    <div class="sol-img-title">Observability &amp; APM</div>
                    <div class="sol-img-desc">Complete visibility across your IT stack</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col_txt:
            st.markdown("""
            <div style="padding-left:24px;">
                <div class="section-label" style="text-align:left;">Solution 03</div>
                <h3 style="font-size:30px; font-weight:800; color:#1C1107; margin-bottom:16px; letter-spacing:-0.5px;">Observability, Monitoring &amp; APM</h3>
                <p style="font-size:15px; color:#6B5E52; line-height:1.8; margin-bottom:20px;">
                    Gain complete visibility into your applications, infrastructure, and IT operations.
                    We help you choose observability and APM platforms that improve performance,
                    reliability, and faster issue resolution at scale.
                </p>
                <ul style="list-style:none; display:flex; flex-direction:column; gap:10px; margin-bottom:28px;">
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Application performance monitoring (APM)</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Infrastructure &amp; log management tools</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Real-time alerting &amp; incident management</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Cloud-scale observability platform evaluation</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Reliability engineering advisory</li>
                </ul>
                <a target="_self" href="/Contact" class="btn-gradient" style="text-decoration:none;">Get Observability Advisory &#8594;</a>
            </div>
            """, unsafe_allow_html=True)

    with tab4:
        col_img, col_txt = st.columns([1, 1])
        with col_img:
            st.markdown("""
            <div class="sol-img-card">
                <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=900&q=90" alt="CRM and Customer Experience" />
                <div class="sol-img-overlay">
                    <span class="sol-img-tag">SOLUTION 04</span>
                    <div class="sol-img-icon">&#129309;</div>
                    <div class="sol-img-title">CRM &amp; Customer Experience</div>
                    <div class="sol-img-desc">Drive engagement and revenue growth</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col_txt:
            st.markdown("""
            <div style="padding-left:24px;">
                <div class="section-label" style="text-align:left;">Solution 04</div>
                <h3 style="font-size:30px; font-weight:800; color:#1C1107; margin-bottom:16px; letter-spacing:-0.5px;">CRM &amp; Customer Experience Solutions</h3>
                <p style="font-size:15px; color:#6B5E52; line-height:1.8; margin-bottom:20px;">
                    Select CRM and customer experience platforms that align with your sales processes,
                    improve customer engagement, and drive revenue growth. We help you evaluate
                    scalability, integrations, and usability before committing.
                </p>
                <ul style="list-style:none; display:flex; flex-direction:column; gap:10px; margin-bottom:28px;">
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> CRM platform evaluation &amp; comparison</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Customer engagement tool advisory</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Integration compatibility mapping</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> User adoption &amp; change management</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Right-fit vendor shortlisting</li>
                </ul>
                <a target="_self" href="/Contact" class="btn-gradient" style="text-decoration:none;">Get CRM Advisory &#8594;</a>
            </div>
            """, unsafe_allow_html=True)


# ─── HOW WE WORK ─────────────────────────────────────────────────────────────
st.markdown("""
<div style="padding: 80px 60px 40px; background: #FAF8F4; text-align:center;">
    <div class="section-label">How We Work</div>
    <h2 class="section-title">Understand &#8594; Curate &#8594; <span class="gradient-text">Enable</span></h2>
    <p class="section-subtitle">A simple, proven approach to simplify your technology buying journey.</p>
</div>
""", unsafe_allow_html=True)

hw_c1, hw_c2, hw_c3 = st.columns(3)

with hw_c1:
    st.markdown("""
    <div style="padding: 0 12px 80px; background: #FAF8F4;">
        <div class="feature-card">
            <div class="feature-num">01</div>
            <div class="feature-icon">&#128269;</div>
            <div class="feature-title">Understand</div>
            <div class="feature-desc">We deep-dive into your business needs, current technology landscape, challenges, and growth goals to build a clear picture of what you truly need.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with hw_c2:
    st.markdown("""
    <div style="padding: 0 12px 80px; background: #FAF8F4;">
        <div class="feature-card">
            <div class="feature-num">02</div>
            <div class="feature-icon">&#129513;</div>
            <div class="feature-title">Curate</div>
            <div class="feature-desc">We shortlist the most relevant, best-fit technology solutions from our global partner ecosystem &#8212; cutting through the noise so you don't have to.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with hw_c3:
    st.markdown("""
    <div style="padding: 0 12px 80px; background: #FAF8F4;">
        <div class="feature-card">
            <div class="feature-num">03</div>
            <div class="feature-icon">&#128640;</div>
            <div class="feature-title">Enable</div>
            <div class="feature-desc">We help you make informed decisions, connect with the right vendors, and navigate procurement &#8212; ensuring you buy right the first time.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ─── CTA BANNER ──────────────────────────────────────────────────────────────
st.markdown("""
<section class="cta-banner">
    <h2 class="cta-title">Ready to Choose the <span class="gradient-text">Right Technology?</span></h2>
    <p class="cta-sub">Let's simplify your software buying journey.</p>
    <div class="cta-buttons">
        <a target="_self" href="/Contact" class="btn-gradient">&#128197; Schedule a Consultation</a>
        <a target="_self" href="/Solutions" class="btn-outline">&#128269; Explore Solutions</a>
    </div>
</section>
""", unsafe_allow_html=True)

footer()
