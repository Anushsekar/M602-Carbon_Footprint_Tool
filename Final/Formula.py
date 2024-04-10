def sum_energy_usage(monthly_electricity_bill, monthly_natural_gas_bill, monthly_fuel_bill):
    result = (monthly_electricity_bill * 12 * 0.0005) + (monthly_natural_gas_bill * 12 * 0.0053) + (monthly_fuel_bill * 12 * 2.32)
    return result

def sum_waste(total_waste_generated_per_month, recycling_percentage):
    result = (total_waste_generated_per_month * 12 * (0.57 - recycling_percentage / 100))
    return result

def sum_business_travel(total_kilometers_traveled_per_year, average_fuel_efficiency):
    result = total_kilometers_traveled_per_year / (average_fuel_efficiency / 100) * 2.31
    return result
