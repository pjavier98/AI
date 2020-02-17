# -*- coding: utf-8 -*-
"""diabetes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NvMFFfr4G1TEFIqxvf6ncRO01JuZ3yBx
"""

import pandas as pd
import numpy as np

data = pd.read_csv("diabetes.csv")

data.drop(['Pregnancies', 'DiabetesPedigreeFunction'], inplace=True, axis=1)

# Eliminar as pessoas com glucose, insulina ou indice de massa corporal igual a 0
glucose = data[data['Glucose'] == 0].index
insulin = data[data['Insulin'] == 0].index
bmi = data[data['BMI'] == 0].index

new_set = index = glucose.union(insulin)
new_set = new_set.union(bmi)

data.drop(new_set, inplace=True, axis=0)

# Separando o banco em treino e teste (0.7 e 0.3 respectivamente)
from sklearn.model_selection import train_test_split

def fit(X_train, Y_train, X_test, Y_test):
  train = len(X_train) == len(Y_train)
  test = len(X_test) == len(Y_test)
  return (train and test)

independent_features = ['Glucose',	'BloodPressure', 'SkinThickness',	'Insulin',	'BMI',	'Age']
dependent_feature = ['Outcome']

X = data[independent_features]
Y = data[dependent_feature]

def hold_out():
  X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3)
  fit(X_train, Y_train, X_test, Y_test)
  
  X_train = X_train.reset_index(drop=True)
  Y_train = Y_train.reset_index(drop=True)

  X_test = X_test.reset_index(drop=True)
  Y_test = Y_test.reset_index(drop=True)

  return X_train, X_test, Y_train, Y_test

# calcular a distancia de cada um dos atributos daquela instancia
def euclidean_distance(train_instance, test_instance):
  numbers_of_attrs = len(test_instance)
  distance = 0

  for j in range(0, numbers_of_attrs):
    distance += (train_instance[j] - test_instance[j]) ** 2
  return (distance ** 0.5)

def KNN(X_train, Y_train, test_instance, k_neighbors):
  numbers_of_attrs = len(test_instance)
  distances_list = []

  for i, train_instance in enumerate(X_train.values):
    is_diabetic = Y_train.values[i][0]
    distance = euclidean_distance(train_instance, test_instance)
    distances_list.append((distance, is_diabetic))
  
  # # ordenar pela menor distancia para posteriormente selecionar k vizinhos
  distances_list.sort()
  return distances_list[:k_neighbors]

# criando lista de distancias para cada uma das instâncias
def predict(X_train, X_test, Y_train, Y_test, k_neighbors, test_size):
  predict_list = []
  for test_instance in X_test.values:
    instance_dist = KNN(X_train, Y_train, test_instance, k_neighbors)
    
    diabetics_list = []
    for _, is_diabetic in instance_dist:
      diabetics_list.append(is_diabetic)
    
    is_diabetic = 0
    if (diabetics_list.count(1) > diabetics_list.count(0)):
      is_diabetic = 1
    
    predict_list.append(is_diabetic)
  return predict_list

# validações dos resultados
def accuracy(confusion_matrix, predict_list, Y_test):
  tp, tn, fp, fn = 0, 0, 0, 0

  for i, predict_value in enumerate(predict_list):
    real_value = Y_test.values[i][0]
    
    
    if (real_value == 1): # true positive and false negative
      if (real_value == predict_value):
        tp += 1
        confusion_matrix[0][0] += 1
      else:
        fn += 1
        confusion_matrix[1][0] += 1
    else: # true negative and false positive
      if (real_value == predict_value):
        tn += 1
        confusion_matrix[1][1] += 1
      else:
        fp += 1
        confusion_matrix[0][1] += 1
  
  return tp, tn, fp, fn

def print_results(title, tp, tn, fp, fn, size):
  accuracy = tp + tn
  errors = fp + fn
  
  print(title)
  
  print("Numbers of hits: ", accuracy)
  print("Numbers of errors: ", errors)

  print("Precision: {0:.2f}".format(tp / (tp + fp)))
  print("Recall: {0:.2f}".format(tp / (tp + fn)))

  print("Percentage of hits: {0:.2f}%".format((accuracy / size) * 100))
  print("Percentage of errors: {0:.2f}%".format((errors / size) * 100))
  print()

def print_confused_matrix(confusion_matrix):
  columns = ['Diabetic', 'Non-Diabetic']
  matrix = pd.DataFrame(confusion_matrix, columns=columns, index=columns)
  print(matrix)


def random_subsampling():
  k_neighbors = 17 # impar e primo
  k_times = 7
  
  true_positive = 0 # pessoas que são diabeticas e foram classificados como diabeticas 
  true_negative = 0 # pessoas que não são diabeticas e foram classificados como não diabeticas
  false_positive = 0 # pessoas que não são diabeticas classificadas como diabeticas
  false_negative = 0 # pessoas que são diabeticas classificadas como não diabeticas

  # accuracy = true_positive + true_negative
  # errors = false_positive + false_negative

  confusion_matrix = [[0 for x in range(2)] for y in range(2)] 

  # [TP => [0, 0], FP => [0, 1]]
  # [FN => [1, 0] , TN => [1, 1]]

  for i in range(0, k_times):
    tp, tn, fp, fn = 0, 0, 0, 0

    X_train, X_test, Y_train, Y_test = hold_out()

    test_size = len(X_test)

    predict_list = predict(X_train, X_test, Y_train, Y_test, k_neighbors, test_size)
    tp, tn, fp, fn = accuracy(confusion_matrix, predict_list, Y_test)
    title = 'Iteration: ' + str(i + 1)
    print_results(title, tp, tn, fp, fn, test_size)

  for i in range(0, 2):
    for j in range(0, 2):
      confusion_matrix[i][j] /= k_times
      confusion_matrix[i][j] = round(confusion_matrix[i][j], 2)
  
  title = 'Final result after: ' + str(k_times) + ' iterations'
  print_results(title, tp, tn, fp, fn, test_size)
  print_confused_matrix(confusion_matrix)

  
random_subsampling()