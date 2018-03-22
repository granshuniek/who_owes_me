from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('debts/', views.DebtListView.as_view(), name='debts'),
    path('debt/<int:pk>', views.DebtDetailView.as_view(), name='debt-detail'),

    path('debtors/', views.DebtorListView.as_view(), name='debtors'),
    path('debtor/<int:pk>', views.DebtorDetailView.as_view(), name='debtor-detail'),

    path('creditors/', views.CreditorListView.as_view(), name='creditors'),
    path('reditor/<int:pk>', views.CreditorDetailView.as_view(), name='creditor-detail'),
]
