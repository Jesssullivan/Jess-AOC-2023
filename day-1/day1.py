from re import finditer

fp = 'day1.txt'

char_numlist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
                'eight', 'nine']

char_map = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}


def verify_numeric(num):
    try:
        return char_map[num]
    except KeyError:
        return num


def findnum(ln, array):

    match_dict = {}

    for n in array:
        for match in finditer(n, ln):
            match_dict[match.start()] = match.group()

    min_match = match_dict[min(match_dict.keys())]
    max_match = match_dict[max(match_dict.keys())]

    return eval(str(verify_numeric(min_match)) + str(verify_numeric(max_match)))


with open(fp) as f:
    line = f.readline().strip()
    sums = 0
    while line:
        sums += findnum(line, char_numlist)
        line = f.readline()

print(sums)
