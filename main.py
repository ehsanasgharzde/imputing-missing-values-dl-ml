########## Importing required libraries
import pandas
import seaborn
from random import choice
from matplotlib import pyplot
from sklearn.linear_model import LinearRegression

########## It's not unused! It's simply permission to use the next library
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer


########## Loading AMR-NSH-Buoy-Data1394.xls files in a Pandas DataFrame and getting a copy
dataset = pandas.read_excel("AMR-and-NSH-Buoy-Data1394.xls")

########## Finding the number of missing values for every column
print(dataset.isnull().sum())

########## Univariate:
########## Median, Mean, Mode

########## Analyse the data in non-time columns
########## Buoy Amirabad Battery Voltage(1)
figure, axus = pyplot.subplots(figsize=(10, 10))
seaborn.distplot(dataset["Buoy Amirabad Battery Voltage(1)"])


########## Loading AMR-NSH-Buoy-Data1394.xls files in a Pandas DataFrame and getting a copy
mediandataset = pandas.read_excel("AMR-and-NSH-Buoy-Data1394.xls")

########## Replacing the missing values with the median value of each column
for index in range(2, len(dataset.columns)):
    mediandataset[dataset.columns[index]].fillna(dataset[dataset.columns[index]].median(), inplace=True)
    
########## Finding the number of missing values for every column
# print(mediandataset.isnull().sum())

########## Analyse the data in non-time columns
########## Buoy Amirabad Battery Voltage(1)
figure, axus = pyplot.subplots(figsize=(10, 10))
seaborn.distplot(mediandataset["Buoy Amirabad Battery Voltage(1)"])


########## Creating a csv file
# mediandataset.to_csv("univariate-method-results/AMR-and-NSH-Buoy-Data1394-median.csv")


########## Loading AMR-NSH-Buoy-Data1394.xls files in a Pandas DataFrame and getting a copy
meandataset = pandas.read_excel("AMR-and-NSH-Buoy-Data1394.xls")

########## Replacing the missing values with the mean value of each column
for index in range(2, len(dataset.columns)):
    meandataset[dataset.columns[index]].fillna(dataset[dataset.columns[index]].mean(), inplace=True)

########## Finding the number of missing values for every column
# print(meandataset.isnull().sum())

########## Analyse the data in non-time columns
########## Buoy Amirabad Battery Voltage(1)
figure, axus = pyplot.subplots(figsize=(10, 10))
seaborn.distplot(meandataset["Buoy Amirabad Battery Voltage(1)"])

########## Creating a csv file
# meandataset.to_csv("univariate-method-results/AMR-and-NSH-Buoy-Data1394-mean.csv")


########## Loading AMR-NSH-Buoy-Data1394.xls files in a Pandas DataFrame and getting a copy
modedataset = pandas.read_excel("AMR-and-NSH-Buoy-Data1394.xls")

########## Replacing the missing values with the mode value of each column
for index in range(2, len(dataset.columns)):
    modedataset[dataset.columns[index]].fillna(dataset[dataset.columns[index]].mode(), inplace=True)

########## Finding the number of missing values for every column
# print(modedataset.isnull().sum())

########## Analyse the data in non-time columns
########## Buoy Amirabad Battery Voltage(1)
figure, axus = pyplot.subplots(figsize=(10, 10))
seaborn.distplot(modedataset["Buoy Amirabad Battery Voltage(1)"])


########## Creating a csv file
# modedataset.to_csv("univariate-method-results/AMR-and-NSH-Buoy-Data1394-mode.csv")



########## Multivariate:
    
########## MICE Algorithm (Recommanded)
########## Multivariate Imputation by Chained Equations Algorithm
########## Links to Additional Readings:
########## https://www.numpyninja.com/post/mice-algorithm-to-impute-missing-values-in-a-dataset
########## https://scikit-learn.org/stable/modules/impute.html#iterative-imputer

########## KNN Algorithm (Not Recommanded)
########## K-Nearest Neighbors Algorithm
########## Links to Additional Readings:
########## https://www.mygreatlearning.com/blog/knn-algorithm-introduction/

########## Simple if/else method following the datetime pattern in the dataset
########## to Impute "DateTime Processor" and "SunDateTime" (Recommanded)

########## for NaT values we can design an AI to learn the pattern how the date and time
########## are changing then apply it to NaT values (Not Recommanded)

########## Loading AMR-NSH-Buoy-Data1394.xls files in a Pandas DataFrame and getting a copy
micedataset = pandas.read_excel("AMR-and-NSH-Buoy-Data1394.xls")

