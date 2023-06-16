# NACCS전송 중간중간에 필

import os
import shutil
import time
import pyautogui
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont
from tkinter import *
from tkinter import filedialog, messagebox
import sys
from PIL import Image
import pyperclip


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


root = Tk()
root.title("MSX..............")
root.geometry("600x550")


# NACCS 창 최상위로 올리기
def active_window():
    program_name = "netNACCS"
    windows = pyautogui.getAllWindows()

    target_window = None
    for window in windows:
        if program_name in window.title:
            target_window = window
            break

    if target_window:
        if target_window.isMinimized:
            target_window.restore()
        target_window.activate()
    else:
        messagebox.showerror('エラー', f"{program_name}を起動してください。")
        raise Exception(f"{program_name}を起動してください。")

# 파일리스트 반환
def get_file_list(folder_path):
    file_list = []

    for filename in os.listdir(folder_path):
        name, ext = os.path.splitext(filename)
        if ext == ".txt":
            file_list.append(name)

    return file_list



# MSX 실행
def start_msx(file_list):
    active_window()

    # 완료 폴더 경로 설정
    sended_folder = os.path.join(txt_frame0_path.get(), "sended")
    os.makedirs(sended_folder, exist_ok=True)

    path = txt_frame0_path.get().replace('/', '\\')  # '/'를 '\'로 변경
    pyperclip.copy(path)  # 변경된 문자열을 클립보드에 복사

    for file_name in file_list:
        time.sleep(1)
        pyautogui.hotkey("ctrl", "o")
        time.sleep(1)
        pyautogui.hotkey("f4")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl", "a")
        time.sleep(0.5)
        pyautogui.press("delete")
        time.sleep(0.5)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(2)
        pyautogui.hotkey("alt", "n")
        time.sleep(0.5)
        pyautogui.typewrite(file_name)
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(2)
        pyautogui.hotkey("f11")
        time.sleep(2)
        pyautogui.typewrite(file_name + ".pdf")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(2)
        pyautogui.typewrite("AL")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.hotkey("f12")
        time.sleep(6)
        pyautogui.hotkey("Alt", "f4")
        time.sleep(1)
     

        txt_file_path = os.path.join(txt_frame0_path.get(), file_name + ".txt")
        pdf_file_path = os.path.join(txt_frame0_path.get(), file_name + ".pdf")
        txt_sended_path = os.path.join(sended_folder, file_name + ".txt")
        pdf_sended_path = os.path.join(sended_folder, file_name + ".pdf")
        shutil.move(txt_file_path, txt_sended_path)
        shutil.move(pdf_file_path, pdf_sended_path)

    messagebox.showinfo('COMPLETE', "送信を完了しました。") 

def add_path0():
    addpath_selected = filedialog.askdirectory()
    if addpath_selected == '': #사용자가 취소를 누를 때
        return
    txt_frame0_path.delete(0, END)
    txt_frame0_path.insert(0,addpath_selected)
    return addpath_selected

# send msx 디렉토리 선택 -> 자동실행
def add_path():
    addpath_selected = txt_frame0_path.get()
    if addpath_selected == '':
        return

    # txt_folder_path.delete(0, END)
    # txt_folder_path.insert(0, addpath_selected)

    file_list = get_file_list(addpath_selected)
    start_msx(file_list)


