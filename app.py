import streamlit as st
import pickle
import pandas as pd

# Load data and model
data = pickle.load(open("data.pkl", "rb"))
model = pickle.load(open("model.pkl", "rb"))

# Extract unique values for dropdowns
area_type = data["area_type"].unique()
location = data["location"].unique()

# Title
st.title("🏠 Bengaluru House Price Prediction")

# UI inputs
selected_area_type = st.selectbox("Area Type", area_type)
selected_location = st.selectbox("Location", location)
total_sqft = st.text_input("Total sqft area", value=300)
bhk = st.text_input("BHK")
bath = st.text_input("Bathroom Count")


# Prediction function
def predict_price(df):
    prediction = model.predict(df)[0]
    return max(0, prediction)  # Avoid negative prices


# Button click
if st.button("Predict"):
    try:
        # Convert inputs
        sqft_val = float(total_sqft)
        bath_val = float(bath)
        bhk_val = int(bhk)

        # Input validation
        if sqft_val < 300 or bhk_val < 1 or bath_val < 1:
            st.error("⚠️ Please enter realistic values (min 300 sqft, 1 BHK, 1 Bath)")
        else:
            # Create input dataframe
            input_df = pd.DataFrame(
                [[selected_area_type, selected_location, sqft_val, bath_val, bhk_val]],
                columns=["area_type", "location", "total_sqft", "bath", "bhk"],
            )

            # Predict and show result
            result = predict_price(input_df)

            # Convert result to Crores (CRS)
            result_in_crs = result / 100  # Convert Lakhs to Crores

            st.success(f"🏷️ Estimated Price: ₹ {result_in_crs:.2f} Crores")

    except ValueError:
        st.error("❌ Please enter numeric values for sqft, BHK, and bathroom count.")
