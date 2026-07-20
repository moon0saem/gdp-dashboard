import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Streamlit Examples",
    page_icon=":sparkles:",
    layout="wide",
)

st.title("✨ Streamlit 요소 예시 페이지")
st.caption("이 페이지는 다양한 Streamlit 위젯과 레이아웃을 한 번에 보여주기 위해 구성한 예시입니다.")

st.markdown("""
이 예제에서는 제목, 사이드바, 탭, 메트릭, 차트, 데이터프레임, 업로드, 다운로드, 진행 상태 표시 등
여러 가지 Streamlit 요소를 함께 확인할 수 있습니다.
""")

with st.sidebar:
    st.header("사이드바 컨트롤")
    theme = st.selectbox("테마를 선택하세요", ["Light", "Dark", "Auto"])
    view_mode = st.radio("표시 모드를 선택하세요", ["요약", "상세", "전체"])
    show_help = st.checkbox("도움말 표시", value=True)
    st.slider("범위를 조정하세요", 0, 100, (25, 75))

    st.divider()
    st.text_input("이름을 입력해 주세요", placeholder="홍길동")

st.subheader("1. 기본 텍스트와 레이아웃")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("조회수", "12,430", "+12.3%")
with col2:
    st.metric("활성 사용자", "1,204", "-2.1%")
with col3:
    st.metric("완료율", "87%", "+4.0%")

st.info("정보 박스를 사용하면 중요한 메시지를 강조할 수 있습니다.")

st.subheader("2. 위젯 예시")

with st.form("example_form"):
    name = st.text_input("이름", value="Streamlit")
    description = st.text_area("한 줄 설명", "여러 요소를 테스트하는 예시 페이지입니다.")
    age = st.number_input("나이", min_value=0, max_value=120, value=25)
    selected_date = st.date_input("날짜 선택")
    selected_time = st.time_input("시간 선택")
    submitted = st.form_submit_button("제출")

if submitted:
    st.success(f"{name}님, 제출이 완료되었습니다. 선택한 날짜는 {selected_date}이고 시간은 {selected_time}입니다.")

st.subheader("3. 탭과 확장 패널")

tab1, tab2, tab3 = st.tabs(["요약", "데이터", "추가 기능"])

with tab1:
    st.write("탭을 사용하면 관련 내용을 묶어서 보여줄 수 있습니다.")
    st.progress(70)
    with st.expander("더 보기"):
        st.write("확장 패널 안에 추가 설명이나 힌트를 넣을 수 있습니다.")

with tab2:
    sample_df = pd.DataFrame(
        {
            "카테고리": ["A", "B", "C", "D"],
            "값": [10, 25, 15, 30],
            "비율": [0.2, 0.5, 0.3, 0.6],
        }
    )
    st.dataframe(sample_df, use_container_width=True)

with tab3:
    uploaded_file = st.file_uploader("CSV 파일을 업로드해 보세요", type=["csv"])
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        st.download_button(
            label="업로드된 파일 다운로드",
            data=bytes_data,
            file_name=uploaded_file.name,
            mime="text/csv",
        )
    else:
        st.caption("업로드된 파일이 없으면 이 영역은 비어 있습니다.")

st.subheader("4. 차트와 코드")

chart_data = pd.DataFrame(
    {
        "월": ["1월", "2월", "3월", "4월", "5월", "6월"],
        "판매량": [20, 35, 30, 45, 50, 60],
    }
)

st.line_chart(chart_data.set_index("월"))

st.code(
    "import streamlit as st\n\nst.title('Hello, Streamlit!')",
    language="python",
)

st.subheader("5. 상태 표시")

if st.button("상태 표시 실행"):
    with st.spinner("잠시만 기다려 주세요..."):
        st.balloons()
    st.toast("작업이 완료되었습니다.", icon="🎉")
