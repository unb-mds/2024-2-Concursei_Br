# Guia de Contribuição - Concursei BSB

Obrigado por considerar contribuir para o **Concursei BSB**! Este projeto faz parte da disciplina **MDS** e busca promover transparência e acessibilidade aos dados de concursos públicos. Este documento fornece diretrizes para garantir que sua contribuição seja clara, útil e de acordo com os padrões do projeto.

---

## Como Contribuir

Existem várias formas de contribuir para o projeto:

1. **Relatar problemas (issues):**
   - Caso encontre um bug ou tenha sugestões para melhorias, abra uma [issue](https://github.com/seu-repositorio/issues). 
   - Ao abrir uma issue, forneça uma descrição detalhada e, se possível, inclua capturas de tela ou exemplos para ajudar na reprodução.

2. **Sugerir melhorias:**
   - Sugestões de novas funcionalidades, otimizações ou melhorias na experiência do usuário são sempre bem-vindas.
   - Crie uma issue com a etiqueta `enhancement` e detalhe sua ideia.

3. **Criar ou melhorar funcionalidades:**
   - Verifique a seção de [issues abertas](https://github.com/seu-repositorio/issues) e escolha algo para trabalhar.
   - Siga o processo descrito na seção **Fluxo de Trabalho** abaixo.

4. **Atualizar a documentação:**
   - Se encontrar erros ou informações desatualizadas na documentação (como README ou guias), sinta-se à vontade para corrigi-los.

5. **Testar funcionalidades:**
   - Ajude testando novas funcionalidades e relatando problemas ou sugerindo melhorias.

---

## Requisitos para Contribuição

Antes de começar, certifique-se de:

1. Ter uma conta no GitHub configurada.
2. Ter o ambiente de desenvolvimento configurado. Consulte o [README.md](README.md) para as instruções de configuração do projeto.
3. Conhecer as boas práticas descritas no [Código de Conduta](CODE_OF_CONDUCT.md).

---

## Fluxo de Trabalho

Siga estas etapas para contribuir com o código:

1. **Faça um fork do repositório:**
   - Clique no botão `Fork` no topo da página do repositório.
   - Clone o seu fork localmente:
     ```bash
     git clone https://github.com/sua-conta/concursei-bsb.git
     cd concursei-bsb
     ```

2. **Crie uma branch para a sua contribuição:**
   - Nomeie a branch de forma descritiva, por exemplo:
     ```bash
     git checkout -b melhoria-relatorio-concursos
     ```

3. **Implemente suas mudanças:**
   - Faça commits pequenos e descritivos. Exemplo:
     ```bash
     git commit -m "Adiciona gráfico interativo para relatórios"
     ```

4. **Sincronize com a branch principal:**
   - Antes de abrir um pull request, certifique-se de que sua branch está atualizada:
     ```bash
     git pull origin main
     ```

5. **Abra um Pull Request (PR):**
   - Envie suas mudanças para o repositório remoto:
     ```bash
     git push origin melhoria-relatorio-concursos
     ```
   - No GitHub, abra um Pull Request para a branch principal (`main`) e inclua:
     - Uma descrição clara das mudanças realizadas.
     - Links ou imagens, se necessário, para facilitar a revisão.
   - Aguarde os mantenedores revisarem seu PR. Você pode ser solicitado a fazer ajustes.

---

## Boas Práticas de Código

- **Siga o padrão do projeto:** Utilize a estrutura e estilo de código existentes.
- **Comente o código:** Adicione comentários claros para explicar partes complexas ou lógicas importantes.
- **Adicione testes:** Se adicionar funcionalidades, escreva testes para garantir que funcionam corretamente.
- **Atualize a documentação:** Garanta que as mudanças sejam refletidas nos arquivos de documentação relevantes.

---

## Estrutura do Projeto

Aqui está uma visão geral da estrutura do projeto para ajudar você a se orientar:
```
├── concursei_bsb/                       # Diretório principal
    ├── app/                             # Front e app principal
    ├── data/                            # Dados
    ├── scrap/                           # API
├── .venv/                               # Arquivos estáticos e públicos
├── gitpage/                             # Scripts de teste
├── .github/ISSUE_TEMPLATE/              # Documentação do projeto
└── README.md                            # Informações gerais do projeto
```
---

## Ferramentas Recomendadas

- **Editor:** Recomendamos o uso do [VS Code](https://code.visualstudio.com/).
- **Versionamento:** Certifique-se de que o [Git](https://git-scm.com/) está instalado e configurado.
- **Linter:** Utilize o linter configurado no projeto (como `ESLint` ou `Prettier`).
- **Node.js e npm:** Consulte o README para versões específicas.

---

## Código de Conduta

Ao contribuir, você concorda em seguir o [Código de Conduta](CODE_OF_CONDUCT.md) do projeto. Seja respeitoso, colaborativo e aberto a novas ideias.

---

## Como Relatar Problemas

Se encontrar um problema, faça o seguinte:

1. **Verifique se já há uma issue aberta.**
2. **Crie uma nova issue** se o problema não foi relatado. Inclua:
   - Passos para reproduzir o problema.
   - Comportamento esperado e o que ocorreu.
   - Detalhes sobre o ambiente (ex.: navegador, sistema operacional).

---

Agradecemos suas contribuições e por ajudar a tornar o **Concursei BSB** uma plataforma incrível!
