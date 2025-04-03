import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,6))
Y = np.linspace(50, 90, 400)
AD1 = 10 - 0.1 * Y  
AD2 = 9 - 0.1 * Y  

SRAS = 3 * np.ones_like(Y)

plt.plot(Y, AD1, label='AD₁ (initial)', color='blue')
plt.plot(Y, AD2, label='AD₂ (after velocity falls)', color='red')
plt.plot(Y, SRAS, label='SRAS (sticky prices)', color='green', linestyle='--')

plt.axvline(x=70, label='LRAS (full employment)', color='purple', linestyle=':')

A_Y, A_P = 70, 3
B_Y, B_P = 60, 3
C_Y, C_P = 70, 2

plt.scatter([A_Y], [A_P], color='black')
plt.text(A_Y+1, A_P, 'A')
plt.scatter([B_Y], [B_P], color='black')
plt.text(B_Y-8, B_P+0.1, 'B')
plt.scatter([C_Y], [C_P], color='black')
plt.text(C_Y+1, C_P-0.3, 'C')

plt.title('AD–AS Adjustment to a Fall in Velocity (Constant Money Supply)')
plt.xlabel('Output (Y)')
plt.ylabel('Price Level (P)')
plt.legend()
plt.grid(True)
plt.show()