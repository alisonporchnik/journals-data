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



for row in reader:
    if search_string in row[search_field]:
        print(row)




# result = {}
# for row in reader:
#     key = row[0]
#     if key in result:
#         # implement your duplicate row handling here
#         pass
#     result[key] = row[1:]
# print result
