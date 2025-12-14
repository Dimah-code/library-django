from django.test import TestCase, Client
from django.urls import reverse

from .models import Book


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Book 1",
            subtitle="Subtitle of Book 1",
            author="Book Author",
            isbn="1234567891123",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "Book 1")
        self.assertEqual(self.book.subtitle, "Subtitle of Book 1")
        self.assertEqual(self.book.author, "Book Author")
        self.assertEqual(self.book.isbn, "1234567891123")

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Book 1")
        self.assertTemplateUsed(response, "books/book_list.html")
