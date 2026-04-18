GLOBAL_CSS = """<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    /* ===== RESET & BASE ===== */
    * { margin: 0; padding: 0; box-sizing: border-box; }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif !important;
        background-color: #FAF8F4 !important;
        color: #1C1107 !important;
    }

    /* Hide Streamlit defaults */
    #MainMenu { visibility: hidden; }
    [data-testid="stFooter"] { visibility: hidden; }
    header { visibility: hidden; }
    .stDeployButton { display: none; }
    [data-testid="stToolbar"] { display: none; }
    [data-testid="stDecoration"] { display: none; }
    [data-testid="stStatusWidget"] { display: none; }

    /* Remove default padding */
    .block-container {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        max-width: 100% !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
    }

    /* ===== STREAMLIT LIGHT THEME OVERRIDES ===== */
    [data-testid="stSidebar"] {
        background: #FFFFFF !important;
        border-right: 1px solid rgba(232,93,4,0.15);
    }

    [data-testid="stSidebar"] a {
        color: #4A3728 !important;
        text-decoration: none;
        transition: color 0.3s;
    }

    [data-testid="stSidebar"] a:hover {
        color: #E85D04 !important;
    }

    /* Input fields - light */
    .stTextInput input, .stTextArea textarea, .stSelectbox select {
        background: #FFFFFF !important;
        border: 1.5px solid rgba(232,93,4,0.25) !important;
        border-radius: 10px !important;
        color: #1C1107 !important;
        font-size: 14px !important;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #E85D04 !important;
        box-shadow: 0 0 0 3px rgba(232,93,4,0.12) !important;
    }

    /* Form submit button */
    .stButton button {
        background: linear-gradient(135deg, #E85D04, #7C3AED) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        font-size: 15px !important;
        width: 100% !important;
        box-shadow: 0 4px 20px rgba(232,93,4,0.3) !important;
        transition: all 0.3s !important;
    }
    .stButton button:hover {
        box-shadow: 0 8px 30px rgba(232,93,4,0.45) !important;
        transform: translateY(-2px) !important;
    }

    /* Tabs - light orange theme */
    .stTabs [data-baseweb="tab-list"] {
        background: #F0EBE3 !important;
        border-radius: 12px !important;
        padding: 6px !important;
        gap: 4px !important;
        border: 1px solid rgba(232,93,4,0.2) !important;
    }
    .stTabs [data-baseweb="tab"] {
        background: transparent !important;
        color: #A89888 !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        padding: 10px 20px !important;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #E85D04, #7C3AED) !important;
        color: white !important;
    }
    .stTabs [data-baseweb="tab-border"] { display: none !important; }
    .stTabs [data-baseweb="tab-panel"] { padding-top: 28px !important; }

    /* ===== TYPOGRAPHY ===== */
    .gradient-text {
        background: linear-gradient(135deg, #E85D04, #7C3AED);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .warm-gradient-text {
        background: linear-gradient(135deg, #E85D04, #D97706);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    /* ===== NAVBAR (LIGHT) ===== */
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 16px 60px;
        background: rgba(250,248,244,0.97);
        backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(232,93,4,0.12);
        position: sticky;
        top: 0;
        z-index: 999;
        width: 100%;
        box-shadow: 0 2px 20px rgba(28,17,7,0.06);
    }

    .navbar-logo {
        font-size: 22px;
        font-weight: 800;
        background: linear-gradient(135deg, #E85D04, #7C3AED);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -0.5px;
    }

    .navbar-tagline {
        font-size: 10px;
        color: #A89888;
        font-weight: 500;
        letter-spacing: 1px;
    }

    .navbar-links a {
        color: #4A3728;
        text-decoration: none;
        font-size: 14px;
        font-weight: 500;
        transition: color 0.3s;
    }

    .navbar-links a:hover {
        color: #E85D04;
    }

    /* ===== BUTTONS ===== */
    .btn-gradient {
        background: linear-gradient(135deg, #E85D04, #7C3AED);
        color: white !important;
        padding: 12px 28px;
        border-radius: 10px;
        font-weight: 700;
        font-size: 14px;
        border: none;
        cursor: pointer;
        text-decoration: none !important;
        display: inline-block;
        transition: all 0.3s;
        box-shadow: 0 4px 20px rgba(232,93,4,0.3);
    }
    .btn-gradient:hover {
        box-shadow: 0 8px 35px rgba(232,93,4,0.45);
        transform: translateY(-2px);
    }

    .btn-outline {
        background: transparent;
        color: #E85D04 !important;
        padding: 12px 28px;
        border-radius: 10px;
        font-weight: 700;
        font-size: 14px;
        border: 2px solid #E85D04;
        cursor: pointer;
        text-decoration: none !important;
        display: inline-block;
        transition: all 0.3s;
    }
    .btn-outline:hover {
        background: rgba(232,93,4,0.06);
        box-shadow: 0 4px 20px rgba(232,93,4,0.15);
    }

    /* ===== HERO SECTION (LIGHT) ===== */
    .hero-bg {
        min-height: 90vh;
        background: linear-gradient(135deg, #FAF8F4 0%, #F0EBE3 40%, #FAF8F4 100%);
        display: flex;
        align-items: center;
        padding: 80px 60px;
        position: relative;
        overflow: hidden;
    }
    .hero-bg::before {
        content: '';
        position: absolute;
        top: -150px;
        right: 10%;
        width: 500px;
        height: 500px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(232,93,4,0.1) 0%, transparent 70%);
        animation: floatOrb 8s ease-in-out infinite;
    }
    .hero-bg::after {
        content: '';
        position: absolute;
        bottom: -100px;
        left: 5%;
        width: 350px;
        height: 350px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(124,58,237,0.08) 0%, transparent 70%);
        animation: floatOrb 6s ease-in-out infinite reverse;
    }
    @keyframes floatOrb {
        0%, 100% { transform: translateY(0) scale(1); }
        50% { transform: translateY(-30px) scale(1.05); }
    }

    /* Hero text */
    .hero-eyebrow {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: #E85D04;
        margin-bottom: 20px;
        background: rgba(232,93,4,0.08);
        border: 1px solid rgba(232,93,4,0.2);
        padding: 6px 16px;
        border-radius: 100px;
    }
    .hero-h1 {
        font-size: clamp(40px, 5.5vw, 68px);
        font-weight: 900;
        line-height: 1.05;
        letter-spacing: -2px;
        color: #1C1107;
        margin-bottom: 24px;
        animation: fadeInUp 0.8s ease forwards;
    }
    .hero-sub {
        font-size: 18px;
        line-height: 1.75;
        color: #6B5E52;
        max-width: 540px;
        margin-bottom: 40px;
        font-weight: 400;
        animation: fadeInUp 0.8s ease 0.2s both;
    }
    .hero-cta-group {
        display: flex;
        gap: 16px;
        flex-wrap: wrap;
        animation: fadeInUp 0.8s ease 0.4s both;
    }

    /* Stat badge (hero right panel) */
    .stat-badge {
        background: #FFFFFF;
        border: 1px solid rgba(232,93,4,0.2);
        border-radius: 16px;
        padding: 20px 28px;
        text-align: center;
        box-shadow: 0 8px 32px rgba(28,17,7,0.08);
        animation: float 4s ease-in-out infinite;
    }
    .stat-badge:nth-child(2) { animation-delay: 1.5s; }
    .stat-badge:nth-child(3) { animation-delay: 3s; }
    .stat-badge-number {
        font-size: 32px;
        font-weight: 900;
        background: linear-gradient(135deg, #E85D04, #7C3AED);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .stat-badge-label {
        font-size: 12px;
        color: #A89888;
        margin-top: 4px;
        font-weight: 500;
    }
    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-12px); }
    }

    /* ===== PARTNER STRIP (LIGHT) ===== */
    .partner-strip {
        background: #FFFFFF;
        border-top: 1px solid rgba(232,93,4,0.1);
        border-bottom: 1px solid rgba(232,93,4,0.1);
        padding: 28px 60px;
    }
    .partner-logos {
        display: flex;
        gap: 32px;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;
    }
    .partner-logo {
        font-size: 13px;
        font-weight: 700;
        color: #C4B5A8;
        padding: 8px 18px;
        border: 1.5px solid rgba(28,17,7,0.1);
        border-radius: 8px;
        transition: all 0.3s;
        letter-spacing: 0.5px;
    }
    .partner-logo:hover {
        color: #E85D04;
        border-color: rgba(232,93,4,0.3);
        background: rgba(232,93,4,0.04);
    }

    /* ===== STATS SECTION (LIGHT) ===== */
    .stats-section {
        background: #FFFFFF;
        padding: 60px;
        border-top: 1px solid rgba(232,93,4,0.1);
        border-bottom: 1px solid rgba(232,93,4,0.1);
    }
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        max-width: 1000px;
        margin: 0 auto;
    }
    .stat-item {
        text-align: center;
        padding: 32px 24px;
        border-right: 1px solid rgba(232,93,4,0.12);
    }
    .stat-item:last-child { border-right: none; }
    .stat-number {
        font-size: 52px;
        font-weight: 900;
        background: linear-gradient(135deg, #E85D04, #7C3AED, #D97706);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1;
        margin-bottom: 10px;
        animation: fadeInUp 0.8s ease forwards;
    }
    .stat-label { font-size: 14px; color: #4A3728; font-weight: 600; }
    .stat-sublabel { font-size: 12px; color: #A89888; margin-top: 4px; }

    /* ===== SECTION STYLES (LIGHT) ===== */
    .section { padding: 80px 60px; width: 100%; }
    .section-white { background: #FFFFFF; }
    .section-beige { background: #FAF8F4; }
    .section-soft { background: #F0EBE3; }
    .section-dark { background: #FAF8F4; }
    .section-darker { background: #FFFFFF; }

    .section-label {
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: #E85D04;
        margin-bottom: 12px;
        text-align: center;
    }
    .section-title {
        font-size: clamp(30px, 4vw, 46px);
        font-weight: 800;
        letter-spacing: -1px;
        line-height: 1.15;
        color: #1C1107;
        margin-bottom: 16px;
        text-align: center;
    }
    .section-subtitle {
        font-size: 17px;
        color: #6B5E52;
        max-width: 560px;
        margin: 0 auto 56px;
        line-height: 1.7;
        text-align: center;
    }

    /* ===== CARDS (LIGHT) ===== */
    .service-card {
        background: #FFFFFF;
        border: 1px solid rgba(232,93,4,0.12);
        border-radius: 16px;
        padding: 32px 28px;
        transition: all 0.35s ease;
        position: relative;
        overflow: hidden;
        box-shadow: 0 2px 12px rgba(28,17,7,0.04);
    }
    .service-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        background: linear-gradient(135deg, #E85D04, #7C3AED);
        transform: scaleX(0);
        transform-origin: left;
        transition: transform 0.35s;
    }
    .service-card:hover {
        border-color: rgba(232,93,4,0.25);
        box-shadow: 0 12px 40px rgba(232,93,4,0.12);
        transform: translateY(-5px);
    }
    .service-card:hover::before { transform: scaleX(1); }
    .card-icon { font-size: 36px; margin-bottom: 16px; display: block; }
    .card-title { font-size: 18px; font-weight: 700; color: #1C1107; margin-bottom: 12px; }
    .card-desc { font-size: 14px; color: #6B5E52; line-height: 1.7; margin-bottom: 16px; }
    .card-bullets { list-style: none; margin-top: 12px; }
    .card-bullets li {
        font-size: 13px; color: #A89888; padding: 4px 0;
        display: flex; align-items: center; gap: 8px;
    }
    .card-bullets li::before { content: '→'; color: #E85D04; font-size: 12px; }
    .cards-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
        gap: 24px;
        max-width: 1200px;
        margin: 0 auto;
    }

    /* ===== FEATURE CARDS (How We Work) ===== */
    .feature-card {
        background: #FFFFFF;
        border: 1px solid rgba(232,93,4,0.12);
        border-radius: 20px;
        padding: 40px 32px;
        text-align: center;
        transition: all 0.35s;
        position: relative;
        overflow: hidden;
        box-shadow: 0 4px 20px rgba(28,17,7,0.05);
    }
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 4px;
        background: linear-gradient(135deg, #E85D04, #7C3AED, #D97706);
        transform: scaleX(0);
        transition: transform 0.35s;
    }
    .feature-card:hover::before { transform: scaleX(1); }
    .feature-card:hover {
        border-color: rgba(232,93,4,0.3);
        box-shadow: 0 20px 60px rgba(232,93,4,0.12);
        transform: translateY(-5px);
    }
    .feature-num {
        font-size: 64px; font-weight: 900;
        color: rgba(232,93,4,0.08);
        line-height: 1; margin-bottom: 16px;
    }
    .feature-icon { font-size: 44px; margin-bottom: 16px; }
    .feature-title { font-size: 22px; font-weight: 800; color: #1C1107; margin-bottom: 12px; }
    .feature-desc { font-size: 15px; color: #6B5E52; line-height: 1.7; }

    /* ===== TESTIMONIAL CARDS (LIGHT) ===== */
    .testimonial-card {
        background: #FFFFFF;
        border: 1px solid rgba(232,93,4,0.12);
        border-radius: 20px;
        padding: 36px 32px;
        transition: all 0.3s;
        position: relative;
        box-shadow: 0 4px 20px rgba(28,17,7,0.05);
    }
    .testimonial-card::before {
        content: '"';
        position: absolute;
        top: 16px; right: 24px;
        font-size: 80px;
        color: rgba(232,93,4,0.1);
        font-family: Georgia, serif;
        line-height: 1;
    }
    .testimonial-card:hover {
        border-color: rgba(232,93,4,0.25);
        box-shadow: 0 16px 50px rgba(232,93,4,0.1);
        transform: translateY(-4px);
    }
    .testimonial-stars { color: #D97706; font-size: 18px; margin-bottom: 16px; letter-spacing: 2px; }
    .testimonial-text { font-size: 15px; color: #4A3728; line-height: 1.75; margin-bottom: 24px; font-style: italic; }
    .testimonial-author { display: flex; align-items: center; gap: 14px; }
    .testimonial-avatar {
        width: 48px; height: 48px; border-radius: 50%;
        background: linear-gradient(135deg, #E85D04, #7C3AED);
        display: flex; align-items: center; justify-content: center;
        font-size: 18px; font-weight: 700; color: white; flex-shrink: 0;
        box-shadow: 0 4px 12px rgba(232,93,4,0.3);
    }
    .testimonial-name { font-size: 15px; font-weight: 700; color: #1C1107; }
    .testimonial-role { font-size: 12px; color: #A89888; }

    /* ===== SOLUTION IMAGE CARDS ===== */
    .sol-img-card {
        border-radius: 16px; overflow: hidden; position: relative;
        height: 280px; cursor: pointer; transition: all 0.4s;
        border: 1px solid rgba(232,93,4,0.15);
        box-shadow: 0 4px 20px rgba(28,17,7,0.08);
    }
    .sol-img-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 20px 60px rgba(232,93,4,0.2);
    }
    .sol-img-card img {
        width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s;
    }
    .sol-img-card:hover img { transform: scale(1.06); }
    .sol-img-overlay {
        position: absolute; inset: 0;
        background: linear-gradient(180deg, rgba(28,14,5,0.15) 0%, rgba(28,14,5,0.75) 60%, rgba(28,14,5,0.95) 100%);
        display: flex; flex-direction: column; justify-content: flex-end; padding: 24px;
    }
    .sol-img-icon { font-size: 28px; margin-bottom: 8px; }
    .sol-img-title { font-size: 18px; font-weight: 700; color: #FAF8F4; margin-bottom: 6px; }
    .sol-img-desc { font-size: 13px; color: rgba(250,248,244,0.75); line-height: 1.5; }
    .sol-img-tag {
        position: absolute; top: 16px; right: 16px;
        background: linear-gradient(135deg, #E85D04, #D97706);
        color: white; font-size: 11px; font-weight: 700;
        padding: 4px 12px; border-radius: 100px; letter-spacing: 1px;
    }

    /* ===== INDUSTRY IMAGE CARDS ===== */
    .industry-img-card {
        border-radius: 16px; overflow: hidden; position: relative;
        height: 220px; transition: all 0.35s;
        border: 1px solid rgba(232,93,4,0.12);
        box-shadow: 0 4px 16px rgba(28,17,7,0.06);
    }
    .industry-img-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 50px rgba(232,93,4,0.18);
    }
    .industry-img-card img {
        width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s;
    }
    .industry-img-card:hover img { transform: scale(1.07); }
    .industry-img-overlay {
        position: absolute; inset: 0;
        background: linear-gradient(180deg, rgba(28,14,5,0.2) 0%, rgba(28,14,5,0.82) 100%);
        display: flex; flex-direction: column; justify-content: flex-end; padding: 20px;
    }
    .industry-img-title { font-size: 17px; font-weight: 700; color: #FAF8F4; margin-bottom: 4px; }
    .industry-img-sub { font-size: 12px; color: rgba(250,248,244,0.7); }

    /* ===== SPLIT CARDS (Who We Work With) ===== */
    .split-cards {
        display: grid; grid-template-columns: 1fr 1fr; gap: 32px;
        max-width: 900px; margin: 0 auto;
    }
    .split-card {
        background: #FFFFFF;
        border: 1px solid rgba(232,93,4,0.15);
        border-radius: 20px; padding: 40px 32px;
        transition: all 0.3s;
        box-shadow: 0 4px 20px rgba(28,17,7,0.05);
    }
    .split-card:hover {
        border-color: rgba(232,93,4,0.3);
        box-shadow: 0 16px 50px rgba(232,93,4,0.1);
    }
    .split-card-icon { font-size: 40px; margin-bottom: 16px; }
    .split-card-title { font-size: 20px; font-weight: 700; color: #1C1107; margin-bottom: 16px; }
    .split-card-list { list-style: none; }
    .split-card-list li {
        font-size: 15px; color: #6B5E52; padding: 6px 0;
        display: flex; align-items: center; gap: 10px;
        border-bottom: 1px solid rgba(232,93,4,0.06);
    }
    .split-card-list li::before { content: '✓'; color: #E85D04; font-weight: 700; }

    /* ===== WHY GRID ===== */
    .why-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 20px; max-width: 1000px; margin: 0 auto;
    }
    .why-item {
        display: flex; align-items: flex-start; gap: 14px;
        background: #FFFFFF;
        border: 1px solid rgba(232,93,4,0.12);
        border-radius: 12px; padding: 20px; transition: all 0.3s;
        box-shadow: 0 2px 10px rgba(28,17,7,0.04);
    }
    .why-item:hover {
        border-color: rgba(232,93,4,0.3);
        box-shadow: 0 8px 30px rgba(232,93,4,0.1);
    }
    .why-check { color: #E85D04; font-size: 20px; margin-top: 2px; flex-shrink: 0; }
    .why-text { font-size: 14px; color: #4A3728; line-height: 1.6; font-weight: 500; }

    /* ===== PROCESS STEPS ===== */
    .process-steps {
        display: flex; justify-content: center; align-items: center;
        gap: 0; flex-wrap: wrap; max-width: 1100px; margin: 0 auto; position: relative;
    }
    .process-step {
        display: flex; flex-direction: column; align-items: center;
        text-align: center; width: 180px; position: relative; z-index: 2;
    }
    .step-connector {
        width: 60px; height: 2px;
        background: linear-gradient(135deg, #E85D04, #7C3AED);
        margin-top: -52px; position: relative; z-index: 1;
    }
    .step-number {
        width: 56px; height: 56px; border-radius: 50%;
        background: linear-gradient(135deg, #E85D04, #7C3AED);
        display: flex; align-items: center; justify-content: center;
        font-size: 20px; font-weight: 800; color: white; margin-bottom: 16px;
        box-shadow: 0 8px 24px rgba(232,93,4,0.35); position: relative;
    }
    .step-number::after {
        content: ''; position: absolute; inset: -4px;
        border-radius: 50%; border: 2px solid rgba(232,93,4,0.2);
    }
    .step-title { font-size: 15px; font-weight: 700; color: #1C1107; margin-bottom: 6px; }
    .step-desc { font-size: 12px; color: #A89888; line-height: 1.5; padding: 0 8px; }

    /* ===== CTA BANNER (DARK - one dark section for contrast) ===== */
    .cta-banner {
        background: linear-gradient(135deg, #1A0E05 0%, #2D1A0E 50%, #1A0E05 100%);
        padding: 80px 60px; text-align: center; position: relative; overflow: hidden;
        border-top: 1px solid rgba(232,93,4,0.3);
    }
    .cta-banner::before {
        content: ''; position: absolute; top: 50%; left: 50%;
        transform: translate(-50%,-50%);
        width: 600px; height: 300px;
        background: radial-gradient(ellipse, rgba(232,93,4,0.12) 0%, transparent 70%);
    }
    .cta-title {
        font-size: clamp(28px,4vw,46px); font-weight: 800; letter-spacing: -1px;
        color: #FAF8F4; margin-bottom: 16px; position: relative; z-index: 2;
    }
    .cta-sub {
        font-size: 17px; color: rgba(250,248,244,0.7);
        margin-bottom: 40px; position: relative; z-index: 2;
    }
    .cta-buttons {
        display: flex; gap: 16px; justify-content: center;
        flex-wrap: wrap; position: relative; z-index: 2;
    }

    /* ===== ABOUT IMAGE ===== */
    .about-img {
        border-radius: 20px; overflow: hidden; position: relative;
        box-shadow: 0 20px 60px rgba(232,93,4,0.15);
    }
    .about-img img {
        width: 100%; height: 100%; object-fit: cover; border-radius: 20px;
    }
    .about-img-badge {
        position: absolute; bottom: 24px; left: 24px;
        background: linear-gradient(135deg, #E85D04, #7C3AED);
        border-radius: 12px; padding: 16px 20px;
    }
    .about-img-badge-num { font-size: 28px; font-weight: 900; color: white; }
    .about-img-badge-text { font-size: 12px; color: rgba(255,255,255,0.85); }

    /* ===== FOOTER (DARK) ===== */
    .footer {
        background: #1A0E05;
        border-top: 1px solid rgba(232,93,4,0.2);
        padding: 60px 60px 30px;
    }
    .footer-grid {
        display: grid;
        grid-template-columns: 1.6fr 1fr 1fr 1fr;
        gap: 48px; margin-bottom: 48px;
    }
    .footer-logo {
        font-size: 22px; font-weight: 800;
        background: linear-gradient(135deg, #E85D04, #D97706);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 12px;
    }
    .footer-tagline { font-size: 13px; color: #6B5E52; line-height: 1.7; max-width: 260px; }
    .footer-heading {
        font-size: 12px; font-weight: 700; letter-spacing: 2px;
        text-transform: uppercase; color: #4A3728; margin-bottom: 20px;
    }
    .footer-links { list-style: none; display: flex; flex-direction: column; gap: 10px; }
    .footer-links a { font-size: 14px; color: #6B5E52; text-decoration: none; transition: color 0.3s; }
    .footer-links a:hover { color: #E85D04; }
    .footer-bottom {
        border-top: 1px solid rgba(232,93,4,0.1); padding-top: 24px;
        display: flex; justify-content: space-between; align-items: center;
    }
    .footer-copy { font-size: 13px; color: #4A3728; }
    .footer-bottom-tagline { font-size: 13px; color: #4A3728; font-style: italic; }

    /* ===== PRICING CARDS ===== */
    .pricing-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px,1fr));
        gap: 24px; max-width: 1000px; margin: 0 auto;
    }
    .pricing-card {
        background: #FFFFFF;
        border: 1px solid rgba(232,93,4,0.15);
        border-radius: 20px; padding: 40px 32px;
        position: relative; transition: all 0.35s;
        text-align: center;
        box-shadow: 0 4px 20px rgba(28,17,7,0.05);
    }
    .pricing-card.featured::before {
        content: '';
        position: absolute; inset: -2px;
        border-radius: 22px;
        background: linear-gradient(135deg,#E85D04,#7C3AED,#D97706);
        z-index: -1;
    }
    .pricing-card.featured::after {
        content: 'MOST POPULAR';
        position: absolute; top: -14px; left: 50%;
        transform: translateX(-50%);
        background: linear-gradient(135deg,#E85D04,#7C3AED);
        color: white; font-size: 11px; font-weight: 700;
        letter-spacing: 2px; padding: 4px 16px;
        border-radius: 100px; white-space: nowrap;
    }
    .pricing-card:hover {
        box-shadow: 0 20px 60px rgba(232,93,4,0.15);
        transform: translateY(-5px);
    }
    .pricing-card-title { font-size: 20px; font-weight: 700; color: #1C1107; margin-bottom: 8px; }
    .pricing-card-subtitle { font-size: 13px; color: #A89888; margin-bottom: 28px; }
    .pricing-card-icon { font-size: 44px; margin-bottom: 20px; }
    .pricing-features { list-style: none; text-align: left; margin-bottom: 32px; }
    .pricing-features li {
        font-size: 14px; color: #6B5E52; padding: 8px 0;
        display: flex; align-items: center; gap: 10px;
        border-bottom: 1px solid rgba(232,93,4,0.06);
    }
    .pricing-features li::before { content: '✓'; color: #E85D04; font-weight: 700; flex-shrink: 0; }
    .pricing-cta {
        display: inline-block; width: 100%; padding: 14px;
        border-radius: 10px; font-weight: 700; font-size: 15px;
        text-align: center; text-decoration: none;
        cursor: pointer; transition: all 0.3s;
    }
    .pricing-cta.primary {
        background: linear-gradient(135deg,#E85D04,#7C3AED);
        color: white;
        box-shadow: 0 4px 20px rgba(232,93,4,0.3);
    }
    .pricing-cta.secondary {
        border: 2px solid rgba(232,93,4,0.3);
        color: #E85D04;
    }
    .pricing-cta.secondary:hover {
        border-color: #E85D04;
        background: rgba(232,93,4,0.05);
    }

    /* ===== PAGE HEADER ===== */
    .page-header {
        padding: 80px 60px 60px;
        text-align: center;
        background: linear-gradient(135deg, #FAF8F4, #F0EBE3);
        position: relative; overflow: hidden;
        border-bottom: 1px solid rgba(232,93,4,0.1);
    }
    .page-header-watermark {
        position: absolute; top: 50%; left: 50%;
        transform: translate(-50%,-50%);
        font-size: 180px; font-weight: 900;
        color: rgba(232,93,4,0.04);
        pointer-events: none; line-height: 1; white-space: nowrap;
    }

    /* ===== SERVICE DETAIL (zig-zag) ===== */
    .service-detail {
        display: flex; align-items: center; gap: 60px;
        max-width: 1000px; margin: 0 auto 60px; padding: 0 20px;
    }
    .service-detail.reverse { flex-direction: row-reverse; }
    .service-detail-icon-block {
        flex-shrink: 0; width: 160px; height: 160px;
        border-radius: 24px;
        background: linear-gradient(135deg,rgba(232,93,4,0.08),rgba(124,58,237,0.08));
        border: 1px solid rgba(232,93,4,0.2);
        display: flex; align-items: center; justify-content: center;
        font-size: 64px; transition: all 0.3s;
        box-shadow: 0 8px 32px rgba(232,93,4,0.1);
    }
    .service-detail-icon-block:hover {
        box-shadow: 0 16px 50px rgba(232,93,4,0.18);
        transform: translateY(-4px);
    }
    .service-detail-title {
        font-size: 28px; font-weight: 800; color: #1C1107;
        margin-bottom: 12px; letter-spacing: -0.5px;
    }
    .service-detail-desc { font-size: 16px; color: #6B5E52; line-height: 1.7; margin-bottom: 20px; }
    .service-detail-list {
        list-style: none;
        display: grid; grid-template-columns: 1fr 1fr; gap: 8px;
    }
    .service-detail-list li {
        font-size: 14px; color: #A89888;
        display: flex; align-items: center; gap: 8px;
    }
    .service-detail-list li::before { content: '→'; color: #E85D04; }

    /* ===== GRADIENT DIVIDER ===== */
    .gradient-divider {
        height: 1px;
        background: linear-gradient(135deg,transparent,#E85D04,#7C3AED,transparent);
        margin: 0 60px; opacity: 0.25;
    }

    /* ===== INDUSTRY TAGS ===== */
    .industry-tags {
        display: flex; gap: 12px; flex-wrap: wrap;
        justify-content: center; max-width: 800px; margin: 0 auto;
    }
    .industry-tag {
        background: rgba(232,93,4,0.06);
        border: 1.5px solid rgba(232,93,4,0.2);
        border-radius: 100px; padding: 12px 24px;
        font-size: 14px; color: #E85D04; font-weight: 600;
        transition: all 0.3s;
    }
    .industry-tag:hover {
        background: rgba(232,93,4,0.12);
        border-color: rgba(232,93,4,0.4);
        box-shadow: 0 4px 16px rgba(232,93,4,0.12);
    }

    /* ===== TRUST BADGES ===== */
    .trust-badges {
        display: flex; gap: 32px; justify-content: center;
        flex-wrap: wrap; margin-top: 48px;
    }
    .trust-badge {
        display: flex; align-items: center; gap: 10px;
        font-size: 14px; color: #A89888; font-weight: 500;
    }
    .trust-badge-icon { color: #E85D04; font-size: 18px; }

    /* ===== CONTACT FORM CONTAINER ===== */
    .contact-form-container {
        background: #FFFFFF;
        border: 1px solid rgba(232,93,4,0.15);
        border-radius: 20px; padding: 40px;
        box-shadow: 0 4px 24px rgba(28,17,7,0.06);
    }

    /* ===== BLOG CARDS ===== */
    .blog-card {
        background: #FFFFFF;
        border: 1px solid rgba(232,93,4,0.12);
        border-radius: 16px; overflow: hidden;
        transition: all 0.35s;
        box-shadow: 0 4px 20px rgba(28,17,7,0.05);
    }
    .blog-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 60px rgba(232,93,4,0.14);
        border-color: rgba(232,93,4,0.25);
    }
    .blog-card-img { width: 100%; height: 200px; object-fit: cover; display: block; transition: transform 0.5s; }
    .blog-card:hover .blog-card-img { transform: scale(1.04); }
    .blog-card-body { padding: 24px; }
    .blog-tag {
        display: inline-block;
        background: rgba(232,93,4,0.08);
        border: 1px solid rgba(232,93,4,0.2);
        color: #E85D04; font-size: 11px; font-weight: 700;
        letter-spacing: 1.5px; text-transform: uppercase;
        padding: 4px 12px; border-radius: 100px; margin-bottom: 12px;
    }
    .blog-card-title { font-size: 17px; font-weight: 700; color: #1C1107; margin-bottom: 10px; line-height: 1.4; }
    .blog-card-excerpt { font-size: 14px; color: #6B5E52; line-height: 1.7; margin-bottom: 16px; }
    .blog-card-meta { font-size: 12px; color: #A89888; display: flex; align-items: center; gap: 12px; }
    .blog-featured {
        border-radius: 20px; overflow: hidden; position: relative;
        height: 400px; transition: all 0.4s;
        box-shadow: 0 8px 40px rgba(28,17,7,0.12);
    }
    .blog-featured:hover { transform: translateY(-5px); box-shadow: 0 24px 70px rgba(232,93,4,0.2); }
    .blog-featured img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.5s; }
    .blog-featured:hover img { transform: scale(1.04); }
    .blog-featured-overlay {
        position: absolute; inset: 0;
        background: linear-gradient(180deg, rgba(28,14,5,0.05) 0%, rgba(28,14,5,0.88) 100%);
        display: flex; flex-direction: column; justify-content: flex-end; padding: 36px;
    }

    /* ===== CAREER CARDS ===== */
    .career-card {
        background: #FFFFFF;
        border: 1px solid rgba(232,93,4,0.12);
        border-radius: 16px; padding: 28px 32px;
        transition: all 0.35s;
        box-shadow: 0 4px 20px rgba(28,17,7,0.05);
        display: flex; align-items: flex-start; gap: 20px;
    }
    .career-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 16px 50px rgba(232,93,4,0.12);
        border-color: rgba(232,93,4,0.3);
    }
    .career-card-icon {
        flex-shrink: 0; width: 56px; height: 56px;
        background: linear-gradient(135deg,rgba(232,93,4,0.1),rgba(124,58,237,0.1));
        border-radius: 14px; font-size: 26px;
        display: flex; align-items: center; justify-content: center;
    }
    .career-card-title { font-size: 18px; font-weight: 700; color: #1C1107; margin-bottom: 6px; }
    .career-card-dept { font-size: 13px; color: #E85D04; font-weight: 600; margin-bottom: 10px; }
    .career-card-desc { font-size: 14px; color: #6B5E52; line-height: 1.7; margin-bottom: 14px; }
    .career-badge {
        display: inline-block; font-size: 11px; font-weight: 600;
        padding: 4px 12px; border-radius: 100px; margin-right: 8px; margin-bottom: 4px;
    }
    .career-badge.location { background: rgba(124,58,237,0.08); color: #7C3AED; border: 1px solid rgba(124,58,237,0.2); }
    .career-badge.type { background: rgba(232,93,4,0.08); color: #E85D04; border: 1px solid rgba(232,93,4,0.2); }
    .career-value-card {
        background: #FFFFFF;
        border: 1px solid rgba(232,93,4,0.12);
        border-radius: 20px; padding: 36px 28px; text-align: center;
        transition: all 0.35s;
        box-shadow: 0 4px 20px rgba(28,17,7,0.05);
    }
    .career-value-card:hover {
        border-color: rgba(232,93,4,0.3);
        box-shadow: 0 16px 50px rgba(232,93,4,0.1);
        transform: translateY(-5px);
    }
    .career-value-icon { font-size: 44px; margin-bottom: 16px; }
    .career-value-title { font-size: 18px; font-weight: 700; color: #1C1107; margin-bottom: 12px; }
    .career-value-desc { font-size: 14px; color: #6B5E52; line-height: 1.7; }

    /* ===== ANIMATIONS ===== */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(24px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-30px); }
        to { opacity: 1; transform: translateX(0); }
    }
    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(30px); }
        to { opacity: 1; transform: translateX(0); }
    }
    @keyframes shimmer {
        0% { background-position: -200% center; }
        100% { background-position: 200% center; }
    }
    .animate-left { animation: slideInLeft 0.8s ease forwards; }
    .animate-right { animation: slideInRight 0.8s ease forwards; }

    /* Pulsing dot */
    .pulse-dot {
        width: 10px; height: 10px; border-radius: 50%; background: #E85D04;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.4); opacity: 0.6; }
    }

    /* ===== RESPONSIVE ===== */
    @media (max-width: 768px) {
        .hero-bg { flex-direction: column; padding: 40px 24px; min-height: auto; }
        .section { padding: 60px 24px; }
        .navbar { padding: 16px 24px; }
        .split-cards { grid-template-columns: 1fr; }
        .contact-grid { grid-template-columns: 1fr; }
        .footer-grid { grid-template-columns: 1fr; gap: 32px; }
        .process-steps { flex-direction: column; gap: 24px; }
        .step-connector { display: none; }
        .stats-grid { grid-template-columns: 1fr 1fr; }
    }
</style>"""
