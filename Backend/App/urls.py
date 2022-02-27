from django.urls import path
from .views import *

app_name="App"

urlpatterns = [
    path('CodesBank/', BanksListView.as_view()),
    path('CodeSpend/', CodeSpendView.as_view()),
    path('CodeIncome/', CodesIncomeView.as_view()),
    path('Income/', IncomeView.as_view()),
    path('Expenses/', ExpensesView.as_view()),


    path('Expenses/<int:pk>/', getDetailExpenses, name= "expenses_detail"),
    path('Income/<int:pk>/', getDetailIncomes, name= "income_detail"),
    path('CodesBank/<int:pk>/', getDetailCodeBank, name= "bank_detail"),
    path('CodeIncome/<int:pk>/', getDetailCodeIncome, name= "code_income_detail"),
    path('CodeSpend/<int:pk>/', getDetailCodeExpenses, name= "code_income_detail"),

    path('Expenses/usd', TotalExpenses.as_view()),
    path('Expenses/bs', TotalExpensesBs.as_view()),

    path('Income/usd', TotalIncomeUSD.as_view()),
    path('Income/bs', TotalIncomeBS.as_view()),
]