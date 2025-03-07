import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# Change Name & Logo
st.set_page_config(page_title="Disease Prediction", page_icon="⚕️", layout="wide")

# Custom Styling
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
    }
    .main {
        background-color: #f5f7fa;
    }
    .stButton>button {
        background-color: #008CBA;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border-radius: 10px;
    }
    .stButton>button:hover {
        background-color: #005f75;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
        padding: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Menu
with st.sidebar:
    selected = option_menu(
        menu_title="Disease Prediction",
        options=[
            'Diabetes Prediction',
            'Heart Disease Prediction',
            'Parkinsons Prediction',
            'Lung Cancer Prediction',
            'Hypo-Thyroid Prediction'
        ],
        icons=["activity", "heart", "person", "lungs", "thermometer"],
        menu_icon="stethoscope",
        default_index=0,
    )

# Load Models
models = {
    'diabetes': pickle.load(open('Models/diabetes_model.sav', 'rb')),
    'heart_disease': pickle.load(open('Models/heart_disease_model.sav', 'rb')),
    'parkinsons': pickle.load(open('Models/parkinsons_model.sav', 'rb')),
    'lung_cancer': pickle.load(open('Models/lungs_disease_model.sav', 'rb')),
    'thyroid': pickle.load(open('Models/Thyroid_model.sav', 'rb'))
}

def display_input(label, key, type="number"):
    return st.number_input(label, key=key, step=1) if type == "number" else st.text_input(label, key=key)

# Disease Prediction Pages
if selected == 'Diabetes Prediction':
    st.title("Diabetes Prediction 🩸")
    st.subheader("Enter details below:")
    col1, col2 = st.columns(2)
    with col1:
        Pregnancies = display_input('Number of Pregnancies', 'Pregnancies')
        Glucose = display_input('Glucose Level', 'Glucose')
        BloodPressure = display_input('Blood Pressure', 'BloodPressure')
        SkinThickness = display_input('Skin Thickness', 'SkinThickness')
    with col2:
        Insulin = display_input('Insulin Level', 'Insulin')
        BMI = display_input('BMI Value', 'BMI')
        DiabetesPedigreeFunction = display_input('Diabetes Pedigree Function', 'DiabetesPedigreeFunction')
        Age = display_input('Age', 'Age')
    
    if st.button("Predict Diabetes"):
        diab_prediction = models['diabetes'].predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        st.success("The person is diabetic" if diab_prediction[0] == 1 else "The person is not diabetic")

elif selected == 'Heart Disease Prediction':
    st.title("Heart Disease Prediction ❤️")
    st.subheader("Enter details below:")
    age = display_input('Age', 'age')
    sex = display_input('Sex (1 = Male, 0 = Female)', 'sex')
    cp = display_input('Chest Pain Type (0-3)', 'cp')
    trestbps = display_input('Resting Blood Pressure', 'trestbps')
    chol = display_input('Serum Cholesterol', 'chol')
    fbs = display_input('Fasting Blood Sugar (1 = True, 0 = False)', 'fbs')
    restecg = display_input('Resting ECG Results (0-2)', 'restecg')
    thalach = display_input('Maximum Heart Rate', 'thalach')
    exang = display_input('Exercise Induced Angina (1 = Yes, 0 = No)', 'exang')
    oldpeak = display_input('ST Depression Induced by Exercise', 'oldpeak')
    slope = display_input('Slope of Peak Exercise ST Segment (0-2)', 'slope')
    ca = display_input('Major Vessels Colored by Fluoroscopy (0-3)', 'ca')
    thal = display_input('Thal (0 = Normal, 1 = Fixed Defect, 2 = Reversible Defect)', 'thal')

    if st.button("Predict Heart Disease"):
        heart_prediction = models['heart_disease'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        st.success("The person has heart disease" if heart_prediction[0] == 1 else "The person does not have heart disease")


elif selected == 'Parkinsons Prediction':
    st.title("Parkinson's Disease Prediction 🧠")
    st.subheader("Enter details below:")
    
    inputs = [
        display_input('MDVP:Fo(Hz)', 'fo'),
        display_input('MDVP:Fhi(Hz)', 'fhi'),
        display_input('MDVP:Flo(Hz)', 'flo'),
        display_input('MDVP:Jitter(%)', 'Jitter_percent'),
        display_input('MDVP:Jitter(Abs)', 'Jitter_Abs'),
        display_input('MDVP:RAP', 'RAP'),
        display_input('MDVP:PPQ', 'PPQ'),
        display_input('Jitter:DDP', 'DDP'),
        display_input('MDVP:Shimmer', 'Shimmer'),
        display_input('MDVP:Shimmer(dB)', 'Shimmer_dB'),
        display_input('Shimmer:APQ3', 'APQ3'),
        display_input('Shimmer:APQ5', 'APQ5'),
        display_input('MDVP:APQ', 'APQ'),
        display_input('Shimmer:DDA', 'DDA'),
        display_input('NHR', 'NHR'),
        display_input('HNR', 'HNR'),
        display_input('RPDE', 'RPDE'),
        display_input('DFA', 'DFA'),
        display_input('Spread1', 'spread1'),
        display_input('Spread2', 'spread2'),
        display_input('D2', 'D2'),
        display_input('PPE', 'PPE')
    ]
    
    if st.button("Predict Parkinson's Disease"):
        parkinsons_prediction = models['parkinsons'].predict([inputs])
        st.success("The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease")

elif selected == 'Lung Cancer Prediction':
    st.title("Lung Cancer Prediction 🫁")
    st.subheader("Enter details below:")
    
    inputs = [
        display_input('Gender (1 = Male, 0 = Female)', 'GENDER'),
        display_input('Age', 'AGE'),
        display_input('Smoking (1 = Yes, 0 = No)', 'SMOKING'),
        display_input('Yellow Fingers (1 = Yes, 0 = No)', 'YELLOW_FINGERS'),
        display_input('Anxiety (1 = Yes, 0 = No)', 'ANXIETY'),
        display_input('Peer Pressure (1 = Yes, 0 = No)', 'PEER_PRESSURE'),
        display_input('Chronic Disease (1 = Yes, 0 = No)', 'CHRONIC_DISEASE'),
        display_input('Fatigue (1 = Yes, 0 = No)', 'FATIGUE'),
        display_input('Allergy (1 = Yes, 0 = No)', 'ALLERGY'),
        display_input('Wheezing (1 = Yes, 0 = No)', 'WHEEZING'),
        display_input('Alcohol Consuming (1 = Yes, 0 = No)', 'ALCOHOL_CONSUMING'),
        display_input('Coughing (1 = Yes, 0 = No)', 'COUGHING'),
        display_input('Shortness Of Breath (1 = Yes, 0 = No)', 'SHORTNESS_OF_BREATH'),
        display_input('Swallowing Difficulty (1 = Yes, 0 = No)', 'SWALLOWING_DIFFICULTY'),
        display_input('Chest Pain (1 = Yes, 0 = No)', 'CHEST_PAIN')
    ]
    
    if st.button("Predict Lung Cancer"):
        lungs_prediction = models['lung_cancer'].predict([inputs])
        st.success("The person has lung cancer" if lungs_prediction[0] == 1 else "The person does not have lung cancer")
elif selected == 'Hypo-Thyroid Prediction':
    st.title("Hypo-Thyroid Prediction 🦠")
    st.subheader("Enter details below:")
    
    inputs = [
        display_input('Age', 'age'),
        display_input('Sex (1 = Male, 0 = Female)', 'sex'),
        display_input('On Thyroxine (1 = Yes, 0 = No)', 'on_thyroxine'),
        display_input('TSH Level', 'tsh'),
        display_input('T3 Measured (1 = Yes, 0 = No)', 't3_measured'),
        display_input('T3 Level', 't3'),
        display_input('TT4 Level', 'tt4')
    ]
    
    if st.button("Predict Hypo-Thyroid"):
        thyroid_prediction = models['thyroid'].predict([inputs])
        st.success("The person has Hypo-Thyroid disease" if thyroid_prediction[0] == 1 else "The person does not have Hypo-Thyroid disease")
