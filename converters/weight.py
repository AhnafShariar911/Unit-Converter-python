"""Weight unit converter"""

class WeightConverter:
    """Convert between different weight units"""
    
    # Conversion factors to kilograms
    UNITS = {
        'milligram': 0.000001,
        'gram': 0.001,
        'kilogram': 1,
        'ounce': 0.0283495,
        'pound': 0.453592,
        'ton': 1000,
    }
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        """Convert weight from one unit to another"""
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in WeightConverter.UNITS:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in WeightConverter.UNITS:
            raise ValueError(f"Unknown unit: {to_unit}")
        
        # Convert to kilograms first, then to target unit
        kilograms = value * WeightConverter.UNITS[from_unit]
        result = kilograms / WeightConverter.UNITS[to_unit]
        
        return round(result, 6)
    
    @staticmethod
    def get_units():
        """Get list of available units"""
        return list(WeightConverter.UNITS.keys())
