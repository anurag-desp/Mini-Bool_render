# Author: Anurag Raj    Name: MiniBool      # Mentor: Dr. Tusarkanti Dash Sir

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

# Global Variables
used = []       # The groups that were part of the matched pairs formation
unused = []     # The groups that were not the part of the matched pairs formation
total = []      # Total groups 
final_matched = []  # Finally matched groups that cannot be matched any further

# For the programmer's purposes. Display a lst with each element in a new line.
def display(lst):
    for i in lst:
        print("\t", i)  

# Removes duplicates from the list provided to it and return the new list
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

# Draw kmps for 2 variables
def twoVarKmap(minterms, dont_care, num):
    mint = [' ',' ', ' ', ' ']
    for i in range(len(minterms)):
        mint[minterms[i]] = num
    
    for i in range(len(dont_care)):
        mint[dont_care[i]] = 'X'
    
    print("\t\t  0    1")
    print("\t\t \___.___.")
    print(f"\t\t0| {mint[0]} | {mint[1]} |")
    print("\t\t |___|___|")

    print(f"\t\t1| {mint[2]} | {mint[3]} |")
    print("\t\t |___|___|")

# Draw kmps for 3 variables
def threeVarKmap(minterms, dont_care, num):
    mint = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    for i in range(len(minterms)):
        mint[minterms[i]] = num

    for i in range(len(dont_care)):
        mint[dont_care[i]] = 'X'
        
    print("\t\t  00   01   11  10")
    print("\t\t \___.___.___.___.")
    print(f"\t\t0| {mint[0]} | {mint[1]} | {mint[3]} | {mint[2]} |")

    print("\t\t |___|___|___|___|")
    print(f"\t\t1| {mint[4]} | {mint[5]} | {mint[7]} | {mint[6]} |")
    print("\t\t |___|___|___|___|")

# Draw kmps for 4 variables
def fourVarKmap(minterms, dont_care, num):
    mint = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    
    for i in range(len(minterms)):
        mint[minterms[i]] = num

    for i in range(len(dont_care)):
        mint[dont_care[i]] = 'X'

    print("\t\t   00   01  11  10")
    print("\t\t  \___.___.___.___.")
    print(f"\t\t00| {mint[0]} | {mint[1]} | {mint[3]} | {mint[2]} |")

    print("\t\t  |___|___|___|___|")
    print(f"\t\t01| {mint[4]} | {mint[5]} | {mint[7]} | {mint[6]} |")

    print("\t\t  |___|___|___|___|")
    print(f"\t\t11| {mint[12]} | {mint[13]} | {mint[15]} | {mint[14]} |")

    print("\t\t  |___|___|___|___|")
    print(f"\t\t10| {mint[8]} | {mint[9]} | {mint[11]} | {mint[10]} |")
    print("\t\t  |___|___|___|___|")

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
                 print("epis(unique)")
                 display(epis)
                 return epis

            print("epis(unique)")
            display(epis)
            return findEPIs(prime_implicants, minterms,epis)    
        
        count = 0
                
    count = 0
    length = 0
    pi = []
    for k in prime_implicants:
        for j in k:
            if j in minterms:
                count += 1

        if count >= 1:
            if len(k) > len(pi):
                pi = k
                count = 0
                continue

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
        print("epis(max covered)")
        display(epis)
        return epis

    print("epis(max covered)")
    display(epis)
    return findEPIs(prime_implicants, minterms, epis)

# Get the EPIs as argument in the function that will return  the boolean exprssion in a list with each element as the terms $
# De Morgan's fucntion:
    # check each term of the expression, if an alphabet is succeded by a ` then just append the alphabet in new term then append +, if not the append the alphabet followed by `
def deMorgans(expression, to_convert):
    # to_contert = 0: sop -> pos, to_contert = 1: pos -> sop

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

    # print(bool_list)

    deci_list = primeToDecmal(bool_list)

    minterms = []
    for i in deci_list:
        for j in i:
            if j not in minterms:
                minterms.append(j)
    
    minterms.sort()

    return minterms

