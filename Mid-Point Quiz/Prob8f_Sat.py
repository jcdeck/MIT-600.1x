#Write a Python function called satisfiesF that has the specification below. #
#Then make the function call run_satisfiesF(L, satisfiesF). Your code should look like
#-------Problem Description------ 
#def f(s):
#    return 'a' in s
      
#L = ['a', 'b', 'a']
#print satisfiesF(L)
#print L

#----------------Sample Output-------

#2
#['a', 'a']

#----------------------------------------



def satisfiesF(L):
    
    muteList = [ ]

    def f(s):
        return 'a' in s 
    
    
    for string in L: 
        print f(string) 
        if f(string) == True: 
            muteList.append(string)
            print list 
          
    L[:] = muteList
            
    
    return len(L)    
    
run_satisfiesF(L, satisfiesF) 
