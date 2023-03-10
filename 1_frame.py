import tkinter.ttk as ttk   
from tkinter import*

root = Tk()
root.title("IMPORT MSX")
root.resizable(False,False)



#프레임1 (엑셀파일선택, 경로)
xls_frame = LabelFrame(root, text="Select MSX files")
xls_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_xls_path = Entry(xls_frame)
txt_xls_path.pack(side="left", fill="x", expand="True", ipady=4) #

btn_xls_path = Button(xls_frame, text="...txt files",padx=5, pady=5, width=12)
btn_xls_path.pack(side="right")


#SEND MSX
splitpdf_frame = LabelFrame(root, text="Send MSX for NACCS")
splitpdf_frame.pack(fill="x",padx=5, pady=5, ipady=5)

btn_splitpdf = Button(splitpdf_frame, text="START", padx=5, pady=5, width="20")
btn_splitpdf.pack()




# 진행상황 profress bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x")



# 종료 프레임
close_frame = Frame(root)
close_frame.pack(side="right", padx=5, pady=5)

btn_close = Button(close_frame, padx=5, pady=5, text="CLOSE", width=12)
btn_close.pack()


p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x")





root.mainloop()

