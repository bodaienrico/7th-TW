import time
import random


def get_acc_time(random_sentence):
    string = random_sentence
    word_count = len(string.split())
    while str(input('Enter "yes" when ready: ')):
        t0 = time.time()
        inputText = str(input('Enter the sentence :"%s" as fast as possible: \n' % string))
        t1 = time.time()
        acc = len(set(inputText.split()) & set(string.split()))
        acc = acc/word_count
        timeTaken = t1 - t0
        wordPM = (word_count/timeTaken)
        print(wordPM, acc, timeTaken)
        break

def print_out_random_line(random_sentence):
    print(random_sentence)


def split_sentence(random_sentence):
    lst_random_sentence = list(random_sentence)
    return lst_random_sentence


def main():
    lines = open('sentences.txt', 'r').read().splitlines()
    random_sentence = random.choice(lines)
    print_out_random_line(random_sentence)
    get_acc_time(random_sentence)

if __name__ == "__main__":
    main()