import pyautogui
import os
import time
import tkinter as tk
from tkinter import messagebox

# NACCS를 최상단 윈도우로 불러오기
def active_window():
    program_name = "netNACCS"
    windows = pyautogui.getAllWindows() # 현재 실행 중인 모든 창 가져오기

    target_window = None # 대상 프로그램 찾기
    for window in windows:
        if program_name in window.title:
            target_window = window
            break

    if target_window: # 대상 프로그램 창이 있는 경우
        if target_window.isMinimized: # 최소화되어 있는 경우
            target_window.restore() # 창을 복원
        target_window.activate() # 창을 최상위로 올리기




# txt 파일 리스트 리턴
def get_file_list(folder_path):
    folder_path = "C:\import"
    file_list = [] # 파일 리스트 초기화

    for filename in os.listdir(folder_path): # 폴더 내 모든 파일에 대해서
        name, ext = os.path.splitext(filename)
        if ext == ".txt": # 확장자가 .txt 인 경우
            file_list.append(name) # 파일 이름만 파일 리스트에 추가

    return file_list
            


def start_msx(folder_path):
    active_window() # NACCS 창 최상위로 올리기
    file_list = get_file_list(folder_path) # txt 파일 리스트 가져오기

    for file_name in file_list:
        pyautogui.hotkey("ctrl", "o") # Ctrl + O 입력
        time.sleep(0.5)
        pyautogui.typewrite(file_name) # 파일이름 입력
        pyautogui.press("enter") # 엔터 입력
        time.sleep(0.5)
        pyautogui.hotkey("f11")
        time.sleep(0.5)
        pyautogui.typewrite(file_name + ".pdf") # 파일이름 입력
        pyautogui.press("enter") # 엔터 입력
        pyautogui.typewrite("AL")
        pyautogui.press("enter") # 엔터 입력
        pyautogui.hotkey("f12")
        time.sleep(1)
        pyautogui.hotkey("Alt", "f4")
        pyautogui.hotkey("Alt", "f4")

    messagebox.showinfo("작업 완료")