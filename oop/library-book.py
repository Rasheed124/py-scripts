class LibraryBook:

    __library_name = "Central Library"
    __number_registered_books = 0
    __libray_book_list =  {}

    def __init__(self, title: str, author: str):

        if not isinstance(title, str):
            raise TypeError("Title title must be a string.")
        if not isinstance(author, str):
            raise TypeError("author title must be a string.")

        self.title = title.strip()
        self.author = author
        self.__book_id = LibraryBook.generate_book_id()


    @property
    def book_id(self):
        return self.__book_id

    def add_book(self):
        if self.book_id not in LibraryBook.__libray_book_list:
            LibraryBook.__libray_book_list[self.book_id] = {
                "libray_name" : LibraryBook.__library_name,
                "book_title" : self.title,
                "book_author" : self.author
            }
            print(f" \"{self.title}\" added successfully in library")
        else:
            print("Book already exsits in library")


    def remove_book(self):
        if not LibraryBook.__libray_book_list:
            print("Libray is Empty")
            return

        if self.book_id in LibraryBook.__libray_book_list:
            LibraryBook.__libray_book_list.pop(self.book_id)
            print("Book remove from the library")

    
    @classmethod
    def get_book_details(cls):

        if not cls.__libray_book_list:
            print("The Book is empty.")
            return
        
        cls.__number_registered_books =  len(cls.__libray_book_list)
        
        print("\n--- Book Details ---")

        print(f"--- We have {cls.__number_registered_books} books in the library \n \n")

        for book_id, details in cls.__libray_book_list.items():
            library_name = details["libray_name"]
            book_title = details["book_title"]
            book_author = details["book_author"]

            print(f"Library Name: {library_name}")
            print(f"Book Title: {book_title}")
            print(f"Book Author: {book_author}")
            print("-" * 25)

    
    @staticmethod
    def generate_book_id():
        import random
        import string

        while True:
            book_id = "".join(
                random.choices(
                    string.ascii_uppercase + string.digits,
                    k=8
                )
            )

            if book_id not in LibraryBook.__libray_book_list:
                return book_id


    def __str__(self):
        return f"The {self.title} written by {self.author}"


book1 = LibraryBook("The nine behaviour", "Rasheed")
book2 = LibraryBook("Do it OR Leave it", "Adeola")
book3 = LibraryBook("Learn now or harder later", "Fatimah")


LibraryBook._

book1.add_book()
book2.add_book()
book3.add_book()

book1.remove_book()

LibraryBook.get_book_details()
