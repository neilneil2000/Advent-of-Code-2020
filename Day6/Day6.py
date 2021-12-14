def main():
    groups = read_input_file("Day6\DaySixInput")
    group_values = calculate_all_yes(groups)
    count = 0
    for group in group_values:
        count += len(group)
    print(f'Answer = {count}')
    print('END')

def calculate_all_yes(groups):
    group_values = []
    for group in groups:
        values = set(group[0])
        if len(group) > 1:
            for i in range(1,len(group)):
                values.intersection_update(group[i])
        group_values.append(values)
    return group_values



def read_input_file(filename) -> list:
    """Relies on blank line at end of file"""
    groups = []
    group = []
    with open(filename,'r') as f:
        for line in f:
            line = line.strip()
            if line == '':
                groups.append(group)
                group = [] 
            else:
                group.append(set(line))
    return groups

if __name__ == '__main__':
    main()