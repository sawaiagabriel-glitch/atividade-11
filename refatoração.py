#código vulnerável

import sqlite3

def busca_usuario_por_email(email_digitado):
    conexao = sqlite3.connect('usuarios.db')
    cursor = conexao.cursor()

    query = "SELECT nome, email FROM usuarios WHERE email = '" + email_digitado + "'"

    print(f"Executando query: {query}")
    cursor.execute(query)

    return cursor.fetchone()
#código refatorado
import sqlite3

def busca_usuario_por_email(email_digitado):
    if "@" not in email_digitado:
        return None

    conexao = sqlite3.connect('usuarios.db')
    cursor = conexao.cursor()

    query = "SELECT nome, email FROM usuarios WHERE email = ?"
    cursor.execute(query, (email_digitado,))

    usuario = cursor.fetchone()
    conexao.close()

    return usuario
