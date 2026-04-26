from core.computation import compute_ves, many_compute_ves
from core.classification import classify_curve
import numpy as np
import pandas as pd


#test single row
print(compute_ves(10,2,0.5,3))

data = {
    "AB/2":    [1.5, 2, 3],
    "MN/2":    [0.5,  0.5,  0.5],
    "Voltage": [98, 85, 76],
    "Current": [70, 60, 80]
}
print(data)
df = pd.DataFrame(data)
print(df)
print(many_compute_ves(df))


# H-type test — goes down then up
data = np.array([50, 40, 20, 10, 25, 60, 80])
print(classify_curve(data))  # should print H-type
# A-type — continuously increasing
rho_a_A = np.array([10, 20, 30, 40, 50, 60, 70])
print(classify_curve(rho_a_A))  # should print A-type

# Q-type — continuously decreasing
rho_a_Q = np.array([70, 60, 50, 40, 30, 20, 10])
print(classify_curve(rho_a_Q))  # should print Q-type

# K-type — goes up then down
rho_a_K = np.array([10, 20, 80, 90, 40, 20, 10])
print(classify_curve(rho_a_K))  # should print K-type