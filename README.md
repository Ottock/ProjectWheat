# DESENVOLVIMENTO DE ALGORITMOS DE PROCESSAMENTO DE IMAGENS PARA IDENTIFICAÇÃO DE PRAGAS EM LAVOURAS DE TRIGO
#
##### Otto Camargo Kuchkarian 1; Wânderson de Oliveira Assis 2
##### 1. Aluno de Iniciação Científica do Instituto Mauá de Tecnologia (IMT);
##### 2. Professor do Instituto Mauá de Tecnologia (IMT)
##
### Índice
##### 1. Descrição;
##### 2. Objetivo;
##### 3. Como usar;
##### 4.
###
## 1. Descrição
A cultura do trigo é vital para a segurança alimentar, geração de renda e desenvolvimento social no Brasil, 
mas enfrenta desafios significativos devido a pragas que comprometem a produtividade e a rentabilidade 
dos agricultores. Com os avanços na tecnologia de processamento computacional e ferramentas de
processamento de imagens, soluções baseadas em IoT estão se tornando cada vez mais relevantes para a 
agricultura de precisão. Este trabalho visa desenvolver um sistema de processamento de imagem para 
monitorar lavouras de trigo em tempo real, utilizando Python, OpenCV e a plataforma Roboflow. Serão 
criados modelos de detecção para identificar pragas comuns e espigas de trigo, integrando Machine Learning 
para melhorar a precisão. Diversos testes avaliarão a robustez do sistema, garantindo sua eficácia em diferentes condições de campo. A abordagem proposta permitirá a detecção precoce de pragas, 
contribuindo para a produtividade e sustentabilidade da produção de trigo no Brasil, e pode servir como
modelo para outras culturas agrícolas, promovendo avanços na agricultura de precisão.
####
## 2. Objetivo 
O objetivo deste trabalho é desenvolver um sistema de processamento de imagem para analisar dados coletados por meio de câmeras e 
sensores aplicados na agricultura de precisão, especificamente na cultura do trigo. Utilizando a linguagem de programação Python e suas bibliotecas associadas, bem como a plataforma Roboflow, busca-se implementar uma solução computacional capaz de realizar 
o processamento de imagens e a identificação de padrões e pragas na área de plantação. Essa abordagem permitirá um monitoramento contínuo e automatizado das lavouras, facilitando a detecção precoce de pragas e a adoção de medidas corretivas. 
#### 
## 3. Como usar 
### .venv: 
".venv" é o ambiente virtual gerado que carrega todas as bibliotecas utilizadas para realizar o projeto com exatidão.
Abaixo segue a lista dessas extensões e suas específicas versões:
- [Python 3.12.4](https://www.python.org/downloads/)
- [matplotlib 3.9.0](https://pypi.org/project/matplotlib/)
- [opencv-pyhton 4.10.0.84](https://pypi.org/project/opencv-python/)
- [roboflow 1.1.36](https://pypi.org/project/roboflow/)
### achives:
"archives" é a pasta que contém uma pesquisa feita no começo do projeto para compreender tecnologias IoT, a vida do trigo e entre outras informações importantes.
### database:
A pasta "database" possui sub-pastas das 5 espécies escolhidas para o modelo identificar. Abaixo está listado as 5 espécies selecionadas:
##### X-| Nome da Pasta | "Nome da Espécie" | (Nome Científico);
##### 1- Metopolophium: "Pulgão-verde-pálido" (Metopolophium dirhodum);
##### 2- Rhopalosiphum: "Piolho-da-cereja-brava" - (Rhopalosiphum padi);
##### 3- Schizaphis: "Pulgão-verde-dos-cereais" - (Schizaphis graminum);
##### 4- Sipha maydis: "Pulgão-preto-dos-cereais" - (Sipha maydis);
##### 5- Sitobion avenae: "Pulgão-da-espiga" - (Sitobion avenae);
##
### functions:
A pasta "functions" é reservada para funções importantes utilizadas no projeto. Para utilizar alguma dentro de um arquivo Python, basta importar a biblioteca e especificar qual irá utilizar:
from functions import "Nome da função".
##
### models:
Nesta pasta, possui alguns testes, como o download do modelo Roboflow, a precisao que o modelo tem para determinadas classes de objetos e o teste que o sistema tem para lidar com imagens e videos.

##
### src:
Possui a aplicação principal do projeto.

##
### study:
Esta pasta tem arquivos de estudo que auxiliaram no desenvolvimento do projeto, para utilizar a biblioteca opencv e a plataforma Roboflow.

##
### tests:
A pasta "tests" possui em seu conteúdo diversos testes para verificar a funcionalidade correta de certos processos e funções.
##
