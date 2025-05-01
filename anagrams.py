import os

def symmetric(n):
    if n == 1:
        string = "0"
        list1 = [string]
        return list1
    else:
        list = symmetric(n-1)
        list1 = []
        for w in list:
            for i in range(len(w)+1):
                list1.append(w[:i] + str(n-1) + w[i:])
        return list1

while True:
    word = str(input("Enter a line of scrambled text (enter to exit): " ))

    if word == "":
        print("")
        break

    else:
        word1 = word.lower()
        length = len(word1)
        list = symmetric(length)

        for i in range(len(list)):
            teststring = ""
            for j in range(len(list[i])):
                teststring = teststring + word1[int(list[i][j])]
            # print(teststring)
            my_local_file = os.path.join(os.path.dirname(__file__), 'dict.txt')
            for line in open(my_local_file):
                if teststring == line.rstrip().lower():
                    print(line.rstrip())
