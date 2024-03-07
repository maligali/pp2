import os

currentdic = os.getcwd()
all = os.listdir(currentdic)

print("Only directories: ")
dirs = [d for d in all if os.path.isdir(os.path.join(currentdic, d))]
print(', '.join(dirs))

print("Only files: ")
files = [f for f in all if os.path.isfile(os.path.join(currentdic, f))]
print(', '.join(files))

print("All directories and files: ")
print(', '.join(all))