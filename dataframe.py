import streamlit as st
import pandas as pd

df = pd.read_excel("동아한겨레1면제목_20130101_20230430.xlsx")

def main():
    st.title("DataFrame Keyword Search")

    # Load the DataFrame
    #df = pd.read_excel("동아한겨레1면제목_20130101_20230430.xlsx")

    # Display the DataFrame
    st.write("Original DataFrame:")
    st.write(df)

    # Keyword input
    keyword = st.text_input("Enter a keyword to search")

    # Perform search on button click
    if st.button("Search"):
        result = []
        for i, d in enumerate(df['title']):
            if keyword in d:
                result.append(i)
            else:
                pass
    
        filtered_data = df[df.index.isin(result)]
        st.write("Filtered DataFrame:")
        st.write(filtered_data)

if __name__ == "__main__":
    main()
