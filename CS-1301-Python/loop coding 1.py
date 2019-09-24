def countts(string):
    count = 0
    for letter in string:
        if letter == "t" or letter == "T":
            count += 1
        else:
            continue
    return count

print(countts("TTTTTTttttTTTT"))
