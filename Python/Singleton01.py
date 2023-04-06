class Singleton:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.value = 0
            print("Criado a instancia")
        return cls.instance

    def increment(self):
        self.value += 1
        print("Chamado metodo increment(self)")
        print(f"Value: {self.value}")

#-----------------------------------
# Cliente
print("Invocado s1 com a classe Singleton")
s1 = Singleton()

print("Invocado s2 com a classe Singleton")
s2 = Singleton()

print("Comparado s1 com s2")
print (s1 == s2)

print("Inicio do ciclo do metodo increment de s1 e s2")
s1.increment()
s2.increment()
s1.increment()