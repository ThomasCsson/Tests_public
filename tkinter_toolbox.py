import tkinter as tk
from tkinter import ttk
from rdkit import Chem
from rdkit.Chem import Draw
import time



starttime = time.time()
#window
window = tk.Tk()
window.title('ToolKit')
window.geometry('400x200')

#stuff
input_label = ttk.Label(master = window, text = 'Input SMILES: ')
input_label.pack()

#button functions

#mol converter
def button1_command():
    smi = entry.get()
    mol = Chem.MolFromSmiles(smi)
    output_string.set(mol)

#insaturation
def button2_command():
    smi = entry.get()
    molint = Chem.MolFromSmiles(smi)
    mol = Chem.AddHs(molint)
    C,N,HX, = 0,0,0
    halogens_hydrogen = ['F','Cl','Br','I','At','H']
    for atom in mol.GetAtoms():
            atom_sym = atom.GetSymbol()
            if atom_sym == 'C':
                  C = C+1
            elif atom_sym == 'N':
                  N = N + 1
            elif atom_sym in halogens_hydrogen:
                  HX = HX + 1
    insaturation = C + 1 + (N-HX)/2
    output_string.set(f'The insaturation of the input molecule is: {insaturation}')

#molar mass
def button3_command():
    smi = entry.get()
    molint = Chem.MolFromSmiles(smi)
    mol = Chem.AddHs(molint)
    mm = 0
    for atom in mol.GetAtoms():
        mm = mm + atom.GetMass()
    mm_rounded = ((1000*mm)//1)/1000
    molarmass = mm_rounded
    output_string.set(f'The molecular mass of the input molecule is of {molarmass} [g/mol]')

#secret
def button4_command():
    pass

#image generator
def button5_command():
    smi = entry.get()
    mol = Chem.MolFromSmiles(smi)
    img = Draw.MolToImage(mol)
    img.show()
    output_string.set(f'The molecule is shown in external window')

#bond types
def button6_command():
    smi = entry.get()
    bonds = []
    x = 0
    mol = Chem.MolFromSmiles(smi)
    for bond in mol.GetBonds():
        if bonds.count(bond) == 0:
            bonds.append(bond.GetBondType())
    for i in range (0,len(bonds)):
        for i in bonds:
            if bonds.count(i)!=1:
                bonds.remove(i)
    output = ('The bonds types in the given molecule are: ', bonds)
    output_string.set(output)

#image w/ Hs
def button7_command():
    smi = entry.get()
    mol = Chem.MolFromSmiles(smi)
    molHs = Chem.AddHs(mol)
    img = Draw.MolToImage(molHs)
    img.show()
    output_string.set(f'The molecule is shown in external window')



#window management (button & frames)

#frame 1

input_frame1 = ttk.Frame(master = window)

entry = ttk.Entry(master = input_frame1)
toggle = ttk.Checkbutton(master = input_frame1)
#frame 2

input_frame2 = ttk.Frame(master = window)
button1 = ttk.Button(master = input_frame2,text = 'SMILE to Mol', command = button1_command)
button2 = ttk.Button(master = input_frame2, text = 'Insaturation',command = button2_command)

entry.pack(side = 'left')
toggle.pack()
button1.pack(side = 'left')
button2.pack(side = 'right')

#frame 3

input_frame3 = ttk.Frame(master = window)

button3 = ttk.Button(master = input_frame3,text = 'Molar mass',command = button3_command)
button4 = ttk.Button(master = input_frame3,text = 'Secret function',command = button4_command)

button3.pack(side = 'left')
button4.pack(side = 'left')

#frame 4

input_frame4 = ttk.Frame(master = window)

button5 = ttk.Button(master = input_frame4, text = 'Image generator', command = button5_command)
button5.pack(side = 'left')
button6 = ttk.Button(master = input_frame4, text = 'Bond types',command = button6_command)
button6.pack(side = 'left')

#frame 3

input_frame5 = ttk.Frame(master = window)

button7 = ttk.Button (master = input_frame5, text = 'Image generator with hydrogens',command = button7_command)
button7.pack()


#Packing of frames

input_frame1.pack()
input_frame2.pack()
input_frame3.pack()
input_frame4.pack()
input_frame5.pack()

#output management
output_frame = ttk.Frame(master = window)
output_string = tk.StringVar()
output_label = ttk.Label(master = output_frame, text = 'Output',textvariable=output_string)
output_label.pack()
output_frame.pack()


endtime = time.time()
runtime = endtime-starttime
print(f'Runtime: {runtime}s')
window.mainloop() 