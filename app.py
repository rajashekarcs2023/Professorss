import streamlit as st
from agent_communication import get_agent_comm

st.title("Multi-Agent Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize agent communication
if "agent_comm" not in st.session_state:
    st.session_state.agent_comm = get_agent_comm()

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What would you like to know?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Send user input to coordinator agent and get response
    with st.spinner("Thinking..."):
        response = st.session_state.agent_comm.get_response(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})