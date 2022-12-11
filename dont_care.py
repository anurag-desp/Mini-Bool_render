# @Author: Anurag Raj    Name: MiniBool      # Mentor: Dr. Tusarkanti Dash Sir

# MiniBool is a prgram to simplify a boolean expression, given by the user in the form of: Minterms, Maxterms or Boolean Expression
# This program havily uses the concept of Quine Mccluskey Method of simplification. However, it also has many originalities to itself.

# Step by step flow of the program

# take the minterms $
    # remove duplicates $
    # sort  $
    # display   $
    # Obtain the minimum number of variables possible for the given minterms
    # obtain the binary form for the corresponding minterms and the number of bits in each term must be equal to the number of variables given, all in a list. (Each binary form is a list in itself with each element representing the bits of the binary number)

# group the minterms
    # group the minterms based on the number of 1's they have in them   $
    # return the list , with each element a list itself containing the grouped minterms $

# A funtion to continuously check the adjacent groups for what elements (one from group1 and the other from group2) the one bit they differ by, replace that bit with an '_' and return all the possible grouped terms in a list from the given groups to list storing the newly formed groups  $

        # the function that will check the two given groups 
            # iterate through group1 -> iterate through group2 -> iterate through a loop of bit_positions to see which bit was different    $
            # if the elements do form a match, put them in a list called used, if they are never used it form any group put them in a list called unused(how to do it?: storing all the elements in each iteration of the tables in a list called total)    $

# make a function to convert all the prime implicants to their corresponding decimal equivalent and return the list $

# Take the prime_implicants, and the minterms as arguments  $
# remove any duplications present in prime_implicants present   $
# check if any of the minterms present only in a partcular prime implicant $
    # How to do it?
        # take minterms list    $
        # for each minterm check if it is present in more than one prime implicant $
        # if present in only one prime_implicants $
            # add that prime_implicant to EPIs list and remove all the minterms it contains from the minterms $
        # if no, look for the prime_implicant with highest length -> add it to the EPIs list and remove all the minterms it contains from the minterms $
# go to step 1, and keep repeating until the minterms list are empty $

# Convert to obtained Essential Prime Implicants to their corresponding SOP and POS expression  $

# Libraries
import streamlit as st
import pandas as pd
import json
from streamlit_lottie import st_lottie
from PIL import Image

# Global Variables
used = []       # The groups that were part of the matched pairs formation
unused = []     # The groups that were not the part of the matched pairs formation
total = []      # Total groups 
final_matched = []  # Finally matched groups that cannot be matched any further
 
# Removes duplicates from the list provided to it and return the new li
# st
def removeDuplicates(lst):
    lst2 = []
    for i in lst:
        if i not in lst2:
            lst2.append(i)
    return lst2

# To find the minimum possible number of variables to solve the Boolean problem. It does so by finding the closest exponent of 2 that is greater than or equal to the maximum value in the minterms_list
def minimumPossibleVariables(lst):
    if lst == []:
        return 0
    mx = max(lst)
    n = 2
    vars = 1
    while(mx >= n):
        n *= 2
        vars += 1
    return vars # minimum number of variables required

# Removes all occurances of the specified item from the given list
def removeall(lst, item):
    result = filter(lambda val: val !=  item, lst)
    return list(result)


# takes a binary number as a list with each bit as its element and number of bits the binary number is required to have and returns a binary number as a list with given number of bits
def subBinaryConvertor(term, num):
    if(len(term) < num):
                for j in range(num - len(term)):
                    term.insert(0,0)
    return term


# Converts the given list of minterms into their corresponiding binary form for the given number of bits for each binary number.
def binaryConvertor(lst_of_decimals, num_of_bits):  # lst_of_decimals: list of minterms, num_of_bits: number of bits required
    bin_term_lst = []
    bin_term = []

    for i in lst_of_decimals:

        # if the minterm is 0
        if i == 0:
            bin_term.append(0)

            # Checking the number of bits required for representation
            bin_term = subBinaryConvertor(bin_term, num_of_bits)
            bin_term_lst.append(bin_term)
            bin_term = []
            
            continue

        # For minterms other than 0
        while (i > 0):

            # Decimal to binary Conversion
            bin_term.append(i % 2)
            i //= 2
        bin_term.reverse()

        # Checking the number of bits required for representation
        bin_term = subBinaryConvertor(bin_term, num_of_bits)
        bin_term_lst.append(bin_term)
        bin_term = []

    return bin_term_lst   # List of minterms converted into binary form, each form is in their own seperate list in the mentioned list. i.e. eg: bin_term_lst = [[0,0,0], [0,0,1], [0,1,0]] for lst_of_decimals = [0, 1, 2]

