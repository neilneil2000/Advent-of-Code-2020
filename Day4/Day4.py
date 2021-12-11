from passport import Passport

def main():
    passports = read_input_file("Day4/DayFourInput")
    valid_counter = 0
    for passport in passports:
        if passport.check_validity():
            valid_counter += 1
    print(f'There are {valid_counter} valid passports')
    valid_counter = 0
    for passport in passports:
        if passport.check_validity_strict():
            valid_counter += 1
    print(f'There are {valid_counter} strictly valid passports')
    print('END')


def read_input_file(filename):
    passports = []
    passports.append(Passport())
    with open(filename,'r') as f:
        for line in f:
            line = line.strip()
            if len(line) == 0:
                passports.append(Passport())
            else:
                passports[-1].parse_info(line.split())
    return passports

if __name__ == '__main__':
    main()
