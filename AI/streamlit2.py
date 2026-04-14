import streamlit as st
import time
#streamlit run /Users/skyler/Desktop/VScode/AI/streamlit_test2.py

#st.session_state为字典类型{"count":0,"message":[]}
if "count" not in st.session_state:
    st.session_state["count"] = 1
if "message" not in st.session_state:
    st.session_state["message"] = []

st.title("AI chatbox")
st.divider()

prompt = st.chat_input("input your questions:")
if prompt:
    #st.session_state的内容:{"count":0,"message":[{"role":"user","content":prompt}]}
    st.session_state['message'].append({"role":"user","content":prompt})
    #一次性输出user输入的内容
    for i in st.session_state['message']:
        st.chat_message(i['role']).markdown(i['content'])
    
    with st.spinner("thinking..."):
        time.sleep(1)
        response = f"i do not know{st.session_state['count']}"
        #把ai回答添加到历史界面中
        st.session_state['message'].append({"role":"assistant","content":response})
        #st.session_state的内容:{"count":0,"message":[{"role":"user","content":prompt},{"role":"assistant","content":response}]}
        st.session_state['count'] += 1
        #将ai回答渲染到界面中
        st.chat_message("assistant").markdown(response)
