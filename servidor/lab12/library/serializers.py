import json
from rest_framework import serializers
from .models import Book, Author, User, Lend


class AuthorSerializer(serializers.Serializer):

    class Meta:
        model = Author
        fields = "__all__"

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    nationality = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.natioanlity = validated_data.get(
            'nationality', instance.natioanlity)

        instance.save()
        return instance


class BookSerializer(serializers.Serializer):

    class Meta:
        model = Book
        fields = "__all__"

    id = serializers.IntegerField(read_only=True)
    code = serializers.IntegerField(read_only=True)
    tittle = serializers.CharField(read_only=True)
    isbn = serializers.CharField(read_only=True)
    editorial = serializers.CharField(read_only=True)
    pageNumber = serializers.IntegerField(read_only=True)
    author = AuthorSerializer()
    # authorObj = serializers.JSONField()


class createBookSerializer(serializers.Serializer):

    class Meta:
        model = Book
        fields = "__all__"

    id = serializers.IntegerField(read_only=True)
    tittle = serializers.CharField(read_only=True)
    code = serializers.IntegerField(read_only=True)
    isbn = serializers.CharField(read_only=True)
    editorial = serializers.CharField(read_only=True)
    pageNumber = serializers.IntegerField(read_only=True)
    author = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.code = validated_data.get('code', instance.code)
        instance.tittle = validated_data.get(
            'tittle', instance.tittle)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.editorial = validated_data.get(
            'editorial', instance.editorial)
        instance.pageNumber = validated_data.get(
            'page_number', instance.pageNumber)
        instance.author = validated_data.get(
            'author', instance.author)

        instance.save()
        return instance


class UserSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = "__all__"

    id = serializers.IntegerField(read_only=True)
    numUser = serializers.IntegerField(read_only=True)
    dni = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    address = serializers.CharField(read_only=True)
    phoneNumber = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.numUser = validated_data.get(
            'user_number', instance.numUser)
        instance.dni = validated_data.get('dni', instance.dni)
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.phoneNumber = validated_data.get(
            'phone_number', instance.phoneNumber)

        instance.save()
        return instance


class LendSerializer(serializers.Serializer):

    class Meta:
        model = Lend
        fields = "__all__"

    id = serializers.IntegerField(read_only=True)
    # bookObj = serializers.ReadOnlyField()
    book_id = BookSerializer()
    # userObj = serializers.ReadOnlyField()
    user_id = UserSerializer()
    lendDate = serializers.CharField(read_only=True)
    returnDate = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return Lend.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.book_id = validated_data.get('book', instance.book_id)
        instance.user_id = validated_data.get(
            'user', instance.user_id)
        instance.lendDate = validated_data.get('lend_date', instance.lendDate)
        instance.returnDate = validated_data.get(
            'return_date', instance.returnDate)
        instance.save()
        return instance


class createLendSerializer(serializers.Serializer):

    class Meta:
        model = Lend
        fields = "__all__"

    id = serializers.IntegerField(read_only=True)
    book_id = serializers.ReadOnlyField()
    # book_id = serializers.IntegerField(default=1)
    user_id = serializers.ReadOnlyField()
    # user_id = serializers.IntegerField(default=1)
    lendDate = serializers.CharField(read_only=True)
    returnDate = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return Lend.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.book_id = validated_data.get('book_id', instance.book_id)
        instance.user_id = validated_data.get(
            'user_id', instance.user_id)
        instance.lendDate = validated_data.get('lend_date', instance.lendDate)
        instance.returnDate = validated_data.get(
            'return_date', instance.returnDate)
        instance.save()
        return instance
