import os
import time
import pyautogui
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



root = Tk()
root.title("MSX 自動化")
root.geometry("600x450")


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
    for file_name in file_list:
        time.sleep(1)
        pyautogui.hotkey("ctrl", "o")
        time.sleep(1)
        pyautogui.typewrite(file_name)
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.hotkey("f11")
        time.sleep(1)
        pyautogui.typewrite(file_name + ".pdf")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.typewrite("AL")
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.hotkey("f12")
        time.sleep(1)
        pyautogui.hotkey("Alt", "f4")
        time.sleep(1)
        # pyautogui.hotkey("Alt", "f4")
        # time.sleep(1)

    show_image()


def show_image():
    # 새로운 창 생성
    image_window = Toplevel(root)
    image_window.title("COMPLETE!")
    image_window.attributes("-topmost", True)  # 새로운 창을 윈도우 중앙에 배치하기 전, 윈도우 프로그램 중 제일 앞으로 보냄
    # 이미지 레이블 생성
    image_label = Label(image_window, image=photo)
    image_label.pack()

        # 창의 크기 설정
    image_window.geometry("320x320")

    # 창을 윈도우 중앙에 배치
    image_window.update_idletasks()
    width = image_window.winfo_width()
    height = image_window.winfo_height()
    x = (image_window.winfo_screenwidth() // 2) - (width // 2)
    y = (image_window.winfo_screenheight() // 2) - (height // 2)
    image_window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# 이미지 로드
img = Image.open(resource_path("pepe.png"))
# 이미지를 Tkinter PhotoImage 객체로 변환
photo = ImageTk.PhotoImage(img)



# send msx 디렉토리 선택 -> 자동실행
def add_path():
    addpath_selected = filedialog.askdirectory()
    if addpath_selected == '':
        return

    txt_folder_path.delete(0, END)
    txt_folder_path.insert(0, addpath_selected)

    file_list = get_file_list(addpath_selected)
    start_msx(file_list)


# check files -> 자동실행
def add_checkpath():
    checkpath_selected = filedialog.askdirectory()
    txt_files = []
    pdf_files = []

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

    # 동일한 이름을 가진 파일이 존재하는지 확인
    for file_name in txt_files:
        # txt 파일 이름에서 확장자를 제외한 이름 추출
        name_without_ext = os.path.splitext(file_name)[0]
        # pdf 파일이 존재하지 않으면 경고 메시지 출력
        if f'{name_without_ext}.pdf' not in pdf_files:
            messagebox.showinfo('確認',f'{file_name}と同じファイル名のPDFファイルが存在しません。')




# 프레임1 생성
frame1 = LabelFrame(root, text="START_Check Files")
frame1.pack(fill="x", padx=5, pady=5, ipady=5)

btn_check_path = Button(frame1, text="フォルダー選択", command=add_checkpath)
btn_check_path.pack()


# 프레임2 생성
frame2 = LabelFrame(root, text="START_Send MSX Files")
frame2.pack(fill="x", padx=5, pady=5, ipady=5)

txt_folder_path = Entry(frame2)
txt_folder_path.pack(side="left", fill="x", expand="True", ipady=4)

btn_add_path = Button(frame2, text="フォルダー選択", command=add_path)
btn_add_path.pack(side=LEFT)


#메시지 작성
message = tk.Message(root, text="条件1．NACCSを起動し、ログインしておくこと。\
                     \n条件2．指定するフォルダーには、各MSX.txtファイル1個と、\
                     \n           そのMSX.pdfファイル1個を同じファイル名で必ずペアにしておくこと\
                     条件3．NACCS設定で、送信をf12、添付ファイルの追加をf11に設定すること \
                     \n\r使用方法\n1．START_Check_filesで作業をするフォルダーのファイルペア状況を確認する。\
                     \t(ペアになっていない場合、エラーメッセージが出ます。)\
                     \n2．START_Send MSX Filesでフォルダー選択すると、自動的に作業が始まります。\
                     3．完了\
                     \n\r\r        注意!！一度作業が始まると絶対に止まりません。注意してくだいさい\
                     \n        注意!！COMPLETEメッセージが出るまでパソコンを操作しないでください。", width=550, font=("Meiryo UI", 11 ,"bold"))
message.pack()




root.mainloop()
# pyinstaller -w -F --add-data '*.png;.' 5_add...............