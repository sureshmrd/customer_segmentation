# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import pickle
import streamlit as st
loaded_model=pickle.load(open("customer_trained.sav","rb"))

#creating prediction

def customer_predtiction(input_data):
    
    #numpy_array=np.asarray(input_data)
    
    #reshape
    prediction=loaded_model.fit_predict(input_data)
    return prediction
 
     
     
def main():
    st.title("Customer Segmentation")
    
    Income1=st.text_input("Enter Income 1:")
    SpendingScore1=st.text_input("Enter Spending Score 1:")
    list1=[Income1,SpendingScore1]
    
    Income2=st.text_input("Enter Income 2:")
    SpendingScore2=st.text_input("Enter Spending Score 2:")
    list2=[Income2,SpendingScore2]
    
    Income3=st.text_input("Enter Income 3:")
    SpendingScore3=st.text_input("Enter Spending Score 3:")
    list3=[Income3,SpendingScore3]
    
    Income4=st.text_input("Enter Income 4:")
    SpendingScore4=st.text_input("Enter Spending Score 4:")
    list4=[Income4,SpendingScore4]
    
    Income5=st.text_input("Enter Income 5:")
    SpendingScore5=st.text_input("Enter Spending Score 5")
    list5=[Income5,SpendingScore5]
    
    list=[list1,list2,list3,list4,list5]
    
    customers=[]
    
    if st.button('Customer Segmentation'):
        customers = customer_predtiction(list)
        
    st.success(customers)
        
        
if __name__ == '__main__':
    main()
    
    
    
    
    
    