'''
We will embark on a journey to recreate the groundbreaking work of Dr. Ignaz Semmelweis, 
a Hungarian physician who revolutionized hygiene practices in the mid-1800s. Prior to this time, 
hygiene was neglected, leading to numerous deaths, particularly in hospitals where doctors didn't 
wash their hands before surgeries. Driven by the high mortality rates, Dr. Semmelweis investigated 
the situation in Vienna general hospital and discovered a shocking disparity between Clinic 1 and Clinic 2. 
Through data analysis, he realized that medical students who frequented the autopsy room were unknowingly 
spreading harmful bacteria, causing deadly childbed fever among women giving birth. Our task is to use 
Python to recreate the steps taken by Dr. Semmelweis, enabling us to appreciate the importance of his 
work and the profound impact that simple actions can have on saving lives.

By Simon Tran
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in the yearly dataset
yearly_df = pd.read_excel("Python-Projects-The-Discovery-of-Handwashing\yearly_deaths_by_clinic.xlsx") # copy relative path
print(yearly_df)

# Let's examine the dataset
yearly_df.shape # this gives me the dimension of row x column
yearly_df.info()

yearly_df.groupby("clinic") ["deaths"].sum() # this summarizes the total number of deaths from 1841-1846 for clinics 1 and 2
yearly_df.groupby("clinic") ["births"].sum() # this summarizes the total number of births from 1841-1846 for clinics 1 and 2

# To make the analysis easier, we can calculate the proportion of deaths.
yearly_df["Proportion of Deaths"] = yearly_df["deaths"] / yearly_df["births"]
yearly_df

# Separate the dataset into 2 datasets, one for each clinic
clinic_1 = yearly_df[yearly_df["clinic"] == "clinic 1"]
clinic_2 = yearly_df[yearly_df["clinic"] == "clinic 2"]

# Visualize the Number of deaths from 1841-1846 in clinic 1
fig,ax = plt.subplots(figsize = (10,4))
plt.bar(clinic_1.year, clinic_1.deaths, width= 0.6, color= "red")
plt.title("Clinic 1: Number of Deaths per Year", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Number of Deaths", fontsize=14)
plt.show()

# Visualize the Number of deaths from 1841-1846 in clinic 2
fig,ax = plt.subplots(figsize = (10,4))
plt.bar(clinic_2.year, clinic_2.deaths, width= 0.6, color= "green")
plt.title("Clinic 2: Number of Deaths per Year", fontsize=16)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Number of Deaths", fontsize=14)
plt.show()

# Visualize the proportions of deaths for both clincs 1 and 2
ax = clinic_1.plot(x= "year", y= "Proportion of Deaths", label= "clinic_1", color="red")
clinic_2.plot(x= "year", y= "Proportion of Deaths", label= "clinic_2", ax=ax, ylabel= "Proportion of Deaths", color="green")
plt.show()

'''
By looking further into why this happened, Dr Semmelweis realized that many medical students 
worked at clinic 1 who also as a part of their study, spend a lot of time in the autopsy room. 
So, he realized that dealing with corpses spread bacteria that would be transferred to the women giving birth, 
infecting them with the deadly childbed fever, which was the main reason for the high mortality rates. 
'''

# Read in the monthly dataset
monthly_df = pd.read_excel("Python-Projects-The-Discovery-of-Handwashing\monthly_deaths.xlsx")
monthly_df.head(5)
monthly_df.info()

# Calculate the proportion of deaths per month
monthly_df["Proportion of Deaths"]= monthly_df["deaths"] / monthly_df["births"]
monthly_df.head(5)

'''
Dr Semmelweis ordered the doctors to wash their hands and made it obligatory in the summer of 1847
to see if that will affect the number of deaths, and since we have the monthly data now, we can trace 
the number of deaths before and after the handwashing started. 
'''
# Change the data type of "date" column from string to datatime
monthly_df.dtypes
monthly_df['date'] =  pd.to_datetime(monthly_df['date'])

# Label the date at which handwashing started to "start_handwashing"
start_handwashing = pd.to_datetime('1847-06-01')

# Split monthly into before and after handwashing_start
before_washing = monthly_df[monthly_df["date"] < start_handwashing]
after_washing = monthly_df[monthly_df["date"] >= start_handwashing]

# Let's plot the before handwashing
fig,ax = plt.subplots(figsize = (10,4))
x= before_washing["date"]
y= before_washing["Proportion of Deaths"]
plt.plot(x, y, color= "orange")
plt.title("Before Handwashing", fontsize=16)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Proportion of Deaths", fontsize=14)
plt.show()

# Let's plot the after handwashing
fig,ax = plt.subplots(figsize = (10,4))
x= after_washing["date"]
y= after_washing["Proportion of Deaths"]
plt.plot(x, y, color= "purple")
plt.title("After Handwashing", fontsize=16)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Proportion of Deaths", fontsize=14)
plt.show()

# Let's combined the two plots to see the difference
ax = before_washing.plot(x= "date", y= "Proportion of Deaths", label= "Before Handwashing", color="orange")
after_washing.plot(x= "date", y= "Proportion of Deaths", label= "After Handwashing", ax=ax, ylabel= "Proportion deaths", color="purple") 
plt.show()

'''
The difference is pretty clear! the proportion of 
deaths dramatically decreased after handwashing was made obligatory.
'''

# Let's calculate how much did handwashing decreased the proportion of deaths on average
before_proportion = before_washing["Proportion of Deaths"]
after_proportion = after_washing["Proportion of Deaths"]
before_proportion.mean()
after_proportion.mean()

# Calculate the difference between both proportions
mean_diff = after_proportion.mean() - before_proportion.mean()
mean_diff

'''
The minus sign indicates that there is a decrease. 
So handwashing decreased the proportion of deaths from 10.5% to 2.1% i.e, by approximately 8.4%.
'''

# End of Code