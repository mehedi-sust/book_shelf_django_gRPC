from django.contrib.auth.models import User
from django_grpc_framework import generics
from book.serializers import BookSerializer
from proto_compiled import book_pb2
from proto_compiled import book_pb2_grpc
import json
from google._upb._message import RepeatedScalarContainer
from book.models import Book


class BookService(generics.ModelService):
    """
    gRPC service that allows books to be added, retrieved, updated or deleted.
    """

    def AddBook(self, request, context):
        try:
            genres = request.book.genres
            json_genres = json.dumps(list(genres))

            data_r = {
                "title": request.book.title,
                "author": request.book.author,
                "year_published": request.book.year_published,
                "genres": json_genres,
            }
            book_serializer = BookSerializer(data=data_r, many=False)
            if book_serializer.is_valid():
                book = book_serializer.save()
                response = book_pb2.AddBookResponse(id=book.id)
                return response
            else:
                print(book_serializer.errors)
                context.set_code(400)
                context.set_details(str(book_serializer.errors))
                return book_pb2.AddBookResponse()
        except Exception as e:
            print(e)
            context.set_code(500)
            context.set_details(str(e))
            return book_pb2.AddBookResponse()

    def GetBook(self, request, context):
        try:
            book = Book.objects.get(id=request.id)
            book_proto = book_pb2.Book(
                id=book.id,
                title=book.title,
                author=book.author,
                year_published=book.year_published,
                genres=json.loads(book.genres),
            )
            response = book_pb2.GetBookResponse(book=book_proto)
            return response
        except Book.DoesNotExist:
            context.set_code(404)
            context.set_details("Book not found")
            response = book_pb2.GetBookResponse()

            return response

    def UpdateBook(self, request, context):
        try:
            req_book = request.book
            genres = req_book.genres
            json_genres = json.dumps(list(genres))
            data_r = {
                "title": req_book.title,
                "author": req_book.author,
                "year_published": req_book.year_published,
                "genres": json_genres,
            }
            book = Book.objects.get(id=req_book.id)
            book_serializer = BookSerializer(instance=book, data=data_r)
            if book_serializer.is_valid():
                book = book_serializer.save()
                return book_pb2.UpdateBookResponse(success=True)
            else:
                context.set_code(400)
                context.set_details(book_serializer.errors)
                return book_pb2.UpdateBookResponse(success=False)
        except Exception as e:
            context.set_code(404)
            print(e)
            context.set_details("Book not found")
            return Empty()

    def DeleteBook(self, request, context):
        try:
            book = Book.objects.get(id=request.id)
            book.delete()
            return book_pb2.DeleteBookResponse(success=True)
        except Book.DoesNotExist:
            context.set_code(404)
            context.set_details("Book not found")
            return book_pb2.DeleteBookResponse(success=False)

    def ListBooks(self, request, context):
        books = Book.objects.all()
        book_protos = []
        for book in books:
            book_proto = book_pb2.Book(
                id=book.id,
                title=book.title,
                author=book.author,
                year_published=book.year_published,
                genres=json.loads(book.genres),
            )
            book_protos.append(book_proto)
        return book_pb2.ListBooksResponse(books=book_protos)
