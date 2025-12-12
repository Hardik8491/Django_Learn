from django.shortcuts import render
from django.http import HttpResponse

def students(request):
    students=[
        {'id':1 ,'name':'john doe' ,'age':25},
        {'id':2 ,'name':'john king' ,'age':24}
        ]
    return HttpResponse(students)