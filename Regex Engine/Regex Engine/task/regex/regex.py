import sys
sys.setrecursionlimit(10000)


# compare single character
def single_char(regex, input_str):
    if not regex:
        return True
    if not input_str:
        return False
    if regex == input_str:
        return True
    if regex == '.' and input_str != '':
        return True
    if regex != input_str:
        return False


def match_strings(match_regex, match_str):
    if len(match_regex) == 0:
        return True
    if len(match_str) == 0:
        return False
    elif not single_char(match_regex[0], match_str[0]):
        return False
    # else:
    #     match_strings(match_regex[1:], match_str[1:])


def compare_substrings(string):
    regex, char = string.strip().split('|')
    # print(char.strip())
    if match_strings(regex, char):
        return True
    else:
        new_check = f'{regex}|{char[1:]}'
        return compare_substrings(new_check)


if __name__ == '__main__':
    # print(compare_substrings('apple|apple'))  # True
    # print(compare_substrings('ap|apple'))  # True
    # print(compare_substrings('le|apple'))  # True
    # print(compare_substrings('a|apple'))  # True
    print(compare_substrings('.|apple'))  # True
    print(compare_substrings('apwle|apple'))  # False
    print(compare_substrings('peach|apple'))  # False

    # print(compare_substrings(input()))
