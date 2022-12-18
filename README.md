# coleta-de-dados-imobiliarios
## Trabalho final de Algoritmos e Grafos - Cenário 2 (Coleta de dados imobilários) 

![image](https://user-images.githubusercontent.com/39037985/208254788-a2802b20-dea2-4b00-9042-c6720c0ddfa4.png)

## O Problema 

O seguinte repositorio tem como objetivo apresentar a solução do projeto sugerido pela disciplina de Algoritmos e Grafos do curso de Sistemas 
de Informação da Universidade Federal de Itajubá. A atividade em questão propõem o estudo de um cenário envolvendo a coleta de dados imobiliários na 
cidade de Elói Mendes/MG e a elaboração de uma solução que abrange conceitos relacionados à teoria dos grafos.

O cenário estudado trata-se de um projeto de Recadastramento Imobiliário Multifinalitário Georreferenciado realizado em Elói Mendes, Minas Gerais. O 
recadastramento imobiliário visa atualizar o Cadastro Técnico Multifinalitário (CTM) que, por sua vez, pode ser entendido como um sistema de registro dos 
elementos espaciais que representam a estrutura urbana, constituído por uma componente geométrica e outra descritiva que lhe conferem agilidade e 
diversidade no fornecimento de dados para atender diferentes funções (BLACHUT et al, 1974).

Em outras palavras, o CTM é uma base cartográfica e alfanumérica que descreve o sistema urbano (e rural) através das suas unidades imobiliárias, 
juntamente com os eixos de logradouros, possibilitando construir diversas bases temáticas a partir dela, tais como o planejamento urbano, cadastro 
tributário, a base de dados do sistema de saúde, o cadastro de áreas verdes e públicas, entre outras. 

 Desse modo, os principais objetivos de um Cadastro Técnico Multifinalitário são: aplicar a cobrança justa de impostos (ex. IPTU), servir de base para o 
 planejamento municipal, garantir a propriedade imobiliária, facilitar os processos de desapropriações legais, fiscalizar os planos de desenvolvimento 
 regional, gerar dados geoespaciais, facilitar a atualização cadastral e garantir a função social da terra.

O processo de recadastramento inicia-se a partir do imageamento da cidade, que é realizado por meio de drones que sobrevoam a região capturando imagens 
dos lotes e imóveis. Após essa etapa, é feita a delimitação dos lotes e suas respectivas edificações através de um software CAD (Computer Aided Design). 
Um Sistema de Informação Geográfico (SIG) armazena os dados de geolocalização dos imóveis, bem como o polígono correspondente, resultando no Mapa de 
Parcelas. 

Seguido da vetorização do espaço, há o processo da coleta de dados em campo, cujo propósito é obter informações que não são adquiridas com as imagens 
aéreas. Nessa fase, Agentes de Coleta vão a campo e, por meio de dispositivos móveis (smartphone, tablet), coletam características de todos os imóveis da 
região, tais como tipo, foto da fachada, acesso e ponto de interesse. 

Diante desse panomara apresentado, o projeto consiste em um estudo de determinada região de Elói Mendes para auxiliar na programação, definição do 
cronograma e custos da coleta de dados em campo, de modo a otimizar o planejamento e reduzir o esforço dessa atividade. O estudo propõem comparar o 
cronograma e custos quando se tem apenas um agente de coleta e quando se tem dois. A ideia é que, quando existir dois agentes, a divisão da quantidade de 
imóveis seja similar.

## A Solução

Em teoria dos grafos, um ramo da matemática, o problema do carteiro chinês (PCC), circuito do carteiro ou problema da inspeção de rotas consiste em 
encontrar um caminho mais curto ou circuito fechado que visite cada aresta de um grafo (conectado) não-direcionado. Quando o grafo possui um circuito 
euleriano (um passeio fechado que abrange toda aresta uma vez), esse circuito é uma solução ótima.

Alan Goldman do U.S. National Bureau of Standards cunhou pela primeira vez o nome 'problema do carteiro chinês' para este problema, uma vez que foi 
originalmente estudado pelo matemático chinês Mei-Ku Kuan em 1962.

## 👨‍💻 Tecnologias
  Para o desenvolvimento da solução foi utilizado as seguintes tecnologias:

 * Python
 * Python Notebook
