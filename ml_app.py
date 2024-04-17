import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(criterion='gini', max_depth = 10, mini_samples_leafs=5 random_state=0)
#clf_gini.fit(X_train, y_train)
model = joblib.load('finalized_model.joblib')
  # caching the model for faster loading
@st.cache
def predict(Buying, Maint,  Doors, Persons, Lug_boot, Safety):
    if Safety == 'med':
        safety = 1
    elif Safety == 'high':
        safety = 2
    elif Safety == 'low':
        safety = 3
    df = pd.DataFrame([[Buying, Maint, Doors, Persons, Lug_boot, safety]], columns=['Buying', 'Maint',  'Doors','Persons', 'Lug_boot', 'Safety'])
    prediction = model.predict([[Buying, Maint, Doors, Persons, Lug_boot, safety]])
    return prediction
st.title('Car Evaluation Classification')
st.image("""https://www.google.com/search?sca_esv=9422fde534929437&sca_upv=1&rlz=1C5CHFA_enIN1084IN1084&sxsrf=ACQVn0_FMmZ7uFVB78Y2_bH3GITDjBaE4g:1713333901495&q=aston+martin&uds=AMwkrPvE5CskFmMADUMlIkB3aXvAh5sKdFl7sCPH8YBTCx_o8fEQKP4pae_-PyjDmi7XypA3cPgtVfwSstodkXqoe-Ky77-SbPdOhk_F3HWINq6CsBhOSpMQHjKDgiT5bLEXTyz491auduTYrYrJ3D4vKRcD1qPfgMkoEUy15SoiHdPfLFuEZoQ6JE0elsXs9NEJTiMaczOAJnNndZiC5NyiNaeAXlBxsn5UQgMtrt32sIYh_ZAvW4ozUoQ2Nu1TFQie9Q7lY4kWtiFCsJ4wBr8l83NVRHcYdIYuW-tVJjSuH8FU4DCeA_E&udm=2&prmd=isnvmbtz&sa=X&ved=2ahUKEwjZ4tGUysiFAxXAd2wGHTGMDrsQtKgLegQIDRAB&biw=1600&bih=865&dpr=1.8#vhid=eyuoV6lLpvLdxM&vssid=mosaic""")
st.header('Enter the Information of the Car:')
st.text("vhigh = 1 high = 2 med = 3 low = 4")
Buying = st.number_input('buying:', min_value=1, max_value=4, value=1)
st.text("vhigh = 1 high = 2 med = 3 low = 4")
Maint = st.number_input('maint:', min_value=1, max_value=4, value=1)
st.text("2-Doors = 1  3-Doors = 2 4-Doors = 3 5more = 4")
Doors = st.number_input('doors:', min_value=1, max_value=4, value=1)
st.text("2-persons = 1  4-persons = 2 more = 3 ")
Persons = st.number_input('persons:', min_value=1, max_value=3, value=1)
st.text("small = 1  med = 2 big = 3 ")
Lug_boot = st.number_input('lug_boot:', min_value=1, max_value=3, value=1)
Safety = st.radio('safety:', ('med', 'high', 'low'))
if st.button('Submit_Car_Infos'):
    cal_eval = predict(Buying, Maint, Doors, Persons, Lug_boot, Safety)
    st.success(f'The Evaluation of Car : {cal_eval[0]}')
