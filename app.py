import streamlit as st
from datetime import datetime, timedelta

# ── Page Config ──────────────────────────────────────────
st.set_page_config(
    page_title="📋 ฟอร์มแจ้ง Call Margin",
    page_icon="📋",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Sarabun', sans-serif;
    }

    .main {
        background: linear-gradient(135deg, #0f1923 0%, #1a2d3d 50%, #0f1923 100%);
        min-height: 100vh;
    }

    .stApp {
        background: linear-gradient(135deg, #0f1923 0%, #1a2d3d 50%, #0f1923 100%);
    }

    .header-box {
        background: linear-gradient(135deg, #1e3a5f, #2a5298);
        border: 1px solid #3d7abf;
        border-radius: 12px;
        padding: 20px 24px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(45, 120, 210, 0.3);
    }

    .header-box h1 {
        color: #e8f4fd;
        margin: 0;
        font-size: 1.6rem;
        font-weight: 700;
        letter-spacing: 0.5px;
    }

    .date-badge {
        background: rgba(255,255,255,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 20px;
        padding: 4px 14px;
        color: #a8d4f5;
        font-size: 0.85rem;
        display: inline-block;
        margin-top: 8px;
    }

    .section-card {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 16px;
    }

    .section-title {
        color: #7db9e8;
        font-size: 0.78rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-bottom: 12px;
        border-bottom: 1px solid rgba(125, 185, 232, 0.2);
        padding-bottom: 6px;
    }

    .output-box {
        background: rgba(20, 50, 80, 0.6);
        border: 1px solid #3d7abf;
        border-radius: 10px;
        padding: 20px;
        margin-top: 8px;
        color: #e8f4fd;
        font-size: 1rem;
        line-height: 1.8;
        white-space: pre-wrap;
        font-family: 'Sarabun', sans-serif;
        box-shadow: 0 0 20px rgba(45, 120, 210, 0.15);
    }

    /* Streamlit widget overrides */
    .stSelectbox > div > div {
        background: rgba(255,255,255,0.07) !important;
        border: 1px solid rgba(255,255,255,0.15) !important;
        color: #e8f4fd !important;
        border-radius: 8px !important;
    }

    .stNumberInput > div > div > input,
    .stTextInput > div > div > input {
        background: rgba(255,255,255,0.07) !important;
        border: 1px solid rgba(255,255,255,0.15) !important;
        color: #e8f4fd !important;
        border-radius: 8px !important;
    }

    .stCheckbox > label {
        color: #c8dff0 !important;
        font-size: 0.95rem !important;
    }

    label[data-testid="stWidgetLabel"] {
        color: #a8d4f5 !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
    }

    .copy-btn {
        background: linear-gradient(135deg, #1e6fbf, #2a8cde);
        color: white;
        border: none;
        padding: 10px 28px;
        border-radius: 8px;
        cursor: pointer;
        font-family: 'Sarabun', sans-serif;
        font-size: 0.95rem;
        font-weight: 600;
        margin-top: 10px;
        transition: all 0.2s;
    }

    .copy-btn:hover {
        background: linear-gradient(135deg, #2a8cde, #3da0f5);
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(45, 140, 222, 0.4);
    }

    div[data-testid="stHorizontalBlock"] {
        gap: 12px;
    }

    .stButton > button {
        background: linear-gradient(135deg, #1e6fbf, #2a8cde) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-family: 'Sarabun', sans-serif !important;
        font-weight: 600 !important;
        padding: 0.5rem 2rem !important;
        transition: all 0.2s !important;
    }

    .stButton > button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(45, 140, 222, 0.4) !important;
    }

    hr {
        border-color: rgba(255,255,255,0.1) !important;
    }
</style>
""", unsafe_allow_html=True)

# ── Date Calculation ──────────────────────────────────────
today_th = datetime.utcnow() + timedelta(hours=7)
session_date = today_th - timedelta(days=1)

def thai_date(dt):
    return dt.strftime(f"%d/%m/{dt.year + 543}")

session_date_str = thai_date(session_date)
today_str = thai_date(today_th)

# ── Header ────────────────────────────────────────────────
st.markdown(f"""
<div class="header-box">
    <h1>📋 ฟอร์มแจ้ง Call Margin</h1>
    <div class="date-badge">
        📅 วันที่ Session: <strong>{session_date_str}</strong>
        &nbsp;&nbsp;|&nbsp;&nbsp;
        วันไทยปัจจุบัน: {today_str}
    </div>
</div>
""", unsafe_allow_html=True)

# ── Form Fields ───────────────────────────────────────────
st.markdown('<div class="section-card"><div class="section-title">⚙️ ข้อมูล Session</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    session = st.selectbox(
        "Session",
        options=['ก่อนปิดตลาด', 'เปิดตลาด', 'กลางวัน'],
        index=0
    )
with col2:
    currency = st.selectbox(
        "สกุลเงิน",
        options=['USD', 'THB', 'EUR'],
        index=0
    )

amount = st.number_input(
    "จำนวนเงิน",
    min_value=0.0,
    value=1500.0,
    step=100.0,
    format="%.0f"
)

st.markdown('</div>', unsafe_allow_html=True)

# ── Time Period Checkboxes ────────────────────────────────
st.markdown('<div class="section-card"><div class="section-title">🕐 ช่วงเวลา</div>', unsafe_allow_html=True)

col_t, col_t1, col_t2, _ = st.columns([1, 1, 1, 3])
with col_t:
    t = st.checkbox("T", value=True)
with col_t1:
    t1 = st.checkbox("T+1", value=False)
with col_t2:
    t2 = st.checkbox("T+2", value=False)

st.markdown('</div>', unsafe_allow_html=True)

# ── Advisory Fields ───────────────────────────────────────
st.markdown('<div class="section-card"><div class="section-title">💬 คำแนะนำและหมายเหตุ</div>', unsafe_allow_html=True)

advice = st.text_input(
    "คำแนะนำ",
    value="แนะนำเติมเงินหรือลดสถานะจำนวนสัญญา"
)

remark = st.text_input(
    "หมายเหตุ",
    value="",
    placeholder="เช่น กรุณาดำเนินการก่อน 18:00 น."
)

st.markdown('</div>', unsafe_allow_html=True)

# ── Generate Message ──────────────────────────────────────
t_labels = []
if t:  t_labels.append('T')
if t1: t_labels.append('T+1')
if t2: t_labels.append('T+2')

t_str = f" เป็นช่วงเวลา {' / '.join(t_labels)}" if t_labels else ''
amount_fmt = f"{int(amount):,}"

message = (
    f"สวัสดีครับ ขอแจ้ง Call Margin สำหรับช่วง Trading Session {session}"
    f"ของวันที่ {session_date_str}\n"
    f"โดยมี Call Margin อยู่ที่ประมาณ {currency} {amount_fmt}{t_str}\n"
    f"{advice}ครับ"
)
if remark.strip():
    message += f"\n\nหมายเหตุ: {remark.strip()}"

# ── Output ────────────────────────────────────────────────
st.markdown("---")
st.markdown('<p style="color:#7db9e8; font-weight:600; font-size:0.9rem; text-transform:uppercase; letter-spacing:1px;">📤 ข้อความที่จะส่ง</p>', unsafe_allow_html=True)
st.markdown(f'<div class="output-box">{message}</div>', unsafe_allow_html=True)

# Copy button via clipboard API
st.markdown(f"""
<br>
<button class="copy-btn" onclick="
    navigator.clipboard.writeText(`{message.replace('`', chr(96))}`).then(() => {{
        this.textContent = '✅ คัดลอกแล้ว!';
        setTimeout(() => this.textContent = '📋 คัดลอกข้อความ', 2000);
    }});
">📋 คัดลอกข้อความ</button>
""", unsafe_allow_html=True)

# Text area for manual copy fallback
with st.expander("📝 คัดลอกแบบ manual (กรณีปุ่มด้านบนไม่ทำงาน)"):
    st.text_area("", value=message, height=130, label_visibility="collapsed")

st.markdown("<br><br>", unsafe_allow_html=True)
