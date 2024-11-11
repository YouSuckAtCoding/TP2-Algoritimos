def evenInStack(idStack):
    
    temp = idStack;
    count = 0;

    while temp:
        
        if(temp[-1] % 2 == 0):
            count+=1;
           
        temp.pop();
    
    return count;


print(evenInStack([3,5,4,8,7,9,4,5,1]));