def energy_suggestion(energy_usage):
    if energy_usage <= 5:
        return "Your energy usage is very low! Keep up the good work by using energy-efficient appliances and turning off lights when not in use."
    elif 5 < energy_usage <= 10:
        return "Your energy usage is moderate. Consider further reducing energy consumption by using renewable energy sources and investing in energy-efficient technologies."
    else:
        return "Your energy usage is high. Take steps to reduce energy consumption by improving insulation, upgrading to energy-efficient appliances, and using energy-saving practices."

def waste_suggestion(waste_generation):
    if waste_generation <= 2:
        return "Your waste generation is very low! Continue to reduce waste by practicing recycling, composting, and reducing single-use items."
    elif 2 < waste_generation <= 5:
        return "Your waste generation is moderate. Aim to further reduce waste by avoiding excessive packaging, buying in bulk, and repairing items instead of replacing them."
    else:
        return "Your waste generation is high. Take steps to minimize waste by avoiding disposable products, recycling more, and supporting sustainable packaging."

def travel_suggestion(business_travel):
    if business_travel <= 2:
        return "Your business travel emissions are very low! Consider alternative transportation options such as walking, biking, or using public transportation whenever possible."
    elif 2 < business_travel <= 5:
        return "Your business travel emissions are moderate. Try to minimize unnecessary trips, combine errands, and carpool to reduce your carbon footprint."
    else:
        return "Your business travel emissions are high. Explore alternatives like telecommuting, video conferencing, or using more fuel-efficient vehicles to lower emissions."
