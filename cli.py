"""Command-line interface for Unit Converter"""

from converters import (
    LengthConverter, WeightConverter, TemperatureConverter,
    VolumeConverter, CurrencyConverter
)


def display_menu():
    """Display main menu"""
    print("\n" + "="*50)
    print("          UNIT CONVERTER APPLICATION")
    print("="*50)
    print("1. Length Conversion")
    print("2. Weight Conversion")
    print("3. Temperature Conversion")
    print("4. Volume Conversion")
    print("5. Currency Conversion")
    print("6. Exit")
    print("="*50)


def length_conversion():
    """Handle length conversion"""
    print("\nAvailable units:", ", ".join(LengthConverter.get_units()))
    try:
        value = float(input("Enter value: "))
        from_unit = input("From unit: ")
        to_unit = input("To unit: ")
        result = LengthConverter.convert(value, from_unit, to_unit)
        print(f"\n✓ {value} {from_unit} = {result} {to_unit}\n")
    except ValueError as e:
        print(f"✗ Error: {e}\n")


def weight_conversion():
    """Handle weight conversion"""
    print("\nAvailable units:", ", ".join(WeightConverter.get_units()))
    try:
        value = float(input("Enter value: "))
        from_unit = input("From unit: ")
        to_unit = input("To unit: ")
        result = WeightConverter.convert(value, from_unit, to_unit)
        print(f"\n✓ {value} {from_unit} = {result} {to_unit}\n")
    except ValueError as e:
        print(f"✗ Error: {e}\n")


def temperature_conversion():
    """Handle temperature conversion"""
    print("\nAvailable units:", ", ".join(TemperatureConverter.get_units()))
    try:
        value = float(input("Enter value: "))
        from_unit = input("From unit: ")
        to_unit = input("To unit: ")
        result = TemperatureConverter.convert(value, from_unit, to_unit)
        print(f"\n✓ {value} {from_unit} = {result} {to_unit}\n")
    except ValueError as e:
        print(f"✗ Error: {e}\n")


def volume_conversion():
    """Handle volume conversion"""
    print("\nAvailable units:", ", ".join(VolumeConverter.get_units()))
    try:
        value = float(input("Enter value: "))
        from_unit = input("From unit: ")
        to_unit = input("To unit: ")
        result = VolumeConverter.convert(value, from_unit, to_unit)
        print(f"\n✓ {value} {from_unit} = {result} {to_unit}\n")
    except ValueError as e:
        print(f"✗ Error: {e}\n")


def currency_conversion():
    """Handle currency conversion"""
    print("\nCommon currencies:", ", ".join(CurrencyConverter.get_common_currencies()))
    try:
        amount = float(input("Enter amount: "))
        from_currency = input("From currency (e.g., USD): ").upper()
        to_currency = input("To currency (e.g., EUR): ").upper()
        result = CurrencyConverter.convert(amount, from_currency, to_currency)
        print(f"\n✓ {amount} {from_currency} = {result} {to_currency}\n")
    except Exception as e:
        print(f"✗ Error: {e}\n")


def main():
    """Main CLI entry point"""
    while True:
        display_menu()
        choice = input("Select an option (1-6): ").strip()
        
        if choice == "1":
            length_conversion()
        elif choice == "2":
            weight_conversion()
        elif choice == "3":
            temperature_conversion()
        elif choice == "4":
            volume_conversion()
        elif choice == "5":
            currency_conversion()
        elif choice == "6":
            print("\nThank you for using Unit Converter. Goodbye!\n")
            break
        else:
            print("✗ Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()
