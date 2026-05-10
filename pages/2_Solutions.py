import streamlit as st
from PIL import Image
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import GLOBAL_CSS
from components import navbar, footer

st.set_page_config(
    page_title="Solutions — Bytewave Digital",
    page_icon=Image.open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "logo_favicon.png")),
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
navbar("Solutions")

# ─── PAGE HEADER ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <div class="page-header-watermark">SOLUTIONS</div>
    <div class="section-label">Technology Solutions</div>
    <h1 class="section-title">The Right Technology, <span class="gradient-text">Curated for You</span></h1>
    <p class="section-subtitle">
        We help you navigate a complex technology landscape &#8212; evaluating and comparing solutions
        so you can make confident, informed buying decisions.
    </p>
</div>
""", unsafe_allow_html=True)

# ─── ALL SOLUTIONS OVERVIEW GRID ─────────────────────────────────────────────
st.markdown("""
<div style="padding: 80px 60px 40px; background: #FAF8F4;">
    <div style="text-align:center; margin-bottom:48px;">
        <div class="section-label">All Solutions</div>
        <h2 class="section-title">Four Core Areas, <span class="gradient-text">One Partner</span></h2>
        <p class="section-subtitle">Choose a focus area below to explore in depth, or scroll down for the tabbed deep-dives.</p>
    </div>
