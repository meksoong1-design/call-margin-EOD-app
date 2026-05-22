import streamlit as st
from datetime import datetime, timedelta
import streamlit.components.v1 as components
import html
import json

# Page Config
st.set_page_config(
    page_title="ฟอร์มแจ้ง Call Margin",
    page_icon=None,
    layout="centered",
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Sarabun', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #0f1923 0%, #1a2d3d 50%, #0f1923 100%);
    }

    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 1rem !important;
        padding-left: 1.2rem !important;
        padding-right: 1.2rem !important;
        max-width: 760px !important;
    }

    div[data-testid="stVerticalBlock"] {
        gap: 0.45rem !important;
    }

    div[data-testid="stHorizontalBlock"] {
        gap: 0.6rem !important;
    }

    .header-box {
        background: linear-gradient(135deg, #1e3a5f, #2a5298);
        border: 1px solid #3d7abf;
        border-radius: 10px;
        padding: 12px 16px;
        margin-bottom: 10px;
        box-shadow: 0 4px 16px rgba(45, 120, 210, 0.25);
    }

    .header-box h1 {
        color: #e8f4fd;
        margin: 0;
        font-size: 1.25rem;
        font-weight: 700;
        letter-spacing: 0.3px;
    }

    .date-badge {
        background: rgba(255,255,255,0.1);
        border: 1px solid rgba(255,255,255,0.18);
        border-radius: 999px;
        padding: 3px 10px;
        color: #a8d4f5;
        font-size: 0.78rem;
        display: inline-block;
        margin-top: 6px;
    }

    .section-card {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 10px;
        padding: 12px 14px;
        margin-bottom: 8px;
    }

    .section-title {
        color: #7db9e8;
        font-size: 0.72rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        margin-bottom: 6px;
        border-bottom: 1px solid rgba(125, 185, 232, 0.18);
        padding-bottom: 4px;
    }

    .output-label {
        color: #7db9e8;
        font-weight: 700;
        font-size: 0.78rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin: 4px 0 6px 0;
    }

    .output-box {
        background: rgba(20, 50, 80, 0.6);
        border: 1px solid #3d7abf;
        border-radius: 10px;
        padding: 12px 14px;
        margin-top: 4px;
        color: #e8f4fd;
        font-size: 0.9rem;
        line-height: 1.55;
        white-space: pre-wrap;
        font-family: 'Sarabun', sans-serif;
        box-shadow: 0 0 16px rgba(45, 120, 210, 0.12);
    }

    label[data-testid="stWidgetLabel"] {
        color: #a8d4f5 !important;
        font-weight: 600 !important;
        font-size: 0.78rem !important;
        margin-bottom: 2px !important;
    }

    .stSelectbox > div > div,
    .stNumberInput > div > div > input,
    .stTextInput > div > div > input {
        background: rgba(255,255,255,0.07) !important;
        border: 1px solid rgba(255,255,255,0.15) !important;
        color: #e8f4fd !important;
        border-radius: 8px !important;
        min-height: 2.1rem !important;
        font-size: 0.86rem !important;
    }

    div[data-baseweb="select"] > div {
        min-height: 2.1rem !important;
    }

    input {
        padding-top: 0.3rem !important;
        padding-bottom: 0.3rem !important;
    }

    .stCheckbox {
        margin-top: -4px !important;
        margin-bottom: -4px !important;
    }

    .stCheckbox > label {
        color: #c8dff0 !important;
        font-size: 0.84rem !important;
    }

    div[data-testid="stExpander"] {
        border: 1px solid rgba(255,255,255,0.12) !important;
        border-radius: 8px !important;
        background: rgba(255,255,255,0.03) !important;
    }

    hr {
        margin-top: 0.4rem !important;
        margin-bottom: 0.4rem !important;
        border-color: rgba(255,255,255,0.1) !important;
    }
</style>
""", unsafe_allow_html=True)

# Date Calculation
today_th = datetime.utcnow() + timedelta(hours=7)

def thai_date(dt):
    return dt.strftime(f"%d/%m/{dt.year + 543}")

today_str = thai_date(today_th)

# Header placeholder
header_placeholder = st.empty()

# Main Form
st.markdown('<div class="section-card"><div class="section-title">ข้อมูลหลัก</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1.25, 0.9, 1.1])

with col1:
    session = st.selectbox(
        "Session",
        options=["ก่อนปิดตลาด", "เปิดตลาด"],
        index=0
    )

# Session Date Logic
if session == "เปิดตลาด":
    session_date = today_th
else:
    session_date = today_th - timedelta(days=1)

session_date_str = thai_date(session_date)

# Header
header_placeholder.markdown(f"""
<div class="header-box">
    <h1>ฟอร์มแจ้ง Call Margin</h1>
    <div class="date-badge">
        Session: <strong>{session_date_str}</strong>
        &nbsp;|&nbsp;
        วันนี้: {today_str}
    </div>
</div>
""", unsafe_allow_html=True)

with col2:
    currency = st.selectbox(
        "สกุลเงิน",
        options=["USD", "THB", "EUR"],
        index=0
    )

with col3:
    amount = st.number_input(
        "จำนวนเงิน",
        min_value=0.0,
        value=1500.0,
        step=100.0,
        format="%.0f"
    )

st.markdown('<div style="height:4px;"></div>', unsafe_allow_html=True)

col_t1, col_t2, col_t3, col_space = st.columns([0.55, 0.65, 0.65, 3])

with col_t1:
    t = st.checkbox("T", value=True)

with col_t2:
    t1 = st.checkbox("T+1", value=False)

with col_t3:
    t2 = st.checkbox("T+2", value=False)

st.markdown('</div>', unsafe_allow_html=True)

# Advisory Fields
st.markdown('<div class="section-card"><div class="section-title">คำแนะนำและหมายเหตุ</div>', unsafe_allow_html=True)

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

# Generate Message
t_labels = []

if t:
    t_labels.append("T")
if t1:
    t_labels.append("T+1")
if t2:
    t_labels.append("T+2")

t_str = f" เป็นช่วงเวลา {' / '.join(t_labels)}" if t_labels else ""
amount_fmt = f"{int(amount):,}"

message = (
    f"สวัสดีครับ ขอแจ้ง Call Margin สำหรับช่วง Trading Session {session}"
    f"ของวันที่ {session_date_str}\n"
    f"โดยมี Call Margin อยู่ที่ประมาณ {currency} {amount_fmt}{t_str}\n"
    f"{advice}ครับ"
)

if remark.strip():
    message += f"\n\nหมายเหตุ: {remark.strip()}"

safe_message_html = html.escape(message)
message_json = json.dumps(message, ensure_ascii=False)

# Output
st.markdown('<div class="output-label">ข้อความที่จะส่ง</div>', unsafe_allow_html=True)

st.markdown(
    f'<div class="output-box">{safe_message_html}</div>',
    unsafe_allow_html=True
)

# Copy Button
components.html(f"""
<button id="copyBtn" style="
    background: linear-gradient(135deg, #1e6fbf, #2a8cde);
    color: white;
    border: none;
    padding: 8px 18px;
    border-radius: 8px;
    cursor: pointer;
    font-family: Sarabun, sans-serif;
    font-size: 14px;
    font-weight: 600;
    width: 100%;
    height: 38px;
">
คัดลอกข้อความ
</button>

<script>
const textToCopy = {message_json};

document.getElementById("copyBtn").addEventListener("click", async function() {{
    const btn = this;

    try {{
        await navigator.clipboard.writeText(textToCopy);
        btn.innerText = "คัดลอกแล้ว";
        setTimeout(() => {{
            btn.innerText = "คัดลอกข้อความ";
        }}, 2000);
    }} catch (err) {{
        const textarea = document.createElement("textarea");
        textarea.value = textToCopy;
        textarea.style.position = "fixed";
        textarea.style.left = "-9999px";
        textarea.style.top = "-9999px";
        document.body.appendChild(textarea);
        textarea.focus();
        textarea.select();

        try {{
            document.execCommand("copy");
            btn.innerText = "คัดลอกแล้ว";
        }} catch (e) {{
            btn.innerText = "กด Ctrl+C เพื่อคัดลอก";
        }}

        document.body.removeChild(textarea);

        setTimeout(() => {{
            btn.innerText = "คัดลอกข้อความ";
        }}, 2000);
    }}
}});
</script>
""", height=48)

with st.expander("คัดลอกแบบ manual"):
    st.text_area(
        "",
        value=message,
        height=100,
        label_visibility="collapsed"
    )
