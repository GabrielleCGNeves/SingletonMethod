class Singleton:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.value = 0
            print("Chamado a instancia")
        return cls.instance

    def increment(self):
        self.value += 1
        print(f"Value: {self.value}")