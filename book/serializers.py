from rest_framework import serializers
from book.models import Book
from proto_compiled import book_pb2


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "year_published", "genres"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        """
        Create and return a new `Book` instance, given the validated data.
        """
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Book` instance, given the validated data.
        """
        instance.title = validated_data.get("title", instance.title)
        instance.author = validated_data.get("author", instance.author)
        instance.year_published = validated_data.get(
            "year_published", instance.year_published
        )
        instance.genres = validated_data.get("genres", instance.genres)
        instance.save()
        return instance


class ProtoBookSerializer(serializers.Serializer):
    def to_internal_value(self, data):
        book = book_pb2.Book()
        book.title = data.get("title", "")
        book.author = data.get("author", "")
        book.year_published = data.get("year_published", 0)
        book.genres.extend(data.get("genres", []))
        return {"book": book}

    def to_representation(self, instance):
        book = instance["book"]
        return {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "year_published": book.year_published,
            "genres": book.genres,
        }
