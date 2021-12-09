def main():
    list = read_input_file("Day2/DayTwoInput")
    count = check_list_validity(list)
    print(f'{str(count)} Valid Passwords')
    count = check_list_validity_part2(list)
    print(f'{str(count)} Valid Passwords')
    

def check_list_validity_part2(list):
    count = 0
    for item in list:
        if check_item_validity_part2(item):
            count += 1
    return count


def check_item_validity_part2(row):
    password = list(row['password'])
    valid = False
    if password[row['min']-1] == row['letter']:
        valid = True
    if password[row['max']-1] == row['letter']:
        valid = not valid
    return valid


def check_list_validity(list):    
    count = 0
    for item in list:
        if check_item_validity(item):
            count += 1
    return count


def check_item_validity(row):
    password = list(row['password'])
    count = 0
    for letter in password:
        if letter == row['letter']:
            count += 1
    if count in range(row['min'],row['max']+1):
        return True
    return False

def read_input_file(filename):
    input = []
    f = open(filename,'r')
    while True:
        line = f.readline()
        if not line:
            break
        row = {}
        line = line.strip().split('-')
        row.update({'min':int(line.pop(0))})
        line = line[0].split()
        row.update({'max':int(line.pop(0))})
        line[0] = line[0].split(':')
        row.update({'letter':line[0].pop(0)})
        row.update({'password':line[1]})
        input.append(row)
    print("Read " + str(len(input)) + " lines")
    return input

if __name__ == "__main__":
    main()