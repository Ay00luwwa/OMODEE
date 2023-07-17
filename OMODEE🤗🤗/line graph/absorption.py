import csv
import matplotlib.pyplot as plt

# Read the Tetracycline1 dataset from a CSV file
with open('OMODEE🤗🤗/line graph/tetracycline1.csv', 'r') as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames
    if 'conc' not in headers:
        print("Error: 'conc' column not found in the dataset.")
        print("Headers:", headers)
        exit()

    time = []
    concentration = []
    for row in reader:
        time.append(float(row['Time']))
        concentration.append(float(row['conc']))

# Create a line plot of tetracycline concentration over time
plt.plot(time, concentration)
plt.xlabel('Time (hours)')
plt.ylabel('Tetracycline Concentration (mg/L)')
plt.title('Tetracycline Absorption Profile')
plt.show()
