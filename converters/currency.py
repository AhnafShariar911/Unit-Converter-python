"""Currency converter using live exchange rates"""

import requests

class CurrencyConverter:
    """Convert between different currencies using real-time exchange rates"""
    
    API_URL = "https://api.exchangerate-api.com/v4/latest"
    COMMON_CURRENCIES = [
        'USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'CHF', 'CNY',
        'INR', 'MXN', 'BRL', 'SGD', 'HKD', 'NZD', 'KRW', 'SEK'
    ]
    
    @staticmethod
    def get_exchange_rates(base_currency):
        """Fetch exchange rates for the given base currency"""
        try:
            response = requests.get(f"{CurrencyConverter.API_URL}/{base_currency}")
            response.raise_for_status()
            data = response.json()
            return data.get('rates', {})
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch exchange rates: {str(e)}")
    
    @staticmethod
    def convert(amount, from_currency, to_currency):
        """Convert amount from one currency to another"""
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()
        
        try:
            rates = CurrencyConverter.get_exchange_rates(from_currency)
            
            if to_currency not in rates:
                raise ValueError(f"Unknown currency: {to_currency}")
            
            exchange_rate = rates[to_currency]
            result = amount * exchange_rate
            
            return round(result, 2)
        except Exception as e:
            raise Exception(f"Currency conversion failed: {str(e)}")
    
    @staticmethod
    def get_common_currencies():
        """Get list of common currencies"""
        return CurrencyConverter.COMMON_CURRENCIES
    
    @staticmethod
    def get_all_currencies():
        """Get list of all available currencies"""
        try:
            response = requests.get(f"{CurrencyConverter.API_URL}/USD")
            data = response.json()
            return list(data.get('rates', {}).keys())
        except requests.exceptions.RequestException:
            return CurrencyConverter.COMMON_CURRENCIES
