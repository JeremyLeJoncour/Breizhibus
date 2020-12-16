import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
config = {
      'user': 'root',
      'password': 'root',
      'host': 'localhost',
      'port': '8081',
      'database': 'breizhibus',
      'raise_on_warnings': True,
    }

#Création du Cursor
link = mysql.connector.connect(**config)
cursor = link.cursor()

#La fenêtre Tk s'appelle window
window = Tk()

bgtkinter = '#6335ff'

#Personnalisation de la fenêtre
window.title("Projet Breizhibus")
window.geometry("1360x800")
window.config(bg = bgtkinter)
window.minsize(350, 450)

#Images
logo = Image.open('titre.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(bd = 0, image=logo)
logo_label.image= logo
logo_label.pack()

#Menu
menu_frame = tk.Frame(window, height = 100, width = 500, bg = bgtkinter)
menu_frame.pack(pady=30)

menu = ['Afficher les lignes']
titre_menu = StringVar()
titre_menu.set("Menu")

logo2 = Image.open('image2.png')
logo2 = ImageTk.PhotoImage(logo2)
logo2_label = tk.Label(menu_frame, bd = 0, image=logo2)
logo2_label.image = logo2
logo2_label.pack(side = LEFT, padx = 10)

opt = tk.OptionMenu(menu_frame, titre_menu, *menu)
opt.config(height = 2, width = 24, font=('Consolas', 15), bg = bgtkinter, fg="white", activebackground = bgtkinter, activeforeground="white", highlightthickness=0)
opt.pack(side = LEFT, padx = 60)

#Présentation des boutons lignes
line_arret_frame = tk.Frame(window, bg = bgtkinter)
line_arret_frame.pack(pady = 10)

line_frame = tk.Frame(line_arret_frame, bg = bgtkinter)
line_frame.pack(side = LEFT, pady = 30)


def get_arrets(btn_line):
    arret_list = []
    
    cursor.execute(f"SELECT nom, adresse FROM arrets JOIN arrets_lignes ON arrets.id_arrets = arrets_lignes.id_arret JOIN lignes ON arrets_lignes.id_ligne=lignes.id_lignes WHERE nom_ligne = '{btn_line}'")
    rows_arrets = cursor.fetchall()
    
    for arret in rows_arrets : 
        arret_list.append(arret)
    return arret_list  

def affiche_arret(line):
    arret_line = get_arrets(line)
    
    for widget in arret_frame.winfo_children():
        widget.destroy()
    
    for items in arret_line:
        arret_label0 = tk.Label(arret_frame, text= items[0]+',  '+items[1], font=('Consolas', 15), bg = bgtkinter, fg = 'white')
        arret_label0.pack(padx = 10, pady = 10, ipadx = 15)

def btn_lines():
    for widget in line_frame.winfo_children():
        widget.destroy()

    cursor.execute("SELECT * FROM lignes")
    rows_lignes = cursor.fetchall()
    list_color = ['#cd003e', '#22ff4e', '#3c9bff', '#303030']
    for ligne, i in  zip(rows_lignes, list_color)  :
        btn_lines = Button(line_frame, text=f"{ligne[1]}", font=('Consolas', 15), height = 2, width =12, bg =f'{i}', fg='white', command = lambda x = ligne[1]: affiche_arret(x))
        btn_lines.pack(pady = 7)
    return btn_lines

def callback(*args):  
    btn_lines()
    
titre_menu.trace("w", callback)
arret_frame = tk.Frame(line_arret_frame, bg = bgtkinter)
arret_frame.pack(side = LEFT, padx = 10)

#Afficher la fenêtre
window.mainloop()