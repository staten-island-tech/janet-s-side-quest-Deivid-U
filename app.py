## This function opens the CSV for You!
def csv_to_list(file_path):
    data_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            row = [int(value) if value.isdigit() else value for value in row]
            data_list.append(row)

    return data_list


file_path = "SalesData.csv"  
data = csv_to_list(file_path)
""" print(data)  # Output the list """

""" temperatures = ["Label", 32, 50, 77, 104]

celsius = list(map(lambda x: (x - 32)*5/9, temperatures[1:]))

print(celsius[1:]) """

def row_average(data):
    row_averages = {}

    for row in data[1:]:
        location = row[0]
        sales = list(map(int, row[1:]))
        row_averages[location] = round(sum(sales) / len(sales), 2)
    return row_averages

averages = row_average(data)
""" print(averages) """

def sort_profit(data):
    ordered_list = {}
    ordered_list = sorted(averages.items(), key=lambda x: x[1], reverse=True)
    return ordered_list

sorted_profits = dict(sort_profit(data))

""" print(sorted_profits) """

def universal_average(data):
    totals = {}
    days = {}
    for row in data[1:]:
        location = row[0]
        totals[location] = sum(row[1:])
        days[location] = len(row[1:])
    universal_average = sum(totals.values()) / sum(days.values())
    return universal_average

all_stores_average = universal_average(data)

""" print(universal_average(data)) """

def danger(averages, uni_average):
    for location in averages:
        if location.value < 0.8 



