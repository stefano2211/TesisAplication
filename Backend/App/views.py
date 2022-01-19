from django.http import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework import viewsets
from rest_framework import generics
\

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
