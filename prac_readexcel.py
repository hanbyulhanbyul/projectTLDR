import pandas as pd
SCCchat = pd.read_csv(r'SCCchat.csv')
df = pd.DataFrame(SCCchat)

name = [1]
names = df[df.columns[name]]
msg = [2]
msgs = df[df.columns[msg]]
print(msgs)

# values = df.values
# date = df.index
# type = df.columns
# print(values)


# f = open("testfile3.txt", "w+")
# for i in range(1,11):
#    data = "This is line %d.\n" % i
#    f.write(data)
#    print(data)
# f.close()

# f=open("testfile3.txt", "a+")
# for i in range(2):
#    f.write("append line %d\n" % (i))
# f.close()

# f = open("testfile3.txt", "r")
# if f.mode == 'r':
#    contents = f.read()
#    print(contents)

# test_file = open("testfile3.txt", "r")
# print(test_file.read())
# tutor_file = open("test.txt", "r")
# print(tutor_file.read())
#
#
def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print (word_count (tutor_file.read()))

