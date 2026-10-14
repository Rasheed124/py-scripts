# class LibraryBook:

#     __library_name = "Central Library"
#     __number_registered_books = 0
#     __libray_book_list =  {}

#     def __init__(self, title: str, author: str):

#         if not isinstance(title, str):
#             raise TypeError("Title title must be a string.")
#         if not isinstance(author, str):
#             raise TypeError("author title must be a string.")

#         self.title = title.strip()
#         self.author = author
#         self.__book_id = LibraryBook.generate_book_id()


#     @property
#     def book_id(self):
#         return self.__book_id

#     def add_book(self):
#         if self.book_id not in LibraryBook.__libray_book_list:
#             LibraryBook.__libray_book_list[self.book_id] = {
#                 "libray_name" : LibraryBook.__library_name,
#                 "book_title" : self.title,
#                 "book_author" : self.author
#             }
#             print(f" \"{self.title}\" added successfully in library")
#         else:
#             print("Book already exsits in library")


#     def remove_book(self):
#         if not LibraryBook.__libray_book_list:
#             print("Libray is Empty")
#             return

#         if self.book_id in LibraryBook.__libray_book_list:
#             LibraryBook.__libray_book_list.pop(self.book_id)
#             print("Book remove from the library")

    
#     @classmethod
#     def get_book_details(cls):

#         if not cls.__libray_book_list:
#             print("The Book is empty.")
#             return
        
#         cls.__number_registered_books =  len(cls.__libray_book_list)
        
#         print("\n--- Book Details ---")

#         print(f"--- We have {cls.__number_registered_books} books in the library \n \n")

#         for book_id, details in cls.__libray_book_list.items():
#             library_name = details["libray_name"]
#             book_title = details["book_title"]
#             book_author = details["book_author"]

#             print(f"Library Name: {library_name}")
#             print(f"Book Title: {book_title}")
#             print(f"Book Author: {book_author}")
#             print("-" * 25)

    
#     @staticmethod
#     def generate_book_id():
#         import random
#         import string

#         while True:
#             book_id = "".join(
#                 random.choices(
#                     string.ascii_uppercase + string.digits,
#                     k=8
#                 )
#             )

#             if book_id not in LibraryBook.__libray_book_list:
#                 return book_id

#     @classmethod
#     def get_library_name(cls):
#         return cls.__library_name

#     @classmethod
#     def set_library_name(cls, name):
#         cls.__library_name = name

#     def __str__(self):
#         return f"The {self.title} written by {self.author}"


# book1 = LibraryBook("The nine behaviour", "Rasheed")
# book2 = LibraryBook("Do it OR Leave it", "Adeola")
# book3 = LibraryBook("Learn now or harder later", "Fatimah")



# book1.add_book()
# book2.add_book()
# book3.add_book()

# LibraryBook.__library_name = "Never Library"


# # book1.remove_book()

# LibraryBook.get_book_details()



# # LibraryBook.set_library_name("General Library")


# # book1.add_book()
# # book3.add_book()

# # LibraryBook.get_book_details()





# After Ai review



import random
import string