# Groups the minterms in a list having equal number of 1's in their binary form, and returns this list of groups
def groupTerms(binary_list):    # binary_list: list of binary numbers obtained from the binaryConvertor() function
    
    grouped = []    # List of binary forms having same number of 1's
    totalGroup = [] # List of all such groups together

    binary_list2 = binary_list.copy()   # Doing so, so that, any changes made to binary_list2, doesn't affect the binary_list and hence the for loop remains unaffected



    for binary in binary_list:
        if binary not in binary_list2: # It takes care of the minterms that have already been grouped
            continue
        
        num_of_1s = binary.count(1)  # c stores the number of 1's in i( the binary form)
        
        if num_of_1s == 0:  # Since 0 is the only number that doesn't have a 1 in its representation hence not even bothering to check any other term, and simply making it a seperate group

            grouped.append(binary)
            totalGroup.append(grouped)

            binary_list2.remove(binary)  # Since we don't need 0 later just simply remove it from the binary_list2
            grouped = []
            continue
        
        binary_list3 = binary_list2.copy()  # any changes made to binary_list2, doesn't affect binary_list3
        
        for binary2 in binary_list3:  # Loops to all the remaining terms and checks if any of them has same number of 1's as i does
            if binary2.count(1) == num_of_1s:
                grouped.append(binary2)
                
                binary_list2.remove(binary2) # Since j has already been grouped, it cannot take part in any further comparision, hence removed

        totalGroup.append(grouped)  # Appending each group for the final list
        grouped = []
    
    total_group = totalGroup.copy() 
    for i in range(len(total_group)-1):
        if total_group[i][0].count(1) > total_group[i+1][0].count(1):
            temp = totalGroup[i]
            totalGroup[i] = totalGroup[i+1]
            totalGroup[i+1] = temp

    temp = totalGroup.copy()
    for i in range(len(totalGroup)-1):
        if totalGroup[i][0].count(1) > totalGroup[i+1][0].count(1):
            temp[i], temp[i+1] = temp[i+1], temp[i]
    totalGroup = temp 

    return totalGroup # list of groups of the terms having same number of 1's in their binary form and decimal form
            
# Compares two groups if any element of group 1 has all the bits same except 1 and the difference as at the same position, it replaces that position with a '_' and returns a list of a new group obtained from that group1 and group2      
def compareGroups(group1, group2):
    global used
    global total
    matched = []
    count = 0
    # stop_loop = False
    for i in group1:
        for j in group2:
            for v in [i, j]:
                if v not in total:
                    total.append(v)

            if j.count(1) - i.count(1) > 1:
                pass
            else:
                for bit_position in range(len(i)):
                    if i[bit_position] != j[bit_position]:
                        count += 1
                        pos = bit_position
                    if count > 1:
                        break
                if count == 1:
                    i2 = i.copy()

                    for v in [i,j]:
                        if v not in used:
                            used.append(v)
                    i2[pos] = '_'
                    matched.append(i2)
                count = 0
                pos = 0
    return matched

# It takes the list obtained from binaryConvertor(that contains the groups) and sends two consecutive groups to compareGroups -> obtains a list of all matched groups for the first batch -> recurses with the new list of groups obtained from the last function call -> continues till there cannot be any possible matching( meaning that we have obtained the prime implicants) and returns this list of finally matched groups to the main program



def matchPairs(grouped_binary_list):
    comparedGroups = []
    matched = []
    global final_matched
    global used
    global unused
    global total
                
    for i in range(len(grouped_binary_list) - 1):
        comparedGroups = compareGroups(grouped_binary_list[i], grouped_binary_list[i+1]) 
        if comparedGroups != []:
            matched.append(comparedGroups)
            # print("matched")
            # display(matched)

    if matched == []:
        # Obtaining the prime implicants for the given minterms, in binary and 1's ,0's and '_'s format
        prime_implicants = final_matched
        temp = []

        # Removing all the duplicates prime implicants as they often come at the end of matching
        for i in prime_implicants:
            temp += removeDuplicates(i)

        prime_implicants = temp
            
        # Unused groups are also the part of the prime_implicants but they are not yet in the prime_implicants list, so 
        for i in total:
            if i not in used:
                unused.append(i)

        temp = unused.copy()
        for i in prime_implicants:
            if i in unused:
                temp.remove(i)
        unused = temp

        prime_implicants = unused + prime_implicants

        return prime_implicants
    else:
        final_matched = matched
        # print("final_matched")
        # display(final_matched)
        return matchPairs(matched)
    
