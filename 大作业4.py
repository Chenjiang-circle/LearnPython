file1 = open("test1.py", 'r')
file2 = open("exam2_1812050146_new.py", 'w')

i = 0
for line in file1:
    i += 1
    line = line.replace("\n", "")
    line = "{0:<50}#{1}\n".format(line, i)
    file2.write(line)
file1.close()
file2.close()
