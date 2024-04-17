import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(
  model = joblib.load('finalized_model.joblib')
  # caching the model for faster loading
  @st.cache
