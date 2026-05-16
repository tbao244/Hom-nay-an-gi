import tkinter as tk
from tkinter import ttk
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import math

khoiluongtai=ctrl.Antecedent(np.arange(0,10.1,0.1),'khoiluongtai')
mucdoban=ctrl.Antecedent(np.arange(0,101,1),'mucdoban')
loaivai=ctrl.Antecedent(np.arange(0,11,1),'loaivai')

thoigiat = ctrl.Consequent(np.arange(30,100.1,10), 'thoigiat')
mucnuoc = ctrl.Consequent(np.arange(10,50.1,10), 'mucnuoc')

khoiluongtai['nho'] = fuzz.trimf(khoiluongtai.universe,[0,0,5])
khoiluongtai['trungbinh'] = fuzz.trimf(khoiluongtai.universe,[0,5,10])
khoiluongtai['lon'] = fuzz.trimf(khoiluongtai.universe,[5,10,10])

mucdoban['thap'] = fuzz.trimf(mucdoban.universe,[0,0,50])
mucdoban['trungbinh'] = fuzz.trimf(mucdoban.universe,[0,50,100])
mucdoban['cao'] = fuzz.trimf(mucdoban.universe,[50,100,100])

loaivai['mong'] = fuzz.trapmf(loaivai.universe, [0, 0, 3, 3])
loaivai['binhthuong'] = fuzz.trapmf(loaivai.universe, [3, 4, 7, 8])
loaivai['nang'] = fuzz.trapmf(loaivai.universe, [8, 9, 11, 11])

thoigiat['ngan'] = fuzz.trimf(thoigiat.universe, [30, 40, 55])
thoigiat['trungbinh'] = fuzz.trimf(thoigiat.universe, [50, 65, 80])
thoigiat['dai'] = fuzz.trimf(thoigiat.universe, [75, 90, 100])

mucnuoc['thap'] = fuzz.trimf(mucnuoc.universe, [0, 0, 5])
mucnuoc['trungbinh'] = fuzz.trimf(mucnuoc.universe, [0, 5, 10])
mucnuoc['cao'] = fuzz.trimf(mucnuoc.universe, [5, 10, 10])

