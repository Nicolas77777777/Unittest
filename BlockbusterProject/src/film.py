
class Film:
    def __init__(self, id:int, title:str ) :
        self.__id = id 
        self.__title= title

    def setID(self,id:int)-> None: 
        self.__id = id

    def setTitle(self,title: str)-> None:
        self.__title =title

    def getID(self):
        return self.__id
    
    def getTitle(self) :
        return self.__title
    
    def isEqual(self ,otherFilm) -> bool:
        if otherFilm == self.getID():
        #if self.getID() == otherFilm.getID():
            print(True)
            return True
        else:
            print(False)
            return False
        
    def __str__(self) -> str:
        return f'ID = {self.__id} Title = {self.__title}'
        



