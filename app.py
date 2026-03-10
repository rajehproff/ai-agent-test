import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. تحميل الإعدادات والمفتاح السري
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# إعداد الصفحة (تظهر في تبويب المتصفح)
st.set_page_config(page_title="عربي | Arabii", page_icon="🌙", layout="centered")

# 2. تنسيق الواجهة بألوان فخمة (CSS)
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stTextInput > div > div > input {
        background-color: #262730;
        color: gold;
        border-color: #4b4b4b;
    }
    h1 {
        color: #D4AF37; /* اللون الذهبي الملكي */
        text-align: center;
        font-family: 'Arial';
    }
    .welcome-msg {
        text-align: center;
        color: #cccccc;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. محتوى الصفحة
st.markdown("<h1>عربي - ARABII</h1>", unsafe_allow_html=True)
st.markdown("<p class='welcome-msg'>أهلاً بك في المساعد الإبداعي لبراند عربي. استلهم تصاميمك من روح التراث والشعر.</p>", unsafe_allow_html=True)

# التأكد من وجود المفتاح قبل تشغيل الذكاء الاصطناعي
if not API_KEY:
    st.error("خطأ: لم يتم العثور على مفتاح API. تأكد من ضبط ملف .env")
else:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-2.5-flash')

    # خانة الإدخال
    user_input = st.text_input("عن ماذا تبحث اليوم؟ (شخصية تاريخية، بيت شعر، فكرة تصميم)", placeholder="مثلاً: المتنبي، الأندلس، صقر قريش...")

    if st.button('ابتكر الآن'):
        if user_input.strip() == "":
            st.warning("من فضلك اكتب شيئاً أولاً.")
        else:
            with st.spinner('جاري استحضار الإلهام...'):
                try:
                    prompt = f"أنت مستشار إبداعي لبراند ملابس ستريت وير (Streetwear) اسمه 'عربي'. قدم أفكاراً لتصاميم تيشرتات مستوحاة من: {user_input}. ركز على دمج الخط العربي والشعر بأسلوب عصري."
                    response = model.generate_content(prompt)
                    
                    st.success("إليك بعض الأفكار المقترحة:")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"حدث خطأ: {e}")

# تذييل الصفحة
st.markdown("---")
st.caption("براند عربي | فخر الهوية بلمسة عصرية")