</div>
""", unsafe_allow_html=True)

with st.container():

    row1_c1, row1_c2 = st.columns(2)

    with row1_c1:
        st.markdown("""
        <div class="sol-img-card" style="height:240px; margin-bottom:24px;">
            <img src="https://images.unsplash.com/photo-1485827404703-89b55fcc595e?auto=format&fit=crop&w=900&q=90" alt="AI and Automation" />
            <div class="sol-img-overlay">
                <span class="sol-img-tag">01</span>
                <div class="sol-img-icon">&#129302;</div>
                <div class="sol-img-title">AI &amp; Automation Solutions</div>
                <div class="sol-img-desc">Intelligent automation for modern enterprises</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with row1_c2:
        st.markdown("""
        <div class="sol-img-card" style="height:240px; margin-bottom:24px;">
            <img src="https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=900&q=90" alt="Cybersecurity" />
            <div class="sol-img-overlay">
                <span class="sol-img-tag">02</span>
                <div class="sol-img-icon">&#128274;</div>
                <div class="sol-img-title">Cybersecurity &amp; Cloud Security</div>
                <div class="sol-img-desc">Strengthen your security posture end-to-end</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    row2_c1, row2_c2 = st.columns(2)

    with row2_c1:
        st.markdown("""
        <div class="sol-img-card" style="height:240px; margin-bottom:40px;">
            <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=900&q=90" alt="Observability and APM" />
            <div class="sol-img-overlay">
                <span class="sol-img-tag">03</span>
                <div class="sol-img-icon">&#128301;</div>
                <div class="sol-img-title">Observability &amp; APM</div>
                <div class="sol-img-desc">Complete visibility across your IT stack</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with row2_c2:
        st.markdown("""
        <div class="sol-img-card" style="height:240px; margin-bottom:40px;">
            <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=900&q=90" alt="CRM and Customer Experience" />
            <div class="sol-img-overlay">
                <span class="sol-img-tag">04</span>
                <div class="sol-img-icon">&#129309;</div>
                <div class="sol-img-title">CRM &amp; Customer Experience</div>
                <div class="sol-img-desc">Drive engagement and revenue growth</div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ─── TABBED DEEP DIVES ────────────────────────────────────────────────────────
st.markdown("""
<div style="padding: 60px 60px 24px; background: #FFFFFF; text-align:center;">
    <div class="section-label">Deep Dive</div>
    <h2 class="section-title">Explore Each <span class="gradient-text">Solution Category</span></h2>
    <p class="section-subtitle">Select a tab to learn what we evaluate, why it matters, and how we help you choose right.</p>
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
                <h3 style="font-size:28px; font-weight:800; color:#1C1107; margin-bottom:14px; letter-spacing:-0.5px;">AI &amp; Automation Solutions</h3>
                <p style="font-size:15px; color:#6B5E52; line-height:1.8; margin-bottom:16px;">
                    Leverage next-generation AI and automation tools that streamline workflows, enhance productivity, and drive intelligent decision-making. We help organizations identify the right AI platforms aligned to real business use cases and deliver measurable outcomes.
                </p>
                <div style="background:rgba(232,93,4,0.06); border-left:3px solid #E85D04; border-radius:0 8px 8px 0; padding:14px 18px; margin-bottom:20px;">
                    <p style="font-size:14px; color:#4A3728; line-height:1.7; margin:0; font-style:italic;">
                        Why you need this: AI adoption without a clear use-case strategy leads to expensive pilots that never scale. We anchor your AI journey to measurable business outcomes.
                    </p>
                </div>
                <div style="font-size:13px; font-weight:700; color:#E85D04; letter-spacing:2px; text-transform:uppercase; margin-bottom:12px;">Key Areas We Evaluate</div>
                <ul style="list-style:none; display:flex; flex-direction:column; gap:8px; margin-bottom:28px;">
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> AI readiness assessment</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Workflow automation platform evaluation</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Agentic AI &amp; LLM tool advisory</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Use-case alignment &amp; business value mapping</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Integration with existing data infrastructure</li>
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
                <h3 style="font-size:28px; font-weight:800; color:#1C1107; margin-bottom:14px; letter-spacing:-0.5px;">Cybersecurity &amp; Cloud Security</h3>
                <p style="font-size:15px; color:#6B5E52; line-height:1.8; margin-bottom:16px;">
                    Protect your organization with the right security tools and posture. We help you evaluate and adopt cybersecurity and cloud security solutions aligned to your risk profile, compliance requirements, and IT environment.
                </p>
                <div style="background:rgba(124,58,237,0.06); border-left:3px solid #7C3AED; border-radius:0 8px 8px 0; padding:14px 18px; margin-bottom:20px;">
                    <p style="font-size:14px; color:#4A3728; line-height:1.7; margin:0; font-style:italic;">
                        Why you need this: Cyber threats are growing in sophistication. The right security stack is the foundation of operational trust, regulatory compliance, and business continuity.
                    </p>
                </div>
                <div style="font-size:13px; font-weight:700; color:#E85D04; letter-spacing:2px; text-transform:uppercase; margin-bottom:12px;">Key Areas We Evaluate</div>
                <ul style="list-style:none; display:flex; flex-direction:column; gap:8px; margin-bottom:28px;">
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Security posture assessment &amp; gap analysis</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Cloud security platform evaluation</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Endpoint &amp; network security advisory</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> SIEM, SOC &amp; threat detection tools</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Compliance &amp; regulatory alignment</li>
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
                <h3 style="font-size:28px; font-weight:800; color:#1C1107; margin-bottom:14px; letter-spacing:-0.5px;">Observability, Monitoring &amp; APM</h3>
                <p style="font-size:15px; color:#6B5E52; line-height:1.8; margin-bottom:16px;">
                    Gain complete visibility into your applications, infrastructure, and IT operations. We help you choose observability and APM platforms that improve performance, reliability, and faster issue resolution at scale.
                </p>
                <div style="background:rgba(217,119,6,0.06); border-left:3px solid #D97706; border-radius:0 8px 8px 0; padding:14px 18px; margin-bottom:20px;">
                    <p style="font-size:14px; color:#4A3728; line-height:1.7; margin:0; font-style:italic;">
                        Why you need this: In cloud environments, downtime costs thousands per minute. Observability is the foundation of reliability engineering and proactive IT operations.
                    </p>
                </div>
                <div style="font-size:13px; font-weight:700; color:#E85D04; letter-spacing:2px; text-transform:uppercase; margin-bottom:12px;">Key Areas We Evaluate</div>
                <ul style="list-style:none; display:flex; flex-direction:column; gap:8px; margin-bottom:28px;">
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Application performance monitoring (APM)</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Infrastructure &amp; log management tools</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Distributed tracing &amp; real-time analytics</li>
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
                <h3 style="font-size:28px; font-weight:800; color:#1C1107; margin-bottom:14px; letter-spacing:-0.5px;">CRM &amp; Customer Experience Solutions</h3>
                <p style="font-size:15px; color:#6B5E52; line-height:1.8; margin-bottom:16px;">
                    Select CRM and customer experience platforms that align with your sales processes, improve customer engagement, and drive revenue growth. We help you evaluate scalability, integrations, and usability before committing to the right long-term fit.
                </p>
                <div style="background:rgba(232,93,4,0.06); border-left:3px solid #E85D04; border-radius:0 8px 8px 0; padding:14px 18px; margin-bottom:20px;">
                    <p style="font-size:14px; color:#4A3728; line-height:1.7; margin:0; font-style:italic;">
                        Why you need this: Most organizations waste 6&#8211;12 months on the wrong CRM before switching. We shortcut that process with a structured, data-driven evaluation.
                    </p>
                </div>
                <div style="font-size:13px; font-weight:700; color:#E85D04; letter-spacing:2px; text-transform:uppercase; margin-bottom:12px;">Key Areas We Evaluate</div>
                <ul style="list-style:none; display:flex; flex-direction:column; gap:8px; margin-bottom:28px;">
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> CRM platform evaluation &amp; comparison</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Customer engagement tool advisory</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Integration compatibility &amp; stack mapping</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> User adoption &amp; onboarding assessment</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Commercial comparison &amp; TCO analysis</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Right-fit vendor shortlisting</li>
                </ul>
                <a target="_self" href="/Contact" class="btn-gradient" style="text-decoration:none;">Get CRM Advisory &#8594;</a>
            </div>
            """, unsafe_allow_html=True)


# ─── CTA ─────────────────────────────────────────────────────────────────────
st.markdown("""
<section class="cta-banner">
    <h2 class="cta-title">Not Sure Which Solution <span class="gradient-text">You Need?</span></h2>
    <p class="cta-sub">Talk to our experts and we'll help you identify the right technology fit for your business.</p>
    <div class="cta-buttons">
        <a target="_self" href="/Contact" class="btn-gradient">&#128172; Talk to an Expert</a>
        <a target="_self" href="/Services" class="btn-outline">&#9881;&#65039; See How We Help</a>
    </div>
</section>
""", unsafe_allow_html=True)

footer()
