import openai
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

openai_api_key = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))


def clear_history():
    st.session_state.conversation_history = [{"role": "system", "content": "You are a knowledgeable and polite AI dietitian assistant. You provide structured and concise answers related to fitness, body recomposition, and nutrition."}]
    st.session_state.messages = []

max_history = 5

def prompt_output(users_prompt):
    # global conversation_history

    prompt = f"""You are a highly knowledgeable and polite AI dietician assistant. You provide clear, concise, and well-calculated answers related to nutrition, fitness, and body recomposition.  

 **Guidelines for Answering:**  
1. **Limit your response to 250 tokens.** Keep it **concise and direct**, covering only essential details.
2. You must give your answer such that your complete answers finishes in 250 tokens. So, always be concise and direct  
3. **Use structured bullet points** for clarity.  
4. Always ask about body height and weight before giving any tips or suggesting any diet or workout plans.
5. **Always calculate & provide macros + calories** for diet-related queries.  
6. **Ask for food and workout preferences** before giving recommendations.  
7. **If the user seems demotivated, provide short, encouraging advice.**  
8. **Focus on key takeaways rather than lengthy explanations.** 

Question of your user is : {users_prompt}
"""
    
    if "conversation_history" not in st.session_state:
        st.session_state.conversation_history = [
            {"role": "system", "content": "You are a knowledgeable and polite AI dietitian assistant. You provide structured and concise answers related to fitness, body recomposition, and nutrition."}
        ]

    st.session_state.conversation_history.append({'role':'user', 'content':prompt})

    if len(st.session_state.conversation_history)>max_history:
        st.session_state.conversation_history = st.session_state.conversation_history[-max_history:]

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages= st.session_state.conversation_history
, max_tokens = 250
, temperature = 0.6
, response_format = {
    "type": "text"
  })
    output = response["choices"][0]["message"]["content"]
    st.session_state.conversation_history.append({'role':'assistant','content': output})
    return output