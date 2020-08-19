import re
NumberOfCoordinates = int(input('Enter the number of coordinates\n'))
for coordinate in range(NumberOfCoordinates):
    sequence = input('enter a coordinate\n')
    pattern = re.match(r'R(\d+)C(\d+)', sequence)
    if pattern:  # convert to Excel Numeration System
        RowNumber = pattern.group(1)
        ColumnNumber = int(pattern.group(2))
        Column = ''
        while ColumnNumber:
            # (ColumnNumber-1) % 26 generates numbers from 0 to 25
            # so minimum ord('A') = 65 ==> A
            # maximum ord('A') + 25 = 90 ==> Z
            Column = chr(ord('A') + (ColumnNumber-1) % 26) + Column
            ColumnNumber = (ColumnNumber-1) // 26
        print(Column + RowNumber)
    else: # convert from Excel Numeration system to the other one
        # split string into two parts [column , row]
        counter = 0
        for char in sequence:
            if not char.isdigit():
                counter += 1
        column = sequence[:counter]
        row = int(sequence[counter:])
        # convert column
        column_number = 0
        for char in column:
            order = ord(char) - ord('A') + 1
            column_number = column_number*26 + order
        print('R'+str(row)+'C'+str(column_number))
