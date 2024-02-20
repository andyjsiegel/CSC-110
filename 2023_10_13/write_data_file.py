import json
def write_csv(data_dict, csv_file):
    keys = list(data_dict.keys())  # Get the keys of the dictionary
    values = list(data_dict.values())  # Get the values of the dictionary as a list of lists
    result_strings = []
    for index in range(len(keys)):
        result_strings.append(keys[index] + ',' + ','.join(str(value) for value in values[index]))

    print(result_strings)
    with open(csv_file, 'w') as f:
        csv_content = '\n'.join(result_strings) + "\n"
        print(json.dumps(csv_content))
        f.write(csv_content)
        f.close()
        print("Written!")

populations = {"Country": ["United States", "Brazil", "Mexico", "Canada"], "Population (in mil)": [331.00, 212.56, 128.93, 37.74]}
stipends = {"Peter": [1000], "Joan": [50500], "Mary": [2400]}

write_csv(populations, "population.csv")
write_csv(stipends, "stipends.csv")
