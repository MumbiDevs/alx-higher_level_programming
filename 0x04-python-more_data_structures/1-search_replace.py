def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another in a new list.

    Args:
        my_list (list): The initial list.
        search: The element to replace in the list.
        replace: The new element.

    Returns:
        list: A new list with all occurrences of 'search' replaced by 'replace'.

    Description:
        This function creates a new list based on the input 'my_list' where all occurrences
        of the element 'search' are replaced by the element 'replace'. The input 'my_list'
        remains unmodified.
    """
    # Create a new list to store the modified elements
    new_list = []

    # Iterate over each element in the input list
    for element in my_list:
        # If the current element matches the 'search' element, replace it with 'replace'
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)

    # Return the new list
    return new_list

# Example usage:
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    new_list = search_replace(my_list, 2, 89)
    print(new_list)
    print(my_list)
