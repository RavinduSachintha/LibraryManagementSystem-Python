# main.py

# imports
import config
import tkinter as tk
import backend
from tkinter import messagebox

################################################################
window = tk.Tk()
window.resizable(width=False, height=False)
window.geometry('{}x{}'.format(1000, 600))
window.wm_title(config.WINDOW_CONFIG['main_window_title'])

# frames
header_frame = tk.Frame(window, bg='lightgray', width=980, height=100, padx=5, pady=5)
center_frame = tk.Frame(window, bg='lightgray', width=980, height=500, padx=0, pady=0)
bottom_frame = tk.Frame(window, bg='lightgray', width=980, height=20, pady=5)

# layout all of the main containers
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

header_frame.grid(row=0, sticky="ew")
center_frame.grid(row=1, sticky="nsew")
bottom_frame.grid(row=2, sticky="ew")

# label for header frame
title_label = tk.Label(header_frame, text='Project title', font="Helvetica 30 bold", height=1, bg='lightgray')
title_label.pack(fill='x')

# create the center widgets
center_frame.grid_rowconfigure(0, weight=1)
center_frame.grid_columnconfigure(1, weight=1)

navigation_frame = tk.Frame(center_frame, bg='black', width=200, height=440, padx=5, pady=100)
content_frame = tk.Frame(center_frame, bg='green', width=800, height=440, padx=3, pady=3)

navigation_frame.grid(row=0, column=0, sticky="ns")
content_frame.grid(row=0, column=1, sticky="nsew")

# background image
image = tk.PhotoImage(file='background.gif')

#######################################################################

#######################################################################

# login frame
login_frame = tk.Frame(content_frame)
login_frame.place(x=0, y=0, relwidth=1, relheight=1)

# login frame background
login_bg_image_label = tk.Label(login_frame, image=image)
login_bg_image_label.place(x=0, y=0, relwidth=1, relheight=1)

# login_dialog_frame inside the login frame
login_dialog_frame = tk.Frame(login_frame, bg='gray', width=800, height=440, padx=10, pady=10)
login_dialog_frame.place(x=225, y=150)


# login page function
def login_page():
    # login components in home frame
    username_label = tk.Label(login_dialog_frame, text='Username', anchor='w', bg='gray')
    username_entry = tk.Entry(login_dialog_frame, width=30)
    password_label = tk.Label(login_dialog_frame, text='Password', anchor='w', bg='gray')
    password_entry = tk.Entry(login_dialog_frame, width=30, show='*')
    login_submit_button = tk.Button(login_dialog_frame, text='Log In', font='Helvetica 14 bold',
                                    command=lambda: login(username_entry.get(), password_entry.get()))

    username_label.grid(row=0, column=0, pady=3, padx=5)
    username_entry.grid(row=0, column=1, pady=3)
    password_label.grid(row=1, column=0, pady=3, padx=5)
    password_entry.grid(row=1, column=1, pady=3)
    login_submit_button.grid(row=2, columnspan=2, pady=10)

    # login function
    def login(username, password):
        res = (username == config.WINDOW_CONFIG['username'] and password == config.WINDOW_CONFIG['password'])
        if res:
            navigation_state_check(res)
            login_frame.place_forget()
            member_frame.place_forget()
            borrow_frame.place_forget()
            book_frame.place(x=0, y=0, relwidth=1, relheight=1)
            username_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            book_page()
        else:
            navigation_state_check(res)
            messagebox.showinfo("Access Denied", "You have entered wrong credentials.. Try again.")


#############################################################

#############################################################

# book frame
book_frame = tk.Frame(content_frame)
book_frame.place_forget()

# book frame background
book_bg_image_label = tk.Label(book_frame, image=image)
book_bg_image_label.place(x=0, y=0, relwidth=1, relheight=1)


