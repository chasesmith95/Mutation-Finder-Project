'''
Created on Jun 30, 2014

@author: vpsmith
'''
from tkinter import *
from tkinter import ttk
from MutationFinder import Excel,Fasta
import glob

                     
class ExcelInput(ttk.Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)   
        self.runButton = Button(self, text="Execute", command=self.runExcelInput)
        self.cancelButton = Button(self, text="Cancel", command=self.quit)
        self.output_sheetStr= StringVar()
        self.input_fileStr=StringVar()
        self.output_folderStr=StringVar()
        self.input_fileStr= StringVar()
        self.input_sheetStr= StringVar()
        self.input_listStr= StringVar()
        self.ensembl_var=IntVar()
        self.ensembl= ttk.Checkbutton(self, text="Ensembl", variable=self.ensembl_var, command= self.ensembl_var.get())
        self.excel= None 
        self.output_sheet = ttk.Entry(self)
        self.mutation_sequence = ttk.Entry(self, width=3)
        self.mutSYSEQ = ttk.Entry(self,  width=3)
        self.mutSYStrength = ttk.Entry(self, width=3)
        self.regular_sequence = ttk.Entry(self,width=3)
        self.regSYSEQ = ttk.Entry(self, width=3)
        self.regSYStrength = ttk.Entry(self, width=3)
        self.protein_sequence = ttk.Entry(self, width=3)
        self.input_file = ttk.Entry(self)
        self.input_sheet = ttk.Entry(self)
        self.mutIndex_col = ttk.Entry(self, width=3)
        self.output_file = ttk.Entry(self)
        self.accession_col = ttk.Entry(self, width=3)
        self.ensembl_col=StringVar()
        self.aChange_col = ttk.Entry(self, width=3)
        self.amerLength_col = ttk.Entry(self, width=3)
        self.geneType_col = ttk.Entry(self, width=7)
        
        
        
        self.mutIndex_col = StringVar()
        self.mutation_sequence = StringVar()
        self.mutSYSEQ = StringVar()
        self.mutSYStrength = StringVar()
        self.regular_sequence = StringVar()
        self.regSYSEQ = StringVar()
        self.regSYStrength = StringVar()
        self.protein_sequence = StringVar()
        
        self.input_folder = StringVar()
        self.input_sheet = StringVar()
        self.input_file= StringVar()
        self.output_sheet = StringVar()
        self.output_file = StringVar()
        self.accession_col = StringVar()
        self.aChange_col = StringVar()
        self.amerLength = StringVar()
        self.geneType_col = StringVar()
        self.numSYReturns= StringVar()
        self.amerLengthList=["octamers (8 aa)","nonamers (9 aa)","decamers (10 aa)",  "endecamers (11 aa)", "15 - mers (15 aa) for MHC Type II only"]
        self.amerLengthDict= {"octamers (8 aa)": 8, "nonamers (9 aa)": 9 ,"decamers (10 aa)": 10,  "endecamers (11 aa)": 11, "15 - mers (15 aa) for MHC Type II only": 15}
        self.immuneTypeList=['H2-Ad', 'H2-Ak', 'H2-Db', 'H2-Ed', 'H2-Ek', 'H2-Kb', 'H2-Kd', 'H2-Kk', 'H2-Ld', 'HLA-A*01', 'HLA-A*02:01', 'HLA-A*03', 'HLA-A*11:01', 'HLA-A*24:02', 'HLA-A*26', 'HLA-A*68:01', 'HLA-B*07:02', 'HLA-B*08', 'HLA-B*13', 'HLA-B*14:02', 'HLA-B*15:01 (B62)', 'HLA-B*15:10', 'HLA-B*15:16', 'HLA-B*18', 'HLA-B*27:05', 'HLA-B*27:09', 'HLA-B*35:01', 'HLA-B*37', 'HLA-B*38:01', 'HLA-B*39:01', 'HLA-B*39:02', 'HLA-B*40:01 (B60)', 'HLA-B*41:01', 'HLA-B*44:02', 'HLA-B*45:01', 'HLA-B*47:01', 'HLA-B*49:01', 'HLA-B*50:01', 'HLA-B*51:01', 'HLA-B*53:01', 'HLA-B*57:01', 'HLA-B*58:02', 'HLA-DRB1*0101', 'HLA-DRB1*0301 (DR17)', 'HLA-DRB1*0401 (DR4Dw4)', 'HLA-DRB1*0701', 'HLA-DRB1*1101', 'HLA-DRB1*1501 (DR2b)', 'RT1.Al']
        self.listFileVariables=[self.input_folder, self.input_file, self.input_sheet, self.output_file, self.output_sheet,  self.amerLength_col, self.geneType_col, self.numSYReturns] 
        self.listFileLabels= ["Input Folder", "Input File", "Input Sheet", "Output File", "Output Sheet", "Amer Length", "Immune Type", "Returns per Mutation"]
        
        self.listVariables=[self.accession_col,self.ensembl_col, self.mutIndex_col,self.aChange_col, self.mutation_sequence, self.regular_sequence, self.mutSYSEQ, self.regSYSEQ, self.mutSYStrength, self.regSYStrength, self.protein_sequence]
        self.listLabels=["*Accession Id", "*Ensembl Id", "*Mutation Index", "*Amino Change", "Mutation Sequence", "Regular Sequence", "Mutation SY Sequence", "Regular SY Sequence", "Mutation SY Strength", "Regular SY Strength", "Protein Sequence"]
        self.runButton.pack(side=RIGHT, padx=5, pady=5, anchor=S)
        self.cancelButton.pack(side=BOTTOM, padx=5, pady=5, anchor=SE)
        self.ensembl.pack(side=BOTTOM, padx=5, pady=5, anchor=E)
        self.initUIListBoxExternals()
        self.initUIListBox()
        
       
    def initUI(self):
        
       
        #self.parent.title("Mutation Finder: Excel Format")
        self.columnconfigure(0, pad=10)
        self.columnconfigure(1, pad=10)
        self.columnconfigure(2, pad=10)
        self.columnconfigure(3, pad=10)
        self.columnconfigure(4, pad=10)
        self.rowconfigure(0, pad=20)
        self.rowconfigure(1, pad=20)
        self.rowconfigure(2, pad=20)
        self.rowconfigure(3, pad=20)
        self.rowconfigure(4, pad=20)
        self.rowconfigure(5, pad=10)
        self.rowconfigure(6, pad=10)
        self.rowconfigure(7, pad=10)
        self.rowconfigure(8, pad=10)
        self.rowconfigure(9, pad=10)
        self.rowconfigure(10, pad=10)
        self.rowconfigure(11, pad=10)
        self.rowconfigure(12, pad=10)
        
       
        Label(self, text="Input File Name:").grid(row=2, column=1)
        Label(self, text="Input Sheet Name:").grid(row=3, column=1)
        
        
        Label(self, text="Accession ID:").grid(row=2, column=3)
        Label(self, text="Mutation Index:").grid(row=3, column=3)
        Label(self, text="Amino Acid Change:").grid(row=4, column=3)
        Label(self, text="Amer Length:").grid(row=4, column=1)
        Label(self, text="Gene Type:").grid(row=5, column=3)
        Label(self, text="INPUT LOCATIONS: ").grid(row=1, column=2)
        Label(self, text="OUTPUT LOCATIONS: ").grid(row=5, column=2)
        Label(self, text="Mutation Sequence:").grid(row=7, column=1)
        Label(self, text="Mutation SYPFEITHI:").grid(row=8, column=1)
        Label(self, text="Mutation SYPFEITHI Strength:").grid(row=9, column=1)
        
        Label(self, text="Regular Sequence:").grid(row=7, column=3)
        Label(self, text="Regular SYPFEITHI:").grid(row=8, column=3)
        Label(self, text="Regular SYPFEITHI Strength:").grid(row=9, column=3)
        Label(self, text="Output Sheet Name:").grid(row=6, column=1)
        Label(self, text="Output File Name:").grid(row=11, column=1)
        Label(self, text="Protein Sequence:").grid(row=6, column=3)
        
        self.input_file.grid(row=2, column=2)
        self.input_sheet.grid(row=3, column=2)
       
        
        self.accession_col.grid(row=2, column=4, sticky=W)
        self.mutIndex_col.grid(row=3, column=4, sticky=W)
        self.aChange_col.grid(row=4, column=4, sticky=W)
        self.amerLength_col.grid(row=4, column=2, sticky=W)
        self.geneType_col.grid(row=5, column=4, sticky=W)
        
        self.output_sheet.grid(row=6, column=2)
        self.protein_sequence.grid(row=6, column=4,sticky=W)
        self.mutation_sequence.grid(row=7, column=2, sticky=W)
        self.mutSYSEQ.grid(row=8, column=2, sticky=W) 
        self.mutSYStrength.grid(row=9, column=2,sticky=W) 
        self.regular_sequence.grid(row=7, column=4,sticky=W)
        self.regSYSEQ.grid(row=8, column=4,sticky=W)
        self.regSYStrength.grid(row=9, column=4,sticky=W)
        self.output_file.grid(row=11, column=2)
        #packs both of the cancel and run buttons
        self.ensembl.grid(row=11, column=4)
        self.runButton.grid(row=12, column=4)
        self.cancelButton.grid(row=12, column=3, sticky=E)
        self.pack(fill=BOTH, expand=1, padx=5, pady=5)
    def initUIListBox(self):
        self.canvas = Canvas(self, width=200, height=200)
        self.scroll = Scrollbar(self, bd=2,  orient="vertical",  command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scroll.set, scrollregion=(0,0,100,400))
        Label(self, text="Input and Output Variable Columns:").pack(side=TOP, anchor=W)
        self.canvas.pack(side=LEFT, expand=True, anchor=S)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.frame = Frame(self.canvas, width=200, height=500)
        self.canvas.create_window(100, 200, window=self.frame)
        i=0
        j=i
        while i < len(self.listVariables):
            Label(self.frame, text= self.listLabels[i]).grid(row=i, column=0, sticky=N, padx=5, pady=5)
            (self.listVariables[i]).set(chr(i + ord("A")))
            Entry(self.frame, textvariable=(self.listVariables[i]), width=3).grid(row=i, column=1, sticky=N, padx=5, pady=5)
            i=i+1
       
    def initUIListBoxExternals(self):
        self.frameExternal=Frame(self, width=200, height=200)
        i=0
        while i < len(self.listFileVariables):
            Label(self.frameExternal, text= self.listFileLabels[i]).grid(row=i, column=0, sticky=N, padx=5, pady=5)
            if(i==5):
                self.frameExternal.box = ttk.Combobox(self.frameExternal, textvariable=self.amerLength)
                self.frameExternal.box['values'] = self.amerLengthList
                self.frameExternal.box.current(0)
                self.frameExternal.box.grid(column=1, row=i, sticky=N, padx=5, pady=5)
            elif(i==6):
                self.frameExternal.box = ttk.Combobox(self.frameExternal, textvariable=self.geneType_col)
                self.frameExternal.box['values'] = self.immuneTypeList
                self.frameExternal.box.current(0)
                self.frameExternal.box.grid(column=1, row=i, sticky=N, padx=5, pady=5)
            elif(i==7):
                self.frameExternal.spin=Spinbox(self.frameExternal, textvariable=self.numSYReturns, from_ = 1, to = 15).grid(column=1, row=i, sticky=N, padx=5, pady=5)
            elif(i!=5 and i!=6):
                Entry(self.frameExternal, textvariable=self.listFileVariables[i]).grid(row=i, column=1, sticky=N, padx=5, pady=5)   
            i=i+1
        self.frameExternal.pack(side=RIGHT, expand=1, padx=15, pady=5)
    def runExcelInput(self):
        
        self.input_listStr=(self.accession_col.get()
        + self.ensembl_col.get()
        + self.mutIndex_col.get()
        + self.aChange_col.get()
        + self.mutation_sequence.get()
        + self.regular_sequence.get()
        + self.mutSYSEQ.get()
        + self.regSYSEQ.get()
        + self.mutSYStrength.get()
        + self.regSYStrength.get()
        + self.protein_sequence.get())
        print(self.geneType_col.get())
        print(str(self.amerLengthDict[self.amerLength.get()]))
        print(str(self.numSYReturns.get()))
        self.input_folderStr=self.input_folder.get()
        if(len(self.input_folderStr)<1):
            self.runButton.config("disable")
            self.output_fileStr=self.output_file.get()
            self.output_sheetStr=self.output_sheet.get()
            self.input_fileStr=self.input_file.get()
            self.input_sheetStr=self.input_sheet.get()
            self.excel=Excel(str(self.input_fileStr), str(self.input_sheetStr), str(self.output_fileStr), str(self.output_sheetStr),list(self.input_listStr), str(self.amerLengthDict[self.amerLength.get()]), str(self.geneType_col.get()),str(self.numSYReturns.get()), bool(self.ensembl_var.get()))
            self.excel.getEverything()
            return
        else:
            print(self.input_folderStr)
            print(glob.glob(self.input_folderStr + r'/*.*'))
            self.cycleThroughAllFiles()
       
    def cycleThroughAllFiles(self):
        fileroot=(self.input_folderStr + r'/*.*')
        fileList= glob.glob(fileroot)
        i=0
        while i<len(fileList):
            files=fileList[i]
            if((str(files).find(' SY.txt'))>=0):
                i=i+1
            elif((str(files).find(' SY.txt'))<0):
                try:
                    print(files)
                    filesOut= files.replace('.txt', ' SY.txt')
                    fileIn =files
                    self.excel=Excel(fileIn, '' ,filesOut,'', (self.input_listStr), str(self.amerLength), str(self.geneType_col),str(self.numSYReturns.get()), bool(self.ensembl_var.get()))
                    self.excel.getEverything()
                except:
                    print("File: " + files +" Does not work")
            i=i+1     
        
        
        

