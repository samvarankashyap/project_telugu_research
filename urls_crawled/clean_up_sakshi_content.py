from os import listdir
from os.path import isfile, join
mypath = "./sakshi_content/"
outpath = "./cleaned_sakshi_content/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(len(onlyfiles))


# 1st pass cleans all the empty lines
for filename in onlyfiles:
    print(filename)
    with open(mypath+filename, "r") as infile, open(outpath+filename, 'wb') as outfile:
        for line in infile:
            if "Read latest" in line: continue
            if not line.strip(): continue  # skip the empty line
            if "You are here" in line:
                outfile.write(line.lstrip("You are here").encode('utf-8'))
            else:
                outfile.write(line.encode('utf-8'))  # non-empty line. Write it to output
