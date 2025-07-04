from django.contrib import admin
from .models import ExpenseIncome


@admin.register(ExpenseIncome)
class ExpenseIncomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'amount', 'transaction_type', 'tax', 'tax_type', 'created_at')
    list_filter = ('transaction_type', 'tax_type', 'user')
    search_fields = ('title', 'description')

    # Change admin site branding
admin.site.site_header = "Expense Tracker "
admin.site.site_title = "Expense Tracker Portal"
admin.site.index_title = "Welcome to Expense Tracker Dashboard"




