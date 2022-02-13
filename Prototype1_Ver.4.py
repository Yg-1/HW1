def readRecords(filename):
    result = []
    try:
        f = open(filename, 'r')
        f.readline()
        for line in f:
            line = line.rstrip('\n')
            line = line.replace('\t', ',')
            fields = line.split(',')
            result.append(fields)
        f.close()
        return result
    except:
        print('File not found')


def parseLine(line):
    return line[1], line[2], line[3], line[4], line[5], line[6]


def calPercent(years):
    b = []
    for line in alist:
        id, first, last, gradyear, year, house = parseLine(line)
        if gradyear == years:
            b.append(line)
        numb = len(b)
        perc = len(b) / len(alist)
    return numb, perc

def displayAll(n):
    print(*readRecords('potter.txt'), sep='\n')

def displayByLastName(n):
    n2 = input("\nPlease enter the last name\nor enter 'return' to return to the previous menu:")
    n2 = n2.lower()
    while n2 != 'return':
        b = []
        for line in alist:
            id, first, last, gradyear, year, house = parseLine(line)
            last = last.lower()
            if last.startswith(n2):
                b.append(line)
        if len(b) != 0:
            print(*b, sep='\n')
        else:
            print('\nNo matches')
        n2 = input("\nPlease enter the last name\nor enter 'return' to return to the previous menu:")
        n2 = n2.lower()

def displayByGradYear(n3):
    while n3 != 'return':
        b = []
        if len(str(n3)) == 4 and n3.isdigit():
            for line in alist:
                id, first, last, gradyear, year, house = parseLine(line)
                if gradyear == n3:
                    b.append(line)
            num, perc = calPercent(n3)
            if len(b) != 0:
                print(*b, sep='\n')
                print('\nNumbers of students:', num, '\nTotal Graduate Percentage:', str(round(perc * 100)) + '%')
            else:
                print('\nNo matches')
        else:
            print('\nPlease enter a valid year(4 digits)')
        n3 = input("\nPlease enter the year(4 digits)\nor enter 'return' to return to the previous menu:")
        n3 = n3.lower()

def menu():
    n = input("\n\nPlease choose a function\n\n'All' for all students record\n'Name' to search the students\n'Year' to search the graduate year\n'Stop'to end the program:")
    n = n.lower()
    b = []
    while n != 'stop':
        if n == 'all':
            displayAll(n)
        elif n == 'name':
            displayByLastName(n)
        elif n== 'year':
            n3 = input("\nPlease enter the year(4 digits)\nor enter 'return' to return to the previous menu:")
            n3 = n3.lower()
            displayByGradYear(n3)
        else:
            print('\nPlease choose a valid function')
        n = input("\n\nPlease choose a function\n\n'All' for all students record\n'Name' to search the students\n'Year' to search the graduate year\n'Stop'to end the program:")
        n = n.lower()
    return print('\nProgram ends\nThanks for using!')

alist = readRecords('potter.txt')
menu()
