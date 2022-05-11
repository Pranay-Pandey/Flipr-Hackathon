#importing libraries
import heartpy as hp
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#the model
def model():
    
    dataset = pd.read_csv('ECG_training.csv')
    test_data = pd.read_csv('ECG_testing.csv')
    
    #ecgdata contains all the input data from the dataset
    ecgdata = []
    ecgtestdata = []
    
    #Y is the classification column for the dataset
    Y = []
    Y = dataset['Classification']
    y_test = test_data['Classification'] 
    
    ecg_reading = dataset['ECG']
    ecg_test_reading = test_data['ECG'] 
    
    #getting all the ecg data from the dataset to ecgdata
    for i in range(len(ecg_reading)):
        ecg = ecg_reading[i]
        ecg = ecg.split(',')
        ecg = [int(j) for j in ecg]
        ecgdata.append(ecg)
        
    #for test data
    for i in range(len(ecg_test_reading)):
        ecg = ecg_test_reading[i]
        ecg = ecg.split(',')
        ecg = [int(j) for j in ecg]
        ecgtestdata.append(ecg)
        
        
        
    # making dataframe for the features to be extracted frgom the ecg data
    X = pd.DataFrame()
    X_test = pd.DataFrame()
    
    
    #Extracting features
    for i in range(len(ecgdata)):


        k = [120,121,139,604,825,1112,1355,1847,1975,2071,2103,2305,2306,2448,2504,2599,2640,2981,3201,3325] 
                    # Rows of data where the noise is too high and their exclusion improves the accuracy
        if(i in k):
            continue


        ecg = ecgdata[i]
        ecg = np.nan_to_num(ecg)
        working_data, measures = hp.process(ecg, 300.0)
        df_dictionary = pd.DataFrame([measures])
        X = pd.concat([X, df_dictionary], ignore_index=True)
        
    #The extracted features = X
    k = [120,121,139,604,825,1112,1355,1847,1975,2071,2103,2305,2306,2448,2504,2599,2640,2981,3201,3325]
    for i in k:
        Y.pop(i)
        
        
    
    #for Test data
    for i in range(len(ecgtestdata)):

        ecg = ecgtestdata[i]
        ecg = np.nan_to_num(ecg)
        working_data, measures = hp.process(ecg, 300.0)
        df_dictionary = pd.DataFrame([measures])
        X_test = pd.concat([X, df_dictionary], ignore_index=True)
        
    
    
    
    
   
    # Removing the Nan data
    from sklearn.impute import SimpleImputer
    imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
    imputer = imputer.fit(X)

    X = imputer.transform(X)
    
    imputer2 = SimpleImputer(missing_values=np.nan, strategy='mean')
    imputer2 = imputer.fit(X_test)

    X_test = imputer.transform(X_test)
    
    
    #Using Sklearn Random Forest Classifier for Binary Classification
    from sklearn.ensemble import RandomForestClassifier
    rf = RandomForestClassifier()
    rf.fit(X,Y)
    
    #predictions
    predictions = rf.predict(X_test)

    from sklearn.metrics import f1_score
    print(f1_score(y_test,predictions,pos_label='N'))


model()
