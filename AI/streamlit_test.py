import streamlit as st
import time
#streamlit run /Users/skyler/Desktop/VScode/AI/streamlit_test.py

st.title("AI chatbox")
st.write("hi")
st.divider()
name = st.chat_input("input your name")
st.write(f"Hello:{name}")

if name:
    st.write(f"Hi:{name}")

#消息容器
#角色支持：human,ai,user,assistant
st.chat_message("ai").markdown("111")
st.chat_message("assistant").markdown("1111111")

def thinking():
    with st.spinner("ing..."):
        time.sleep(3)
        st.write("Finish!")