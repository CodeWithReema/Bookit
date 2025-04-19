from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Book, Branch, Inventory

def index(request):
    return render(request, 'index.html')
# Book Views
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'  # Template to display all books
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'  # Template to display a single book
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    fields = ['author', 'title', 'price']
    template_name = 'book_form.html'  # Template for creating a book
    success_url = reverse_lazy('book-list')

class BookUpdateView(UpdateView):
    model = Book
    fields = ['author', 'title', 'price']
    template_name = 'book_form.html'  # Template for updating a book
    success_url = reverse_lazy('book-list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'  # Template for confirming delete
    success_url = reverse_lazy('book-list')

# Branch Views
class BranchListView(ListView):
    model = Branch
    template_name = 'branch_list.html'
    context_object_name = 'branches'

class BranchDetailView(DetailView):
    model = Branch
    template_name = 'branch_detail.html'
    context_object_name = 'branch'

class BranchCreateView(CreateView):
    model = Branch
    fields = ['name', 'address', 'city', 'state', 'zip', 'phone']
    template_name = 'branch_form.html'
    success_url = reverse_lazy('branch-list')

class BranchUpdateView(UpdateView):
    model = Branch
    fields = ['name', 'address', 'city', 'state', 'zip', 'phone']
    template_name = 'branch_form.html'
    success_url = reverse_lazy('branch-list')

class BranchDeleteView(DeleteView):
    model = Branch
    template_name = 'branch_confirm_delete.html'
    success_url = reverse_lazy('branch-list')

# Inventory Views
class InventoryListView(ListView):
    model = Inventory
    template_name = 'inventory_list.html'
    context_object_name = 'inventory'

class InventoryDetailView(DetailView):
    model = Inventory
    template_name = 'inventory_detail.html'
    context_object_name = 'inventory_item'

class InventoryCreateView(CreateView):
    model = Inventory
    fields = ['book_code', 'branch_code', 'quantity']
    template_name = 'inventory_form.html'
    success_url = reverse_lazy('inventory-list')

class InventoryUpdateView(UpdateView):
    model = Inventory
    fields = ['book_code', 'branch_code', 'quantity']
    template_name = 'inventory_form.html'
    success_url = reverse_lazy('inventory-list')

class InventoryDeleteView(DeleteView):
    model = Inventory
    template_name = 'inventory_confirm_delete.html'
    success_url = reverse_lazy('inventory-list')

