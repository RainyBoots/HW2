from sre_parse import CATEGORIES
from django.shortcuts import render
from django.http import HttpResponse, Http404


def index(request):
    return HttpResponse("Привет, мир!") # вернет страничку с надписью "Привет, мир!" на русском языке.


def category(request):
    return HttpResponse("Это страница категории.")

CATEGORIES = {
    1: "Чилл территории Python",
    2: "Django, сложно, но можно!",
    3: "Flask, бегите, глупцы!",
}

def blog_catalog(request):
       return HttpResponse("Тут будет блог")
   
def category_list(request):
       categories = ", ".join([str(key) for key in CATEGORIES.keys()])
       return HttpResponse(categories)
   
def category_detail(request, category_id):
    category_id = int(category_id)
    category_str = CATEGORIES.get(category_id)
    if not category_str:
        raise Http404(f"Категория с id={category_id} не найдена")
    return HttpResponse(f"<h1>{category_str}</h1><a href='/category/'>Назад</a>")