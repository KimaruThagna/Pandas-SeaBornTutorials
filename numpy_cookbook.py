'''
HANDY NUMPY UTILITIES ESPECIALLY FOR DATA SCIENCE
READING CSVs WITH NUMPY IS ONLY ADVISABLE IF THE DATA SET HAS COLUMNS THAT ARE PURELY NUMBERS
'''

import numpy as np
#numpy sorting
unsorted_fruits=np.array(['banana','mango','apple','tomato','sugarcane'])
sorted_fruits=unsorted_fruits[np.argsort(unsorted_fruits)]
#np.argsort(unsorted_fruits) returns a list of indices in the sorted order
print(sorted_fruits)

# expand dimensions, i,e making a 1D become 2D
oneD=np.array([1,2,3,4])
twoD=np.expand_dims(oneD,axis=0)
print(oneD,twoD)
# combine 2 arrays along the 0 axis
arr2=np.array([10,20,30,40])
combined = np.concatenate([oneD,arr2],axis=0)
print(combined)
print(np.column_stack(combined) )#takes an ndarray as columns to form a 2d array
#read from csv using numpy
redWine=np.genfromtxt('winequality-red.csv',delimiter=',',skip_header=True)
# boolean indexing
print(redWine[2])
a=np.array([80,45,60,12,0,100])
a_boolean=a>50#.........will return a list of true false values with True where
# an item of a satisfies the condition
print(a_boolean)
print(a[a_boolean])#---creates an array of values that were true
fixed_acidity=redWine[ :,0]# pick all rows from column 0
# january_bool = pickup_month == 1
acidity_bool=fixed_acidity>5
above5=acidity_bool[acidity_bool]
print(above5.shape[0])# number of rows returned
#ASSUME A DATASET CALLED nyctaxis
# column 7 is distance(miles) column 8 is time of travel in seconds
# trip_mph = taxi[:,7] / (taxi[:,8] / 3600) find the speed in mph
# cleaned_taxi only comprises of rows where trip_mph is <100
# cleaned_taxi=taxi[trip_mph<100]
# taxi = np.genfromtxt('nyctaxis.csv', delimiter=',', skip_header=1) this skips the column-headers


# boolean indexing in image thresholding eg if  threshold_val=100
# img=nd.array (img_as_pixel_array)
# new_img=img[img>threshold_val]
