import streamlit as st

st.title("Try calculating fair value yourself!")

# Initialize session state to manage the flow of the app
# if "show_next_input" not in st.session_state:
#     st.session_state["show_next_input"] = False


# # Initial input box
# initial_input = st.text_input("Enter something:")

# # Show "Next" button if the user provides an input
# if initial_input:
#     if st.button("Next"):
#         st.session_state["show_next_input"] = True

# # Show a second input box if the "Next" button is clicked
# if st.session_state["show_next_input"]:
#     st.text_input("Enter your next input here:", key="second_input")

if "current_slide" not in st.session_state:
    st.session_state["current_slide"] = 1  # Start at slide 1

# Function to go to the next slide
def next_slide():
    st.session_state["current_slide"] += 1

# Function to go back to the previous slide (optional)
def previous_slide():
    if st.session_state["current_slide"] > 1:
        st.session_state["current_slide"] -= 1

# Content for Slide 1
if st.session_state["current_slide"] == 1:
    st.header("Step 1: Provide Your First Input")
    user_input1 = st.text_input("Enter something:")
    if user_input1:
        if st.button("Next"):
            next_slide()

# Content for Slide 2
elif st.session_state["current_slide"] == 2:
    st.header("Step 2: Provide Your Next Input")
    user_input2 = st.text_input("Enter your next input:")
    if st.button("Previous"):
        previous_slide()
    if user_input2:
        if st.button("Next"):
            next_slide()

# Content for Slide 3 (or add more slides as needed)
elif st.session_state["current_slide"] == 3:
    st.header("Step 3: Final Step")
    user_input3 = st.text_input("Enter your final input:")
    if st.button("Previous"):
        previous_slide()
    if user_input3:
        st.success("Thank you! You've completed all steps!")
