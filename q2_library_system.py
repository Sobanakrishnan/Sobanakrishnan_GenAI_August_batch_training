def add_book(catalog, book_id, title, author, year):
    catalog[book_id] = (title, author, year)


def borrow_book(catalog, borrowed_books, book_id):
    if book_id in catalog and book_id not in borrowed_books:
        borrowed_books.append(book_id)
        print(f"Borrowed: {catalog[book_id][0]}")
    else:
        print(f"Cannot borrow book_id {book_id}")


def return_book(borrowed_books, book_id):
    if book_id in borrowed_books:
        borrowed_books.remove(book_id)
        print(f"Returned book_id {book_id}")
    else:
        print(f"book_id {book_id} was not borrowed")


def register_member(members, member_id):
    members.add(member_id)


def show_available(catalog, borrowed_books):
    print("Available books:")
    for book_id, details in catalog.items():
        if book_id not in borrowed_books:
            title, author, year = details
            print(f"  {book_id}: {title} by {author} ({year})")


def main():
    catalog = {}
    borrowed_books = []
    members = set()

    add_book(catalog, 1, "The Alchemist", "Paulo Coelho", 1988)
    add_book(catalog, 2, "Clean Code", "Robert C. Martin", 2008)
    add_book(catalog, 3, "Deep Work", "Cal Newport", 2016)
    add_book(catalog, 4, "1984", "George Orwell", 1949)

    register_member(members, "M001")
    register_member(members, "M002")
    register_member(members, "M003")
    register_member(members, "M001")
    print(f"Members: {members}")

    borrow_book(catalog, borrowed_books, 1)
    borrow_book(catalog, borrowed_books, 3)

    return_book(borrowed_books, 1)

    show_available(catalog, borrowed_books)


main()
