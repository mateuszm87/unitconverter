import tkinter as tk
from tkinter import ttk

# Conversion functions
def convert_acceleration(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "G" and to_unit == "m/s²":
        return value * 9.80665
    elif from_unit == "m/s²" and to_unit == "G":
        return value / 9.80665
    else:
        raise ValueError("Invalid unit conversion")

def convert_displacement(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "mil" and to_unit == "µm":
        return value * 25.4
    elif from_unit == "µm" and to_unit == "mil":
        return value / 25.4
    else:
        raise ValueError("Invalid unit conversion")

def convert_pressure(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "psi" and to_unit == "kPa":
        return value * 6.89476
    elif from_unit == "kPa" and to_unit == "psi":
        return value / 6.89476
    else:
        raise ValueError("Invalid unit conversion")

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "°F" and to_unit == "°C":
        return (value - 32) * 5/9
    elif from_unit == "°C" and to_unit == "°F":
        return value * 9/5 + 32
    else:
        raise ValueError("Invalid unit conversion")

def convert_velocity(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "in/s" and to_unit == "mm/s":
        return value * 25.4
    elif from_unit == "mm/s" and to_unit == "in/s":
        return value / 25.4
    else:
        raise ValueError("Invalid unit conversion")

# Define the unit conversion based on the quantity
def unit_conversion(quantity, value, from_unit, to_unit):
    try:
        value = float(value)
        if quantity == 'Acceleration':
            return convert_acceleration(value, from_unit, to_unit)
        elif quantity == 'Displacement':
            return convert_displacement(value, from_unit, to_unit)
        elif quantity == 'Pressure':
            return convert_pressure(value, from_unit, to_unit)
        elif quantity == 'Temperature':
            return convert_temperature(value, from_unit, to_unit)
        elif quantity == 'Velocity':
            return convert_velocity(value, from_unit, to_unit)
        else:
            return "Conversion not implemented"
    except ValueError as e:
        return str(e)

# GUI functions
def on_convert():
    quantity = combo_quantity.get()
    from_unit = combo_from_unit.get()
    to_unit = combo_to_unit.get()
    value = entry_value.get()
    
    result = unit_conversion(quantity, value, from_unit, to_unit)
    label_result.config(text=f"Result: {result}")

root = tk.Tk()
root.title("Unit Converter")

# Dropdown for selecting the physical quantity
quantities = ['Acceleration', 'Displacement', 'Pressure', 'Temperature', 'Velocity']
combo_quantity = ttk.Combobox(root, values=quantities, state="readonly")
combo_quantity.grid(column=0, row=0, padx=10, pady=10)
combo_quantity.set("Select Quantity")

# Dropdown for selecting the from unit
units = {
    'Acceleration': ['G', 'm/s²'],
    'Displacement': ['mil', 'µm'],
    'Pressure': ['psi', 'kPa'],
    'Temperature': ['°F', '°C'],
    'Velocity': ['in/s', 'mm/s']
}
combo_from_unit = ttk.Combobox(root, values=[], state="readonly")
combo_from_unit.grid(column=1, row=0, padx=10, pady=10)

# Dropdown for selecting the to unit
combo_to_unit = ttk.Combobox(root, values=[], state="readonly")
combo_to_unit.grid(column=2, row=0, padx=10, pady=10)

# Entry for input value
entry_value = tk.Entry(root)
entry_value.grid(column=0, row=1, padx=10, pady=10)

# Button to perform conversion
button_convert = tk.Button(root, text="Convert", command=on_convert)
button_convert.grid(column=1, row=1, padx=10, pady=10)

# Label to display result
label_result = tk.Label(root, text="Result: ")
label_result.grid(column=2, row=1, padx=10, pady=10)

# Update the units when a quantity is selected
def on_quantity_change(event):
    selected_quantity = combo_quantity.get()
    if selected_quantity in units:
        combo_from_unit['values'] = units[selected_quantity]
        combo_to_unit['values'] = units[selected_quantity]
        combo_from_unit.set(units[selected_quantity][0])
        combo_to_unit.set(units[selected_quantity][1])

combo_quantity.bind('<<ComboboxSelected>>', on_quantity_change)

root.mainloop()