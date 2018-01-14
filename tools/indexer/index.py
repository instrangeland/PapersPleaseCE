# Input.txt must be one (1) line, and have data in a list sorted by commas with a comma at the start and end
# EXAMPLE
# ,Jacob Wysko,Julian Lachniet,
in_file = open("input.txt","r")
index = []
string = in_file.read()
for x in range(len(string)):
	if string[x - 1:x] == ",":
		index.append(x)
in_file.close()
out_file = open("output.txt","w")
out_file.write(str(index))
out_file.close()
