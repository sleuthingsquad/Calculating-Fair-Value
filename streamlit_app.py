import streamlit as st

st.title("Try calculating fair value yourself!")

# # Initialize session state to manage the flow of the app
# # if "show_next_input" not in st.session_state:
# #     st.session_state["show_next_input"] = False


# # # Initial input box
# # initial_input = st.text_input("Enter something:")

# # # Show "Next" button if the user provides an input
# # if initial_input:
# #     if st.button("Next"):
# #         st.session_state["show_next_input"] = True

# # # Show a second input box if the "Next" button is clicked
# # if st.session_state["show_next_input"]:
# #     st.text_input("Enter your next input here:", key="second_input")

# if "current_slide" not in st.session_state:
#     st.session_state["current_slide"] = 1  # Start at slide 1

# # Function to go to the next slide
# def next_slide():
#     st.session_state["current_slide"] += 1

# # Function to go back to the previous slide (optional)
# def previous_slide():
#     if st.session_state["current_slide"] > 1:
#         st.session_state["current_slide"] -= 1

# # Content for Slide 1
# if st.session_state["current_slide"] == 1:
#     st.header("Step 1: Provide Your First Input")
#     user_input1 = st.text_input("Enter something:")
#     if user_input1:
#         if st.button("Next"):
#             next_slide()

# # Content for Slide 2
# elif st.session_state["current_slide"] == 2:
#     st.header("Step 2: Provide Your Next Input")
#     user_input2 = st.text_input("Enter your next input:")
#     if st.button("Previous"):
#         previous_slide()
#     if user_input2:
#         if st.button("Next"):
#             next_slide()

# # Content for Slide 3 (or add more slides as needed)
# elif st.session_state["current_slide"] == 3:
#     st.header("Step 3: Final Step")
#     user_input3 = st.text_input("Enter your final input:")
#     if st.button("Previous"):
#         previous_slide()
#     if user_input3:
#         st.success("Thank you! You've completed all steps!")


#chosen option

# Initialize session state for tracking the conversation flow
if "step" not in st.session_state:
    st.session_state["step"] = 1
if "number1" not in st.session_state:
    st.session_state["number1"] = None
if "number2" not in st.session_state:
    st.session_state["number2"] = None
if "feedback" not in st.session_state:
    st.session_state["feedback"] = None

# Define navigation functions
def go_to_next_step():
    st.session_state["step"] += 1

def go_to_previous_step():
    st.session_state["step"] -= 1

# Step 1: Ask for the first number
if st.session_state["step"] == 1:
    st.write("Hello! Please provide your first number.")
    number1 = st.text_input("Enter the first number:")

    if number1:
        st.session_state["number1"] = number1
        go_to_next_step()

# Step 2: Ask for feedback or continue
elif st.session_state["step"] == 2:
    st.subheader("Chatbot:")
    st.write(f"Got it! You entered: {st.session_state['number1']}.")
    st.write("Now, are you ready to proceed, or do you have any questions?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Go Back"):
            go_to_previous_step()
    with col2:
        if st.button("I have a question"):
            go_to_next_step()

# Step 3: Ask for clarification
elif st.session_state["step"] == 3:
    st.subheader("Chatbot:")
    st.write("What did you not understand?")
    st.button("How do I get this value?")
    st.button("How do I calculate compound interest?")
    
    
# Step 4: Ask for the second number
elif st.session_state["step"] == 4:
    st.subheader("Chatbot:")
    st.write("Great! Now, please provide your second number.")
    number2 = st.text_input("Enter the second number:")
    
    if number2:
        st.session_state["number2"] = number2
        st.success(f"Thank you! You provided the numbers {st.session_state['number1']} and {st.session_state['number2']}.")