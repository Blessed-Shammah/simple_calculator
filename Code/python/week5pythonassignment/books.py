# Base Book class
class Book:
    # Constructor to set up the book
    def __init__(self, title, author, pages):
        self.title = title    # Book title
        self.author = author  # Book author
        self.pages = pages    # Number of pages
        self.is_open = False  # Tracks if book is open

    # Method to open or close the book
    def open_book(self):
        self.is_open = not self.is_open
        if self.is_open:
            return f"{self.title} is now open"
        else:
            return f"{self.title} is now closed"

    # Method to show book details
    def show_info(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

    # Method that will be different in subclasses
    def read(self):
        return f"Reading {self.title} by {self.author}"

# ComicBook subclass
class ComicBook(Book):
    # Constructor adds a new attribute
    def __init__(self, title, author, pages, hero):
        super().__init__(title, author, pages)  # Call parent constructor
        self.hero = hero                       # Comic book hero

    # Override read method
    def read(self):
        return f"Reading {self.title} featuring {self.hero} 🦸"

# Novel subclass
class Novel(Book):
    # Constructor adds a new attribute
    def __init__(self, title, author, pages, genre):
        super().__init__(title, author, pages)  # Call parent constructor
        self.genre = genre                     # Novel genre

    # Override read method
    def read(self):
        return f"Reading {self.title}, a {self.genre} novel 📖"

# Test the classes
def main():
    # Create a comic book and a novel
    comic = ComicBook("Spider-Man", "Stan Lee", 32, "Spider-Man")
    novel = Novel("The Hobbit", "J.R.R. Tolkien", 310, "Fantasy")

    # Show book info
    print("Book Info:")
    print(comic.show_info())
    print(novel.show_info())

    # Test reading (different for each type)
    print("\nReading Books:")
    print(comic.read())
    print(novel.read())

    # Test opening books
    print("\nOpening Books:")
    print(comic.open_book())
    print(novel.open_book())

if __name__ == "__main__":
    main()