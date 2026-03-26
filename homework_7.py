import sqlite3
conn = sqlite3.connect("books.db")
def create_table():
    conn.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
    )
    ''')
    conn.commit()
    print("Таблица создана")
def insert_books():
    books = [
        ("1984", "George Orwell", 1949, "Dystopia", 328, 5),
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction", 281, 3),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic", 180, 4),
        ("Moby Dick", "Herman Melville", 1851, "Adventure", 635, 2),
        ("War and Peace", "Leo Tolstoy", 1869, "Historical", 1225, 1),
        ("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 310, 6),
        ("Crime and Punishment", "Fyodor Dostoevsky", 1866, "Psychological", 671, 2),
        ("Pride and Prejudice", "Jane Austen", 1813, "Romance", 279, 4),
        ("The Catcher in the Rye", "J.D. Salinger", 1951, "Fiction", 277, 3),
        ("Brave New World", "Aldous Huxley", 1932, "Dystopia", 311, 5)
    ]
    conn.executemany('''
    INSERT INTO books (
        name, author, publication_year, genre,
        number_of_pages, number_of_copies
    )
    VALUES (?, ?, ?, ?, ?, ?)
    ''', books)
    conn.commit()
    print("Книги добавлены")
if __name__ == "__main__":
    create_table()
    insert_books()

    conn.close()
    print("Соединение закрыто")