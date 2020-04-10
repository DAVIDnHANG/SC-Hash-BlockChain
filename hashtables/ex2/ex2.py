#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # algo For
    # Base Case: find the starting case None, such that ///  (None=i_0, destination=j_0).
    # case_1: for next we find i_1 such that i_1 = j_0, ///  (i_1,     j_1)
    # so that means,                        i_2 = j_1  /// (i_2,     j_2)
    # hash each ticket st  hash(key) = source, hash(value) = destination.
    #base case: at index=0, we look for source = NONE,
    # When we call hash_table_retrieve on (key)=None, it returns the hash(value) = destination=j_0,
    #then we assign it to route[index=0] = destination=j_0 at index=0,
    #now on index=1, we can use hash_table_retrieve(hashtable ,route[i=0]) = route[index=1] to call destination=j_1.

    hashtable = HashTable(length)
    route = [None] * length

    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    for index in range(length):
        if index == 0:
            route[index] = hash_table_retrieve(hashtable, "NONE")
        else:
            previousValue = route[index-1]
            route[index] = hash_table_retrieve(hashtable, previousValue)
    return route[0:-1]

