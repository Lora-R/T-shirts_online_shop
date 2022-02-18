import tkinter as tk
from tkinter import *
from log_reg_service import register, login
from product_service import get_products, buy_product
from PIL import ImageTk, Image


def clear_window(window):
    for el in window.pack_slaves():
        el.destroy()


def render_product_screen(window):
    clear_window(window)

    main_frame = Frame(window)
    main_frame.pack(fill=BOTH, expand=1)
    main_frame.columnconfigure(0, weight=10)

    canvas = Canvas(main_frame)
    canvas.pack(side=LEFT, fill=BOTH, expand=1)

    vsbar = tk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    vsbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=vsbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    second_frame = Frame(canvas)
    canvas.create_window((0,0), window=second_frame, anchor='nw')

    row = 0
    col = 0
    products = get_products()

    for product in products:
        if col == 2:
            col = 0
            row += 4
        tk.Label(second_frame, text=f"'{product['name']}'", font=('Helvetica', 15, 'bold')).pack(padx=10, pady=20)

        image = Image.open(f"./db/images/{product['img']}")
        image_resize = image.resize((650, 900))
        photo = ImageTk.PhotoImage(image_resize)

        image_label = tk.Label(second_frame, image=photo)
        image_label.image = photo
        image_label.pack(padx=10, pady=5)

        tk.Label(second_frame, text=f"Price: {product['price']}", font=('Helvetica', 11, 'bold')).pack(padx=10, pady=5)
        tk.Button(second_frame, text='Buy', font=('Helvetica', 18, 'bold'), height=1, width=30,
                  command=lambda b=product['id']: buy_product(b)

                  ).pack(padx=10, pady=5)

        tk.Label(second_frame, text="  *  *  *  ").pack(padx=10, pady=30)
        col += 1

def render_login_page(window):
    clear_window(window)

    tk.Label(window, text='User: ').pack(padx=10, pady=10)
    username = tk.Entry()
    username.pack(padx=10, pady=10)

    tk.Label(window, text='Password: ').pack(padx=10, pady=10)
    password = tk.Entry(show="*")
    password.pack(padx=10, pady=10)

    def get_login_info(window):
        username_info = username.get()
        password_info = password.get()
        result = login(username_info, password_info)
        if result:
            render_product_screen(window)
        else:
            tk.Label(window,
                     text="Invalid Credentials!",
                     fg="red"
                     ).pack(padx=10, pady=10)

    tk.Button(
        window,
        text="Login",
        bg="green",
        fg="black",
        height=2, width=20,
        command=lambda: get_login_info(window)
    ).pack(padx=10, pady=10)


def render_main_screen(window):
    tk.Button(
        window,
        text="Login",
        bg="green",
        fg="white",
        height=2, width=20,
        command=lambda: render_login_page(window)
    ).pack(padx=10, pady=10)

    tk.Button(
        window,
        text="Register",
        bg="yellow",
        fg="black",
        height=2, width=20,
        command=lambda: render_register_screen(window)
    ).pack(padx=10, pady=10)


def render_register_screen(window):
    clear_window(window)

    tk.Label(window, text='User: ').pack(padx=10, pady=10)
    username = tk.Entry()
    username.pack(padx=10, pady=10)

    tk.Label(window, text='Email: ').pack(padx=10, pady=10)
    email = tk.Entry()
    email.pack(padx=10, pady=10)

    tk.Label(window, text='Password: ').pack(padx=10, pady=10)
    password = tk.Entry(show="*")
    password.pack(padx=10, pady=10)

    def get_info():
        username_info = username.get()
        email_info = email.get()
        password_info = password.get()
        product = []
        result = register(username_info, email_info, password_info, product)
        if result:
            render_login_page(window)

    tk.Button(
        window,
        text="Register",
        bg="green",
        fg="black",
        height=2, width=20,
        command=lambda: get_info()
    ).pack(padx=10, pady=10)
