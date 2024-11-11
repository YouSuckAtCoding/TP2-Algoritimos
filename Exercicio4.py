def sortStack(stack):
    aux = [];
            
            #Estão sendo utilizado 2 stacks mas poderia ser feito com qualquer estrutura auxiliar, como lista.
            #Não é possível ordenar um stack sem uma estrutura de suporte, as operações de um stack não permitem
            #Enquanto o stack possuir elementos, é passado para o auxiliar os elementos em ordem ao mesmo tempo que
            #eles são removidos do stack inicial.

            #No final eles são inseridos novamente no stack inicial ordenados.
    while stack:
        
        top = stack.pop();
        
        while aux and aux[-1] < top:
            stack.append(aux.pop());

        aux.append(top);

    while aux:
        stack.append(aux.pop());

    return stack;

print(sortStack([1,4,8,7,45,11]));

    