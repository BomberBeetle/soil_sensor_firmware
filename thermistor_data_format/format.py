import csv
rows = []
with open('thermistor_data_unformatted.csv') as file:
    data = csv.reader(file, dialect="excel", delimiter=';')
    for row in data:
        rows.append(row)

for row in rows:
    for i in range(3):
        res = list(row[i+1].replace(".", ""))
        res.insert(-4 if (len(res) > 4) else -3, ",")
        row[i+1] = ''.join(res)
    print(' | '.join(row))
    
with open('thermistor_data_formatted.csv', 'w') as outfile:
    writer = csv.writer(outfile, delimiter=';')
    writer.writerows(rows)

