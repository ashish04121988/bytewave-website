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
            <div class="hero-eyebrow">Vendor-Neutral IT Software Reseller</div>
            <h1 class="hero-h1">
                Simplifying Technology Decisions.<br>
                <span class="gradient-text">Maximizing Business Outcomes.</span>
            </h1>
            <p class="hero-sub">
                We help businesses cut through complexity and choose the right SaaS, cloud, and IT solutions &#8212; without the noise.
            </p>
            <p class="hero-sub">
                Built on the legacy of Fundoo Data, Bytewave Digital is a vendor-neutral IT software reseller helping you identify and procure the right technology &#8212; faster, smarter, and without the noise.
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
            <div class="stat-badge-number">15+</div>
            <div class="stat-badge-label">Technology Partners</div>
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
            <div class="stat-number">6</div>
            <div class="stat-label">Solution Categories</div>
            <div class="stat-sublabel">CRM, Cloud, AI &amp; more</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">15+</div>
            <div class="stat-label">Technology Partners</div>
            <div class="stat-sublabel">global ecosystem</div>
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
            Bytewave Digital was born from the legacy of <strong style="color:#E85D04;">Fundoo Data</strong> &#8212; where we helped
            organizations with deep corporate intelligence and business insights. Through these engagements,
            we worked closely with SMEs, mid-size companies, and large enterprises, gaining firsthand visibility into how technology decisions are made.
        </p>
        <p style="font-size:16px; color:#6B5E52; line-height:1.85; margin-bottom:28px;">
            We identified a consistent gap &#8212; organizations were overwhelmed with choices and struggled to find the right-fit technology solutions aligned to their business needs. <strong style="color:#1C1107;">Bytewave Digital was created to simplify that journey.</strong>
        </p>
        <div style="display:flex; flex-direction:column; gap:10px; margin-bottom:32px;">
            <div style="display:flex; align-items:center; gap:12px; font-size:14px; color:#4A3728;">
                <span style="color:#E85D04; font-weight:700;">&#10003;</span> Vendor-neutral technology advisory
            </div>
            <div style="display:flex; align-items:center; gap:12px; font-size:14px; color:#4A3728;">
                <span style="color:#E85D04; font-weight:700;">&#10003;</span> Access to leading global software providers
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

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "&#128187; CRM", "&#128226; Marketing", "&#128301; Observability", "&#9729;&#65039; Cloud &amp; IT", "&#129302; AI", "&#128101; HR &amp; Finance"
    ])

    with tab1:
        col_img, col_txt = st.columns([1, 1])
        with col_img:
            st.markdown("""
            <div class="sol-img-card">
                <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=900&q=90" alt="CRM Solutions" />
                <div class="sol-img-overlay">
                    <span class="sol-img-tag">SOLUTION 01</span>
                    <div class="sol-img-icon">&#129309;</div>
                    <div class="sol-img-title">CRM Solutions</div>
                    <div class="sol-img-desc">Drive sales excellence through the right CRM platform</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col_txt:
            st.markdown("""
            <div style="padding-left:24px;">
                <div class="section-label" style="text-align:left;">Solution 01</div>
                <h3 style="font-size:30px; font-weight:800; color:#1C1107; margin-bottom:16px; letter-spacing:-0.5px;">CRM Solutions</h3>
                <p style="font-size:15px; color:#6B5E52; line-height:1.8; margin-bottom:20px;">
                    Select CRM platforms that align with your sales processes, improve customer engagement,
                    and drive revenue growth. We help you evaluate scalability, integrations, and usability
                    before making a decision.
                </p>
                <ul style="list-style:none; display:flex; flex-direction:column; gap:10px; margin-bottom:28px;">
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Scalability evaluation &amp; comparison</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Integration compatibility mapping</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> User adoption assessment</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Commercial comparison &amp; vendor shortlisting</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Right-fit recommendation</li>
                </ul>
                <a target="_self" href="/Contact" class="btn-gradient" style="text-decoration:none;">Get CRM Advisory &#8594;</a>
            </div>
            """, unsafe_allow_html=True)

    with tab2:
        col_img, col_txt = st.columns([1, 1])
        with col_img:
            st.markdown("""
            <div class="sol-img-card">
                <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=900&q=90" alt="Marketing Automation" />
                <div class="sol-img-overlay">
                    <span class="sol-img-tag">SOLUTION 02</span>
                    <div class="sol-img-icon">&#128226;</div>
                    <div class="sol-img-title">Marketing Automation</div>
                    <div class="sol-img-desc">Navigate the martech landscape with confidence</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col_txt:
            st.markdown("""
            <div style="padding-left:24px;">
                <div class="section-label" style="text-align:left;">Solution 02</div>
                <h3 style="font-size:30px; font-weight:800; color:#1C1107; margin-bottom:16px; letter-spacing:-0.5px;">Marketing Automation Tools</h3>
                <p style="font-size:15px; color:#6B5E52; line-height:1.8; margin-bottom:20px;">
                    Navigate the crowded martech landscape with confidence. We guide you in choosing platforms
                    that enhance lead generation, campaign management, and customer journey orchestration
                    aligned to your marketing strategy.
                </p>
                <ul style="list-style:none; display:flex; flex-direction:column; gap:10px; margin-bottom:28px;">
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Lead generation platforms</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Campaign management tools</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Customer journey orchestration</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Martech stack evaluation</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> ROI-focused selection</li>
                </ul>
                <a target="_self" href="/Contact" class="btn-gradient" style="text-decoration:none;">Get MarTech Advisory &#8594;</a>
            </div>
            """, unsafe_allow_html=True)

    with tab3:
        col_img, col_txt = st.columns([1, 1])
        with col_img:
            st.markdown("""
            <div class="sol-img-card">
                <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=900&q=90" alt="Observability" />
                <div class="sol-img-overlay">
                    <span class="sol-img-tag">SOLUTION 03</span>
                    <div class="sol-img-icon">&#128301;</div>
                    <div class="sol-img-title">Observability</div>
                    <div class="sol-img-desc">Complete visibility at cloud scale</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col_txt:
            st.markdown("""
            <div style="padding-left:24px;">
                <div class="section-label" style="text-align:left;">Solution 03</div>
                <h3 style="font-size:30px; font-weight:800; color:#1C1107; margin-bottom:16px; letter-spacing:-0.5px;">Observability for Cloud-Scale Apps</h3>
                <p style="font-size:15px; color:#6B5E52; line-height:1.8; margin-bottom:20px;">
                    Gain complete visibility into your applications and infrastructure. We help you choose
                    observability platforms that ensure performance, reliability, and faster issue resolution
                    at cloud scale &#8212; so your teams can act on insights, not guesses.
                </p>
                <ul style="list-style:none; display:flex; flex-direction:column; gap:10px; margin-bottom:28px;">
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Application monitoring</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Infrastructure visibility</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Performance analytics</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Reliability engineering tools</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Cloud-scale platform evaluation</li>
                </ul>
                <a target="_self" href="/Contact" class="btn-gradient" style="text-decoration:none;">Get Observability Advisory &#8594;</a>
            </div>
            """, unsafe_allow_html=True)

    with tab4:
        col_img, col_txt = st.columns([1, 1])
        with col_img:
            st.markdown("""
            <div class="sol-img-card">
                <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=900&q=90" alt="Cloud and IT" />
                <div class="sol-img-overlay">
                    <span class="sol-img-tag">SOLUTION 04</span>
                    <div class="sol-img-icon">&#9729;&#65039;</div>
                    <div class="sol-img-title">Cloud &amp; IT Solutions</div>
                    <div class="sol-img-desc">Scale with confidence in the cloud</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col_txt:
            st.markdown("""
            <div style="padding-left:24px;">
                <div class="section-label" style="text-align:left;">Solution 04</div>
                <h3 style="font-size:30px; font-weight:800; color:#1C1107; margin-bottom:16px; letter-spacing:-0.5px;">Cloud &amp; IT Solutions</h3>
                <p style="font-size:15px; color:#6B5E52; line-height:1.8; margin-bottom:20px;">
                    Choose the right cloud platforms and infrastructure tools to support scalability and performance.
                    We help you evaluate public, private, and hybrid options aligned to your business goals and budget.
                </p>
                <ul style="list-style:none; display:flex; flex-direction:column; gap:10px; margin-bottom:28px;">
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Public, private &amp; hybrid cloud evaluation</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Infrastructure comparison</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Cost optimization</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Scalability planning</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Vendor negotiation support</li>
                </ul>
                <a target="_self" href="/Contact" class="btn-gradient" style="text-decoration:none;">Get Cloud Advisory &#8594;</a>
            </div>
            """, unsafe_allow_html=True)

    with tab5:
        col_img, col_txt = st.columns([1, 1])
        with col_img:
            st.markdown("""
            <div class="sol-img-card">
                <img src="https://images.unsplash.com/photo-1485827404703-89b55fcc595e?auto=format&fit=crop&w=900&q=90" alt="AI Solutions" />
                <div class="sol-img-overlay">
                    <span class="sol-img-tag">SOLUTION 05</span>
                    <div class="sol-img-icon">&#129302;</div>
                    <div class="sol-img-title">Agentic AI Solutions</div>
                    <div class="sol-img-desc">Intelligent automation for modern businesses</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col_txt:
            st.markdown("""
            <div style="padding-left:24px;">
                <div class="section-label" style="text-align:left;">Solution 05</div>
                <h3 style="font-size:30px; font-weight:800; color:#1C1107; margin-bottom:16px; letter-spacing:-0.5px;">Agentic AI Solutions</h3>
                <p style="font-size:15px; color:#6B5E52; line-height:1.8; margin-bottom:20px;">
                    Leverage next-generation AI tools that automate workflows, enhance productivity, and drive
                    intelligent decision-making. We help you identify AI platforms that align with your use
                    cases and deliver measurable business value.
                </p>
                <ul style="list-style:none; display:flex; flex-direction:column; gap:10px; margin-bottom:28px;">
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Workflow automation AI platforms</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Decision-making &amp; productivity tools</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Use-case alignment</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> AI readiness assessment</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Business value mapping</li>
                </ul>
                <a target="_self" href="/Contact" class="btn-gradient" style="text-decoration:none;">Get AI Advisory &#8594;</a>
            </div>
            """, unsafe_allow_html=True)

    with tab6:
        col_img, col_txt = st.columns([1, 1])
        with col_img:
            st.markdown("""
            <div class="sol-img-card">
                <img src="https://images.unsplash.com/photo-1521737711867-e3b97375f902?auto=format&fit=crop&w=900&q=90" alt="HR and Finance" />
                <div class="sol-img-overlay">
                    <span class="sol-img-tag">SOLUTION 06</span>
                    <div class="sol-img-icon">&#128101;</div>
                    <div class="sol-img-title">HR &amp; Finance Software</div>
                    <div class="sol-img-desc">Smarter workforce and financial management</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col_txt:
            st.markdown("""
            <div style="padding-left:24px;">
                <div class="section-label" style="text-align:left;">Solution 06</div>
                <h3 style="font-size:30px; font-weight:800; color:#1C1107; margin-bottom:16px; letter-spacing:-0.5px;">HR &amp; Finance Software</h3>
                <p style="font-size:15px; color:#6B5E52; line-height:1.8; margin-bottom:20px;">
                    Enable smarter workforce and financial management with the right tools. We help you
                    identify solutions that improve operational efficiency, compliance, and decision-making
                    across your HR and finance functions.
                </p>
                <ul style="list-style:none; display:flex; flex-direction:column; gap:10px; margin-bottom:28px;">
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Workforce management platforms</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Financial reporting tools</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Payroll &amp; compliance solutions</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Operational efficiency evaluation</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Compliance alignment</li>
                </ul>
                <a target="_self" href="/Contact" class="btn-gradient" style="text-decoration:none;">Get HR &amp; Finance Advisory &#8594;</a>
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

# ─── TESTIMONIALS ────────────────────────────────────────────────────────────
st.markdown("""
<div style="padding: 80px 60px 40px; background: #FFFFFF; text-align:center;">
    <div class="section-label">Client Stories</div>
    <h2 class="section-title">What Our <span class="gradient-text">Clients Say</span></h2>
    <p class="section-subtitle">Real outcomes from organizations who chose the right technology with Bytewave.</p>
</div>
""", unsafe_allow_html=True)

t_c1, t_c2, t_c3 = st.columns(3)

with t_c1:
    st.markdown("""
    <div style="padding: 0 12px 80px; background: #FFFFFF;">
        <div class="testimonial-card">
            <div class="testimonial-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
            <div class="testimonial-text">
                "Bytewave Digital saved us months of evaluation time. They understood our sales process deeply and recommended a CRM that our team actually loves using. The pipeline has grown by 3x in just two quarters."
            </div>
            <div class="testimonial-author">
                <div class="testimonial-avatar">RS</div>
                <div>
                    <div class="testimonial-name">Rajan Sharma</div>
                    <div class="testimonial-role">VP Sales, Infoveda Technologies, Bengaluru</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with t_c2:
    st.markdown("""
    <div style="padding: 0 12px 80px; background: #FFFFFF;">
        <div class="testimonial-card">
            <div class="testimonial-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
            <div class="testimonial-text">
                "We were overwhelmed by cloud options. The Bytewave team cut through the complexity, mapped our exact needs, and helped us choose a platform that reduced our IT costs by nearly 40%."
            </div>
            <div class="testimonial-author">
                <div class="testimonial-avatar">PM</div>
                <div>
                    <div class="testimonial-name">Priya Mehta</div>
                    <div class="testimonial-role">CTO, Nexora Fintech, Mumbai</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with t_c3:
    st.markdown("""
    <div style="padding: 0 12px 80px; background: #FFFFFF;">
        <div class="testimonial-card">
            <div class="testimonial-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
            <div class="testimonial-text">
                "As a mid-size manufacturing firm, we never had a dedicated technology advisor. Bytewave filled that role perfectly &#8212; vendor-neutral, fast, and incredibly thorough in their evaluation process."
            </div>
            <div class="testimonial-author">
                <div class="testimonial-avatar">AK</div>
                <div>
                    <div class="testimonial-name">Arjun Kapoor</div>
                    <div class="testimonial-role">MD, Aagman Industries, Noida</div>
                </div>
            </div>
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
