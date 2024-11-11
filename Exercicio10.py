from collections import deque

def oddnQueue(queue):
    temp = queue;
    count = 0;
    while temp:

        curr = temp.popleft();
        if(curr % 2 != 0):
            count +=1;
    
    return count;

queue = deque();
queue.append(1);
queue.append(5);
queue.append(2);
queue.append(7);
queue.append(10);
print(oddnQueue(queue))