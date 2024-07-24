from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic, View
from .models import Stock
from .forms import SearchForm, GrowthEstimationForm
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from decimal import Decimal



class IndexView(generic.ListView):
    template_name = "stocks/index.html"
    context_object_name = "stock_list"

    
    def get_queryset(self):
        queryset = Stock.objects.all()
 
        search_text = self.request.GET.get('search_text', '')
        
        if search_text:
            queryset = queryset.filter(ticker__icontains=search_text)
        
        return queryset[:500]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add the search form to the context
        context['search_form'] = SearchForm(self.request.GET)

        return context
    
class DetailView(generic.DetailView):
    model = Stock
    template_name = "stocks/detail.html"
    context_object_name = 'stock'
    
class CompareView(generic.TemplateView):
    template_name = "stocks/compare.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk1 = self.kwargs.get('pk1')
        pk2 = self.kwargs.get('pk2')

        stock1 = get_object_or_404(Stock, pk=pk1)
        stock2 = get_object_or_404(Stock, pk=pk2)

        context['stock1'] = stock1
        context['stock2'] = stock2
        
        context['differences'] = {
            'market_price': stock1.market_price - stock2.market_price,
            'fifty_two_week_high': stock1.fifty_two_week_high - stock2.fifty_two_week_high,
            'fifty_two_week_low': stock1.fifty_two_week_low - stock2.fifty_two_week_low,
            'market_cap': stock1.market_cap - stock2.market_cap,
            'enterprise_value': stock1.enterprise_value - stock2.enterprise_value,
            'total_revenue': stock1.total_revenue - stock2.total_revenue,
            'net_income': stock1.net_income - stock2.net_income,
            'ebitda': stock1.ebitda - stock2.ebitda,
            'pe_ratio': stock1.pe_ratio - stock2.pe_ratio,
            'pb_ratio': stock1.pb_ratio - stock2.pb_ratio,
            'ps_ratio': stock1.ps_ratio - stock2.ps_ratio,
            'earnings_growth': stock1.earnings_growth - stock2.earnings_growth,
            'revenue_growth': stock1.revenue_growth - stock2.revenue_growth,
            'gross_margins': stock1.gross_margins - stock2.gross_margins,
            'ebitda_margins': stock1.ebitda_margins - stock2.ebitda_margins,
            'operating_margins': stock1.operating_margins - stock2.operating_margins,
            'roa': stock1.roa - stock2.roa,
            'roe': stock1.roe - stock2.roe,
            'dividend_rate': stock1.dividend_rate - stock2.dividend_rate,
            'dividend_yield': stock1.dividend_yield - stock2.dividend_yield,
            'payout_ratio': stock1.payout_ratio - stock2.payout_ratio,
            'total_debt': stock1.total_debt - stock2.total_debt,
            'quick_ratio': stock1.quick_ratio - stock2.quick_ratio,
            'current_ratio': stock1.current_ratio - stock2.current_ratio,
            'beta': stock1.beta - stock2.beta,
            'average_volume': stock1.average_volume - stock2.average_volume
        }

        return context
    
class ExpectedGrowthView(View):
    form_class = GrowthEstimationForm
    template_name = 'stocks/expected.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            stock_symbol = form.cleaned_data['stock_symbol']
            years = form.cleaned_data['years']

            # Perform growth calculation
            stock = Stock.objects.get(ticker=stock_symbol)
            current_price = Decimal(stock.market_price)
            estimated_price = current_price * ((1 + Decimal(stock.revenue_growth)) ** Decimal(years))

            context = {
                'form': form,
                'stock_symbol': stock_symbol,
                'years': years,
                'estimated_price': estimated_price
            }
            return render(request, self.template_name, context)
        
        return render(request, self.template_name, {'form': form})
    
    
    
def get_stock_ids(request):
    symbol1 = request.GET.get('symbol1')
    symbol2 = request.GET.get('symbol2')

    try:
        stock1 = get_object_or_404(Stock, ticker=symbol1)
        stock2 = get_object_or_404(Stock, ticker=symbol2)
        
        return JsonResponse({'pk1': stock1.pk, 'pk2': stock2.pk})
    except:
        return JsonResponse({'error': 'One or both stocks not found'}, status=404)

    
    
    
    
    
# Create your views here.
