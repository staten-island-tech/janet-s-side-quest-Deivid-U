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
print(data)  # Output the list

""" temperatures = ["Label", 32, 50, 77, 104]

celsius = list(map(lambda x: (x - 32)*5/9, temperatures[1:]))

print(celsius[1:]) """



    

