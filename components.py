import streamlit as st

def navbar(active_page="Home"):
    pages = {
        "Home": "/",
        "About": "/About",
        "Solutions": "/Solutions",
        "Services": "/Services",
        "Industries": "/Industries",
        "Blog": "/Blog",
        "Careers": "/Careers",
    }
    nav_links = ""
    for name, path in pages.items():
        active_style = "color:#E85D04 !important; font-weight:700;" if name == active_page else ""
        nav_links += f'<a target="_self" href="{path}" style="{active_style}">{name}</a>'

    st.markdown(f"""
    <nav class="navbar">
        <div>
            <div class="navbar-logo">⚡ BYTEWAVE DIGITAL</div>
            <div class="navbar-tagline">Right Technology. No Noise.</div>
        </div>
        <div style="display:flex; gap:28px; align-items:center;" class="navbar-links">
            {nav_links}
            <a target="_self" href="/Contact" class="btn-gradient" style="text-decoration:none; padding:10px 22px; border-radius:8px; font-weight:700; font-size:13px; color:white; background:linear-gradient(135deg,#E85D04,#7C3AED);">Schedule a Consultation</a>
        </div>
    </nav>
    """, unsafe_allow_html=True)


def footer():
    st.markdown("""
    <div class="footer">
        <div class="footer-grid">
            <div>
                <div class="footer-logo">⚡ BYTEWAVE DIGITAL</div>
                <div class="footer-tagline">
                    Born from the legacy of Fundoo Data, Bytewave Digital is a vendor-neutral IT software reseller helping organizations identify, evaluate, and procure the right technology solutions.
                </div>
                <div style="margin-top:24px; display:flex; gap:12px;">
                    <a target="_self" href="#" style="width:36px; height:36px; background:#FFFFFF; border:1px solid rgba(232,93,4,0.3); border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:14px; text-decoration:none; color:#E85D04; font-weight:700;">in</a>
                    <a target="_self" href="#" style="width:36px; height:36px; background:#FFFFFF; border:1px solid rgba(232,93,4,0.3); border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:14px; text-decoration:none; color:#E85D04; font-weight:700;">&#120143;</a>
                </div>
            </div>
            <div>
                <div class="footer-heading">Quick Links</div>
                <ul class="footer-links">
                    <li><a target="_self" href="/">Home</a></li>
                    <li><a target="_self" href="/About">About</a></li>
                    <li><a target="_self" href="/Solutions">Solutions</a></li>
                    <li><a target="_self" href="/Services">Services</a></li>
                    <li><a target="_self" href="/Industries">Industries</a></li>
                    <li><a target="_self" href="/Contact">Contact</a></li>
                </ul>
            </div>
            <div>
                <div class="footer-heading">Resources</div>
                <ul class="footer-links">
                    <li><a target="_self" href="/Blog">Blog &amp; Insights</a></li>
                    <li><a target="_self" href="/Careers">Careers</a></li>
                    <li><a target="_self" href="/Contact">Schedule a Consultation</a></li>
                    <li><a target="_self" href="/Contact">Talk to an Expert</a></li>
                </ul>
            </div>
            <div>
                <div class="footer-heading">Get In Touch</div>
                <ul class="footer-links">
                    <li><a target="_self" href="/Contact">Send Us a Message</a></li>
                    <li><a target="_self" href="/Contact">Explore Solutions</a></li>
                </ul>
                <div style="margin-top:20px; display:flex; flex-direction:column; gap:8px;">
                    <span style="font-size:13px; color:#4A3728;">&#128231; contact@bytewavedigital.com</span>
                    <span style="font-size:13px; color:#4A3728;">&#128222; +91-9810773138</span>
                    <span style="font-size:13px; color:#4A3728;">&#128205; Noida, India (Serving Globally)</span>
                    <span style="font-size:13px; color:#4A3728;">&#127760; www.bytewavedigital.com</span>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <div class="footer-copy">&#169; 2024 Bytewave Digital. All rights reserved.</div>
            <div class="footer-bottom-tagline">Right Technology. No Noise.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
