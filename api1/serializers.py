from rest_framework import serializers
from .models import Student, Book, Burrower


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields =  '__all__'


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class BurrowerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Burrower
        fields = '__all__'