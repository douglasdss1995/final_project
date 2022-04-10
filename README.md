# Filmes

Projeto desenvolvido como exercicio para o curso de Python com Django

## Descrição

Criar uma aplicação Django para cadastro de filmes e assinantes. Os assinantes podem escolher um ou mais filmes como favoritos e o mesmo filme também pode ser favoritado por mais de um assinante;

Os assinantes devem possuir nome e e-mail para cadastro, enquanto os filmes é importante ter o título e categoria (Comédia, Romance, etc.).

Deve ser criado um cadastro de anúncios dos filmes que serão lançados e com a data do seu lançamento. Sempre que for lançado um filme que se encaixe no favorito de um assinante o mesmo deve receber um e-mail.

Além dos endpoints criar as telas no admin.

## Requisitos

* Docker instalado na máquina 

## Como iniciar

* Execute o comando abaixo para utilizar o docker compose e criar o banco de dados:
  * ```cd .\docker-compose\```
  * ```docker-compose -f .\docker-compose-postgres.yml up -d```
* Acesse a URL:
  * ``http://127.0.0.1:16543``
  * Username: email@email.com
  * Password: 123456
* Crie a conexão
* Crie um banco de dados de acordo com o nome existente na váriavel **DB_NAME** 
* Retorne a pasta raiz e execute os comando abaixo para baixar as dependencias:
  * ``pip install -r .\requirements.txt``
* Execute o comando abaixo para a estrutura do banco de dados
  * ``python .\manage.py migrate``
* Execute eo comando abaixo para iniciar o projeto:
  * ``python .\manage.py runserver``
* Execute o comando abaixo para criar um usuário de acesso:
  * ``python.exe .\manage.py createsuperuser --email email@email.com``
  * Informe os dados conforme requisitado
* Acesse a URL:
  * ``http://127.0.0.1:8000/ ``
