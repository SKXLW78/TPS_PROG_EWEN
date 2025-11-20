#!/usr/bin/env python
# coding: utf-8

# In[1]:


def calcul_moyenne_numpy(coefficients, notes):
    coefficients = np.average(coefficients)
    notes = np.average(notes)
    moyenne = np.average(notes, weights=coefficients)
    return moyenne

coef_ue1={
    'R101':10,'R102':10,'R103':7,'R104':7,'R105':0,'R106':5,'R107':0,'R108':6,'R109':0,
    'R110':5,'R111':4,'R112':2,'R113':5,'R114':5,'R115':0,'SAE11':20,'SAE12':20,'SAE13':0,
    'SAE14':0,'SAE15':0,'SAE16':7,
}
coef_ue2={
    'R101':4,'R102':0,'R103':2,'R104':8,'R105':6,'R106':0,'R107':0,'R108':0,'R109':0,
    'R110':5,'R111':5,'R112':2,'R113':9,'R114':9,'R115':3,'SAE11':0,'SAE12':0,'SAE13':29,
    'SAE14':0,'SAE15':0,'SAE16':7,
}
coef_ue3={
    'R101':4,'R102':0,'R103':2,'R104':0,'R105':0,'R106':5,'R107':15,'R108':6,'R109':4,
    'R110':5,'R111':5,'R112':2,'R113':0,'R114':0,'R115':3,'SAE11':0,'SAE12':0,'SAE13':0,
    'SAE14':20,'SAE15':20,'SAE16':7,
}

note_ue1={
    'R101':12,'R102':12,'R103':12,'R104':4,'R105':0,'R106':14,'R107':0,'R108':9,'R109':0,
    'R110':12,'R111':9,'R112':12,'R113':7,'R114':12,'R115':0,'SAE11':1,'SAE12':5,'SAE13':0,
    'SAE14':0,'SAE15':0,'SAE16':13,
}
note_ue2={
    'R101':12,'R102':0,'R103':12,'R104':4,'R105':6,'R106':0,'R107':0,'R108':0,'R109':0,
    'R110':12,'R111':9,'R112':12,'R113':7,'R114':12,'R115':13,'SAE11':0,'SAE12':0,'SAE13':8,
    'SAE14':0,'SAE15':0,'SAE16':13,
}
note_ue3={
    'R101':12,'R102':0,'R103':12,'R104':0,'R105':0,'R106':9,'R107':9,'R108':9,'R109':13.9,
    'R110':12,'R111':9,'R112':12,'R113':0,'R114':0,'R115':13,'SAE11':0,'SAE12':0,'SAE13':0,
    'SAE14':12,'SAE15':14,'SAE16':13,
}

moyenne_ue1 = calcul_moyenne(coef_ue1, note_ue1)
moyenne_ue2 = calcul_moyenne(coef_ue2, note_ue2)
moyenne_ue3 = calcul_moyenne(coef_ue3, note_ue3)

print('Moyenne pondérée de l\'UE 1 :', round(moyenne_ue1, 2))
print('Moyenne pondérée de l\'UE 2 :', round(moyenne_ue2, 2))
print('Moyenne pondérée de l\'UE 3 :', round(moyenne_ue3, 2))  







