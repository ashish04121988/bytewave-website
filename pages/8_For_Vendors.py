import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import GLOBAL_CSS
from components import navbar, footer

st.set_page_config(
    page_title="For Vendors — Bytewave Digital",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
navbar("For Vendors")

# ─── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="background:linear-gradient(135deg,#FFF5EE 0%,#FAF8F4 60%,#FFF0E8 100%); padding:100px 80px 80px 80px; position:relative; overflow:hidden;">
    <div style="position:absolute;top:-60px;right:-60px;width:400px;height:400px;background:radial-gradient(circle,rgba(232,93,4,0.08) 0%,transparent 70%);border-radius:50%;"></div>
    <div style="position:absolute;bottom:-40px;left:10%;width:300px;height:300px;background:radial-gradient(circle,rgba(124,58,237,0.06) 0%,transparent 70%);border-radius:50%;"></div>
    <div style="max-width:860px; position:relative; z-index:1;">
        <div class="section-label">Vendor Partnership</div>
        <h1 style="font-size:clamp(36px,5vw,64px); font-weight:900; letter-spacing:-2px; color:#1C1107; line-height:1.1; margin-bottom:20px;">
            Scale Your SaaS Through <span class="gradient-text">Qualified Customer Access</span>
        </h1>
        <p style="font-size:20px; color:#4A3728; font-weight:600; margin-bottom:12px;">
            Choose Bytewave Digital to drive contextual adoption &#8212; not just leads.
        </p>
        <p style="font-size:16px; color:#6B5E52; line-height:1.85; margin-bottom:40px; max-width:720px;">
            Bytewave Digital helps technology vendors accelerate growth through strategic customer access, use-case-driven selling, and a strong B2B ecosystem across SMB, Mid-Market, and Enterprise segments.
        </p>
        <div style="display:flex; gap:16px; flex-wrap:wrap;">
            <a target="_self" href="/Contact" class="btn-gradient" style="text-decoration:none;">&#128073; Become a Vendor Partner</a>
            <a target="_self" href="/Contact" class="btn-outline" style="text-decoration:none;">&#128197; Schedule a Discussion</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ─── WHY WORK WITH BYTEWAVE ───────────────────────────────────────────────────
st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section section-beige">
    <div class="section-label">Why Partner With Us</div>
    <h2 class="section-title">Why Work With <span class="gradient-text">Bytewave</span></h2>
    <p class="section-subtitle">We go beyond lead generation — we drive adoption through trusted customer relationships and contextual engagement.</p>
    <div class="cards-grid">
        <div class="service-card">
            <span class="card-icon">&#127760;</span>
            <div class="card-title">Distribution, Not Just Leads</div>
            <div class="card-desc">We don&#8217;t generate cold leads &#8212; we enable access to an active customer ecosystem through trusted business networks and strategic alliances.</div>
        </div>
        <div class="service-card">
            <span class="card-icon">&#127919;</span>
            <div class="card-title">Contextual Selling</div>
            <div class="card-desc">We engage customers based on real business challenges and use cases, ensuring stronger relevance and higher conversion rates.</div>
        </div>
        <div class="service-card">
            <span class="card-icon">&#128640;</span>
            <div class="card-title">Faster Go-To-Market</div>
            <div class="card-desc">Skip long onboarding cycles and accelerate opportunities through an already engaged business network with established trust.</div>
        </div>
        <div class="service-card">
            <span class="card-icon">&#128200;</span>
            <div class="card-title">Performance-Driven Model</div>
            <div class="card-desc">Our approach is aligned to outcomes &#8212; focused on adoption, revenue, and long-term customer value, not just top-of-funnel activity.</div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── ECOSYSTEM ADVANTAGE ──────────────────────────────────────────────────────
st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)
eco_left, eco_right = st.columns([1, 1])