def book_page():
    # frames
    book_search_frame = tk.Frame(book_frame, bg='sienna2', width=200, height=100)
    # book_list_frame = tk.Frame(book_frame, bg='gray', width=200, height=300)
    book_action_frame = tk.Frame(book_frame, bg='wheat3', width=200, height=200)

    book_search_frame.grid(row=0, sticky="ew", padx=(120, 0), pady=(50, 0))
    # book_list_frame.grid(row=2, sticky="nsew", padx=(120, 0), pady=(10, 0))
    book_action_frame.grid(row=1, sticky="ew", padx=(120, 0), pady=(10, 0))

    def get_all_data():
        book_list_frame = tk.Frame(book_frame, bg='gray', width=200, height=300)
        book_list_frame.grid(row=2, sticky="nsew", padx=(120, 0), pady=(10, 0))

        tk.Label(book_list_frame, text='BOOK ID', bg='gray', fg='white').grid(row=0, column=0, padx=5, pady=5)
        tk.Label(book_list_frame, text='ISBN NO', bg='gray', fg='white').grid(row=0, column=1, padx=5, pady=5)
        tk.Label(book_list_frame, text='BOOK NAME', bg='gray', fg='white').grid(row=0, column=2, padx=5, pady=5)
        tk.Label(book_list_frame, text='PUBLISHER', bg='gray', fg='white').grid(row=0, column=3, padx=5, pady=5)
        tk.Label(book_list_frame, text='BOOK COUNT', bg='gray', fg='white').grid(row=0, column=4, padx=5, pady=5)

        data = backend.select_all_books()
        for index, dat in enumerate(data):
            tk.Label(book_list_frame, text=dat[0], bg='gray', fg='black').grid(row=index + 1, column=0, padx=5, pady=5)
            tk.Label(book_list_frame, text=dat[1], bg='gray', fg='black').grid(row=index + 1, column=1, padx=5, pady=5)
            tk.Label(book_list_frame, text=dat[2], bg='gray', fg='black').grid(row=index + 1, column=2, padx=5, pady=5)
            tk.Label(book_list_frame, text=dat[3], bg='gray', fg='black').grid(row=index + 1, column=3, padx=5, pady=5)
            tk.Label(book_list_frame, text=dat[4], bg='gray', fg='black').grid(row=index + 1, column=4, padx=5, pady=5)

    def get_by_id(id):
        book_list_frame = tk.Frame(book_frame, bg='gray', width=200, height=300)
        book_list_frame.grid(row=2, sticky="nsew", padx=(120, 0), pady=(10, 0))

        tk.Label(book_list_frame, text='BOOK ID', bg='gray', fg='white').grid(row=0, column=0,padx=5, pady=5)
        tk.Label(book_list_frame, text='ISBN NO', bg='gray', fg='white').grid(row=0, column=1, padx=5, pady=5)
        tk.Label(book_list_frame, text='BOOK NAME', bg='gray', fg='white').grid(row=0, column=2, padx=5, pady=5)
        tk.Label(book_list_frame, text='PUBLISHER', bg='gray', fg='white').grid(row=0, column=3, padx=5, pady=5)
        tk.Label(book_list_frame, text='BOOK COUNT', bg='gray', fg='white').grid(row=0, column=4, padx=5, pady=5)

        data = backend.select_book_by_id(id)

        tk.Label(book_list_frame, text=data[0], bg='gray', fg='black').grid(row=1, column=0, padx=5, pady=5)
        tk.Label(book_list_frame, text=data[1], bg='gray', fg='black').grid(row=1, column=1, padx=5, pady=5)
        tk.Label(book_list_frame, text=data[2], bg='gray', fg='black').grid(row=1, column=2, padx=5, pady=5)
        tk.Label(book_list_frame, text=data[3], bg='gray', fg='black').grid(row=1, column=3, padx=5, pady=5)
        tk.Label(book_list_frame, text=data[4], bg='gray', fg='black').grid(row=1, column=4, padx=5, pady=5)

    # Search books
    search = tk.Entry(book_search_frame)
    search.grid(row=0, column=0, sticky="ew", padx=20, pady=5)
    search_button = tk.Button(book_search_frame, text='Search By ID', command=lambda: get_by_id(int(search.get())))
    search_button.grid(row=0, column=1, sticky="ew", padx=20, pady=5)
    view_button = tk.Button(book_search_frame, text='View All Books', command=lambda: get_all_data())
    view_button.grid(row=0, column=2, sticky="ew", padx=20, pady=5)

    # Insert book
    isbn_label = tk.Label(book_action_frame, text='ISBN NO : ', bg='wheat3')
    name_label = tk.Label(book_action_frame, text='BOOK NAME : ', bg='wheat3')
    publisher_label = tk.Label(book_action_frame, text='PUBLISHER ID : ', bg='wheat3')
    count_label = tk.Label(book_action_frame, text='BOOK COUNT : ', bg='wheat3')

    isbn_entry = tk.Entry(book_action_frame)
    name_entry = tk.Entry(book_action_frame)
    publisher_entry = tk.Entry(book_action_frame)
    count_entry = tk.Entry(book_action_frame)

    # clear function
    def clear():
        isbn_entry.delete(0, 'end')
        name_entry.delete(0, 'end')
        publisher_entry.delete(0, 'end')
        count_entry.delete(0, 'end')

    def insert_book(isbn, name, publisher, count):
        backend.insert_book(isbn, name, publisher, count)
        get_all_data()
        clear()

    submit_button = tk.Button(book_action_frame, text='Insert Book', width=40,
                              command=lambda: insert_book(isbn_entry.get(), name_entry.get(),
                                                          int(publisher_entry.get()),
                                                          int(count_entry.get())))

    isbn_label.grid(row=0, column=0, padx=20, pady=(10, 3))
    name_label.grid(row=1, column=0, padx=20, pady=3)
    publisher_label.grid(row=2, column=0, padx=20, pady=3)
    count_label.grid(row=3, column=0, padx=20, pady=3)
    isbn_entry.grid(row=0, column=1, padx=20, pady=(10, 3))
    name_entry.grid(row=1, column=1, padx=20, pady=3)
    publisher_entry.grid(row=2, column=1, padx=20, pady=3)
    count_entry.grid(row=3, column=1, padx=20, pady=3)
    submit_button.grid(row=4, columnspan=2, pady=5, padx=30)

    get_all_data()


