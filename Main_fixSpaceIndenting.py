import os
import pathlib


def pad(spaces:int):
	s = ""

	for i in range(0,spaces):
		s = s + " "

	return s


def cleanline(line:str, spacespertab = 4):
	i = 0
	while line[i] == ' ':
		i=i+1
	
	leadingspace = line[:i].replace(pad(spacespertab),"\t")

	return leadingspace + line[i:]
	

teststrs = ["    johnjohn",
"        johnjohn",
"     john"]

res = []

for test in teststrs:
	res.append(cleanline(test))


numberspacespertab = 4

# the project directory
projectdir = pathlib.Path(__file__).parent.parent

for dir in os.walk(projectdir):

	for file in dir[2]:
		
		if file.endswith('.py'):
			# rename the python file

			orifilename= os.path.join(dir[0],file)
			tempfilename = os.path.join(dir[0],file+'.temp')

			os.rename(orifilename, tempfilename)

			if not os.path.exists(tempfilename):
				print("Issue. temporary file for "+file+" doesn't exist")
				exit(2)

			fin = open(tempfilename,"r")
			fout = open(orifilename,"w")

			line = fin.readline()

			while line:
				fout.write(cleanline(line))
				line = fin.readline()
			
			fin.close()
			fout.flush()
			fout.close()

			os.remove(tempfilename)

