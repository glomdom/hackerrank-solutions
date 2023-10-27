#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'possibleChanges' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY usernames as parameter.
#

def possibleChanges(usernames):
    result = []

    for user in usernames:
        if len(user) < 1:
            result.append("NO")
        
        for i in range(len(user) - 1):
            if user[i] > user[i + 1]:
                result.append("YES")

                break
        else:
            result.append("NO")

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    usernames_count = int(input().strip())

    usernames = []

    for _ in range(usernames_count):
        usernames_item = input()
        usernames.append(usernames_item)

    result = possibleChanges(usernames)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
