#Mohamed walid mohamed mohamed
#Section 3

from tkinter import *
import webbrowser

SITES = [
    ("Facebook", "https://www.facebook.com", "blue"),         
    ("GeeksforGeeks", "https://www.geeksforgeeks.org", "darkgreen"), 
    ("مكتبة نور", "https://www.noor-book.com", "purple"),       
    ("Online Compiler", "https://www.programiz.com/online-compiler/", "green"), 
    ("Wikipedia", "https://www.wikipedia.org", "lightgray"),  
    ("GitHub", "https://github.com", "black"),               
]

def open_site(link, name):
    root.title(f'Opening: {name}...')
    webbrowser.open(link)

root = Tk()
root.title('Favorite website player')
root.geometry('350x450') 

for name, link, color in SITES:
    
    text_color = 'white' if color in ["blue", "darkgreen", "purple", "black"] else 'black'
    
    Button(root, 
           text=name, 
           command=lambda l=link, n=name: open_site(l, n),
           width=35, 
           bg=color,        
           fg=text_color,   
           font=('Arial', 10, 'bold'),
           pady=10
    ).pack(pady=7, padx=20) 

root.mainloop()