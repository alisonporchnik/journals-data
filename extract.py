import csv
reader = csv.reader(open('x.csv','rU'))

for row in reader:
    first_row = row
#    print(first_row)
    break

start_num = 0
first_row_string = ''

for field in first_row:
    first_row_string = first_row_string + str(start_num)
    first_row_string = first_row_string + ' = '
    first_row_string = first_row_string + field + ', '
    start_num += 1

print(first_row_string)    
    
    
    

search_field = input('Enter field to search: ')
search_string = raw_input('Search for what tag? ')
screen_or_file = input('Print to screen (0) or print to file (1)?')
if screen_or_file == 1:
    file_name = raw_input('Enter filename: ')

if screen_or_file == 0:
    for row in reader:
        if search_string in row[search_field]:
            print(row)

if screen_or_file == 1:
    with open(file_name, 'w') as fp:
        a = csv.writer(fp, delimiter=',')
        data = []
        for row in reader:
            if search_string in row[search_field]:
                data.append(row)
        a.writerows(data)    
    
