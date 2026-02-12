from django.shortcuts import render
# this part is allowing to add indexes to a project
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

def index(request):
# Query the database for a list of ALL categories currently stored.
# Order the categories by the number of likes in descending order.
# Retrieve the top 5 only -- or all if less than 5.
# Place the list in our context_dict dictionary (with our boldmessage!)
# that will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]
    popular_pages=Page.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = popular_pages
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')
def show_category(request, category_name_slug):
# Create a context dictionary which we can pass
# to the template rendering engine.
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
    # We get here if we didn't find the specified category.
    # Don't do anything -
    # the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['pages'] = None
    # Go render the response and return it to the client.
    return render(request, 'rango/category.html', context=context_dict)
