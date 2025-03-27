# class UnitConverter:
#     def __init__(self):
#         # Conversion rates relative to base units (meters, kilograms, celsius)
#         self.length_units = {
#             'km': 1000,
#             'm': 1,
#             'cm': 0.01,
#             'mm': 0.001,
#             'mi': 1609.34,
#             'yd': 0.9144,
#             'ft': 0.3048,
#             'in': 0.0254
#         }
        
#         self.weight_units = {
#             'kg': 1,
#             'g': 0.001,
#             'mg': 0.000001,
#             'lb': 0.453592,
#             'oz': 0.0283495
#         }

#     def convert_length(self, value, from_unit, to_unit):
#         if from_unit not in self.length_units or to_unit not in self.length_units:
#             return "Invalid length units"
#         # Convert to base unit (meters) then to target unit
#         meters = value * self.length_units[from_unit]
#         result = meters / self.length_units[to_unit]
#         return round(result, 6)

#     def convert_weight(self, value, from_unit, to_unit):
#         if from_unit not in self.weight_units or to_unit not in self.weight_units:
#             return "Invalid weight units"
#         # Convert to base unit (kilograms) then to target unit
#         kilos = value * self.weight_units[from_unit]
#         result = kilos / self.weight_units[to_unit]
#         return round(result, 6)

#     def convert_temperature(self, value, from_unit, to_unit):
#         # Temperature needs special handling due to different scales
#         if from_unit == 'C' and to_unit == 'F':
#             return (value * 9/5) + 32
#         elif from_unit == 'F' and to_unit == 'C':
#             return (value - 32) * 5/9
#         elif from_unit == 'C' and to_unit == 'K':
#             return value + 273.15
#         elif from_unit == 'K' and to_unit == 'C':
#             return value - 273.15
#         elif from_unit == 'F' and to_unit == 'K':
#             return (value - 32) * 5/9 + 273.15
#         elif from_unit == 'K' and to_unit == 'F':
#             return (value - 273.15) * 9/5 + 32
#         elif from_unit == to_unit:
#             return value
#         else:
#             return "Invalid temperature units"

# def main():
#     converter = UnitConverter()
    
#     # Example usage
#     print("Unit Converter")
#     print("-" * 20)
    
#     # Length conversion example
#     length = 5.5
#     print(f"{length} meters = {converter.convert_length(length, 'm', 'ft')} feet")
    
#     # Weight conversion example
#     weight = 100
#     print(f"{weight} kg = {converter.convert_weight(weight, 'kg', 'lb')} pounds")
    
#     # Temperature conversion example
#     temp = 32
#     print(f"{temp}°F = {converter.convert_temperature(temp, 'F', 'C')}°C")

# if __name__ == "__main__":
#     main()                                                            

import streamlit as st

# 🎨 Apply Custom Styling
st.set_page_config(page_title="Smart Unit Converter", layout="wide")

# 🎯 Unit Converter Class
class UnitConverter:
    def __init__(self):
        self.length_units = {
            'km': 1000, 'm': 1, 'cm': 0.01, 'mm': 0.001,
            'mi': 1609.34, 'yd': 0.9144, 'ft': 0.3048, 'in': 0.0254
        }
        
        self.weight_units = {
            'kg': 1, 'g': 0.001, 'mg': 0.000001,
            'lb': 0.453592, 'oz': 0.0283495
        }

    def convert_length(self, value, from_unit, to_unit):
        if from_unit not in self.length_units or to_unit not in self.length_units:
            return "Invalid length units"
        meters = value * self.length_units[from_unit]
        result = meters / self.length_units[to_unit]
        return round(result, 6)

    def convert_weight(self, value, from_unit, to_unit):
        if from_unit not in self.weight_units or to_unit not in self.weight_units:
            return "Invalid weight units"
        kilos = value * self.weight_units[from_unit]
        result = kilos / self.weight_units[to_unit]
        return round(result, 6)

    def convert_temperature(self, value, from_unit, to_unit):
        if from_unit == 'C' and to_unit == 'F':
            return round((value * 9/5) + 32, 2)
        elif from_unit == 'F' and to_unit == 'C':
            return round((value - 32) * 5/9, 2)
        elif from_unit == 'C' and to_unit == 'K':
            return round(value + 273.15, 2)
        elif from_unit == 'K' and to_unit == 'C':
            return round(value - 273.15, 2)
        elif from_unit == 'F' and to_unit == 'K':
            return round((value - 32) * 5/9 + 273.15, 2)
        elif from_unit == 'K' and to_unit == 'F':
            return round((value - 273.15) * 9/5 + 32, 2)
        elif from_unit == to_unit:
            return value
        else:
            return "Invalid temperature units"

# 🎯 Initialize Converter
converter = UnitConverter()

# 🖼 Sidebar Layout
st.sidebar.title("Smart Unit Converter")
conversion_type = st.sidebar.radio("Select Conversion Type:", ["Length", "Weight", "Temperature"])
st.sidebar.write("🔄 **Live Conversion Mode** (No need to press a button!)")

# 🔢 User Input Section
st.markdown("<h2 style='text-align: center;'>🔄 Convert Units Instantly</h2>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 1, 2])
value = col1.number_input("🔢 Enter Value:", min_value=0.0, format="%.2f")

# 📏 Length Conversion
if conversion_type == "Length":
    from_unit = col2.selectbox("🔽 From:", list(converter.length_units.keys()))
    to_unit = col3.selectbox("🔼 To:", list(converter.length_units.keys()))
    result = converter.convert_length(value, from_unit, to_unit)

# ⚖️ Weight Conversion
elif conversion_type == "Weight":
    from_unit = col2.selectbox("🔽 From:", list(converter.weight_units.keys()))
    to_unit = col3.selectbox("🔼 To:", list(converter.weight_units.keys()))
    result = converter.convert_weight(value, from_unit, to_unit)

# 🌡 Temperature Conversion
elif conversion_type == "Temperature":
    from_unit = col2.selectbox("🔽 From:", ["C", "F", "K"])
    to_unit = col3.selectbox("🔼 To:", ["C", "F", "K"])
    result = converter.convert_temperature(value, from_unit, to_unit)

# ✅ Show Result
st.success(f"💡 **{value} {from_unit} = {result} {to_unit}**")

# 🔥 Dark Mode Toggle
dark_mode = st.sidebar.toggle("🌙 Dark Mode")
if dark_mode:
    st.markdown("""
        <style>
        body {
            background-color: #2e2e2e;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)
