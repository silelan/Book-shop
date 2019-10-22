
from django.views.generic import View
from .models import *
from django.conf import settings
from .forms import *
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db.models import Q

class IndexView(View):
    template_name = 'books/index.html'
    
    def get(self, request):
        form = BookInfoForm()
        books = BookInfo.objects.all()
        form1= BookSoldForm()
        booksold = BookSold.objects.filter(~Q(qty_sold = 0))
        for data in booksold:
            print(data.qty_sold)
    
        # sold_count += sold_count
        context = {
            'form':form,
            'books':books,
            'booksold':booksold,
            'form1':form1,
            'year':False
        }
        return render(request,self.template_name,context)
        
    def post(self, request):
        form = BookInfoForm(request.POST)
        books = BookInfo.objects.all()
        form1= BookSoldForm()
        booksold = BookSold.objects.filter(~Q(qty_sold = 0))
        context = {
            'form':form,
            'year':False
        }
        if form.is_valid():
            sold = BookSold(book_id=form.save())
            form.save()
            sold.save()
        return HttpResponseRedirect("")
    # book_id = models.AutoField(primary_key=True)
        

class SoldView(View):

    template_name = 'books/index.html'
    form = BookInfoForm()
    books = BookInfo.objects.all()
    booksold = BookSold.objects.filter(~Q(qty_sold = 0))
    
    def get(self, request):

        context = {
            'form':self.form,
            'books':self.books,
            'booksold':self.booksold,
            'year':False
        }
        # return HttpResponseRedirect("")
        return render(request,self.template_name,context)
    
    def post(self, request):
        # print(request.POST.get('book_id'))
        book = BookSold.objects.filter(book_id=request.POST.get('book_id'))
        count = book[0].qty_sold+1
        book.update(qty_sold=count)
        booksold = BookSold.objects.filter(~Q(qty_sold = 0))
        context = {
            'created': 'done',
            'form':self.form,
            'books':self.books,
            'booksold':booksold,
            'year':False
        }
        # return HttpResponseRedirect("")
        return render(request,self.template_name,context)

class FindView(View):

    template_name = 'books/index.html'
    form = BookInfoForm()
    books = BookInfo.objects.all()
    booksold = BookSold.objects.filter(~Q(qty_sold = 0))
    

    def post(self, request):
        # print(request.POST.get('search_by_year'))
        booksold = BookSold.objects.filter(~Q(qty_sold = 0))
        year = request.POST.get('search_by_year')
        context = {
            'form':self.form,
            'books':self.books,
            'booksold':booksold,
            'year':int(year)
        }
        # return HttpResponseRedirect("")
        return render(request,self.template_name,context)