# Introdução
Este script foi feito para automatizar o envio de mensagens para inscritos em cursos do Cerest Oeste.
Primeiramente nós criamos um formulário online (Google forms) para inscrição dos participantes, pedindo: nome completo, telefone para contato, cpf e profissão.
Após, geramos um csv contendo todos os dados. Um dia antes de cada evento, nós enviamos mensagens lembrando sobre o curso e repassando informações para todos os inscritos.
Como a maioria dos inscritos nós não temos na agenda do telefone, viu-se necessário automatizar este processo.


Com esse script você pode:
* Enviar mensagens automatizadas por WhatsApp para múltiplas pessoas sem ter contantos salvos.

# Instruções
1. Clone o projeto: 
```console
WhoAmI@WhoAmI:~$ git clone https://github.com/LuizFritsch/automatizando-tarefas.git
```
2. Baixe as dependencias.
3. Altere para o seu csv
4. Execute:
```console
WhoAmI@WhoAmI:~$ python3 sender.py
```
