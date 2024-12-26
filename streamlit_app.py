import streamlit as st

st.title("Try calculating fair value yourself!")


import pandas as pd

df = pd.DataFrame(
    [
       {"Current": "", "5 Years ago": "", "10 Years ago": "","Compounded change in past 5 years": "", "Compounded change in past 10 years": "",  "Next 5 Years Prediction": ""},
       {"Current": "", "5 Years ago": "", "10 Years ago": "","Compounded change in past 5 years": "", "Compounded change in past 10 years": "",  "Next 5 Years Prediction": ""}
    
    ],
   index = ["EPS", "P/E ratio"]
)


edited_df = st.data_editor(df, use_container_width=True)

st.dataframe(edited_df, use_container_width=True)

# # Initialize session state for tracking the conversation flow
# if "step" not in st.session_state:
#     st.session_state["step"] = 1
# if "number1" not in st.session_state:
#     st.session_state["number1"] = None
# if "number2" not in st.session_state:
#     st.session_state["number2"] = None
# if "feedback" not in st.session_state:
#     st.session_state["feedback"] = None

# # Define navigation functions
# def go_to_next_step():
#     st.session_state["step"] += 1

# def go_to_previous_step():
#     st.session_state["step"] -= 1

# # Step 1: Ask for the first number
# if st.session_state["step"] == 1:
#     st.write("Hello! Please provide the Earnings per Share and P/E ratio from the past few years.")
#     eps_now = st.text_input("Enter the current earnings per share:")
#     eps_5 = st.text_input("Enter the earnings per share 5 years ago:")
#     eps_10 = st.text_input("Enter the earnings per share 10 years ago:")
    
#     pe_now = st.text_input("\nEnter the current P/E ratio:")
#     pe_5 = st.text_input("Enter the P/E ratio 5 years ago:")
#     pe_10 = st.text_input("Enter the P/E ratio 10 years ago:")

#     #st.button("Let's go to the next step")
#     if st.button("Let's go to the next step!"):
#         st.session_state["eps_now"] = eps_now
#         st.session_state["eps_5"] = eps_5
#         st.session_state["eps_10"] = eps_10

#         st.session_state["pe_now"] = pe_now
#         st.session_state["pe_5"] = pe_5
#         st.session_state["pe_10"] = pe_10


#         go_to_next_step()

# # Step 2: Ask for feedback or continue
# elif st.session_state["step"] == 2:
    
    
#     st.write(f'For your company:\n The current EPS is {st.session_state["eps_now"]} \n The EPS 5 years ago was {st.session_state["eps_5"]} \n The EPS 10 years ago was {st.session_state["eps_10"]} \n The current PE ratio is {st.session_state["pe_now"]} \n The PE ratio 5 years ago was {st.session_state["pe_5"]} \n The PE ratio 10 years ago was {st.session_state["pe_10"]}')

#     st.write("Please enter the growth of EPS and P/E ratio in compound interest:")
#     st.write("You can get these values from a company's annual report. There are also sites that offer this information for different companies.")

#     five_year_EPS = st.text_input("EPS growth in the past 5 years")
#     ten_year_EPS = st.text_input("EPS growth in the past 10 years")

#     five_year_PE = st.text_input("PE growth in the past 5 years")
#     ten_year_PE = st.text_input("PE growth in the past 10 years")

#     col1, col2, col3 = st.columns(3)
#     with col1:
#         if st.button("Go Back"):
#             go_to_previous_step()
#     with col2:
#         if st.button("I have a question"):
#             go_to_next_step()

#     with col3:
#         if st.button("Next step"):
#             go_to_next_step()
#             go_to_next_step()


# # Step 3: Ask for clarification
# elif st.session_state["step"] == 3:
#     st.write("What did you not understand?")
#     st.button("How do I get this value?")
#     st.button("How do I calculate compound interest?")
    
    
# # Step 4: Ask for the second number
# elif st.session_state["step"] == 4:
#     st.write("Predict the EPS and P/E ratio 5 years from now")
#     eps_future = st.text_input("Enter the EPS 5 years from now:")
#     PE_future = st.text_input("Enter the P/E ratio 5 years from now:")
    
#     if st.button("Next Step"):
#       go_to_next_step()  

# elif st.session_state["step"] == 5:

    # future_pred = int(st.text_input("Future value of the stock in 5 years"))
    # wanted_return = int(st.slider("How much return in percentage do you want per year from the stock?"))
    
    # if future_pred and wanted_return:

    #     rate = (wanted_return/100) + 1
    #     exponent = rate**5
    #     principal = future_pred/exponent

    #     st.write("The fair value is:", round(principal, 1))
     #see if there is a way to put "fair value" before adding values