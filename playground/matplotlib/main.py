import matplotlib.pyplot as plt 
import pandas as pd

data = {
  'DiabetesePedigreeFunction': [0.2,0.4,0.6,0.8,1.0],
  'BMI': [22,25,30,28,35]
}

diabetes = pd.DataFrame(data)

plt.scatter(diabetes['DiabetesePedigreeFunction'], diabetes['BMI'])

plt.xlabel('Diabetese Pedigree Function')
plt.ylabel('BMI'
           )

plt.title('Scatter plot of DiabetesePedigreeFunction vs BMI')

plt.show()