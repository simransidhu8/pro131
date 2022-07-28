import csv
import pandas as pd

#read data file
df = pd.read_csv("main.csv")

radius = []
mass = []
gravity = []

del df["Unnamed: 0.1"]
del df["Unnamed: 0"]

#moving data into arrays
radius.append(df['Radius'])
mass.append(df['Mass'])

#converting measurements into SI units
def convert_to_si(radius, mass):
    for i in range(0, len(radius)-1):
        try:
            #converting mass into kilograms
            mass[i] = mass[i]*1989e+30

            #converting radius into meters
            radius[i] = radius[i]*6957e+8
        
        except: pass

convert_to_si(radius, mass)

#creating function to find gravity
def find_gravity(radius, mass):
    G = 6.67e-11
    #calculating gravity and adding it into gravity array
    for index in range(0, len(mass)):
        try:
            g = G*(mass[index])/((radius[index])**2) 
            gravity.append(g)
        
        except: pass

find_gravity(radius, mass)

#merging gravity data with column
for i in gravity:
    df["Gravity"] = gravity[0:96]
print(df)

#creating new data file
df.to_csv('star_data_with_gravity.csv')