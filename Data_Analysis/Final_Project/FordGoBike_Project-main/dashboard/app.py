import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# 1. إعداد شكل الصفحة
st.set_page_config(page_title="Bike Share Dashboard", layout="wide")
st.title("📊 لوحة تحكم بيانات الدراجات")

# 2. قراءة الداتا (تأكد إن ملف الـ CSV في نفس الفولدر أو حط المسار بتاعه)
@st.cache_data # دي بتسرع تحميل الداتا
def load_data():
    # استبدل المسار ده بمسار الداتا النضيفة بتاعتك لو مختلف
    return pd.read_csv('cleaned_bike_data.csv') 

data = load_data()

# 3. إنشاء الفلتر (القائمة المنسدلة) في الشريط الجانبي (Sidebar)
st.sidebar.header("خيارات الفلترة")
gender_filter = st.sidebar.selectbox(
    "اختر الجنس (Gender):",
    ['All', 'Male', 'Female', 'Other']
)

# 4. فلترة الداتا بناءً على اختيار المستخدم
if gender_filter == 'Male':
    filtered_data = data[data['member_gender_Male'] == 1]
elif gender_filter == 'Female':
    filtered_data = data[data['member_gender_Female'] == 1]
elif gender_filter == 'Other':
    filtered_data = data[data['member_gender_Other'] == 1]
else:
    filtered_data = data

# 5. رسم المخططات لو في بيانات
if len(filtered_data) > 0:
    fig = make_subplots(rows=1, cols=2,
                        specs=[[{"type": "domain"}, {"type": "xy"}]],
                        subplot_titles=('توزيع أنواع المستخدمين', 'متوسط مدة الرحلة بالثواني'))

    label_map = {1: 'Subscriber', 0: 'Customer'}

    # الرسمة الأولى: الدائرة
    user_counts = filtered_data['user_type_Subscriber'].value_counts().reset_index()
    user_counts.columns = ['user_type_Subscriber', 'count']
    labels = user_counts['user_type_Subscriber'].map(label_map)

    fig.add_trace(
        go.Pie(labels=labels, values=user_counts['count'], marker_colors=['#636EFA', '#EF553B'], hole=0.3),
        row=1, col=1
    )

    # الرسمة التانية: الأعمدة
    avg_duration = filtered_data.groupby('user_type_Subscriber')['duration_sec'].mean().reset_index()
    avg_duration['label'] = avg_duration['user_type_Subscriber'].map(label_map)

    fig.add_trace(
        go.Bar(x=avg_duration['label'], y=avg_duration['duration_sec'], marker_color=['#636EFA', '#EF553B']),
        row=1, col=2
    )

    fig.update_layout(height=500, showlegend=False)

    # 6. عرض الرسمة في صفحة الويب
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("لا توجد بيانات مطابقة لهذا الاختيار.")