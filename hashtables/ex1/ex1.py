#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    # check if length is one or less, return None.
    # insert the first index,value into the hash_table.
    # second loop:
    # then do math difference=limit-Value at Index.
    # use the difference to retrieve the hash table.
    ht = HashTable(16)
    if length <= 1:
        return None
    for index, value in enumerate(weights):  # enumerate is to call index, and value of array
        difference = limit - value
        Hashretrieve = hash_table_retrieve(ht, difference)
        if Hashretrieve is None:
            hash_table_insert(ht, value, index)
        else:
            if index >= Hashretrieve:
                return (index, Hashretrieve)
            else:
                return (Hashretrieve, index)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
