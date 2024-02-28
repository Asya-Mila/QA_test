from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('name', ['Оно'])
    def test_set_book_genre_positive(self, name):  # 2
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Ужасы')
        assert collector.get_book_genre('Оно') == 'Ужасы'

    @pytest.fixture(autouse=True)
    def test_add_new_book_on_the_list_positive(self, book):  # 3
        assert book == ['Алиса в стране чудес', 'Скотный двор', '1984']

    def test_add_new_book_one_from_the_list_negative(self, book):  # 4
        assert '1984' in book

    def test_get_books_genre_negative(self, books_genre):  # 5
        assert 'Аниме' not in books_genre

    @pytest.mark.parametrize('name', ['', 'Сказка о Тройке Авторы: Аркадий и Борис C.'])
    def test_add_new_book_with_invalid_name(self, name):  # 6
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    def test_add_book_in_favorites_positive(self):  # 7
        collector = BooksCollector()
        collector.add_new_book('Норвежский лес')
        collector.add_book_in_favorites('Норвежский лес')
        assert collector.get_list_of_favorites_books() == ['Норвежский лес']

    def test_get_list_of_favorites_books_negative(self, favorites_books):  # 8
        assert '1984' not in favorites_books

    def test_delete_book_from_favorites_positive(self):  # 9
        collector = BooksCollector()
        collector.add_new_book('Марсианин')
        collector.add_book_in_favorites('Марсианин')
        collector.delete_book_from_favorites('Марсианин')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_books_with_specific_genre_positive(self):  # 10
        collector = BooksCollector()
        one_book = 'Мастер и Маргарита'
        collector.add_new_book(one_book)
        collector.set_book_genre(one_book, 'Детективы')
        assert one_book in collector.get_books_with_specific_genre('Детективы')

    def test_get_books_for_children_positive(self):  # 11
        collector = BooksCollector()
        collector.add_new_book('Алладин')
        collector.set_book_genre('Алладин', 'Мультфильмы')
        assert len(collector.get_books_for_children()) == 1 and collector.get_book_genre('Алладин') == 'Мультфильмы'
