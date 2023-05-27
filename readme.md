# Book Shelf Service

The Book Shelf Service is a gRPC service that allows users to manage books. It provides functionality to add, retrieve, update, and delete books using the gRPC protocol.

## Prerequisites

Before getting started with the Book Shelf project, make sure you have the following prerequisites installed on your system:

1. **Python**: Ensure that Python is installed on your machine. You can download the latest version of Python from the official Python website: [python.org](https://www.python.org).

3. **PostgreSQL**: Book Shelf utilizes a PostgreSQL database. Install PostgreSQL and configure it on your machine. You can download PostgreSQL from the official website: [postgresql.org](https://www.postgresql.org). Or you can run it on docker. And dont forget to create the database. 


## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/mehedi-sust/book_shelf_django_gRPC.git
   ```

2. Install the dependencies:
   ```shell
      pip install -r requirements.txt
   ```
3. Generate the protobuf files:

   ```shell
   protoc -I proto --python_out=proto_compiled --grpc_python_out=proto_compiled proto/book.proto
   ```
4. Run the Django development server:
   ```shell
   python manage.py grpcrunserver
   ```

## Usage

The Book Service provides the following gRPC methods:

- **AddBook**: Add a new book to the database.
- **GetBook**: Retrieve information about a specific book.
- **UpdateBook**: Update the information of an existing book.
- **DeleteBook**: Delete a book from the database.
- **ListBooks**: List all books in the database.

To interact with the Book Service, you can use a gRPC client. An example client script (`api_call.py`) is provided in the repository. You can modify this script to make gRPC calls to the Book Service.

## Running Unit Tests

To run the unit tests for the Book Service, follow these steps:

1. Ensure that the project dependencies are installed (refer to the Installation section above).

2. Open a terminal or command prompt and navigate to the project directory.

3. Run the following command to execute the unit tests:

    ```shell
    python manage.py test
    ```

   This command will run all the unit tests defined in the project.

   **Note:** Make sure you have a test database configured in your Django settings for running the tests.


## Contributing

Contributions to the Book Service are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. 

See the [LICENSE](LICENSE) file for more information.
