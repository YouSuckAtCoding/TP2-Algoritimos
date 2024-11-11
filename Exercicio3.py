
def bruteForce(array):
    
    dupes = [];
    for l in range (0, array.len - 1):
        for i in range(1, array.len - 1):
            if(array[l] == array[i]):   
                dupes.append(array[i]);

    return dupes;

def hashArray(array):

    hash = set();
    for i in range(0, array.len - 1):
        hash.add(array[i]);

    return hash;
    
    

