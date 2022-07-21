f = open('python.jpg',"wb+") # wb+ are Replace and check like rb+ ab+ xb rb wb ab this is all are binary mode
print('File Name: ',f.name)
print('File Mode: ',f.mode)
print('File Redable: ',f.readable())
print('File Writable: ',f.writable())
print('File Closed: ',f.closed)
f.close()
print('File Closed: ',f.closed)