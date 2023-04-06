class Carrinho:

    __instance = None

    def __init__(self):
        if Carrinho.__instance is None:
            Carrinho.__instance = self
            self.item = []
        else:
            raise Exception("Esta classe é um singleton")

    @staticmethod
    def get_instance():
        if not Carrinho.__instance:
            Carrinho()
        return Carrinho.__instance
        
    def add_item(self, item):
        self.item.append(item)

    def get_item(self):
        return(self.item)

class Produto: 
    
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
# -------------------------------------------------
# Cliente

#Utilizando o Sinlgeton - Criar Carrinho
carrinho1 = Carrinho.get_instance()

#Criando Produtos
produto1 = Produto("Banana", 4.00)
produto2 = Produto("Melao", 10.00)
produto3 = Produto("Amandita", 12.00)
produto4 = Produto("Bolacha Waffle", 4.69)

#Adicionando itens no carrinho
carrinho1.add_item(produto3)
carrinho1.add_item(produto3)
carrinho1.add_item(produto2)
carrinho1.add_item(produto1)
carrinho1.add_item(produto4)

#Finaliza a compra e mostra lista total
print("-------------- Carrinho 01 --------------")
for item in carrinho1.get_item():
    print(item.nome, " - ", item.preco)