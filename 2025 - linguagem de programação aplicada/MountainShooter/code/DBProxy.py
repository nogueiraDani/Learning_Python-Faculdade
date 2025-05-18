import sqlite3


# Define uma classe chamada DBProxy.
# Esta classe implementa o padrão de projeto Proxy. Ela atua como um intermediário
# para acessar o banco de dados, controlando e potencialmente estendendo as operações.
class DBProxy:
    # Método construtor da classe. É chamado quando um objeto DBProxy é criado.
    def __init__(self, db_name: str):
        # Armazena o nome do arquivo do banco de dados na variável de instância 'db_name'.
        self.db_name = db_name
        # Estabelece uma conexão com o banco de dados SQLite especificado pelo 'db_name'. Se o arquivo não existir, ele será criado.
        self.connection = sqlite3.connect(db_name)
        # Executa um comando SQL para criar uma tabela chamada 'dados' se ela ainda não existir.
        self.connection.execute(
            """
                CREATE TABLE IF NOT EXISTS dados(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                score INTEGER NOT NULL,
                date TEXT NOT NULL)
            """
        )

    # Define um método para salvar um novo score no banco de dados. Recebe um dicionário 'score_dict' com os dados.
    def save(self, score_dict: dict):
        # Executa um comando SQL de inserção de dados na tabela 'dados'.
        # Os valores para 'name', 'score' e 'date' serão retirados do dicionário 'score_dict'.
        # Os ':' antes das chaves no SQL são placeholders para os valores do dicionário.
        self.connection.execute(
            "INSERT INTO dados (name, score, date) VALUES (:name, :score, :date)",
            score_dict,
        )
        # Salva as alterações feitas no banco de dados (tornando a inserção permanente).
        self.connection.commit()

    # Define um método para recuperar os 10 melhores scores do banco de dados.
    def retrieve_top10(self) -> list:
        # Executa um comando SQL para selecionar todos os registros da tabela 'dados',
        # ordenando-os em ordem decrescente pela coluna 'score' e limitando o resultado a 10 registros.
        return self.connection.execute(
            "SELECT * FROM dados ORDER BY score DESC LIMIT 10"
        ).fetchall()
        # Retorna todos os resultados da consulta como uma lista de tuplas.

    # Define um método para fechar a conexão com o banco de dados. É importante fazer isso ao terminar de usar o banco de dados.
    def close(self):
        # Fecha a conexão com o banco de dados.
        return self.connection.close()
