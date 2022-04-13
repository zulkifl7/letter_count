'''
The goal is to count every alphabet in string 
and displaying the perticular letter count. 

Note that any symbols wont be counted
But, Space will be counted


Technically
----------
* I'm creating a function called letter_counter

(inside letter_counter)

* There is asentece atribute  default  with default none value
* If sentence is none there will be a user input promt 
    otherwise it will get the value of the atribute to work

* Using a dictionary to store values 
* using a loop to initialize the dictionary

* Using loops and conditional statements to 
get the matches and count

* Displaying using some loops and formating

(inside main)
* default string is none so program will get a user input
* Looping until user wants to stop
* if user say yes it will run the latter_counter
* if the use wants to stop he can say no and stop
* for invalid inputs Question will be repeated
'''


def letter_counter(sentence=None):
    if sentence == None:
        sentence = input("Enter your string here : ")

    # alphabets and string to be counted
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sent = sentence.upper()

    # creating the empty dict
    alphabet_dict = {}
    for a in alphabet:
        alphabet_dict[a] = 0

    # Counting
    for s_letter in sent:
        for a_letter in alphabet:
            if s_letter == a_letter:
                alphabet_dict[a_letter] += 1

    # Displaying
    print('''The String is\n===========\n{}\n===========\n\nLetters\n-----------'''.format(sent))
    for letter in alphabet_dict.keys():
        if alphabet_dict[letter] > 0:
            print("{} ==> {}".format(letter, alphabet_dict[letter]))


def main():
    # default string is none so program will get a user input
    count_str = "None"
    letter_counter(count_str)
    continue_q = input("Do you want to continue for another string? ").upper()

    # Looping until user wants to stop
    m = 1
    while m == 1:
        # if user say yes it will run the latter_counter
        if continue_q == "Y" or continue_q == "YES":
            letter_counter(None)
            continue_q = input(
                "Do you want to continue for another string? ").upper()
        # if the use wants to stop he can say no and stop
        elif continue_q == "N" or continue_q == "NO":
            break
        # for invalid inputs Question will be repeated
        else:
            print('''Invalid Input!\nEnter Yes or No''')
            continue_q = input(
                "Do you want to continue for another string? ").upper()


if __name__ == "__main__":
    main()