# Handles all the inputs and returns a list containing the list of minterms, number of variables, 0(for maxterms) or 1(for minterms)
def takeInput():
    print("\n\t\t\t\t	\u25E6 \u25E6 \u25E6 \u2BCC  BOOLEAN EXPRESSION MINIMISER \u2BCC \u25E6 \u25E6 \u25E6")
    print("Input Formats: ")
    print("\t\u25CC 1.  Minterms")
    print("\t\u25CC 2.  Maxterms")
    print("\t\u25CC 3.  Boolean Expression")
    print("\t\u25CC 4.  Exit\n")

    choice = int(input("Enter your choice(1,2,3,4): "))

    # Handles minterm input
        # takes input
        # sorts them
        # removes duplicates
        # asks for number of variables required
            # checks if it is feseable
        # if it is a 2, 3 or 4 variable expression, then prints a K-Map
        # returns the list of minterms, number of variables, 0 in a list. 0 indicates that minterms was chosen
    if choice == 1:
        print("\n\t\t\u26E7 Keep entering the minterms, and when done with entering, just press 'enter'")
        print("\t\t\u26E7 Do not worry about order or repetition\n\n")
        minterms = []
        dont_care = []
        temp_list = []
        
        str_minterms = input("\t\tEnter (space seperated) minterms: ")
        temp_list = str_minterms.split(' ')

        str_dont_care = input("\t\tEnter (space seperated) don't care terms: ")
        str_dont_care = str_dont_care.split(' ')

        temp_list = removeall(temp_list, '')
        temp_dont_care = removeall(str_dont_care, '')

        for i in temp_list:
            minterms.append(int(i))

        for i in temp_dont_care:
            dont_care.append(int(i))

        original_minterms = []
        for i in minterms:
            if i not in dont_care:
                original_minterms.append(i)
                
        minterms = minterms + dont_care

        minterms = removeDuplicates(minterms)

        minterms.sort()
        dont_care.sort()

        # Prints the minterms and the number of minterms
        print("\n\t\t\tYour minterms\n\t\t\t\u03A3m",end = " ")
        print(tuple(original_minterms), end = "\n")

        print("\n\t\t\tYour Don't Care terms\n\t\t\t\u03A3d",end = " ")
        print(tuple(dont_care), end = "\n")

        print("\t\tTotal number of minterms entered: ", len(minterms), end = "\n\n")

        # handles the number of variables part
            # Asks if the user wishes to go with it the solution with minimum number of variables required
            # If the user wishes to give custom number of variables, then check if the given number is feseable or not
        num_of_variables = minimumPossibleVariables(minterms)

        print("\t\t\tNumber Of Variables: ", num_of_variables)

        # K-Map printing
        if num_of_variables in [2,3,4]:
            if num_of_variables == 2:
                print()
                print("K-Map for the given minterms")
                print()
                twoVarKmap(minterms, dont_care, 1)
            elif num_of_variables == 3:
                print()
                print("K-Map for the given minterms")
                print()
                threeVarKmap(minterms, dont_care, 1)
            else:
                print()
                print("K-Map for the given minterms")
                print()
                fourVarKmap(minterms, dont_care, 1)
        print()
        print()

        return [minterms, num_of_variables, original_minterms, dont_care, 1]
    

    # Handles maxterm input
    # takes input
    # sorts them
    # removes duplicates
    # asks for number of variables required
        # checks if it is feseable
    # if it is a 2, 3 or 4 variable expression, then prints a K-Map
    # converts the maxterms to corresponding minterms
    # returns the list of minterms, number of variables, 1 in a list. 1 indicates that maxterms was chosen
    elif choice == 2:
        print("\n\t\t\u26E7 Keep entering the maxterms, and when done with entering, just press 'enter'")
        print("\t\t\u26E7 Do not worry about order or repetition\n\n")

        maxterms = []
        dont_care = []
        temp_list = []
        
        str_maxterms = input("\t\tEnter (space seperated) maxterms: ")
        temp_list = str_maxterms.split(' ')

        str_dont_care = input("\t\tEnter (space seperated) don't care terms: ")
        str_dont_care = str_dont_care.split(' ')

        temp_list = removeall(temp_list, '')
        temp_dont_care = removeall(str_dont_care, '')

        for i in temp_list:
            maxterms.append(int(i))
        
        for i in temp_dont_care:
            dont_care.append(int(i))
        
        original_maxterms = []
        for i in maxterms:
            if i not in dont_care:
                original_maxterms.append(i)
                
        maxterms = maxterms + dont_care
        maxterms = removeDuplicates(maxterms)

        maxterms.sort()
        dont_care.sort()

        # Prints the maxterms and the number of maxterms entered
        print("\n\t\t\tYour maxterms\n\t\t\t\u03A0 M",end = " ")
        print(tuple(original_maxterms), end = "\n")

        print("\n\t\t\tYour Don't Care terms\n\t\t\t\u03A3d",end = " ")
        print(tuple(dont_care), end = "\n")

        print("\t\tTotal number of maxterms entered: ", len(maxterms), end = "\n\n")

        # handles the number of variables part
            # Asks if the user wishes to go with it the solution with minimum number of variables required
            # If the user wishes to give custom number of variables, then check if the given number is feseable or not
        num_of_variables = minimumPossibleVariables(maxterms)

        print("\t\t\tNumber Of Variables: ", num_of_variables)

        # Prints the K-Map
        if num_of_variables in [2,3,4]:
            if num_of_variables == 2:
                print()
                print("K-Map for the given maxterms")
                print()
                twoVarKmap(maxterms, dont_care, 0)
            elif num_of_variables == 3:
                print()
                print("K-Map for the given maxterms")
                print()
                threeVarKmap(maxterms, dont_care, 0)
            else:
                print()
                print("K-Map for the given maxterms")
                print()
                fourVarKmap(maxterms, dont_care, 0)
                
        print()
        print()

        # Converts the maxterms to minterms
        # minterms = maxToMin(maxterms, num_of_variables)
        # print(minterms)

        return [maxterms, num_of_variables, original_maxterms, dont_care, 0]
    

    # Handles the Boolean expression input
    # Asks t either put expression in SOP or POS form
    # If SOP:
        # Asks for the number of variables that the function contains
        # Takes the input expression
        # removes all ,' ', . , ()
        # seperates each + seperated term -> traverses through the list and appends in a list whatever is encountered, as soon as a + is encountered, it appends the list in another list that contains each term and empties the previous list
        # Minterms are obtained from the list obtained from above
    # If POS:
        # It is necessary to put a . here to indicate an AND operator, putting nothing will not work as it did in SOP
        # Asks for the number of variables that the function contains
        # Takes the input expression
        # removes all ,' ' , ()
        # seperates each . seperated term -> traverses through the list and appends in a list whatever is encountered, as soon as a . is encountered, it appends the list in another list that contains each term and empties the previous list
        # The list obtained above is an expression for maxterms, but hte program is optimized for minterms, so this list is sent to demorgan function that converts the list into a list of corresponding SOP expression.
        # Minterms are obtained from the above list
    elif choice == 3:
        print("\n\t\tPlease enter the expression in either SOP or POS form")
        print("\t\t\u25CC 1.  SOP")
        print("\t\t\u25CC 2.  POS")
        choice = int(input("\t\tEnter Your choice: "))

        if choice == 1:
            print("\n\t\t\t\t\u2746\u2746\u2746  SOP \u2746\u2746\u2746")

            print()
            print("\t\t._____________________________________________.")
            print("\t\t| \u25E6 OR  \u27A2  + (example: A + B)                 |")
            print("\t\t| \u25E6 AND \u27A2  nothing or . (example: AB or A.B)  |")
            print("\t\t| \u25E6 NOT \u27A2  ` (example : A`, B`)               |")
            print("\t\t|_____________________________________________|")

            print("\n\t\t\u2687 Examples for the expression: AB`C + A`B`C` or A.B`.C + A`.B`.C`, ABCD` + AC`D or A.B.C.D` + A.C`.D etc")
            print()

            # Takes input number of variables, and the SOP expression and removes the redundants
            # num_of_vars = int(input("\t\tEnter the number of variables of your function: "))
            exp = list(input("\t\tEnter the SOP expression: "))
            exp = removeall(exp, ' ')
            exp = removeall(exp, '.')
            exp = removeall(exp, '(')
            exp = removeall(exp, ')')

            dont_care = list(input("\t\tEnter the Don't Care SOP expression: "))
            dont_care = removeall(dont_care, ' ')
            dont_care = removeall(dont_care, '.')
            dont_care = removeall(dont_care, '(')
            dont_care = removeall(dont_care, ')')
            
            alphas = []

            exp = exp + ['+'] + dont_care
            for i in exp:
                if i.isalpha():
                    if i not in alphas:
                        alphas.append(i.upper())
                    if i.islower():
                        exp[exp.index(i)] = i.upper()
            
            for i in dont_care:
                if i.isalpha():
                    if i.islower():
                        dont_care[dont_care.index(i)] = i.upper()
            
            alphas.sort()            
            should_be = []
            for i in range(65, ord(alphas[-1])+1):
                should_be.append(chr(i))
                
            # obtainng the number of variables and the variables in a serial order
            num_of_vars = len(should_be)
            print("\n\t\tNumber of variables in the given boolean function: ", num_of_vars)
            print("\t\t\t The Variables: ", tuple(should_be))

            # Each + seperated term is seperated here
            new_exp = []
            term = []
            for i in exp:
                if i != '+':
                    term.append(i)
                else:
                    new_exp.append(term)
                    term = []
            if term != []:
                new_exp.append(term)

            new_dont_care_exp = []
            term = []
            for i in dont_care:
                if i != '+':
                    term.append(i)
                else:
                    new_dont_care_exp.append(term)
                    term = []
            if term != []:
                new_dont_care_exp.append(term)

            # minterms are obtained from the expression
            minterms = expToMinOrMaxterms(new_exp, should_be, 0)
            dont_care_minterms = expToMinOrMaxterms(new_dont_care_exp, should_be, 0)

            og_minterms = []
            for i in minterms:
                if i not in dont_care_minterms:
                    og_minterms.append(i)

            # Prints the minterms and the number of minterms
            print("\n\n\t\t\tYour Minterms\n\t\t\t\u03A3m",end = " ")
            print(tuple(og_minterms), end = "\n")

            print("\n\t\t\tYour Don't Care terms\n\t\t\t\u03A3d",end = " ")
            print(tuple(dont_care_minterms), end = "\n")

            print("\t\tTotal number of minterms entered: ", len(minterms), end = "\n\n")

            # K-Map printing
            if num_of_vars in [2,3,4]:
                if num_of_vars == 2:
                    print()
                    print("K-Map for the given minterms")
                    print()
                    twoVarKmap(minterms, dont_care_minterms, 1)
                elif num_of_vars == 3:
                    print()
                    print("K-Map for the given minterms")
                    print()
                    threeVarKmap(minterms, dont_care_minterms, 1)
                else:
                    print()
                    print("K-Map for the given minterms")
                    print()
                    fourVarKmap(minterms, dont_care_minterms, 1)

            print()
            print()
            
            return [minterms, num_of_vars, og_minterms, dont_care_minterms, 1]

        elif choice == 2:
            
            print("\n\t\t\t\t\u2746\u2746\u2746  POS \u2746\u2746\u2746\n")

            print()
            print("\t\t._____________________________________________.")
            print("\t\t| \u25E6 OR  \u27A2  + (example: A + B)                 |")
            print("\t\t| \u25E6 AND \u27A2  . (example: AB or A.B)             |")
            print("\t\t| \u25E6 NOT \u27A2  ` (example : A`, B`)               |")
            print("\t\t|_____________________________________________|")

            print("\t\tNOTE: please use a '.' to denote AND operator\n")
            print("\n\t\t\u2687 Examples for the expression: (A + B + C`).(A` + B` + C), (A + B + D`).(A` + C + D) etc.")
            print()

            # Takes input number of variables, and the POS expression and removes the redundants
            exp = list(input("\t\tEnter the POS expression: "))
            exp = removeall(exp, ' ')
            exp = removeall(exp, '(')
            exp = removeall(exp, ')')

            dont_care = list(input("\t\tEnter the Don't Care POS expression: "))
            dont_care = removeall(dont_care, ' ')
            dont_care = removeall(dont_care, '(')
            dont_care = removeall(dont_care, ')')
            
            alphas = []

            exp = exp + ['.'] + dont_care
            for i in exp:
                if i.isalpha():
                    if i not in alphas:
                        alphas.append(i.upper())
                    if i.islower():
                        exp[exp.index(i)] = i.upper()
            
            for i in dont_care:
                if i.isalpha():
                    if i.islower():
                        dont_care[dont_care.index(i)] = i.upper()
            
            alphas.sort()            
            should_be = []
            for i in range(65, ord(alphas[-1])+1):
                should_be.append(chr(i))
                
            # obtainng the number of variables and the variables in a serial order
            num_of_vars = len(should_be)
            print("\n\t\tNumber of variables in the given boolean function: ", num_of_vars)
            print("\t\t\t The Variables: ", tuple(should_be))

            # Each + seperated term is seperated here
            new_exp = []
            term = []
            for i in exp:
                if i != '.':
                    term.append(i)
                else:
                    new_exp.append(term)
                    term = []
            if term != []:
                new_exp.append(term)

            new_dont_care_exp = []
            term = []
            for i in dont_care:
                if i != '.':
                    term.append(i)
                else:
                    new_dont_care_exp.append(term)
                    term = []
            if term != []:
                new_dont_care_exp.append(term)

            # minterms are obtained from the expression
            maxterms = expToMinOrMaxterms(new_exp, should_be, 1)
            dont_care_maxterms = expToMinOrMaxterms(new_dont_care_exp, should_be, 1)

            og_maxterms = []
            for i in maxterms:
                if i not in dont_care_maxterms:
                    og_maxterms.append(i)

            # Prints the maxterms and the number of maxterms
            print("\n\n\t\t\tYour maxterms\n\t\t\t\u03A3m",end = " ")
            print(tuple(og_maxterms), end = "\n")

            print("\n\t\t\tYour Don't Care terms\n\t\t\t\u03A3d",end = " ")
            print(tuple(dont_care_maxterms), end = "\n")

            print("\t\tTotal number of maxterms entered: ", len(maxterms), end = "\n\n")

            # K-Map printing
            if num_of_vars in [2,3,4]:
                if num_of_vars == 2:
                    print()
                    print("K-Map for the given maxterms")
                    print()
                    twoVarKmap(maxterms, dont_care_maxterms, 0)
                elif num_of_vars == 3:
                    print()
                    print("K-Map for the given maxterms")
                    print()
                    threeVarKmap(maxterms, dont_care_maxterms, 0)
                else:
                    print()
                    print("K-Map for the given maxterms")
                    print()
                    fourVarKmap(maxterms, dont_care_maxterms, 0)

            print()
            print()
            
            return [maxterms, num_of_vars, og_maxterms, dont_care_maxterms, 0]

    elif choice == 4:
        print("\t\t\t\t\t\t. . . . . \u2363 THANK YOU! \u2363 . . . . .\n")
        exit(0)
    
    else:
        print("\n\t\t\t\t\t\t##### INVALID CHOICE! #####\n")
        return 0

