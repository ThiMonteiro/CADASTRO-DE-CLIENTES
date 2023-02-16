from tkinter import *
import pyodbc


class Func():

    def limpar_tela(self):
        self.entry_codigo.delete(0, END)
        self.entry_nome.delete(0, END)
        self.entry_ddd.delete(0, END)
        self.entry_telefone.delete(0, END)
        self.entry_cidade.delete(0, END)

    def conecta_bd(self):
        dados_conexao = (
            "Driver={SQL Server};"
            "Server=coloque o seu servidor;"
            "Database=CLIENTES;")

        self.conexao = pyodbc.connect(dados_conexao)
        self.cursor = self.conexao.cursor()

    def desconecta_bd(self):
        self.conexao.close()

    def monta_tabelas(self):
        ## CHAMAREMOS A FUNÇÃO QUE CONECTA EM NOSSO BANCO DE DADOS ##
        self.conecta_bd()

        ## VAMOS CRIAR A TABELA ##
        comando = """IF OBJECT_ID('TABELA DE CLIENTES') IS NULL
        BEGIN
            CREATE TABLE [TABELA DE CLIENTES]
            ([COD] [INT],
            [NOME_CLIENTE] [VARCHAR] (150),
            [DDD] [INT], [TELEFONE] [INT],
            [CIDADE] [VARCHAR] (50))
        END"""

        self.cursor.execute(comando)

        self.conexao.commit()

        self.desconecta_bd()

    def adicionar_cliente(self):
        self.codigo = self.entry_codigo.get()
        self.nome = self.entry_nome.get()
        self.ddd = self.entry_ddd.get()
        self.telefone = self.entry_telefone.get()
        self.cidade = self.entry_cidade.get()

        self.conecta_bd()

        comando = f"""INSERT INTO [TABELA DE CLIENTES]
        ([COD], [NOME_CLIENTE], [DDD], [TELEFONE], [CIDADE])
        VALUES
        ({self.codigo}, '{self.nome}', {self.ddd}, {self.telefone}, '{self.cidade}')"""

        self.cursor.execute(comando)

        self.cursor.commit()

        self.desconecta_bd()

        self.selecionar_lista()

        self.limpar_tela()

    def selecionar_lista(self):
        self.lista_cli.delete(*self.lista_cli.get_children())

        self.conecta_bd()

        comando = """SELECT [COD], [NOME_CLIENTE], [DDD], [TELEFONE], [CIDADE] FROM [TABELA DE CLIENTES]
        ORDER BY [NOME_CLIENTE] ASC"""

        lista = self.cursor.execute(comando)

        for i in lista:
            self.lista_cli.insert("", END, values=(
                i[0], i[1], i[2], i[3], i[4]))

        self.desconecta_bd()

    def duplo_clique(self, event):
        self.limpar_tela()

        self.lista_cli.selection()

        for n in self.lista_cli.selection():
            col1, col2, col3, col4, col5 = self.lista_cli.item(n, 'values')

            self.entry_codigo.insert(END, col1)
            self.entry_nome.insert(END, col2)
            self.entry_ddd.insert(END, col3)
            self.entry_telefone.insert(END, col4)
            self.entry_cidade.insert(END, col5)

    def deletar_cliente(self):
        self.codigo = self.entry_codigo.get()
        self.nome = self.entry_nome.get()
        self.ddd = self.entry_ddd.get()
        self.telefone = self.entry_telefone.get()
        self.cidade = self.entry_cidade.get()

        self.conecta_bd()

        comando = f"""DELETE FROM [TABELA DE CLIENTES]
        WHERE [COD] = {self.codigo}"""

        self.cursor.execute(comando)
        self.conexao.commit()
        self.limpar_tela()
        self.selecionar_lista()

        self.desconecta_bd()

    def alterar_cliente(self):
        self.codigo = self.entry_codigo.get()
        self.nome = self.entry_nome.get()
        self.ddd = self.entry_ddd.get()
        self.telefone = self.entry_telefone.get()
        self.cidade = self.entry_cidade.get()

        comando = f"""UPDATE [TABELA DE CLIENTES] SET 
        [NOME_CLIENTE] = '{self.nome}', [DDD] = {self.ddd}, [TELEFONE] = {self.telefone}, [CIDADE] = '{self.cidade}'
        WHERE [COD] = {self.codigo}"""

        self.conecta_bd()
        self.cursor.execute(comando)
        self.conexao.commit()
        self.desconecta_bd()

        self.selecionar_lista()
        self.limpar_tela()
