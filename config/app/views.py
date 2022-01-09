import datetime

from django.db.models import Sum
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import Expenditure, Bank, Item
from .forms import ExpenseForm, ItemForm, BankForm
from django.utils import timezone

from .filters import ExpenditureFilter


# Create your views here.

# Expenses

class ExpenditureListView(LoginRequiredMixin, ListView):
    context_object_name = 'expenditures'
    login_url = 'login/'
    model = Expenditure
    # paginate_by = 10
    ordering = ["-date"]
    today = datetime.date.today()

    def get_queryset(self):
        queryset = super().get_queryset()
        filter = ExpenditureFilter(self.request.GET, queryset)
        return filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()

        filter = ExpenditureFilter(self.request.GET, queryset)

        context["filter"] = filter
        context['total'] = float(Expenditure.objects.aggregate(Sum('amount')).get('amount__sum', 0.00))
        context['current_month_total'] = float(Expenditure.objects.filter(date__year=self.today.year, date__month=self.today.month).aggregate(Sum('amount')).get('amount__sum', 0.00))

        return context


class ExpenditureDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'expenditure'
    login_url = '/login/'
    model = Expenditure


class ExpenditureCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'app/expenditure_detail.html'
    form_class = ExpenseForm
    model = Expenditure

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)


class ExpenditureUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'app/expense_detail.html'
    form_class = ExpenseForm
    model = Expenditure


class ExpenditureDeleteView(LoginRequiredMixin, DeleteView):
    model = Expenditure
    success_url = reverse_lazy('expenditure_list')


# Item

class ItemCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'app/item_form.html'
    form_class = ItemForm
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_list'] = Item.objects.order_by('-id')
        return context


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'app/item_form.html'
    form_class = ItemForm
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_list'] = Item.objects.order_by('-id')
        return context


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('item')


# Bank Details
class BankListView(LoginRequiredMixin, ListView):
    context_object_name = 'banks'
    login_url = '/login/'
    model = Bank

    def get_queryset(self):
        return Bank.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['bank_bal'] = Bank.objects.aggregate(Sum('opening_bal')).get('opening_bal__sum', 0.00)
        context['exp_total'] = Expenditure.objects.aggregate(Sum('amount')).get('amount__sum', 0.00)
        rem_bal = context['bank_bal'] - context['exp_total']
        if context is not None:
            context['rem_bal'] = float(rem_bal)
        else:
            context['rem_bal'] = 0.00

        context['date_today'] = timezone.now()

        return context


class BankUpdateView(LoginRequiredMixin, UpdateView):
    context_object_name = 'bank'
    login_url = '/login/'
    redirect_field_name = 'app/bank_list.html'
    form_class = BankForm
    model = Bank