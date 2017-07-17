from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student, Book, Burrower
from .serializers import StudentSerializer, BookSerializer, BurrowerSerializer


class StudentList(APIView):

    def get(self, requst):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass

