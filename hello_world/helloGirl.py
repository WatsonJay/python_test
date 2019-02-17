import tkinter as tk
from tkinter import messagebox
import random

def no_close():
    return

#关闭窗口提示
def close_window():
    messagebox.showinfo(title="不要嘛~", message="不选好不许走！")

#关闭窗口
def close_all_window():
    window.destroy()

def love():
    love= tk.Toplevel(window)
    love.geometry("300x100+580+250")
    love.title("爱你么么哒~")
    btn = tk.Button(love, text="老婆真好！", width=10, height=2, command=close_all_window)
    btn.place(x=110, y=30)
    love.protocol("WM_DELETE_WINDOW", no_close)

def on_enter(e):
    global pos
    dx = random.randint(100, 200)
    dy = random.randint(100, 300)
    print(pos,dx,dy)
    pos = (pos[0] + dx) % 200, (pos[1] - 250 + dy) % 350 + 250
    btn_no.place(x=pos[0], y=pos[1])


window = tk.Tk()
window.title("我来道歉的")  # 窗口标题
window.geometry("360x640+550+50")  # 窗口大小
window.protocol("WM_DELETE_WINDOW", close_window)  # 窗口关闭
label = tk.Label(window, text="老婆我知道错了", font=("微软雅黑",18))
label.place(x=90, y=50)
label = tk.Label(window, text="别生我的气了好不好嘛", font=("微软雅黑",24))
label.place(x=15, y=100)
btn_yes = tk.Button(window, text="原谅你", width=15, height=2, command=love)
btn_yes.place(x=120, y=200)
btn_no = tk.Button(window, text="不原谅", width=15, height=2)
pos = [120, 300]
btn_no.place(x=120, y=300)
btn_no.bind("<Enter>", on_enter)
window.mainloop()

