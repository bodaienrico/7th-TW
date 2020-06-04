#import time
import random
#import sys



def print_out_random_line(random_sentence):
    print(random_sentence)


def split_sentence(random_sentence):
    lst_random_sentence = list(random_sentence)
    return lst_random_sentence
    # print(lst_random_sentence)


def typing_input():
    input_1 = input("Enter sentence:")
    input_split = list(input_1)
    return input_split
    # print(input_split)


def get_win(return_value_2, return_value):
    if return_value == return_value_2:
        print("Fuck yeah")
    else:
        print("Sorry Bro")


def main():
    lines = open('sentences.txt', 'r').read().splitlines()
    random_sentence = random.choice(lines)
    print_out_random_line(random_sentence)
    return_value = typing_input()
    return_value_2 = split_sentence(random_sentence)
    get_win(return_value_2, return_value)
    #x = print_out_random_line()
    #x.split()
    #print(x)


if __name__ == "__main__":
    main()

#TODO: input
#TODO: input compare with random text and tell accuracy
#TODO: stopwatch start from first letter and end on ENTER
#TODO: WordPerMinute calculator 