class FastaInput(ttk.Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)   
        self.runButton = Button(self, text="Execute", command=self.runInputFasta)
        self.cancelButton = Button(self, text="Cancel", command=self.quit)
        self.output_sheetStr= StringVar()
        self.input_fileStr= StringVar()
        self.input_sheetStr= StringVar()
        self.input_listStr= StringVar()
        self.fasta=None
        self.input_file = Entry(self)
        self.input_sheet = Entry(self)
        self.mutIndex_col = Entry(self, width=3)
        self.accession_col = Entry(self, width=3)
        self.aChange_col = Entry(self, width=3)
        self.output_file = Entry(self)
        self.initUI()
    def initUI(self):
       
        self.columnconfigure(0, pad=10)
        self.columnconfigure(1, pad=10)
        self.columnconfigure(2, pad=10)
        self.columnconfigure(3, pad=10)
        self.columnconfigure(4, pad=10)
        self.rowconfigure(0, pad=20)
        self.rowconfigure(1, pad=20)
        self.rowconfigure(2, pad=20)
        self.rowconfigure(3, pad=20)
        self.rowconfigure(4, pad=20)
        self.rowconfigure(5, pad=20)
        self.rowconfigure(6, pad=20)
        self.rowconfigure(7, pad=20)
        self.rowconfigure(8, pad=20)
        self.rowconfigure(9, pad=20)

        Label(self, text="INPUT LOCATIONS: ").grid(row=1, column=2)
       
        #the input sheets and files with text edit and labels
        Label(self, text="Input File Name:").grid(row=3, column=1)
        Label(self, text="Input Sheet Name:").grid(row=4, column=1)
        Label(self, text="Accession ID:").grid(row=3, column=3, sticky=E)
        Label(self, text="Mutation Index:").grid(row=4, column=3,sticky=E)
        Label(self, text="Amino Acid Change:").grid(row=5, column=3,sticky=E)
        
        Label(self, text="OUTPUT LOCATIONS: ").grid(row=6, column=2)
        Label(self, text="Output File Name:").grid(row=7, column=1)
        
        self.input_file.grid(row=3, column=2, padx= 5, pady=5)
        self.input_sheet.grid(row=4, column=2, padx=5, pady=5)
        self.accession_col.grid(row=3, column=4, sticky=E, padx=15, pady=5)
        self.mutIndex_col.grid(row=4, column=4, sticky=E, padx=15, pady=5)
        self.aChange_col.grid(row=5, column=4, sticky=E, padx=15, pady=5)
        self.output_file.grid(row=7, column=2, padx=5, pady=5) 
        
        #packs both of the cancel and run buttons
        self.runButton.grid(row=9, column=4)
        self.cancelButton.grid(row=9, column=3, sticky=E)
        self.pack(fill=BOTH, expand=1, padx=5, pady=5)
        
    def runInputFasta(self):
        self.output_sheetStr=self.output_file.get()
        self.input_fileStr=self.input_file.get()
        self.input_sheetStr=self.input_sheet.get()
        
        self.input_listStr=(self.accession_col.get()
        + self.mutIndex_col.get()
        + self.aChange_col.get())
        print(self.input_listStr)
        self.runButton.config("disable")
        self.fasta=Fasta(str(self.input_fileStr),str(self.input_sheetStr),str(self.input_listStr), str(self.output_sheetStr))
        self.fasta.processMutatedProteinFasta()
       

def main():
    #Setup Tk()
    window = Tk()
    window.title("Mutation Finder")
    #Setup the notebook (tabs)
    notebook = ttk.Notebook(window)
    fasta = ttk.Frame(notebook)
    excel = ttk.Frame(notebook)
    notebook.add(fasta, text="Fasta Format")
    notebook.add(excel, text="Excel Format")
    notebook.grid()
    #Create tab frames
    fastaFormat = FastaInput(master=fasta)
    fastaFormat.grid()
    excelFormat = ExcelInput(master=excel)
    excelFormat.grid()
    #Main loop
    window.mainloop()
    
if __name__ == '__main__':
    main()  