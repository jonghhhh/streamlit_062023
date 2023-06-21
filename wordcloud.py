import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_word_cloud(text):
    wordcloud = WordCloud().generate(text)

    # Display the generated wordcloud
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    st.pyplot()

def main():
    st.title("Word Cloud Generator")

    # Text input
    text = st.text_area("Enter your text here", height=200)

    # Generate word cloud on button click
    if st.button("Generate Word Cloud"):
        generate_word_cloud(text)

if __name__ == "__main__":
    main()