########## Slicing out "DateTime Processor" and "SunDateTime"
gregdatetime = pandas.Series(micedataset["DateTime Processor"])
solardatetime = pandas.Series(micedataset["SunDateTime"])

########## Setting all the rows all over again
########## Gregorian date and time for "DateTime Processor"
DAY2MONTH = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,       
    5: 31,
    6: 30,       
    7: 31,       
    8: 31,       
    9: 30,       
    10: 31,  
    11: 30,       
    12: 31,            
}

YEAR = 2015
MONTH = 3
DAY = 20

HOUR = 21

for index in range(len(gregdatetime)):
    SECOND = choice([11, 10, 9, 6, 5, 8])
    
    if HOUR > 23:
        DAY += 1
        HOUR = 0
    
    if DAY2MONTH[MONTH] < DAY:
        MONTH += 1
        DAY = 1
        
    if MONTH > 12:
        YEAR += 1
        MONTH = 1
        
    if SECOND < 10:
        secondstr = f"0{SECOND}"
    else:
        secondstr = f"{SECOND}"
        
    if HOUR < 10:
        hourstr = f"0{HOUR}"
    else:
        hourstr = f"{HOUR}"
        
    if DAY < 10:
        daystr = f"0{DAY}"
    else:
        daystr = f"{DAY}"
        
    if MONTH < 10:
        monthstr = f"0{MONTH}"
    else:
        monthstr = f"{MONTH}"
        
        
    datetimestr = f"{YEAR}-{monthstr}-{daystr} {hourstr}:00:{secondstr}"
    
    gregdatetime[index] = datetimestr
    
    HOUR += 1

########## Solar date and time for "SunDateTime"
DAY2MONTH = {
    1: 31,
    2: 31,
    3: 31,
    4: 31,       
    5: 31,
    6: 31,       
    7: 30,       
    8: 30,       
    9: 30,       
    10: 30,  
    11: 30,       
    12: 29,            
}

YEAR = 1394
MONTH = 1
DAY = 1

HOUR = 1

for index in range(len(solardatetime)):
    SECOND = choice([11, 10, 9, 6, 5, 8])
    
    if HOUR > 23:
        DAY += 1
        HOUR = 0
    
    if DAY2MONTH[MONTH] < DAY:
        MONTH += 1
        DAY = 1
        
    if MONTH > 12:
        YEAR += 1
        MONTH = 1
        
    if SECOND < 10:
        secondstr = f"0{SECOND}"
    else:
        secondstr = f"{SECOND}"
        
    if HOUR < 10:
        hourstr = f"0{HOUR}"
    else:
        hourstr = f"{HOUR}"
        
    if DAY < 10:
        daystr = f"0{DAY}"
    else:
        daystr = f"{DAY}"
        
    if MONTH < 10:
        monthstr = f"0{MONTH}"
    else:
        monthstr = f"{MONTH}"
        
        
    datetimestr = f"{YEAR}-{monthstr}-{daystr} {hourstr}:30:{secondstr}"
        
    solardatetime[index] = datetimestr
    
    HOUR += 1
    

timeseriesdataset = pandas.concat([gregdatetime, solardatetime], axis=1)


########## Dropping "DateTime Processor" and "SunDateTime"
micedataset = micedataset.drop(["DateTime Processor", "SunDateTime"], axis=1)
micecolumns = micedataset.columns

########## Setting linearregression and iterativeimputer
linreg = LinearRegression()
iterimp = IterativeImputer(estimator=linreg, max_iter=5000, tol=1e-12, verbose=2, imputation_order="roman")

########## Activating the iterativeimputer
micevalues = iterimp.fit_transform(micedataset)

########## Creating the micedataset again
micedataset = pandas.DataFrame(micevalues)
micedataset.columns = micecolumns

########## Combining the micedataset and timeseriesdataset
micedataset = pandas.concat([timeseriesdataset, micedataset], axis=1)

########## Finding the number of missing values for every column
print(micedataset.isnull().sum())

########## Analyse the data in non-time columns
########## Buoy Amirabad Battery Voltage(1)
figure, axus = pyplot.subplots(figsize=(10, 10))
seaborn.distplot(micedataset["Buoy Amirabad Battery Voltage(1)"])


########## Creating a csv file
micedataset.to_csv("multivariate-method-results/AMR-and-NSH-Buoy-Data1394-mice.csv")