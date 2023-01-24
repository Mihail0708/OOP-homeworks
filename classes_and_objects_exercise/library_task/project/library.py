from library_task.project.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author, book_name, days_to_return, user: User):
        if book_name in self.books_available[author]:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)

            if user.username in self.rented_books:
                self.rented_books[user.username][book_name] = days_to_return
            else:
                self.rented_books[user.username] = {book_name: days_to_return}

            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for key, value in self.rented_books.items():
            if book_name in value:
                return f'The book "{book_name}" is already rented and will be available in {value[book_name]} days!'

    def return_book(self, author, book_name, user: User):
        if book_name in self.rented_books[user.username]:
            user.books.remove(book_name)
            del self.rented_books[user.username][book_name]

            if author in self.books_available:
                self.books_available[author].append(book_name)
            else:
                self.books_available[author] = [book_name]

        else:
            return f"{user.username} doesn't have this book in his/her records!"

