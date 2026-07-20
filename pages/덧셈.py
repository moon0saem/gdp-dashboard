from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st

font_path = Path(__file__).resolve().parents[1] / "fonts" / "NotoSansKR-Regular.ttf"
font_path_str = str(font_path)

if font_path.exists():
    font_manager = matplotlib.font_manager
    font_manager.fontManager.addfont(font_path_str)
    plt.rcParams["font.family"] = "Noto Sans KR"
    plt.rcParams["axes.unicode_minus"] = False
    sns.set_theme(font="Noto Sans KR")
else:
    st.warning("폰트 파일을 찾을 수 없습니다. fonts 폴더를 확인해 주세요.")

st.set_page_config(page_title="데이터 시각화 비교", page_icon="📊", layout="wide")

st.title("데이터 시각화 예시 비교")
st.markdown("아래 예시는 matplotlib, seaborn, plotly로 같은 데이터를 시각화한 비교 예시입니다.")

sample_df = pd.DataFrame(
    {
        "월": ["1월", "2월", "3월", "4월", "5월", "6월"],
        "매출": [120, 150, 170, 140, 200, 230],
        "방문자": [80, 95, 110, 100, 130, 150],
    }
)

st.subheader("1. matplotlib로 그린 선 그래프")
st.caption("기본적인 선 그래프 스타일로 월별 매출 변화를 보여줍니다.")
fig_matplotlib, ax = plt.subplots(figsize=(7, 3.5))
ax.plot(sample_df["월"], sample_df["매출"], marker="o", color="#4c78a8", linewidth=2)
ax.set_title("월별 매출 추이 (matplotlib)")
ax.set_xlabel("월")
ax.set_ylabel("매출")
ax.grid(True, alpha=0.3)
plt.xticks(rotation=0)
plt.tight_layout()
st.pyplot(fig_matplotlib)

st.subheader("2. seaborn으로 그린 막대 그래프")
st.caption("seaborn은 통계적 느낌이 나는 그래프를 빠르게 만들기 좋습니다.")
fig_seaborn, ax2 = plt.subplots(figsize=(7, 3.5))
sns.barplot(data=sample_df, x="월", y="방문자", palette="pastel", ax=ax2)
ax2.set_title("월별 방문자 수 (seaborn)")
ax2.set_xlabel("월")
ax2.set_ylabel("방문자")
ax2.grid(axis="y", alpha=0.3)
plt.tight_layout()
st.pyplot(fig_seaborn)

st.subheader("3. plotly로 그린 인터랙티브 그래프")
st.caption("plotly는 마우스로 확대, 이동, 툴팁 확인이 가능한 대화형 그래프입니다.")
fig_plotly = px.line(
    sample_df,
    x="월",
    y="매출",
    title="월별 매출 추이 (plotly)",
    labels={"월": "월", "매출": "매출"},
)
fig_plotly.update_traces(line=dict(color="#f58518", width=3), marker=dict(size=8))
st.plotly_chart(fig_plotly, use_container_width=True)

st.markdown("### 라이브러리 비교 요약")
st.info("- matplotlib: 정적 그래프와 세밀한 커스터마이징에 적합합니다.\n- seaborn: 통계 분석 스타일의 그래프를 빠르게 그리기 좋습니다.\n- plotly: 웹에서 상호작용이 가능한 대화형 시각화에 적합합니다.")