############################################################

#############################################################

# member frame
member_frame = tk.Frame(content_frame)
member_frame.place_forget()

# member frame background
member_bg_image_label = tk.Label(member_frame, image=image)
member_bg_image_label.place(x=0, y=0, relwidth=1, relheight=1)


def member_page():
    # frames
    member_search_frame = tk.Frame(member_frame, bg='sienna2', width=200, height=100)
    # member_list_frame = tk.Frame(member_frame, bg='gray', width=200, height=300)
    member_action_frame = tk.Frame(member_frame, bg='wheat3', width=200, height=200)

    member_search_frame.grid(row=0, sticky="ew", padx=(50, 0), pady=(50, 0))
    # member_list_frame.grid(row=2, sticky="nsew", padx=(50, 0), pady=(10, 0))
    member_action_frame.grid(row=1, sticky="ew", padx=(50, 0), pady=(10, 0))

    def get_all_data():
        member_list_frame = tk.Frame(member_frame, bg='gray', width=200, height=300)
        member_list_frame.grid(row=2, sticky="nsew", padx=(50, 0), pady=(10, 0))

        tk.Label(member_list_frame, text='MEMBER ID', bg='gray', fg='white').grid(row=0, column=0, padx=5, pady=5)
        tk.Label(member_list_frame, text='NAME', bg='gray', fg='white').grid(row=0, column=1, padx=5, pady=5)
        tk.Label(member_list_frame, text='TYPE', bg='gray', fg='white').grid(row=0, column=2, padx=5, pady=5)
        tk.Label(member_list_frame, text='ADDRESS', bg='gray', fg='white').grid(row=0, column=3, padx=5, pady=5)
        tk.Label(member_list_frame, text='PHONE', bg='gray', fg='white').grid(row=0, column=4, padx=5, pady=5)
        tk.Label(member_list_frame, text='EMAIL', bg='gray', fg='white').grid(row=0, column=5, padx=5, pady=5)

        data = backend.select_all_members()
        for index, dat in enumerate(data):
            tk.Label(member_list_frame, text=dat[0], bg='gray', fg='black').grid(row=index + 1, column=0, padx=5,
                                                                                 pady=5)
            tk.Label(member_list_frame, text=dat[1], bg='gray', fg='black').grid(row=index + 1, column=1, padx=5,
                                                                                 pady=5)
            tk.Label(member_list_frame, text=dat[2], bg='gray', fg='black').grid(row=index + 1, column=2, padx=5,
                                                                                 pady=5)
            tk.Label(member_list_frame, text=dat[3], bg='gray', fg='black').grid(row=index + 1, column=3, padx=5,
                                                                                 pady=5)
            tk.Label(member_list_frame, text=dat[4], bg='gray', fg='black').grid(row=index + 1, column=4, padx=5,
                                                                                 pady=5)
            tk.Label(member_list_frame, text=dat[5], bg='gray', fg='black').grid(row=index + 1, column=5, padx=5,
                                                                                 pady=5)

    def get_by_id(id):
        member_list_frame = tk.Frame(member_frame, bg='gray', width=200, height=300)
        member_list_frame.grid(row=2, sticky="nsew", padx=(50, 0), pady=(10, 0))

        tk.Label(member_list_frame, text='MEMBER ID', bg='gray', fg='white').grid(row=0, column=0, padx=5, pady=5)
        tk.Label(member_list_frame, text='NAME', bg='gray', fg='white').grid(row=0, column=1, padx=5, pady=5)
        tk.Label(member_list_frame, text='TYPE', bg='gray', fg='white').grid(row=0, column=2, padx=5, pady=5)
        tk.Label(member_list_frame, text='ADDRESS', bg='gray', fg='white').grid(row=0, column=3, padx=5, pady=5)
        tk.Label(member_list_frame, text='PHONE', bg='gray', fg='white').grid(row=0, column=4, padx=5, pady=5)
        tk.Label(member_list_frame, text='EMAIL', bg='gray', fg='white').grid(row=0, column=5, padx=5, pady=5)

        data = backend.select_member_by_id(id)

        tk.Label(member_list_frame, text=data[0], bg='gray', fg='black').grid(row=1, column=0, padx=5,
                                                                              pady=5)
        tk.Label(member_list_frame, text=data[1], bg='gray', fg='black').grid(row=1, column=1, padx=5,
                                                                              pady=5)
        tk.Label(member_list_frame, text=data[2], bg='gray', fg='black').grid(row=1, column=2, padx=5,
                                                                              pady=5)
        tk.Label(member_list_frame, text=data[3], bg='gray', fg='black').grid(row=1, column=3, padx=5,
                                                                              pady=5)
        tk.Label(member_list_frame, text=data[4], bg='gray', fg='black').grid(row=1, column=4, padx=5,
                                                                              pady=5)
        tk.Label(member_list_frame, text=data[5], bg='gray', fg='black').grid(row=1, column=5, padx=5,
                                                                              pady=5)

    # Search books
    search = tk.Entry(member_search_frame)
    search.grid(row=0, column=0, sticky="ew", padx=20, pady=5)
    search_button = tk.Button(member_search_frame, text='Search By ID', command=lambda: get_by_id(int(search.get())))
    search_button.grid(row=0, column=1, sticky="ew", padx=20, pady=5)
    view_button = tk.Button(member_search_frame, text='View All Books', command=lambda: get_all_data())
    view_button.grid(row=0, column=2, sticky="ew", padx=20, pady=5)

    # Insert member
    name_label = tk.Label(member_action_frame, text='NAME : ', bg='wheat3')
    type_label = tk.Label(member_action_frame, text='TYPE : ', bg='wheat3')
    address_label = tk.Label(member_action_frame, text='ADDRESS : ', bg='wheat3')
    phone_label = tk.Label(member_action_frame, text='PHONE : ', bg='wheat3')
    email_label = tk.Label(member_action_frame, text='EMAIL : ', bg='wheat3')

    name_entry = tk.Entry(member_action_frame)
    type_entry = tk.Entry(member_action_frame)
    address_entry = tk.Entry(member_action_frame)
    phone_entry = tk.Entry(member_action_frame)
    email_entry = tk.Entry(member_action_frame)

    # clear function
    def clear():
        name_entry.delete(0, 'end')
        type_entry.delete(0, 'end')
        address_entry.delete(0, 'end')
        phone_entry.delete(0, 'end')
        email_entry.delete(0, 'end')

    def insert_member(name, type, address, phone, email):
        backend.insert_member(name, type, address, phone, email)
        get_all_data()
        clear()

    submit_button = tk.Button(member_action_frame, text='Insert Member',
                              command=lambda: insert_member(name_entry.get(), type_entry.get(), address_entry.get(),
                                                            phone_entry.get(), email_entry.get()))

    name_label.grid(row=0, column=0, padx=20, pady=(10, 3))
    type_label.grid(row=1, column=0, padx=20, pady=3)
    address_label.grid(row=2, column=0, padx=20, pady=3)
    phone_label.grid(row=3, column=0, padx=20, pady=3)
    email_label.grid(row=4, column=0, padx=20, pady=3)
    name_entry.grid(row=0, column=1, padx=20, pady=(10, 3))
    type_entry.grid(row=1, column=1, padx=20, pady=3)
    address_entry.grid(row=2, column=1, padx=20, pady=3)
    phone_entry.grid(row=3, column=1, padx=20, pady=3)
    email_entry.grid(row=4, column=1, padx=20, pady=3)
    submit_button.grid(row=5, columnspan=2, pady=5, padx=30)

    get_all_data()


