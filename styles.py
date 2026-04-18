GLOBAL_CSS = """<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    /* ===== RESET & BASE ===== */
    * { margin: 0; padding: 0; box-sizing: border-box; }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif !important;
        background-color: #0B1F3A !important;
        color: #E2E8F0 !important;
    }

    /* Hide Streamlit defaults */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
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

    /* Sidebar nav styling */
    [data-testid="stSidebar"] {
        background: #0D2347 !important;
        border-right: 1px solid rgba(37,99,235,0.3);
    }

    [data-testid="stSidebar"] a {
        color: #94A3B8 !important;
        text-decoration: none;
        transition: color 0.3s;
    }

    [data-testid="stSidebar"] a:hover {
        color: #2563EB !important;
    }

    /* ===== TYPOGRAPHY ===== */
    .gradient-text {
        background: linear-gradient(135deg, #2563EB, #7C3AED, #F97316);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .blue-purple-gradient {
        background: linear-gradient(135deg, #2563EB, #7C3AED);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    /* ===== NAVBAR ===== */
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 18px 60px;
        background: rgba(11,31,58,0.95);
        backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(37,99,235,0.2);
        position: sticky;
        top: 0;
        z-index: 999;
        width: 100%;
    }

    .navbar-logo {
        font-size: 24px;
        font-weight: 800;
        background: linear-gradient(135deg, #2563EB, #7C3AED);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -0.5px;
    }

    .navbar-tagline {
        font-size: 11px;
        color: #64748B;
        font-weight: 400;
        letter-spacing: 0.5px;
    }

    .navbar-links {
        display: flex;
        gap: 40px;
        align-items: center;
        list-style: none;
    }

    .navbar-links a {
        color: #94A3B8;
        text-decoration: none;
        font-size: 14px;
        font-weight: 500;
        transition: color 0.3s;
    }

    .navbar-links a:hover { color: #E2E8F0; }

    .btn-gradient {
        background: linear-gradient(135deg, #2563EB, #7C3AED);
        color: white !important;
        padding: 10px 24px;
        border-radius: 8px;
        font-weight: 600;
        font-size: 14px;
        border: none;
        cursor: pointer;
        text-decoration: none !important;
        display: inline-block;
        transition: all 0.3s;
        box-shadow: 0 0 20px rgba(37,99,235,0.3);
    }

    .btn-gradient:hover {
        box-shadow: 0 0 30px rgba(37,99,235,0.5);
        transform: translateY(-1px);
    }

    .btn-outline {
        background: transparent;
        color: #E2E8F0 !important;
        padding: 10px 24px;
        border-radius: 8px;
        font-weight: 600;
        font-size: 14px;
        border: 1.5px solid rgba(37,99,235,0.6);
        cursor: pointer;
        text-decoration: none !important;
        display: inline-block;
        transition: all 0.3s;
    }

    .btn-outline:hover {
        border-color: #2563EB;
        box-shadow: 0 0 15px rgba(37,99,235,0.3);
    }

    /* ===== HERO SECTION (legacy) ===== */
    .hero-section {
        min-height: 90vh;
        background: radial-gradient(ellipse at 20% 50%, rgba(37,99,235,0.15) 0%, transparent 50%),
                    radial-gradient(ellipse at 80% 20%, rgba(124,58,237,0.15) 0%, transparent 50%),
                    linear-gradient(180deg, #0B1F3A 0%, #0D1B2E 100%);
        display: flex;
        align-items: center;
        padding: 60px;
        position: relative;
        overflow: hidden;
    }

    .hero-section::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -20%;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(37,99,235,0.08) 0%, transparent 70%);
        animation: float 6s ease-in-out infinite;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }

    @keyframes glow-pulse {
        0%, 100% { box-shadow: 0 0 40px rgba(37,99,235,0.3), 0 0 80px rgba(124,58,237,0.2); }
        50% { box-shadow: 0 0 60px rgba(37,99,235,0.5), 0 0 120px rgba(124,58,237,0.3); }
    }

    .hero-left {
        flex: 1;
        max-width: 55%;
        z-index: 2;
    }

    .hero-right {
        flex: 1;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 2;
    }

    .hero-eyebrow {
        font-size: 13px;
        font-weight: 600;
        color: #7C3AED;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .hero-eyebrow::before {
        content: '';
        display: inline-block;
        width: 30px;
        height: 2px;
        background: linear-gradient(135deg, #2563EB, #7C3AED);
    }

    .hero-h1 {
        font-size: clamp(38px, 5vw, 62px);
        font-weight: 900;
        line-height: 1.1;
        letter-spacing: -1.5px;
        color: #F1F5F9;
        margin-bottom: 24px;
    }

    .hero-sub {
        font-size: 18px;
        line-height: 1.7;
        color: #94A3B8;
        max-width: 520px;
        margin-bottom: 40px;
        font-weight: 400;
    }

    .hero-cta-group {
        display: flex;
        gap: 16px;
        flex-wrap: wrap;
    }

    .logo-centerpiece {
        width: 320px;
        height: 320px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(37,99,235,0.2) 0%, rgba(124,58,237,0.1) 50%, transparent 70%);
        display: flex;
        align-items: center;
        justify-content: center;
        animation: glow-pulse 3s ease-in-out infinite;
        position: relative;
    }

    .logo-wave-text {
        font-size: 100px;
        font-weight: 900;
        background: linear-gradient(135deg, #2563EB, #7C3AED, #F97316);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1;
        animation: float 4s ease-in-out infinite;
    }

    /* ===== TRUST STRIP ===== */
    .trust-strip {
        background: rgba(13,35,71,0.8);
        border-top: 1px solid rgba(37,99,235,0.2);
        border-bottom: 1px solid rgba(37,99,235,0.2);
        padding: 28px 60px;
    }

    .trust-items {
        display: flex;
        justify-content: center;
        gap: 60px;
        flex-wrap: wrap;
    }

    .trust-item {
        display: flex;
        align-items: center;
        gap: 10px;
        color: #94A3B8;
        font-size: 14px;
        font-weight: 500;
        transition: all 0.3s;
        cursor: default;
    }

    .trust-item:hover {
        color: #E2E8F0;
    }

    .trust-icon {
        font-size: 20px;
        filter: drop-shadow(0 0 6px rgba(37,99,235,0.6));
        transition: filter 0.3s;
    }

    .trust-item:hover .trust-icon {
        filter: drop-shadow(0 0 10px rgba(37,99,235,0.9));
    }

    /* ===== SECTION COMMON ===== */
    .section {
        padding: 80px 60px;
        width: 100%;
    }

    .section-dark {
        background: #0B1F3A;
    }

    .section-darker {
        background: #081729;
    }

    .section-label {
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: #2563EB;
        margin-bottom: 12px;
        text-align: center;
    }

    .section-title {
        font-size: clamp(32px, 4vw, 48px);
        font-weight: 800;
        letter-spacing: -1px;
        line-height: 1.15;
        color: #F1F5F9;
        margin-bottom: 16px;
        text-align: center;
    }

    .section-subtitle {
        font-size: 17px;
        color: #94A3B8;
        max-width: 560px;
        margin: 0 auto 56px;
        line-height: 1.7;
        text-align: center;
    }

    /* ===== CARDS ===== */
    .cards-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
        gap: 24px;
        max-width: 1200px;
        margin: 0 auto;
    }

    .service-card {
        background: rgba(13,35,71,0.7);
        border: 1px solid rgba(37,99,235,0.2);
        border-radius: 16px;
        padding: 32px 28px;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }

    .service-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(135deg, #2563EB, #7C3AED);
        opacity: 0;
        transition: opacity 0.3s;
    }

    .service-card:hover {
        border-color: rgba(37,99,235,0.5);
        box-shadow: 0 0 30px rgba(37,99,235,0.2);
        transform: translateY(-4px);
    }

    .service-card:hover::before { opacity: 1; }

    .card-icon {
        font-size: 36px;
        margin-bottom: 16px;
        display: block;
        filter: drop-shadow(0 0 8px rgba(37,99,235,0.5));
    }

    .card-title {
        font-size: 18px;
        font-weight: 700;
        color: #F1F5F9;
        margin-bottom: 12px;
    }

    .card-desc {
        font-size: 14px;
        color: #94A3B8;
        line-height: 1.7;
        margin-bottom: 16px;
    }

    .card-bullets {
        list-style: none;
        margin-top: 12px;
    }

    .card-bullets li {
        font-size: 13px;
        color: #64748B;
        padding: 4px 0;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .card-bullets li::before {
        content: '→';
        color: #2563EB;
        font-size: 12px;
    }

    /* ===== ABOUT SECTION ===== */
    .about-section {
        background: radial-gradient(ellipse at center, rgba(37,99,235,0.08) 0%, transparent 70%);
        text-align: center;
        padding: 80px 60px;
    }

    .about-content {
        max-width: 800px;
        margin: 0 auto;
    }

    .about-icon {
        font-size: 48px;
        margin-bottom: 20px;
        filter: drop-shadow(0 0 12px rgba(37,99,235,0.6));
    }

    .about-body {
        font-size: 18px;
        line-height: 1.8;
        color: #94A3B8;
        margin-bottom: 32px;
    }

    .about-tags {
        display: flex;
        gap: 12px;
        justify-content: center;
        flex-wrap: wrap;
    }

    .about-tag {
        background: rgba(37,99,235,0.15);
        border: 1px solid rgba(37,99,235,0.3);
        border-radius: 100px;
        padding: 8px 20px;
        font-size: 13px;
        color: #93C5FD;
        font-weight: 500;
    }

    /* ===== WHO WE WORK WITH ===== */
    .split-cards {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 32px;
        max-width: 900px;
        margin: 0 auto;
    }

    .split-card {
        background: rgba(13,35,71,0.6);
        border: 1px solid rgba(124,58,237,0.25);
        border-radius: 20px;
        padding: 40px 32px;
        transition: all 0.3s;
    }

    .split-card:hover {
        border-color: rgba(124,58,237,0.5);
        box-shadow: 0 0 30px rgba(124,58,237,0.15);
    }

    .split-card-icon {
        font-size: 40px;
        margin-bottom: 16px;
    }

    .split-card-title {
        font-size: 20px;
        font-weight: 700;
        color: #F1F5F9;
        margin-bottom: 12px;
    }

    .split-card-list {
        list-style: none;
        margin-top: 16px;
    }

    .split-card-list li {
        font-size: 14px;
        color: #94A3B8;
        padding: 6px 0;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .split-card-list li::before {
        content: '✓';
        color: #2563EB;
        font-weight: 700;
    }

    /* ===== PROCESS STEPS ===== */
    .process-steps {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;
        gap: 0;
        margin-top: 48px;
    }

    .process-step {
        background: rgba(13,35,71,0.6);
        border: 1px solid rgba(37,99,235,0.2);
        border-radius: 16px;
        padding: 32px 24px;
        text-align: center;
        position: relative;
        transition: all 0.3s;
    }

    .process-step:hover {
        border-color: rgba(37,99,235,0.5);
        box-shadow: 0 0 30px rgba(37,99,235,0.2);
        transform: translateY(-4px);
    }

    .step-number {
        font-size: 48px;
        font-weight: 900;
        background: linear-gradient(135deg, #2563EB, #7C3AED);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1;
        margin-bottom: 12px;
    }

    .step-title {
        font-size: 18px;
        font-weight: 700;
        color: #F1F5F9;
        margin-bottom: 8px;
    }

    .step-desc {
        font-size: 13px;
        color: #94A3B8;
        line-height: 1.6;
    }

    .step-connector {
        height: 2px;
        background: linear-gradient(135deg, #2563EB, #7C3AED);
        opacity: 0.4;
        flex-shrink: 0;
    }

    /* ===== WHY GRID ===== */
    .why-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 20px;
        max-width: 900px;
        margin: 0 auto;
    }

    .why-item {
        display: flex;
        align-items: center;
        gap: 16px;
        background: rgba(13,35,71,0.5);
        border: 1px solid rgba(37,99,235,0.15);
        border-radius: 12px;
        padding: 18px 20px;
        transition: all 0.3s;
    }

    .why-item:hover {
        border-color: rgba(37,99,235,0.35);
        background: rgba(37,99,235,0.08);
    }

    .why-check {
        color: #2563EB;
        font-size: 16px;
        font-weight: 700;
        flex-shrink: 0;
    }

    .why-text {
        font-size: 14px;
        color: #CBD5E1;
        line-height: 1.5;
    }

    /* ===== CTA BANNER ===== */
    .cta-banner {
        background: linear-gradient(135deg, rgba(37,99,235,0.12) 0%, rgba(124,58,237,0.12) 100%);
        border-top: 1px solid rgba(37,99,235,0.2);
        border-bottom: 1px solid rgba(37,99,235,0.2);
        padding: 80px 60px;
        text-align: center;
    }

    .cta-title {
        font-size: clamp(28px, 3.5vw, 44px);
        font-weight: 800;
        letter-spacing: -1px;
        color: #F1F5F9;
        margin-bottom: 16px;
    }

    .cta-sub {
        font-size: 17px;
        color: #94A3B8;
        max-width: 500px;
        margin: 0 auto 40px;
        line-height: 1.7;
    }

    .cta-buttons {
        display: flex;
        gap: 16px;
        justify-content: center;
        flex-wrap: wrap;
    }

    /* ===== PAGE HEADER ===== */
    .page-header {
        background: linear-gradient(135deg, rgba(37,99,235,0.12) 0%, rgba(124,58,237,0.08) 100%),
                    #081729;
        border-bottom: 1px solid rgba(37,99,235,0.2);
        padding: 80px 60px 60px;
        text-align: center;
        position: relative;
        overflow: hidden;
    }

    .page-header-watermark {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: clamp(80px, 15vw, 160px);
        font-weight: 900;
        color: rgba(37,99,235,0.04);
        letter-spacing: 10px;
        pointer-events: none;
        white-space: nowrap;
    }

    /* ===== GRADIENT DIVIDER ===== */
    .gradient-divider {
        height: 1px;
        background: linear-gradient(135deg, transparent, rgba(37,99,235,0.3), rgba(124,58,237,0.3), transparent);
        width: 100%;
    }

    /* ===== SERVICE DETAIL ===== */
    .service-detail {
        display: flex;
        align-items: center;
        gap: 60px;
        max-width: 1000px;
        margin: 0 auto;
    }

    .service-detail.reverse {
        flex-direction: row-reverse;
    }

    .service-detail-icon-block {
        font-size: 80px;
        flex-shrink: 0;
        filter: drop-shadow(0 0 20px rgba(37,99,235,0.4));
        animation: float 4s ease-in-out infinite;
    }

    .service-detail-content {
        flex: 1;
    }

    .service-detail-title {
        font-size: clamp(24px, 3vw, 36px);
        font-weight: 800;
        color: #F1F5F9;
        margin-bottom: 16px;
        letter-spacing: -0.5px;
    }

    .service-detail-desc {
        font-size: 16px;
        color: #94A3B8;
        line-height: 1.8;
        margin-bottom: 24px;
    }

    .service-detail-list {
        list-style: none;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 8px 24px;
    }

    .service-detail-list li {
        font-size: 14px;
        color: #CBD5E1;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .service-detail-list li::before {
        content: '→';
        color: #2563EB;
        font-size: 12px;
        flex-shrink: 0;
    }

    /* ===== FOOTER ===== */
    .footer {
        background: #060F1C;
        border-top: 1px solid rgba(37,99,235,0.2);
        padding: 60px 60px 40px;
    }

    .footer-grid {
        display: grid;
        grid-template-columns: 2fr 1fr 1fr;
        gap: 60px;
        margin-bottom: 40px;
    }

    .footer-logo {
        font-size: 22px;
        font-weight: 800;
        background: linear-gradient(135deg, #2563EB, #7C3AED);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 16px;
    }

    .footer-tagline {
        font-size: 14px;
        color: #475569;
        line-height: 1.7;
        max-width: 320px;
    }

    .footer-heading {
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: #64748B;
        margin-bottom: 20px;
    }

    .footer-links {
        list-style: none;
        display: flex;
        flex-direction: column;
        gap: 12px;
    }

    .footer-links a {
        font-size: 14px;
        color: #475569;
        text-decoration: none;
        transition: color 0.3s;
    }

    .footer-links a:hover { color: #94A3B8; }

    .footer-bottom {
        border-top: 1px solid rgba(37,99,235,0.1);
        padding-top: 24px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 12px;
    }

    .footer-copy {
        font-size: 13px;
        color: #334155;
    }

    .footer-bottom-tagline {
        font-size: 13px;
        color: #2563EB;
        font-weight: 600;
        letter-spacing: 1px;
    }

    /* ===== NEW ADDITIONS ===== */

    /* Hero with background image */
    .hero-bg {
        min-height: 92vh;
        background-image: linear-gradient(135deg, rgba(11,31,58,0.93) 0%, rgba(37,99,235,0.15) 100%),
                          url('https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1920&q=80');
        background-size: cover;
        background-position: center;
        display: flex;
        align-items: center;
        padding: 60px;
        position: relative;
        overflow: hidden;
    }

    /* Floating stat badge */
    .stat-badge {
        background: rgba(13,35,71,0.85);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(37,99,235,0.4);
        border-radius: 16px;
        padding: 20px 28px;
        text-align: center;
        animation: float 4s ease-in-out infinite;
        margin-bottom: 16px;
    }
    .stat-badge-number { font-size: 32px; font-weight: 900; background: linear-gradient(135deg,#2563EB,#7C3AED); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text; }
    .stat-badge-label { font-size: 12px; color: #94A3B8; margin-top: 4px; }

    /* Partner logo strip */
    .partner-strip {
        background: rgba(13,35,71,0.6);
        border-top: 1px solid rgba(37,99,235,0.15);
        border-bottom: 1px solid rgba(37,99,235,0.15);
        padding: 28px 60px;
        overflow: hidden;
    }
    .partner-logos {
        display: flex;
        gap: 40px;
        align-items: center;
        justify-content: center;
        flex-wrap: wrap;
    }
    .partner-logo {
        font-size: 15px;
        font-weight: 700;
        color: #475569;
        padding: 8px 20px;
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 8px;
        transition: all 0.3s;
        letter-spacing: 0.5px;
    }
    .partner-logo:hover { color: #94A3B8; border-color: rgba(37,99,235,0.3); }

    /* Stats section */
    .stats-section {
        background: linear-gradient(135deg, rgba(37,99,235,0.12) 0%, rgba(124,58,237,0.12) 100%);
        border-top: 1px solid rgba(37,99,235,0.2);
        border-bottom: 1px solid rgba(37,99,235,0.2);
        padding: 60px;
    }
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 2px;
        max-width: 1000px;
        margin: 0 auto;
    }
    .stat-item {
        text-align: center;
        padding: 32px 24px;
        border-right: 1px solid rgba(37,99,235,0.15);
        position: relative;
    }
    .stat-item:last-child { border-right: none; }
    .stat-number {
        font-size: 52px;
        font-weight: 900;
        background: linear-gradient(135deg,#2563EB,#7C3AED,#F97316);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1;
        margin-bottom: 10px;
        animation: fadeInUp 0.8s ease forwards;
    }
    .stat-label { font-size: 14px; color: #94A3B8; font-weight: 500; line-height: 1.4; }
    .stat-sublabel { font-size: 12px; color: #475569; margin-top: 4px; }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Solution image card */
    .sol-img-card {
        border-radius: 16px;
        overflow: hidden;
        position: relative;
        height: 280px;
        cursor: pointer;
        transition: all 0.4s ease;
        border: 1px solid rgba(37,99,235,0.2);
    }
    .sol-img-card:hover { transform: translateY(-6px); box-shadow: 0 20px 60px rgba(37,99,235,0.25); }
    .sol-img-card img {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.4s ease;
    }
    .sol-img-card:hover img { transform: scale(1.05); }
    .sol-img-overlay {
        position: absolute;
        inset: 0;
        background: linear-gradient(180deg, rgba(11,31,58,0.2) 0%, rgba(11,31,58,0.85) 60%, rgba(11,31,58,0.97) 100%);
        display: flex;
        flex-direction: column;
        justify-content: flex-end;
        padding: 24px;
    }
    .sol-img-icon { font-size: 28px; margin-bottom: 8px; filter: drop-shadow(0 0 8px rgba(37,99,235,0.6)); }
    .sol-img-title { font-size: 18px; font-weight: 700; color: #F1F5F9; margin-bottom: 6px; }
    .sol-img-desc { font-size: 13px; color: #94A3B8; line-height: 1.5; }
    .sol-img-tag {
        position: absolute;
        top: 16px;
        right: 16px;
        background: linear-gradient(135deg,#2563EB,#7C3AED);
        color: white;
        font-size: 11px;
        font-weight: 700;
        padding: 4px 12px;
        border-radius: 100px;
        letter-spacing: 1px;
    }

    /* Feature card (How We Work) */
    .feature-card {
        background: rgba(13,35,71,0.7);
        border: 1px solid rgba(37,99,235,0.2);
        border-radius: 20px;
        padding: 40px 32px;
        text-align: center;
        transition: all 0.3s;
        position: relative;
        overflow: hidden;
    }
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 4px;
        background: linear-gradient(135deg,#2563EB,#7C3AED,#F97316);
        transform: scaleX(0);
        transition: transform 0.3s;
    }
    .feature-card:hover::before { transform: scaleX(1); }
    .feature-card:hover {
        border-color: rgba(37,99,235,0.5);
        box-shadow: 0 0 40px rgba(37,99,235,0.15);
        transform: translateY(-4px);
    }
    .feature-num {
        font-size: 64px;
        font-weight: 900;
        background: linear-gradient(135deg, rgba(37,99,235,0.15), rgba(124,58,237,0.15));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1;
        margin-bottom: 16px;
    }
    .feature-icon { font-size: 44px; margin-bottom: 16px; filter: drop-shadow(0 0 10px rgba(37,99,235,0.5)); }
    .feature-title { font-size: 22px; font-weight: 800; color: #F1F5F9; margin-bottom: 12px; }
    .feature-desc { font-size: 15px; color: #94A3B8; line-height: 1.7; }

    /* Testimonial card */
    .testimonial-card {
        background: rgba(13,35,71,0.7);
        border: 1px solid rgba(37,99,235,0.15);
        border-radius: 20px;
        padding: 36px 32px;
        backdrop-filter: blur(10px);
        transition: all 0.3s;
        position: relative;
    }
    .testimonial-card::before {
        content: '"';
        position: absolute;
        top: 20px; right: 24px;
        font-size: 80px;
        color: rgba(37,99,235,0.15);
        font-family: Georgia, serif;
        line-height: 1;
    }
    .testimonial-card:hover {
        border-color: rgba(37,99,235,0.35);
        box-shadow: 0 0 30px rgba(37,99,235,0.12);
    }
    .testimonial-stars { color: #F97316; font-size: 18px; margin-bottom: 16px; letter-spacing: 2px; }
    .testimonial-text { font-size: 15px; color: #CBD5E1; line-height: 1.75; margin-bottom: 24px; font-style: italic; }
    .testimonial-author { display: flex; align-items: center; gap: 14px; }
    .testimonial-avatar {
        width: 48px; height: 48px; border-radius: 50%;
        background: linear-gradient(135deg,#2563EB,#7C3AED);
        display: flex; align-items: center; justify-content: center;
        font-size: 18px; font-weight: 700; color: white; flex-shrink: 0;
        box-shadow: 0 0 15px rgba(37,99,235,0.4);
    }
    .testimonial-name { font-size: 15px; font-weight: 700; color: #F1F5F9; }
    .testimonial-role { font-size: 12px; color: #64748B; }

    /* Industry image card */
    .industry-img-card {
        border-radius: 16px;
        overflow: hidden;
        position: relative;
        height: 220px;
        transition: all 0.3s;
        border: 1px solid rgba(37,99,235,0.15);
    }
    .industry-img-card:hover { transform: translateY(-4px); box-shadow: 0 20px 50px rgba(37,99,235,0.2); }
    .industry-img-card img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.4s; }
    .industry-img-card:hover img { transform: scale(1.06); }
    .industry-img-overlay {
        position: absolute; inset: 0;
        background: linear-gradient(180deg, rgba(11,31,58,0.3) 0%, rgba(11,31,58,0.88) 100%);
        display: flex; flex-direction: column; justify-content: flex-end; padding: 20px;
    }
    .industry-img-title { font-size: 17px; font-weight: 700; color: #F1F5F9; margin-bottom: 4px; }
    .industry-img-sub { font-size: 12px; color: #94A3B8; }

    /* About section with image */
    .about-img {
        border-radius: 20px;
        overflow: hidden;
        position: relative;
        box-shadow: 0 20px 60px rgba(37,99,235,0.25);
    }
    .about-img img { width: 100%; height: 100%; object-fit: cover; border-radius: 20px; }
    .about-img-badge {
        position: absolute;
        bottom: 24px; left: 24px;
        background: linear-gradient(135deg, #2563EB, #7C3AED);
        border-radius: 12px;
        padding: 16px 20px;
        backdrop-filter: blur(10px);
    }
    .about-img-badge-num { font-size: 28px; font-weight: 900; color: white; }
    .about-img-badge-text { font-size: 12px; color: rgba(255,255,255,0.8); }

    /* Tabs override */
    .stTabs [data-baseweb="tab-list"] {
        background: rgba(13,35,71,0.6) !important;
        border-radius: 12px !important;
        padding: 6px !important;
        gap: 4px !important;
        border: 1px solid rgba(37,99,235,0.2) !important;
    }
    .stTabs [data-baseweb="tab"] {
        background: transparent !important;
        color: #64748B !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        font-size: 14px !important;
        padding: 10px 20px !important;
        transition: all 0.3s !important;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #2563EB, #7C3AED) !important;
        color: white !important;
    }
    .stTabs [data-baseweb="tab-border"] { display: none !important; }
    .stTabs [data-baseweb="tab-panel"] { padding-top: 32px !important; }

    /* Scroll reveal animation */
    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-30px); }
        to { opacity: 1; transform: translateX(0); }
    }
    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(30px); }
        to { opacity: 1; transform: translateX(0); }
    }
    .animate-left { animation: slideInLeft 0.8s ease forwards; }
    .animate-right { animation: slideInRight 0.8s ease forwards; }

</style>"""
