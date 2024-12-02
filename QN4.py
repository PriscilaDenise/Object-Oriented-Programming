class Author:
    def __init__ (self, name, nationality):
        self.name = name
        self.nationality = nationality

class Book (Author):
    def __init__ (self,name, nationality, title, genre, availabilty):
        super().__init__(name, nationality)
        self.title = title
        self.genre = genre
        self.availabilty = availabilty

    def borrow_book(self):
        if self.availabilty == True:
            self.availabilty = False
            print(f"{self.title} has been borrowed.")
        else:
            print(f"{self.title} is not available.")
        
    def display_info(self):
        print(f"Title: {self.title}\nAuthor: {self.name}\nAvailability: {self.availabilty}")
        

BK1 = Book('Peter. K', 'Ugandan', 'Python Programming', 'Programming', True)
BK1.borrow_book()
BK1.display_info()