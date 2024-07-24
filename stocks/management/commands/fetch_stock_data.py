from django.core.management.base import BaseCommand
import yfinance as yf
from stocks.models import Stock
import requests
from bs4 import BeautifulSoup

class Command(BaseCommand):
    help = "Fetch stock data and fill the model"
    
    def handle(self, *args, **kwargs):
        url = 'https://stockanalysis.com/list/sp-500-stocks/'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        symbol_elements = soup.find_all(class_='sym svelte-eurwtr')
        tickers = [element.get_text(strip=True) for element in symbol_elements]

        for ticker in tickers:
            stock_data = yf.Ticker(ticker).info

            Stock.objects.update_or_create(
                ticker=ticker, 
                defaults={
                    'company_name': stock_data.get('longName', 'N/A'),
                    'sector': stock_data.get('sector', 'N/A'),
                    'market_price': stock_data.get('currentPrice', 0.0),
                    'fifty_two_week_high': stock_data.get('fiftyTwoWeekHigh', 0.0),
                    'fifty_two_week_low': stock_data.get('fiftyTwoWeekLow', 0.0),
                    'market_cap': stock_data.get('marketCap', 0),
                    'enterprise_value': stock_data.get('enterpriseValue', 0),
                    'total_revenue': stock_data.get('totalRevenue', 0),
                    'net_income': stock_data.get('netIncomeToCommon', 0),
                    'ebitda': stock_data.get('ebitda', 0),
                    'pe_ratio': stock_data.get('trailingPE', 0.0),
                    'pb_ratio': stock_data.get('priceToBook', 0.0),
                    'ps_ratio': stock_data.get('priceToSalesTrailing12Months', 0.0),
                    'earnings_growth': stock_data.get('earningsQuarterlyGrowth', 0.0),
                    'revenue_growth': stock_data.get('revenueGrowth', 0.0),
                    'gross_margins': stock_data.get('grossMargins', 0.0),
                    'ebitda_margins': stock_data.get('ebitdaMargins', 0.0),
                    'operating_margins': stock_data.get('operatingMargins', 0.0),
                    'roa': stock_data.get('returnOnAssets', 0.0),
                    'roe': stock_data.get('returnOnEquity', 0.0),
                    'dividend_rate': stock_data.get('dividendRate', 0.0),
                    'dividend_yield': stock_data.get('dividendYield', 0.0),
                    'payout_ratio': stock_data.get('payoutRatio', 0.0),
                    'total_debt': stock_data.get('totalDebt', 0),
                    'quick_ratio': stock_data.get('quickRatio', 0.0),
                    'current_ratio': stock_data.get('currentRatio', 0.0),
                    'beta': stock_data.get('beta', 0.0),
                    'average_volume': stock_data.get('averageVolume', 0)
                }
            )
            
        self.stdout.write(self.style.SUCCESS('Successfully fetched and stored stock data'))
 
            

