❤️ Heart Disease Prediction using Machine Learning & Streamlit

This project is an interactive Heart Disease Prediction Web App built using Machine Learning (Logistic Regression) and Streamlit.
Users can enter medical details, and the app instantly predicts the risk of heart disease.

✅ Project Highlights

🔍 Machine Learning model for heart disease risk prediction

🧹 Complete data preprocessing & feature selection

🌐 Streamlit web interface for real-time input

⚡ Fast, lightweight, and easy to use

📁 End-to-end integration (model + frontend)

🛠️ Tech Stack

Python

Pandas

Scikit-Learn

Streamlit

Pickle

📂 Project Structure
Heart_Disease/
│── app.py               # Streamlit user interface
│── backend_model.py     # ML model training file
│── heart.csv            # Dataset
│── heart_model.pkl      # Saved ML model
│── README.md            # Documentation

🚀 How to Run
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Train the model
python backend_model.py

3️⃣ Run the Streamlit App
streamlit run app.py

📊 Model Information

Algorithm: Logistic Regression

Target column: condition

Input fields include:

age, sex, cp, trestbps, chol

fbs, restecg, thalach

exang, oldpeak, slope

ca, thal

✅ Output:

1 → High risk of heart disease

0 → No heart disease

🙏 Acknowledgement

💫 Grateful to my mentor KODI PRAKASH SENAPATI for continuous guidance and motivation throughout this project.

🔮 Future Enhancements

✅ Add more ML models (Random Forest, SVM, ANN)

✅ Deploy on Streamlit Cloud / HuggingFace

✅ Add analytics dashboard & charts

✅ Enhance UI and design
