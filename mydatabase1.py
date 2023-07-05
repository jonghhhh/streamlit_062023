import streamlit as st
import pandas as pd

data = pd.read_csv("전국관광지정보표준데이터.csv", encoding='cp949')  # 검색할 데이터 파일의 경로를 적절히 수정하세요.

def main():
    st.title("전국 관광지 정보 검색")
    st.write("검색 원하는 키워드를 입력해 관련된 관광 정보를 모두 열람하세요")
    query = st.text_input("검색어:")

    result = []
    for i, d in enumerate(data['관광지소개']):
        if query in d:
            result.append(i)
        else:
            pass

    filtered_data = data[data.index.isin(result)]

    if len(filtered_data) > 0:
        st.write("데이터 일부")
        st.dataframe(filtered_data)
    else:
        st.write("검색어에 부합하는 내용이 없습니다")

if __name__ == "__main__":
    main()

