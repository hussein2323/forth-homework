def add_element(list_00, element):
    list_00.append(element)
    return list_00

def delete_element(list_00, index):
    if 0 <= index < len(list_00):
        list_00.pop(index)
    return list_00

def update_element(list_00, index, new_value):
    if 0 <= index < len(list_00):
        list_00[index] = new_value
    return list_00