import streamlit as st

st.title("Try calculating fair value yourself!")
st.subheader("Grab a pen or pencil and a piece of paper!")


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
    st.write("Hello! Please provide the Earnings per Share and P/E ratio from the past few years.")
    eps_now = st.text_input("Enter the current earnings per share:")
    eps_5 = st.text_input("Enter the earnings per share 5 years ago:")
    eps_10 = st.text_input("Enter the earnings per share 10 years ago:")
    
    pe_now = st.text_input("\nEnter the current P/E ratio:")
    pe_5 = st.text_input("Enter the P/E ratio 5 years ago:")
    pe_10 = st.text_input("Enter the P/E ratio 10 years ago:")

    #st.button("Let's go to the next step")
    if st.button("Let's go to the next step!"):
        st.session_state["eps_now"] = eps_now
        st.session_state["eps_5"] = eps_5
        st.session_state["eps_10"] = eps_10

        st.session_state["pe_now"] = pe_now
        st.session_state["pe_5"] = pe_5
        st.session_state["pe_10"] = pe_10


        go_to_next_step()

# Step 2: Ask for feedback or continue
elif st.session_state["step"] == 2:
    
    
    st.write(f'For your company:\n The current EPS is {st.session_state["eps_now"]} \n The EPS 5 years ago was {st.session_state["eps_5"]} \n The EPS 10 years ago was {st.session_state["eps_10"]} \n The current PE ratio is {st.session_state["pe_now"]} \n The PE ratio 5 years ago was {st.session_state["pe_5"]} \n The PE ratio 10 years ago was {st.session_state["pe_10"]}')

    st.write("Please enter the growth of EPS and P/E ratio in compound interest:")
    
    five_year_EPS = st.text_input("EPS growth in the past 5 years")
    ten_year_EPS = st.text_input("EPS growth in the past 10 years")

    five_year_PE = st.text_input("PE growth in the past 5 years")
    ten_year_PE = st.text_input("PE growth in the past 10 years")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Go Back"):
            go_to_previous_step()
    with col2:
        if st.button("I have a question"):
            go_to_next_step()

    with col3:
        if st.button("Next step"):
            go_to_next_step()
            go_to_next_step()


# Step 3: Ask for clarification
elif st.session_state["step"] == 3:
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