from tkinter import *
from PIL import ImageTk, Image

root = Tk()

# Adjust size
root.geometry("1200x800")
root.minsize(1200, 800)
root.resizable(1, 1)
root.title("Học tiếng anh điiii")
root.configure(background="#ffffff")

# Create the main frame for the window GUI
main_frame = Frame(root)
main_frame.pack(expand=True, fill=BOTH)

# Create the main canvas for holding everything inside GUI
main_canvas = Canvas(main_frame)
main_canvas.pack(side=TOP, fill=BOTH, expand=1)
main_canvas.configure(cursor="circle #FF00FF")

# Create the header text for the product's name


def turn_on_home_page():
    # forget unused canvas
    vocab_page.place_forget()
    daily_task_page.place_forget()
    ielts_page.place_forget()
    home_page.place(relx=0.0, rely=0, relheight=1, relwidth=1)


def turn_on_vocab_page():
    # forget unused canvas
    home_page.place_forget()
    daily_task_page.place_forget()
    ielts_page.place_forget()
    input_area.place(relx=0.0, rely=0.0, relheight=1, relwidth=0.41)
    # viet_label.place_forget()
    vocab_page.place(relx=0.0, rely=0, relheight=1, relwidth=1)


def turn_on_daily_task_page():
    # forget unused canvas
    vocab_page.place_forget()
    home_page.place_forget()
    ielts_page.place_forget()
    daily_task_page.place(relx=0.0, rely=0, relheight=1, relwidth=1)


def turn_on_ielts_page():
    # forget unused canvas
    vocab_page.place_forget()
    daily_task_page.place_forget()
    home_page.place_forget()
    ielts_page.place(relx=0.0, rely=0, relheight=1, relwidth=1)

# page declaration
home_page = None
vocab_page = None
daily_task_page = None
ielts_page = None

# function to create a single nav button
def create_nav_button(nav_bar, x, y, text_string, command):
    nav_button = Button(nav_bar)
    nav_button.place(relx=x, rely=y, relheight=1, relwidth=1/4)
    nav_button.configure(activebackground="black", activeforeground="pink", background="#F7A7A6",
                         foreground="#5E4388", highlightcolor="black", pady="0", text=text_string,
                         font="-family {Comic Sans MS} -size 12 -weight bold", command=command)
    return nav_button

# function to create a single page
def create_page(main_canvas, text_string, current_page):
    page = Canvas(main_canvas, bg="white")
    page.place(relx=0.0, rely=0.0, relheight=1, relwidth=1.0)
    header = Canvas(page, bg="white")
    header.place(relx=0.0, rely=0.0, relheight=0.2, relwidth=1.0)
    # header text
    header_text = Label(header)
    header_text.place(relx=0.0, rely=0.0, relheight=0.75, relwidth=1.0)
    header_text.configure(background="#5E4388", anchor="c", font="-family {Comic Sans MS} -size 60 -weight bold",
                          foreground="#F7A7A6", text=text_string)
    # nav bar
    nav_bar = Canvas(header)
    nav_bar.place(relx=0.0, rely=0.75, relheight=0.25, relwidth=1.0)
    main_menu_nav_button = create_nav_button(
        nav_bar, 0, 0, "MAIN MENU", turn_on_home_page)
    vocab_nav_button = create_nav_button(
        nav_bar, 1/4, 0, "VOCABULARY", turn_on_vocab_page)
    daily_task_nav_button = create_nav_button(
        nav_bar, 1/2, 0, "DAILY TASK", turn_on_daily_task_page)
    ielts_nav_button = create_nav_button(
        nav_bar, 3/4, 0, "IELTS", turn_on_ielts_page)
    if current_page == "menu":
        main_menu_nav_button.configure(
            background="#5E4388", foreground="#F7A7A6")
    elif current_page == "vocab":
        vocab_nav_button.configure(background="#5E4388", foreground="#F7A7A6")
    elif current_page == "task":
        daily_task_nav_button.configure(
            background="#5E4388", foreground="#F7A7A6")
    elif current_page == "ielts":
        ielts_nav_button.configure(background="#5E4388", foreground="#F7A7A6")
    return page

# page initialization
home_page = create_page(main_canvas, "MAIN MENU", "menu")
vocab_page = create_page(main_canvas, "VOCABULARY", "vocab")
daily_task_page = create_page(main_canvas, "DAILY TASKS", "task")
ielts_page = create_page(main_canvas, "IELTS", "ielts")

''' Main Menu '''
# main menu body
home_page_body = Canvas(home_page, bg="#CBCAE6")
home_page_body.place(relx=0.0, rely=0.2, relheight=0.8, relwidth=1.0)

