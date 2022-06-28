# -*- coding: utf-8 -*-
"""app-arvore-covid.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P2hps5TogszyTwfVft5GpT5nQI5HYQEQ
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier 
from sklearn import metrics
from sklearn.preprocessing import OrdinalEncoder

dataset = pd.read_csv('dados26abril22.csv', sep=';')

nomesClassesED = ['REC','OBT']
colunas = dataset.columns.to_list()
nomesColunas = colunas [1:3]
nomesColunas = nomesColunas+colunas[4:]

dataset_features = dataset[nomesColunas]
dataset_classes = dataset['EVOLUCAO']

feature_treino,feature_teste,classes_treino,classes_teste = train_test_split(dataset_features,
                                                                             dataset_classes,
                                                                             test_size=0.15,
                                                                             random_state=15)

#construção da árvore
arvore = DecisionTreeClassifier()

#treino a arvore
arvore.fit(feature_treino,classes_treino)

#entrada de dados
import streamlit as st

nomes_classes = ['Recuperação','Risco de óbito']
sexo = list(set(dataset['SEXO'])) 
faixas_etarias = list(set(dataset['FAIXAETARIA']))
hospitalizado = list(set(dataset['HOSPITALIZADO'])) 
febre = list(set(dataset['FEBRE'])) 
tosse = list(set(dataset['TOSSE']))
garganta = list(set(dataset['GARGANTA'])) 
dispneia = list(set(dataset['DISPNEIA'])) 
gestante = list(set(dataset['GESTANTE'])) 
cor = list(set(dataset['RACA_COR']))
srag = list(set(dataset['SRAG'])) 
 
info_sexo = st.selectbox('Escolha o sexo do paciente', sexo)
info_idade = st.selectbox('Escolha a idade do paciente', faixas_etarias)
info_hospital = st.selectbox('O paciente foi hospitalizado?', hospitalizado  )
info_febre = st.selectbox('O paciente teve febre?', febre )
info_tosse = st.selectbox('O paciente tem tosse?', tosse )
info_garganta = st.selectbox('O paciente tem dor de garganta?', garganta )
info_dispneia = st.selectbox('O paciente tem dispneia (dificuldade para respirar)?', dispneia )
info_gestante = st.selectbox('Trata-se de paciente gestante?', gestante )
info_cor = st.selectbox('Indique a raça/cor do paciente', cor )
info_srag = st.selectbox('O paciente desenvolveu Sindrome Respiratória Aguda Grave?', srag )

encoder = OrdinalEncoder()
dataset['SEXO'] = encoder.fit_transform(pd.DataFrame(dataset['SEXO']))
dataset['FAIXAETARIA'] = encoder.fit_transform(pd.DataFrame(dataset['FAIXAETARIA']))
dataset['EVOLUCAO'] = encoder.fit_transform(pd.DataFrame(dataset['EVOLUCAO']))
dataset['HOSPITALIZADO'] = encoder.fit_transform(pd.DataFrame(dataset['HOSPITALIZADO']))
dataset['FEBRE'] = encoder.fit_transform(pd.DataFrame(dataset['FEBRE']))
dataset['TOSSE'] = encoder.fit_transform(pd.DataFrame(dataset['TOSSE']))
dataset['GARGANTA'] = encoder.fit_transform(pd.DataFrame(dataset['GARGANTA']))
dataset['DISPNEIA'] = encoder.fit_transform(pd.DataFrame(dataset['DISPNEIA']))
dataset['GESTANTE'] = encoder.fit_transform(pd.DataFrame(dataset['GESTANTE']))
dataset['RACA_COR'] = encoder.fit_transform(pd.DataFrame(dataset['RACA_COR']))
dataset['SRAG'] = encoder.fit_transform(pd.DataFrame(dataset['SRAG']))

if st.button('Prever evolução'):
    individuo = [info_sexo.index(sexo), info_idade.index(faisas_etarias), info_hospital.index(hospitalizado), info_febre.index(febre), info_tosse.index(tosse), info_garganta.index(garganta), info_dispneia.index(dispneia), info_gestante.index(), info_cor.index(cor), info_srag.index(srag)]
   
    predicao = arvore.predict([individuo])
    st.write('a predição de evolução para esse paciente é: '+nomes_classes[int(predicao[0])])