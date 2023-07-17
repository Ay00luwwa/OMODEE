import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file and store it in tetracycline_df
tetracycline_df = pd.read_csv('OMODEE🤗🤗/Bar graph/tetracycline1.csv')

# Question 1: What is the absorption profile of tetracycline?
plt.bar(tetracycline_df['Time'], tetracycline_df['conc'])
plt.xlabel('Time (hours)')
plt.ylabel('Tetracycline Concentration (mg/L)')
plt.title('Tetracycline Absorption Profile')
plt.show()

# Question 2: How is tetracycline eliminated from the body?
plt.bar(tetracycline_df['Time'], tetracycline_df['conc'])
plt.xlabel('Time (hours)')
plt.ylabel('Tetracycline Concentration (mg/L)')
plt.title('Tetracycline Elimination Profile')
plt.show()
