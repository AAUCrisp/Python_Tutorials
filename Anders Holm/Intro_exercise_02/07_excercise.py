

word_list = ["a car", "a house", "a dog", "kids", "a tv", "money"]

def format_list(word_list):
    i = 0
    string = " "
    for i in word_list:
        if i == word_list[-1]:
            string = string + "and " + i
        elif i == word_list[-2]:
            string = string + i + " "
        else:
            string = string + i + ", "
    return string
 
def main():
    print("When I get older. I want" + format_list(word_list))

main()
