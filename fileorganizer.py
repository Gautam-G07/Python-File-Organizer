import os
import shutil

folder_path=r"C:\Users\Gautam G\OneDrive\Documents"
files=os.listdir(folder_path)
os.makedirs(os.path.join(folder_path, "Images"), exist_ok=True)
os.makedirs(os.path.join(folder_path, "Pdfs"), exist_ok=True)
os.makedirs(os.path.join(folder_path, "ppts"), exist_ok=True)
os.makedirs(os.path.join(folder_path, "Text"), exist_ok=True)
os.makedirs(os.path.join(folder_path, "Music"), exist_ok=True)

for i in files:
    source = os.path.join(folder_path, i)
    if os.path.isfile(source):
        if i.endswith('.txt'):
            shutil.move(source,os.path.join(folder_path, 'Text'))
        elif i.endswith('.pdf'):    
            shutil.move(source, os.path.join(folder_path, 'Pdfs'))
    
        elif i.endswith('.pptx'):
            shutil.move(source, os.path.join(folder_path, 'ppts'))  
    
        elif i.endswith('.jpg') or i.endswith('.png'):
            shutil.move(source, os.path.join(folder_path, 'Images'))
        elif i.endswith('.mp3'):
            shutil.move(source, os.path.join(folder_path, 'Music'))