from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
# -------- Level 1 --------
def view_available_books(library_books):
    """Print all books that are currently available.
    Returns a list of the available book dicts."""
    print("Available Books:")
    available_list = []

    for book in library_books:
        if book["available"] == True:
            print(f"[{book['id']}] {book['title']} — {book['author']}")
            available_list.append(book)

    if len(available_list) == 0:
        print("No books are currently available.")

    return available_list

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
"""
Print and return all books where the author OR genrematches the search. Search is case-insensitive. Returns list of matching book dicts.
"""
"""
U: Must let user type a search word. Then look through all books, return the ones where the author contains that word or the genre contains that word. Probably have to use .lower? So that it'll be case-insensitive.
C: A match can be partial. It must return a list, and also print results. Loop through library books, and yes use .lower().
A: Convert the user's search term to lowercase; then loop over every book dictionary; then convert the author and genre fields to lowercase; then if the search term appears inside the author or genre, it's a match; print it and add it to a results list; finally, return the list when done.
S: write code for this.
E: Double check that it handles upper/lowercase, check that it checks author/genre, if it returns a list, and if it handles 0 results.
"""
def full_books_search(library_books_list, search_term):
    print(f"Search results for '{search_term}': ")
    search_lower = search_term.lower()
    matches = []


    for book in library_books_list:
        author_lower = book["author"].lower()
        genre_lower = book["genre"].lower()

        if search_lower in author_lower or search_lower in genre_lower:
            print(f"[{book['id']}] {book['title']} - {book['author']} ({book['genre']})")
            matches.append(book)

    if len(matches) == 0:
        print("No matching books found.")

    return matches

# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out
"""
U: Need a function that checks out a book using its ID. It shoudl only check when it's available. if it's unavailable or the ID doesn't exist, print a message.
C: Each book is a dictionary w/ keys: ID, available, due date, checkouts. Due date is 2 weeks- 14 days- from today- use datetime. Must update available, due date, and checkouts during checkout. And return true for successful checkout, false for otherwise.
A: Loop through every book in the list. Check if ID matches. If not available- print message. If available, set unavailable, calculate due date, increment checkout counter.
S: Write final code that does all updates & prints confirmation.
E: Test valid ID, book available, valid ID, book already unavailable, invalid ID, and make sure the due date prints in year month day form.
"""
def checkout_book(library_books_list, book_id):
    book_id = book_id.upper() #so that if user inputs something else it'll still be matched
    for book in library_books_list:
        if book["id"] == book_id:
            if book["available"] is False:
                print(f"Book{book_id} ('{book['title']}') is already checked out.")
                return False
            book["available"] = False

            due_date = datetime.today().date() + timedelta(weeks=2) #used ai to help figure out how to achieve add/subtract dates & times & figure out what timedelta is
            book["due_date"] = due_date.strftime("%Y-%m-%d")

            #increase checkoutcounter
            book["checkouts"] += 1 
# Set its availability to True and clear the due_date
            print(f"Checked out [{book['id']}] {book['title']} — due on {book['due_date']}.")
            return True
    print(f"No book found with ID '{book_id}'.")
    return False
#--------- Level 4 --------
# TODO: Create a function to list all overdue books (and another to return a book by ID, resetting the availability and due date)
# A book is overdue if its due_date is before today AND it is still checked out
"""
U: Need to return a book using the ID. If the book is checked out, it's marked as available and due date is cleared. If it's already available or the ID doesn't exist, a different message is printed.
C: Books have id, available, due_date. Returning a book means that available will be true and due date will be none. Also, 3 cases like found & checked out, found but already available, or ID not found at all should be handled.
A: Loop through the list of books, check for a matching ID, if the book is checked out then make availabel true and clear due date, if book is already available then print a message, and if loop ends with no match print no book found.
S: To implement return logic and messages, just write code basically.
E: Test out returning checked-out, already available, and invalid ID cases.
"""
def return_book(library_books_list, book_id):
    # Normalize ID in case user types lowercase
    book_id = book_id.upper()

    for book in library_books_list:
        if book["id"] == book_id:

            # If it's already available, we can't "return" it
            if book["available"] is True:
                print(f"Book {book_id} ('{book['title']}') is already available.")
                return False

            # Mark as returned
            book["available"] = True
            book["due_date"] = None

            print(f"Book {book_id} ('{book['title']}') has been returned.")
            return True

    # If loop is finished with no match, this runs once
    print(f"No book found with ID '{book_id}'.")
    return False

# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!
"""
U: Need to convert each book from dictionary form into a book class. Books should have attributes- with ID, title, author, availability, DDUEH date, checkouts, and methods, with return, checkout, and is_overdue.
Also need a menu system that allows user to view available books, search by author/genre, checkout a book, return a book, view overdue books, and view top 3 most checked out books. The menu should loop until the user decides to quit.
C: Already wrote functions for checking out/returning using dicts. Book objects can hold the same data but make actions easier. Menu requires input, loops, and conditionals. Converting dicts to book objects could be handled by a helper function.
A: Create a book class with checkout, return book, is overdue, and __str__().
Write a converter function to change dictionaries into Book objects. How to do that? Also helper functions for searching, listing availabel books, top 3, overdue books. Make while loop menu that prompts user for actions. Each menu calls correct helper function/BOok method.
S: Just write code-.
E: Test checking out book and make sure due date and availability is updated. Return book and make sure fields reset. Make sure search finds correct results and overdue logic works with past dates, also that menu responds correctly to each number.
"""
#LEVEL 5 START NOWW RAHH ALMOST DONE
#we just went over OOP in my other CS class so I'm good I believe
class Book:
    def __init__(self, id, title, author, genre, available=True, due_date=None, checkouts=0):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date  # "YYYY-MM-DD" or None
        self.checkouts = checkouts

    def checkout(self):
        # Checkout book if available.
        if not self.available:
            print(f"Book {self.id} ('{self.title}') is already checked out.")
            return False

        # due date?
        # that delta thing I have trouble remembering..
        # timedelta!
        due = datetime.today().date() + timedelta(weeks=2)

        self.available = False
        self.due_date = due.strftime("%Y-%m-%d")  # nice clean date wih no hideous decimals yay!
        self.checkouts += 1

        print(f"Checked out [{self.id}] {self.title} - due on {self.due_date}.")
        return True

    def return_book(self):
        # Return book if it's checked out.
        if self.available:
            print(f"Book {self.id} ('{self.title}') is already available.")
            return False

        self.available = True
        self.due_date = None

        print(f"Book {self.id} ('{self.title}') has been returned.")
        return True

    def is_overdue(self):
        # True if due date is less than today AND still checked out.
        if self.available or self.due_date is None:
            return False

        try:
            due = datetime.strptime(self.due_date, "%Y-%m-%d").date()
        except ValueError:
            # If the date format is bad, treat it as not overdue for safety.
            return False

        return due < datetime.today().date()

    def __str__(self):
        status = "Available" if self.available else f"Checked out (Due: {self.due_date})"
        return f"[{self.id}] {self.title} — {self.author} ({self.genre}) [{status}]"
    
#Dictionary to book!
def dicts_to_books(dict_list):
    """Convert the original list of book dictionaries into Book objects."""
    books = []
    for d in dict_list:
        books.append(
            Book(
                id=d["id"],
                title=d["title"],
                author=d["author"],
                genre=d["genre"],
                available=d["available"],
                due_date=d["due_date"],
                checkouts=d["checkouts"],
            )
        )
    return books
#FInd books!

def find_book_by_id(book_list, book_id):
    """Return a Book object with the given ID, or None if not found."""
    book_id = book_id.upper()

    for book in book_list:
        if book.id == book_id:
            return book

    return None

#View books!
def view_available_books(book_list):
    print("Available Books: ")
    available = [b for b in book_list if b.available]
    if not available:
        print("No books are currently available.")
    else:
        for b in available:
            print(str(b))
    return available

#Search books!
def search_books_objects(book_list, search_term):
    search_lower = search_term.lower()
    matches = []

    for b in book_list:
        if search_lower in b.author.lower() or search_lower in b.genre.lower():
            matches.append(b)
    if not matches:
        print(f"No books found matching '{search_term}'.")
    else:
        print(f"Search results for '{search_term}': ")
        for b in matches:
            print(str(b))
    return matches

#Listing overdue books!
def list_overdue_books_objects(book_list):
    overdue = [b for b in book_list if b.is_overdue()]
    if not overdue:
        print("No overdue books.")
    else:
        print("Overdue Books: ")
        for b in overdue:
            print(str(b))
    return overdue

#see top 3 most checked out books
def top_3_viewed(book_list):
    if not book_list:
        print("No books in catalog.")
        return []
    sorted_books = sorted(book_list, key=lambda b: b.checkouts, reverse=True) #lambda for little thing, used google for that
    top_three = sorted_books[:3]
    print("Top 3 most checked out books: ")
    for b in top_three:
        print(f"{b.checkouts} checkouts - {str(b)}")
    return top_three

#Run menu finallyyy!!
def run_menu(book_list):
    while True:
        print("\n***** Library Menu *****")
        print("1. View available books")
        print("2. Search by author or genre")
        print("3. Checkout a book")
        print("4. Return a book")
        print("5. View overdue books")
        print("6. View top 3 most checked out books")
        print("7. Quit menu")

        choice = input("Choose an option (1-7): ").strip()  # remove any spaces
        
        if choice == "1":
            view_available_books(book_list)

        elif choice == "2":
            term = input("Enter author or genre: ").strip()
            search_books_objects(book_list, term)
        
        elif choice == "3":
            book_id = input("Enter book ID to checkout: ").strip()
            book = find_book_by_id(book_list, book_id)
            if book:
                book.checkout()   # <-- fixed
            else:
                print(f"No book found with ID '{book_id}'.")
        
        elif choice == "4":
            book_id = input("Enter book ID to return: ").strip()
            book = find_book_by_id(book_list, book_id)
            if book:
                book.return_book()
            else:
                print(f"No book found with ID '{book_id}'.")
        
        elif choice == "5":
            list_overdue_books_objects(book_list)

        elif choice == "6":
            top_3_viewed(book_list)

        elif choice == "7":
            print("Bye, have a lovely day! Thanks for visiting!")
            break

        else:
            print("Invalid choice. Please enter a number 1-7!")


if __name__ == "__main__":
    # You can use this space to test your functions
    #TESTING LEVEL 5
        book_objects = dicts_to_books(library_books)
        run_menu(book_objects)
"""
        #LEVEL 1
        print("Testing Level 1 of viewing book")
        avail = view_available_books(library_books)
        #TESTING LEVEL 2
        print("Testing Level 2 search function")
        full_books_search(library_books, "fantasy")
        full_books_search(library_books, "Historical")
        full_books_search(library_books, "Romance") 

        #TESTING LEVEL 3
        print("\nTesting Level 3 checkout")
        checkout_book(library_books, "B1") #should checkout and be available
        checkout_book(library_books, "B1") #should say now unavailable
        checkout_book(library_books, "B999") #should be invalid ID

        #TESTING LEVEL 4
        print("\nTesting Level 4 return")
        return_book(library_books, "B1") #should return it successfully
        return_book(library_books, "B1") #should be unavailable now
        return_book(library_books, "XYZ") #should be invalid
        """

