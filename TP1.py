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


# In[ ]:





# In[ ]:


import matplotlib.pyplot as plt

import numpy as np

coef_ue1 = {
    'R101': 10, 'R102': 10, 'R103': 7, 'R104': 7, 'R106': 5, 'R108': 6,
    'R110': 5, 'R111': 4, 'R112': 2, 'R113': 5, 'R114': 5, 
    'SAE11': 20, 'SAE12': 20, 'SAE16': 7}
coef_ue2 = {
    'R101': 4, 'R103': 2, 'R104': 8, 'R105': 6, 'R110': 5, 'R111': 5,
    'R112': 2, 'R113': 9, 'R114': 9, 'R115': 3, 'SAE13': 29, 'SAE16': 7}
coef_ue3 = {
    'R101': 4, 'R103': 2, 'R106': 5, 'R107': 15, 'R108': 6, 'R109': 4,
    'R110': 5, 'R111': 5, 'R112': 2, 'R115': 3, 'SAE14': 20, 'SAE15': 20, 'SAE16': 7}

notes1 = {
    'R101': 14, 'R102': 13, 'R103': 13, 'R104': 14, 'R106': 15, 'R108': 13,
    'R110': 12, 'R111': 12, 'R112': 10, 'R113': 14, 'R114': 12, 
    'SAE11': 16, 'SAE12': 15, 'SAE16': 14}
notes2 = { 
    'R101': 14, 'R103': 13, 'R104': 20, 'R105': 20, 'R110': 12, 'R111': 12,
    'R112': 10, 'R113': 14, 'R114': 12, 'R115': 12, 'SAE13': 15, 'SAE16': 14}
notes3 = {
    'R101': 14, 'R103': 13, 'R106': 15, 'R107': 12, 'R108': 13, 'R109': 14,
    'R110': 12, 'R111': 12, 'R112': 10, 'R115': 12, 'SAE14': 14, 'SAE15': 13, 'SAE16': 14}


def moyenne_ponderee(notes, coef_ue):
    totalnotes = 0
    totalcoeff = 0

    for i in notes: 
        if i in coef_ue:
            totalnotes += notes[i] * coef_ue[i]
            totalcoeff += coef_ue[i]

        if totalcoeff == 0:
            return 0
        else:
            return totalnotes / totalcoeff

moyenne1 = moyenne_ponderee(notes1, coef_ue1)
moyenne2 = moyenne_ponderee(notes2, coef_ue2)
moyenne3 = moyenne_ponderee(notes3, coef_ue3)



def get_color(value):
    if value >= 10:
        return 'green'
    elif 8 <= value < 10:
        return 'orange'
    else:
        return 'red'

colors = [] 
for m in moyennes:
    couleur = get_color(m) 
    colors.append(couleur)

plt.bar(['UE1','UE2','UE3'],[moyenne1,moyenne2,moyenne3],color=colors)
plt.title('Moyenne des UE')
plt.xlabel('Moyenne des UE')
plt.ylabel('Note')


plt.show()


# In[ ]:




