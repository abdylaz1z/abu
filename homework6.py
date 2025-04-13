import sqlite3

class Library:
    def __init__(self, db_name='library_db.sqlite'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT
            )
        """)

    def add_book(self):
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        self.cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
        self.connection.commit()

    def delete_book(self, id):
        self.cursor.execute("DELETE FROM books WHERE id = ?", (id,))
        self.connection.commit()
        print(f"Книга с id {id} успешно удалена.")

    def list_books(self):
        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()
        for book in books:
            print(book)

library = Library()
library.add_book()
library.list_books()
