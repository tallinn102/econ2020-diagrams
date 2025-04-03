import matplotlib.pyplot as plt
import numpy as np

Y = np.linspace(40, 90, 400)

IS = 5 - 0.05 * Y  
LM1 = 0.05 * Y - 2  
LM2 = 0.05 * Y - 1  
A_Y, A_i = 70, 1.5
B_Y, B_i = 60, 2

plt.figure(figsize=(8,6))
plt.plot(Y, IS, label='IS', color='blue')
plt.plot(Y, LM1, label='LM₁ (original)', color='green')
plt.plot(Y, LM2, label='LM₂ (after increase in money demand)', color='red')

plt.scatter([A_Y], [A_i], color='black')
plt.text(A_Y+1, A_i, 'A')
plt.scatter([B_Y], [B_i], color='black')
plt.text(B_Y-8, B_i+0.1, 'B')

plt.title('Short-Run Effect of an Increase in Money Demand (Constant Money Supply)')
plt.xlabel('Output (Y)')
plt.ylabel('Interest Rate (i)')
plt.legend()
plt.grid(True)
plt.show()