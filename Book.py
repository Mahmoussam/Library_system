class Book():
    """Book class represents Book object and members"""
    def __init__(self,title,author,cost):
        self._title=title
        self._author=author
        self._cost=cost
    def getTitle(self):
        return self._title
    def getAuthor(self):
        return self._author
    def getCost(self):
        return self._cost
    
