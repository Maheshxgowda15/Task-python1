# Program to demonstrate operations on a list, dictionary, and set

# Working with a list
def list_operations():
    # Create a list
    my_list = [1, 2, 3, 4, 5]
    print("Initial list:", my_list)

    # Adding elements
    my_list.append(6)  # Add to the end
    print("List after appending 6:", my_list)

    my_list.insert(0, 0)  # Insert at the beginning
    print("List after inserting 0 at the beginning:", my_list)

    # Removing elements
    my_list.remove(3)  # Remove by value
    print("List after removing 3:", my_list)

    # Modifying elements
    my_list[1] = 20  # Change the value at index 1
    print("List after modifying index 1 to 20:", my_list)

    return my_list

# Working with a dictionary
def dictionary_operations():
    # Create a dictionary
    my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
    print("Initial dictionary:", my_dict)

    # Adding key-value pairs
    my_dict['email'] = 'alice@example.com'
    print("Dictionary after adding email:", my_dict)

    # Removing key-value pairs
    del my_dict['age']  # Remove by key
    print("Dictionary after removing age:", my_dict)

    # Modifying values
    my_dict['city'] = 'San Francisco'  # Change the value for 'city'
    print("Dictionary after modifying city to San Francisco:", my_dict)

    return my_dict

# Working with a set
def set_operations():
    # Create a set
    my_set = {1, 2, 3, 4, 5}
    print("Initial set:", my_set)

    # Adding elements
    my_set.add(6)  # Add a single element
    print("Set after adding 6:", my_set)

    my_set.update([7, 8])  # Add multiple elements
    print("Set after adding 7 and 8:", my_set)

    # Removing elements
    my_set.discard(3)  # Remove by value (does not raise an error if not found)
    print("Set after discarding 3:", my_set)

    # Attempting to remove an element not in the set using remove (will raise an error)
    try:
        my_set.remove(10)  # This will raise a KeyError if 10 is not present
    except KeyError:
        print("Attempted to remove 10, but it is not in the set.")

    # Modifying (sets are unordered, so we just show the current elements)
    print("Final set elements:", my_set)

    return my_set

# Main function to execute operations
def main():
    print("List Operations:")
    list_operations()
    
    print("\nDictionary Operations:")
    dictionary_operations()
    
    print("\nSet Operations:")
    set_operations()

# Entry point of the program
if __name__ == "__main__":
    main()
