from django.db.models import fields
from rest_framework import serializers
from .models import *


class CodeBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeBank
        fields = '__all__'

class CodeSpendSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeExpenses
        fields = '__all__'

class CodeIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeIncome
        fields = '__all__'

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'

class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = '__all__'

class ExpensesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = (
            "typeMoney",
            "price",
        )

class IncomeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = (
            "typeMoney",
            "price",
        )