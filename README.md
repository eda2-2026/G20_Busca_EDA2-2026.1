## Sistema de inteligente de Treino

## Link do vídeo ##

[text](https://www.youtube.com/watch?v=6-fUCZv2oOg)

## Autores

Gustavo Xavier Evangelista - 241025247
Pedro Henrique Ferreira Xavier - 241025990


## Visão Geral

Este projeto consiste em um sistema que auxilia na escolha de exercícios físicos de forma personalizada, com base em critérios definidos pelo usuário.

A proposta é simular um assistente de treino simples, capaz de sugerir exercícios adequados considerando fatores como tempo disponível, grupo muscular e nível de dificuldade, além de acompanhar a evolução de carga ao longo do tempo.

O sistema foi pensado para ser útil no dia a dia, ajudando na tomada de decisão durante o treino sem a necessidade de planejamento prévio complexo.

---

## Objetivo

Oferecer recomendações rápidas e coerentes de exercícios, permitindo que o usuário:

- Escolha o que treinar com base no tempo disponível  
- Mantenha consistência no treino  
- Evite regressão de carga  
- Acompanhe sua evolução de forma simples  

---

## Como o sistema funciona

O usuário informa alguns critérios básicos, como:

- Grupo muscular desejado  
- Tempo disponível  
- Nível de dificuldade  
- Carga alvo (opcional)  

A partir dessas informações, o sistema analisa os exercícios cadastrados e retorna sugestões que melhor se encaixam na situação atual.

Além disso, o sistema utiliza o histórico de cargas para recomendar progressão de treino, incentivando evolução contínua.

---

## Funcionalidades

- Filtragem de exercícios por múltiplos critérios  
- Recomendação do exercício mais adequado  
- Sugestão de carga ideal com base no histórico  
- Sugestão de progressão de carga  
- Acompanhamento de evolução por exercício  
- Visualização do histórico de treinos  

---

## Estrutura do Sistema

Cada exercício possui informações como:

- Nome  
- Grupo muscular  
- Duração média  
- Nível de dificuldade  
- Histórico de cargas utilizadas  

Esses dados permitem que o sistema faça recomendações mais precisas e adaptadas ao usuário.

---

## Fluxo de Uso

1. O usuário informa seus critérios (tempo, grupo muscular, etc.)  
2. O sistema filtra os exercícios disponíveis  
3. As opções são avaliadas com base nos dados cadastrados  
4. O sistema retorna:
   - Exercícios recomendados  
   - Melhor opção  
   - Carga sugerida  
   - Possível progressão  

---

## Sobre o uso de algoritmos

O sistema utiliza algoritmos de busca para organizar e processar os dados de forma eficiente.

Esses algoritmos são responsáveis por:

- Filtrar exercícios rapidamente  
- Localizar valores ideais dentro de conjuntos ordenados  
- Selecionar a melhor opção entre várias possibilidades  

Embora não sejam o foco principal do projeto, eles garantem que o sistema funcione de maneira eficiente e escalável.

### Algoritmos e estruturas de dados utilizados

Atualmente, o sistema utiliza diferentes abordagens de busca sobre a mesma base de exercícios (arquivo `backend/exercicios.json`) para fins de comparação:

- **Busca sequencial**: utilizada em operações simples como localizar um exercício para edição ou remoção.
- **Busca binária**: aplicada sobre listas ordenadas por nome ou tempo para localizar um exercício de forma mais eficiente que a busca sequencial.
- **Tabela hash (hashing)**: estrutura de dados usada para mapear diretamente o nome do exercício para o objeto correspondente, permitindo busca em tempo esperado constante.

No menu principal do sistema (arquivo `backend/app.py`), existem opções distintas para busca por nome utilizando:

- Tabela hash (estrutura de dados de dispersão)
- Busca binária em lista ordenada

Isso permite observar, na prática, o impacto da escolha do algoritmo e da estrutura de dados no comportamento do sistema.

---

## Tecnologias

- Linguagem: Python  

---

## Conclusão

Este projeto demonstra como conceitos computacionais podem ser aplicados para resolver problemas simples do cotidiano.

Ao transformar dados básicos em recomendações úteis, o sistema oferece uma forma prática de organizar treinos e apoiar a evolução do usuário de maneira objetiva e automatizada.

---

