# Sample Flask Auth

Este projeto foi desenvolvido como uma aplicação prática para aprender a implementar autenticação de API utilizando Flask e um banco de dados MySQL.

## 📂 Arquivos e Diretórios Necessários

### 📄 1.1 Arquivo **.env**

Crie um arquivo **.env** na raiz do projeto com as seguintes variáveis de ambiente:

```bash
MYSQL_ROOT_PASSWORD=your_root_password
MYSQL_DATABASE=your_database_name
MYSQL_USER=your_user
MYSQL_PASSWORD=your_password
```

### 📁 1.2 Diretório **mysql**

Crie um diretório vazio chamado **mysql** na raiz do projeto.

> Este diretório será utilizado para armazenar os arquivos do banco de dados.

---

## 📦 Instalação das Dependências

Certifique-se de que você está utilizando **Python 3.12.8**. Em seguida, execute o comando abaixo para instalar as dependências:

```bash
pip install -r requirements.txt
```

---

## 🗄️ Criando o Banco de Dados

### 🐳 3.1 Subindo o banco de dados com Docker

No terminal, navegue até o diretório onde está o arquivo **docker-compose.yml** e execute o comando:

```bash
docker-compose up
```

> Isso iniciará o banco de dados na porta **3306**.

### ⚙️ 3.2 Criando as tabelas no banco de dados

Com o banco de dados rodando, abra o terminal no diretório do projeto e execute os seguintes comandos:

```bash
flask shell
db.create_all()
db.session.commit()
exit()
```

> Esses comandos irão criar as tabelas no banco de dados.

---

## 🚀 Rodando o Projeto

### ▶️ 4.1 Iniciando o servidor Flask

Abra o terminal no diretório do projeto e execute o comando:

```bash
python app.py
```

> O projeto estará disponível em: [http://localhost:5000](http://localhost:5000)

---

## 📌 Resumo de Comandos

| Comando                           | Descrição                          |
| --------------------------------- | ---------------------------------- |
| `pip install -r requirements.txt` | Instala as dependências do projeto |
| `docker-compose up`               | Inicia o banco de dados via Docker |
| `python app.py`                   | Inicia o servidor Flask            |

---

⚠️ **Certifique-se de que o Docker está instalado e rodando antes de executar o projeto.**

