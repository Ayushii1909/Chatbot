
import streamlit as st

st.set_page_config(
    page_title="College Helpdesk Chatbot",
    page_icon="🎓"
)

st.title("🎓 College Helpdesk Chatbot")
st.write("Hello! Welcome to the College Helpdesk.")
st.write("Ask me about admission, courses, fees, exams, library, or timings.")

def get_response(message):
    message = message.lower().strip()

    if message in ["bye", "exit", "quit"]:
        return "Goodbye! Best of luck with your studies!"

    elif "hello" in message or message == "hi" or "hey" in message:
        return "Hello! How can I help you today?"

    elif "admission" in message or "apply" in message:
        return "For admission, prepare your marksheet, ID proof, photographs, and required documents. Confirm exact requirements with your college office."

    elif "course" in message or "program" in message:
        return "Colleges may offer diploma, undergraduate, and postgraduate programs. Contact your college for its current course list."

    elif "fee" in message or "fees" in message or "payment" in message:
        return "Fees depend on the course and semester. Please contact your college accounts department for accurate details."

    elif "exam" in message or "timetable" in message:
        return "Check your college notice board or student portal for the latest examination timetable."

    elif "library" in message or "book" in message:
        return "The college library provides textbooks and reference books. Ask the librarian about borrowing rules."

    elif "timing" in message or "hours" in message:
        return "College timings may vary by department. Please confirm the schedule with your college office."

    elif "contact" in message or "phone" in message or "email" in message:
        return "Please check your college's official website for contact numbers and email addresses."

    elif "thank" in message:
        return "You're welcome! Happy to help."

    else:
        return "Sorry, I don't know that yet. Try asking about admission, courses, fees, exams, library, or timings."

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! 👋 What would you like to know about college?"
        }
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_message = st.chat_input("Type your question here...")

if user_message:
    st.session_state.messages.append(
        {"role": "user", "content": user_message}
    )

    answer = get_response(user_message)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    st.rerun()
