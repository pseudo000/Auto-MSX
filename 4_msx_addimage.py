import os
import time
import pyautogui
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("MSX 自動化")
root.geometry("420x150")


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
        pyautogui.hotkey("Alt", "f4")
        time.sleep(1)

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
img = Image.open("pepe.png")
# 이미지를 Tkinter PhotoImage 객체로 변환
photo = ImageTk.PhotoImage(img)



# 디렉토리 선택
def add_path():
    addpath_selected = filedialog.askdirectory()
    if addpath_selected == '':
        return

    txt_folder_path.delete(0, END)
    txt_folder_path.insert(0, addpath_selected)

    file_list = get_file_list(addpath_selected)
    start_msx(file_list)



# 프레임1 생성
frame1 = LabelFrame(root, text="START")
frame1.pack(fill="x", padx=5, pady=5, ipady=5)

txt_folder_path = Entry(frame1)
txt_folder_path.pack(side="left", fill="x", expand="True", ipady=4)

btn_add_path = Button(frame1, text="フォルダー選択", command=add_path)
btn_add_path.pack(side=LEFT)

root.mainloop()
