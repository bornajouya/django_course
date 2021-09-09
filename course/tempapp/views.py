from django.shortcuts import render
from loginAPI.models import Book, Comment
from django.db.models import F
from loginAPI.admin import bookAdmin


def search(input):
    result = list(Book.objects.all().annotate(author_name=F("author_fk__user_name"))
                  .filter(name__icontains=str(input)).values())

    return result


def go_to_search(request):
    flag = False
    query = request.GET.get("query")

    result_list = search(query)
    print(result_list)
    if len(result_list) > 0:
        flag = True
    return flag,result_list


# Create your views here.
def index(request):

    flag , result_list = go_to_search(request)

    if flag:
        contex = {"book": result_list, "title": "Book blog"}
        return render(request, template_name="index.html", context=contex)

    book_query = list(Book.objects.all().annotate(author_name=F("author_fk__user_name")).values())
    contex = {"book": book_query, "title": "Book blog"}

    return render(request, template_name="index.html", context=contex)

from .forms import bookForm
def post(request, id):
    # contex = {"book":book_query,"title":"Book blog"}

    flag, result_list = go_to_search(request)

    if flag:
        contex = {"book": result_list, "title": "Book blog"}
        return render(request, template_name="index.html", context=contex)

    bookform = bookForm(request.GET)

    if bookform.is_valid():

        try:
            comment_ins = Comment(name=str(bookform.cleaned_data['name']), email=bookform.cleaned_data['email'],
                                  text=str(bookform.cleaned_data['message']), book=Book.objects.get(id=id))
            comment_ins.save()
        except Exception as ex:
            print(str(ex))


    else:
        print(str(bookform.errors))
        print(request.GET)

    book_ins = Book.objects.get(id=id)
    jdatetime = bookAdmin.custom(bookAdmin, book_ins)
    comments = list(Comment.objects.filter(book=book_ins).values())
    context = {"book": book_ins, "jdatetime": jdatetime, "comments": comments}
    return render(request, template_name="post.html", context=context)

