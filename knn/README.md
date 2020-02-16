# Projeto de implementação e validação de um classificador:

* Foi utilizada uma base de 
dados do kaggle sobre 
diabéticos, utilizamos o 
algoritmo KNN para montar um 
classificador para de acordo 
com algumas características 
fosse identificado se a pessoa 
era ou não diabética.

* No início foram eliminadas algumas 
tabelas que não possuiam muita 
relevância e algumas que possuiam muitos 
outliers.

* O dataset também foi processado 
eliminando dados incompletos a exemplo 
de glicose, pressão arterial e espesura 
da pele igual a 0.

* Posteriormente o dataset foi divido em 0.7 a parte de treinamento e 0.3 a parte 
de teste. 

* O processo do KNN executou em 
aproxidamente 1000 instâncias, 700 de 
treino e 300 de teste.

* Para melhorar o algoritmo foi usado o 
Random Subsampling em que fazemos o 
processo de divisão aleatoria do banco k 
vezes e com isso temos a acurácia do 
classificador obtida a partir da
média das acurácias obtidas nas k 
execuções.

* Foram utilizadas algumas métricas tais 
como acurâcia, quantidade de erros, 
precisão e recall.

* Por fim foi feita uma matriz de confusão 
para observar melhor os resultados.

Exemplo de saida do algoritmo:

```
Iteration: 1
Numbers of hits:  240
Numbers of errors:  72
Precision: 0.61
Recall: 0.56
Percentage of hits: 76.92%
Percentage of errors: 23.08%

Iteration: 2
Numbers of hits:  241
Numbers of errors:  71
Precision: 0.63
Recall: 0.64
Percentage of hits: 77.24%
Percentage of errors: 22.76%

Iteration: 3
Numbers of hits:  240
Numbers of errors:  72
Precision: 0.72
Recall: 0.55
Percentage of hits: 76.92%
Percentage of errors: 23.08%

Iteration: 4
Numbers of hits:  231
Numbers of errors:  81
Precision: 0.62
Recall: 0.60
Percentage of hits: 74.04%
Percentage of errors: 25.96%

Iteration: 5
Numbers of hits:  242
Numbers of errors:  70
Precision: 0.65
Recall: 0.61
Percentage of hits: 77.56%
Percentage of errors: 22.44%

Iteration: 6
Numbers of hits:  244
Numbers of errors:  68
Precision: 0.74
Recall: 0.56
Percentage of hits: 78.21%
Percentage of errors: 21.79%

Iteration: 7
Numbers of hits:  245
Numbers of errors:  67
Precision: 0.59
Recall: 0.69
Percentage of hits: 78.53%
Percentage of errors: 21.47%

Final result after: 7 iterations
Numbers of hits:  245
Numbers of errors:  67
Precision: 0.59
Recall: 0.69
Percentage of hits: 78.53%
Percentage of errors: 21.47%

              Diabetic  Non-Diabetic
Diabetic         58.71         32.00
Non-Diabetic     39.57        181.71
```