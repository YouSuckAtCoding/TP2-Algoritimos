
def funcao1(n):  #Complexidade O(n)
    for i in range(n): 
       print(i)
# Função 2

def funcao2(n):   #Complexidade O(n²)
    for i in range(n):
     for j in range(n):
        print(i, j)

# Função 3          
def funcao3 (n):    #Complexidade O(2^n) (Honestamente, é uma discussão legal sobre isso aqui. 
    if n <= 1:      #Mas foi a resposta que achei. T(n) = T(n-1) + T(n-2) + T(1) -> O(2^n)
        return n
    return funcao3(n - 1) + funcao3(n - 2)