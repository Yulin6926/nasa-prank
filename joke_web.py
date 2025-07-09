import streamlit as st
import time
import random

st.set_page_config(page_title="NASA终端", layout="wide")

st.markdown("## 👨‍💻 系统初始化中，请勿关闭网页...")
time.sleep(1.5)

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

with st.empty():
    for _ in range(30):
        line = "".join(random.choices(chars, k=60))
        st.code(line)
        time.sleep(0.1)

st.markdown("### ⚠️ 正在入侵 NASA 系统...")
time.sleep(1.5)
st.markdown("### 🔓 正在尝试获取权限...")
time.sleep(1.5)
st.error("权限获取失败：你以为你是谁 😂")
