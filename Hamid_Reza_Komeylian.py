# 1402-03-17 - Ver:10
# Hamid Reza Komeylian
# +989127982546

from colorama import Fore

# split data


def splitter(d):
    d = d.split(',')
    d[2] = d[2].split(';')
    d[3] = d[3].split(';')
    d[4] = d[4].split(';')
    d[0] = int(d[0])
    d[1] = int(d[1])
    for i in range(len(d[3])):
        d[3][i] = int(d[3][i])
    for i in range(len(d[4])):
        # last date in line combined with \n   a like YES\n
        if d[4][i] == 'YES' or d[4][i] == 'YES\n':
            d[4][i] = True
        else:
            d[4][i] = False
    return d


# calculate_voters 1 - 5
def calculate_voters(file_path):
    # Read data from file
    f = open(file_path, 'r')
    a = f.readlines()
    f.close()
    # Make dictionary for voters
    mydic = {}
    # Calculate voters in dictionary
    for i in range(1, len(a)):
        a[i] = splitter(a[i])
        for ii in range(len(a[i][2])):
            key = a[i][2][ii]
            value = a[i][3][ii]
            if key in mydic:
                mydic[key] += value
            else:
                mydic[key] = value

    for key, value in mydic.items():
        mydic[key] = value/i
    return mydic


# calculate_voters Percentage
def calculate_voters_p(file_path):
    # Read data from file
    f = open(file_path, 'r')
    a = f.readlines()
    f.close()
    # Make dictionary for voters
    mydic2 = {}
    # Calculate voters in dictionary
    for i in range(1, len(a)):
        a[i] = splitter(a[i])
        for ii in range(len(a[i][2])):
            key = a[i][2][ii]
            value = a[i][3][ii]
            if key in mydic2:
                mydic2[key] += value
            else:
                mydic2[key] = value

    summ = sum(mydic2.values())
    # print(summ)
    for key, value in mydic2.items():
        mydic2[key] = value/summ
    return mydic2


# calculate voters Acceptance
def calculate_voters_A(file_path):
    # Read data from file
    f = open(file_path, 'r')
    a = f.readlines()
    f.close()
    # Make dictionary for voters
    mydic3 = {}
    # Calculate voters in dictionary
    for i in range(1, len(a)):
        a[i] = splitter(a[i])
        # True + Ture = 2 | True + False = 1 | False + False = 0 | True = 1 / False = 0
        for ii in range(len(a[i][2])):
            #print(a[i][2][ii], a[i][4][ii])
            key = a[i][2][ii]
            value = a[i][4][ii]
            if key in mydic3:
                mydic3[key] += value
            else:
                mydic3[key] = value

    for key, value in mydic3.items():
        mydic3[key] = value/i
    return mydic3


# Print the Resaults:
def printresult():
    print(F'\n\n{Fore.RED}Resault voters 1 - 5 :{Fore.WHITE}\n')
    for key, value in calculate_voters(file_path).items():
        print(F'{key}\t{Fore.GREEN}{value:.2f}{Fore.WHITE}')
    print(F'{"-"*18}')
    total_sum = (sum(calculate_voters(file_path).values())) / \
        (len(calculate_voters(file_path)))
    print(F'Meyangin  :  {Fore.MAGENTA}{total_sum:.2f}{Fore.WHITE}')
    print(F'\n\n')


# Print the Resaults 2:
def printresult2():
    print(F'\n\n{Fore.RED}Resault Percentage:{Fore.WHITE}\n')
    for key, value in calculate_voters_p(file_path).items():
        print(F'{key}\t{Fore.GREEN}{value*100:.3f} %{Fore.WHITE}')
    print(F'{"-"*12}')
    total_sum = (sum(calculate_voters_p(file_path).values()))
    print(F'sum  :  {Fore.MAGENTA}{total_sum*100:.3f} %{Fore.WHITE}')
    print(F'\n\n')


# Print the Resaults 3:
def printresult3():
    print(F'\n\n{Fore.RED}Resault voters Get YES  :{Fore.WHITE}\n')
    for key, value in calculate_voters_A(file_path).items():
        print(F'{key}\t{Fore.GREEN}{value*100:.2f} %{Fore.WHITE}')
    print(F'{"-"*22}')
    total_sum = (sum(calculate_voters_A(file_path).values())) / \
        (len(calculate_voters_A(file_path)))
    print(F'Meyangin  :  {Fore.MAGENTA}{total_sum*100:.2f} %{Fore.WHITE}')
    print(F'\n\n')


# print All Resaults:
def allprint(file_path):
    # Part 1
    calculate_voters(file_path)
    printresult()

    # Part 2
    calculate_voters_p(file_path)
    printresult2()

    # Part 3
    calculate_voters_A(file_path)
    printresult3()

    return allprint


def allprint2(file_path):
    # calculate_voters(file_path)
    # calculate_voters_p(file_path)
    # calculate_voters_A(file_path)

    # print(mydic3)

    print(
        F'\n\n{Fore.RED}Resault    (voters 1 - 5)  (Voters Percentage)      (Voters Get YES){Fore.WHITE}')
    for key, value in calculate_voters(file_path).items():
        print(
            F'{Fore.LIGHTCYAN_EX}{"-"*68}{Fore.WHITE} \n{key.ljust(15)}\t{Fore.GREEN}{value:.2f}\t\t{calculate_voters_p(file_path)[key]*100 if key in calculate_voters_p(file_path) else None: .3f} % \t\t{calculate_voters_A(file_path)[key]*100 if key in calculate_voters_A(file_path) else None: .2f} % {Fore.WHITE}')
    print(F'{"="*68}')
    total_sum = (sum(calculate_voters(file_path).values())) / \
        (len(calculate_voters(file_path)))
    total_sum2 = (sum(calculate_voters_p(file_path).values()))
    total_sum3 = (sum(calculate_voters_A(file_path).values())) / \
        (len(calculate_voters_A(file_path)))

    print(F'{"Avg/Sum ".ljust(15)}\t{Fore.LIGHTYELLOW_EX}{total_sum:.2f}\t\t{total_sum2*100:.3f} %\t\t {total_sum3*100:.2f} %{Fore.WHITE}')
    print(F'\n\n')


###########################################################################

# Call the function with the file path
file_path = "C:\Python\Data.txt"

# report 1:
#allprint(file_path)


# report 2:
allprint2(file_path)
