def validBirthYear(byr):
    val = int(byr)
    return True if (len(byr) == 4 and val >= 1920 and val <= 2002) else False


def validIssueYear(iyr):
    val = int(iyr)
    return True if (len(iyr) == 4 and val >= 2010 and val <= 2020) else False


def validExpirationYear(eyr):
    val = int(eyr)
    return True if (len(eyr) == 4 and val >= 2020 and val <= 2030) else False


def validHeight(hgt):
    if hgt[:-2] == "":
        return False
    val = int(hgt[:-2])
    if hgt[-2:] == "cm":
        return True if (val >= 150 and val <= 193) else False
    else:
        return True if (val >= 59 and val <= 76) else False


def validHairColor(hcl):
    if hcl[0] == '#':
        for char in hcl[1:]:
            val = ord(char)
            if val < 48 or val > 57 and val < 97 or val > 102:
                return False
        return True
    return False


def validEyeColor(ecl):
    colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if ecl in colors:
        return True
    return False


def validPassportID(pid):
    return True if len(pid) == 9 and pid.isdigit() else False


def isPassportValid(passport):
    if len(passport) == 8 or len(passport) == 7 and "cid" not in passport:
        if (validBirthYear(passport["byr"]) and validIssueYear(passport["iyr"]) and
                validExpirationYear(passport["eyr"]) and validHeight(passport["hgt"]) and
                validHairColor(passport["hcl"]) and validEyeColor(passport["ecl"]) and
                validPassportID(passport["pid"])):

            return True
    return False


def main():
    f = open("input.txt", "r")

    data = f.read().split("\n")

    numValidPassports = 0
    passports = []

    currentPassport = {}

    for index, elem in enumerate(data):
        if elem == "":
            passports.append(currentPassport)
            currentPassport = {}
        else:
            elem = elem.split(" ")
            for field in elem:
                currentPassport[field[:3]] = field[4:]

    print(len(passports))
    for passport in passports:
        numValidPassports += isPassportValid(passport)

    print(numValidPassports)


main()