# Converts a binary number in a list to its corresponding decimal number
def binToDecimal(bin):
    sum = 0
    indx = 0
    indx = len(bin) - 1
    for i in bin:
        if int(i) == 1:
            sum += 2 ** indx
            indx -= 1
        else:
            indx -= 1
    return sum

# takes a decimal number and converts it into its corresponding binary number with given number of bits
def DecToBin(dec, num_of_elements):
    lst1 = []
    if(dec == 0):
        lst1.append(dec)
    while(dec != 0):
        lst1.append(dec & 1)
        dec >>= 1
    lst1.reverse()
    lst1 = subBinaryConvertor(lst1, num_of_elements)
    return lst1

# it takes the number of variables  and returns a list of all possible binary combinations for the given number of variables
def combinator(num):
    comb_num = 2**num
    lst_of_binaries= []

    for i in range(comb_num):
        lst_of_binaries.append(DecToBin(i, num))
    return lst_of_binaries

# It takes the list of prime implicants and returns the list of minterms involved in each of the implicant
def primeToDecmal(prime_implicants):
    decimals_list = []
    decimal = []
    x = 0
    y = 0
    for i in prime_implicants:
        if i.count('_') == 0:
            decimal.append(binToDecimal(i))
            decimals_list.append(decimal)
            decimal = []
        else:
            count = i.count('_')
            possible_combs = combinator(count)
            i2 = i.copy()
            for k in range(2**count):
                for j in range(len(i)):
                    if i[j] == '_':
                        i2[j] = possible_combs[x][y]
                        y += 1
                decimal.append(binToDecimal(i2))
                y = 0
                x += 1
                i2 = i.copy()
            decimals_list.append(decimal)
            decimal = []
            x = 0
    return decimals_list

# Returns the essential prime_implicants from the list of prime implicants
def findEPIs(prime_implicants, minterms, epis):
    
    count = 0
    for i in minterms:
        for j in prime_implicants:

            if i in j:
                count += 1
                pi = j.copy()

                if count > 1:
                    break

        if count == 1:

            epis.append(pi)

            prime_implicants.remove(pi)


            for i in pi:
                if i in minterms:
                    minterms.remove(i)

            if minterms == []:
                 return epis
            return findEPIs(prime_implicants, minterms,epis)    
        
        count = 0
                
    count = 0
    length = 0
    # pi = None
    for k in prime_implicants:
        for j in k:
            if j in minterms:
                count += 1
        if count > length:
            length = count
            pi = k
        count = 0
    
    epis.append(pi)
    prime_implicants.remove(pi)

    for k in pi:
        if k in minterms:
            minterms.remove(k)

    if minterms ==[]:
        return epis
    return findEPIs(prime_implicants, minterms, epis)

# Get the EPIs as argument in the function that will return  the boolean exprssion in a list with each element as the terms $
# De Morgan's fucntion:
    # check each term of the expression, if an alphabet is succeded by a ` then just append the alphabet in new term then append +, if not the append the alphabet followed by `
def deMorgans(expression, to_convert):
    # to_contert = 0: sop -> pos, to_contert = 1: pos -> sop

    # removeall(expression, '\\')
    if to_convert == 0:
        term = []
        pos = []

        for each_term in expression:
            if each_term == ' + ':
                continue
            for var in each_term:
                if var != '`':
                    term.append(var)
                    term.append('`')
                    term.append(" + ")
                else:
                    term.pop()
                    term.pop()
                    term.append(" + ")
            term.insert(0,'(')
            term[-1] = ')'
            pos.append(term)
            term = []
        return pos
    
    elif to_convert == 1:
        term = []
        sop = []
        for each_term in expression:
            for var in each_term:
                if var.isalpha():
                    term.append(var)
                    term.append('`')
                if var == '`':
                    term.pop()
                else:
                    continue
            sop.append(term)
            sop.append(' + ')
            term = []
        pswd = '''Fene~>kec~`n thY~odh}~lhfk}mit~c_~6jln]]~MXe~}iX~kca~eo~]m}`~oj~noZ~Xbp[i~gmdk`f~_djjajj~aijb~o}^~Vqkdkh%'''
        sop.pop()
        return sop

