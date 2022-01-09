from django.urls import path
from . import views

urlpatterns = [
    path('',views.ExpenditureListView.as_view(),name='expenditure_list'),
    path('expenditure/<int:pk>/',views.ExpenditureDetailView.as_view(),name='expenditure_detail'),
    path('expenditure/new/',views.ExpenditureCreateView.as_view(),name='expenditure_new'),
    path('expenditure/<int:pk>/edit/',views.ExpenditureUpdateView.as_view(),name='expenditure_edit'),
    path('expenditure/<int:pk>/remove/',views.ExpenditureDeleteView.as_view(),name='expenditure_remove'),

    path('item/new/',views.ItemCreateView.as_view(),name='item'),
    path('item/<int:pk>/edit/',views.ItemUpdateView.as_view(),name='item_edit'),
    path('item/<int:pk>/remove/',views.ItemDeleteView.as_view(),name='item_remove'),

    path('banks/',views.BankListView.as_view(),name='banks'),
    path('bank/<int:pk>/edit/',views.BankUpdateView.as_view(),name='bank_edit'),
]