############################################################

#############################################################

# borrow frame
borrow_frame = tk.Frame(content_frame)
borrow_frame.place_forget()

# borrow frame background
borrow_bg_image_label = tk.Label(borrow_frame, image=image)
borrow_bg_image_label.place(x=0, y=0, relwidth=1, relheight=1)


def borrow_page():
    # frames
    borrow_search_frame = tk.Frame(borrow_frame, bg='sienna2', width=200, height=100)
    borrow_list_frame = tk.Frame(borrow_frame, bg='gray', width=200, height=300)
    borrow_action_frame = tk.Frame(borrow_frame, bg='wheat3', width=200, height=200)

    borrow_search_frame.grid(row=0, sticky="ew", padx=(50, 0), pady=(50, 0))
    borrow_list_frame.grid(row=2, sticky="nsew", padx=(50, 0), pady=(10, 0))
    borrow_action_frame.grid(row=1, sticky="ew", padx=(50, 0), pady=(10, 0))

    def get_all_data():
        tk.Label(borrow_list_frame, text='ID', bg='gray', fg='white').grid(row=0, column=0, padx=5, pady=5)
        tk.Label(borrow_list_frame, text='BOOK', bg='gray', fg='white').grid(row=0, column=1, padx=5, pady=5)
        tk.Label(borrow_list_frame, text='MEMBER', bg='gray', fg='white').grid(row=0, column=2, padx=5, pady=5)
        tk.Label(borrow_list_frame, text='ISSUED DATE', bg='gray', fg='white').grid(row=0, column=3, padx=5, pady=5)
        tk.Label(borrow_list_frame, text='DUE DATE', bg='gray', fg='white').grid(row=0, column=4, padx=5, pady=5)
        tk.Label(borrow_list_frame, text='RETURNED DATE', bg='gray', fg='white').grid(row=0, column=5, padx=5, pady=5)

        data = backend.select_all_borrowings()
        for index, dat in enumerate(data):
            tk.Label(borrow_list_frame, text=dat[0], bg='gray', fg='black').grid(row=index + 1, column=0, padx=5,
                                                                                 pady=5)
            tk.Label(borrow_list_frame, text=dat[1], bg='gray', fg='black').grid(row=index + 1, column=1, padx=5,
                                                                                 pady=5)
            tk.Label(borrow_list_frame, text=dat[2], bg='gray', fg='black').grid(row=index + 1, column=2, padx=5,
                                                                                 pady=5)
            tk.Label(borrow_list_frame, text=dat[3], bg='gray', fg='black').grid(row=index + 1, column=3, padx=5,
                                                                                 pady=5)
            tk.Label(borrow_list_frame, text=dat[4], bg='gray', fg='black').grid(row=index + 1, column=4, padx=5,
                                                                                 pady=5)
            tk.Label(borrow_list_frame, text=dat[5], bg='gray', fg='black').grid(row=index + 1, column=5, padx=5,
                                                                                 pady=5)

    # Update borrowing
    updating_book_id_label = tk.Label(borrow_search_frame, text='BOOK ID : ', bg='sienna2')
    return_date_label = tk.Label(borrow_search_frame, text='RETURNED DATE : ', bg='sienna2')

    updating_book_id_entry = tk.Entry(borrow_search_frame)
    return_date_entry = tk.Entry(borrow_search_frame)

    # Insert borrowing
    book_id_label = tk.Label(borrow_action_frame, text='BOOK ID : ', bg='wheat3')
    mem_id_label = tk.Label(borrow_action_frame, text='MEMBER ID : ', bg='wheat3')
    issued_date_label = tk.Label(borrow_action_frame, text='ISSUED DATE : ', bg='wheat3')
    due_date_label = tk.Label(borrow_action_frame, text='DUE DATE : ', bg='wheat3')

    book_id_entry = tk.Entry(borrow_action_frame)
    mem_id_entry = tk.Entry(borrow_action_frame)
    issued_date_entry = tk.Entry(borrow_action_frame)
    due_date_entry = tk.Entry(borrow_action_frame)

    # clear function
    def clear():
        book_id_entry.delete(0, 'end')
        mem_id_entry.delete(0, 'end')
        issued_date_entry.delete(0, 'end')
        due_date_entry.delete(0, 'end')

    def insert_borrowing(book_id, mem_id, issued_date, due_date):
        backend.insert_borrowing(book_id, mem_id, issued_date, due_date)
        get_all_data()
        clear()

    def update_borrowing(book_id, return_date):
        backend.update_borrowing(book_id, return_date)
        get_all_data()
        clear()

    submit_button = tk.Button(borrow_action_frame, text='Borrow A Book',
                              command=lambda: insert_borrowing(int(book_id_entry.get()), int(mem_id_entry.get()),
                                                               issued_date_entry.get(),
                                                               due_date_entry.get()))

    update_button = tk.Button(borrow_search_frame, text='Return A Book',
                              command=lambda: update_borrowing(int(updating_book_id_entry.get()),
                                                               return_date_entry.get()))

    book_id_label.grid(row=0, column=0, padx=20, pady=(10, 3))
    mem_id_label.grid(row=1, column=0, padx=20, pady=3)
    issued_date_label.grid(row=2, column=0, padx=20, pady=3)
    due_date_label.grid(row=3, column=0, padx=20, pady=3)
    book_id_entry.grid(row=0, column=1, padx=20, pady=(10, 3))
    mem_id_entry.grid(row=1, column=1, padx=20, pady=3)
    issued_date_entry.grid(row=2, column=1, padx=20, pady=3)
    due_date_entry.grid(row=3, column=1, padx=20, pady=3)
    submit_button.grid(row=5, columnspan=2, pady=5, padx=30)

    updating_book_id_label.grid(row=0, column=0, padx=5, pady=5)
    return_date_label.grid(row=0, column=2, padx=5, pady=5)
    updating_book_id_entry.grid(row=0, column=1, padx=5, pady=5)
    return_date_entry.grid(row=0, column=3, padx=5, pady=5)
    update_button.grid(row=0, column=4, padx=5, pady=5)

    get_all_data()


