import sqlite3

# cria uma conexão com o banco de dados
conn = sqlite3.connect('exemplo.db')

# cria uma tabela no banco de dados
c = conn.cursor()
c.execute('''CREATE TABLE usuarios
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              nome TEXT,
              idade INTEGER)''')

# insere dados na tabela
c.execute("INSERT INTO exemplo (nome, idade) VALUES ('João', 25)")
c.execute("INSERT INTO exemplo (nome, idade) VALUES ('Maria', 30)")

# recupera dados da tabela
c.execute("SELECT * FROM exemplo")
dados = c.fetchall()
print(dados)

# fecha a conexão com o banco de dados
conn.close()
