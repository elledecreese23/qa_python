from main import BooksCollector

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
        assert len(collector.get_books_rating()) == 2

    def test_set_book_rating_add_book_rating_6_rating_is_6(self):
        collector = BooksCollector()
        collector.add_new_book('Товарищ')
        collector.set_book_rating('Товарищ', 6)
        assert collector.get_book_rating('Товарищ') == 6

    def test_get_book_rating_book_doesnt_exist_got_rating_is_none(self):
        collector = BooksCollector()
        assert collector.get_book_rating('Страшилки') is None

    def test_add_book_in_favorites_add_book_in_favorites_return_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Страх и ненависть')
        collector.add_book_in_favorites('Страх и ненависть')
        assert collector.get_list_of_favorites_books() == ['Страх и ненависть']

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Страх и ненависть')
        collector.delete_book_from_favorites('Страх и ненависть')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_add_book_in_favorites_book_not_added_in_dictionary(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Новая книга,не из словаря')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_in_list_2_books(self):
        collector = BooksCollector()
        collector.add_new_book('Страх и ненависть')
        collector.add_new_book('Страх и любовь')
        collector.add_book_in_favorites('Страх и ненависть')
        collector.add_book_in_favorites('Страх и любовь')
        assert len(collector.get_list_of_favorites_books())==2


    def test_get_books_with_specific_rating_raiting_is_6_and_2(self):
        collector = BooksCollector()
        collector.add_new_book('Любовь и роботы')
        collector.set_book_rating('Любовь и роботы', 6)
        collector.add_new_book('Роботы и люди')
        collector.set_book_rating('Роботы и люди', 3)
        collector.add_new_book('Смерть и роботы')
        collector.set_book_rating('Смерть и роботы', 6)
        collector.add_new_book('Шляпник')
        collector.set_book_rating('Шляпник', 2)
        new_list=collector.get_books_with_specific_rating(6)
        new_list2=collector.get_books_with_specific_rating(2)
        assert len(new_list)==2 and len(new_list2)==1


    def test_set_book_rating_add_book_rating_out_of_range(self):
        collector=BooksCollector()
        collector.add_new_book('out of range')
        collector.set_book_rating('out of range',13)
        assert collector.get_book_rating('out of range')==1, 'Rating out of range'