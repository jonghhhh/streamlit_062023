import streamlit as st
import pandas as pd

def search_dataframe(dataframe, keyword):
    # Filter the DataFrame based on the keyword
    filtered_df = dataframe[dataframe['Text'].str.contains(keyword, case=False)]
    return filtered_df

def main():
    st.title("DataFrame Keyword Search")

    # Load the DataFrame
    df = pd.read_csv("your_dataframe.csv")

    # Display the DataFrame
    st.write("Original DataFrame:")
    st.write(df)

    # Keyword input
    keyword = st.text_input("Enter a keyword to search")

    # Perform search on button click
    if st.button("Search"):
        filtered_data = search_dataframe(df, keyword)
        st.write("Filtered DataFrame:")
        st.write(filtered_data)

if __name__ == "__main__":
    main()