with eco_left:
    st.markdown("""
    <div style="padding:80px 40px 80px 80px; background:#FAF8F4;">
        <div class="section-label" style="text-align:left;">Our Advantage</div>
        <h2 style="font-size:clamp(28px,3.5vw,42px); font-weight:800; letter-spacing:-1px; color:#1C1107; margin-bottom:20px; line-height:1.15;">
            Our <span class="gradient-text">Ecosystem Advantage</span>
        </h2>
        <p style="font-size:16px; color:#6B5E52; line-height:1.85; margin-bottom:32px;">
            We sit at the intersection of customer access and technology distribution &#8212; giving vendors a unique edge in reaching the right buyers at the right time.
        </p>
        <div style="display:flex; flex-direction:column; gap:14px;">
            <div style="display:flex; align-items:flex-start; gap:14px; font-size:15px; color:#4A3728; line-height:1.6;">
                <span style="color:#E85D04; font-weight:700; font-size:18px; margin-top:2px;">&#10003;</span>
                <span>Strategic ecosystem relationships with Fundoodata and industry networks</span>
            </div>
            <div style="display:flex; align-items:flex-start; gap:14px; font-size:15px; color:#4A3728; line-height:1.6;">
                <span style="color:#E85D04; font-weight:700; font-size:18px; margin-top:2px;">&#10003;</span>
                <span>Access to active B2B customer networks across SMB, Mid-Market, and Enterprise</span>
            </div>
            <div style="display:flex; align-items:flex-start; gap:14px; font-size:15px; color:#4A3728; line-height:1.6;">
                <span style="color:#E85D04; font-weight:700; font-size:18px; margin-top:2px;">&#10003;</span>
                <span>Direct business engagement capabilities with decision-makers</span>
            </div>
            <div style="display:flex; align-items:flex-start; gap:14px; font-size:15px; color:#4A3728; line-height:1.6;">
                <span style="color:#E85D04; font-weight:700; font-size:18px; margin-top:2px;">&#10003;</span>
                <span>Use-case-led solution positioning for stronger buyer relevance</span>
            </div>
            <div style="display:flex; align-items:flex-start; gap:14px; font-size:15px; color:#4A3728; line-height:1.6;">
                <span style="color:#E85D04; font-weight:700; font-size:18px; margin-top:2px;">&#10003;</span>
                <span>Faster vendor-led growth opportunities with shorter sales cycles</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with eco_right:
    st.markdown("""
    <div style="padding:80px 80px 80px 40px; background:#FAF8F4; display:flex; align-items:center;">
        <div style="background:linear-gradient(135deg,#FFF5EE,#FFF0E8); border:1px solid rgba(232,93,4,0.15); border-radius:24px; padding:40px; width:100%;">
            <div style="text-align:center; margin-bottom:28px;">
                <span style="font-size:48px;">&#128101;</span>
                <h3 style="font-size:22px; font-weight:800; color:#1C1107; margin:12px 0 6px;">B2B Ecosystem Reach</h3>
                <p style="font-size:14px; color:#6B5E52;">Across industries and segments</p>
            </div>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:16px;">
                <div style="background:#FFFFFF; border-radius:12px; padding:20px; text-align:center; border:1px solid rgba(232,93,4,0.1);">
                    <div style="font-size:28px; font-weight:900; color:#E85D04;">SMB</div>
                    <div style="font-size:12px; color:#6B5E52; margin-top:4px;">Small &amp; Medium</div>
                </div>
                <div style="background:#FFFFFF; border-radius:12px; padding:20px; text-align:center; border:1px solid rgba(124,58,237,0.1);">
                    <div style="font-size:28px; font-weight:900; color:#7C3AED;">Mid</div>
                    <div style="font-size:12px; color:#6B5E52; margin-top:4px;">Mid-Market</div>
                </div>
                <div style="background:#FFFFFF; border-radius:12px; padding:20px; text-align:center; border:1px solid rgba(232,93,4,0.1); grid-column:1/-1;">
                    <div style="font-size:28px; font-weight:900; color:#E85D04;">Enterprise</div>
                    <div style="font-size:12px; color:#6B5E52; margin-top:4px;">Large Organisations</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ─── WHERE WE ADD VALUE ───────────────────────────────────────────────────────
st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section section-beige">
    <div class="section-label">Solution Areas</div>
    <h2 class="section-title">Where We <span class="gradient-text">Add Value</span></h2>
    <p class="section-subtitle">We work with vendors across these key technology domains to drive contextual adoption.</p>
    <div class="cards-grid">
        <div class="service-card">
            <span class="card-icon">&#128202;</span>
            <div class="card-title">CRM &amp; Sales Platforms</div>
            <div class="card-desc">Drive adoption of customer engagement and pipeline management solutions across SMB to Enterprise buyers.</div>
        </div>
        <div class="service-card">
            <span class="card-icon">&#128268;</span>
            <div class="card-title">Marketing Automation</div>
            <div class="card-desc">Enable scalable demand generation and customer lifecycle management with the right MarTech solutions.</div>
        </div>
        <div class="service-card">
            <span class="card-icon">&#128064;</span>
            <div class="card-title">Observability &amp; DevOps</div>
            <div class="card-desc">Support cloud-native businesses with monitoring, performance, and reliability tools for engineering excellence.</div>
        </div>
        <div class="service-card">
            <span class="card-icon">&#9729;&#65039;</span>
            <div class="card-title">Cloud &amp; Infrastructure</div>
            <div class="card-desc">Help organizations adopt scalable, secure, and cost-effective cloud infrastructure solutions aligned to their scale.</div>
        </div>
        <div class="service-card">
            <span class="card-icon">&#129302;</span>
            <div class="card-title">AI &amp; Emerging Tech</div>
            <div class="card-desc">Enable adoption of next-generation AI platforms and digital transformation solutions for forward-thinking businesses.</div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── ENGAGEMENT MODELS ────────────────────────────────────────────────────────
st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section" style="background:#FFFFFF;">
    <div class="section-label">Collaboration</div>
    <h2 class="section-title">Engagement <span class="gradient-text">Models</span></h2>
    <p class="section-subtitle">We support flexible collaboration models designed to align with your go-to-market strategy.</p>
    <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(300px,1fr)); gap:28px; margin-top:40px;">
        <div style="background:linear-gradient(135deg,#FFF5EE,#FFF0E8); border:1px solid rgba(232,93,4,0.15); border-radius:20px; padding:36px;">
            <div style="width:48px;height:48px;background:linear-gradient(135deg,#E85D04,#F97316);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:22px;margin-bottom:20px;">&#128279;</div>
            <h3 style="font-size:18px; font-weight:800; color:#1C1107; margin-bottom:12px;">Affiliate / Referral Model</h3>
            <p style="font-size:14px; color:#6B5E52; line-height:1.75;">We generate qualified opportunities and connect customers with the right vendor, earning referral-based commissions on successful deals.</p>
        </div>
        <div style="background:linear-gradient(135deg,#F5F0FF,#EDE8FF); border:1px solid rgba(124,58,237,0.15); border-radius:20px; padding:36px;">
            <div style="width:48px;height:48px;background:linear-gradient(135deg,#7C3AED,#A855F7);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:22px;margin-bottom:20px;">&#129309;</div>
            <h3 style="font-size:18px; font-weight:800; color:#1C1107; margin-bottom:12px;">Co-Selling Opportunities</h3>
            <p style="font-size:14px; color:#6B5E52; line-height:1.75;">We work jointly with vendors on strategic opportunities, combining customer access with product expertise to accelerate deal closures.</p>
        </div>
        <div style="background:linear-gradient(135deg,#FFF5EE,#FFF0E8); border:1px solid rgba(232,93,4,0.15); border-radius:20px; padding:36px;">
            <div style="width:48px;height:48px;background:linear-gradient(135deg,#E85D04,#7C3AED);border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:22px;margin-bottom:20px;">&#127919;</div>
            <h3 style="font-size:18px; font-weight:800; color:#1C1107; margin-bottom:12px;">Reseller Engagement</h3>
            <p style="font-size:14px; color:#6B5E52; line-height:1.75;">We actively position and sell vendor solutions, driving adoption through direct customer engagement and partner-led execution.</p>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── HOW WE WORK ──────────────────────────────────────────────────────────────
