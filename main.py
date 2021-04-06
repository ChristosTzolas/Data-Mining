import pandas as pd
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns

# Data Analysis

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Create a dataframe for the healthcare dataset

patients_header = ['id', 'gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status', 'stroke']
patients = pd.read_csv('healthcare-dataset-stroke-data\healthcare-dataset-stroke-data.csv', sep=',', names=patients_header, 
                     usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], encoding="ISO-8859-1", low_memory=False, header=0)

# Print basic info regarding our data (characteristics and possible values)

print("\n************ Data Analysis ************\n")

print("The characteristics in our dataset are:\n")
for col in patients.columns:
    print(col)
# or print(patients.columns)    
print(f"\nSpecifically, there are {len(patients.id.unique())} unique patient ids in the data, of {len(patients.age.unique())} different ages.\n")

print("Regarding the possible values of the characteristics, those are:\n")
print(f"Genders: {(patients.gender.unique())}")
print(f"Work types: {(patients.work_type.unique())}")
print(f"Resident types: {(patients.Residence_type.unique())}")
print(f"Smoking statuses: {(patients.smoking_status.unique())}")
print(f"BMI range: {min(patients.bmi.unique())} - {max(patients.bmi.unique())}")
print(f"Average glucose levels range: {min(patients.avg_glucose_level.unique())} - {max(patients.avg_glucose_level.unique())}\n")
print("(The rest of the characteristics have binary values)\n\nSummary Statistics:\n")

# print summary statistics
print(patients.describe(), "\n")

# Count gender instances
print("Gender Distribution:\n")
print(patients['gender'].value_counts(), "\n")

print("Mean: {}".format(patients['age'].mean()))
print("Median: {}".format(patients['age'].median()), "\n")
print("Most common ages:\n")
print(patients['age'].value_counts().head(10), "\n")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Correlation between smoking and strokes

# Stroke occurencies among smoking types 
# We may need to change 0s and 1s to Had/Hadn't Stroke
for i in patients['smoking_status'].unique():
     print("Smoking Status: {}\nStroke Occurence:\n{}\n".format(i, patients[patients['smoking_status']==i]['stroke'].value_counts().head(2)))

print("Stroke frequency of all patients:")
print(patients['stroke'].value_counts(), "\n")

# Make a graph too

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Copy dataset to change data (round ages, bmi, glucose levels)

better_patients = patients.copy()
better_patients['age'] = better_patients['age'].round(-1)
better_patients['avg_glucose_level'] = better_patients['avg_glucose_level'].round(-1)
better_patients['bmi'] = better_patients['bmi'].round(-1)
# Save to csv
better_patients.to_csv("better_dataset.csv")

# Plot some graphs about the patients (display frequency of characteristics)

# patients['gender'].value_counts().plot.bar()
# plt.show()
sns.countplot(better_patients['gender'])
plt.show()

# better_patients['age'].value_counts().plot.bar()
# plt.show()
sns.countplot(better_patients['age'])
plt.show()

sns.countplot(better_patients['hypertension'])
plt.show()
sns.countplot(better_patients['heart_disease'])
plt.show()
sns.countplot(better_patients['ever_married'])
plt.show()
sns.countplot(better_patients['work_type'])
plt.show()
sns.countplot(better_patients['Residence_type'])
plt.show()
sns.countplot(better_patients['avg_glucose_level'])
plt.show()
sns.countplot(better_patients['bmi'])
plt.show()
sns.countplot(better_patients['smoking_status'])
plt.show()
sns.countplot(better_patients['stroke'])
plt.show()

# plt.plot(patients.age, patients.bmi)

# plt.xlabel('Ages')
# plt.ylabel('BMI')
# plt.show()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# How to replace display cols:
# # mappings to standardize and clean the values
# mappings = {'MALE' : 'Male', 'FEMALE' : 'Female', 'Male(Child)' : 'Boy', 'Female(Child)' : 'Girl'}
# # replace values using the defined mappings
# data['SEX'] = data['SEX'].replace(mappings)
# data['SEX'].value_counts()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------