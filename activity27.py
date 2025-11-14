

print("Adding Data to Dictionary..")
print("==================================")
tuloy = True

empty_dictionary = {}

def print_anime():
    for i,j in empty_dictionary.items():
        print(f"Code {i}, Title {j}")
    #for i in empty_dictionary.values():
        #print(f"Code {i}")

def to_search(key):
    print("Searching....")
    print(f"Result shows {empty_dictionary[key].upper()} on our database")


while tuloy == True:
    keys = input("Input keys for this anime: ")
    value = input ("Enter anime title: ")
    
    empty_dictionary[keys] = value

    choice = input ("Would you like to continue adding anime \ny-Yes\nn-NO\np-Print\ns-Search\n: ").lower()

    if choice == 'y':
        print("Continuing....")
        continue
    elif choice == 'n':
        print ("Stopped..")
        break
    elif choice == 'p':
        print_anime()
        continue

    elif choice == 's':
        code = input("Please input the key word: ")
        to_search(code)
        continue

    else:
        print("Invalid...")
        continue


