def main():
    groups = read_input_file("Day6\DaySixInput")
    count = 0
    for group in groups:
        count += len(group)
    print(f'Answer = {count}')
    print('END')

def read_input_file(filename) -> list:
    groups = []
    group = []
    with open(filename,'r') as f:
        for line in f:
            line = line.strip()
            if line == '':
                groups.append(set(group))
                group = [] 
            else:
                group.extend(list(line))
    return groups

if __name__ == '__main__':
    main()