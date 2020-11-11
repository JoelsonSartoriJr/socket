## Sobre o projeto

O objetivo deste trabalho é familiarizar-se com o a programação de aplicações de rede com o uso de sockets.
Para isso, Python desenvolvemos uma aplicação utilizando o UDP que emule as garantias oferecidas pelo protocolo TCP.
Ao iniciar o programa o usuário deverá indicar se deseja utilizar o algoritmo Go-Back-N ou o algoritmo de Repetição Seletiva para o reenvio de pacotes perdidos.

## Iniciar o projeto

Abaixo estão apresentados os passos para rodar tanto o cliente quanto o server localmente.

### Pré-requisitos

A biblioteca que você deve ter instalado para rodar o código é a Sockets.
```sh
pip install sockets
```
## Como executar

1. Clone este repositório para a sua máquina.
2. Realizar a instalação das dependências.
3. Executar o arquivo do server com o comando e na mesma ordem:
  ```sh
  python envia.py
  ```
4. Executar o arquivo do cliente com o comando:
  ```sh
  python recebe.py
  ```
