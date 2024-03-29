import sys
import pctle_funcs as p

#returns sorted list of dicts based on highest letters in country name
def highest_letters(data): 
    sorted_countries = []
    for l_dict in data:
        del_list = []
        for country in l_dict:
            if l_dict[country] == 0: #deleting countries with none of that letter from a letters dict
                del_list.append(country)
        for i in range(len(del_list)): #delete indexes with 0 val
            l_dict.pop(del_list[i])
        sorted_countries.append(list(sorted(l_dict.items(), key = lambda x:x[1],reverse=True)))
    return sorted_countries

#returns sorted list in order of highest percentage of letters in list of dicts
def h_pct_letter(data): 
    data = p.pct_and_remove(p.letter_dicts(data))
    sorted_pct = []
    for l_dict in data:
        sorted_pct.append(list(sorted(l_dict.items(), key = lambda x:x[1],reverse=True)))
    return sorted_pct

#returns sorted list in order of lowest percentage of letters in list of dicts
def l_pct_letter(data):
    data = p.pct_and_remove(p.letter_dicts(data))
    sorted_pct = []
    for l_dict in data:
        sorted_pct.append(list(sorted(l_dict.items(), key = lambda x:x[1],reverse=False)))
    return sorted_pct



if __name__ == "__main__":
    #if input data(argv[1]) and output (argv[2])
    if len(sys.argv) == 3:
        f = open(sys.argv[1],"r")
        data = f.readlines()
        print(h_pct_letter(data))
        #p.file_write(h_pct_letter(data), sys.argv[2])
        
    #if only input (argv[1])
    elif len(sys.argv) == 2:
        f = open(sys.argv[1],"r")
        data = f.readlines()
        print(h_pct_letter(data))
    
    #if no command line arguments
    else:
        f = open("countries.txt", "r")
        data = f.readlines()
        p.print_le(h_pct_letter(data))