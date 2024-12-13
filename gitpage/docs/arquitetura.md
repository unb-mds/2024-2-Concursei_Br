# Arquitetura

Esta arquitetura descreve um fluxo de dados composto por cinco componentes principais: 

1. **DataClass**: Responsável por iniciar o processo, utilizando o método `fetchData()` para capturar dados.
2. **WebScrap**: Um módulo de raspagem web que coleta informações usando o método `scrape()` e contém a lógica para interagir com fontes externas.
3. **API**: Atua como intermediária, fornecendo os dados através do método `getData()`, possibilitando o acesso de forma padronizada.
4. **RegexReader**: Processa os dados recebidos por meio do método `process(data)` para organizar ou extrair informações relevantes.
5. **FrontEnd**: Recebe os dados processados e os apresenta ao usuário final com o método `displayData(data)`.

O fluxo segue uma sequência linear, com cada componente desempenhando um papel específico para transformar dados brutos em informações utilizáveis no front-end.

<img style = "display: flex; justify-self: center; margin: 70px 0 70px 0;" src="/img_docs/img_arquitetura.png" alt="arquitetura" width="40%"/>