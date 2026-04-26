import numpy as np
import pandas as pd

""" geometric factor K
    ab means L (current electrode difference)
    mn means l(potential electrode difference)
"""
def K_factor(ab: float, mn:float)-> float:    # -> means it is a HINT that will return a float value
    K=np.pi*((ab**2)-(mn**2))/(2*mn)
    return K


#Apparent resistivty
def app_resisistivity(K:float, V: float, I:float)->float:
    App_Resistivity=K*(V/I)
    return App_Resistivity

#compute_ves() - Final Resistivity
def compute_ves(ab:float, mn:float, V:float, I:float)->float :
    validate_inputs(ab, mn, V, I)
    K=K_factor(ab, mn)
    App_Resistivity=app_resisistivity(K,V,I)
    return App_Resistivity

def validate_inputs(ab:float, mn:float, V:float, I:float)->None: #guard function
    """ 
        __rules__
            ab > 0
            mn > 0
            mn < ab
            I != 0
            V >= 0
    """
    
    if(ab<=0):
        raise ValueError("Oops! AB/2 must be greater than 0!")
    
    if(mn<=0):
        raise ValueError("Oops! MN/2 must be greater than 0!")
    if(mn>ab):
        raise ValueError("Oops! MN/2 must be less than AB/2 (Schlumberger condition)!")
    
    if(I==0):
        raise ValueError("Oops! Current (I) cannot be zero!")
    if(V<0):
        raise ValueError("Oops! Voltage (V) cannot be negative!!")
        

def many_compute_ves(df: pd.DataFrame)->pd.DataFrame:
    ab= df["AB/2"].values
    mn= df["MN/2"].values
    V= df["Voltage"].values
    I= df["Current"].values
    
    K=np.pi*((ab**2)-(mn**2))/(2*mn) #we are not using compute ves, beacuse it will make it slower 
    apparent_res=K*(V/I)
    
    df["App Resistivity"]=apparent_res
    return df