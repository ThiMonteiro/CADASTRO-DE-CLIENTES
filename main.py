from tkinter import *
from tkinter import ttk
from func import Func


class Application(Func):
    def __init__(self) -> None:
        self.window = Tk()
        self.tela()
        self.frames_da_tela()
        self.botoes_frame1()
        self.label_frame1()
        self.entry_frame1()
        self.lista_frame2()
        self.monta_tabelas()
        self.selecionar_lista()
        self.window.mainloop()

    def tela(self):
        self.window.title("Cadastro de Clientes")
        self.window.configure(background="#F2DA63")
        self.window.geometry("800x600")
        self.window.resizable(True, True)
        self.window.maxsize(width=900, height=700)
        self.window.minsize(width=700, height=400)

    def frames_da_tela(self):
        ### Criação dos Frames ###

        self.frame1 = Frame(
            self.window,
            bd=2,
            bg="#FFFFFF",
            highlightbackground="#2165BF",
            highlightthickness=3)

        self.frame1.place(
            relx=0.03,
            rely=0.10,
            relwidth=0.93,
            relheight=0.40)

        self.frame2 = Frame(
            self.window,
            bd=2,
            bg="#FFFFFF",
            highlightbackground="#2165BF",
            highlightthickness=3)

        self.frame2.place(
            relx=0.03,
            rely=0.55,
            relwidth=0.93,
            relheight=0.40)

    def botoes_frame1(self):
        ### Criação dos botões ###

        ## BOTÃO LIMPAR ##
        self.botao_limpar = Button(
            self.frame1,
            text="Limpar",
            bd=2,
            bg="#D9042B",
            fg="#FFFFFF",
            font=("Times", "10", "bold italic"),
            command=self.limpar_tela)

        self.botao_limpar.place(
            relx=0.51,
            rely=0.10,
            relwidth=0.10,
            relheight=0.14)

        ## BOTÃO NOVO ##
        self.botao_novo = Button(
            self.frame1,
            text="Novo",
            bd=2,
            bg="#58E610",
            fg="#FFFFFF",
            font=("Times", "10", "bold italic"),
            command=self.adicionar_cliente)

        self.botao_novo.place(
            relx=0.18,
            rely=0.10,
            relwidth=0.10,
            relheight=0.14)

        ## BOTÃO ALTERAR ##
        self.botao_alterar = Button(
            self.frame1,
            text="Alterar",
            bd="2",
            bg="#F2C572",
            fg="#FFFFFF",
            font=("Times", "10", "bold italic"),
            command=self.alterar_cliente)

        self.botao_alterar.place(
            relx=0.29,
            rely=0.10,
            relwidth=0.10,
            relheight=0.14)

        ## BOTÃO APAGAR ##
        self.botao_apagar = Button(
            self.frame1,
            text="Apagar",
            bd=2,
            bg="#D9042B",
            fg="#FFFFFF",
            font=("Times", "10", "bold italic"),
            command=self.deletar_cliente)

        self.botao_apagar.place(
            relx=0.40,
            rely=0.10,
            relwidth=0.10,
            relheight=0.14)

    def label_frame1(self):
        ## LABEL CODIGO ###
        self.lb_codigo = Label(
            self.frame1,
            text="Código",
            bg="#FFFFFF",
            fg="#2165BF",
            font=("Times", "11", "bold"))

        self.lb_codigo.place(
            relx=0.02,
            rely=0.03)

        ## LABEL NOME DO CLIENTE ##
        self.lb_nome = Label(
            self.frame1,
            text="Nome",
            bg="#FFFFFF",
            fg="#2165BF",
            font=("Times", "11", "bold"))

        self.lb_nome.place(
            relx=0.02,
            rely=0.35)

        ## LABEL DDD ##
        self.lb_dd = Label(
            self.frame1,
            text="DDD",
            bg="#FFFFFF",
            fg="#2165BF",
            font=("Times", "11", "bold"))

        self.lb_dd.place(
            relx=0.02,
            rely=0.65)

        ## LABEL TELEFONE ##
        self.lb_telefone = Label(
            self.frame1,
            text="Telefone",
            bg="#FFFFFF",
            fg="#2165BF",
            font=("Times", "11", "bold"))

        self.lb_telefone.place(
            relx=0.10,
            rely=0.65)

        ## LABEL CIDADE ##
        self.lb_cidade = Label(
            self.frame1,
            text="Cidade",
            bg="#FFFFFF",
            fg="#2165BF",
            font=("Times", "11", "bold"))

        self.lb_cidade.place(
            relx=0.50,
            rely=0.65)

    def entry_frame1(self):
        ## ENTRY CODIGO ##
        self.entry_codigo = Entry(
            self.frame1,
            bd=2,
            fg="#000000",
            font=("verdana", "9", "bold"))

        self.entry_codigo.place(
            relx=0.02,
            rely=0.12,
            relwidth=0.14,
            relheight=0.12)

        ## ENTRY NOME ##
        self.entry_nome = Entry(
            self.frame1,
            bd=2,
            fg="#000000",
            font=("verdana", "9", "bold"))

        self.entry_nome.place(
            relx=0.02,
            rely=0.45,
            relwidth=0.68,
            relheight=0.12)

        ## ENTRY DD ##
        self.entry_ddd = Entry(
            self.frame1,
            bd=2,
            fg="#000000",
            font=("verdana", "9", "bold"))

        self.entry_ddd.place(
            relx=0.02,
            rely=0.75,
            relwidth=0.05,
            relheight=0.12)

        ## ENTRY TELEFONE ##
        self.entry_telefone = Entry(
            self.frame1,
            bd=2,
            fg="#000000",
            font=("verdana", "9", "bold"))

        self.entry_telefone.place(
            relx=0.10,
            rely=0.75,
            relwidth=0.20,
            relheight=0.12)

        ## ENTRY CIDADE ##
        self.entry_cidade = Entry(
            self.frame1,
            bd=2,
            fg="#000000",
            font=("verdana", "9", "bold"))

        self.entry_cidade.place(
            relx=0.50,
            rely=0.75,
            relwidth=0.20,
            relheight=0.12)

    def lista_frame2(self):
        ## Criação da lista ###
        self.lista_cli = ttk.Treeview(
            self.frame2,
            height=3,
            columns=("col1", "col2", "col3", "col4", "col5"))

        self.lista_cli.heading("#0", text="")
        self.lista_cli.heading("#1", text="Codigo")
        self.lista_cli.heading("#2", text="Nome")
        self.lista_cli.heading("#3", text="DDD")
        self.lista_cli.heading("#4", text="Telefone")
        self.lista_cli.heading("#5", text="Cidade")

        self.lista_cli.column("#0", width=1)
        self.lista_cli.column("#1", width=50)
        self.lista_cli.column("#2", width=200)
        self.lista_cli.column("#3", width=50)
        self.lista_cli.column("#4", width=125)
        self.lista_cli.column("#5", width=125)

        self.lista_cli.place(
            relx=0.01,
            rely=0.03,
            relwidth=0.94,
            relheight=0.85)

        self.scroollista = Scrollbar(self.frame2, orient='vertical')

        self.lista_cli.configure(yscrollcommand=self.scroollista.set)

        self.scroollista.place(
            relx=0.95,
            rely=0.03,
            relwidth=0.04,
            relheight=0.95)

        self.lista_cli.bind("<Double-1>", self.duplo_clique)


if __name__ == "__main__":
    Application()
