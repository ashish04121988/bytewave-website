import streamlit as st

def navbar(active_page="Home"):
    pages = {
        "Home": "/",
        "Services": "/Services",
        "Pricing": "/Pricing",
        "Process": "/Process",
        "Results": "/Results",
        "Contact": "/Contact",
    }
    nav_links = ""
    for name, path in pages.items():
        active_style = "color:#E2E8F0 !important;" if name == active_page else ""
        nav_links += f'<a target="_self" href="{path}" style="{active_style}">{name}</a>'

    st.markdown(f"""
    <nav class="navbar">
        <div>
            <div class="navbar-logo">⚡ BYTEWAVE</div>
            <div class="navbar-tagline">Your Growth Partner in Technology & Sales</div>
        </div>
        <div style="display:flex; gap:40px; align-items:center;">
            {nav_links}
            <a target="_self" href="/Contact" class="btn-gradient" style="text-decoration:none; padding:10px 20px; border-radius:8px; font-weight:600; font-size:13px; color:white; background:linear-gradient(135deg,#2563EB,#7C3AED);">Book Strategy Call</a>
        </div>
    </nav>
    """, unsafe_allow_html=True)


def footer():
    st.markdown("""
    <footer class="footer">
        <div class="footer-grid">
            <div>
                <div class="footer-logo">⚡ BYTEWAVE</div>
                <div class="footer-tagline">
                    Bytewave Digital Solutions bridges the gap between technology companies and businesses through smart reselling and revenue acceleration.
                </div>
                <div style="margin-top:24px; display:flex; gap:12px;">
                    <a target="_self" href="#" style="width:36px; height:36px; background:rgba(37,99,235,0.15); border:1px solid rgba(37,99,235,0.3); border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:16px; text-decoration:none;">in</a>
                    <a target="_self" href="#" style="width:36px; height:36px; background:rgba(37,99,235,0.15); border:1px solid rgba(37,99,235,0.3); border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:16px; text-decoration:none;">𝕏</a>
                </div>
            </div>
            <div>
                <div class="footer-heading">Quick Links</div>
                <ul class="footer-links">
                    <li><a target="_self" href="/">Home</a></li>
                    <li><a target="_self" href="/Services">Services</a></li>
                    <li><a target="_self" href="/Pricing">Pricing</a></li>
                    <li><a target="_self" href="/Process">Our Process</a></li>
                    <li><a target="_self" href="/Results">Results</a></li>
                </ul>
            </div>
            <div>
                <div class="footer-heading">Get In Touch</div>
                <ul class="footer-links">
                    <li><a target="_self" href="/Contact">Book a Consultation</a></li>
                    <li><a target="_self" href="/Contact">Get a Demo</a></li>
                    <li><a target="_self" href="/Contact">Start Generating Leads</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <div class="footer-copy">© 2024 Bytewave Digital Solutions. All rights reserved.</div>
            <div class="footer-bottom-tagline">"From Leads to Revenue — We Do It All"</div>
        </div>
    </footer>
    """, unsafe_allow_html=True)
