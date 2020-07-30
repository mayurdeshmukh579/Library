class Library:
    def __init__(self,list,name):
        self.booklist=list
        self.name=name
        self.lendDict={}

    def display(self):
        print(f"We have following books in {self.name} libeary")
        for book in self.booklist:
            print(book)

    def lendBook(self,book,user):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Your database is updated.")
        else:
            print(f"Book is already taken by {self.lendDict[book]}")

    def addbook(self,book):
        self.booklist.append(book)
        print("Book is updated to the book list")

    def returnbook(self,book):
        self.booklist.pop(book)

if __name__=='__main__':

    mayur = Library(['harry potter','larry'],"codevita")

    while(True):
        print(f"Welcome to the library of {mayur.name}.Enter your choice to continue")
        print("1.Display Book")
        print("2.Lend a Book")
        print("3.Add a Book")
        print("4.Return a Book")
        user_choice=int(input("Enter your choice hare:"))
        if user_choice==1:
            mayur.display()
        elif user_choice==2:
            book=input("Enter book name:")
            user=input("Enter your name:")

            mayur.lendBook(book,user)
        elif user_choice==3:
            book=input("Enter the book you want to add:")
            mayur.addbook(book)
        elif user_choice==4:
            book=input("Enter the name of book you want to return:")
            mayur.returnbook(book)
        else:
            print("Wrong input.")

        print("Type q for quit and c for continue")
        user_choice2=input("Enter here:")


        while(user_choice2!="q"  and user_choice2!="c"):


            if user_choice2=="q" or "Q":
                exit()
            elif user_choice2=="c" or "C":
                continue




