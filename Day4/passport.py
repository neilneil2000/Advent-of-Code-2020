class Passport:

    valid_hex = {'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f'}
    valid_eye_colour = {'amb','blu','brn','gry','grn','hzl','oth'}
    valid_numeral = {'0','1','2','3','4','5','6','7','8','9'}

    def __init__(self):
        self.data = {'byr': None,
                     'iyr': None,
                     'eyr': None,
                     'hgt': None,
                     'hcl': None,
                     'ecl': None,
                     'pid': None,
                     'cid': None}
        self.valid = False
    
    def parse_info(self, info):
        for item in info:
            item = item.split(':')
            self.data[item[0]] = item[1]

    def check_year(self,year,low,high):
        if year is None:
            return False
        year = int(year)
        if year < low:
            return False
        if year > high:
            return False
        return True

    def check_expiration_year(self):
        year = self.data['eyr']
        return self.check_year(year,2020,2030)

    def check_issue_year(self):
        year = self.data['iyr']
        return self.check_year(year,2010,2020)

    def check_birth_year(self):
        year = self.data['byr']
        return self.check_year(year,1920,2002)

    def check_height(self):
        try:
            height = self.data['hgt']
            value = int(height[:-2])
            unit = height[-2:]
            if unit == 'cm':
                if value > 193:
                    return False
                elif value < 150:
                    return False
            elif unit == 'in':
                if value > 76:
                    return False
                elif value < 59:
                    return False
            else:
                return False
            return True
        except:
            return False

    def check_hair_colour(self):
        hair_colour = self.data['hcl']
        if hair_colour is None:
            return False
        if hair_colour[:1] != '#':
            return False
        if len(hair_colour) != 7:
            return False
        for character in hair_colour[1:]:
            if character not in Passport.valid_hex:
                return False
        return True

    def check_eye_colour(self):
        eye_colour = self.data['ecl']
        if eye_colour is None:
            return False
        if eye_colour in Passport.valid_eye_colour:
            return True
        return False

    def check_passport_id(self):
        passport_id = self.data['pid']
        if passport_id is None:
            return False
        if len(passport_id) != 9:
            return False
        for character in passport_id:
            if character not in Passport.valid_numeral:
                return False
        return True



    def check_validity_strict(self):
        valid = True
        valid &= self.check_birth_year()
        valid &= self.check_issue_year()
        valid &= self.check_expiration_year()
        valid &= self.check_height()
        valid &= self.check_hair_colour()
        valid &= self.check_eye_colour()
        valid &= self.check_passport_id()
        self.valid = valid
        return valid
    
    def check_validity(self):
        if self.data['cid'] is None:
            checker = 7
        else:
            checker = 8
        data_counter = 0
        for item in self.data.values():
            if item is not None:
                data_counter += 1
        if data_counter == checker:
            self.valid = True
        else:
            self.valid = False
        return self.valid
