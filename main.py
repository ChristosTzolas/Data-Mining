import pandas as pd
import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns

# Data Analysis #

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Create a dataframe for the healthcare dataset

healthcare_header = ['id', 'gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status', 'stroke']
healthcare = pd.read_csv('healthcare-dataset-stroke-data\healthcare-dataset-stroke-data.csv', sep=',', names=healthcare_header, 
                     usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], encoding="ISO-8859-1", low_memory=False, header=0)

# Print basic info regarding our data (characteristics and possible values)

print("\n************ Data Analysis ************\n")

print("The characteristics in our dataset are:\n")
for col in healthcare.columns:
    print(col)
# Alternatively:
# print(healthcare.columns)    
print(f"\nSpecifically, there are {len(healthcare.id.unique())} unique ids in the data, of {len(healthcare.age.unique())} different ages.\n")

print("Regarding the possible values of the characteristics, those are:\n")
print(f"Genders: {(healthcare.gender.unique())}")
print(f"Work types: {(healthcare.work_type.unique())}")
print(f"Resident types: {(healthcare.Residence_type.unique())}")
print(f"Smoking statuses: {(healthcare.smoking_status.unique())}")
print(f"BMI range: {min(healthcare.bmi.unique())} - {max(healthcare.bmi.unique())}")
print(f"Average glucose levels range: {min(healthcare.avg_glucose_level.unique())} - {max(healthcare.avg_glucose_level.unique())}\n")
print("(The rest of the characteristics have binary values)\n\nSummary Statistics:\n")

# Summary statistics
print(healthcare.describe(), "\n")
# Count gender instances
print("Gender Distribution:\n")
print(healthcare['gender'].value_counts(), "\n")
# Output mean and median age 
print("Mean age of the dataset: {}".format(healthcare['age'].mean()))
print("Median age of the dataset: {}".format(healthcare['age'].median()), "\n")
# Output the top 10 ages present in the dataset
print("Most common ages:\n")
print(healthcare['age'].value_counts().head(10), "\n")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Correlation between smoking and strokes

# # Stroke occurencies among smoking types 
# for i in healthcare['smoking_status'].unique():
#      print("Smoking Status: {}\nStroke Occurence:\n{}\n".format(i, healthcare[healthcare['smoking_status']==i]['stroke'].value_counts().head(2)))

print("Stroke frequency for all the patients:")
print(healthcare['stroke'].value_counts(), "\n")

test_healthcare = healthcare.copy()
test_healthcare.drop(columns=['hypertension','age','id','gender','heart_disease','ever_married', 'work_type', 'Residence_type', 'avg_glucose_level', 'bmi'], inplace=True)
strokers = test_healthcare[test_healthcare['stroke']==1]
non_strokers = test_healthcare[test_healthcare['stroke']==0]
strokers = pd.DataFrame(strokers)
non_strokers = pd.DataFrame(non_strokers)
print("*** Correlation between smoking and strokes ***\n\nPeople who had a stroke:")
print(strokers['smoking_status'].value_counts(),"\n")
print("People who hadn't a stroke:")
print(non_strokers['smoking_status'].value_counts(),"\n")

all_boyz = [strokers, non_strokers]
good_data = pd.concat(all_boyz)
sns.catplot(x="smoking_status", y="stroke", kind="bar",data=good_data)

plt.title('Correlation between smoking types and strokes', fontsize=14)
plt.xlabel('Smoking Status', fontsize=14)
plt.ylabel('Percentage of Strokes (%)', fontsize=14)
plt.show()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Copy dataset to change data (round the ages, bmi, glucose levels)

better_healthcare = healthcare.copy()
better_healthcare['age'] = better_healthcare['age'].round(-1)
better_healthcare['avg_glucose_level'] = better_healthcare['avg_glucose_level'].round(-1)
better_healthcare['bmi'] = better_healthcare['bmi'].round(-1)
# Save to csv
better_healthcare.to_csv("better_dataset.csv")

# # Plot some graphs about the healthcare (display frequency of characteristics)

# # healthcare['gender'].value_counts().plot.bar()
# # plt.show()
# sns.countplot(better_healthcare['gender'])
# plt.show()

# # better_healthcare['age'].value_counts().plot.bar()
# # plt.show()
# sns.countplot(better_healthcare['age'])
# plt.show()

# # Add plot settings
# sns.countplot(better_healthcare['hypertension'])
# plt.show()
# sns.countplot(better_healthcare['heart_disease'])
# plt.show()
# sns.countplot(better_healthcare['ever_married'])
# plt.show()
# sns.countplot(better_healthcare['work_type'])
# plt.show()
# sns.countplot(better_healthcare['Residence_type'])
# plt.show()
# sns.countplot(better_healthcare['avg_glucose_level'])
# plt.show()
# sns.countplot(better_healthcare['bmi'])
# plt.show()
# sns.countplot(better_healthcare['smoking_status'])
# plt.show()
# sns.countplot(better_healthcare['stroke'])
# plt.show()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# [ Random notes - Delete later ]

# # How to replace display cols: with mappings to standardize and clean the values
# mappings = {'MALE' : 'Male', 'FEMALE' : 'Female', 'Male(Child)' : 'Boy', 'Female(Child)' : 'Girl'}
# # replace values using the defined mappings
# data['gender'] = data['gender'].replace(mappings)
# data['gender'].value_counts()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------