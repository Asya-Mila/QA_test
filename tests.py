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


    def test_get_book_genre_is_ampty_positive(self, collector):    # 3
        collector.add_new_book('Harry Potter')
        assert collector.get_book_genre('Harry Potter') != None


    def test_add_new_book_one_from_the_list_negative(self, collector):# 4
        collector.add_new_book('Book')
        collector.add_new_book('New_Book')
        assert 'Book2' not in collector.get_books_genre()


    @pytest.mark.parametrize('name', ['', 'Сказка о Тройке Авторы: Аркадий и Борис C.'])
    def test_add_new_book_with_invalid_name(self, name):  # 5
        collector = BooksCollector()
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0


    def test_add_book_in_favorites_positive(self):  # 6
        collector = BooksCollector()
        collector.add_new_book('Норвежский лес')
        collector.add_book_in_favorites('Норвежский лес')
        assert collector.get_list_of_favorites_books() == ['Норвежский лес']


    def test_add_book_in_favorites_negative(self, collector ): # 7
        collector.add_new_book('Book1')
        collector.add_new_book('Book2')
        collector.add_book_in_favorites('Book1')
        assert collector.get_list_of_favorites_books() != ['Book2']


    def test_delete_book_from_favorites_positive(self):  # 8
        collector = BooksCollector()
        collector.add_new_book('Марсианин')
        collector.add_book_in_favorites('Марсианин')
        collector.delete_book_from_favorites('Марсианин')
        assert len(collector.get_list_of_favorites_books()) == 0


    def test_delete_book_from_favorites_check_delete_positive(self): # 9
        collector = BooksCollector()
        collector.add_new_book('Литература')
        collector.add_book_in_favorites('Литература')
        collector.add_new_book('Физика')
        collector.add_book_in_favorites('Физика')
        collector.delete_book_from_favorites('Литература')
        assert 'Литература' not in collector.get_list_of_favorites_books()


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