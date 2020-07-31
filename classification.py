# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 21:00:52 2020

@author: Jayadev
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
import sys
import warnings
from sklearn.exceptions import DataConversionWarning
warnings.filterwarnings(action='ignore', category=DataConversionWarning)
missing_values = ['n/a', 'na', '--','-',' ']
df=pd.read_csv(sys.argv[1],header=0,na_values = missing_values)
mean=df['CGPA/ percentage'].mean()
dff=df['CGPA/ percentage'].fillna(mean)
dff=dff.to_frame()
dff1=df[['Have you worked on MySQL or Oracle database','Have you studied OOP Concepts','Programming Language Known other than Java (one major)'
                                        ,'Have you worked core Java','Degree','Major/Area of Study','Course Type'
                                        ,'Which-year are you studying in?','Areas of interest']].fillna(method='ffill',axis=1)
dff2=pd.concat([dff,dff1],axis='columns')
dff3=df[['Label','Rate your written communication skills [1-10]','Rate your verbal communication skills [1-10]']]
dff4=pd.concat([dff3,dff2],axis='columns')
dummies=pd.get_dummies(data=dff4,columns=['Have you worked on MySQL or Oracle database','Have you studied OOP Concepts','Programming Language Known other than Java (one major)'
                                        ,'Have you worked core Java','Degree','Major/Area of Study','Course Type'
                                        ,'Which-year are you studying in?','Areas of interest'])
dummies.replace('ineligible', 1, inplace=True)
dummies.replace('eligible', 0, inplace=True)
X=dummies.iloc[:,1:45]
y=dummies['Label']
sc = StandardScaler()
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3) 
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
from sklearn.ensemble import RandomForestClassifier
clf=RandomForestClassifier(n_estimators=100)
clf.fit(X_train,y_train)
y_pred=clf.predict(X_test)
print(metrics.f1_score(y_test, y_pred))


