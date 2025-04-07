import streamlit as st
from openai import OpenAI

st.title("Deepseek CoT Chat")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["DEEPSEEK_API_KEY"]
)

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input(f"Message Deepseek R1...")
if prompt:
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        reasoning_placeholder = st.empty()
        message_placeholder = st.empty()
        full_response = ""
        reasoning_response = ""
        
        with reasoning_placeholder.expander("Reasoning", expanded=True, icon="🧠"):
            st.empty()
            
        for response in client.chat.completions.create(
            model="deepseek/deepseek-r1:free",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            if hasattr(response.choices[0].delta, 'reasoning') and response.choices[0].delta.reasoning:
                incremental_content = response.choices[0].delta.reasoning or ""
                reasoning_response += incremental_content
                with reasoning_placeholder.expander("Reasoning", expanded=True, icon="🧠"):
                    st.markdown(reasoning_response + ("⬤" if response.choices[0].finish_reason is None else ""))
            else:
                incremental_content = response.choices[0].delta.content or ""
                full_response += incremental_content
                message_placeholder.markdown(full_response + "⬤")

        message_placeholder.markdown(full_response)
        if reasoning_response:
            with reasoning_placeholder.expander("Reasoning", expanded=True, icon="🧠"):
                st.markdown(reasoning_response)
        
    st.session_state["messages"].append({"role": "assistant", "content": full_response})
