# Visão Geral
Este projeto implementa uma página de cadastro simples utilizando o microframework Flask em Python. O sistema é empacotado em contêineres Docker, demonstrando a utilização da arquitetura de microsserviços. A orquestração dos serviços é feita através do Docker Compose.

## Arquitetura de Microsserviços
A arquitetura de microsserviços é uma abordagem para desenvolver uma aplicação como um conjunto de pequenos serviços, cada um executando em seu próprio processo e se comunicando com mecanismos leves, geralmente uma API HTTP. Este projeto utiliza contêineres Docker para encapsular o ambiente de execução de cada serviço, garantindo assim a portabilidade e a escalabilidade.

## Dockerfile
O `Dockerfile` incluído neste projeto define todas as etapas necessárias para construir a imagem do contêiner do serviço de cadastro. Ele começa com uma imagem base do Python, instala as dependências e copia os arquivos do projeto para dentro do contêiner.

## Docker Compose
O `docker-compose.yml` é utilizado para definir e orquestrar múltiplos contêineres Docker. Ele permite configurar serviços, redes e volumes com um único arquivo, facilitando o gerenciamento dos componentes da aplicação.

## Estrutura do Projeto
•  `app/`: Contém o código fonte da aplicação Flask;

•  `Dockerfile`: Define as instruções para construir a imagem do contêiner;

•  `docker-compose.yml`: Define e orquestra os serviços do projeto.

## Como Executar
Para executar o projeto, siga os passos abaixo:
1. Clone o repositório para sua máquina local.
2. Navegue até a pasta do projeto e construa a imagem do Docker com `docker build -t cadastro-flask .`.
3. Inicie os serviços com `docker-compose up`.
4. Acesse `http://localhost:5000` no seu navegador para ver a página de cadastro.

## Contribuições
Contribuições são bem-vindas! Se você tem sugestões para melhorar o projeto ou adicionar novas funcionalidades, por favor, crie um fork do repositório e submeta um pull request.
