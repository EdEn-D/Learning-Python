import os

os.chdir(r'C:/Users/Eden/Desktop') #changes current working directiry to desktop
newfolder = r'C:\Users\Eden\Desktop\New folder'
if not os.path.exists(newfolder):
    #os.makedirs(newfolder)
    os.makedirs('New')
    os.makedirs('New/cunt') #this will make a folder inside new even though it exists