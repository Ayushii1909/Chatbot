# College Helpdesk Chatbot
# A simple rule-based chatbot using only Python if-elif-else conditions.

print("=" * 42)
print("       COLLEGE HELPDESK CHATBOT")
print("=" * 42)
print("Hello! I am your College Helpdesk Chatbot.")
print("Ask me about admission, courses, fees, exams, library, or timings.")
print("Type 'bye' to end the conversation.\n")

while True:
    user_input = input("You: ").strip().lower()

    if user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Best of luck with your studies.")
        break

    elif "hello" in user_input or "hi" in user_input or "hey" in user_input:
        print("Bot: Hello! Welcome to the college helpdesk. How can I help you?")

    elif "admission" in user_input or "apply" in user_input:
        print("Bot: For admission, keep your previous marksheet, ID proof, "
              "photographs, and required application documents ready. "
              "Please confirm exact requirements with the college office.")

    elif "course" in user_input or "program" in user_input:
        print("Bot: Colleges may offer diploma, undergraduate, and postgraduate "
              "programs. Contact the college office for the current course list.")

    elif "fee" in user_input or "fees" in user_input or "payment" in user_input:
        print("Bot: Fee amounts depend on the course and semester. "
              "Please check the latest fee details with the accounts department.")

    elif "exam" in user_input or "timetable" in user_input:
        print("Bot: Please check the official college notice board or student "
              "portal for the latest exam timetable and announcements.")

    elif "library" in user_input or "book" in user_input:
        print("Bot: The library can help you find textbooks and reference books. "
              "Ask the librarian about borrowing rules and return dates.")

    elif "time" in user_input or "timing" in user_input or "hours" in user_input:
        print("Bot: College and office timings can vary by department. "
              "Please confirm today's timings with the college office.")

    elif "contact" in user_input or "phone" in user_input or "email" in user_input:
        print("Bot: You can find official phone numbers and email addresses "
              "on your college's official website or student portal.")

    elif "thank" in user_input:
        print("Bot: You're welcome! Happy to help.")

    elif "help" in user_input:
        print("Bot: You can ask about admission, courses, fees, exams, "
              "library, timings, or contact details.")

    else:
        print("Bot: Sorry, I don't know that yet. Try asking about admission, "
              "courses, fees, exams, library, timings, or contact details.")
