def format_log(line):
    return "{0}{1}{2}".format(line[0][0:7],"."*(80-7-len(line[-1])), line[-1])

input_file = open("input.txt")
output_file = open("output.txt", "w")

for line in input_file:
    if line[-1] == "\n":
        line = line[0:len(line)-1]
    line = line.split("\t")
    line = format_log(line)
    output_file.write(line+"\n")
