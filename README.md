# house_sales_insights

## 1. Negócio

A house rocket é uma empresa americana queatua no setor imobiliário, recentemente a companhia dicidiu iniciar uma operação em Seattle. Dessa forma, a house rocket se viu na necessidade de ter uma análise na sua base de imóveis para determinar quais imóveis deve comprar, por qual preço e em que momento do ano deve ser vendido.

### 1.1 Questões de negócio

Tendo em vista o contexto da empresa, existem duas questões de negócio para se responder.

1. Qual o melhor preço de compra para cada imóvel?
2. Uma vez que o imóvel já foi comprado qual seria o melhor momento para vender?

### 1.2. Base de dados

A base de dados fornecida ao time de dados possue 21436 linhas com as descrições das casas, sendo esses 19 atributos.

As colunas da base de dados foram traduzidas para português, ficando da seguinte forma:

| Nome da coluna | Tradução | Descrição |
| ----------- | -------- | --------- |
| id | id | ID exclusivo para cada casa vendida |
| date | data_venda | Data da venda da casa |
| price | preco | Preço de cada casa vendida |
| bedrooms | quartos | Número de quartos |
| bedrooms | banheiros | Número de banheiros, onde 0,5 representa um quarto com vaso sanitário, mas sem chuveiro |
| sqft_living | m2_construido_total | Metragem quadrada do espaço interior dos apartamentos |
| sqft_lot | m2_terreno_total | Metragem quadrada do espaço terrestre |
| floors | andares | Número de andares |
| waterfront | vista_agua | Variável fictícia para saber se o apartamento estava com vista para a orla ou não |
| view | vista_geral | Índice de 0 a 4 de quão boa era a vista do imóvel. 0 é a pior vista e 4 é a melhor vista |
| condition | condicao | Índice de 1 a 5 sobre a condição do apartamento. 1 é a pior condição e 5 é a melhor |
| grade | design_construcao | Índice de 1 a 13, onde 1-3 fica aquém da construção e design de edifícios, 7 tem um nível médio de construção e design e 11-13 tem um alto nível de construção e design. |
| sqft_above | m2_construidos_chao | Metragem quadrada do espaço interno da habitação que está acima do nível do solo |
| sqft_basement | m2_porao | Metragem quadrada do espaço interno da habitação que está abaixo do nível do solo |
| yr_built | ano_construído | Ano em que a casa foi construída |
| yr_renovated | ano_reformado | Ano da última reforma da casa |
| zipcode | cep | Em que área de código postal a casa está |
| lat | latitude | latitude |
| long | longitude | longitude |
| sqft_living15 | nao_traduzido | Metragem quadrada do espaço habitacional interior para os 15 vizinhos mais próximos |
| sqft_lot15 | nao_traduzido | A metragem quadrada dos lotes dos 15 vizinhos mais próximos |

## 2. Premissas

Pensando em como resolver os problemas de negócio foram assumidas as seguintes premissas:

1. O preço de reforma é calculado com base na condição do Imóvel;
2. Dados nulos ou NA serão preenchidos com a média ou moda;
3. Preço do dólar para conversão é de 5.44R$;
4. Conversão do Sqft para M2 = Sqfrt_area/ 10.764;
5. m2_living = metragem quadrada do imóvel;
6. m2_lot = área total do terreno do imóvel;
7. Outliers são erros de digitação.

## 3. Planejamento da Solução

###3.1 A entrega da análise será feita de duas formas: 
  - Base de imóveis para comprar e a base de reformas foram entregues em CSV;
  - Dashboard no Streamlit referente a base de compra.
  
###3.2 Ferramentas utilizadas: 
  1)  Python
      - Jupyter Notebook;
      - Pycharm.
      
###3.3 Etapas da Solução:
  1) Processo 1: Coleta, Tratamento e Tranformações de Dados:
    Os dados foram entregues em CSV, então os dados foram extraídos pelo pandas;
    Converter Datatypes;
    Verificar Nulos;
    Deletar Colunas;
    Converter sqft para m2;
    Criar colunas level;
    Criar coluna dormitory_type;
    Criar coluna condition_type;
    Criar coluna renovate_price;
    Criar coluna price_per_m2.
   
   2) Processo 2: Análise Exploratória de dados:
    Análise Exploratória;
    Estatística Descritiva;
    Validação das Hipóteses;
    Preenchimento de dados geoespaciais com API;
    Finalizar base de recomendação de compra.
    
   3) Processo 3: Dashboard no Streamlit:
    Criar Cartões com os números do Negócios: Investimento total, Receita total, Lucro total e Margem de lucro.
    Filtros: zipcode, preço, número de banheiros, número de quartos, vista para o mar e área da casa.
    Gráfico de barras: quantidade de imóveis por tipo de dormitório, preço mediano por tipo de dormitório.
    Gráfico de linha: Variação do preço mediano ao longo dos anos.
    Mapa Iterativo da região.
    
##4. Resultados da Análise:
      Total de Imóveis disponíveis para Compra: 10689;
      Imóveis reformados são em média 15% mais caros;
      Segundo Semestre é o melhor período do ano, podendo vender o imóvel por até 5% mais caro;
      Imóveis em condições ruins são uma boa oportunidade de negócio, se forem reformados para serem revendidos;
      Imóveis com vista para o mar são 312% mais caros em média;
      O preço mediano dos imóveis está no seu topo histórico.
      
##5. Resultados Financeiros:
      Investimento total: 4,125,953,819.0
      Receita prevista no melhor cenário: 5,984,438,004.65
      Lucro máximo da Operação: 1,858,484,185.65
      Margem de lucro: 31%
      
##6. Próximos Passos:
     Refatorar os códigos do jupyter notebook usando list comprehensions e funções para ter um código mais performático;
     Modelar os dados para utilizar modelos de ML de sistema de recomendação ou previsão para melhorar o portifólio de imóveis.