############################################################


def click_books(log_state):
    if log_state:
        login_frame.place_forget()
        member_frame.place_forget()
        borrow_frame.place_forget()
        book_frame.place(x=0, y=0, relwidth=1, relheight=1)
        book_page()


def click_members(log_state):
    if log_state:
        login_frame.place_forget()
        book_frame.place_forget()
        borrow_frame.place_forget()
        member_frame.place(x=0, y=0, relwidth=1, relheight=1)
        member_page()


def click_borrows(log_state):
    if log_state:
        login_frame.place_forget()
        book_frame.place_forget()
        member_frame.place_forget()
        borrow_frame.place(x=0, y=0, relwidth=1, relheight=1)
        borrow_page()


def click_logout(log_state):
    if log_state:
        book_frame.place_forget()
        member_frame.place_forget()
        borrow_frame.place_forget()
        login_frame.place(x=0, y=0, relwidth=1, relheight=1)


# buttons for navigation frame
book_button = tk.Button(navigation_frame, text='Book Details', font='Helvetica 16', anchor='w', bg='black',
                        fg='white', borderwidth=0, command=lambda: click_books(False))
member_button = tk.Button(navigation_frame, text='Member Details', font='Helvetica 16', anchor='w', bg='black',
                          fg='white', borderwidth=0, command=lambda: click_members(False))
