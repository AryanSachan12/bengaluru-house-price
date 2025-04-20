# 🏠 Bengaluru House Price Prediction App

Welcome to the **Bengaluru House Price Prediction App** — a machine learning-based web app built using **Streamlit** that helps users estimate property prices in Bangalore based on key features like location, square footage, number of bedrooms, and bathrooms.

---

## 📌 Features

- 🔮 Predicts property price in **lakhs INR** using a trained Ridge Regression model
- 📊 Cleaned and preprocessed real-world housing dataset
- 🧠 Built using **scikit-learn**, **pandas**, and **Streamlit**
- 💡 Simple and intuitive user interface
- 📦 Model and preprocessing steps serialized using `pickle`

---

## 🚀 Demo

### 👉 [Live Demo](#) (https://aryansachan12-bengaluru-house-price-app-vb5xnh.streamlit.app/)

---

## 🛠️ Tech Stack

- Python 3.10+
- Streamlit
- pandas
- scikit-learn
- Ridge Regression
- pickle

---

## 📁 Dataset

- Source: Kaggle – Bengaluru House Data
- Includes fields: `location`, `area_type`, `total_sqft`, `bath`, `bhk`, `price`

---

## 🧹 Data Cleaning & Preprocessing

- Handled missing values
- Converted range-based square footage to numeric
- Removed extreme outliers
- One-hot encoded categorical features
- Scaled numerical features using `StandardScaler`

---

## 🧠 Model

- **Ridge Regression** was selected for its regularization capabilities
- Trained with OneHotEncoded + Scaled features in a `Pipeline`

---

## 💻 How to Run Locally

```bash
# Clone the repo
git clone https://github.com/AryanSachan12/bengaluru-house-price
cd bengaluru-house-price

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 📦 Project Structure

```
.
├── app.py               # Streamlit UI
├── model.pkl            # Trained ML model
├── data.pkl             # Data for dropdowns
├── dataset/             # Raw and cleaned dataset
├── requirements.txt     # Python dependencies
└── README.md
```

---

## ✨ Future Improvements

- 📈 Model performance enhancement (e.g., ensemble models)
- 🗺️ Add maps to show neighborhood visuals
- 💾 Deploy app to Streamlit Cloud or Render
- 🌐 API endpoint for predictions

---

## 🙌 Acknowledgements

- 📊 [Kaggle Dataset](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data)
- 🧰 Streamlit for UI framework
- 🤖 scikit-learn for modeling

---

## 🧑‍💻 Author

Made with ❤️ by **Aryan Sachan**  
📧 aryansachan2004@gmail.com  
🌐 [GitHub](https://github.com/AryanSachan12)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
