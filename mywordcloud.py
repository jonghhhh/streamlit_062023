import streamlit as st

import re 
from kiwipiepy import Kiwi
kiwi = Kiwi()

from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def kiwi_tokenize(txt, nouns=True, remove1=False, stopwords=[]):
    '''문자열 txt를 받아 kiwi로 형태소 추출: nouns=명사만 추출 여부, remove1=1음절 토큰 제외 여부, stopwords=불용어 리스트 '''
    try:
        # 정제(cleaning): 비문자숫자 등 노이즈 제거
        txt1=re.sub(r"[^\s가-힣a-zA-Z0-9]", " ", txt)   # re.sub: 문자열 부분 교체. r은 정규표현식 사용한다는 표시. 
                                                        # "[^ 가-힣a-zA-Z1-9]"는 한글 영어 숫자 이외의 문자열 의미. 
                                                        # txt1=txt1.replace("X", " "):  특정 단어만 삭제할 때에는 replace 함수로 간단히 실행
        # 토큰화(tokenization): 형태소 추출
        morphs=kiwi.tokenize(txt1)
        morphs_all=[m[0] for m in morphs]                # 모든 품사에 해당하는 형태소 모두 추출
        morphs_select=['NNG', 'NNP', 'NP', 'NR', 'VV', 'VX', 'VCP', 'VCN', 'VA','VA-I', 'MM', 'MAG']  # 일반명사, 고유명사, 용언(동사, 형용사 등), 관형사, 일반부사 # 품사 분류표 참조
        # 명사 추출(nou extraction) 여부 선택
        if nouns==True:                                 
            token_lst=[m[0] for m in morphs if m[1] in morphs_select[:4]]  
        else:             
            token_lst=[m for m in morphs if m[1] in morphs_select]     
            # stemming(어간 추출, 동사-형용사 등 용언의 원형 복구) 적용    
            token_lst=[m[0]+'다' if m[1].startswith('V') else m[0] for m in token_lst]  
        # 1음절 토큰 제외 여부 선택
        if remove1==True:                                 
            token_lst=[t for t in token_lst if len(t)>1 ]
        else: 
            pass
        # 불용어(stopwords) 적용: 제외해야 할 토큰들의 집합    
        token_lst=[t for t in token_lst if t not in stopwords]   
    except: 
        token_lst=[] 
    return token_lst

def generate_wordcloud(text):
    token_list=kiwi_tokenize(text, nouns=True, remove1=True, stopwords=[])
    keywords_all=Counter(token_list).most_common(100)

    mywordcloud = WordCloud(
        font_path = 'NanumGothic-Regular.ttf',       # 폰트 저장 경로
        background_color='white',                                                       
        colormap = "Accent_r",                                                         # 사용 색상 지정  # https://matplotlib.org/stable/tutorials/colors/colormaps.html
        width=1500, height=1000                                                        # 그림 픽셀
        ).generate_from_frequencies(dict(keywords_all)) 
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12, 8))    
    plt.imshow(mywordcloud, interpolation='bilinear') 
    plt.axis('off') 
    st.pyplot(fig)

def main():
    st.title("워드클라우드(Word Cloud) 만들기")
    st.write("가공할 텍스트를 입력하세요:")
    text_input = st.text_area("텍스트", "")
    
    if st.button("워드클라우드 시작"):
        if text_input:
            generate_wordcloud(text_input)
        else:
            st.warning("Please enter some text.")


if __name__ == "__main__":
    main()
