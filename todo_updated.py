action = input("Please specify a command [list, add, mark, archive]: ")
# task_list = ["[ ] lalal"]

my_todo_file = 'todos.txt'

my_file = open(my_todo_file,'r')
task_list = my_file.read().splitlines()
my_file.close()

def add(chosen_list):
    what_to_add = "[ ] "
    what_to_add += input("Add an item: ")
    chosen_list.append(what_to_add)
    print("Item added.")

def list_todos(chosen_list):
    print("You've saved following to-do items:")
    for i in chosen_list:
        print(chosen_list.index(i)+1,i)

def marking(chosen_list):
    print("You've saved following to-do items:")
    for i in chosen_list:
        print(chosen_list.index(i)+1,i)
    marked = int(input("which one you want to mark as completed?"))-1 # wziecie nr todosa od urzytkownika i odjecie 1, zeby miec nr indeksu
    confirmation = chosen_list[marked]
    task_to_mark = list(chosen_list[marked]) # zmiana slowa na liste liter
    task_to_mark[1] = 'x' # zamiana drugiej pozycji w liscie, ze spacji na x
    task_to_mark = ''.join(task_to_mark) # polaczenie listy spowrotem w slowo
    chosen_list[marked] = task_to_mark
    print(confirmation[4:len(confirmation)]+" is completed")

# to update
def archive(chosen_list):
    check_mark = "[x]"
    not_done = [i for i in chosen_list if check_mark not in i]
    return not_done
    print("All completed tasks got deleted")  

# to update

  
if action == "add": add(task_list)

if action == "list": list_todos(task_list)

if action == "mark": marking(task_list)

if action == "archive":
    task_list = archive(task_list)


with open(my_todo_file, 'w') as output:
    for row in task_list:
        output.write(str(row) + '\n')

# print(task_list)
