import streamlit as st

# 設定網頁標題
st.set_page_config(page_title="我的簡單網頁", page_icon="🌐", layout="centered")

# 標題
st.title("🌟 歡迎來到我的簡單網頁")

# 副標題
st.subheader("這是一個使用 Streamlit 製作的基本網頁")

# 內文
st.write("""
這個網頁展示了如何使用 Streamlit 建立一個基本的標題頁面。
你可以在這裡放置更多內容，例如圖片、圖表或輸入元件。
""")

# 簡單的按鈕範例
if st.button("點我一下"):
    st.success("你點了按鈕！🎉")
