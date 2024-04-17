import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(criterion='gini', max_depth = 3, random_state=0)
#clf_gini.fit(X_train, y_train)
model = joblib.load('finalized_model.joblib')
  # caching the model for faster loading
@st.cache
