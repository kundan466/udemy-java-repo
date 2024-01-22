def get_nr_items(user_input):
    # Split the user_input string by comma and store the resulting items in the 'items' list
    items = user_input.split(',')
    # Return the length of the 'items' list
    return len(items)