if __name__ == "__main__":

    while True:
        # Getting the results of the input and seperated them for convenience
        input_results = takeInput()

        # Handling the Invalid Choice condition
        while input_results == 0:
            input_results = takeInput()

        minterms = input_results[0]
        num_of_variables = input_results[1]
        original_minterms = input_results[2]
        dont_care = input_results[3]
        zero_or_one = input_results[4]

        if minterms == []:
            print("There is NOTHING to solve here!")
            continue

        # Obtaining the list of binary numbers for the given list of minterms with number of bits ineach equal to the given number of variables
        binary_list = binaryConvertor(minterms, num_of_variables)

        # Obtaining the grouped binary list based on the number of 1's each binary number has
        grouped_binary_list = groupTerms(binary_list)

        # Obtaining the prime implicants for the given minterms, in binary and 1's ,0's and '_'s format
        prime_implicants = matchPairs(grouped_binary_list)
        prime_implicants = removeDuplicates(prime_implicants)

        # If only one group is formed based on the number of 1's they have then it doesn't make sense to match them as they all will we unused and hence a prime implicant, so when this type of group is sent to matchPairs() function, it will return [], also unused will be [], to will unused as it should be this condition is used
        if len(grouped_binary_list) == 1:
            unused = grouped_binary_list[0]

        # All the possible prime implicants are obtained
        prime_implicants = unused + prime_implicants
        prime_implicants = removeDuplicates(prime_implicants)

        print("prime_implicants")
        display(prime_implicants)

        # Obtaining the corresponding decimals or minterms involved in each of the prime implicant. This will later be used to find Essential Prime Implicants
        prime_decimals = primeToDecmal(prime_implicants)
        print("prime_decimals")
        display(prime_decimals)
        
        decimals_to_send = prime_decimals.copy()    # So that the original list is unchanged


        to_send = original_minterms.copy()   # So that the original list of minterms is unchanged

        # Obtaining the Essential Prime implicants in the form of lists of minterms
        EPIs = findEPIs(decimals_to_send, to_send, [])
        print("EPIs")
        display(EPIs)

        # Obtaining the Essential Prime Implicants from the list of prime implicants
        EPIs_binary = []
        for i in EPIs:
            EPIs_binary.append(prime_implicants[prime_decimals.index(i)])

        # Getting the SOP expression for the EPIs
        sop = getSop(EPIs_binary)

        print("\t\t\t\u2740 The minimised expression in SOP form \u2740")
        print("\t\t\t\t", end = '')

        # if SOP == [], then the solution will always be true.
        if sop == []:
            print(1," Always TRUE")

        for i in range(len(sop)):
            for j in sop[i]:
                print(j, end = "")

        print()
        print()

        print("\t\t\t\u2740 The minimised expression in POS form \u2740")
        print("\t\t\t\t", end = '')

        # PRinting the POS expression  
        if sop != []:    
            pos = deMorgans(sop, 0)
            for i in pos:
                for j in i:
                    print(j, end = '')
                print(' ', end ='')
        else:
            print("1 Always TRUE")

        print()
        print()
        print()

        # Printing the solution K-Map if the number of variables is 2 ,3 or 4
        temp_dont_care = []
        if num_of_variables in [2,3,4]:
            print("\tSolution in K-Map\n")
            for each in EPIs:
                for i in each:
                    if i in dont_care:
                        temp_dont_care.append(i)
                if num_of_variables == 2:
                    twoVarKmap(each, temp_dont_care, zero_or_one)
                    print()
                elif num_of_variables == 3:
                    threeVarKmap(each, temp_dont_care, zero_or_one)
                    print()
                else:
                    fourVarKmap(each, temp_dont_care, zero_or_one)
                    print()
                temp_dont_care = []

        print()
        print()
        print("\t\t\t\t\t\t   \u273E \u273E \u273E \u273E \u273E  \u2744  \u273E \u273E \u273E \u273E \u273E")

        # making them empty as they are global variables and to make this program endless until exit is entered, they need to be refreshed for each iteration
        used = []
        unused = []
        total = []
        final_matched = []


    




