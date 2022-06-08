
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
    st.header("test html import")
    
    HtmlFile = open("ttestt_world_price_info_0608.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    print(source_code)
    components.html(source_code, width = 850 , height = 650)
    
elif cate == '날씨':
    st.header("test html import")
    
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

## Load data
# from sklearn.datasets import load_iris
# iris = load_iris()
# iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)
# iris_df['target'] = iris['target']
# iris_df['target'] = iris_df['target'].apply(lambda x: 'setosa' if x == 0 else ('versicolor' if x == 1 else 'virginica'))

# ## Return table/dataframe
# # table
# st.table(iris_df.head())

# # dataframe
# st.dataframe(iris_df)
# st.write(iris_df)


## Select Box
# occupation = st.selectbox("직군을 선택하세요.",
#                           ["Backend Developer",
#                            "Frontend Developer",
#                            "ML Engineer",
#                            "Data Engineer",
#                            "Database Administrator",
#                            "Data Scientist",
#                            "Data Analyst",
#                            "Security Engineer"])
# st.write("당신의 직군은 ", occupation, " 입니다.")


