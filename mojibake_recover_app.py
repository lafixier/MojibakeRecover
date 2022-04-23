# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 07:26:35 2020
"""


import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import sys



num = -1
file = ""
encoding = "shift-jis"


def opennewfile():
    global file, encoding_dic, text
    user_name = os.getlogin()

    typ = [('テキストファイル','*.txt'), ("すべてのファイル", "*.*")]
    try:
        dir = "C:/Users/" + user_name + "/Documents/"
        file = filedialog.askopenfilename(filetypes = typ, initialdir = dir) 
    except:
        file = filedialog.askopenfilename(filetypes = typ)

    outputtext_bx.delete(0.0, tk.END)
    text = ""
    try:
        if encoding == "auto":
            with open(file, "r") as tf:
                for line in tf:
                    text += line
        else:
            with open(file, "r", encoding = encoding) as tf:
                for line in tf:
                    text += line

    except:
        if file != "":
            messagebox.showerror("エラー", "この文字コードでは開けません。: " + encoding_dic[encoding])

    root.title(file + "  - Mojibake Recover -")
    outputtext_bx.delete(0.0, tk.END)
    outputtext_bx.insert(tk.END, str(text))

def openfile():
    global file, encoding_dic, text

    outputtext_bx.delete(0.0, tk.END)
    text = ""
    try:
        if encoding == "auto":
            with open(file, "r") as tf:
                for line in tf:
                    text += line
        else:
            with open(file, "r", encoding = encoding) as tf:
                for line in tf:
                    text += line
    except:
        if file != "":
            messagebox.showerror("エラー", "この文字コードでは開けません。: " + encoding_dic[encoding])

    root.title(file + "  - Mojibake Recover -")
    outputtext_bx.delete(0.0, tk.END)
    outputtext_bx.insert(tk.END, str(text))




def savefile():
    global text

    user_name = os.getlogin()
    typ = [("テキストファイル", "*.txt")]
    try:
        dir = "C:/Users/" + user_name + "/Documents/"
        file = filedialog.asksaveasfilename(initialfile = "*.txt", filetypes = typ, initialdir = dir)
    except:
        file = filedialog.asksaveasfilename(initialfile = "*.txt", filetypes = typ)
    with open(file, "w", encoding = "utf-8") as f:
        f.write(text)
    messagebox.showinfo("保存", file + " に保存しました。")







def chooseencoding():
    global encoding
    global num

    encoding_list = ["utf-8", "utf-16", "utf-16be", "shift-jis", "jis", "euc-jp", "euc", "ascii", "utf-7", "cesu-8", "latin1"]
    encoding_list_sub= ["UTF-8", "UTF-16", "UTF-16BE", "Shift-JIS(ANSI)", "JIS(ISO-2022-JP)", "EUC-JP", "EUC", "ASCII", "UTF-7", "CESU-8", "Latin1"]

    num += 1
    if num + 1 > len(encoding_list):
        num = 0
    encoding_txtbox.delete(0.0, tk.END)
    encoding_txtbox.insert(tk.END, str(encoding_list_sub[num]))
    encoding = encoding_list[num]


def quit_msg():
    ans = messagebox.askquestion("確認", "終了しますか？")
    if ans == "yes":
        sys.exit()


if __name__ == '__main__':
    encoding_dic= {"utf-8": "UTF-8", "utf-16": "UTF-16", "utf-16be": "UTF-16BE", "shift-jis": "Shift-JIS(ANSI)", "jis": "JIS(ISO-2022-JP)", "euc-jp": "EUC-JP", "euc": "EUC", "ascii": "ASCII", "utf-7": "UTF-7", "cesu-8": "CESU-8", "latin1": "Latin1"}

    root = tk.Tk()
    root.title("Mojibake Recover")
    root.geometry("900x600")
    root.iconbitmap(default = "mr.ico")


    opennewfile_bt = tk.Button(root, text = "新しいファイルを開く", command = opennewfile)
    openfile_bt = tk.Button(root, text = "ファイルを開く", command = openfile)
    encoding_bt = tk.Button(root, text = "文字コード", command = chooseencoding)
    outputtext_bx = tk.Text(root, width = 90, height = 40)
    encoding_txtbox = tk.Text(root, width = 20, height = 1)
    save_bt = tk.Button(root, text = "名前を付けて保存", command = savefile)
    end_bt = tk.Button(root, text = "終了", command = quit_msg)
    encoding_txtbox.insert(tk.END, str("Shift-jis(ANSI)"))

    opennewfile_bt.place(x = 10, y = 10)
    openfile_bt.place(x = 10, y = 35)
    encoding_bt.place(x = 10, y = 60)
    outputtext_bx.place(x = 200, y = 20)
    encoding_txtbox.place(x = 10, y = 90)
    save_bt.place(x = 10, y = 125)
    end_bt.place(x = 10, y = 150)


    root.mainloop()
