from django.urls import path
from .views import *

app_name="App"

urlpatterns = [
    path('CodesBank/', BanksListView.as_view()),
    path('CodeSpend/', CodeSpendView.as_view()),
    path('CodeIncome/', CodesIncomeView.as_view()),
    path('Income/', IncomeView.as_view()),
    path('Expenses/', ExpensesView.as_view()),
]