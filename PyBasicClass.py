class Worker :
    ProcessCounter =  0
    def __init__(self) -> None:
        #self.__dict__ = dic
        Worker.ProcessCounter +=1
        print("Counter:",Worker.ProcessCounter)
        pass
    def Parser(self, lst):        
        for l in lst:
            print(l) 

A = Worker()
myList = [1,2,3,4,5]


B = Worker()
A.Parser(myList)