'''
- The library has a catalog of books. Each book has a title, author, and ISBN.  
- A library doesn't just have one copy of a book — it might have 3 copies of 'Clean Code' sitting on the shelf. 
- Each physical copy needs to be tracked separately, because copy #1 might be checked out while copy #2 and #3 are available.
- Members can borrow a copy of a book, if an available copy exists. 
- When they do, we need to track: which member borrowed it, which specific copy, and the due date (2 weeks from borrow date, fixed for now).
- A member can return a book. If it's returned after the due date, calculate a late fee — $0.50 per day late. 
- Don't worry about payment processing, just calculate and report the amount owed.
- Also: a member can only borrow up to 5 books at a time. If they're at the limit, borrowing should fail with a clear reason.
'''

'''IMPROVEMENTS
1. cls not self — classmethods take the class as their first arg, so name it cls to signal that clearly.
2. Reduce coupling — BorrowReturn calling Shelf methods directly means peer classes talking to each other; route it through one owning Library class instead (like on orchestrator).
'''

from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, ISBN):
        self.title=title
        self.author=author
        self.ISBN=ISBN

class BookCopy:
    def __init__(self, book:Book, copy_id, due_date=None, borrowed_by=None):
        self.book=book
        self.copy_id=copy_id
        self.due_date=due_date
        self.borrowed_by=borrowed_by

class Shelf:
    books=[] # Declaring as class attribute, global single shelf for this library
    
    # Using classmethod - consdering the class Shelf as the single global shelf (no instances)
    @classmethod
    def add_book(self, book: BookCopy):
        Shelf.books.append(book)
    
    @classmethod
    def remove_book(self, book: BookCopy):
        Shelf.books.remove(book)

    @classmethod
    def is_available(self, requestedbook: Book):
        for book in Shelf.books:
            if book.book.title==requestedbook.title:
                return book
        else:
            return False
    
class Member:
    def __init__(self, member_id, payment_due, borrowed_count=0):
        self.member_id=member_id
        self.payment_due=payment_due
        self.borrowed_count=borrowed_count

class BorrowReturn:
    borrowed_list=[] # Class attribute, global borrowed list this library
    def borrow_book(self, requestedbook: Book, member: Member):
        available_book = Shelf.is_available(requestedbook)
        if available_book:
            if member.borrowed_count==5:
                print(f"Sorry, maximum borrow count reached for memeber_id: {member.member_id}")
                return False

            Shelf.remove_book(available_book) # Remove book from shelf
            
            available_book.borrowed_by=member.member_id # Update the book copy with member who borrowed it

            today = datetime.now().date()   
            two_weeks_later = today + timedelta(weeks=2)
            available_book.due_date=two_weeks_later # Update the book copy with due date

            member.borrowed_count+=1 # Increment member borrow count

            BorrowReturn.borrowed_list.append(available_book) # Add to the list of borrowed list

            print(f"Your borrow is succesful! Due date is : {available_book.due_date}")
        
        else:
            print("Sorry, book unavailable")
    
    def return_book(self, returnedbook: BookCopy, member: Member):
        
        # Computing dues
        today = datetime.now().date()
        if today>returnedbook.due_date:
            extra_days=(today-returnedbook.due_date).days
            dues=round(extra_days*0.50,2)
            member.payment_due+=dues
        
        # Resetting borrower attributes in bookcopy
        BorrowReturn.borrowed_list.remove(returnedbook)
        returnedbook.due_date=None
        returnedbook.borrowed_by=None
        Shelf.add_book(returnedbook)

        # Decrementing member borrow count
        member.borrowed_count-=1

        print(f"Thanks for returning. Payment due : ${member.payment_due}")


#############
# Driver Code
#############

# Create a shelf
shelf = Shelf()

# Create books
book1 = Book("Harry Potter", "J.K. Rowling", "111")
book2 = Book("The Hobbit", "J.R.R. Tolkien", "222")

# Create physical copies
copy1 = BookCopy(book1, 1)
copy2 = BookCopy(book1, 2)
copy3 = BookCopy(book2, 3)

# Add copies to shelf
shelf.add_book(copy1)
shelf.add_book(copy2)
shelf.add_book(copy3)

# Create members
member1 = Member(101, 0)
member2 = Member(102, 0)

# Borrow/Return manager
library = BorrowReturn()


library.borrow_book(book1, member1)
library.return_book(copy1, member1)


            









    





