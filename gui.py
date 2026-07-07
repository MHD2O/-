import customtkinter as ctk
from tkinter import filedialog,messagebox
class CertificateGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Engineering Club Certificate Sender")
        self.geometry("900x700")
        self._mk("اسم الدورة بالعربية",0); self.course_ar=self.e
        self._mk("Course Name (English)",1); self.course_en=self.e
        self._mk("التاريخ",2); self.date=self.e
        self._mk("عدد الساعات",3); self.hours=self.e
        self._mk("عنوان البريد",4); self.subject=self.e
        ctk.CTkButton(self,text="اختيار Excel",command=self.pick_excel).grid(row=5,column=0,padx=8,pady=8)
        ctk.CTkButton(self,text="اختيار قالب",command=self.pick_template).grid(row=5,column=1,padx=8,pady=8)
        ctk.CTkLabel(self,text="نص الرسالة").grid(row=6,column=0,columnspan=2)
        self.body=ctk.CTkTextbox(self,width=700,height=180); self.body.grid(row=7,column=0,columnspan=2,padx=8,pady=8)
        self.progress=ctk.CTkProgressBar(self); self.progress.grid(row=8,column=0,columnspan=2,sticky="ew",padx=8,pady=8); self.progress.set(0)
        ctk.CTkButton(self,text="إنشاء الشهادات",command=self.generate).grid(row=9,column=0,padx=8,pady=8)
        ctk.CTkButton(self,text="إنشاء وإرسال الشهادات",command=self.send).grid(row=9,column=1,padx=8,pady=8)
    def _mk(self,l,r):
        ctk.CTkLabel(self,text=l).grid(row=r,column=0,sticky="w"); self.e=ctk.CTkEntry(self,width=500); self.e.grid(row=r,column=1)
    def pick_excel(self): self.excel=filedialog.askopenfilename(filetypes=[('Excel','*.xlsx')])
    def pick_template(self): self.tpl=filedialog.askopenfilename(filetypes=[('PowerPoint','*.pptx')])
    def generate(self): messagebox.showinfo("Info","اربطها مع certificate.py")
    def send(self): messagebox.showinfo("Info","اربطها مع outlook_sender.py")
if __name__=="__main__": CertificateGUI().mainloop()
