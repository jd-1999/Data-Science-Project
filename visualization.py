# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 21:21:29 2020

@author: Jayadev
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from matplotlib.backends.backend_pdf import PdfPages
import sys
missing_values = ['n/a', 'na', '--','-',' ']
df=pd.read_csv(sys.argv[1],na_values = missing_values)
df2=df[df['Areas of interest']=='Data Science '] 
df11=df2['Programming Language Known other than Java (one major)']=='Python'
df11=df11.to_frame()
df3=df[df['Which-year are you studying in?']=='Fourth-year']
df4=df3['CGPA/ percentage']>8.0
df5=df4.to_frame()
df6=df[df['Areas of interest']=='Digital Marketing ']
df7=df6['Rate your written communication skills [1-10]']>8
df8=df6['Rate your verbal communication skills [1-10]']>8
df7=df7.to_frame()
df8=df8.to_frame()
df9=pd.concat([df7,df8],axis='columns')
df10=(df9['Rate your written communication skills [1-10]'])&(df9['Rate your verbal communication skills [1-10]'])
df10=df10.to_frame()
df2=df[df['Areas of interest']=='Data Science '] 
df11=df2['Programming Language Known other than Java (one major)']=='Python'
df11=df11.to_frame()
df12=df
with PdfPages('visualization-output.pdf') as pdf:
    figu=plt.figure(figsize=(10,8))
    ax = sns.countplot(x='Areas of interest', data=df)	
    ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha='right')
    ax.set_ylabel('Number of students')
    plt.title('The number of students applied to different technologies')
    plt.tight_layout()
    pdf.savefig(figu)
    plt.close()
    figu=plt.figure(figsize=(10,8))
    ax = sns.countplot(x='Programming Language Known other than Java (one major)', data=df11)
    plt.title('Students who applied for Data science and knew python')
    ax.set(xlabel='Do you know Python?',ylabel='Number of students')
    ax.set(xticklabels=['No','Yes'])
    pdf.savefig(figu)
    plt.close()
    figu=plt.figure(figsize=(10,8))
    ax = sns.countplot(x='How Did You Hear About This Internship?', data=df)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha='right')
    ax.set_ylabel('Number of students')
    plt.title('Different ways student learned about this program')
    plt.tight_layout()
    pdf.savefig(figu)
    plt.close()
    figu=plt.figure()
    ax = sns.countplot(x='CGPA/ percentage', data=df5)
    ax.set(xticklabels=['No','Yes'])
    plt.title('Students in fourth-year who have CGPA>8')
    ax.set(xlabel='CGPA')
    pdf.savefig(figu)
    plt.close()
    figu=plt.figure(figsize=(10,8))
    ax = sns.countplot(x=df10.iloc[:,0] )
    plt.title('Students who applied for Digital Marketing and had verbal and written communication greater than 8')
    ax.set(xlabel='Is the marks in verbal and written communication >8')
    ax.set(xticklabels=['No','Yes'])
    pdf.savefig(figu)
    plt.close()
    figu=plt.figure(figsize=(15,10))
    ax = sns.countplot(x='Areas of interest', data=df,hue='Which-year are you studying in?')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")	
    ax.set_ylabel('Number of students')
    plt.title('Year and area wise classification')
    plt.tight_layout()
    pdf.savefig(figu)
    plt.close()
    figu=plt.figure(figsize=(15,8))
    ax = sns.countplot(x='College name', data=df)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
    ax.set_xlabel('College name',fontsize=18)
    ax.set_ylabel('Number of students',fontsize=18)
    plt.title('College wise classification')
    plt.tight_layout()  
    pdf.savefig(figu)
    plt.close()
    figu=plt.figure()
    ax = sns.countplot(x='City', data=df)
    ax.set_ylabel('Number of students')
    plt.title('City wise classification')
    plt.tight_layout()
    pdf.savefig(figu)
    plt.close()
    labelencoder = LabelEncoder()
    df12['Areas of interest'] = labelencoder.fit_transform(df12['Areas of interest'])
    df12['Which-year are you studying in?']=labelencoder.fit_transform(df12['Which-year are you studying in?'])
    df12['Major/Area of Study']=labelencoder.fit_transform(df12['Major/Area of Study'])
    figu=plt.figure()
    sns.boxplot(x='Label',y='CGPA/ percentage',data=df12)
    plt.title('Relationship between CGPA and target variable')
    pdf.savefig(figu)
    plt.close()
    figu=plt.figure()
    sns.boxplot(x='Label',y='Areas of interest',data=df12)
    plt.title('Relationship between Area of interest and target variable')
    pdf.savefig(figu)
    plt.close()
    figu=plt.figure()
    sns.boxplot(x='Label',y='Which-year are you studying in?',data=df12)
    plt.title('Relationship between Year of Study and target variable')
    pdf.savefig(figu)
    plt.close() 
    figu=plt.figure()
    sns.boxplot(x='Label',y='Major/Area of Study',data=df12)
    plt.title('Relationship between Major and target variable')
    pdf.savefig(figu)
    plt.close() 
    
    
    
    