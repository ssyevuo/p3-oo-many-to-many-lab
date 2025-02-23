class Author:
    all_authors = []
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return list(set(contract.book for contract in self.contracts()))

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

class Book:
    all_books = [] #tracks all books
    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        self.title = title
        Book.all_books.append(self) #add books to the all_books list

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return list(set(contract.author for contract in self.contracts()))

class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    
    @classmethod
    def contracts_by_date(cls, date):
        return sorted(
            [contract for contract in cls.all if contract.date == date],
            key=lambda c: c.date
        )