
with open("rosalind_ba9j.txt", "r") as file:
    # Read the entire file content
    bwt = file.read()[:-1]

def BWT(str):
    # append end of character $ to str
    # create a table whose rows are circular shifts of str_w_eof
    # sort rows of table alphabetically

    # bwt -> last letter of alphabetically sorted column
    return 0