st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section section-beige">
    <div class="section-label">Our Process</div>
    <h2 class="section-title">How We Work <span class="gradient-text">With Vendors</span></h2>
    <p class="section-subtitle">A simple, structured approach to accelerating your SaaS growth.</p>
    <div style="display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:28px; margin-top:40px;">
        <div style="background:#FFFFFF; border-radius:20px; padding:36px; border:1px solid rgba(232,93,4,0.1); position:relative;">
            <div style="width:44px;height:44px;background:linear-gradient(135deg,#E85D04,#F97316);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:18px;font-weight:900;color:#FFFFFF;margin-bottom:20px;">1</div>
            <h3 style="font-size:17px; font-weight:800; color:#1C1107; margin-bottom:10px;">Align on Use Cases</h3>
            <p style="font-size:14px; color:#6B5E52; line-height:1.75;">We identify where your solution fits within our customer ecosystem and map it to real business challenges.</p>
        </div>
        <div style="background:#FFFFFF; border-radius:20px; padding:36px; border:1px solid rgba(124,58,237,0.1); position:relative;">
            <div style="width:44px;height:44px;background:linear-gradient(135deg,#7C3AED,#A855F7);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:18px;font-weight:900;color:#FFFFFF;margin-bottom:20px;">2</div>
            <h3 style="font-size:17px; font-weight:800; color:#1C1107; margin-bottom:10px;">Targeted Engagement</h3>
            <p style="font-size:14px; color:#6B5E52; line-height:1.75;">We drive relevant conversations with qualified businesses, ensuring your solution reaches the right decision-makers.</p>
        </div>
        <div style="background:#FFFFFF; border-radius:20px; padding:36px; border:1px solid rgba(232,93,4,0.1); position:relative;">
            <div style="width:44px;height:44px;background:linear-gradient(135deg,#E85D04,#7C3AED);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:18px;font-weight:900;color:#FFFFFF;margin-bottom:20px;">3</div>
            <h3 style="font-size:17px; font-weight:800; color:#1C1107; margin-bottom:10px;">Enable Adoption</h3>
            <p style="font-size:14px; color:#6B5E52; line-height:1.75;">We support customer evaluation, decision-making, and solution adoption to ensure successful, long-term outcomes.</p>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── WHAT MAKES US DIFFERENT ──────────────────────────────────────────────────
