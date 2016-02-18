#Write a function to flatten a list. The list can contain other lists, strings or ints
# test ex. X = [[1, [2, 3]], [[4, 5, 6], [7, [8, 9]]], [[3, 2, 1], [2, 1], [1, [0]]]]
# output  [1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 2, 1, 2, 1, 1, 0]


def flatten(aList): 
    flatList = []
               
    def listPress(aList):
        for item in aList: 
            if isinstance(item, list):
                listPress(item)
            
            else: 
                flatList.append(item) 
                       
    listPress(aList)                                  
                                                                                                                            
    return flatList
          
                 