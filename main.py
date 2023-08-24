from functions import write_todos, get_todos
import time
import glob


now = time.strftime("%b %d, %Y %H:%M:%S")
print("The time is below.")
print("It is", now)
while True:
    user_action = input("Type add, edit, complete, show or exit: ")
    user_action = user_action.strip()


    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos("todos.txt", todos)
        #file = open('todos.txt', 'w')
        #file.writelines(todos)
        #file.close()



    elif user_action.startswith("edit"):
        number = int(user_action[5:])
        number = number - 1

        todos = get_todos()

        change = input(f"What do you want to replace {todos[number]} with? ")
        todos[number] = change + '\n'

        write_todos("todos.txt", todos)



    elif user_action.startswith("show"):
        try:
            #file = open('todos.txt', 'r')
            #todos = file.readlines()
            #file.close()

            todos = get_todos()

            for index, item in enumerate(todos):
                item = item.title().strip("\n")
                print(f"{index +1 } - {item}")
        except ValueError:
            print("Your command is not valid. ")
            continue

    elif user_action.startswith("complete"):
        try:
            try:
                number = int(user_action[9:])

                todos = get_todos()

                index = number - 1
                todo_to_remove = todos[index].title()
                todos.pop(index)

                write_todos("todos.txt", todos)

                print(f"You have removed {todo_to_remove} from the list.")
            except ValueError:
                print("You need to include the index number of the item you want.")
                continue

        except IndexError:
            print("There is no item with that number.")
            continue

    elif 'exit' in user_action:
        break
    else:
        print("Command is not valid!")



print("Bye!")

