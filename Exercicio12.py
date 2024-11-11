class TabelaHash():
    def __init__(self, size):
        self.size = size;
        self.keys = [] * self.size;
        self.values = [] * self.size;
        self.index = -1;

    def inserir(self, key, value):
        self.index +=1;
        if(self.index > self.size):
            self.index -=1;
            return "Full";
        if(key in self.keys):
            return "key exists";
        self.keys.append(key);
        self.values.append(value);

    def buscar(self, key):
        for i in range(0, self.index):
            if(self.keys[i] == key):
                return self.values[i];
        return "None";

    def remover(self, key):
        for i in range(0, self.index):
            if(self.keys[i] == key):
                    self.values[i] = "";
                    self.keys[i] = "";
                    return;


x = TabelaHash(5);
x.inserir(2, "kappa");
print(x.inserir(2, "claus"));
x.inserir(3, "claus");
print(x.buscar(3));
x.remover(2);
print(x.buscar(2));

        
