import matplotlib.pyplot as graph
import os
from fpdf import FPDF
import subprocess
import Formula as source
import suggestions as s

def create_pdf(entries):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Carbon Footprint Analysis Report", ln=True, align="C")
    pdf.ln(5)
    
    for i, entry in enumerate(entries):
        pdf.cell(200, 10, txt=f"Entry {i+1}:", ln=True, align="L")
        pdf.cell(200, 10, txt=f"Total Carbon Footprint: {sum(entry)} metric tons CO2 equivalent", ln=True, align="L")
        pdf.multi_cell(0, 10, txt=f"Energy Usage Suggestion:\n{s.energy_suggestion(entry[0])}")
        pdf.multi_cell(0, 10, txt=f"Waste Generation Suggestion:\n{s.waste_suggestion(entry[1])}")
        pdf.multi_cell(0, 10, txt=f"Business Travel Suggestion:\n{s.travel_suggestion(entry[2])}")
        pdf.ln(0)
        
        # Embed charts as images in the PDF
        pdf.image(f"charts/entry_{i+1}_All_input_data_results.png", x=10, y=pdf.get_y() + 10, w=150)
        pdf.ln(180)
    
    pdf.add_page()
    pdf.image("charts/total_carbon_footprint.png", x=10, y=pdf.get_y() + 10, w=180)
    pdf.ln(110)
    
    # Embed bar chart for total carbon footprint by entry
    pdf.image("charts/total_carbon_footprint_by_entry.png", x=10, y=pdf.get_y() + 10, w=180)
    pdf.ln(110)
    
    pdf.output("carbon_footprint_report.pdf")

def save_chart(chart, filename):
    directory = "charts"
    if not os.path.exists(directory):
        os.makedirs(directory)
    graph.savefig(os.path.join(directory, filename))

def main():
    num_entries = int(input("Enter the number of entries: "))
    total_energy_usage = 0
    total_waste_generation = 0
    total_business_travel = 0
    entries = []

    for i in range(num_entries):
        print(f"\nEntry {i+1}:")
        monthly_electricity_bill = float(input("Enter monthly electricity bill amount: "))
        monthly_natural_gas_bill = float(input("Enter monthly natural gas bill amount: "))
        monthly_fuel_bill = float(input("Enter monthly fuel bill amount: "))
        total_waste_generated_per_month = float(input("Enter total waste generated per month (kg): "))
        recycling_percentage = float(input("Enter recycling percentage (%): "))
        total_kilometers_traveled_per_year = float(input("Enter total kilometers traveled per year: "))
        average_fuel_efficiency = float(input("Enter average fuel efficiency (km/L): "))

        energy_usage = source.sum_energy_usage(monthly_electricity_bill, monthly_natural_gas_bill, monthly_fuel_bill)
        waste_generation = source.sum_waste(total_waste_generated_per_month, recycling_percentage)
        business_travel = source.sum_business_travel(total_kilometers_traveled_per_year, average_fuel_efficiency)

        total_energy_usage += energy_usage
        total_waste_generation += waste_generation
        total_business_travel += business_travel
        entry = (energy_usage, waste_generation, business_travel)
        entries.append(entry)

        # Pie chart for energy usage
        labels_energy = ['Electricity', 'Natural Gas', 'Fuel']
        values_energy = [monthly_electricity_bill, monthly_natural_gas_bill, monthly_fuel_bill]
        graph.figure(figsize=(8, 8))
        graph.subplot(2, 2, 2)
        graph.pie(values_energy, labels=labels_energy, autopct='%1.1f%%')
        graph.title('Energy Usage')
        save_chart(graph, f"entry_{i+1}_energy_usage.png")

        # Pie chart for waste generation and the previous
        labels_waste = ['Waste', 'Recycled']
        values_waste = [total_waste_generated_per_month, total_waste_generated_per_month * 12 * (recycling_percentage / 100)]
        graph.subplot(2, 2, 4)
        graph.pie(values_waste, labels=labels_waste, autopct='%1.1f%%')
        graph.title('Waste Generation')
        save_chart(graph, f"entry_{i+1}_waste_generation.png")

        # Pie chart for business travel and others
        labels_travel = ['Business Travel', 'Other']
        values_travel = [total_kilometers_traveled_per_year / (average_fuel_efficiency / 100) * 2.31, total_kilometers_traveled_per_year]
        graph.subplot(2, 2, 3)
        graph.pie(values_travel, labels=labels_travel, autopct='%1.1f%%')
        graph.title('Business Travel')
        save_chart(graph, f"entry_{i+1}_All_input_data_results.png")

        graph.tight_layout()
        graph.close('all')

        suggestion_energy = s.energy_suggestion(energy_usage)
        suggestion_waste = s.waste_suggestion(waste_generation)
        suggestion_travel = s.travel_suggestion(business_travel)

        print("\nTotal Carbon Footprint for Entry", i+1, ":", energy_usage + waste_generation + business_travel, "metric tons CO2 equivalent")
        print("Energy Usage Suggestion:", suggestion_energy)
        print("Waste Generation Suggestion:", suggestion_waste)
        print("Business Travel Suggestion:", suggestion_travel)

    # Bar chart for total values by category
    categories = ['Energy Usage', 'Waste Generation', 'Business Travel']
    total_values = [total_energy_usage, total_waste_generation, total_business_travel]

    graph.figure(figsize=(10, 6))
    graph.bar(categories, total_values)
    graph.xlabel('Categories')
    graph.ylabel('Total Carbon Footprint (metric tons CO2 equivalent)')
    graph.title('Total Carbon Footprint by Category')
    save_chart(graph, "total_carbon_footprint.png")

    # Bar chart for total values by entry
    entry_numbers = [i+1 for i in range(num_entries)]
    entry_energy_usage = [entry[0] for entry in entries]
    entry_waste_generation = [entry[1] for entry in entries]
    entry_business_travel = [entry[2] for entry in entries]

    graph.figure(figsize=(10, 6))
    graph.bar(entry_numbers, entry_energy_usage, label='Energy Usage')
    graph.bar(entry_numbers, entry_waste_generation, bottom=entry_energy_usage, label='Waste Generation')
    graph.bar(entry_numbers, entry_business_travel, bottom=[sum(x) for x in zip(entry_energy_usage, entry_waste_generation)], label='Business Travel')
    graph.xlabel('Entry')
    graph.ylabel('Total Carbon Footprint (metric tons CO2 equivalent)')
    graph.title('Total Carbon Footprint by Entry')
    graph.legend()
    save_chart(graph, "total_carbon_footprint_by_entry.png")

    print("\nAnalysis completed for all entries.")
    create_pdf(entries)
    open_pdf("carbon_footprint_report.pdf")

def open_pdf(file_path):
    subprocess.run(["open", file_path])

if __name__ == "__main__":
    main()

