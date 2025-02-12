# **Backlog**

O backlog de um produto é uma lista dinâmica e priorizada de todas as funcionalidades, melhorias, correções e tarefas necessárias para desenvolver e evoluir um produto. Ele serve como a base para o planejamento e execução das equipes de desenvolvimento. Cada item no backlog deve estar claro, ter valor para o usuário ou para o negócio e ser priorizado com base na importância, impacto e viabilidade. O backlog geralmente é continuamente atualizado.
<hr></hr>

# O que é um Épico e uma User Story?

## **Épico**

Um épico é uma grande unidade de trabalho ou um objetivo de alto nível dentro de um projeto que, normalmente, é muito amplo para ser concluído em um único sprint. Ele representa uma necessidade ou funcionalidade ampla e, por isso, é subdividido em **user stories** menores e mais específicas.  

### **Exemplo de Épico**

**"Transparência em Licitações e Contratos"**  
Descrição: Criar funcionalidades que permitam aos cidadãos e empresas acessarem informações sobre processos de licitação, contratos e fornecedores do município.  

---

## **User Story (História de Usuário)**  

Uma user story é uma descrição curta e simples do que um usuário deseja realizar com o sistema, escrita do ponto de vista dele. Seu objetivo é capturar o valor que uma funcionalidade específica oferece ao usuário. As histórias seguem, geralmente, o seguinte formato:  

> **"Como [tipo de usuário], quero [ação/funcionalidade], para que [benefício/valor esperado]."**

---

# Critérios de aceitação

## **Como definir critérios de aceitação?**

**Clareza e especificidade**: Os critérios devem ser objetivos e fáceis de entender.  
**Orientados ao comportamento**: Devem descrever o que o sistema deve fazer, não como deve ser implementado.  
**Testáveis**: Devem permitir a validação por meio de testes claros e repetíveis.

## Estrutura comum para critérios de aceitação

Critérios de aceitação geralmente são escritos no formato Dado... Quando... Então, que segue a lógica:

- **Dado**: o contexto inicial ou condição prévia.
- **Quando**: o evento ou ação realizada pelo usuário.
- **Então**: o resultado esperado ou comportamento do sistema.

---

## Épicos e User Story e seus Critérios de Aceitação

### Critérios de Aceitação para as Histórias de Usuário  

---

#### **História 1: Visualização Gráfica dos Dados**  

**"Como cliente, eu quero visualizar os dados de uma forma mais amigável e correta, para definir melhor a minha opinião sobre determinado dado."**  

Critérios de Aceitação:  

1. **Dado** que o cliente acesse a página de visualização de dados, **quando** os dados forem carregados, **então** eles devem ser exibidos em gráficos interativos e claros (ex.: gráficos de barras, linhas, ou pizza).  
2. **Dado** que o cliente interaja com o gráfico, **quando** ele passar o mouse sobre um ponto ou barra, **então** deve aparecer uma descrição detalhada (ex.: valores exatos e datas).  
3. **Dado** que os dados exibidos sejam grandes ou complexos, **quando** o cliente quiser ver mais detalhes, **então** deve haver uma opção de zoom ou foco em um período específico.  

---

#### **História 2: Filtragem dos Dados**

**"Como cidadão, eu quero filtrar os dados sobre os quais eu tenho interesse e sem distrações, para facilitar o acesso aos meus interesses."**  

Critérios de Aceitação:  

1. **Dado** que o cidadão esteja na interface de visualização de dados, **quando** ele selecionar um filtro (ex.: ano, categoria, município), **então** os dados exibidos devem ser atualizados de acordo com os critérios escolhidos.  
2. **Dado** que o cidadão queira aplicar múltiplos filtros, **quando** ele escolher mais de um critério, **então** os dados devem refletir a interseção das condições.  
3. **Dado** que nenhum filtro seja selecionado, **quando** o cidadão acessar a página, **então** os dados devem ser exibidos de forma geral e sem filtros aplicados.  
4. **Dado** que o filtro aplicado não retorne resultados, **quando** o cidadão finalizar a seleção, **então** uma mensagem amigável deve informar que "não há dados correspondentes".  

---

#### **História 3: Comparação de Dados**

**"Como usuário, eu quero a possibilidade de comparar os dados de diferentes concursos, para que seja possível uma análise das vgas que estão com inscrições abertas."**  

Critérios de Aceitação:  

1. **Dado** que o usuário esteja na interface de comparação, **quando** ele selecionar duas ou mais datas ou períodos, **então** os dados correspondentes devem ser exibidos lado a lado ou sobrepostos no mesmo gráfico.  
2. **Dado** que os dados de diferentes períodos sejam exibidos, **quando** o usuário clicar em uma linha ou barra do gráfico, **então** informações detalhadas (ex.: valor exato e data) devem ser mostradas para cada período selecionado.  
3. **Dado** que o usuário deseje alterar os períodos comparados, **quando** ele ajustar a seleção, **então** os gráficos devem ser atualizados automaticamente.  
4. **Dado** que os períodos selecionados não possuam dados, **quando** o usuário concluir a seleção, **então** uma mensagem deve informar que "não há dados disponíveis para as datas escolhidas".  

---

#### **História 4: Exportação de Dados**

**"Como cidadão interessado, quero exportar os dados sobre o município em formato CSV, para realizar análises detalhadas e cruzar informações com outras bases de dados."**  

Critérios de Aceitação:  

1. **Dado** que o cidadão esteja visualizando os dados filtrados, **quando** ele clicar no botão de exportação, **então** um arquivo no formato CSV contendo os dados visíveis deve ser baixado.
2. **Dado** que o arquivo CSV seja gerado, **quando** o cidadão abrir o arquivo, **então** os dados devem estar organizados em colunas com cabeçalhos claros e consistentes.  
3. **Dado** que o cidadão não tenha selecionado filtros, **quando** ele clicar no botão de exportação, **então** o CSV deve conter todos os dados disponíveis.  
4. **Dado** que ocorra algum erro na exportação, **quando** o cidadão tentar realizar o download, **então** uma mensagem de erro deve ser exibida com instruções para tentar novamente.  
