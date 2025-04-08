# Problem #2: Index Game

def access_element(my_list, index):
    # Accessing an element at a specific index
    if index < 0 or index >= len(my_list):
        return "Index out of range."
    return my_list[index]

def modify_element(my_list, index, new_value):
    # Modifying an element at a specific index
    if index < 0 or index >= len(my_list):
        return "Index out of range."
    my_list[index] = new_value
    return my_list

def slice_list(my_list, start, end):
    # Slicing the list from start to end index (end is exclusive)
    if start < 0 or end > len(my_list) or start > end:
        return "Invalid slice indices."
    return my_list[start:end]

def main():
    # Initialize a list with mixed elements (numbers and strings)
    game_list = [10, 'apple', 25, 'banana', 40, 'orange']

    while True:
        print("\nCurrent list:", game_list)
        print("Select an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            index = int(input("Enter the index to access: "))
            print("Accessed element:", access_element(game_list, index))
        
        elif choice == '2':
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            print("Updated list:", modify_element(game_list, index, new_value))
        
        elif choice == '3':
            start = int(input("Enter the start index for slicing: "))
            end = int(input("Enter the end index for slicing: "))
            print("Sliced list:", slice_list(game_list, start, end))
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Call the main function to run the game
if __name__ == "__main__":
    main()
