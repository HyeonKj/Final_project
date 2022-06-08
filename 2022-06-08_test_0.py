
# ## Title
# st.title('Streamlit Tutorial')
# ## Header/Subheader
# st.header("This is header")
# st.subheader("This is subheader")
# ## Text
# st.text("Hello Streamlit! 이 글은 튜토리얼 입니다.")

import streamlit as st
import streamlit.components.v1 as components

# >>> import plotly.express as px
# >>> fig = px.box(range(10))
# >>> fig.write_html('test.html')

## Sidebars
st.sidebar.header("사이드바 메뉴")
cate = st.sidebar.selectbox("메뉴를 선택하세요.", ["물가", "날씨"])
if cate == '물가':

    st.header("지도에서 원하시는 국가를 선택하세요 ")
    
    HtmlFile = open("ttestt_world_price_info_0608.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code, width = 850 , height = 650)
    
elif cate == '날씨':

    st.header("선택한 국가의 주간 일기예보")
    
    HtmlFile = open("./weekly_weather/가나 주간 일기예보.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code, width = 1100 , height = 650)
    
    #  ## Markdown syntax
    # st.markdown("# This is a Markdown title")
    # st.markdown("## This is a Markdown header")
    # st.markdown("### This is a Markdown subheader")
    # st.markdown("- item 1\n"
    #             "   - item 1.1\n"
    #             "   - item 1.2\n"
    #             "- item 2\n"
    #             "- item 3")
    # st.markdown("1. item 1\n"
    #             "   1. item 1.1\n"
    #             "   2. item 1.2\n"
    #             "2. item 2\n"
    #             "3. item 3")



# Select Box
occupation = st.selectbox("직군을 선택하세요.",
                          ["그리스",
                           "호주",
                           "괌",
                           "홍콩",])

if occupation == '괌':

    st.write("선택한 도시 명 : ", occupation, "의 월 평균 기온에 대해 안내드립니다.")
    
    HtmlFile = open("./monthly_weather/괌 괌_월평균기온.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code, width = 900 , height = 650)

else:
    st.write("선택한 도시 명 : ", occupation, "의 월 평균 기온은 아직 업데이트 중입니다. 빠른 시일 업데이트하도록 하겠습니다.")


