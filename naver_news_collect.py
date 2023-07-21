import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from urllib import parse

def naver_news_search(query, date_from, date_to, to_page):
    query = parse.quote(query)
    target_url = "https://search.naver.com/search.naver?where=news&query={}&sort=0&photo=0&field=0&nso=so:r,p:from{}to{},a:all&start=1".format(query, date_from, date_to) # sort=0: 관련도순, 2: 오래된순
    ## 페이지URL 수집
    page_former = target_url[:-1]
    page_num = []
    p=1
    while p <= to_page*10-9:
        page_num.append(p)
        p += 10
    page_urls = []
    for i in page_num:
        page_url = page_former + str(i)
        page_urls.append(page_url)

    ## 복수 페이지를 돌면서 기사 수집
    stories_all=[]
    progress_bar = st.progress(0,  text='100페이지까지 수집 진도 표시')
    for i, page_url in enumerate(page_urls): 
        try:
            r=requests.get(page_url)
            soup=BeautifulSoup(r.text, "html.parser")
            time.sleep(0.5)                   # 0.5초 쉬었다 다음 실행

            stories_1page=soup.select("div.news_area")

            stories=[]
            for s in stories_1page:
                try:
                    title=s.select("a.news_tit")[0]["title"].strip()
                    url=s.select("a.news_tit")[0]["href"]
                    n_url=s.select("a.info")[-1]["href"]
                    source=s.select("a.info.press")[0].text.replace("선정", "").replace("언론사", "").strip()
                    date=s.select("span.info")[-1].text
                    text=s.select("a.api_txt_lines.dsc_txt_wrap")[0].text.strip()
                    story=[source, title, date, url, n_url, text]
                except:
                    story=[""]*6
                stories.append(story)
        except:
            pass
        stories_all.append(stories)
        progress_bar.progress(i + 1,  text='100페이지까지 수집 진도 표시')
    result=sum(stories_all,[])
    results=pd.DataFrame(result, columns=['source', 'title', 'date', 'url', 'n_url', 'text'])
    results['n_url']=results['n_url'].apply(lambda x: x if 'naver' in x else None)
    return results

def main():
    st.title("네이버 뉴스 검색(관련도 순)")
    query = st.text_input("검색어 입력:").strip()
    date_from = st.text_input("검색시작일 입력(20230101 형태로):").strip()
    date_to = st.text_input("검색마지막일 입력(20230101 형태로):").strip()
    to_page = int(float(st.number_input("몇 페이지까지(100페이지까지 가능):", min_value=0, max_value=100, step=1)))
    save_path = st.text_input("검색 결과 저장 경로(C://Users/user/Desktop/result.xlsx 방식):").strip()
    if st.button("뉴스 검색 시작"):
        result_file=naver_news_search(query, date_from, date_to, to_page)
        st.dataframe(result_file)
        result_file.to_excel(save_path, index=False)
        st.success("저장 성공: "+save_path+ " 확인")

if __name__ == "__main__":
    main()
