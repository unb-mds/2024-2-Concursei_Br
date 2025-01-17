# **Entendendo a Arquitetura Cliente-Servidor do Streamlit**

O Streamlit utiliza uma **arquitetura cliente-servidor**, estruturada da seguinte forma:

## **1. Backend em Python (Servidor)**
- O backend é o cérebro da aplicação, responsável pelas computações e execução do código.
- Ao executar o comando `streamlit run your_app.py`, um servidor Streamlit é iniciado localmente utilizando Python.
- Esse servidor, também chamado de **host**, é único e serve todos os usuários que acessam o aplicativo, seja em uma rede local ou pela internet.

## **2. Frontend no Navegador (Cliente)**
- O frontend é a interface gráfica que os usuários visualizam e interagem no navegador.
- Quando o app é acessado localmente, o servidor e o cliente são executados na mesma máquina. 
- Ao ser acessado via rede local ou internet, o cliente roda em dispositivos diferentes do servidor.

---

## **Impacto da Arquitetura no Design do App**

1. **Capacidade do Servidor**:
   - O servidor deve ser dimensionado adequadamente para atender múltiplos usuários simultâneos, garantindo um desempenho ideal.

2. **Acesso a Arquivos**:
   - O app só pode acessar arquivos específicos que o usuário faça upload via widgets como `st.file_uploader`.
   - O servidor **não tem acesso direto ao sistema de arquivos do cliente**.

3. **Dispositivos Periféricos**:
   - Para interagir com dispositivos (ex.: câmeras), é necessário usar comandos do Streamlit ou componentes personalizados que comuniquem corretamente o frontend (cliente) com o backend (servidor).

4. **Execução de Processos Externos**:
   - Processos externos ao Python são executados no servidor, não no cliente. 
   - Por exemplo, ao tentar abrir um navegador com o módulo `webbrowser`, ele será aberto no servidor, não no dispositivo do usuário.

---
