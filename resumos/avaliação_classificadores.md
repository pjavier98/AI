# Resumo IA - AB2
# Avaliação de Classificadores:

## Técnica para avaliação:
### Procedimento Básico:
* dividir a base de dados em:
  * treinamento;
  * teste.
* acurácia (taxa de acerto) do classificador 
  * (numero de acertos / base de teste)
* taxa de erro do classificador
  * (numero de erros / base de teste)

### Hold out:
* divisão aleatória da base em:
  * treinamento(2/3)
  * teste(1/3)

### Random Subsampling:
* Hold out executado k vezes;
* Acurácia do classificador é obtida a partir da média das acurácias obtidas nas k execuções.

### k-Fold Cross Validation:
* Base particionada (aleatoriamente) em  k partes (do mesmo tamanho  proximadamente);
* Treinamento e testes executados K vezes;
* Em cada execução:
  * 1 partição de teste
  * k-1 partições de treinamento
* Todas as partições são utilizadas, em algum momento, para teste.

### Stratified Cross-Validation:
* Cada partição utilizada na técnica  k-fold cross  validation deve possuir a mesma distribuição de classes da base original.

### Leave-one-Out:
* Mesmo que k-fold cross validation quando k é o número de instância da base de dados. 

### Matriz de confusão:
* Medidas (por classe):
  * Verdadeiro Positivo (TP(C))
    * elementos da classe C
 classificados como da classe C
  * Verdadeiro Negativo (TN(C))
    * elementos fora da classe C
 classificados como fora da classe C
  * Falso Positivo (FP(C))
    * elementos fora da classe C
 classificados como da classe C
  * Falso Negativo (FN(C))
    * elementos da classe C
 classificados como fora classe C

 ### Precision(C):
* Para todos os elementos
classificados como sendo de C,
quantos foram classificados
corretamente.
```
TP(C) / (TP(C) + FP(C))
```

### Recall(C):
* Para todos os elementos de C, quantos foram classificados
como sendo de C (corretamente).

```
TP(C) / (TP(C) + FN(C))
```

