from tkinter import *

class Main():
    def __init__(self):
        self.janela = Tk()
        self.largura = self.janela.winfo_screenwidth()
        self.altura = self.janela.winfo_screenheight()
        self.janela.geometry("%dx%d" % (self.largura, self.altura))
        self.janela.title("AMA Filmes")

        # Cria o canvas principal
        self.canva1 = Canvas(self.janela, bg="#5CE1E6", width=self.largura, height=self.altura)
        self.canva1.place(x=0, y=0)

        # Cria o canvas do cabeçalho
        self.canvas3 = Canvas(self.canva1, bg="#37C9E4", width=self.largura, height=123)
        self.canvas3.place(x=0, y=0)

        # Cria o canvas do lado esquerdo
        self.canvas2 = Canvas(self.canva1, bg="#37C9E4", width=330, height=self.altura)
        self.canvas2.place(x=0, y=0)

        self.logo = PhotoImage(file="logo.png") 

    
        self.canvas3.create_image(1290, 60, image=self.logo) 
      
    
        self.butao1 = Button(self.canvas2, text="Incluir",fg="white",bg="#0097B2", relief="raised", borderwidth=2, font=("Arial", 13), width=21)
        self.butao1.place(x=69, y=230)
        self.butao2 = Button(self.canvas2, text="Excluir", fg="white",bg="#0097B2", relief="raised", borderwidth=2, font=("Arial", 13),  width=21)
        self.butao2.place(x=69, y=310)
        self.butao3 = Button(self.canvas2, text="Meus Filmes", fg="white", bg="#0097B2", relief="raised", borderwidth=2, font=("Arial", 13),width=21)
        self.butao3.place(x=69, y= 400)
        self.butao3 = Button(self.canvas2, text="Pesquisar", fg="white", bg="#0097B2", relief="raised", borderwidth=2, font=("Arial", 13),width=21)
        self.butao3.place(x=69, y=480)
        # ... (cria outros botões)

        # Cria a entrada
        self.entrada = Entry(self.canva1, width=70, bg="#FCF6DB")
        self.entrada.place(x=420, y=170, height=37)  # Posiciona a entrada mais à esquerda

        self.label_meio = Label(self.canva1, text="Titulo do filme e quantidade", bg="white", font=("Arial", 13), width=27, height=3)
        self.label_meio.place(relx=0.4, rely=0.4, anchor='center')  # Posiciona o Label no meio da tela

        # Cria o botão e o posiciona no final do campo de entrada
        self.botao_enviar = Button(self.canva1, text="Enviar", bg="#0097B2", fg="white")  
        self.botao_enviar.place(x=870, y=170, height="37", width="63")  # Posiciona o botão no final do campo de entrada


        # Cria o label com dimensões e posição especificadas
        self.label_final = Label(self.canva1, text="Filmes", bg="#E2E2E2", font=("Arial", 23), width=43, height=5)
        self.label_final.place(relx=0.6, rely=0.8, anchor='s')  # Posiciona o Label no final da tela

        self.janela.mainloop()

App = Main()

        
        
        
        
