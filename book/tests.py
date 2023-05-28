import grpc
import unittest
from proto_book import book_pb2
from proto_book import book_pb2_grpc
from django.test import Client
from django.test import TestCase
from book.models import Book
from django_grpc_framework.test import Channel
from django_grpc_framework.test import RPCTestCase


class BookServiceTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.channel = Channel()
        self.book1 = book_pb2.Book(
            id=1,
            title="Book1",
            author="Author1",
            year_published=2000,
            genres=["Genre1"],
        )
        self.book2 = book_pb2.Book(
            id=2,
            title="Book2",
            author="Author2",
            year_published=2001,
            genres=["Genre2"],
        )
        self.book3 = book_pb2.Book(
            id=3,
            title="Book3",
            author="Author3",
            year_published=2002,
            genres=["Genre3"],
        )
        self.book4 = book_pb2.Book(
            id=4,
            title="Book4",
            author="Author4",
            year_published=2003,
            genres=["Genre4"],
        )
        self.book5 = book_pb2.Book(
            id=5,
            title="Book5",
            author="Author5",
            year_published=2005,
            genres=["Genre5"],
        )

    def test_add_book(self):
        # print("#"*10,"testing gRPC method: AddBook","#"*10)
        stub = book_pb2_grpc.BookServiceStub(self.channel)
        request = book_pb2.AddBookRequest(book=self.book1)
        response = stub.AddBook(request)
        # print("Added Book for test.")
        # print(response)
        self.assertEqual(response.id, 1)

    def test_get_book(self):
        # print("#"*10,"testing gRPC method: GetBook","#"*10)
        stub = book_pb2_grpc.BookServiceStub(self.channel)
        request = book_pb2.AddBookRequest(book=self.book2)
        response = stub.AddBook(request)
        # print("Added Book for test.")
        # print(response)
        book_id = response.id
        request = book_pb2.GetBookRequest(id=book_id)
        # print("Getting Book.")
        response = stub.GetBook(request)
        # print(response)
        self.assertEqual(response.book, response.book)

    def test_update_book(self):
        # print("#"*10,"testing gRPC method: UpdateBook","#"*10)
        stub = book_pb2_grpc.BookServiceStub(self.channel)
        request = book_pb2.AddBookRequest(book=self.book1)
        response = stub.AddBook(request)
        book_id = response.id
        # print(response)

        book = book_pb2.Book(
            id=book_id,
            title="Updated Test Book",
            author="Updated Test Author",
            year_published=2024,
            genres=["Non-Fiction"],
        )
        request = book_pb2.UpdateBookRequest(book=book)
        response = stub.UpdateBook(request)

        request = book_pb2.GetBookRequest(id=book_id)
        response = stub.GetBook(request)

        updated_book = response.book
        # print(response)

        self.assertEqual(updated_book.title, book.title)
        self.assertEqual(updated_book.author, book.author)
        self.assertEqual(updated_book.year_published, book.year_published)
        self.assertEqual(updated_book.genres, book.genres)

    def test_delete_book(self):
        # print("#"*10,"testing gRPC method: DeleteBook","#"*10)
        stub = book_pb2_grpc.BookServiceStub(self.channel)
        request = book_pb2.AddBookRequest(book=self.book5)
        response = stub.AddBook(request)
        # print(response)
        book_id = response.id

        request = book_pb2.DeleteBookRequest(id=book_id)
        response = stub.DeleteBook(request)
        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(id=book_id)
        # print(response)
