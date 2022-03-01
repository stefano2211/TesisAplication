from django.http import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework import viewsets
from rest_framework import generics
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from django.db.models import Q

from .models import *
from .serializer import *

class BanksListView(APIView):
    def get(self, request,*args, **kwargs):
        bank = CodeBank.objects.all()
        serializers = CodeBankSerializer(bank, many=True)
        return Response(serializers.data)

    def post(self, request, *args, **kwargs):
        serializer = CodeBankSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CodeSpendView(APIView):
    def get(self, request,*args, **kwargs):
        spend = CodeExpenses.objects.all()
        serializers = CodeSpendSerializer(spend, many=True)
        return Response(serializers.data)

    def post(self, request, *args, **kwargs):
        serializer = CodeSpendSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class CodesIncomeView(APIView):
    def get(self, request,*args, **kwargs):
        income = CodeIncome.objects.all()
        serializers = CodeIncomeSerializer(income, many=True)
        return Response(serializers.data)

    def post(self, request, *args, **kwargs):
        serializer = CodeIncomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class IncomeView(APIView):
    def get(self, request,*args, **kwargs):
        income = Income.objects.all()
        serializers = IncomeSerializer(income, many=True)
        return Response(serializers.data)

    def post(self, request, *args, **kwargs):
        serializer = IncomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class ExpensesView(APIView):
    def get(self, request,*args, **kwargs):
        expenses = Expenses.objects.all()
        serializers = ExpensesSerializer(expenses, many=True)
        return Response(serializers.data)

    def post(self, request, *args, **kwargs):
        serializer = ExpensesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)




@api_view(['GET', 'DELETE'])
def getDetailExpenses(request, pk=None):
    if request.method == 'GET':
        expenses = Expenses.objects.filter(id = pk).first()
        expensesSerializer = ExpensesSerializer(expenses)
        return Response(expensesSerializer.data)

    elif request.method == 'DELETE':
        expenses = Expenses.objects.filter(id = pk).first()
        expenses.delete()
        return Response('Eliminado')

@api_view(['GET', 'DELETE'])
def getDetailIncomes(request, pk=None):
    if request.method == 'GET':
        income = Income.objects.filter(id = pk).first()
        incomeSerializer = IncomeSerializer(income)
        return Response(incomeSerializer.data)

    elif request.method == 'DELETE':
        expenses = Income.objects.filter(id = pk).first()
        expenses.delete()
        return Response('Eliminado')

@api_view(['GET', 'DELETE'])
def getDetailCodeBank(request, pk=None):
    if request.method == 'GET':
        CodeBanks = CodeBank.objects.filter(id = pk).first()
        BankSerializer = CodeBankSerializer(CodeBanks)
        return Response(BankSerializer.data)

    elif request.method == 'DELETE':
        Bank = CodeBank.objects.filter(id = pk).first()
        Bank.delete()
        return Response('Eliminado')

@api_view(['GET', 'DELETE'])
def getDetailCodeIncome(request, pk=None):
    if request.method == 'GET':
        CodeIncomes = CodeIncome.objects.filter(id = pk).first()
        IncomeSerializer = CodeIncomeSerializer(CodeIncomes)
        return Response(IncomeSerializer.data)

    elif request.method == 'DELETE':
        Bank = CodeIncome.objects.filter(id = pk).first()
        Bank.delete()
        return Response('Eliminado')

@api_view(['GET', 'DELETE'])
def getDetailCodeExpenses(request, pk=None):
    if request.method == 'GET':
        CodeExpense = CodeExpenses.objects.filter(id = pk).first()
        ExpensesSerializer = CodeSpendSerializer(CodeExpense)
        return Response(ExpensesSerializer.data)

    elif request.method == 'DELETE':
        CodeExpense = CodeExpenses.objects.filter(id = pk).first()
        CodeExpense.delete()
        return Response('Eliminado')






class TotalExpenses(APIView):
    def get(self, request,*args, **kwargs):
        Expense = Expenses.objects.filter(typeMoney="USD")
        serializers = ExpensesSerializers(Expense, many=True)
        return Response(serializers.data)

class TotalExpensesBs(APIView):
    def get(self, request,*args, **kwargs):
        Expense = Expenses.objects.filter(typeMoney="BS")
        serializers = ExpensesSerializers(Expense, many=True)
        return Response(serializers.data)

class TotalIncomeUSD(APIView):
    def get(self, request,*args, **kwargs):
        Incomes = Income.objects.filter(typeMoney="USD")
        serializers = IncomeSerializers(Incomes, many=True)
        return Response(serializers.data)

class TotalIncomeBS(APIView):
    def get(self, request,*args, **kwargs):
        Incomes = Income.objects.filter(typeMoney="BS")
        serializers = IncomeSerializers(Incomes, many=True)
        return Response(serializers.data)

class TotalBankUSD(APIView):
    def get(self, request,*args, **kwargs):
        Banks = CodeBank.objects.filter(type="Dolares")
        serializers = BankSerializers(Banks, many=True)
        return Response(serializers.data)

class TotalBankBS(APIView):
    def get(self, request,*args, **kwargs):
        Banks = CodeBank.objects.filter(type="Bolivares")
        serializers = BankSerializers(Banks, many=True)
        return Response(serializers.data)
