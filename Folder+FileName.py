import os, shutil

#walks through files in a folder and appends the folder name to each file name

RootDir1 = r'ogPath'
TargetFolder = r'targetPath'
for root, dirs, files in os.walk((os.path.normpath(RootDir1)), topdown=False):
        for name in files:
            if name.endswith('.wav'):
                SourceFolder = os.path.join(root,name)
                shutil.copy2(SourceFolder, TargetFolder)