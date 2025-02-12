# Arquitetura

Essa arquitetura segue um fluxo de ETL (Extract, Transform, Load) para coletar e visualizar dados de concursos públicos:

- **Extração (Extract)**: O backend realiza web scraping no site "ConcursosBrasil" para coletar informações sobre concursos públicos.
- **Transformação (Transform)**: Os dados brutos extraídos são processados no módulo ETL, onde podem ser limpos, estruturados e organizados.
- **Carregamento (Load)**: Após o processamento, os dados são armazenados em um arquivo CSV, facilitando seu uso posterior.
- **Visualização**: O frontend acessa os dados do CSV e os apresenta aos usuários por meio de gráficos e narrativas visuais (Data Visualization e Storytelling).

<img style = "display: flex; justify-self: center; margin: 70px 0 70px 0;" src="https://raw.githubusercontent.com/unb-mds/2024-2-Concursei_Bsb/refs/heads/main/gitpage/docs/img_docs/arquitetura.png" alt="arquitetura" width="40%"/>
