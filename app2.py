import streamlit as st
import pickle 
import gr

def model_pred(GenHlth,CholCheck,HighBP,AnyHealthcare,PhysActivity,Veggies):
    values = np.array([GenHlth,CholCheck,HighBP,AnyHealthcare,PhysActivity,Veggies]).reshape(1,-1)
    columns = ['GenHlth','CholCheck','HighBP','AnyHealthcare','PhysActivity','Veggies']
    tab = pd.DataFrame(values,columns=columns)
    loaded_model = pickle.load(open('class_model.pkl', 'rb'))
    x = loaded_model.predict(tab)
    result = int(x[0])
    if result == 0:
        return 'Diabetic'
    else:
        return "Not diabetic"

GenHlth = st.number_input('GenHlth')
CholCheck = st.number_input('CholCheck')
HighBP = st.number_input('HighBP')
AnyHealthcare = st.number_input('AnyHealthcare')
PhysActivity = st.number_input('PhysActivity')
Veggies = st.number_input('Veggies')

if st.button('predict'):
  st.success(model_pred(GenHlth,CholCheck,HighBP,AnyHealthcare,PhysActivity,Veggies))
