import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import GLOBAL_CSS
from components import navbar, footer

st.set_page_config(
    page_title="Solutions — Bytewave Digital",
    page_icon="⚡",
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
        <h2 class="section-title">Six Categories, <span class="gradient-text">One Partner</span></h2>
        <p class="section-subtitle">Choose a category below to explore in depth, or scroll down for the tabbed deep-dives.</p>
    </div>
</div>
""", unsafe_allow_html=True)

with st.container():

    row1_c1, row1_c2, row1_c3 = st.columns(3)

    with row1_c1:
        st.markdown("""
        <div class="sol-img-card" style="height:240px; margin-bottom:24px;">
            <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=900&q=90" alt="CRM" />
            <div class="sol-img-overlay">
                <span class="sol-img-tag">01</span>
                <div class="sol-img-icon">&#129309;</div>
                <div class="sol-img-title">CRM Solutions</div>
                <div class="sol-img-desc">Drive sales excellence &amp; revenue growth</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with row1_c2:
        st.markdown("""
        <div class="sol-img-card" style="height:240px; margin-bottom:24px;">
            <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=900&q=90" alt="Marketing" />
            <div class="sol-img-overlay">
                <span class="sol-img-tag">02</span>
                <div class="sol-img-icon">&#128226;</div>
                <div class="sol-img-title">Marketing Automation</div>
                <div class="sol-img-desc">Navigate the martech landscape confidently</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with row1_c3:
        st.markdown("""
        <div class="sol-img-card" style="height:240px; margin-bottom:24px;">
            <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=900&q=90" alt="Cloud" />
            <div class="sol-img-overlay">
                <span class="sol-img-tag">03</span>
                <div class="sol-img-icon">&#9729;&#65039;</div>
                <div class="sol-img-title">Cloud &amp; IT Solutions</div>
                <div class="sol-img-desc">Scale with confidence in the cloud</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    row2_c1, row2_c2, row2_c3 = st.columns(3)

    with row2_c1:
        st.markdown("""
        <div class="sol-img-card" style="height:240px; margin-bottom:40px;">
            <img src="https://images.unsplash.com/photo-1485827404703-89b55fcc595e?auto=format&fit=crop&w=900&q=90" alt="AI" />
            <div class="sol-img-overlay">
                <span class="sol-img-tag">04</span>
                <div class="sol-img-icon">&#129302;</div>
                <div class="sol-img-title">Agentic AI Solutions</div>
                <div class="sol-img-desc">Intelligent automation for your workflows</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with row2_c2:
        st.markdown("""
        <div class="sol-img-card" style="height:240px; margin-bottom:40px;">
            <img src="https://images.unsplash.com/photo-1521737711867-e3b97375f902?auto=format&fit=crop&w=900&q=90" alt="HR" />
            <div class="sol-img-overlay">
                <span class="sol-img-tag">05</span>
                <div class="sol-img-icon">&#128101;</div>
                <div class="sol-img-title">HR &amp; Finance Software</div>
                <div class="sol-img-desc">Smarter workforce &amp; financial management</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with row2_c3:
        st.markdown("""
        <div class="sol-img-card" style="height:240px; margin-bottom:40px;">
            <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=900&q=90" alt="Observability" />
            <div class="sol-img-overlay">
                <span class="sol-img-tag">06</span>
                <div class="sol-img-icon">&#128301;</div>
                <div class="sol-img-title">Observability</div>
                <div class="sol-img-desc">Complete visibility at cloud scale</div>
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

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "&#128187; CRM", "&#128226; Marketing", "&#9729;&#65039; Cloud &amp; IT", "&#129302; AI", "&#128101; HR &amp; Finance", "&#128301; Observability"
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
                <h3 style="font-size:28px; font-weight:800; color:#1C1107; margin-bottom:14px; letter-spacing:-0.5px;">CRM Solutions</h3>
                <p style="font-size:15px; color:#6B5E52; line-height:1.8; margin-bottom:16px;">
                    Empower your sales organization with CRM platforms that drive pipeline visibility, improve customer engagement, and accelerate revenue growth. We help you evaluate scalability, integrations, and user experience to ensure the right long-term fit for your business.
                </p>
                <div style="background:rgba(232,93,4,0.06); border-left:3px solid #E85D04; border-radius:0 8px 8px 0; padding:14px 18px; margin-bottom:20px;">
                    <p style="font-size:14px; color:#4A3728; line-height:1.7; margin:0; font-style:italic;">
                        Why you need this: Most organizations waste 6&#8211;12 months on the wrong CRM before switching. We shortcut that process with data-driven evaluation.
                    </p>
                </div>
                <div style="font-size:13px; font-weight:700; color:#E85D04; letter-spacing:2px; text-transform:uppercase; margin-bottom:12px;">Key Features We Evaluate</div>
                <ul style="list-style:none; display:flex; flex-direction:column; gap:8px; margin-bottom:28px;">
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Scalability &amp; performance benchmarks</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Integration compatibility with existing stack</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> User adoption &amp; onboarding experience</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Commercial comparison &amp; TCO analysis</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Vendor shortlisting &amp; right-fit recommendation</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Compliance &amp; data security alignment</li>
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
                <h3 style="font-size:28px; font-weight:800; color:#1C1107; margin-bottom:14px; letter-spacing:-0.5px;">Marketing Automation Tools</h3>
                <p style="font-size:15px; color:#6B5E52; line-height:1.8; margin-bottom:16px;">
                    Optimize your demand generation with marketing automation platforms that enable personalized engagement at scale. We help you identify solutions that improve lead nurturing, campaign effectiveness, and conversion rates &#8212; driving measurable marketing ROI.
                </p>
                <div style="background:rgba(124,58,237,0.06); border-left:3px solid #7C3AED; border-radius:0 8px 8px 0; padding:14px 18px; margin-bottom:20px;">
                    <p style="font-size:14px; color:#4A3728; line-height:1.7; margin:0; font-style:italic;">
                        Why you need this: The martech landscape has 10,000+ tools. We narrow it down to the 3 that truly fit your strategy and budget.
                    </p>
                </div>
                <div style="font-size:13px; font-weight:700; color:#E85D04; letter-spacing:2px; text-transform:uppercase; margin-bottom:12px;">Key Features We Evaluate</div>
                <ul style="list-style:none; display:flex; flex-direction:column; gap:8px; margin-bottom:28px;">
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Lead generation &amp; nurturing capabilities</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Campaign management &amp; automation flows</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Customer journey orchestration</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Martech stack compatibility</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Integration mapping with CRM</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> ROI-focused selection framework</li>
                </ul>
                <a target="_self" href="/Contact" class="btn-gradient" style="text-decoration:none;">Get MarTech Advisory &#8594;</a>
            </div>
            """, unsafe_allow_html=True)

    with tab3:
        col_img, col_txt = st.columns([1, 1])
        with col_img:
            st.markdown("""
            <div class="sol-img-card">
                <img src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=900&q=90" alt="Cloud and IT" />
                <div class="sol-img-overlay">
                    <span class="sol-img-tag">SOLUTION 03</span>
                    <div class="sol-img-icon">&#9729;&#65039;</div>
                    <div class="sol-img-title">Cloud &amp; IT Solutions</div>
                    <div class="sol-img-desc">Scale with confidence in the cloud</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col_txt:
            st.markdown("""
            <div style="padding-left:24px;">
                <div class="section-label" style="text-align:left;">Solution 03</div>
                <h3 style="font-size:28px; font-weight:800; color:#1C1107; margin-bottom:14px; letter-spacing:-0.5px;">Cloud &amp; IT Solutions</h3>
                <p style="font-size:15px; color:#6B5E52; line-height:1.8; margin-bottom:16px;">
                    Build a scalable and resilient IT foundation with the right cloud and infrastructure solutions. We help you navigate multi-cloud environments, optimize costs, and choose technologies that support performance, security, and long-term agility.
                </p>
                <div style="background:rgba(217,119,6,0.06); border-left:3px solid #D97706; border-radius:0 8px 8px 0; padding:14px 18px; margin-bottom:20px;">
                    <p style="font-size:14px; color:#4A3728; line-height:1.7; margin:0; font-style:italic;">
                        Why you need this: Cloud decisions lock you in for years. A wrong choice costs 2&#8211;3x more to fix. We help you decide once &#8212; correctly.
                    </p>
                </div>
                <div style="font-size:13px; font-weight:700; color:#E85D04; letter-spacing:2px; text-transform:uppercase; margin-bottom:12px;">Key Features We Evaluate</div>
                <ul style="list-style:none; display:flex; flex-direction:column; gap:8px; margin-bottom:28px;">
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Public, private &amp; hybrid cloud comparison</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Infrastructure &amp; networking requirements</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Cost optimization &amp; rightsizing</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Scalability &amp; performance planning</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Security &amp; compliance posture</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Vendor negotiation support</li>
                </ul>
                <a target="_self" href="/Contact" class="btn-gradient" style="text-decoration:none;">Get Cloud Advisory &#8594;</a>
            </div>
            """, unsafe_allow_html=True)

    with tab4:
        col_img, col_txt = st.columns([1, 1])
        with col_img:
            st.markdown("""
            <div class="sol-img-card">
                <img src="https://images.unsplash.com/photo-1485827404703-89b55fcc595e?auto=format&fit=crop&w=900&q=90" alt="AI Solutions" />
                <div class="sol-img-overlay">
                    <span class="sol-img-tag">SOLUTION 04</span>
                    <div class="sol-img-icon">&#129302;</div>
                    <div class="sol-img-title">Agentic AI Solutions</div>
                    <div class="sol-img-desc">Intelligent automation for modern businesses</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col_txt:
            st.markdown("""
            <div style="padding-left:24px;">
                <div class="section-label" style="text-align:left;">Solution 04</div>
                <h3 style="font-size:28px; font-weight:800; color:#1C1107; margin-bottom:14px; letter-spacing:-0.5px;">Agentic AI Solutions</h3>
                <p style="font-size:15px; color:#6B5E52; line-height:1.8; margin-bottom:16px;">
                    Leverage next-generation AI solutions that go beyond automation to enable intelligent decision-making and task execution. We help you identify use cases and select platforms that drive productivity, innovation, and competitive advantage.
                </p>
                <div style="background:rgba(232,93,4,0.06); border-left:3px solid #E85D04; border-radius:0 8px 8px 0; padding:14px 18px; margin-bottom:20px;">
                    <p style="font-size:14px; color:#4A3728; line-height:1.7; margin:0; font-style:italic;">
                        Why you need this: AI adoption without a clear use-case strategy leads to expensive pilots that never scale. We anchor your AI journey to measurable outcomes.
                    </p>
                </div>
                <div style="font-size:13px; font-weight:700; color:#E85D04; letter-spacing:2px; text-transform:uppercase; margin-bottom:12px;">Key Features We Evaluate</div>
                <ul style="list-style:none; display:flex; flex-direction:column; gap:8px; margin-bottom:28px;">
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Workflow automation AI platforms</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Decision intelligence &amp; analytics tools</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Productivity enhancement evaluation</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Use-case alignment &amp; AI readiness</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Integration with existing data infrastructure</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Business value mapping &amp; ROI projection</li>
                </ul>
                <a target="_self" href="/Contact" class="btn-gradient" style="text-decoration:none;">Get AI Advisory &#8594;</a>
            </div>
            """, unsafe_allow_html=True)

    with tab5:
        col_img, col_txt = st.columns([1, 1])
        with col_img:
            st.markdown("""
            <div class="sol-img-card">
                <img src="https://images.unsplash.com/photo-1521737711867-e3b97375f902?auto=format&fit=crop&w=900&q=90" alt="HR and Finance" />
                <div class="sol-img-overlay">
                    <span class="sol-img-tag">SOLUTION 05</span>
                    <div class="sol-img-icon">&#128101;</div>
                    <div class="sol-img-title">HR &amp; Finance Software</div>
                    <div class="sol-img-desc">Smarter workforce &amp; financial management</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col_txt:
            st.markdown("""
            <div style="padding-left:24px;">
                <div class="section-label" style="text-align:left;">Solution 05</div>
                <h3 style="font-size:28px; font-weight:800; color:#1C1107; margin-bottom:14px; letter-spacing:-0.5px;">HR &amp; Finance Software</h3>
                <p style="font-size:15px; color:#6B5E52; line-height:1.8; margin-bottom:16px;">
                    Streamline core business operations with modern HR and finance solutions that enhance efficiency, ensure compliance, and provide real-time insights. We guide you in selecting platforms that align with your organizational structure and growth plans.
                </p>
                <div style="background:rgba(124,58,237,0.06); border-left:3px solid #7C3AED; border-radius:0 8px 8px 0; padding:14px 18px; margin-bottom:20px;">
                    <p style="font-size:14px; color:#4A3728; line-height:1.7; margin:0; font-style:italic;">
                        Why you need this: HR and finance software directly impacts compliance risk and employee experience. The stakes are too high to get it wrong.
                    </p>
                </div>
                <div style="font-size:13px; font-weight:700; color:#E85D04; letter-spacing:2px; text-transform:uppercase; margin-bottom:12px;">Key Features We Evaluate</div>
                <ul style="list-style:none; display:flex; flex-direction:column; gap:8px; margin-bottom:28px;">
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Workforce management &amp; HRMS platforms</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Financial reporting &amp; ERP tools</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Payroll processing &amp; compliance</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Recruitment &amp; talent management</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Regulatory alignment &amp; audit readiness</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Multi-currency &amp; multi-entity support</li>
                </ul>
                <a target="_self" href="/Contact" class="btn-gradient" style="text-decoration:none;">Get HR &amp; Finance Advisory &#8594;</a>
            </div>
            """, unsafe_allow_html=True)

    with tab6:
        col_img, col_txt = st.columns([1, 1])
        with col_img:
            st.markdown("""
            <div class="sol-img-card">
                <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=900&q=90" alt="Observability" />
                <div class="sol-img-overlay">
                    <span class="sol-img-tag">SOLUTION 06</span>
                    <div class="sol-img-icon">&#128301;</div>
                    <div class="sol-img-title">Observability</div>
                    <div class="sol-img-desc">Complete visibility at cloud scale</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col_txt:
            st.markdown("""
            <div style="padding-left:24px;">
                <div class="section-label" style="text-align:left;">Solution 06</div>
                <h3 style="font-size:28px; font-weight:800; color:#1C1107; margin-bottom:14px; letter-spacing:-0.5px;">Observability for Cloud-Scale Apps</h3>
                <p style="font-size:15px; color:#6B5E52; line-height:1.8; margin-bottom:16px;">
                    Gain full visibility into your applications and infrastructure with modern observability platforms. We help you choose solutions that provide real-time insights across logs, metrics, and traces &#8212; ensuring performance, reliability, and faster issue resolution.
                </p>
                <div style="background:rgba(217,119,6,0.06); border-left:3px solid #D97706; border-radius:0 8px 8px 0; padding:14px 18px; margin-bottom:20px;">
                    <p style="font-size:14px; color:#4A3728; line-height:1.7; margin:0; font-style:italic;">
                        Why you need this: In cloud environments, downtime costs thousands per minute. Observability is the foundation of reliability engineering.
                    </p>
                </div>
                <div style="font-size:13px; font-weight:700; color:#E85D04; letter-spacing:2px; text-transform:uppercase; margin-bottom:12px;">Key Features We Evaluate</div>
                <ul style="list-style:none; display:flex; flex-direction:column; gap:8px; margin-bottom:28px;">
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Application performance monitoring (APM)</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Infrastructure &amp; container visibility</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Log management &amp; analytics</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Distributed tracing capabilities</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Incident detection &amp; alerting</li>
                    <li style="font-size:14px; color:#4A3728; display:flex; align-items:center; gap:10px;"><span style="color:#E85D04;">&#8594;</span> Cloud-scale platform evaluation</li>
                </ul>
                <a target="_self" href="/Contact" class="btn-gradient" style="text-decoration:none;">Get Observability Advisory &#8594;</a>
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
