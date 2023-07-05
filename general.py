import streamlit as st
from PIL import Image
import requests
from io import BytesIO

Navigation = {"page_title":"Streamlitweb.io","page_icon":":smiley:","layout":"centered"}
st.set_page_config(**Navigation)

def videoUserDefined(src: str, width="100%", height=315):
    """An extension of the video widget
    Arguments:
        src {str} -- url of the video Eg:- https://www.youtube.com/embed/B2iAodr0fOo
    Keyword Arguments:
        width {str} -- video width(By default: {"100%"})
        height {int} -- video height (By default: {315})
    """
    st.write(
        f'<iframe width="{width}" height="{height}" src="{src}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
        unsafe_allow_html=True,
    )

def main():
    st.title("데이터저널리즘 웹 프로젝트")
    st.subheader("인터랙티브하게 웹 콘텐츠 만들고 공유하기")
    st.write('''빅데이터와 인공지능 시대에 데이터저널리즘 방식의 뉴스 제작과 수용이 늘어나고 있습니다.
             python과 streamlit을 이용해 다양하고 흥미로운 콘텐츠를 이용자 맞춤형으로 만들어 보세요.
             데이터베이스를 제공해 이용자가 원하는 정보만 선택해 열람하게 할 수도 있습니다. 
             딥러닝 모형을 장착해 즉각적인 정보의 예측과 판단도 가능합니다''')
    st.markdown("<h1 style='color: red; font-size: 15px;'> 파이썬 빅데이터 기술을 바탕으로 참신한 아이디어와 나만의 상상력을 현실로 만들어 보세요^^</h1>", unsafe_allow_html=True)

    menu = ["사이트 정보","사이트 관리자"]
    choice = st.sidebar.selectbox('메뉴 선택',menu)
    if choice == '사이트 정보':
        st.markdown("###### 사이트 정보: 인터랙티브한 웹 콘텐츠 제작 지원과 학습을 위한 사이트")
    if choice == '사이트 관리자':
        st.markdown("###### 사이트 관리자: 경희대 미디어학과 이종혁 교수")

    #Image opening
    response= requests.get("https://mms.businesswire.com/media/20200616005364/en/798639/22/Streamlit_Logo_%281%29.jpg", headers={'User-Agent':'Mozilla/5.0'})
    image = Image.open(BytesIO(response.content))
    st.image(image, width=300, caption="Simple Image")

    # Video playing
    videoUserDefined("https://www.youtube.com/embed/B2iAodr0fOo")

    #widgets
    if st.checkbox("Show/hide"):
        st.text("참고 사이트 = https://docs.streamlit.io/library/api-reference")

    # Radio
    status = st.radio("파이썬에 대한 생각은(가장 가까운 답 하나만 선택)?",("유용하다","내 적성에 맞는다","잘할 수 있다","앞의 어떤 것에도 해당하지 않음"))
    if status == '유용하다':
      st.success("정확한 판단입니다. 노력해 보세요")
    elif status == '내 적성에 맞는다':
      st.success("축복입니다. 즐겁게 해보세요")
    elif status == '잘할 수 있다':
      st.success("이제 시작입니다. 노력과 시간만 투자하면 파이썬 고수가 될 수 있습니다")
    else:
      st.info("오늘 참여한 것만으로도 좋습니다. 관심을 놓지 마세요.")

if __name__ == '__main__':
    main()
