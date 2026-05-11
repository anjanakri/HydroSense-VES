from core.computation import compute_ves, many_compute_ves
from core.classification import classify_curve, classify_water_quality
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

print("----------------")
rho_a2 = np.array([5, 10, 20, 40, 80])
print(classify_curve(rho_a2))          # A-Type
print(classify_water_quality(rho_a2))

print("----------------")
# Fresh water test — min must be > 100
rho_a_fresh = np.array([500, 300, 150, 120, 200, 400])
print(classify_water_quality(rho_a_fresh))   # Fresh Water

# Slightly saline — min between 30-100
rho_a_slight = np.array([200, 100, 50, 35, 80, 150])
print(classify_water_quality(rho_a_slight))  # Slightly Saline

# Highly saline — min < 10
rho_a_saline = np.array([120, 80, 40, 8, 12, 50, 95])
print(classify_water_quality(rho_a_saline))  # Highly Saline
