class FilaAtendimento:
    def __init__(self, array):
        self.array = array;

    def adicionar_cliente(self, nome):
        self.array.append(nome);

    def atender_cliente(self): 
        self.array.pop(0);

    def tamanho_fila(self):
        return len(self.array);

    def getClientes(self):
        return self.array;

x = FilaAtendimento(["kappa" "claus", "xablau", "bilu", "jururu"]);

print(x.tamanho_fila());
print(x.getClientes());
x.adicionar_cliente("maluco");
print(x.getClientes());
print(x.tamanho_fila());
x.atender_cliente();
print(x.getClientes());
print(x.tamanho_fila());
x.atender_cliente();
x.atender_cliente();
x.atender_cliente();
print(x.getClientes());
print(x.tamanho_fila());