import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')

# create a list of filenames
list_of_files = glob.glob(pattern)

# loop through list of files to get each file size
for i in list_of_files:
   print(os.path.getsize(i))

print("\n")

# print only non zero files
for i in list_of_files:
    size = os.path.getsize(i)
    if size !=0:
        print(i)

# remove directory names from files
for i in list_of_files:
    print(os.path.basename(i))

