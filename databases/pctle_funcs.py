#helper funcs
def file_write(data, name):
    f = open(name,"w")
    letter=65
    for l_list in data: #prints top 5 things in list of lists
        if len(l_list) > 5:
            f.write("{}\n".format(chr(letter)))
            for i in range(5):
                f.write("{}: {} - {}%\n".format(i+1,l_list[i][0],l_list[i][1]))
            for i in range(5, len(l_list)):
                if l_list[i][1] == l_list[4][1]:
                    f.write("{}: {} - {}%\n".format(i+1,l_list[i][0],l_list[i][1]))
        else:
            f.write("{}\n".format(chr(letter)))
            for i in range(len(l_list)):
                f.write("{}: {} - {}%\n".format(i+1,l_list[i][0],l_list[i][1]))
        letter += 1
    f.close()
    
#prints top 5 of each list in sorted data
def print_le(data):
    letter = 65
    for l_list in data: #prints top 5 things in list of lists
        if len(l_list) > 5:
            print("{}".format(chr(letter)))
            for i in range(5):
                print("{}: {} - {}%".format(i+1,l_list[i][0],l_list[i][1]))
            for i in range(5, len(l_list)):
                if l_list[i][1] == l_list[4][1]:
                    print("{}: {} - {}%".format(i+1,l_list[i][0],l_list[i][1]))
        else:
            print("{}".format(chr(letter)))
            for i in range(len(l_list)):
                print("{}: {} - {}%".format(i+1,l_list[i][0],l_list[i][1]))
        letter += 1
    return
 


#creates list of dictionaries for each letter in alphabet containing data in each
#dictionary with value being letter count
def letter_dicts(data):
    data = [x.strip() for x in data]
    dict_list = [] #going to contain a dictionary for every letter in alphabet that contains
                   #countries with their values
    alphabet = []
    alph_i = 65
    for i in range(52): #creates list of all upper & lowercase letters
        alphabet.append(chr(alph_i)) # chr takes integer and returns ASCII char
        if i == 25:
            alph_i += 6 #skip non alphabet ASCII chars
        alph_i += 1
    
    for i in range(26):
        dict = {}
        dict_i = 0
        for j in data:
            if alphabet[i] or alphabet[i+26] in j:
                dict[j] = j.count(alphabet[i]) + j.count(alphabet[i+26])
        dict_list.append(dict)
        dict_i += 1
    return dict_list


#returns list of dicts with data with values converted to pct and 
#any 0 values removed
def pct_and_remove(data):
    for l_dict in data:
        del_list = []
        for country in l_dict: #creates dicts with pct values instead of letter counts
            pct = round(100*(l_dict[country] / len(country)),2)
            l_dict[country] = pct
        for country in l_dict:
            if l_dict[country] == 0: #deleting countries with none of that letter from a letters dict
                del_list.append(country)
        for i in range(len(del_list)): #delete indexes with 0 val
            l_dict.pop(del_list[i])
    return data







