import glob

string = ""
for file in glob.glob('*[!ftpserver.py]*'):
    string = string+"\n-> "+file
print(string)