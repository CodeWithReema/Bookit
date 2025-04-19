from django.urls import path
from .views import (
    index, BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView,
    BranchListView, BranchDetailView, BranchCreateView, BranchUpdateView, BranchDeleteView,
    InventoryListView, InventoryDetailView, InventoryCreateView, InventoryUpdateView, InventoryDeleteView,
)

urlpatterns = [
    # Book URLs
    path('', index, name='index'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/add/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),

    # Branch URLs
    path('branches/', BranchListView.as_view(), name='branch-list'),
    path('branches/<int:pk>/', BranchDetailView.as_view(), name='branch-detail'),
    path('branches/add/', BranchCreateView.as_view(), name='branch-create'),
    path('branches/<int:pk>/edit/', BranchUpdateView.as_view(), name='branch-update'),
    path('branches/<int:pk>/delete/', BranchDeleteView.as_view(), name='branch-delete'),

    # Inventory URLs
    path('inventory/', InventoryListView.as_view(), name='inventory-list'),
    path('inventory/<int:pk>/', InventoryDetailView.as_view(), name='inventory-detail'),
    path('inventory/add/', InventoryCreateView.as_view(), name='inventory-create'),
    path('inventory/<int:pk>/edit/', InventoryUpdateView.as_view(), name='inventory-update'),
    path('inventory/<int:pk>/delete/', InventoryDeleteView.as_view(), name='inventory-delete'),
]