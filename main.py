import streamlit as st
import pandas as pd
import plotly.express as px

# 1. 앱 기본 설정
st.set_page_config(page_title="영화 데이터 그래프 도감 1 - 시간", layout="wide")
st.title("영화 데이터 그래프 도감 1 - 시간")

# 2. 데이터 불러오기 및 전처리
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_daily.csv"
    df = pd.read_csv(url)
    
    # 날짜(예: 20230101)를 문자열로 바꾼 뒤 datetime 형식으로 변환
    df['날짜'] = pd.to_datetime(df['날짜'].astype(str), format='%Y%m%d')
    return df

df = load_data()

# ==========================================
# 구역 1: 단일 영화 일별 관객수 변화
# ==========================================
st.markdown("---")
st.header("1. 단일 영화 일관객 변화")

# 드롭다운으로 영화 선택
movie_list = df['영화명'].unique()
selected_movie = st.selectbox("영화를 선택하세요:", movie_list)

# 선택한 영화 데이터만 필터링
filtered_df = df[df['영화명'] == selected_movie]

# 플롯리 선 그래프 생성
fig1 = px.line(
    filtered_df, 
    x='날짜', 
    y='일관객', 
    title=f"'{selected_movie}' 일별 관객수 추이"
)

# 마우스 오버 시 표시될 정보 설정
fig1.update_traces(hovertemplate='날짜: %{x}<br>일관객: %{y:,}명<extra></extra>')
st.plotly_chart(fig1, use_container_width=True)

# 인사이트 문구 자리
st.info("💡 이 그래프로 알 수 있는 것: (여기에 한 문장 설명을 추가하세요)")


# ==========================================
# 구역 2: Top 5 영화 관객수 추이 비교
# ==========================================
st.markdown("---")
st.header("2. 기간 내 총 관객수 Top 5 영화 비교")

# 전체 기간 일관객 합계 기준 상위 5개 영화 이름 추출
top5_movies = df.groupby('영화명')['일관객'].sum().nlargest(5).index

# 상위 5개 영화의 데이터만 필터링
top5_df = df[df['영화명'].isin(top5_movies)]

# 플롯리 다중 선 그래프 생성 (color='영화명'으로 색상 구분)
fig2 = px.line(
    top5_df, 
    x='날짜', 
    y='일관객', 
    color='영화명',
    title="상위 5편의 일별 관객수 비교"
)

# 마우스 오버 시 표시될 정보 설정
fig2.update_traces(hovertemplate='날짜: %{x}<br>일관객: %{y:,}명<extra></extra>')
st.plotly_chart(fig2, use_container_width=True)

# 인사이트 문구 자리
st.info("💡 이 그래프로 알 수 있는 것: (여기에 한 문장 설명을 추가하세요)")


# ==========================================
# 구역 3: 일별 10위권 관객수 합계 (새로 추가된 부분)
# ==========================================
st.markdown("---")
st.header("3. 일별 전체(10위권) 관객수 합계")

# 날짜별 일관객 합계 계산
daily_sum_df = df.groupby('날짜')['일관객'].sum().reset_index()

# 플롯리 영역 그래프 생성
fig3 = px.area(
    daily_sum_df,
    x='날짜',
    y='일관객',
    title="일별 10위권 관객수 합계 추이 (영역 그래프)"
)

# 관객수 합계가 가장 컸던 날 3일 추출
top3_days = daily_sum_df.nlargest(3, '일관객')

# 그래프 위에 Top 3 날짜 표시 (주석 추가)
for index, row in top3_days.iterrows():
    date_str = row['날짜'].strftime('%Y-%m-%d')
    fig3.add_annotation(
        x=row['날짜'],
        y=row['일관객'],
        text=f"{date_str}",
        showarrow=True,
        arrowhead=1,
        ax=0,       # x축 방향 화살표 길이
        ay=-40,     # y축 방향 화살표 길이 (위로 띄움)
        font=dict(size=12, color="red")
    )

# 마우스 오버 시 표시될 정보 설정
fig3.update_traces(hovertemplate='날짜: %{x}<br>총 관객수: %{y:,}명<extra></extra>')
st.plotly_chart(fig3, use_container_width=True)

# 인사이트 문구 자리
st.info("💡 이 그래프로 알 수 있는 것: (여기에 한 문장 설명을 추가하세요)")


# ==========================================
# 구역 4: 향후 추가될 그래프를 위한 예비 구역
# ==========================================
st.markdown("---")
st.header("4. (다음 그래프가 들어갈 자리)")
st.write("새로운 그래프 아이디어가 있다면 여기에 추가됩니다.")
