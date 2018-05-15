# gnome riddle
# run as python3 kabouters.py
from random import shuffle

def kabouters():
    
    success = 0
    for b in range(1000):
        x = [i for i in range(1,101)]
        shuffle(x)
        fail = False
       
        for a in range(100):
            if x[a] != 0 and fail == False:               
                tofind = a+1
                counter = 1
                n = x[tofind-1]
                x[tofind-1] = 0
                
                while n != tofind:
                    prev = n
                    n = x[n-1]
                    x[prev-1]= 0
                    counter += 1   
            
                if counter > 50:
                    fail = True
        if fail == False:
            success += 1
            
    print('succesrate: ' + str(success) + '/1000')
    
kabouters()
