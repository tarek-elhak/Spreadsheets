import re
NumberOfCoordinates = int(input('Enter the number of coordinates\n'))
for coordinate in range(NumberOfCoordinates):
    sequence = input('enter a coordinate\n')
    pattern = re.match(r'R(\d+)C(\d+)',sequence)
    if pattern:  # convert to Excel Numeration System
        RowNumber = pattern.group(1)
        ColumnNumber = int(pattern.group(2))
        Column = ''
        while ColumnNumber:
            Column = chr(ord('A') + (ColumnNumber-1) % 26) + Column
            ColumnNumber = (ColumnNumber-1) // 26
        print(Column + RowNumber)
