import subprocess

#filepath="path of the batch file"
filepath="C:/Users/Allison/Desktop/tester.bat"
p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)

stdout, stderr = p.communicate()
print p.returncode 
# 0 if success