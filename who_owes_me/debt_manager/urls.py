from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('debts/', views.DebtListView.as_view(), name='debts-list'),
    path('debt/<int:pk>', views.DebtDetailView.as_view(), name='debts-detail'),

    path('debtors/', views.DebtorListView.as_view(), name='debtors-list'),
    path('debtor/<int:pk>', views.DebtorDetailView.as_view(), name='debtors-detail'),

    path('creditors/', views.CreditorListView.as_view(), name='creditors-list'),
    path('creditor/<int:pk>', views.CreditorDetailView.as_view(), name='creditors-detail'),
    path('profile/<int:pk>', views.ProfileDetailView.as_view(), name='profile-detail'),
]
