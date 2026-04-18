import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import GLOBAL_CSS
from components import navbar, footer

st.set_page_config(
    page_title="Blog — Bytewave Digital",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
navbar("Blog")

# ─── PAGE HEADER ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <div class="page-header-watermark">BLOG</div>
    <div class="section-label">Insights &amp; Perspectives</div>
    <h1 class="section-title">Technology Insights for <span class="gradient-text">Modern Leaders</span></h1>
    <p class="section-subtitle">
        Expert perspectives on software procurement, sales acceleration, AI adoption, and digital transformation
        &#8212; curated for business and technology leaders.
    </p>
</div>
""", unsafe_allow_html=True)

# ─── FEATURED ARTICLE ────────────────────────────────────────────────────────
st.markdown("""
<section class="section section-white" style="padding-bottom:0;">
    <div class="section-label">Featured Article</div>
    <h2 class="section-title" style="margin-bottom:32px;">Editor's <span class="gradient-text">Pick</span></h2>
</section>
""", unsafe_allow_html=True)

feat_l, feat_r = st.columns([1.2, 0.8])
with feat_l:
    st.markdown("""
    <div class="blog-featured">
        <img src="https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=1200&q=90" alt="AI in Business" />
        <div class="blog-featured-overlay">
            <span class="blog-tag">Agentic AI</span>
            <div style="font-size:24px; font-weight:800; color:#FAF8F4; margin:12px 0 8px; line-height:1.3;">
                How Agentic AI Is Redefining Business Workflows in 2025
            </div>
            <div style="font-size:14px; color:rgba(250,248,244,0.75); line-height:1.6; margin-bottom:16px;">
                AI is no longer just a buzzword &#8212; it's becoming the backbone of intelligent automation.
                Here's how forward-thinking businesses are deploying agentic AI to drive real outcomes.
            </div>
            <div style="font-size:12px; color:rgba(250,248,244,0.55);">April 10, 2025 &nbsp;&#183;&nbsp; 6 min read</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with feat_r:
    st.markdown("""
    <div style="padding:0 0 0 32px; display:flex; flex-direction:column; gap:20px;">
        <div style="font-size:14px; color:#6B5E52; line-height:1.85;">
            <p style="margin-bottom:16px;">
                The rise of Agentic AI marks a fundamental shift in how businesses approach automation and decision-making.
                Unlike traditional rule-based automation, agentic systems can perceive their environment, reason about goals,
                and take autonomous actions &#8212; often across multiple systems simultaneously.
            </p>
            <p style="margin-bottom:16px;">
                For technology buyers, this means a new class of software evaluation criteria: Can the platform integrate
                across your existing stack? Does it support multi-step reasoning? How does it handle edge cases and escalations?
            </p>
            <p>
                At Bytewave Digital, we've helped clients evaluate and shortlist AI platforms across CRM automation, customer
                service orchestration, and financial workflow management &#8212; always with a vendor-neutral lens.
            </p>
        </div>
        <div style="display:flex; gap:12px; flex-wrap:wrap;">
            <span class="blog-tag">AI &amp; Automation</span>
            <span class="blog-tag">Technology Buying</span>
            <span class="blog-tag">Digital Transformation</span>
        </div>
        <a target="_self" href="/Contact" class="btn-gradient" style="text-decoration:none; display:inline-block; width:fit-content;">Talk to an AI Expert &#8594;</a>
    </div>
    """, unsafe_allow_html=True)

# ─── BLOG GRID ───────────────────────────────────────────────────────────────
st.markdown("""
<div style="padding:60px 60px 20px; background:#FAF8F4;">
    <div class="section-label">Latest Articles</div>
    <h2 class="section-title" style="margin-bottom:8px;">Recent <span class="gradient-text">Insights</span></h2>
    <p class="section-subtitle">Thought leadership from the Bytewave Digital team on technology buying, sales strategy, and industry trends.</p>
</div>
""", unsafe_allow_html=True)

b_c1, b_c2, b_c3 = st.columns(3)

with b_c1:
    st.markdown("""
    <div style="padding:0 12px 40px; background:#FAF8F4;">
        <div class="blog-card">
            <img class="blog-card-img" src="https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=800&q=90" alt="CRM Guide" />
            <div class="blog-card-body">
                <span class="blog-tag">CRM</span>
                <div class="blog-card-title">Choosing the Right CRM in 2025: A Buyer's Framework</div>
                <div class="blog-card-excerpt">With hundreds of CRM options in the market, how do you cut through the noise? We break down the five criteria that matter most for growing businesses.</div>
                <div class="blog-card-meta">
                    <span>&#128197; March 28, 2025</span>
                    <span>&#128336; 5 min read</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with b_c2:
    st.markdown("""
    <div style="padding:0 12px 40px; background:#FAF8F4;">
        <div class="blog-card">
            <img class="blog-card-img" src="https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=800&q=90" alt="Cloud Migration" />
            <div class="blog-card-body">
                <span class="blog-tag">Cloud &amp; IT</span>
                <div class="blog-card-title">Public vs. Private vs. Hybrid Cloud: Making the Right Call</div>
                <div class="blog-card-excerpt">Cloud decisions have long-term cost and performance implications. We outline a practical decision model to help mid-size businesses choose wisely.</div>
                <div class="blog-card-meta">
                    <span>&#128197; March 14, 2025</span>
                    <span>&#128336; 7 min read</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with b_c3:
    st.markdown("""
    <div style="padding:0 12px 40px; background:#FAF8F4;">
        <div class="blog-card">
            <img class="blog-card-img" src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=90" alt="MarTech Stack" />
            <div class="blog-card-body">
                <span class="blog-tag">Marketing Tech</span>
                <div class="blog-card-title">Building a Lean MarTech Stack That Actually Converts</div>
                <div class="blog-card-excerpt">Most marketing stacks are bloated with tools that don't talk to each other. Here's how to build a streamlined setup that drives pipeline, not complexity.</div>
                <div class="blog-card-meta">
                    <span>&#128197; February 20, 2025</span>
                    <span>&#128336; 6 min read</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

b_c4, b_c5, b_c6 = st.columns(3)

with b_c4:
    st.markdown("""
    <div style="padding:0 12px 40px; background:#FAF8F4;">
        <div class="blog-card">
            <img class="blog-card-img" src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=90" alt="Observability" />
            <div class="blog-card-body">
                <span class="blog-tag">Observability</span>
                <div class="blog-card-title">Why Observability is Non-Negotiable for Cloud-Scale Apps</div>
                <div class="blog-card-excerpt">As systems grow more complex, visibility becomes your competitive advantage. We explore what modern observability platforms offer and how to choose one.</div>
                <div class="blog-card-meta">
                    <span>&#128197; February 5, 2025</span>
                    <span>&#128336; 4 min read</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with b_c5:
    st.markdown("""
    <div style="padding:0 12px 40px; background:#FAF8F4;">
        <div class="blog-card">
            <img class="blog-card-img" src="https://images.unsplash.com/photo-1521737711867-e3b97375f902?auto=format&fit=crop&w=800&q=90" alt="HR Software" />
            <div class="blog-card-body">
                <span class="blog-tag">HR &amp; Finance</span>
                <div class="blog-card-title">HR Tech in 2025: From Payroll to People Intelligence</div>
                <div class="blog-card-excerpt">Modern HR platforms do far more than manage payroll. Discover how leading organizations are using HR tech to build smarter, more agile workforces.</div>
                <div class="blog-card-meta">
                    <span>&#128197; January 22, 2025</span>
                    <span>&#128336; 5 min read</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with b_c6:
    st.markdown("""
    <div style="padding:0 12px 40px; background:#FAF8F4;">
        <div class="blog-card">
            <img class="blog-card-img" src="https://images.unsplash.com/photo-1556761175-4b46a572b786?auto=format&fit=crop&w=800&q=90" alt="Sales Strategy" />
            <div class="blog-card-body">
                <span class="blog-tag">Sales Strategy</span>
                <div class="blog-card-title">The Anatomy of a High-Performing B2B Sales Pipeline</div>
                <div class="blog-card-excerpt">A leaky pipeline kills revenue. Learn how top-performing sales teams structure their pipeline &#8212; from ICP definition to deal closure &#8212; and what tools support each stage.</div>
                <div class="blog-card-meta">
                    <span>&#128197; January 8, 2025</span>
                    <span>&#128336; 8 min read</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ─── TOPIC CATEGORIES ────────────────────────────────────────────────────────
st.markdown("""
<section class="section section-white">
    <div class="section-label">Browse by Topic</div>
    <h2 class="section-title">Explore <span class="gradient-text">Categories</span></h2>
    <div class="industry-tags" style="margin-top:32px;">
        <span class="industry-tag">&#129302; Agentic AI</span>
        <span class="industry-tag">&#128187; CRM &amp; Sales Tech</span>
        <span class="industry-tag">&#9729;&#65039; Cloud &amp; IT</span>
        <span class="industry-tag">&#128226; Marketing Automation</span>
        <span class="industry-tag">&#128101; HR &amp; Finance</span>
        <span class="industry-tag">&#128301; Observability</span>
        <span class="industry-tag">&#128200; Revenue Growth</span>
        <span class="industry-tag">&#128736; Technology Buying</span>
        <span class="industry-tag">&#127760; Digital Transformation</span>
    </div>
</section>
""", unsafe_allow_html=True)

# ─── NEWSLETTER CTA ──────────────────────────────────────────────────────────
st.markdown("""
<section class="cta-banner">
    <h2 class="cta-title">Stay Ahead of the <span class="gradient-text">Technology Curve</span></h2>
    <p class="cta-sub">Get curated insights on software buying, AI trends, and sales strategy delivered to your inbox.</p>
    <div class="cta-buttons">
        <a target="_self" href="/Contact" class="btn-gradient">&#128231; Subscribe to Insights</a>
        <a target="_self" href="/Solutions" class="btn-outline">&#128269; Explore Solutions</a>
    </div>
</section>
""", unsafe_allow_html=True)

footer()
