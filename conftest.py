import pytest

@pytest.fixture # фикстура, которая создаёт книгу
def book():
    book = ['Алиса в стране чудес', 'Скотный двор', '1984']
    return book


@pytest.fixture
def books_genre():
    books_genre = ['Фантастика', 'Роман', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    return books_genre


@pytest.fixture
def favorites_books():
    favorites_books = ['Меч и магия', 'Джейн Эйр']
    return favorites_books
