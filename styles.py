GLOBAL_CSS = """
<style>
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

    /* ===== HERO SECTION ===== */
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
        margin-bottom: 16px;
    }

    .split-card-list {
        list-style: none;
    }

    .split-card-list li {
        font-size: 15px;
        color: #94A3B8;
        padding: 6px 0;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .split-card-list li::before {
        content: '✓';
        color: #7C3AED;
        font-weight: 700;
    }

    /* ===== WHY CHOOSE US ===== */
    .why-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 20px;
        max-width: 1000px;
        margin: 0 auto;
    }

    .why-item {
        display: flex;
        align-items: flex-start;
        gap: 14px;
        background: rgba(13,35,71,0.5);
        border: 1px solid rgba(37,99,235,0.15);
        border-radius: 12px;
        padding: 20px;
        transition: all 0.3s;
    }

    .why-item:hover {
        border-color: rgba(37,99,235,0.4);
        background: rgba(13,35,71,0.8);
    }

    .why-check {
        color: #2563EB;
        font-size: 20px;
        margin-top: 2px;
        flex-shrink: 0;
    }

    .why-text {
        font-size: 14px;
        color: #CBD5E1;
        line-height: 1.6;
        font-weight: 500;
    }

    /* ===== PROCESS ===== */
    .process-steps {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 0;
        flex-wrap: wrap;
        max-width: 1100px;
        margin: 0 auto;
        position: relative;
    }

    .process-step {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        width: 180px;
        position: relative;
        z-index: 2;
    }

    .step-connector {
        width: 60px;
        height: 2px;
        background: linear-gradient(135deg, #2563EB, #7C3AED);
        margin-top: -52px;
        position: relative;
        z-index: 1;
    }

    .step-number {
        width: 56px;
        height: 56px;
        border-radius: 50%;
        background: linear-gradient(135deg, #2563EB, #7C3AED);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
        font-weight: 800;
        color: white;
        margin-bottom: 16px;
        box-shadow: 0 0 20px rgba(37,99,235,0.4);
        position: relative;
    }

    .step-number::after {
        content: '';
        position: absolute;
        inset: -4px;
        border-radius: 50%;
        border: 2px solid rgba(37,99,235,0.3);
    }

    .step-title {
        font-size: 15px;
        font-weight: 700;
        color: #F1F5F9;
        margin-bottom: 6px;
    }

    .step-desc {
        font-size: 12px;
        color: #64748B;
        line-height: 1.5;
        padding: 0 8px;
    }

    /* ===== METRICS ===== */
    .metrics-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 24px;
        max-width: 900px;
        margin: 0 auto;
    }

    .metric-card {
        background: rgba(13,35,71,0.7);
        border: 1px solid rgba(37,99,235,0.2);
        border-radius: 16px;
        padding: 40px 32px;
        text-align: center;
        transition: all 0.3s;
    }

    .metric-card:hover {
        border-color: rgba(37,99,235,0.5);
        box-shadow: 0 0 40px rgba(37,99,235,0.15);
        transform: translateY(-4px);
    }

    .metric-number {
        font-size: clamp(42px, 5vw, 60px);
        font-weight: 900;
        background: linear-gradient(135deg, #2563EB, #7C3AED, #F97316);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1;
        margin-bottom: 12px;
    }

    .metric-label {
        font-size: 15px;
        color: #94A3B8;
        font-weight: 500;
    }

    /* ===== CTA BANNER ===== */
    .cta-banner {
        background: linear-gradient(135deg, rgba(37,99,235,0.3) 0%, rgba(124,58,237,0.3) 50%, rgba(249,115,22,0.2) 100%);
        border-top: 1px solid rgba(37,99,235,0.3);
        border-bottom: 1px solid rgba(37,99,235,0.3);
        padding: 80px 60px;
        text-align: center;
        position: relative;
        overflow: hidden;
    }

    .cta-banner::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 600px;
        height: 300px;
        background: radial-gradient(ellipse, rgba(37,99,235,0.15) 0%, transparent 70%);
    }

    .cta-title {
        font-size: clamp(28px, 4vw, 46px);
        font-weight: 800;
        letter-spacing: -1px;
        color: #F1F5F9;
        margin-bottom: 16px;
        position: relative;
        z-index: 2;
    }

    .cta-sub {
        font-size: 17px;
        color: #94A3B8;
        margin-bottom: 40px;
        position: relative;
        z-index: 2;
    }

    .cta-buttons {
        display: flex;
        gap: 16px;
        justify-content: center;
        flex-wrap: wrap;
        position: relative;
        z-index: 2;
    }

    /* ===== INDUSTRIES ===== */
    .industry-tags {
        display: flex;
        gap: 12px;
        flex-wrap: wrap;
        justify-content: center;
        max-width: 800px;
        margin: 0 auto;
    }

    .industry-tag {
        background: rgba(37,99,235,0.1);
        border: 1px solid rgba(37,99,235,0.25);
        border-radius: 100px;
        padding: 12px 24px;
        font-size: 14px;
        color: #93C5FD;
        font-weight: 500;
        transition: all 0.3s;
    }

    .industry-tag:hover {
        background: rgba(37,99,235,0.2);
        border-color: rgba(37,99,235,0.5);
        box-shadow: 0 0 15px rgba(37,99,235,0.2);
        color: #BFDBFE;
    }

    /* ===== PRICING ===== */
    .pricing-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 24px;
        max-width: 1000px;
        margin: 0 auto;
    }

    .pricing-card {
        background: rgba(13,35,71,0.7);
        border: 1px solid rgba(37,99,235,0.2);
        border-radius: 20px;
        padding: 40px 32px;
        position: relative;
        transition: all 0.3s;
        text-align: center;
    }

    .pricing-card.featured {
        border: 2px solid transparent;
        background-clip: padding-box;
        position: relative;
    }

    .pricing-card.featured::before {
        content: '';
        position: absolute;
        inset: -2px;
        border-radius: 22px;
        background: linear-gradient(135deg, #2563EB, #7C3AED, #F97316);
        z-index: -1;
    }

    .pricing-card.featured::after {
        content: 'MOST POPULAR';
        position: absolute;
        top: -14px;
        left: 50%;
        transform: translateX(-50%);
        background: linear-gradient(135deg, #2563EB, #7C3AED);
        color: white;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 2px;
        padding: 4px 16px;
        border-radius: 100px;
        white-space: nowrap;
    }

    .pricing-card:hover {
        box-shadow: 0 0 40px rgba(37,99,235,0.2);
        transform: translateY(-4px);
    }

    .pricing-card-title {
        font-size: 20px;
        font-weight: 700;
        color: #F1F5F9;
        margin-bottom: 8px;
    }

    .pricing-card-subtitle {
        font-size: 13px;
        color: #64748B;
        margin-bottom: 28px;
    }

    .pricing-card-icon {
        font-size: 44px;
        margin-bottom: 20px;
        filter: drop-shadow(0 0 10px rgba(37,99,235,0.5));
    }

    .pricing-features {
        list-style: none;
        text-align: left;
        margin-bottom: 32px;
    }

    .pricing-features li {
        font-size: 14px;
        color: #94A3B8;
        padding: 8px 0;
        display: flex;
        align-items: center;
        gap: 10px;
        border-bottom: 1px solid rgba(37,99,235,0.08);
    }

    .pricing-features li::before {
        content: '✓';
        color: #2563EB;
        font-weight: 700;
        flex-shrink: 0;
    }

    .pricing-cta {
        display: inline-block;
        width: 100%;
        padding: 14px;
        border-radius: 10px;
        font-weight: 700;
        font-size: 15px;
        text-align: center;
        text-decoration: none;
        cursor: pointer;
        transition: all 0.3s;
    }

    .pricing-cta.primary {
        background: linear-gradient(135deg, #2563EB, #7C3AED);
        color: white;
        box-shadow: 0 0 20px rgba(37,99,235,0.3);
    }

    .pricing-cta.primary:hover {
        box-shadow: 0 0 35px rgba(37,99,235,0.5);
    }

    .pricing-cta.secondary {
        border: 1.5px solid rgba(37,99,235,0.4);
        color: #93C5FD;
    }

    .pricing-cta.secondary:hover {
        border-color: #2563EB;
        background: rgba(37,99,235,0.1);
    }

    /* ===== TRUST BADGES ===== */
    .trust-badges {
        display: flex;
        gap: 32px;
        justify-content: center;
        flex-wrap: wrap;
        margin-top: 48px;
    }

    .trust-badge {
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 14px;
        color: #64748B;
        font-weight: 500;
    }

    .trust-badge-icon {
        color: #2563EB;
        font-size: 18px;
    }

    /* ===== CONTACT ===== */
    .contact-grid {
        display: grid;
        grid-template-columns: 1fr 1.4fr;
        gap: 60px;
        max-width: 1000px;
        margin: 0 auto;
        align-items: start;
    }

    .contact-left-title {
        font-size: 36px;
        font-weight: 800;
        letter-spacing: -1px;
        line-height: 1.2;
        color: #F1F5F9;
        margin-bottom: 16px;
    }

    .contact-left-sub {
        font-size: 15px;
        color: #94A3B8;
        line-height: 1.7;
        margin-bottom: 40px;
    }

    .contact-info-item {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 16px;
    }

    .contact-info-icon {
        font-size: 20px;
        width: 40px;
        height: 40px;
        background: rgba(37,99,235,0.15);
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
    }

    .contact-info-text {
        font-size: 14px;
        color: #94A3B8;
    }

    .contact-form-container {
        background: rgba(13,35,71,0.7);
        border: 1px solid rgba(37,99,235,0.2);
        border-radius: 20px;
        padding: 40px;
    }

    /* Streamlit form override */
    .stTextInput input, .stTextArea textarea, .stSelectbox select {
        background: rgba(11,31,58,0.8) !important;
        border: 1px solid rgba(37,99,235,0.3) !important;
        border-radius: 8px !important;
        color: #E2E8F0 !important;
        font-size: 14px !important;
    }

    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #2563EB !important;
        box-shadow: 0 0 0 3px rgba(37,99,235,0.15) !important;
    }

    .stButton button {
        background: linear-gradient(135deg, #2563EB, #7C3AED) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        font-size: 15px !important;
        padding: 14px 32px !important;
        width: 100% !important;
        transition: all 0.3s !important;
        box-shadow: 0 0 20px rgba(37,99,235,0.3) !important;
    }

    .stButton button:hover {
        box-shadow: 0 0 35px rgba(37,99,235,0.5) !important;
        transform: translateY(-2px) !important;
    }

    /* ===== FOOTER ===== */
    .footer {
        background: #081729;
        border-top: 1px solid rgba(37,99,235,0.2);
        padding: 60px 60px 30px;
    }

    .footer-grid {
        display: grid;
        grid-template-columns: 1.5fr 1fr 1fr;
        gap: 60px;
        margin-bottom: 48px;
    }

    .footer-logo {
        font-size: 24px;
        font-weight: 800;
        background: linear-gradient(135deg, #2563EB, #7C3AED);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 12px;
    }

    .footer-tagline {
        font-size: 13px;
        color: #64748B;
        line-height: 1.7;
        max-width: 260px;
    }

    .footer-heading {
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: #475569;
        margin-bottom: 20px;
    }

    .footer-links {
        list-style: none;
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    .footer-links a {
        font-size: 14px;
        color: #64748B;
        text-decoration: none;
        transition: color 0.3s;
    }

    .footer-links a:hover { color: #93C5FD; }

    .footer-bottom {
        border-top: 1px solid rgba(37,99,235,0.1);
        padding-top: 24px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .footer-copy {
        font-size: 13px;
        color: #334155;
    }

    .footer-bottom-tagline {
        font-size: 13px;
        color: #334155;
        font-style: italic;
    }

    /* ===== PAGE HEADER ===== */
    .page-header {
        padding: 80px 60px 60px;
        text-align: center;
        background: radial-gradient(ellipse at center top, rgba(37,99,235,0.12) 0%, transparent 60%);
        position: relative;
        overflow: hidden;
    }

    .page-header-watermark {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 200px;
        font-weight: 900;
        color: rgba(37,99,235,0.04);
        pointer-events: none;
        line-height: 1;
        white-space: nowrap;
    }

    /* ===== DIVIDER ===== */
    .gradient-divider {
        height: 1px;
        background: linear-gradient(135deg, transparent, #2563EB, #7C3AED, transparent);
        margin: 0 60px;
        opacity: 0.4;
    }

    /* ===== SERVICE DETAIL (ZIG-ZAG) ===== */
    .service-detail {
        display: flex;
        align-items: center;
        gap: 60px;
        max-width: 1000px;
        margin: 0 auto 60px;
        padding: 0 20px;
    }

    .service-detail.reverse { flex-direction: row-reverse; }

    .service-detail-icon-block {
        flex-shrink: 0;
        width: 160px;
        height: 160px;
        border-radius: 24px;
        background: linear-gradient(135deg, rgba(37,99,235,0.15), rgba(124,58,237,0.15));
        border: 1px solid rgba(37,99,235,0.25);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 64px;
        filter: drop-shadow(0 0 20px rgba(37,99,235,0.3));
        transition: all 0.3s;
    }

    .service-detail-icon-block:hover {
        box-shadow: 0 0 40px rgba(37,99,235,0.2);
    }

    .service-detail-content {}

    .service-detail-title {
        font-size: 28px;
        font-weight: 800;
        color: #F1F5F9;
        margin-bottom: 12px;
        letter-spacing: -0.5px;
    }

    .service-detail-desc {
        font-size: 16px;
        color: #94A3B8;
        line-height: 1.7;
        margin-bottom: 20px;
    }

    .service-detail-list {
        list-style: none;
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 8px;
    }

    .service-detail-list li {
        font-size: 14px;
        color: #64748B;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .service-detail-list li::before {
        content: '→';
        color: #2563EB;
    }

    /* ===== RESPONSIVE ===== */
    @media (max-width: 768px) {
        .hero-section { flex-direction: column; padding: 40px 24px; }
        .hero-left { max-width: 100%; }
        .hero-right { display: none; }
        .section { padding: 60px 24px; }
        .navbar { padding: 16px 24px; }
        .trust-items { gap: 24px; }
        .split-cards { grid-template-columns: 1fr; }
        .contact-grid { grid-template-columns: 1fr; }
        .footer-grid { grid-template-columns: 1fr; gap: 32px; }
        .process-steps { flex-direction: column; gap: 24px; }
        .step-connector { display: none; }
    }
</style>
"""
