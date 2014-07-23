'''
Created on Jul 15, 2014

@author: vpsmith
'''
from tkinter import *
from tkinter import ttk


class ScrollBoxList(ttk.Frame):
    def __init__(self, master):
        Frame.__init__(self, master)   
        
        self.runButton = Button(self, text="Execute", command=self.run)
        self.cancelButton = Button(self, text="Cancel", command=self.quit)
        self.listLabels= ["Accession Id", "Ensembl Id", "Mutation Index", "Amino Acid Change"]
        
        self.accessionId= StringVar()
        self.accession= StringVar()
        self.protein=StringVar()
        self.proteinSeq=StringVar()
        self.listVariables=[ self.accessionId, self.proteinSeq, self.accession, self.protein]
        self.scrollbar = ttk.Scrollbar(self, orient=VERTICAL)
        self.listbox = Listbox(self, height=4, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        self.labelName=StringVar()
        self.labelIndex=IntVar()
        self.entry= StringVar()
        
        self.initUI()
    def data(self):
        
        for i in self.listLabels:
            self.listbox.insert(END, i)
           
    def onSelect(self, val):
        sender = val.widget
        idx = sender.curselection()
        self.labelIndex.set(idx[0])
        print(idx)
        value = sender.get(idx) 
        self.labelName.set(value)
        print(self.entry.get())
        self.listVariables.__setitem__(int(idx[0]), self.entry.get())
        print(value)  
        print(idx[0])
    def run(self):
        print(str(self.listVariables))       
    def initUI(self):
        
        

        
        #Label(self, text="Input Sheet Name:").grid(row=4, column=1)
        #Label(self, text="Accession ID:").grid(row=3, column=3, sticky=E)
      
        #packs both of the cancel and run buttons
        
        self.data()
        self.listbox.bind("<<ListboxSelect>>", self.onSelect) 
        self.listbox.place(x=20, y=20)
        self.scrollbar.place(x=0, y=35)
        
        #self.labelValue.grid(row=3,column=0)
        
        #the input sheets and files with text edit and labels
        
        #self.labelName.grid(row=2,column=0)
        #self.listbox.grid(row=4, column=4, sticky=S)
       
        #self.labelName.pack(side= RIGHT)
        
        #self.labelValue.pack(side=RIGHT)
        self.label = Label(self, text=0, textvariable=self.labelName)        
        self.label.place(x=210, y=20)
        ttk.Entry(self, textvariable= self.entry).place(x=210, y=60)
        self.runButton.place(x=210, y=200)
        self.pack(fill=BOTH, expand=1, padx=5, pady=5)
       

def main():
    #Setup Tk()
    window = Tk()
    window.geometry("400x250+300+300")
    window.title("Mutation Finder")
    ex=ScrollBoxList(window)
    window.mainloop()
if __name__ == '__main__':
    main()  



    
 
       
         
