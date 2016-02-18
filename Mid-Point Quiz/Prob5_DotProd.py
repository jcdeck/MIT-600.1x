# Problem #5 
#Write a Python function that returns the sum of the pairwise products of listA and listB. 
#You should assume that listA and listB have the same length and are two lists of integer numbers. 
#For example, if listA = [1, 2, 3] and listB = [4, 5, 6], the dot product is 1*4 + 2*5 + 3*6, 
#meaning your function should return: 32

def dotProduct(listA,listB):
    dotProd = 0
    i = 0
    while i < len(listA):
        dotProd += listA[i]*listB[i]
        i +=1
    return dotProd