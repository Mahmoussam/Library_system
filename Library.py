from Book import Book
from Section import Section
import json
from pprint import pprint
from GUI import *
class Library():
    """represents the whole library ,is both /View-Controller"""
    def __init__(self,title):
        """library constructor
            @title is title of the library
            builds required data and structures in single loop iteration from source json file and sets required initial instance members beside UI initialization"""
        self._title=title
        self._sections=[]
        self._profit=0
        self._sections_dict={}
        self._current_table_list=[]
        self._last_chosen_row=-1
        #build data from the json file
        file_name='books.json'
        with open(file_name,'r') as file:
            data=json.load(file)
            #add book in O(number of books in file) ,one loop iteration
            for title,content in data.items():
                section_name=content["section"]
                author=content["author"]
                cost=content["cost"]
                book=Book(title,author,cost)
                if section_name in self._sections_dict:
                    #section already created ,just add book
                    self._sections_dict[section_name].addBook(book)
                else:
                    #create new section and append to self._sections
                    section=Section(section_name)
                    self._sections_dict[section_name]=section
                    self.addSection(section)
                    section.addBook(book)
        #init UI
        self.init_ui()
        self.refresh_ui_data()
    def getTitle(self):
        return self._title
    def addSection(self,section):
        self._sections.append(section)
        
    def searchBookByTitle(self,title):
        '''searches for a book by title in all sections
            returns (section,book)ojbects tuple if found
                    None if not found'''
        for section in self._sections:
            book=section.searchBookByTitle(title)
            if book is not None:
                return (section,book)
        return None
    def searchBookByAuthor(self,title):
        '''returns list for all available books by Author title ,from all sections'''
        data=[]
        for section in self._sections:
            books=section.searchBookByAuthor(title)
            if len(books) >0:
                data+=books
        return data
    def sellaBook(self,title):
        '''sell book ,update profit and remove book from memory'''
        section,book=self.searchBookByTitle(title)
        self._profit+=book.getCost()
        section.deleteBook(book.getTitle())
        
    def getTotalProfit(self):
        return self._profit
    #ui stuff
    def refresh_ui_data(self):
        '''reupdate table and totalProfi label'''
        data=[]
        for section in self._sections:
            data+=section.showBooks()
        self.build_books_table(data)
        self.ui.profitLabel.setText(str(self.getTotalProfit()))
    def init_ui(self):
        self.app = QtWidgets.QApplication([])
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.setWindowTitle(self._title)
        self.ui.booksTable.setColumnWidth(0,300)
        self.ui.booksTable.setColumnWidth(2,180)
        self.ui.booksTable.setColumnWidth(3,90)
        self.ui.refreshButton.clicked.connect(lambda: self.refresh_btn_clicked())
        self.ui.searhAuthorBtn.clicked.connect(lambda: self.searchAuthor_btn_clicked())
        self.ui.searhTitleBtn.clicked.connect(lambda: self.searchTitle_btn_clicked())
        self.ui.booksTable.cellClicked.connect(self.getClickedCell)
        self.ui.pushButton_3.clicked.connect(lambda: self.sell_btn_clicked())
    def build_books_table(self,data):
        '''build booksTable from gived 2d list data'''
        self.ui.booksTable.setRowCount(len(data))
        
        #pprint(data)
        row_idx=0
        for row in data:
            self.ui.booksTable.setItem(row_idx,0,QtWidgets.QTableWidgetItem(row[0]))
            self.ui.booksTable.setItem(row_idx,1,QtWidgets.QTableWidgetItem(row[1]))
            self.ui.booksTable.setItem(row_idx,2,QtWidgets.QTableWidgetItem(row[2]))
            self.ui.booksTable.setItem(row_idx,3,QtWidgets.QTableWidgetItem(str(row[3])))
            row_idx+=1
        self._current_table_list=data
        self._last_chosen_row=-1
    def refresh_btn_clicked(self):
        print('refreshing..')
        self.refresh_ui_data()
    def searchAuthor_btn_clicked(self):
        authorName=self.ui.searchField.text()
        authorName=authorName.lstrip().rstrip()
        if authorName=='':
            self.refresh_ui_data()
        else:
            
            data=self.searchBookByAuthor(authorName)
            print('here')
            self.build_books_table(data)
    def searchTitle_btn_clicked(self):
        titleName=self.ui.searchField.text()
        titleName=titleName.lstrip().rstrip()
        pack=self.searchBookByTitle(titleName)
        if pack is not None:
            section,book=pack
            data=[[book.getTitle(),book.getAuthor(),section.getTitle(),book.getCost()]]
            self.build_books_table(data)
        else:
            #not found book title
            pass
    def getClickedCell(self, row, column):
        self._last_chosen_row=row
    def sell_btn_clicked(self):
        if self._last_chosen_row !=-1:
            self.sellaBook(self._current_table_list[self._last_chosen_row][0])
        self.refresh_ui_data()
    def start_all(self):
        '''starts UI and any remaining tasks'''
        self.MainWindow.show()
        self.app.exec_()
if __name__=='__main__':
    print('Testing..')
    mylib=Library('QT Lib')
    print(mylib.searchBookByAuthor("Lucy Maud"))
    mylib.start_all()
    #continued in the shell and cmds,manual testing
    
