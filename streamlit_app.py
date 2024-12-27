import streamlit as st
import pandas as pd

st.title("Try calculating fair value yourself!")

st.subheader("Get and calculate data on the EPS and P/E ratio history!")

df = pd.DataFrame(
    [
       {"Current Value": "", "5 Years ago": "", "10 Years ago": "","5 years annualized growth": "", "10 years annualized growth": ""},
       {"Current Value": "", "5 Years ago": "", "10 Years ago": "","5 years annualized growth": "", "10 years annualized growth": ""}
    
    ],
   index = ["EPS", "P/E ratio"]
)


edited_df = st.data_editor(df,
                           column_config={
                               
        "5 years annualized growth": st.column_config.Column(width=200),
        "10 years annualized growth": st.column_config.Column(width=200)
    
    }
    )

#st.dataframe(edited_df, use_container_width=True)

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

future_pred_input = st.text_input("Future value of the stock in 5 years")
if future_pred_input:
     future_pred = float(future_pred_input)
     wanted_return_input = st.slider("How much return in percentage do you want per year from the stock?")
     if wanted_return_input:
          wanted_return = float(wanted_return_input)

          st.write("The fair value is:")
          rate = (wanted_return/100) + 1
          exponent = rate**5
          principal = future_pred/exponent
          st.write(principal)     

#see about the table sizes

st.subheader("Now let's try calculating the fair value with Graham's method!")
graham_eps_input = st.text_input("Start by entering the trailing 12 months Earnings per Share:")

if graham_eps_input:
    graham_eps = float(graham_eps_input)
    growth_input = st.text_input("Now enter the growth:")
    if growth_input:
        growth = float(growth_input)
        brackets = 8.5 + (2 * growth)
        graham_value = graham_eps * brackets
        st.write("Fair Value:", graham_value)
        margin_of_safety = float(st.slider("How much margin of safety do you want (in %)?"))
        mos_rate = 1 - (margin_of_safety/100)
        discounted_val = graham_value * mos_rate
        st.write("Discounted Value:", discounted_val)

        st.write("You can compare these values with your own fair value to see how close they are to better understand the differences between the methods!")