class LibraryBook:

    library_name = "Central Library"
    __number_registered_books = 0
    __library_book_list = {}

    def __init__(self, title: str, author: str):

        if not isinstance(title, str):
            raise TypeError("Title must be a string.")

        if not isinstance(author, str):
            raise TypeError("Author must be a string.")

        if not title.strip():
            raise ValueError("Title cannot be empty.")

        if not author.strip():
            raise ValueError("Author cannot be empty.")

        self.title = title.strip()
        self.author = author.strip()
        self.__book_id = self.generate_book_id()

    @property
    def book_id(self):
        return self.__book_id

    @classmethod
    def get_library_name(cls):
        return cls.library_name

    @classmethod
    def set_library_name(cls, name):
        if not isinstance(name, str):
            raise TypeError("Library name must be a string.")

        if not name.strip():
            raise ValueError("Library name cannot be empty.")

        cls.library_name = name.strip()

    def add_book(self):
        if self.book_id in LibraryBook.__library_book_list:
            return f'"{self.title}" is already registered.'

        LibraryBook.__library_book_list[self.book_id] = {
            "book_title": self.title,
            "book_author": self.author
        }

        LibraryBook.__number_registered_books = (
            len(LibraryBook.__library_book_list)
        )

        return f'"{self.title}" added successfully.'

    def remove_book(self):
        if self.book_id not in LibraryBook.__library_book_list:
            return f'"{self.title}" is not registered.'

        del LibraryBook.__library_book_list[self.book_id]

        LibraryBook.__number_registered_books = (
            len(LibraryBook.__library_book_list)
        )

        return f'"{self.title}" removed successfully.'

    def display_details(self):
        return (
            f"Book ID: {self.book_id}\n"
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Library: {self.library_name}"
        )

    @classmethod
    def get_book_details(cls):
        if not cls.__library_book_list:
            print("The library is empty.")
            return

        cls.__number_registered_books = len(cls.__library_book_list)

        print("\n--- Library Book Details ---")
        print(f"Library name: {cls.library_name}")
        print(f"Registered books: {cls.__number_registered_books}")
        print("-" * 30)

        for book_id, details in cls.__library_book_list.items():
            print(f"Book ID: {book_id}")
            print(f"Title: {details['book_title']}")
            print(f"Author: {details['book_author']}")
            print(f"Library: {cls.library_name}")
            print("-" * 30)

    @classmethod
    def get_registered_book_count(cls):
        return len(cls.__library_book_list)

    @staticmethod
    def generate_book_id():
        while True:
            book_id = "".join(
                random.choices(
                    string.ascii_uppercase + string.digits,
                    k=8
                )
            )

            if book_id not in LibraryBook.__library_book_list:
                return book_id

    def __str__(self):
        return f'"{self.title}" written by {self.author}'


# -----------------------------------------
# 1. Create three book objects
# -----------------------------------------

book1 = LibraryBook("The Nine Behaviours", "Rasheed")
book2 = LibraryBook("Do It or Leave It", "Adeola")
book3 = LibraryBook("Learn Now or Harder Later", "Fatimah")


# -----------------------------------------
# 2. Register the books
# -----------------------------------------

print(book1.add_book())
print(book2.add_book())
print(book3.add_book())

print("\nRegistered count:", LibraryBook.get_registered_book_count())


# -----------------------------------------
# 3. Display book details
# -----------------------------------------

# print("\n--- Individual Book Details ---")
# print(book1.display_details())
# print()
# print(book2.display_details())
# print()
# print(book3.display_details())


# -----------------------------------------
# 4. Change the class attribute
# -----------------------------------------

print("\n--- Change Shared Library Name ---")

print("Before:", book1.library_name)
print("Before:", book2.library_name)

LibraryBook.set_library_name("General Library")

print("After:", book1.library_name)
print("After:", book2.library_name)
print("Class value:", LibraryBook.library_name)


# -----------------------------------------
# 5. Demonstrate instance attribute shadowing
# -----------------------------------------

print("\n--- Instance Attribute Demonstration ---")

book1.library_name = "Private Collection"

print("Book 1 library:", book1.library_name)
print("Book 2 library:", book2.library_name)
print("Book 3 library:", book3.library_name)
print("Class library:", LibraryBook.library_name)


# -----------------------------------------
# 6. Change the class attribute again
# -----------------------------------------

print("\n--- Change Class Name Again ---")

LibraryBook.set_library_name("National Library")

print("Book 1 library:", book1.library_name)
print("Book 2 library:", book2.library_name)
print("Book 3 library:", book3.library_name)
print("Class library:", LibraryBook.library_name)

# LibraryBook.get_book_details()


# # -----------------------------------------
# # 7. Remove the instance-level attribute
# # -----------------------------------------

# print("\n--- Remove Instance-Level Override ---")

del book1.library_name

print("Book 1 library:", book1.library_name)
print("Class library:", LibraryBook.library_name)


# # -----------------------------------------
# # 8. Display the shared registry
# # -----------------------------------------

LibraryBook.get_book_details()


# # -----------------------------------------
# # 9. Test book removal and counter updates
# # -----------------------------------------

# print("\n--- Remove a Book ---")
# print(book2.remove_book())

# print("Registered count:", LibraryBook.get_registered_book_count())

# LibraryBook.get_book_details()
