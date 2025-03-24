import os
count  = 0
# Get all files and folders from the given path
allfiles = os.walk(r"c:\classroom\feb13\demo")
for (dirname , directories , files) in allfiles:
    # print directory name
    print("Directory : ", dirname)
    print("=============" + "=" * len(dirname))
    # print files in that directory
    for file in files:
        if file.endswith('.py'):
            count += 1

        print(file)


print("Count = ", count)
