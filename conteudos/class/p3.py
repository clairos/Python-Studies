 # POO = herança

class NPC: # classe pai, base, super
    def __init__(self, nome, time, forca, municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100
    
    def info(self):
        print(f"Nome...: {self.nome}")
        print(f"Time...: {self.time}")	
        print(f"Força..: {self.forca}")
        print(f"Munição: {self.municao}")
        print(f"Vivo...: " + ("sim" if self.vivo else "não"))
        print(f"Energia: {self.energia}")
        print("-----------------------")

class Soldado(NPC): # classe filho, utiliza a classe pai como 'parametro'
    def __init__(self, nome, time):
        self.forca = 200
        self.municao = 200
        super().__init__(nome, time, self.forca, self.municao) # chama as informações disponiveis na classe pai

class Guarda(NPC):
    def __init__(self, nome, time):
        self.forca = 100
        self.municao = 20
        super().__init__(nome, time, self.forca, self.municao)

class Elite(NPC):
    def __init__(self, nome, time):
        self.forca = 400
        self.municao = 200
        super().__init__(nome, time, self.forca, self.municao)

    def inf(self):
        super().info()

o1=Guarda("Olho Vivo", 1) 
o2=Soldado("Bala na Agulha", 1) 
o3=Elite("Ninja", 1) 
o4=Guarda("Super Atento", 2) 
o5=Soldado("Tiro Certo", 2) 
o6=Elite("Samurai", 2) 

o1.vivo = False
o6.vivo = False

o1.info()
o2.info()
o3.info()
o4.info()
o5.info()
o6.inf()