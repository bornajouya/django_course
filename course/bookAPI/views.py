from django.shortcuts import render
import sys, os

# Create your views here.
from django.shortcuts import render, HttpResponse
from loginAPI.models import Book,Users
from django.http import JsonResponse
import json
from datetime import datetime, timedelta
from django.db.models import Q
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def book_list(request):
    if request.method == "GET":

        try:
            book_list = list(Book.objects.filter().values())

            for x in book_list:
                x['photo'] = "http://127.0.0.1:8000/media/" + x['photo']

            return JsonResponse(book_list, safe=False, status=200)
        except:
            return JsonResponse({"info": "internal eroro"}, safe=False, status=500)


    elif request.method == "POST":
        try:
            data = request.body.decode("utf-8")
            data = json.loads(data)

        except Exception as es:
            return JsonResponse({"info": "internal error","Error":str(es)}, safe=False, status=500)


        id = data['id']
        print(id)

        # user_ins = Users.objects.get(id=id)

        try:
            book_list = list(Book.objects.filter(author_fk__id=id).values())

            for x in book_list:
                x['photo'] = "http://127.0.0.1:8000/media/" + x['photo']

            return JsonResponse(book_list, safe=False, status=200)
        except:
            return JsonResponse({"info": "internal eroro"}, safe=False, status=500)

@csrf_exempt
def comission(price):
    return price - (price * 20 / 100)

@csrf_exempt
def sp_book(request):
    if request.method == "GET":
        # query
        id = 2

        book_ins = Book.objects.get(id=2)

        print(comission(book_ins.price))
        # MyObject.objects.filter(entered__gte=datetime.now() - timedelta(days=how_many_days))
        book_query = list(Book.objects.annotate(totalprice=F('price')).values()
                          .filter(Q(datetime__gte=datetime.now() - timedelta(days=2))
                                  | Q(name__icontains="م")))

        print(book_query)
        return JsonResponse({"books": list(book_query)}, safe=False, status=200)

@csrf_exempt
def create(request):
    if request.method == "POST":
        try:
            name = str(request.POST.get('name'))
            price = str(request.POST.get('price'))
            pages = str(request.POST.get('pages'))

            Book_ins = Book(name=name)
            Book_ins.price = price
            Book_ins.pages = pages
            Book_ins.save()

            return JsonResponse({"info": f"{name} {price} {pages}"}, status=200)

        except Exception as es:
            exc_type, exc_obj, exc_tb = sys.exc_info()

            return JsonResponse({"info": "internal error","Error":str(es)+str(exc_tb.tb_lineno)}, safe=False, status=500)



    else:
        return HttpResponse(403)


@csrf_exempt
def uploadphoto(request):
    if request.method == "POST":
        try:
            file = request.FILES['file_key']
            book_id = request.POST.get('book_id')

        except Exception as es:
            exc_type, exc_obj, exc_tb = sys.exc_info()

            return JsonResponse({"info": "internal error","Error":str(es)+str(exc_tb.tb_lineno)}, safe=False, status=500)

        Book_ins = Book.objects.get(id=book_id)
        Book_ins.photo = file
        Book_ins.save()

        return JsonResponse({"info":f"photo uploaded"},status=200)


@csrf_exempt
def delete(request):
    if request.method == "DELETE":
        date = request.body.decode("utf-8")
        date = json.loads(date)
        id = date['id']

        Book.objects.filter(id=id).delete()

        return JsonResponse({"info":"file has been deleted"},status=202)

    else:
        return JsonResponse({"info":"method not allowed"},status=405)



