import grpc
from proto_compiled import book_pb2
from proto_compiled import book_pb2_grpc


def call_add_book():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = book_pb2_grpc.BookServiceStub(channel)
        book = book_pb2.Book(
            title="The Great Gatsby",
            author="F. Scott Fitzgerald",
            year_published=1925,
            genres=["Fiction"],
        )
        request = book_pb2.AddBookRequest(book=book)
        # Call the AddBook method on the server
        response = stub.AddBook(request)
        print(request)
        print(response)


def call_get_book(id):
    # Open a gRPC channel
    with grpc.insecure_channel("localhost:50051") as channel:
        # Create a stub for the book service
        stub = book_pb2_grpc.BookServiceStub(channel)

        # Create a GetBookRequest message
        request = book_pb2.GetBookRequest(id=id)

        # Call the GetBook method on the server
        response = stub.GetBook(request)

        # Return the Book message from the response
        print(request)
        print(response)
        return response


def update_book(book_id, title, author, year_published, genres):
    channel = grpc.insecure_channel("localhost:50051")
    stub = book_pb2_grpc.BookServiceStub(channel)

    try:
        book = book_pb2.Book(
            id=book_id,
            title=title,
            author=author,
            year_published=year_published,
            genres=genres,
        )

        # Create a request message with the book to update
        request = book_pb2.UpdateBookRequest(book=book)

        # Call the UpdateBook RPC with the request
        response = stub.UpdateBook(request)

        # Return the updated book as a dictionary
        print(response)
        return response
    except Exception as e:
        raise


def list_books():
    # create a gRPC channel and stub
    channel = grpc.insecure_channel("localhost:50051")
    stub = book_pb2_grpc.BookServiceStub(channel)

    # create a request message
    request = book_pb2.ListBooksRequest()

    try:
        # call the gRPC service method
        response = stub.ListBooks(request)
        print(response)  # prints a list of Book messages
    except grpc.RpcError as e:
        print(f"Error: {e}")


def delete_book(book_id):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = book_pb2_grpc.BookServiceStub(channel)
        request = book_pb2.DeleteBookRequest(id=book_id)
        response = stub.DeleteBook(request)
        print(response)


# call_add_book()
# call_add_book()
# call_get_book(1)
# delete_book(1)
list_books()
# update_book(3,"updated-Title", "J.K", 2001, ["Fantasy"])
# call_get_book(3)
