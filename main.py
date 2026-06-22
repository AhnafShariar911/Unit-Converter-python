"""Unit Converter Application with GUI"""

import tkinter as tk
from tkinter import ttk, messagebox
from converters import (
    LengthConverter, WeightConverter, TemperatureConverter,
    VolumeConverter, CurrencyConverter
)


class UnitConverterApp:
    """Main GUI application for unit converter"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # Set style
        style = ttk.Style()
        style.theme_use('clam')
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the user interface"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title = ttk.Label(main_frame, text="Unit Converter", 
                         font=("Arial", 16, "bold"))
        title.grid(row=0, column=0, columnspan=3, pady=10)
        
        # Converter type selection
        ttk.Label(main_frame, text="Select Converter Type:").grid(row=1, column=0, sticky=tk.W, pady=5)
        
        self.converter_var = tk.StringVar(value="Length")
        converter_types = ["Length", "Weight", "Temperature", "Volume", "Currency"]
        self.converter_combo = ttk.Combobox(main_frame, textvariable=self.converter_var,
                                           values=converter_types, state="readonly", width=30)
        self.converter_combo.grid(row=1, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        self.converter_combo.bind("<<ComboboxSelected>>", self.on_converter_changed)
        
        # Input value
        ttk.Label(main_frame, text="Value to Convert:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.value_entry = ttk.Entry(main_frame, width=30)
        self.value_entry.grid(row=2, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # From unit
        ttk.Label(main_frame, text="From Unit:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.from_unit_var = tk.StringVar()
        self.from_unit_combo = ttk.Combobox(main_frame, textvariable=self.from_unit_var,
                                           state="readonly", width=30)
        self.from_unit_combo.grid(row=3, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # To unit
        ttk.Label(main_frame, text="To Unit:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.to_unit_var = tk.StringVar()
        self.to_unit_combo = ttk.Combobox(main_frame, textvariable=self.to_unit_var,
                                         state="readonly", width=30)
        self.to_unit_combo.grid(row=4, column=1, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Convert button
        convert_btn = ttk.Button(main_frame, text="Convert", command=self.perform_conversion)
        convert_btn.grid(row=5, column=1, sticky=(tk.W, tk.E), pady=15)
        
        # Reset button
        reset_btn = ttk.Button(main_frame, text="Reset", command=self.reset_form)
        reset_btn.grid(row=5, column=2, sticky=(tk.W, tk.E), padx=5)
        
        # Result display
        ttk.Label(main_frame, text="Result:", font=("Arial", 10, "bold")).grid(row=6, column=0, sticky=tk.W, pady=5)
        self.result_frame = ttk.Frame(main_frame, relief=tk.SUNKEN, borderwidth=2)
        self.result_frame.grid(row=7, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        self.result_text = tk.Text(self.result_frame, height=6, width=50, state=tk.DISABLED)
        self.result_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Initialize units
        self.update_units()
        
        # Configure grid weights
        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(2, weight=1)
    
    def on_converter_changed(self, event=None):
        """Handle converter type change"""
        self.update_units()
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.config(state=tk.DISABLED)
    
    def update_units(self):
        """Update unit dropdowns based on converter type"""
        converter_type = self.converter_var.get()
        
        if converter_type == "Length":
            units = LengthConverter.get_units()
        elif converter_type == "Weight":
            units = WeightConverter.get_units()
        elif converter_type == "Temperature":
            units = TemperatureConverter.get_units()
        elif converter_type == "Volume":
            units = VolumeConverter.get_units()
        elif converter_type == "Currency":
            units = CurrencyConverter.get_common_currencies()
        
        self.from_unit_combo['values'] = units
        self.to_unit_combo['values'] = units
        
        if units:
            self.from_unit_combo.set(units[0])
            self.to_unit_combo.set(units[1] if len(units) > 1 else units[0])
    
    def perform_conversion(self):
        """Perform the conversion"""
        try:
            # Get input
            value_str = self.value_entry.get().strip()
            if not value_str:
                messagebox.showerror("Error", "Please enter a value to convert")
                return
            
            try:
                value = float(value_str)
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number")
                return
            
            from_unit = self.from_unit_var.get()
            to_unit = self.to_unit_var.get()
            
            if not from_unit or not to_unit:
                messagebox.showerror("Error", "Please select both units")
                return
            
            converter_type = self.converter_var.get()
            
            # Perform conversion
            if converter_type == "Length":
                result = LengthConverter.convert(value, from_unit, to_unit)
            elif converter_type == "Weight":
                result = WeightConverter.convert(value, from_unit, to_unit)
            elif converter_type == "Temperature":
                result = TemperatureConverter.convert(value, from_unit, to_unit)
            elif converter_type == "Volume":
                result = VolumeConverter.convert(value, from_unit, to_unit)
            elif converter_type == "Currency":
                result = CurrencyConverter.convert(value, from_unit, to_unit)
            
            # Display result
            result_message = f"{value} {from_unit} = {result} {to_unit}"
            
            self.result_text.config(state=tk.NORMAL)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result_message)
            self.result_text.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed: {str(e)}")
    
    def reset_form(self):
        """Reset the form"""
        self.value_entry.delete(0, tk.END)
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete(1.0, tk.END)
        self.result_text.config(state=tk.DISABLED)


def main():
    """Main entry point"""
    root = tk.Tk()
    app = UnitConverterApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