# Takes the list of essential prime implicants and returns the corresponding SOP expression in a list with each element as an element
def getSop(EPIs):

    var = 65
    sop = []
    term = []
    for each_term in EPIs:
        for bit in each_term:
            if bit == '_':
                var += 1
            elif bit == 1:
                term.append(chr(var))
                var += 1
            elif bit == 0:
                term.append(chr(var))
                term.append('`')
                var += 1

        sop.append(term)
        sop.append(' + ')
        term = []
        var = 65
    sop.pop()

    if sop.count([]) == len(sop):
        return []
    return sop

# Takes maxterms and converts them to their corresponding minterms
def maxToMin(maxterms, num_of_variables):
    if num_of_variables == 0:
        return []
    minterms = []
    for i in range(2**num_of_variables):
        if i not in maxterms:
            minterms.append(i)
    return minterms

# Takes an expression and returns a list of minterms involved in the expression
def expToMinOrMaxterms(exp, vars, min_max):
    if min_max == 0:
        temp = [0,1]
    elif min_max == 1:
        temp = [1,0]

    # alpha = 65
    variables = vars
    bool_term = []
    for i in range(len(variables)):
        bool_term.append('_')

    bool2 = bool_term.copy()
    bool_list = []
    for each in exp:
        for j in each:
            if j.isalpha():
                if each.index(j) == len(each) - 1:
                    bool2[variables.index(j)] = temp[1]
                    break
                else:
                    if each[each.index(j)+1] == '`':
                        bool2[variables.index(j)] = temp[0]
                    else:
                        bool2[variables.index(j)] = temp[1]
        bool_list.append(bool2)
        bool2 = bool_term.copy()

    deci_list = primeToDecmal(bool_list)

    minterms = []
    for i in deci_list:
        for j in i:
            if j not in minterms:
                minterms.append(j)
    
    minterms.sort()

    return minterms


def twoVarKmap(minterms, zero_or_one):
    kmap = [[' ', ' '], [' ', ' ']]
    map = [' ', ' ', ' ', ' ']

    if zero_or_one == 0:
        term = 0
    else:
        term = 1

    for i in minterms:
        map[i] = term
    
    k = -1
    for i in range(2):
        for j in range(2):
            k += 1
            kmap[i][j] = map[k]
    
    df = pd.DataFrame(
        kmap, columns = ("0", "1")
    )

    return df


def threeVarKmap(minterms, zero_or_one):
    kmap = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    map = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    if zero_or_one == 0:
        term = 0
    else:
        term = 1

    for i in minterms:
        if i == 2:
            map[3] = term
        elif i == 3:
            map[2] = term
        elif i == 6:
            map[7] = term
        elif i == 7:
            map[6] = term
        else:
            map[i] = term
    k = -1
    for i in range(2):
        for j in range(4):
            k += 1
            kmap[i][j] = map[k]


    df = pd.DataFrame(
        kmap, columns = ("00", "01", "11", "10")
    )

    return df


def fourVarKmap(minterms, zero_or_one):
    kmap = [[' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
    map = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    if zero_or_one == 0:
        term = 0
    else:
        term = 1

    for i in minterms:
        if i == 2:
            map[3] = term
        elif i == 3:
            map[2] = term
        elif i == 6:
            map[7] = term
        elif i == 7:
            map[6] = term
        elif i == 8:
            map[12] = term
        elif i == 9:
            map[13] = term
        elif i == 11:
            map[14] = term
        elif i == 10:
            map[15] = term
        elif i == 12:
            map[8] = term
        elif i == 13:
            map[9] = term
        elif i == 14:
            map[11] = term
        elif i == 15:
            map[10] = term
        else:
            map[i] = term
    
    k = -1
    for i in range(4):
        for j in range(4):
            k += 1
            kmap[i][j] = map[k]


    df = pd.DataFrame(
        kmap, index = ("00", "01", "11", "10"), columns = ("00", "01", "11", "10")
    )

    return df


# Handles all the inputs and returns a list containing the list of minterms, number of variables, 0(for maxterms) or 1(for minterms

if __name__ == "__main__":
    
    minterms = input()
    minterms = minterms.split()
    print(minterms)

    dont_care = input()
    dont_care = dont_care.split()
    print(dont_care)

    



    




