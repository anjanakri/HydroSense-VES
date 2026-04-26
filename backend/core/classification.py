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
        