def main():
    tickets = read_input_file("Day5\DayFiveInput")
    #print(tickets)
    seat_ids = calculate_seat_ids(tickets)
    seat_ids.sort()
    print(f'Highest Seat ID is: {max(seat_ids)}')
    #print(seat_ids)
    missing = find_missing_seat_id(seat_ids)
    print(f'My seat is seat: {missing}')
    

def find_missing_seat_id(seat_ids):
    for i in range(1,len(seat_ids)):
        if seat_ids[i]-seat_ids[i-1] > 1:
            print(f'{seat_ids[i]} : {seat_ids[i-1]}')
            return seat_ids[i]-1

def calculate_seat_ids(tickets):
    seat_ids = []
    for ticket in tickets:
        valid_row = (0,127)
        valid_column = (0,7)
        for letter in ticket:
            if letter == 'F' or letter == 'B':
                half = int((valid_row[1] - valid_row[0] + 1) / 2)
                if letter == 'F':
                    valid_row = (valid_row[0], valid_row[1] - half)
                else:
                    valid_row = (valid_row[0] + half, valid_row[1])
            else:
                half = int((valid_column[1] - valid_column[0] + 1) / 2)
                if letter == 'L':
                    valid_column = (valid_column[0], valid_column[1] - half)
                else:
                    valid_column = (valid_column[0] + half, valid_column[1])
        seat_ids.append(valid_row[0] * 8 + valid_column[0])
    return seat_ids


def read_input_file(filename):
    tickets =[]
    with open(filename,'r') as f:
        for line in f:
            tickets.append(line.strip())
    return tickets


if __name__ == '__main__':
    main()