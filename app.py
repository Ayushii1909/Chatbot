
import streamlit as st

st.set_page_config(page_title="College Helpdesk Chatbot", page_icon="🎓")

st.title("🎓 College Helpdesk Chatbot")
st.write("Hello! Ask me anything about college.")

def get_response(message):
    message = message.lower().strip()

    if "hello" in message or "hi" in message:
        return "Hello! Welcome to the College Helpdesk Chatbot."

    elif "admission" in message:
        return "For admission details, please contact the college admission office."

    elif "fees" in message or "fee" in message:
        return "For fee details, please contact the college accounts department."

    elif "course" in message:
        return "The college offers various courses. Please check with the college office for details."

    elif "library" in message:
        return "The college library provides books and study materials to students."

    elif "exam" in message:
        return "Please contact your faculty or examination department for exam schedules."

    elif "time" in message or "hours" in message:
        return "Please contact the college office for working hours."

    elif "thank" in message:
        return "You're welcome! Have a great day."

    elif "bye" in message:
        return "Goodbye! Best wishes for your studies."

    else:
        return "Sorry, I don't understand that. Try asking about admissions, fees, courses, library, or exams."

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "How can I help you today?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Type your question here...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    response = get_response(user_input)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    st.rerun()
