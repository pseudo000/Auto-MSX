import os
import time
import pyautogui
from tkinter import *
from tkinter import filedialog, messagebox


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

    messagebox.showinfo("작업 완료")


# 디렉토리 선택
def add_path():
    addpath_selected = filedialog.askdirectory()
    if addpath_selected == '':
        return

    txt_folder_path.delete(0, END)
    txt_folder_path.insert(0, addpath_selected)

    file_list = get_file_list(addpath_selected)
    start_msx(file_list)


# GUI 생성
root = Tk()
root.title("MSX 자동화")
root.geometry("400x150")

txt_folder_path = Entry(root, width=50)
txt_folder_path.pack(side=LEFT, padx=10)

btn_add_path = Button(root, text="경로 선택", command=add_path)
btn_add_path.pack(side=LEFT)

root.mainloop()