rule1 = ctrl.Rule(khoiluongtai['nho'] & mucdoban['thap'] & loaivai['mong'], [thoigiat['ngan'], mucnuoc['thap']])
rule2 = ctrl.Rule(khoiluongtai['nho'] & mucdoban['thap'] & loaivai['binhthuong'], [thoigiat['trungbinh'], mucnuoc['thap']])
rule3 = ctrl.Rule(khoiluongtai['nho'] & mucdoban['thap'] & loaivai['nang'], [thoigiat['trungbinh'], mucnuoc['trungbinh']])
rule4 = ctrl.Rule(khoiluongtai['nho'] & mucdoban['trungbinh'] & loaivai['mong'], [thoigiat['ngan'], mucnuoc['thap']])
rule5 = ctrl.Rule(khoiluongtai['nho'] & mucdoban['trungbinh'] & loaivai['binhthuong'], [thoigiat['trungbinh'], mucnuoc['thap']])
rule6 = ctrl.Rule(khoiluongtai['nho'] & mucdoban['trungbinh'] & loaivai['nang'], [thoigiat['trungbinh'], mucnuoc['trungbinh']])
rule7 = ctrl.Rule(khoiluongtai['nho'] & mucdoban['cao'] & loaivai['mong'], [thoigiat['trungbinh'], mucnuoc['thap']])
rule8 = ctrl.Rule(khoiluongtai['nho'] & mucdoban['cao'] & loaivai['binhthuong'], [thoigiat['trungbinh'], mucnuoc['trungbinh']])
rule9 = ctrl.Rule(khoiluongtai['nho'] & mucdoban['cao'] & loaivai['nang'], [thoigiat['dai'], mucnuoc['trungbinh']])
rule10 = ctrl.Rule(khoiluongtai['trungbinh'] & mucdoban['thap'] & loaivai['mong'], [thoigiat['ngan'], mucnuoc['trungbinh']])
rule11 = ctrl.Rule(khoiluongtai['trungbinh'] & mucdoban['thap'] & loaivai['binhthuong'], [thoigiat['trungbinh'], mucnuoc['trungbinh']])
rule12 = ctrl.Rule(khoiluongtai['trungbinh'] & mucdoban['thap'] & loaivai['nang'], [thoigiat['trungbinh'], mucnuoc['cao']])
rule13 = ctrl.Rule(khoiluongtai['trungbinh'] & mucdoban['trungbinh'] & loaivai['mong'], [thoigiat['trungbinh'], mucnuoc['trungbinh']])
rule14 = ctrl.Rule(khoiluongtai['trungbinh'] & mucdoban['trungbinh'] & loaivai['binhthuong'], [thoigiat['trungbinh'], mucnuoc['trungbinh']])
rule15 = ctrl.Rule(khoiluongtai['trungbinh'] & mucdoban['trungbinh'] & loaivai['nang'], [thoigiat['dai'], mucnuoc['cao']])
rule16 = ctrl.Rule(khoiluongtai['trungbinh'] & mucdoban['cao'] & loaivai['mong'], [thoigiat['trungbinh'], mucnuoc['trungbinh']])
rule17 = ctrl.Rule(khoiluongtai['trungbinh'] & mucdoban['cao'] & loaivai['binhthuong'], [thoigiat['dai'], mucnuoc['cao']])
rule18 = ctrl.Rule(khoiluongtai['trungbinh'] & mucdoban['cao'] & loaivai['nang'], [thoigiat['dai'], mucnuoc['cao']])
rule19 = ctrl.Rule(khoiluongtai['lon'] & mucdoban['thap'] & loaivai['mong'], [thoigiat['trungbinh'], mucnuoc['cao']])
rule20 = ctrl.Rule(khoiluongtai['lon'] & mucdoban['thap'] & loaivai['binhthuong'], [thoigiat['trungbinh'], mucnuoc['cao']])
rule21 = ctrl.Rule(khoiluongtai['lon'] & mucdoban['thap'] & loaivai['nang'], [thoigiat['dai'], mucnuoc['cao']])
rule22 = ctrl.Rule(khoiluongtai['lon'] & mucdoban['trungbinh'] & loaivai['mong'], [thoigiat['trungbinh'], mucnuoc['cao']])
rule23 = ctrl.Rule(khoiluongtai['lon'] & mucdoban['trungbinh'] & loaivai['binhthuong'], [thoigiat['dai'], mucnuoc['cao']])
rule24 = ctrl.Rule(khoiluongtai['lon'] & mucdoban['trungbinh'] & loaivai['nang'], [thoigiat['dai'], mucnuoc['cao']])
rule25 = ctrl.Rule(khoiluongtai['lon'] & mucdoban['cao'] & loaivai['mong'], [thoigiat['dai'], mucnuoc['cao']])
rule26 = ctrl.Rule(khoiluongtai['lon'] & mucdoban['cao'] & loaivai['binhthuong'], [thoigiat['dai'], mucnuoc['cao']])
rule27 = ctrl.Rule(khoiluongtai['lon'] & mucdoban['cao'] & loaivai['nang'], [thoigiat['dai'], mucnuoc['cao']])

washing_ctrl = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6,rule7,rule8,rule9,rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18,
    rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27])
washing = ctrl.ControlSystemSimulation(washing_ctrl)

import tkinter as tk
import math

# ======================================================
# WINDOW
# ======================================================

root = tk.Tk()
root.title("Máy Giặt AI Fuzzy")
root.geometry("1180x700")
root.configure(bg="#020817")
root.resizable(False, False)

BG = "#020817"
CARD = "#0f172a"
BLUE = "#1ea7ff"
TEXT = "#f8fafc"

# ======================================================
# HEADER
# ======================================================

header = tk.Frame(root, bg=BG)
header.pack(fill="x", pady=10)

tk.Label(
    header,
    text="SMART WASHING MACHINE",
    font=("Segoe UI", 30, "bold"),
    fg=BLUE,
    bg=BG
).pack()

tk.Label(
    header,
    text="HỆ THỐNG MÁY GIẶT THÔNG MINH SỬ DỤNG FUZZY LOGIC",
    font=("Segoe UI", 13),
    fg="#94a3b8",
    bg=BG
).pack()

# ======================================================
# MAIN
# ======================================================

main = tk.Frame(root, bg=BG)
main.pack(pady=10)

# ======================================================
# LEFT PANEL
# ======================================================

left = tk.Frame(
    main,
    bg=CARD,
    width=520,
    height=560
)

left.pack(side="left", padx=12)
left.pack_propagate(False)

tk.Label(
    left,
    text="THÔNG SỐ ĐẦU VÀO",
    font=("Segoe UI", 24, "bold"),
    fg="white",
    bg=CARD
).pack(pady=18)

