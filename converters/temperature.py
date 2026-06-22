"""Temperature unit converter"""

class TemperatureConverter:
    """Convert between different temperature units"""
    
    UNITS = ['celsius', 'fahrenheit', 'kelvin']
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        """Convert temperature from one unit to another"""
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in TemperatureConverter.UNITS:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in TemperatureConverter.UNITS:
            raise ValueError(f"Unknown unit: {to_unit}")
        
        # Convert to Celsius first
        if from_unit == 'celsius':
            celsius = value
        elif from_unit == 'fahrenheit':
            celsius = (value - 32) * 5/9
        elif from_unit == 'kelvin':
            celsius = value - 273.15
        
        # Convert from Celsius to target unit
        if to_unit == 'celsius':
            result = celsius
        elif to_unit == 'fahrenheit':
            result = (celsius * 9/5) + 32
        elif to_unit == 'kelvin':
            result = celsius + 273.15
        
        return round(result, 2)
    
    @staticmethod
    def get_units():
        """Get list of available units"""
        return TemperatureConverter.UNITS