borrow_button = tk.Button(navigation_frame, text='Borrowing Details', font='Helvetica 16', anchor='w', bg='black',
                          fg='white', borderwidth=0, command=lambda: click_borrows(False))
logout_button = tk.Button(navigation_frame, text='Log Out', font='Helvetica 16', anchor='w', bg='black', fg='white',
                          borderwidth=0, command=lambda: click_logout(False))

book_button.grid(row=1, column=0, sticky="ew")
member_button.grid(row=2, column=0, sticky="ew")
borrow_button.grid(row=3, column=0, sticky="ew")
logout_button.grid(row=4, column=0, sticky="ew")


def navigation_state_check(log_state):
    if log_state:
        book_button['state'] = 'normal'
        member_button['state'] = 'normal'
        borrow_button['state'] = 'normal'
        logout_button['state'] = 'normal'
        book_button['command'] = lambda: click_books(log_state)
        member_button['command'] = lambda: click_members(log_state)
        borrow_button['command'] = lambda: click_borrows(log_state)
        logout_button['command'] = lambda: click_logout(log_state)
    else:
        book_button['state'] = 'disabled'
        member_button['state'] = 'disabled'
        borrow_button['state'] = 'disabled'
        logout_button['state'] = 'disabled'


navigation_state_check(False)
login_page()

# main window loop
window.mainloop()
