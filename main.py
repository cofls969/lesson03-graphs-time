import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 기본 설정
st.set_page_config(page_title="영화 데이터 그래프 도감 1 - 시간", layout="wide")

# 메인 제목
st.title("🎬 영화 데이터 그래프 도감 1 - 시간")
st.write("시간의 흐름에 따른 영화 박스오피스 데이터를 탐색합니다.")
st.divider()

# 데이터 불러오기 및 전처리 (캐싱을 통해 속도 향상)
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_daily.csv"
    df = pd.read_csv(url)
    
    # '날짜' 열이 8자리 숫자(예: 20230101)로 되어 있으므로 datetime 형식으로 변환
    df['날짜'] = pd.to_datetime(df['날짜'].astype(str), format='%Y%m%d')
    
    return df

# 데이터 로드
df = load_data()

# ==========================================
# 구역 1: 영화별 일일 관객수 변화
# ==========================================
st.header("1. 영화별 일일 관객수 변화")

# 영화 선택 드롭다운 (고유한 영화명 추출)
movie_list = df['영화명'].unique()
selected_movie = st.selectbox("그래프를 확인할 영화를 선택하세요:", movie_list)

# 선택한 영화 데이터 필터링 및 날짜순 정렬
filtered_df = df[df['영화명'] == selected_movie].sort_values(by='날짜')

# Plotly 선 그래프 생성
fig1 = px.line(
    filtered_df, 
    x='날짜', 
    y='일관객', 
    markers=True,
    title=f"'{selected_movie}' 일일 관객수 추이"
)

# 마우스 오버 시 보이는 정보(툴팁) 커스텀 설정
fig1.update_traces(
    hovertemplate="<b>날짜:</b> %{x|%Y년 %m월 %d일}<br><b>일관객:</b> %{y:,.0f}명<extra></extra>"
)

# 그래프 화면에 출력
st.plotly_chart(fig1, use_container_width=True)

# 그래프로 알 수 있는 것 문구 자리
st.info("💡 **이 그래프로 알 수 있는 것:** (이곳에 개봉 후 관객수 증감 패턴, 주말/평일 차이 등 분석 내용을 적어주세요.)")

st.divider()

# ==========================================
# 구역 2: 다음 그래프를 위한 자리
# ==========================================
st.header("2. (새로운 그래프 제목을 입력하세요)")
st.write("이곳에 다음 데이터 시각화 그래프를 추가할 수 있습니다.")

# 임시 빈 공간 (추후 코드로 대체)
st.text("그래프가 들어갈 자리입니다.")

# 그래프로 알 수 있는 것 문구 자리
st.info("💡 **이 그래프로 알 수 있는 것:** (여기에 분석 내용을 적어주세요.)")

st.divider()

# ==========================================
# 구역 3: 다음 그래프를 위한 자리
# ==========================================
st.header("3. (새로운 그래프 제목을 입력하세요)")
st.write("구역을 계속 복사해서 늘려갈 수 있습니다.")

st.info("💡 **이 그래프로 알 수 있는 것:** (여기에 분석 내용을 적어주세요.)")