# ======================================================
# KNOB FUNCTION
# ======================================================

def create_knob(parent, title, max_val, unit, y):

    frame = tk.Frame(parent, bg=CARD)
    frame.place(x=20, y=y)

    # LABEL
    tk.Label(
        frame,
        text=title,
        font=("Segoe UI", 15, "bold"),
        fg=TEXT,
        bg=CARD,
        width=12,
        justify="left"
    ).grid(row=0, column=0, padx=5)

    # CANVAS
    canvas = tk.Canvas(
        frame,
        width=120,
        height=120,
        bg=CARD,
        highlightthickness=0
    )

    canvas.grid(row=0, column=1)

    center = 60
    radius = 38

    value_var = tk.DoubleVar(value=0)

    # outer ring
    canvas.create_oval(
        8,8,112,112,
        outline=BLUE,
        width=3
    )

    # knob body
    canvas.create_oval(
        22,22,98,98,
        fill="#d1d5db",
        outline="#6b7280",
        width=3
    )

    # knob center
    canvas.create_oval(
        42,42,78,78,
        fill="#f8fafc",
        outline=""
    )

    # ticks
    for i in range(40):

        angle = math.radians(-90 + i*9)

        x1 = center + 47 * math.cos(angle)
        y1 = center + 47 * math.sin(angle)

        if i % 5 == 0:
            length = 8
            width = 2
        else:
            length = 4
            width = 1

        x2 = center + (47-length) * math.cos(angle)
        y2 = center + (47-length) * math.sin(angle)

        canvas.create_line(
            x1,y1,x2,y2,
            fill="white",
            width=width
        )

    # chỉ hiện số 0
    canvas.create_text(
        60,5,
        text="0",
        fill="white",
        font=("Arial",9,"bold")
    )

    # pointer
    pointer = canvas.create_line(
        center,
        center,
        center,
        24,
        fill=BLUE,
        width=4,
        capstyle="round"
    )

    # DISPLAY
    display = tk.Label(
        frame,
        text=f"0/{max_val}{unit}",
        font=("Consolas", 15, "bold"),
        fg=BLUE,
        bg="black",
        width=11
    )

    display.grid(row=0, column=2, padx=12)

    # ==================================================

    def update_knob(value):

        ratio = value / max_val

        angle_deg = -90 + ratio * 360

        angle = math.radians(angle_deg)

        x = center + radius * math.cos(angle)
        y = center + radius * math.sin(angle)

        canvas.coords(pointer, center, center, x, y)

        display.config(
            text=f"{round(value,1)}/{max_val}{unit}"
        )

    # lưu object
    value_var.update_knob = update_knob

    # ==================================================

    dragging = {"active": False}

    def click(event):
        dragging["active"] = True

    def release(event):
        dragging["active"] = False

    def rotate(event):

        if not dragging["active"]:
            return

        dx = event.x - center
        dy = event.y - center

        angle = math.degrees(math.atan2(dy, dx))

        angle += 90

        if angle < 0:
            angle += 360

        value = (angle / 360) * max_val

        value = round(value,1)

        value_var.set(value)

        update_knob(value)

    canvas.bind("<Button-1>", click)
    canvas.bind("<B1-Motion>", rotate)
    canvas.bind("<ButtonRelease-1>", release)

    return value_var

# ======================================================
# CREATE KNOBS
# ======================================================

khoiluong = create_knob(
    left,
    "KHỐI LƯỢNG\nTẢI",
    10,
    "kg",
    95
)

mucban = create_knob(
    left,
    "MỨC ĐỘ\nBẨN",
    100,
    "",
    235
)

loaivai = create_knob(
    left,
    "LOẠI\nVẢI",
    10,
    "",
    375
)

# ======================================================
# RIGHT PANEL
# ======================================================

right = tk.Frame(
    main,
    bg="#111827",
    width=620,
    height=560
)

right.pack(side="right", padx=12)
right.pack_propagate(False)

# ======================================================
# TOP BAR
# ======================================================

top = tk.Frame(
    right,
    bg="#1f2937",
    height=80
)

top.pack(fill="x")

# ======================================================
# POWER BUTTON
# ======================================================

power = tk.Canvas(
    top,
    width=60,
    height=60,
    bg="#1f2937",
    highlightthickness=0
)

power.place(x=22, y=10)

power.create_oval(
    8,8,52,52,
    fill="black",
    outline="#ef4444",
    width=3
)

