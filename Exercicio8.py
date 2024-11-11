def reverseStack(stack):
    aux = [];

    while stack:

        temp = stack.pop();
        aux.append(temp);

    return aux;

print(reverseStack([9,8,7,6,5,4,3,2,1]));