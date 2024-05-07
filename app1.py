# Conversational Q&A chatbot

import streamlit as st
# streamlit has session mamangement in which context is remembered to manage session

#when user types question, it becomes human message. default message= system message ex: act as comedy chatbot
# if bot provides the response it is called AImessage
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI

#Streamlit UI 
st.set_page_config(page_title= "Conversational Q&A chatbot")
st.header("Hey, how may I help you?")

from dotenv import load_dotenv
load_dotenv()
import os



#initializing 
chat= ChatOpenAI(temperatur= 0.5)

#if, by default there is no message, first message shouldbe from system to bot saying to act as comedy AI
if 'flowmessages' not in st.session_state:
    st.session_state["flowmessages"]= [
        SystemMessage(content= "You're a comedian AI assistant")
    ]

#if this condition is not me, that is, if there is anything from user then it is appended as Human message

## load OpenAI and get responses
def get_chatmodel_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content= question)) # flownmessage is key
    answer= cha(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))

    return answer.content


#all schemas value need to be stored in the session, entire chatbot shold remember context of chat
#streamlit session state: create session key and store all schema data and then append specific value

#in this context. i can ask bot to remember my name. and then after asing multiple questions, and ask bot
# if it remembers name then it will prompt my name

    
    
