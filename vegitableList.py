def my_function(my_formatted_sting):

    while True:
        print("What do you want to manage this array[insert, remove, add, sort, reverse, pop]")
        user = input()

        if user == "insert":
            print("what do you want to add?")
            newArray = input()
            print("Where do you want to insert?")
            newindex = int(input())
            if newindex <= len(my_formatted_sting) and newindex >= 0:
                my_formatted_sting.insert(newindex, newArray)

            else:
                print("out of range of array")
                continue


        elif user =="remove":
            print("what do you want to delete?")
            newdelete = input()
            my_formatted_sting.remove(newdelete)

        elif user =="add":
            print("What do you want to add?")
            newArray = input()
            my_formatted_sting.append(newArray)

        elif user =="sort":
            my_formatted_sting.sort()


        elif user =="reverse":
            my_formatted_sting.reverse()


        else:
            print("That is not in options")
            continue


        return my_formatted_sting

my_formatted_sting =['carrot', 'lettuce', 'onion', 'radish']
print(my_formatted_sting)

my_formatted_sting = my_function(my_formatted_sting)
for i in range(len(my_formatted_sting)):
    if i == 0:
        print("'",my_formatted_sting[0],end='')
    elif len(my_formatted_sting) > 0 and i+1 < len(my_formatted_sting):
        print(",",my_formatted_sting[i],end='')
    elif len(my_formatted_sting)-1 == i:
        print(" and", my_formatted_sting[i], "'")














