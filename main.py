class Pessoa:
    def __init__(self,nome,peso,idade):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo=False
        self.andando=False
        self.dormindo=False

    def comer(self,comida):
        if self.dormindo ==True:
            print(f"{self.nome} não posso tô dormindo")
        elif self.andando ==True:
            print(f"{self.nome} não posso tô andando")
        elif self.comendo == False:
            print(f"{self.nome} começou a comer {comida}")
            self.comendo =True
        else:
            print(f"{self.nome} já tô comendo {comida}")

    def parardecomer(self):
        if self.comendo ==True:
            print("Parou de comer")
            self.comendo =False
        else:
            print(f"{self.nome} não está comendo")

    def andar(self):
        if self.dormindo==True:
            print("Estou domindo")
        elif self.comendo==True:
            print("Estou comendo")
        elif self.andando ==False:
            print("Comecou a andar")
            self.andando=True
        else:
            print("Já está andando")

    def parardeandar(self):
        if self.andando==True:
            print(f"{self.nome} parou de andar")
            self.andando=False
        else:
            print(f"{self.nome} não está andando")

    def dormir(self):
        if self.comendo ==True:
            print("Estou comendo")
        elif self.andando==True:
            print("Estou andando")
        elif self.dormindo==False:
            self.dormindo = True
            print(f"{self.nome} foi dormir")
        else:
            print(f"{self.nome}Já está dormindo")

    def acordar(self):
        if self.dormindo ==True:
            print("Acordei")
            self.dormindo=False
        else:
            print("Não estou dormindo")