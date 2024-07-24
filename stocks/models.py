from django.db import models

class Stock(models.Model):
    ticker = models.CharField(max_length=10, unique=True)
    company_name = models.CharField(max_length=255)
    sector = models.CharField(max_length=255)
    market_price = models.DecimalField(max_digits=10, decimal_places=2)
    fifty_two_week_high = models.DecimalField(max_digits=10, decimal_places=2)
    fifty_two_week_low = models.DecimalField(max_digits=10, decimal_places=2)
    market_cap = models.BigIntegerField(null=True, blank=True)
    enterprise_value = models.BigIntegerField(null=True, blank=True)
    total_revenue = models.BigIntegerField(null=True, blank=True)
    net_income = models.BigIntegerField(null=True, blank=True)
    ebitda = models.BigIntegerField(null=True, blank=True)
    pe_ratio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pb_ratio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ps_ratio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    earnings_growth = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    revenue_growth = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    gross_margins = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ebitda_margins = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    operating_margins = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    roa = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    roe = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    dividend_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    dividend_yield = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    payout_ratio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_debt = models.BigIntegerField(null=True, blank=True)
    quick_ratio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    current_ratio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    beta = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    average_volume = models.BigIntegerField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    longBusinessSummary = models.CharField(max_length=99999)
    
    
    def __str__(self):
        return self.ticker
