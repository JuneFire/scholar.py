import scholar
import time
import tkinter as tk
from tkinter import filedialog
# --txt-globals --phrase "Deep Multi-scale Convolutional"
# args = "Deep Multi-scale Convolutional"


def operafile(filename):
    with open(filename, encoding='utf-8-sig') as f:
        while True:
            line = f.readline().replace('\r', '').replace('\n', '')
            if not line:
                break
            print('Phrase: ', line)
            process(line)


def process(line):
    scholar.run(line, 1)
    time.sleep(0.5)


if __name__ == "__main__":
    '''打开选择文件夹对话框'''
    root = tk.Tk()
    root.withdraw()

    Filepath = filedialog.askopenfilename()  # 获得选择好的文件
    operafile(Filepath)
