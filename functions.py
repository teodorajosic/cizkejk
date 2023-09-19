import tkinter as tk
from tkinter import filedialog as fd

def openFile(filePath,paper,file_path):
    try:
        file_path[0]=filePath
        with open(filePath, 'r') as file:
            fileContent = file.read()
        
        paragraphs=fileContent.split('\n')
        showText(paper, paragraphs)
        return fileContent

    except FileNotFoundError:
        return f"File '{filePath}' not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def getContent (content, paper, file_path):
    content_help = content
    content_help[0] = openFile(fd.askopenfilename(), paper,file_path)
    content = content_help

def save_file(current_file_path, paper):   
    if current_file_path[0]:
        content = paper.get("1.0", tk.END).split("\n")
        with open(current_file_path[0], 'w') as file:
            for paragraph in content:
                file.write(paragraph)
                file.write('\n')
    else:
        save_file_as(paper)

def save_file_as(current_file_path, paper):
    file_path = fd.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    current_file_path[0]=file_path
    content=paper.get("1.0", tk.END).split("\n")
    with open(file_path, 'w') as file:
        for paragraph in content:
            file.write(paragraph)
            file.write('\n')

def formatText(paper):
    text = paper.get("1.0", "end-1c")
    paragraphs = text.split("\n")
    return paragraphs

def showText(paper: tk.Text, paragraphs: list):
    paper.delete("1.0", tk.END)
    for paragraph in paragraphs:
        paper.insert(tk.END, paragraph)
        paper.insert(tk.END, "\n")
    
def create_new_file(current_file_path, paper):    
    paper.delete("1.0", tk.END)  
    current_file_path = ["a"]
    save_file_as() 