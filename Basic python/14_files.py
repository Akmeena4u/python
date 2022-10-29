
""" The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode

"""

lines_data = ['Shivam\n', 'Gaurav\n', 'Kite\n']

with open('data_folder/write_file.txt', 'a') as f:
	f.write('Anuj\n')
	f.writelines(lines_data)

























# with open('data_folder/data.txt') as f:
# 	# for line in f:
# 	# 	print(line)

# 	f.seek(20)
# 	print(f.read(10))

























# f = open('data_folder/data.txt', 'r')

# for line in f:

# 	print(line)


# a = []
# a[4]

# # print(f.readline())
# # print(f.readline())
# # print(f.readline())

# f.close()
