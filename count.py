import os 
import pathlib


# config options
ext = 'js'
ignore_file = './src-ig'
readmeFileName = "./Readme.md"

fReadme = open(readmeFileName, "w")
def countLines(path):
    count = 0
    for f in os.listdir(path):
        fPath = path + "/" + f
        file_ext = pathlib.Path(fPath).suffix
        if (os.path.isfile(fPath) and file_ext in ['.' + ext]):
            fCount = len(open(fPath).readlines())
            fReadme.write(str(f) + "(" + str(fCount) + "), ")
            count = count + fCount
    fReadme.write("\nS(" + str(count) + ")\n")
    return count


total = 0
fReadme.write("## Categories")
for f in os.listdir(ignore_file):
    pathFull = ignore_file + "/" + f
    fReadme.write("\n## " + str(f).upper() + "\n")
    if (os.path.isdir(pathFull)):
        total = total + countLines(pathFull)

print(total)


fReadme.write("\n# Total \n" + str(total))