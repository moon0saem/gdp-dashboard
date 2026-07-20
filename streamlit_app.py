import streamlit as st

st.set_page_config(
    page_title="About Me",
    page_icon=":wave:",
    layout="wide",
)

st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(135deg, #f8fbff 0%, #eef5ff 100%);
    }
    .hero {
        background: linear-gradient(90deg, #f9c2d1 0%, #f7a8c3 100%);
        padding: 2rem 2rem;
        border-radius: 1rem;
        color: #5a2340;
        box-shadow: 0 8px 25px rgba(247, 168, 195, 0.28);
        margin-bottom: 1.2rem;
    }
    .hero h1 {
        margin-bottom: 0.3rem;
        font-size: 2rem;
    }
    .card {
        background: white;
        padding: 1rem 1.2rem;
        border-radius: 0.9rem;
        box-shadow: 0 6px 18px rgba(15, 23, 42, 0.08);
        border: 1px solid #e2e8f0;
        margin-bottom: 1rem;
    }
    .small-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #1e3a8a;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
        <h1>안녕하세요, 저는 최문영입니다</h1>
        <p>중학교 과학을 가르치며, 아이들의 성장을 지원합니다.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2 = st.columns([1.2, 0.8], gap="large")

with col1:
    st.markdown(
        """
        <div class="card">
            <div class="small-title">소개</div>
            <div style="display:flex; align-items:center; gap:1rem; margin-top:0.7rem;">
                <div style="width:90px; height:90px; border-radius:50%; background:linear-gradient(135deg, #ffd6e7 0%, #f9a8d4 100%); display:flex; align-items:center; justify-content:center; font-size:2.2rem;">📷</div>
                <div>
                    <p style="margin:0;">저는 학생들이 스스로 생각하고 배우는 즐거움을 느끼도록 돕는 것을 중요하게 생각합니다.</p>
                    <ul style="margin:0.3rem 0 0 1rem;">
                        <li>이름: 최문영</li>
                        <li>직업: 중학교 과학 교사</li>
                        <li>취미: 사진 촬영, 베이킹, 산책</li>
                    </ul>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="card">
            <div class="small-title">관심 분야</div>
            <p>다음 주제들에 관심이 많습니다.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.checkbox("과학 교육", value=True)
    st.checkbox("식물 재배", value=True)
    st.checkbox("사진 촬영", value=True)
    st.button("저에 대해 더 알아보기")
    st.markdown("</div></div>", unsafe_allow_html=True)

st.divider()

st.markdown(
    """
    <div class="card">
        <div class="small-title">연락처</div>
    </div>
    """,
    unsafe_allow_html=True,
)

tabs = st.tabs(["이메일", "전화번호"])

with tabs[0]:
    st.write("12345678@gmail.com")

with tabs[1]:
    st.write("010-1234-5678")
