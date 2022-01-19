from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(CodeBank)
admin.site.register(CodeExpenses)
admin.site.register(CodeIncome)
admin.site.register(Expenses)
admin.site.register(Income)