# function to create big button in main menu page
def create_big_button(home_page_body, x, y, text_string, command):
    # test_query_button_photo = PhotoImage(
    #     file="Pictures/QueryManagement.png")
    # test_query_button_photoImage = test_query_button_photo.subsample(
    #     1, 1)
    big_button = Button(home_page_body)
    # big_button = Button(
    #     main, image=test_query_button_photoImage, compound=BOTTOM)
    big_button.place(relx=x, rely=y, relheight=0.35, relwidth=0.35)
    big_button.configure(activebackground="#0052A0", activeforeground="white", background="#F7A7A6",
                         foreground="black", highlightcolor="black", pady="0", text=text_string,
                         font="-family {Comic Sans MS} -size 18 -weight bold", command=command)

# big button initialization
main_menu_big_button = create_big_button(
    home_page_body, 0.1, 0.1, "MAIN MENU", turn_on_home_page)
vocab_big_button = create_big_button(
    home_page_body, 0.55, 0.1, "VOCABULARY", turn_on_vocab_page)
daily_task_big_button = create_big_button(
    home_page_body, 0.1, 0.55, "DAILY TASK", turn_on_daily_task_page)
ielts_big_button = create_big_button(
    home_page_body, 0.55, 0.55, "IELTS", turn_on_ielts_page)

''' Vocabulary page '''
# vocab page body
vocab_page_body = Canvas(vocab_page, bg="#CBCAE6")
vocab_page_body.place(relx=0.0, rely=0.2, relheight=0.8, relwidth=1.0)

# input area in vocab page
input_area = Canvas(vocab_page_body, bg="#CBCAE6")
input_area.place(relx=0.0, rely=0.0, relheight=1, relwidth=0.41)

input_area_header = Label(input_area, text="Vocabulary",
                          bd=0, relief=RIDGE, anchor=CENTER)
input_area_header.place(relx=0.01, rely=0.01, relheight=0.07, relwidth=0.98)
input_area_header.configure(
    font="-family {Comic Sans MS} -size 24 -weight bold", bg="#CBCAE6", foreground="#000000")

input_label = Label(input_area, text="Type your word: ")
input_label.place(relx=0.01, rely=0.1, relheight=0.05, relwidth=0.3)
input_label.configure(
    font="-family {Comic Sans MS} -size 12", background="#CBCAE6", foreground="#000000", anchor = W)

vocab_input = Entry(input_area)
vocab_input.place(relx=0.3, rely=0.1, relheight=0.05, relwidth=0.5)

# dictionary initialization (vocab page)
architecture_vocab_eng_list = ["architect", "architectural",
                  "architecture", "air conditioning", "animation"]
architecture_vocab_viet_list = ["kiến trúc sư", "thuộc kiến trúc",
                   "kiến trúc", "điều hòa không khí", "hoạt ảnh"]

# scroll bar initialization (vocab page)
scrollbar = Scrollbar(input_area)
scrollbar.place(relx=0.9, rely=0.2, relheight=0.7, relwidth=0.05)

# function to get the vocab list based on search option
def get_value():
    search_vocab_eng_list = []
    search_text = vocab_input.get()
    for text in architecture_vocab_eng_list:
        if search_text in text:
            search_vocab_eng_list.append(text)

    vocab_list = Listbox(input_area, yscrollcommand=scrollbar.set)
    for word in search_vocab_eng_list:
        vocab_list.insert(END, word)
    vocab_list.place(relx=0.02, rely=0.2, relheight=0.7, relwidth=0.88)

# vocab search button (will display a new Listbox)
vocab_input_button = Button(input_area, text="Search",
                            command=get_value, font="-family {Comic Sans MS} -size 9")
vocab_input_button.place(relx=0.85, rely=0.1, relheight=0.05, relwidth=0.1)

# listbox initialization for the first time
vocab_list = Listbox(input_area, yscrollcommand=scrollbar.set)
for word in architecture_vocab_eng_list:
    vocab_list.insert(END, word)
vocab_list.place(relx=0.02, rely=0.2, relheight=0.7, relwidth=0.88)

# display area in vocab page
display_area = Canvas(vocab_page_body, bg="#CBCAE6")
display_area.place(relx=0.4, rely=0.0, relheight=1, relwidth=0.6)

# function to display vietnamese word and image for the chosen english word
def translate():
    try:
        eng_word = vocab_list.selection_get()
        index = architecture_vocab_eng_list.index(eng_word)
        viet_word = architecture_vocab_eng_list[index]
        viet_label = Label(display_area, text=viet_word,
                           font="-family {Comic Sans MS} -size 12")
        viet_label.place(relx=0.2, rely=0.8, relheight=0.1, relwidth=0.6)
        img_path = str(index) + ".png"
        vocab_img_canvas = Canvas(display_area, bg='pink')
        vocab_img_canvas.place(relx=0.2, rely=0.1, relheight=0.6, relwidth=0.6)
        img = ImageTk.PhotoImage(Image.open(img_path))
        vocab_img_canvas.create_image(anchor=NW, image=img)
        vocab_img_canvas.image = img
    except:
        pass

