class Section():
    """Section class ,
    @title is the title of the secion
    @books is list of all books included in this section"""
    def __init__(self,title):
        self._title=title
        self._books=[]
    def getTitle(self):
        return self._title
    def addBook(self,book):
        self._books.append(book)
    def searchBookByTitle(self,title):
        """search for a book with title ,achievable in O(len(books)) by iterating all books in section
            returns Book object or None if no book found"""
        for book in self._books:
            if book.getTitle() ==title:
                return book
        return None#not found here
    def searchBookByAuthor(self,title):
        """returns all books details by author title in this Section"""
        data=[]
        for book in self._books:
            if book.getAuthor() ==title:
                data.append([book.getTitle(),book.getAuthor(),self.getTitle(),book.getCost()])
        return data
    def deleteBook(self,title):
        ''' deletes book ,using title returns status of deletion'''
        book = self.searchBookByTitle(title)
        if book is not None:
            self._books.remove(book)
            return True
        else:
            return False
    def showBooks(self):
        '''prints content of all books in this section to cmd
            returns all books details <section title included>'''
        data=[]
        print("Title , author , cost")
        for book in self._books:
            print(f"{book.getTitle()} , {book.getAuthor()} , {book.getCost()}")
            data.append([book.getTitle(),book.getAuthor(),self.getTitle(),book.getCost()])
        return data
