def main():
    expenses = read_input_file("Day1/DayOneInput")
    answer = find_pair(expenses,2020)
    print(answer)
    answer = find_triplet(expenses,2020)
    print(answer)

def find_pair(expenses,target):
    product = 0
    for x in range(0,len(expenses)):
        for y in range(x+1,len(expenses)):
            if expenses[x]+expenses[y] == target:
                product = expenses[x]*expenses[y]
                break
        if product>0:
            break
    return product

def find_triplet(expenses,target):
    result = 0
    for x in range(0,len(expenses)):
        result = find_pair(expenses[x+1:],target-expenses[x])
        if result > 0:
            result *=expenses[x]
            break
    return result


def read_input_file(filename):
    f = open(filename,'r')
    values = []
    while True:
        value = f.readline()
        if not value:
            break
        values.append(int(value.strip()))
    f.close()
    return values





if __name__ == '__main__':
    main()