st.markdown('<div class="gradient-divider"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section" style="background:#FFFFFF;">
    <div class="section-label">Our Edge</div>
    <h2 class="section-title">What Makes Us <span class="gradient-text">Different</span></h2>
    <div style="max-width:800px; margin:40px auto 0; text-align:center;">
        <div style="background:linear-gradient(135deg,#FFF5EE,#F5F0FF); border-radius:24px; padding:52px 48px; border:1px solid rgba(232,93,4,0.12);">
            <div style="display:grid; grid-template-columns:1fr auto 1fr; gap:32px; align-items:center; margin-bottom:40px;">
                <div style="background:#FFFFFF; border-radius:16px; padding:28px; border:2px solid rgba(200,200,200,0.3);">
                    <div style="font-size:32px; margin-bottom:12px;">&#128230;</div>
                    <div style="font-size:14px; color:#9CA3AF; font-weight:600; text-transform:uppercase; letter-spacing:1px; margin-bottom:8px;">Most Vendors</div>
                    <div style="font-size:16px; font-weight:700; color:#6B5E52;">Start with the <span style="text-decoration:line-through; color:#9CA3AF;">Product</span></div>
                </div>
                <div style="font-size:32px; color:#E85D04; font-weight:900;">&#8594;</div>
                <div style="background:linear-gradient(135deg,#E85D04,#7C3AED); border-radius:16px; padding:28px;">
                    <div style="font-size:32px; margin-bottom:12px;">&#128101;</div>
                    <div style="font-size:14px; color:rgba(255,255,255,0.7); font-weight:600; text-transform:uppercase; letter-spacing:1px; margin-bottom:8px;">Bytewave Digital</div>
                    <div style="font-size:16px; font-weight:700; color:#FFFFFF;">Starts with the Customer</div>
                </div>
            </div>
            <p style="font-size:15px; color:#6B5E52; margin-bottom:28px;">This ensures:</p>
            <div style="display:flex; justify-content:center; gap:32px; flex-wrap:wrap;">
                <div style="display:flex; align-items:center; gap:8px; font-size:15px; color:#4A3728; font-weight:600;">
                    <span style="color:#E85D04;">&#10003;</span> Higher Relevance
                </div>
                <div style="display:flex; align-items:center; gap:8px; font-size:15px; color:#4A3728; font-weight:600;">
                    <span style="color:#E85D04;">&#10003;</span> Faster Conversions
                </div>
                <div style="display:flex; align-items:center; gap:8px; font-size:15px; color:#4A3728; font-weight:600;">
                    <span style="color:#E85D04;">&#10003;</span> Better Long-Term Adoption
                </div>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── CLOSING CTA ──────────────────────────────────────────────────────────────
st.markdown("""
<section class="cta-banner">
    <h2 class="cta-title">Let&#8217;s Build a Smarter <span class="gradient-text">SaaS Growth Model</span> Together</h2>
    <p class="cta-sub">Work with Bytewave Digital to unlock real customer access, stronger adoption, and scalable growth.</p>
    <div class="cta-buttons">
        <a target="_self" href="/Contact" class="btn-gradient">&#128073; Become a Vendor Partner</a>
        <a target="_self" href="/Contact" class="btn-outline">&#128197; Schedule a Discussion</a>
    </div>
</section>
""", unsafe_allow_html=True)

footer()
