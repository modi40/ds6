import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Car_Model': ['Model A', 'Model B', 'Model C', 'Model D', 'Model E', 'Model F', 'Model G'],
    'Engine_Size': [1.2, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0],
    'Fuel_Efficiency': [22.0, 18.5, 15.0, 12.5, 10.0, 8.5, 7.0]
}

df = pd.DataFrame(data)

colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'cyan']

plt.figure(figsize=(8, 6))
plt.scatter(df['Engine_Size'], df['Fuel_Efficiency'], c=colors, s=100)

for i, txt in enumerate(df['Car_Model']):
    plt.annotate(txt, (df['Engine_Size'][i] + 0.05, df['Fuel_Efficiency'][i]))

plt.title("Engine Size vs Fuel Efficiency")
plt.xlabel("Engine Size (in Litres)")
plt.ylabel("Fuel Efficiency (in km/L)")
plt.grid(True)
plt.tight_layout()
plt.show()
