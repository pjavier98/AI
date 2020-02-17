# Apriori vs Partition:

* Na estratégia Partition, a base de dados é lida apenas duas vezes.

* Na estratégia Apriori, a base de dados é lida em cada uma das k 
iterações.

* Se, por um lado, a estratégia Apriori realiza um número maior de
leituras à base de dados, estas várias leituras permitem que, dentre 
os conjuntos candidatos, apenas os freqüentes passem à iteração 
seguinte.

* Na estratégia Partition, passam para a última fase e devem ser 
processados todos os freqüentes locais (candidatos globais), 
identificados em cada partição. Este fato, dependendo do número de 
candidatos gerados que não são de fato freqüentes, pode comprometer 
o desempenho
deste algoritmo.