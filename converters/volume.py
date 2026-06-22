"""Volume unit converter"""

class VolumeConverter:
    """Convert between different volume units"""
    
    # Conversion factors to liters
    UNITS = {
        'milliliter': 0.001,
        'liter': 1,
        'gallon': 3.78541,
        'quart': 0.946353,
        'pint': 0.473176,
        'cup': 0.236588,
        'fluid_ounce': 0.0295735,
        'tablespoon': 0.0147868,
        'teaspoon': 0.00492892,
    }
    
    @staticmethod
    def convert(value, from_unit, to_unit):
        """Convert volume from one unit to another"""
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in VolumeConverter.UNITS:
            raise ValueError(f"Unknown unit: {from_unit}")
        if to_unit not in VolumeConverter.UNITS:
            raise ValueError(f"Unknown unit: {to_unit}")
        
        # Convert to liters first, then to target unit
        liters = value * VolumeConverter.UNITS[from_unit]
        result = liters / VolumeConverter.UNITS[to_unit]
        
        return round(result, 6)
    
    @staticmethod
    def get_units():
        """Get list of available units"""
        return list(VolumeConverter.UNITS.keys())
