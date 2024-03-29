import os 
import pathlib

# config options
extensions = ['.js', '.ts', '.tsx']
ignore_file = './src-ig'
src_file = './src'
readmeFileName = "./Readme.md"
machineName = 'ln.house.txt'

fReadme = open(readmeFileName, "w")
def countLines(path):
    count = 0
    for f in os.listdir(path):
        fPath = path + "/" + f
        file_ext = pathlib.Path(fPath).suffix
        if (os.path.isfile(fPath) and file_ext in extensions):
            fCount = len(open(fPath).readlines())
            fReadme.write(str(f) + "(" + str(fCount) + "), ")
            count = count + fCount
    fReadme.write("\nS(" + str(count) + ")\n")
    return count


total = 0

fReadme.write("## Categories")

for x_file in [ignore_file]:
    total = total + countLines(x_file)
    for f in os.listdir(x_file):
        pathFull = x_file + "/" + f
        fReadme.write("\n## " + str(f).upper() + "\n")
        if (os.path.isdir(pathFull)):
            total = total + countLines(pathFull)


fMachine = open(machineName, "w")
fMachine.write(str(total))


for x_file in [src_file]:
    total = total + countLines(x_file)
    for f in os.listdir(x_file):
        pathFull = x_file + "/" + f
        fReadme.write("\n## " + str(f).upper() + "\n")
        if (os.path.isdir(pathFull)):
            total = total + countLines(pathFull)


for cfile in os.listdir("."):
    if cfile.endswith(".house.txt") and not cfile.endswith(machineName):
        print(os.path.join("/", cfile))
        with open(cfile, "r") as txt_file:
            otherTotal = int(txt_file.readlines()[0])
            fReadme.write("\n# Other Total \n" + str(otherTotal))
            total = total + otherTotal


goal = 3000

print("Goal: {}".format(goal))

print("Total: {}".format(total))

print(f"To reach the goal: {goal - total}")

fReadme.write("\n# Total \n" + str(total))