# check files -> 자동실행
def add_checkpath():
    checkpath_selected = txt_frame0_path.get()
    txt_files = []
    pdf_files = []

    txt_frame2 = Text(root, height=10)
    txt_frame2.pack(fill="both", expand=True)
    scroll_bar = Scrollbar(txt_frame2, orient="vertical", command=txt_frame2.yview)
    scroll_bar.pack(side="right", fill="y")
    txt_frame2.config(yscrollcommand=scroll_bar.set)

    # 폰트 스타일 정의
    font_style = tkfont.Font(family="Meiryo", size=10)  # 원하는 폰트 패밀리와 크기로 설정
    txt_frame2.configure(font=font_style)

    # 폴더 안의 파일들을 모두 탐색
    for file_name in os.listdir(checkpath_selected):
        # 파일 이름에서 확장자 추출
        file_ext = os.path.splitext(file_name)[1]

        # 파일이 txt인 경우 txt_files 리스트에 추가
        if file_ext == '.txt':
            txt_files.append(file_name)
        # 파일이 pdf인 경우 pdf_files 리스트에 추가
        elif file_ext == '.pdf':
            pdf_files.append(file_name)

    if not txt_files:
        message = "フォルダーに txtファイルが存在しません。\n"
        txt_frame2.insert(END, message)    

    # 동일한 이름을 가진 파일이 존재하는지 확인
    for file_name in txt_files:
        # txt 파일 이름에서 확장자를 제외한 이름 추출
        name_without_ext = os.path.splitext(file_name)[0]
        # pdf 파일이 존재하지 않으면 경고 메시지 출력
        if f'{name_without_ext}.pdf' not in pdf_files:
            message2 = (f'{file_name}と同じファイル名のPDFファイルが存在しません。\n')
            txt_frame2.insert(END, message2)
    
    # txt 파일과 pdf 파일의 개수 출력
    txt_count = len(txt_files)
    pdf_count = len(pdf_files)
    message_count = f"■txt ファイル数: {txt_count}    ■pdf ファイル数: {pdf_count}\n"
    txt_frame2.insert(END, message_count)

    # txt와 pdf가 일치하는 수 출력
    match_count = sum(1 for txt_file in txt_files if os.path.splitext(txt_file)[0] + ".pdf" in pdf_files)
    message_match = f"■txtとpdfが一致する数: {match_count}\n"
    txt_frame2.insert(END, message_match)

    messagebox.showinfo('確認', "ファイルのペアを確認しました。")


#프레임1 (기본 다운로드폴더 지정)
frame0 = LabelFrame(root, text="Select defalut folder")
frame0.pack(fill="x", padx=5, pady=5, ipady=5)

txt_frame0_path = Entry(frame0)
txt_frame0_path.pack(side="left", fill="x", expand="True", ipady=4) #

btn_frame0_path = Button(frame0, text="...folder",padx=5, pady=5, width=12, command = add_path0)
btn_frame0_path.pack(side="right")


# 프레임1 생성
frame1 = LabelFrame(root, text="START_Check Files")
frame1.pack(fill="x", padx=5, pady=5, ipady=5)

btn_check_path = Button(frame1, text="CHECK", command=add_checkpath)
btn_check_path.pack()


# 프레임2 생성
frame2 = LabelFrame(root, text="START_Send MSX Files")
frame2.pack(fill="x", padx=5, pady=5, ipady=5)

btn_add_path = Button(frame2, text="START", command=add_path)
btn_add_path.pack()
# btn_add_path.pack(side=LEFT)



#메시지 작성
# message = tk.Message(root, text="条件1．NACCSを起動し、ログインして下さい。\
#                      \n条件2．フォルダーは、ドキュメントい以外に指定不可です。\
#                      \n条件3．各MSX.txtファイル1個と、そのMSX.pdfファイル1個を　\
#                      \n\t同じファイル名で必ずペアにして下さい。\
#                      条件4．NACCS設定で、送信をf12、添付ファイルの追加をf11に設定して下さい。 \
#                      \n\r使用方法\n1．START_Check_filesで作業をするフォルダーのファイルペア状況を確認する。\
#                      \t(ペアになっていない場合、エラーメッセージが出ます。)\
#                      \n2．START_Send MSX Filesでフォルダー選択すると、自動的に作業が始まります。\
#                      3．完了\
#                      \n\r\r        注意!！COMPLETEメッセージが出るまでパソコンを操作しないでください。", width=550, font=("Meiryo UI", 11 ,"bold"))
                     
# message.pack()




root.mainloop()

# pyinstaller -w -F --add-data 'COMPLETE22.png;.' 7_addtest.py