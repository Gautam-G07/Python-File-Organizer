import os
import shutil

folder_path=r"C:\Users\Gautam G\OneDrive\Documents"
files=os.listdir(folder_path)
os.makedirs("Images", exist_ok=True)
os.makedirs("Pdfs", exist_ok=True)
os.makedirs("ppts", exist_ok=True)
os.makedirs("Text", exist_ok=True)
os.makedirs("Music", exist_ok=True)
for i in files:
    source = os.path.join(folder_path, i)
    if os.path.isfile(source):
        if i.endswith('.txt'):
            shutil.move(source, 'Text')
        elif i.endswith('.pdf'):    
            shutil.move(source, 'Pdfs')
    
        elif i.endswith('.pptx'):
            shutil.move(source, 'ppts')  
    
        elif i.endswith('.jpg') or i.endswith('.png'):
            shutil.move(source, 'Images')
        elif i.endswith('.mp3'):
            shutil.move(source, 'Music')