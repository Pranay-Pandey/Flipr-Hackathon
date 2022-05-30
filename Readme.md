# Measuring Heart Rhythm Disorders

The most common way of analysing the functioning of a heart is to do an Electrocardiogram
(ECG) measurement. This ECG reading is used by cardiologists to identify heart rhythm disorders
and other abnormalities. For example, ECGs are commonly used to detect the presence of
arrhythmias in patients. If present and not treated in time, these arrhythmias can lead to stroke
and possibly heart failure. 

  
In this task, we focus on a very common arrhythmia called Atrial Fibrillation (AF) that occurs in
1-2% of the population (5-10% of the population older than 60 years). It’s a type of irregular
heartbeat that can lead to blood clots, stroke, heart failure and other heart-related complications.
About 15–20% of people who have strokes have AF.
  
 
## Problem Statement

   ECG data that is classified into two parts: Normal and AF.
Objective is to learn a model that classifies the ECG recording correctly into one of the two
categories. Smartwatches such as an Apple watch also use a similar algorithm to detect AF in
ECG data measured through the watch.
     
     
  Model is trained on ECG recordings sampled at 300 Hz.
     
     
  ## Identifing the relevant ECG features.
    
An ECG reading has many features. The statistics of the RR intervals such as its average, standard deviation, RMSSD, etc.
are important parameters in determining the fitness of the heart.
     
Python library <b><a href = 'https://python-heart-rate-analysis-toolkit.readthedocs.io/en/latest/'>Heartpy</a></b> is used for this purpose. 
       
It can extract more than 20 ECG features from the ECG data.
       
     
     
     

  
 
