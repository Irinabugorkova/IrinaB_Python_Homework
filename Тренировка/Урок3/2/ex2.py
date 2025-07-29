from book import Book

library = [
    Book("Мастер и Маргарита", "Булгаков М.А."),
    Book("Обломов", "Гончаров И.А."),
    Book("Никогда не спорьте с идиотами!", "Твен М.")
]

for book in library:
    print(f"{book.title} - {book.author}")