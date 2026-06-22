"""Length unit converter"""

class LengthConverter:
    """Convert between different length units"""
    
    # Conversion factors to meters
    UNITS = {
        'millimeter': 0.001,
        'centimeter': 0.01,
        'meter': 1,
        'kilometer': 1000,
        'inch': 0.0254,
        'foot': 0.3048,
        'yard': 0.9144,
        'mile': 1609.34,
    }
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        """Convert length from one unit to another"""
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in LengthConverter.UNITS:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in LengthConverter.UNITS:
            raise ValueError(f"Unknown unit: {to_unit}")
        
        # Convert to meters first, then to target unit
        meters = value * LengthConverter.UNITS[from_unit]
        result = meters / LengthConverter.UNITS[to_unit]
        
        return round(result, 6)
    
    @staticmethod
    def get_units():
        """Get list of available units"""
        return list(LengthConverter.UNITS.keys())
