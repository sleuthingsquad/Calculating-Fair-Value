import streamlit as st
import pandas as pd

st.title("Try calculating fair value yourself!")

st.subheader("Get and calculate data on the EPS and P/E ratio history!")


df = pd.DataFrame(
    [
       {"Current Value": "", "5 Years ago": "", "10 Years ago": "","Annualized growth in the past 5 years": "", "Annualized growth in the past 10 years": ""},
       {"Current Value": "", "5 Years ago": "", "10 Years ago": "","Annualized growth in the past 5 years": "", "Annualized growth in the past 10 years": ""}
    
    ],
   index = ["EPS", "P/E ratio"]
)


edited_df = st.data_editor(df, 
                           use_container_width=True,
                           column_config={
                               
        "Annualized growth in the past 5 years": st.column_config.Column(width=200),  # Adjust width for each column
        "Annualized growth in the past 10 years": st.column_config.Column(width=200)
    
    },)

st.dataframe(edited_df, use_container_width=True)

st.subheader("Your predictions for the EPS and P/E ratio in the next 5 years:")
df_preds = pd.DataFrame(
    [
       {"Bull Case": "", "Base Case": "", "Bear Case": ""},
       {"Bull Case": "", "Base Case": "", "Bear Case": ""},
       {"Bull Case": "", "Base Case": "", "Bear Case": ""}
    
    ],
   index = ["EPS", "P/E ratio", "Future Price"]
)
edited_df_preds = st.data_editor(df_preds)

st.write("Now, plug in your 3 possible future values and the rate you want. Note down the 3 possible fair values. Read the annual report and do some research, and see what value is right for you!")

future_pred = float(st.text_input("Future value of the stock in 5 years"))
wanted_return = float(st.slider("How much return in percentage do you want per year from the stock?"))

st.write("The fair value is:")

if future_pred and wanted_return:

      rate = (wanted_return/100) + 1
      exponent = rate**5
      principal = future_pred/exponent
      st.write(principal)
        
   #see if there is a way to put "fair value" before adding values

#see about the table size

st.subheader("Now let's try calculating the fair value with Graham's method!")
graham_eps = float(st.text_input("Trailing 12 months Earnings per Share:"))
growth = float(st.text_input("growth"))

#if st.button("Calculate fair value"):
brackets = 8.5 + (2 * growth)
#print(brackets)
graham_value = graham_eps * brackets
#print(graham_value)
st.write("Fair Value:", graham_value)

margin_of_safety = float(st.slider("How much margin of safety do you want (in %)?"))
mos_rate = 1 - (margin_of_safety/100)
discounted_val = graham_value * mos_rate
st.write("Discounted Value:", discounted_val)

st.write("You can compare these values with your own fair value to see how close they are to better understand the differences between the methods!")

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