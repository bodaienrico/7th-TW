#import time
import random
#import sys



def print_out_random_line(random_sentence):
    print(random_sentence)


def split_sentence(random_sentence):   
    lst_random_sentence = list(random_sentence)
    print(lst_random_sentence)
   

def typing_input():
    input_1 = input("Enter sentence:")
    input_split = list(input_1)
    print(input_split)
    


def main():
    lines = open('sentences.txt', 'r').read().splitlines()
    random_sentence = random.choice(lines)
    print_out_random_line(random_sentence)
    typing_input()
    split_sentence(random_sentence)
    #x = print_out_random_line()
    #x.split()
    #print(x)


if __name__ == "__main__":
    main()

#TODO: input
#TODO: input compare with random text and tell accuracy
#TODO: stopwatch start from first letter and end on ENTER
#TODO: WordPerMinute calculator 