# translate button (vocab page)
translate_button = Button(input_area, text="Translate",
                          command=translate, font="-family {Comic Sans MS} -size 9")
translate_button.place(relx=0.8, rely=0.93, relheight=0.05, relwidth=0.15)
# config between Listbox and scrollbar
scrollbar.config(command=vocab_list.yview)

'''Daily-tasks page'''
# dailytask page body
dailytask_page_body = Canvas(daily_task_page, bg="#CBCAE6")
dailytask_page_body.place(relx=0.0, rely=0.2, relheight=0.8, relwidth=1.0)

# dailytask selection area
dailytask_selection_area = Canvas(dailytask_page_body, bg="#CBCAE6")
dailytask_selection_area.place(relx=0.0, rely=0.0, relheight=1, relwidth=0.31)

# dailytask display area
dailytask_display_area = Canvas(dailytask_page_body, bg="#CBCAE6")
dailytask_display_area.place(relx=0.3, rely=0.0, relheight=1, relwidth=0.7)

# setting area (in selection area)
dailytask_setting_area = Canvas(dailytask_selection_area, bg="#CBCAE6")
dailytask_setting_area.place(relx=0.0, rely=0.0, relheight=0.41, relwidth=1)

# customization area (in selection area)
dailytask_customization_area = Canvas(dailytask_selection_area, bg="#CBCAE6")
dailytask_customization_area.place(relx=0.0, rely=0.4, relheight=0.6, relwidth=1)

# setting area header
dailytask_setting_area_header = Label(
    dailytask_setting_area, text="Setting", bd=0, relief=RIDGE, anchor=CENTER, 
    font="-family {Comic Sans MS} -size 24 -weight bold", bg="#CBCAE6", foreground="#000000")
dailytask_setting_area_header.place(
    relx=0.01, rely=0.01, relheight=0.18, relwidth=0.98)

eng_chosen_dictionary = []
viet_chosen_dictionary = []
number_of_ques = 0

# dictionary selection
### label
dictionary_selection_label = Label(
    dailytask_setting_area, text="Select your dictionary:", bd=0, relief=RIDGE, anchor=W, 
    font="-family {Comic Sans MS} -size 12", bg="#CBCAE6", foreground="#000000")
dictionary_selection_label.place(
    relx=0.01, rely=0.25, relheight=0.15, relwidth=0.5)

### option menu
dictionary_options = ['Architecture dictionary', 'IELTS dictionary']
dictionary_value = StringVar()
dictionary_value.set('Choose your dictionary')
dictionary_selection_dropdownlist = OptionMenu(dailytask_setting_area, dictionary_value, *dictionary_options)
dictionary_selection_dropdownlist.place(relx=0.5, rely=0.25, relheight=0.15, relwidth=0.45)

# number of ques selection
### label
number_of_ques_label = Label(
    dailytask_setting_area, text="Number of questions:", bd=0, relief=RIDGE, anchor=W, 
    font="-family {Comic Sans MS} -size 12", bg="#CBCAE6", foreground="#000000")
number_of_ques_label.place(
    relx=0.01, rely=0.5, relheight=0.15, relwidth=0.5)

### option menu
number_of_ques_options = []
for i in range(1, 21):
    number_of_ques_options.append(i)
number_of_ques_value = StringVar()
number_of_ques_value.set('Number of questions')
number_of_ques_dropdownlist = OptionMenu(dailytask_setting_area, number_of_ques_value, *number_of_ques_options)
number_of_ques_dropdownlist.place(relx=0.5, rely=0.5, relheight=0.15, relwidth=0.45)

# function to get all setting value from user
def get_setting():
    if dictionary_value.get() == 'Architecture dictionary':
        eng_chosen_dictionary = architecture_vocab_eng_list.copy()
        viet_chosen_dictionary = architecture_vocab_viet_list
    else:
        pass
    number_of_ques = int(number_of_ques_value.get())

# button to generate quiz (based on above setting)
dailytask_selection_setting_generate_button = Button(dailytask_setting_area, text="Generate quiz",
                        font="-family {Comic Sans MS} -size 12", command = get_setting)
dailytask_selection_setting_generate_button.place(relx=0.5, rely=0.75, relheight=0.15, relwidth=0.45)

turn_on_home_page()
root.mainloop()
