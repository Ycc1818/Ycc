import tkinter as tk
import random
import time
import sys
import math

h, a = [], []
t = ["多喝水利", "好好爱自己", "好好吃饭", "保持好心情", "我想你了", "顺顺利利", "别熬夜", "天凉了多穿衣服"]
c = ["pink", "lightblue", "lightgreen", "lemonchiffon", "hotpink", "skyblue"]

MAX_HEART_WINDOWS = 100
MAX_RANDOM_WINDOWS = 500 #随机弹窗生成数量
current_random_count = 0


def g(n, w, h):
    p = []
    for i in range(n):
        th = i / n * 2 * math.pi
        x = 16 * math.sin(th) ** 3
        y = 13 * math.cos(th) - 5 * math.cos(2 * th) - 2 * math.cos(3 * th) - math.cos(4 * th)
        sx = int(w / 2 + x * 20 - 50)
        sy = int(h / 2 - y * 20 - 80)
        p.append((max(0, min(sx, w - 150)), max(0, min(sy, h - 60))))
    return p


def wx(x, y, tip=None, is_h=True):
    w = tk.Toplevel()
    w.geometry(f"150x60+{x}+{y}")
    w.title("提示")
    w.attributes('-topmost', 1)
    tk.Label(w, text=tip or random.choice(t), bg=random.choice(c), font=("微软雅黑", 14), width=20, height=3).pack()
    w.bind('<space>', lambda e: [_.destroy() for _ in h + a] or sys.exit())
    return w


'''def create_love_window(sw, sh):
    love_window = tk.Toplevel()
    love_window.geometry(f"400x200+{sw // 2 - 200}+{sh // 2 - 100}")
    love_window.title("特别提示")
    love_window.attributes('-topmost', 1)
    love_window.configure(bg='red')

    tk.Label(
        love_window,
        text="我爱你",
        bg='white',
        fg='black',
        font=("微软雅黑", 14, "bold"),
        width=20,
        height=3,
    ).pack(fill=tk.BOTH, expand=True)



    return love_window

'''
def w():
    global current_random_count

    r = tk.Tk()
    r.withdraw()
    sw, sh = r.winfo_screenwidth(), r.winfo_screenheight()

    n = min(MAX_HEART_WINDOWS, 100)

    for i, (x, y) in enumerate(g(n, sw, sh)):
        w = wx(x, y, "充实自己" if i == n - 1 else None)
        h.append(w)
        r.update()
        time.sleep(0.03)

    time.sleep(1)
    [_.destroy() for _ in h if isinstance(_, tk.Toplevel) and _.winfo_exists()]

    max_random_windows = min(sw // 150 * sh // 40 + 50, MAX_RANDOM_WINDOWS)

    for _ in range(max_random_windows):
        x, y = random.randint(0, sw - 150), random.randint(0, sh - 60)
        w = wx(x, y, is_h=False)
        a.append(w)
        current_random_count += 1
        r.update()
        time.sleep(0.005)

        if current_random_count >= MAX_RANDOM_WINDOWS:
            break

    status_window = tk.Toplevel()
    status_window.geometry(f"300x80+{sw // 2 - 150}+{sh - 100}")
    status_window.title("状态")
    status_window.attributes('-topmost', 1)
    status_label = tk.Label(
        status_window,
        text=f"已创建 {current_random_count} 个弹窗 (达到上限 {MAX_RANDOM_WINDOWS})",
        bg="lightyellow",
        font=("微软雅黑", 12)
    )
    status_label.pack(fill=tk.BOTH, expand=True)

    time.sleep(2)

    status_window.destroy()

    for window in a:
        if isinstance(window, tk.Toplevel) and window.winfo_exists():
            window.destroy()
    r.update()
    time.sleep(0.5)
'''
    love_window = create_love_window(sw, sh)

    love_window.after(5000, lambda: [love_window.destroy(), sys.exit()])

    r.mainloop()
'''

if __name__ == "__main__":
    w()