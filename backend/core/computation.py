import numpy as np
import pandas as pd

""" geometric factor K
    ab2 means L (current electrode difference)
    mn2 means l(potential electrode difference)
"""
def K_factor(ab2: float, mn2:float)-> float:    # -> means it is a HINT that will return a float value
    K=np.pi*((ab2**2)-(mn2**2))/mn2
    return K


#Apparent resistivty
def app_resisistivity(K:float, V: float, I:float)->float:
    App_Resistivity=K*(V/I)
    return App_Resistivity

#compute_ves() - Final Resistivity
def compute_ves(ab2:float, mn2:float, V:float, I:float)->float :
    validate_inputs(ab2, mn2, V, I)
    K=K_factor(ab2, mn2)
    App_Resistivity=app_resisistivity(K,V,I)
    return App_Resistivity

def validate_inputs(ab2:float, mn2:float, V:float, I:float)->None: #guard function
    """ 
        __rules__
            ab2 > 0
            mn2 > 0
            mn2 < ab2
            I != 0
            V >= 0
    """
    
    if(ab2<=0):
        raise ValueError("Oops! AB/2 must be greater than 0!")
    
    if(mn2<=0):
        raise ValueError("Oops! MN/2 must be greater than 0!")
    if(mn2>ab2):
        raise ValueError("Oops! MN/2 must be less than AB/2 (Schlumberger condition)!")
    
    if(I==0):
        raise ValueError("Oops! Current (I) cannot be zero!")
    if(V<0):
        raise ValueError("Oops! Voltage (V) cannot be negative!!")
        

def many_compute_ves(df: pd.DataFrame)->pd.DataFrame:
    ab2= df["AB/2"].values
    mn2= df["MN/2"].values
    V= df["Voltage"].values
    I= df["Current"].values
    