import re
fail = open("aadressid.txt")
for read in fail:
    read = fail.readlines()
    nimed = re.search("^~(.+) /$",read)
print(nimed.group(1))
fail.close()