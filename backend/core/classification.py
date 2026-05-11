import numpy as np

def classify_curve(apparent_res: np.ndarray)->str:
    n=len(apparent_res)
    s1=np.mean(apparent_res[:n//3])
    s2=np.mean(apparent_res[n//3: 2*n//3])
    s3 = np.mean(apparent_res[2*n//3:])
    #checking
    if(s1<s2<s3):
        return "A-Type"
    elif(s1>s2>s3):
        return "Q-Type"
    elif(s1>s2<s3):
        return "H-Type"
    elif(s1<s2>s3):
        return "K-Type"
    else:
        return "Unknown"
        
def classify_water_quality(apparent_res: np.ndarray)->str:
    min_res=np.min(apparent_res)
    #checking
    #INTW if min_res>
    if min_res>100:
        return "Fresh Water"
    elif min_res>30:
        return "Slightly Saline"
    elif min_res > 10:
        return "Moderately Saline"
    else:
        return "Highly Saline"