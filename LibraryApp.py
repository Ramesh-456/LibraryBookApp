import datetime


class LibraryApp:
    def __init__(self,BookList,HandlerName):
        self.BookList = BookList
        self.HandlerName = HandlerName

    def ShowBookDet(self):
        print("*******************************************************************")
        print("\t  =========The Books In Library===============")
        num = 1
        for Bookname in self.BookList:
            print(f"{num} --> {Bookname}")
            num+=1
        print("*******************************************************************")





    def LendBook(self):
        LibBooks.AvailableBooks()
        global Lenddet
        print("From the Above Books, What you want ? ")
        BookName = str(input("Enter the Book name you want :: ")).capitalize()
        if (BookName in BookNameList):
            LenderName = str(input("Enter your Name :: "))
            print(f"The Book of {BookName} is issued to {LenderName}")
            file = open("BookLib1.txt", "a")
            file.write(f"The Book {BookName} is Taken by {LenderName} @ {datetime.datetime.now()}\n")
            file.close()
            BookNameList.remove(BookName)


        else:

            print("The book is not available")


    def AvailableBooks(self):
        print("\t\t\t============   The Available Books Are :: ===========================")
        num = 1
        for Blist in BookNameList:
            print(f"{num} --> {Blist}")
            num +=1

    def ReturnBook(self):
        ReturnBookName = str(input("Enter the Book Name you Return :: ")).capitalize()
        if((ReturnBookName not in BookNameList) and (ReturnBookName in LibBooks.BookList)):
            Username = input("Enter your Name :: ")
            print(f"The Book of {ReturnBookName} is returned By {Username}")
            file = open("BookLib2.txt", "a")
            file.write(f"The Book {ReturnBookName} is returned by {Username} @ {datetime.datetime.now()}\n")
            file.close()
            BookNameList.append(ReturnBookName)
        else:
            print("The Error can be found, pls enter correct details or try again")

    def LendDet(self):
        f = open("BookLib1.txt")
        content = f.read()
        print(content)

    def ReturnDet(self):
        f = open("Booklib2.txt")
        content = f.read()
        print(content)

    def AddBook(self):
        AddBookname = input("Enter the BookName you want to add :: ").capitalize()
        if AddBookname not in LibBooks.BookList:
            AdderName = input("Enter your name :: ")
            Addingcodeword = int(input("Enter the code to Add Book :: "))
            if (Addingcodeword == 456):
                print("Code word Accpeted ")
                print("The Books is added to library")
                LibBooks.BookList.append(AddBookname)
                BookNameList.append(AddBookname)
                f = open("AddBookDet.txt","a")
                f.write(f"The Book of {AddBookname} is Added into a Library by {AdderName} @ {datetime.datetime.now()}\n")
                f.close()
            else:
                print("Enter the code word correctly")
        else:
            print("the Book is Already present in the Library")

    def RemoveBook(self):
        RemoveBookName = input("Enter the BookName you want to remove  :: ").capitalize()
        if RemoveBookName in LibBooks.BookList:
            RemoverName = input("Enter your name :: ")
            RemovingCodeWord = int(input("Enter the code word to Remove a Book :: "))
            if(RemovingCodeWord == 456):
                print("Code word Accpeted ")
                print("The Books is Removed from library")
                LibBooks.BookList.remove(RemoveBookName)
                BookNameList.remove(RemoveBookName)
                f = open("RemoveBookDet.txt", "a")
                f.write(f"The Book of {RemoveBookName} is Removed from a Library by {RemoverName} @ {datetime.datetime.now()}\n")
                f.close()
            else:
                print("Enter the code word correctly")
        else:
            print("The book isn't available to remove")

    def AddBookDet(self):
        f = open("AddBookDet.txt")
        content = f.read()
        print(content)


    def RemoveBookDet(self):
        f = open("RemoveBookDet.txt")
        content = f.read()
        print(content)



if __name__ == '__main__':
    LibBooks = LibraryApp(["Python","Java","C++","Web","Harrypotter","Marvelcomics"],"Ramesh")
    BookNameList = LibBooks.BookList.copy()


    while True:
        print("""
                                                    Enter 0 to list all Books in Library
                                                    Enter 1 to list all Available Books
                                                    Enter 2 to lend a Book
                                                    Enter 3 to return a book
                                                    Enter 4 to lend Details
                                                    Enter 5 to return book details
                                                    Enter 6 to Add Books
                                                    Enter 7 to Remove Books
                                                    Enter 8 to view AddingBook Details
                                                    Enter 9 to view RemovingBook Details
                                                    Enter 10 to Exit the Program
                                                    
            """)
        Userinput = int(input("Enter any Number from the above ::  "))
        if Userinput not in [0,1,2,3,4,5,6,7,8,9,10]:
            print("Enter the Valid Number...")
        else:
            if Userinput==0:
                LibBooks.ShowBookDet()
            elif Userinput == 1:
                LibBooks.AvailableBooks()
            elif Userinput==2:
                LibBooks.LendBook()
            elif Userinput == 3:
                LibBooks.ReturnBook()
            elif Userinput == 4:
               LibBooks.LendDet()
            elif Userinput == 5:
                LibBooks.ReturnDet()
            elif Userinput == 6:
                LibBooks.AddBook()
            elif Userinput == 7:
                LibBooks.RemoveBook()
            elif Userinput == 8:
                LibBooks.AddBookDet()
            elif Userinput == 9:
                LibBooks.RemoveBookDet()
            else:
                print(f"******      Thanks for Visiting the Library of {LibBooks.HandlerName}      *******")
                break

