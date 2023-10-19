import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(
    open('D:\Model\Multiple Disease Predictor\saved models\diabetes_model.sav','rb'))

heart_disease_model = pickle.load(
    open('D:\Model\Multiple Disease Predictor\saved models\heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(
    open('D:\Model\Multiple Disease Predictor\saved models\Parkinsons_model.sav', 'rb'))

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

if (selected == 'Diabetes Prediction'):

    st.title('Diabetes Prediction')
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input('Number of Pregnancies',step=1)

    with col2:
        Glucose = st.number_input('Glucose Level',step=1)

    with col3:
        BloodPressure = st.number_input('Blood Pressure value',step=1)

    with col1:
        SkinThickness = st.number_input('Skin Thickness value',step=1)

    with col2:
        Insulin = st.number_input('Insulin Level',step=1)

    with col3:
        BMI = st.number_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.number_input('Age of the Person',step=1)

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

if (selected == 'Heart Disease Prediction'):

    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age',step=1)

    with col2:
        sex = st.number_input('Sex',help='Enter 1 for male and 0 for female',min_value=0,max_value=1)

    with col3:
        cp = st.number_input('Chest Pain types',step=1,min_value=0,max_value=3)

    with col1:
        trestbps = st.number_input('Resting Blood Pressure',step=1)

    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl',step=1)

    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl',step=1,help='1 = true and 0 = false',min_value=0,max_value=1)

    with col1:
        restecg = st.number_input('Resting Electrocardiographic results',step=1,min_value=0,max_value=2)

    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved',step=1)

    with col3:
        exang = st.number_input('Exercise Induced Angina',step=1,help='1 = yes and 0 = no',min_value=0,max_value=1)

    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')

    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment',step=1)

    with col3:
        ca = st.number_input('Major vessels colored by flourosopy',step=1,min_value=0,max_value=3)

    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect',step=1,min_value=0,max_value=2)

    heart_diagnosis = ''

    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

if (selected == "Parkinsons Prediction"):

    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    parkinsons_diagnosis = ''

    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP,
                                                           Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE,
                                                           DFA, spread1, spread2, D2, PPE]])

        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)