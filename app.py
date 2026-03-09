import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. فتح الخزنة وقراءة المفتاح
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# 2. التأكد من وجود المفتاح وتجهيز جوجل
if not API_KEY:
    st.error('يرجى التأكد من إضافة GOOGLE_API_KEY في ملف .env')
else:
    genai.configure(api_key=API_KEY)

    # 3. تصميم واجهة الصفحة
    st.title('المساعد الإبداعي لتصميمات الملابس والمحتوى')
    user_input = st.text_input('اكتب اسم شخصية تاريخية أو بيت شعر عربي:')

    # 4. لما تدوس على الزرار
    if st.button('ابتكر أفكار'):
        if user_input.strip() == "":
            st.warning("من فضلك اكتب نص للابتكار.")
        else:
            with st.spinner('...جاري معالجة الأفكار'):
                try:
                    # الاتصال بأحدث وأسرع نسخة
                    model = genai.GenerativeModel('gemini-2.5-flash')
                    
                    # الطلب المخصص للذكاء الاصطناعي
                    prompt = f"بناءً على هذا النص '{user_input}'، اقترح فكرة مبتكرة لتصميم تيشيرت أو هودي (Streetwear) يدمج الخط العربي والتاريخ، واكتب سكريبت قصير جداً لفيديو تسويقي يحكي القصة وراء هذا التصميم لجذب الانتباه."
                    
                    response = model.generate_content(prompt)
                    
                    # عرض النتيجة
                    st.success("تم الابتكار بنجاح!")
                    st.write(response.text)
                    
                except Exception as e:
                    # لو حصل أي خطأ هيقولنا سببه إيه بالظبط
                    st.error(f"حدث خطأ أثناء الاتصال: {e}")