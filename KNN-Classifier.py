import pandas as pd
import warnings

#import warnings filter
from warnings import simplefilter
#ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)

# define column names
names = ['Name', 'Label', 'U-G', 'G-R', 'R-I', 'I-Z']

# loading training data
df = pd.read_csv('all_trained.csv', header=None, names=names)
df.head()

import numpy as np

from sklearn.model_selection import train_test_split



Xa = np.array(df.iloc[:,3:5]) 	
ya = np.array(df.iloc[:,1])

Xb = np.array(df.iloc[:,2:4]) 
yb = np.array(df.iloc[:,1])

Xc = np.array(df.iloc[:,4:6]) 
yc = np.array(df.iloc[:,1])


Xa_train, Xa_test, ya_train, ya_test = train_test_split(Xa, ya, test_size=0.33, random_state=67)

Xb_train, Xb_test, yb_train, yb_test = train_test_split(Xb, yb, test_size=0.33, random_state=99)

Xc_train, Xc_test, yc_train, yc_test = train_test_split(Xc, yc, test_size=0.33, random_state=86)
from sklearn.neighbors import KNeighborsClassifier


# instantiate learning model
knn1 = KNeighborsClassifier(n_neighbors=4)
knn2 = KNeighborsClassifier(n_neighbors=3)
knn3 = KNeighborsClassifier(n_neighbors=3)




# fitting/training the model
knn1.fit(Xa_train, ya_train)
knn2.fit(Xb_train, yb_train)
knn3.fit(Xc_train, yc_train)

from sklearn.metrics import accuracy_score

pred1 = knn1.predict(Xa_test)

print(accuracy_score(ya_test,pred1))

pred2 = knn2.predict(Xb_test)

print(accuracy_score(yb_test,pred2))

pred3 = knn3.predict(Xc_test)

print(accuracy_score(yc_test,pred3))





##Training Ends
Names = ['Name', 'Label', 'U-G', 'G-R', 'R-I', 'I-Z']

# loading testing data
df2 = pd.read_csv('sdss-differences.csv', header=None, names=Names)
df2.head()

XA = np.array(df2.iloc[:200000,3:5])
XB = np.array(df2.iloc[:200000,2:4])
XC = np.array(df2.iloc[:200000,4:6])

X = np.array(df2.iloc[:,0])

NatSat=[]
Ast=[]
Com=[]

i=0
j=0

# predict the response
for i in range (0,len(XA)):
    
    pred1 = knn1.predict(XA[i:i+1,0:2])
    pred2 = knn2.predict(XB[i:i+1,0:2])
    pred3 = knn3.predict(XC[i:i+1,0:2])
    
    if pred1 == 3:
        NatSat.append(X[i])
        
    elif pred1 == 1:
        if pred2 == 1 or pred3 == 1:
            Ast.append(X[i])
        
    elif pred1 != 1:
        if pred2 == 1 and pred3 == 1:
            Ast.append(X[i])
            
        else:
            Com.append(X[i])

print('Natural Satellites: ',NatSat)
print('Comets: ',Com)
print('Asteroids: ',Ast)
