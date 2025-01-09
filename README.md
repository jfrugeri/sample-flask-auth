# sample-flask-auth
 
## 1. Arquivos e diretórios necessários:
- ### 1.1 Necessário ter o arquivo **.env** na raiz do projeto com as seguintes variáveis:
```bash
MYSQL_ROOT_PASSWORD=your_root_password
MYSQL_DATABASE=yout_database_name
MYSQL_USER=your_user
MYSQL_PASSWORD=your_password
```
- ### 1.2 Crie um diretório vazio chamado **mysql** na raiz do projeto.
> Neste diretório **mysql** será criado arquivos do banco de dados.
---
## 2. Instalação das dependências:
Execute o comando abaixo para instalar as dependências do projeto:
- Python Version: 3.12.8
```bash
pip install -r requirements.txt
```
---
## 3. Criando o banco de dados:
- ### 3.1 Abra o terminal onde esta o arquivo **docker-compose.yml** e execute o comando:
```bash
docker-compose up
```
> Esse comando irá subir o banco de dados. Na porta **3306**.
- ### 3.2 Com o banco de dados rodando, abra o terminal no diretorio do projeto e execute o comando:
```bash
flask shell
db.create_all()
db.session.commit()
exit()
```
> Esse comando acima irá criar a tabela no banco de dados.
---
## 4. Rodando o projeto:

- ### 4.1 Abra o terminal no diretorio do projeto e execute o comando:

```bash
python app.py
```
> O projeto irá rodar em -> http://localhost:5000