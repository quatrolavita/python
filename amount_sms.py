import argparse


def amount_of_sms(string, max_symbol):
    temp = ''
    amount = 1
    for i in string:
        if len(i) > max_symbol:
            return -1
        temp = temp + ' ' + i
        if len(temp) > max_symbol:
            amount += 1
            temp = i

    return amount


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This script display amount of SMS',
                                     epilog="Git: github.com/sashalavrus")
    parser.add_argument('--s', type=str, default="Test massage", help="Enter message in quotation marks")
    parser.add_argument('--k', type=int, default=4, help="Enter max of symbols in one SMS here")
    s = parser.parse_args().s.split(" ")
    k = parser.parse_args().k

    print(amount_of_sms(s, k))
