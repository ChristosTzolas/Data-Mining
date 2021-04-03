import pandas as pd
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

# Data Analysis

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Create a dataframe for the healthcare dataset

patients_header = ['id', 'gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status', 'stroke']
patients = pd.read_csv('healthcare-dataset-stroke-data\healthcare-dataset-stroke-data.csv', sep=',', names=patients_header, 
                     usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], encoding="ISO-8859-1", low_memory=False, header=0)

# Print basic info regarding our data (characteristics and possible values)

print("The characteristics in our dataset are:\n")
for col in patients.columns:
    print(col)

print(f"\nSpecifically, there are {len(patients.id.unique())} unique patient ids in the data, of {len(patients.age.unique())} different ages.\n")

print("Regarding the possible values of these characteristics, those are:\n")
print(f"Genders: {(patients.gender.unique())}")
print(f"Work types: {(patients.work_type.unique())}")
print(f"Resident types: {(patients.Residence_type.unique())}")
print(f"Smoking statuses: {(patients.smoking_status.unique())}")
print(f"BMI range: {min(patients.bmi.unique())} - {max(patients.bmi.unique())}")
print(f"Average glucose levels range: {min(patients.avg_glucose_level.unique())} - {max(patients.avg_glucose_level.unique())}")
print("(The rest of the characteristics have binary values)")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Plot some graphs about the patients (display frequency of characteristics)

plt.plot(patients.age, patients.bmi)

plt.xlabel('Ages')
plt.ylabel('BMI')
plt.show()