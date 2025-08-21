import tkinter as tk, tkinter.filedialog as fd, tkinter.messagebox as mb, PyPDF2 as p
from tkinterdnd2 import DND_FILES, TkinterDnD as tkd
def m():
 if f:=[l.get(i)for i in range(l.size())]:
  if o:=fd.asksaveasfilename(filetypes=[("PDF","*.pdf")],defaultextension='.pdf'):
   try:merger=p.PdfMerger();[merger.append(f)for f in f];merger.write(o);mb.showinfo("+",f"Merged {len(f)} files")
   except:mb.showerror("!","Error")
r=tkd.Tk();r.title("PDF Merger");r.geometry("400x400+{}+{}".format(r.winfo_screenwidth()//2-200,r.winfo_screenheight()//2-200));l=tk.Listbox(r);l.pack(expand=1,fill='both');l.drop_target_register(DND_FILES);l.dnd_bind('<<Drop>>',lambda e:[l.delete(0,'end')]+[l.insert('end',f)for f in sorted([f for f in r.tk.splitlist(e.data)if f.lower().endswith('.pdf')],key=str.lower)]);f=tk.Frame(r);f.pack()
[tk.Button(f,text=t,command=c).pack(side='left')for t,c in[("Add PDFs",lambda:[l.delete(0,'end')]+[l.insert('end',f)for f in sorted(fd.askopenfilenames(filetypes=[("PDF","*.pdf")]),key=str.lower)]),("Merge PDFs",m)]];r.mainloop()