power.create_text(
    30,30,
    text="⏻",
    fill="#ef4444",
    font=("Arial",18,"bold")
)

# ======================================================
# START BUTTON
# ======================================================

start_canvas = tk.Canvas(
    top,
    width=90,
    height=90,
    bg="#1f2937",
    highlightthickness=0
)

start_canvas.place(x=510, y=-4)

outer_btn = start_canvas.create_oval(
    8,8,82,82,
    fill="#0f172a",
    outline=BLUE,
    width=4
)

inner_btn = start_canvas.create_oval(
    22,22,68,68,
    fill="black",
    outline="#d1d5db",
    width=2
)

start_canvas.create_text(
    45,36,
    text="START",
    fill="white",
    font=("Segoe UI",11,"bold")
)

start_canvas.create_text(
    45,52,
    text="PAUSE",
    fill="white",
    font=("Segoe UI",8)
)

# ======================================================
# MACHINE BODY
# ======================================================

machine = tk.Canvas(
    right,
    width=620,
    height=260,
    bg="#111827",
    highlightthickness=0
)

machine.pack()

# outer ring
machine.create_oval(
    200,20,420,240,
    fill="#374151",
    outline="#9ca3af",
    width=6
)

# middle ring
machine.create_oval(
    228,48,392,212,
    fill="#0f172a",
    outline="#6b7280",
    width=5
)

# water center
machine.create_oval(
    250,70,370,190,
    fill="#0ea5e9",
    outline="#bae6fd",
    width=4
)

# light reflection
machine.create_arc(
    258,78,362,182,
    start=110,
    extent=70,
    style="arc",
    outline="#e0f2fe",
    width=5
)

# ======================================================
# OUTPUT
# ======================================================

bottom = tk.Frame(
    right,
    bg="#111827"
)

bottom.pack(fill="both", expand=True)

# TIME
time_frame = tk.Frame(bottom, bg="#111827")
time_frame.place(x=70, y=55)

tk.Label(
    time_frame,
    text="THỜI GIAN GIẶT",
    font=("Segoe UI",16,"bold"),
    fg=BLUE,
    bg="#111827"
).pack()

time_output = tk.Label(
    time_frame,
    text="0 phút",
    font=("Consolas",18,"bold"),
    fg=BLUE,
    bg="black",
    width=12,
    height=2
)

time_output.pack(pady=10)

# WATER
water_frame = tk.Frame(bottom, bg="#111827")
water_frame.place(x=355, y=55)

tk.Label(
    water_frame,
    text="LƯỢNG NƯỚC",
    font=("Segoe UI",16,"bold"),
    fg=BLUE,
    bg="#111827"
).pack()

water_output = tk.Label(
    water_frame,
    text="0 lít",
    font=("Consolas",18,"bold"),
    fg=BLUE,
    bg="black",
    width=12,
    height=2
)

water_output.pack(pady=10)

# ======================================================
# START FUNCTION
# ======================================================

running = False

def start_wash(event=None):

    global running

    kl = khoiluong.get()
    mb = mucban.get()
    lv = loaivai.get()

    # tính demo
    thoigian = round(25 + kl*3 + mb*0.3 + lv*2)
    nuoc = round(10 + kl*2 + lv)

    time_output.config(
        text=f"{thoigian} phút"
    )

    water_output.config(
        text=f"{nuoc} lít"
    )

    running = not running

    if running:

        start_canvas.itemconfig(
            outer_btn,
            fill="#22c55e"
        )

        start_canvas.itemconfig(
            inner_btn,
            fill="#14532d"
        )

    else:

        start_canvas.itemconfig(
            outer_btn,
            fill="#0f172a"
        )

        start_canvas.itemconfig(
            inner_btn,
            fill="black"
        )

start_canvas.bind("<Button-1>", start_wash)

# ======================================================
# RESET FUNCTION
# ======================================================

def reset_machine(event=None):

    global running

    running = False

    # reset output
    time_output.config(text="0 phút")
    water_output.config(text="0 lít")

    # reset start button
    start_canvas.itemconfig(
        outer_btn,
        fill="#0f172a"
    )

    start_canvas.itemconfig(
        inner_btn,
        fill="black"
    )

    # reset knobs
    khoiluong.set(0)
    mucban.set(0)
    loaivai.set(0)

    khoiluong.update_knob(0)
    mucban.update_knob(0)
    loaivai.update_knob(0)

# click nút đỏ để reset
power.bind("<Button-1>", reset_machine)

# ======================================================

root.mainloop()