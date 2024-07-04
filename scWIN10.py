import time
from PIL import Image
from pynput.keyboard import Key, Controller as kc
import customtkinter
from customtkinter import *

Keyboard = kc()


def press(key):
    Keyboard.press(key)
    Keyboard.release(key)


def t(t):
    time.sleep(t)


def dw_clean():

    with Keyboard.pressed(Key.cmd):
        press('e')

    t(1)

    for x in range(0, 5):
        t(0.4)
        press(Key.tab)

    t(0.8)

    press(Key.down)

    t(0.8)

    press(Key.enter)

    t(0.8)

    press(Key.tab)

    t(0.8)

    for x in range(0, 4):
        t(0.4)
        press(Key.down)

    t(0.8)

    press(Key.enter)

    t(0.8)
    
    for x in range(0, 5):
        t(0.4)
        press(Key.down)

    t(0.8)

    press(Key.enter)

    t(0.8)

    press('s')

    t(0.8)

    for x in range(0, 10):
        t(0.4)
        press(Key.down)

    t(0.8)

    press(Key.enter)

    t(0.8)

    press(Key.down)

    t(0.8)

    press(Key.enter)

    t(0.8)

    with Keyboard.pressed(Key.ctrl):
        press('a')

    t(0.8)

    press(Key.menu)

    t(0.8)

    for x in range(0, 3):
        t(0.4)
        press(Key.up)

    t(2)

    press(Key.enter)

    t(0.8)

    press(Key.up)

    t(0.8)

    press(Key.enter)

    t(0.8)

    press(Key.down)

    t(0.8)

    press(Key.enter)

    t(0.8)

    with Keyboard.pressed(Key.alt):
        press(Key.f4)


def tp_clean():
    
    with Keyboard.pressed(Key.cmd):
        press('r')

    t(0.8)

    Keyboard.type('temp')

    t(0.8)

    press(Key.enter)

    t(2)

    press(Key.enter)

    t(0.8)

    with Keyboard.pressed(Key.ctrl):
        press('a')

    t(0.8)

    press(Key.menu)

    t(0.8)

    for x in range(0, 3):
        t(0.4)
        press(Key.up)

    t(0.8)

    for x in range(0, 2):
        t(0.4)
        press(Key.enter)

    t(2)

    with Keyboard.pressed(Key.alt):
        press(Key.f4)


def fc_clean():
    
    with Keyboard.pressed(Key.cmd):
        press('r')

    t(0.8)

    Keyboard.type('prefetch')

    t(0.8)

    press(Key.enter)

    t(2)

    press(Key.enter)

    t(0.8)

    with Keyboard.pressed(Key.ctrl):
        press('a')

    t(0.8)

    press(Key.menu)

    t(0.8)

    for x in range(0, 3):
        t(0.4)
        press(Key.up)

    t(0.8)

    for x in range(0, 3):
        t(0.4)
        press(Key.enter)

    t(2)

    with Keyboard.pressed(Key.alt):
        press(Key.f4)


def rb_clean():
    
    with Keyboard.pressed(Key.cmd):
        press('e')

    t(2)

    for x in range(0, 5):
        t(0.4)
        press(Key.tab)

    t(0.8)

    press(Key.down)

    t(0.8)

    press(Key.enter)

    t(0.8)

    press(Key.tab)

    t(0.8)

    for x in range(0, 4):
        t(0.4)
        press(Key.down)

    t(0.8)

    press(Key.menu)

    t(0.8)

    press(Key.up)

    t(0.8)

    press(Key.enter)

    t(0.8)

    press(Key.tab)

    t(0.8)

    press(Key.enter)

    t(4)

    for x in range(0, 2):
        t(0.4)
        press(Key.down)

    t(0.8)

    for x in range(0, 5):
        t(0.4)
        press(Key.down)
        press(Key.space)

    t(0.8)

    press(Key.enter)

    t(0.8)

    press(Key.enter)

    t(4)

    press(Key.enter)

    t(16)

    for x in range(0, 2):
        t(0.4)
        with Keyboard.pressed(Key.alt):
            press(Key.f4)


cleaner = CTk()

cleaner.title('sᴏᴜʀᴄᴇ ᴄʟᴇᴀɴᴇʀ')
cleaner.geometry('800x500')
cleaner._set_appearance_mode('system')
set_default_color_theme('green')
cleaner.resizable(False, False)
cleaner.iconbitmap('also here with mycleaner.ico')

cleaner_background = customtkinter.CTkImage(light_image=Image.open('write here and ⬇ the directory of this image mybg.jpg'),
                                       dark_image=Image.open('a directory is like this C:/Users/etc..'),
                                       size=(424, 500))

lab0 = customtkinter.CTkLabel(master=cleaner,
                              text='',
                              image=cleaner_background)
lab0.pack()
lab0.place(x=0, y=0)

fra0 = customtkinter.CTkFrame(master=cleaner,
                              width=300,
                              height=400,
                              corner_radius=10)
fra0.pack()
fra0.place(x=462, y=52)

svar0 = customtkinter.StringVar(value='true')


def day_moon():

    if svar0.get() == 'false':
        set_appearance_mode('light')
    elif svar0.get() == 'true':
        set_appearance_mode('dark')


switch_dymn = customtkinter.CTkSwitch(master= cleaner,
                                      text='ᴛʜᴇᴍᴇ',
                                      command=day_moon,
                                      button_length=6,
                                      variable=svar0, offvalue='false', onvalue='true')
switch_dymn.pack()
switch_dymn.place(x=560, y=460)

button1 = customtkinter.CTkButton(master=fra0,
                                  width=200,
                                  height=45,
                                  text='ᴄʟᴇᴀɴ ᴅᴏᴡɴʟᴏᴀᴅ',
                                  command=dw_clean)
button1.pack()
button1.place(relx=0.175, rely=0.15)

button2 = customtkinter.CTkButton(master=fra0,
                                  width=200,
                                  height=45,
                                  text='ᴄʟᴇᴀɴ ᴛᴇᴍᴘ',
                                  command=tp_clean)
button2.pack()
button2.place(relx=0.175, rely=0.35)

button3 = customtkinter.CTkButton(master=fra0,
                                  width=200,
                                  height=45,
                                  text='ᴄʟᴇᴀɴ ᴘʀᴇғᴇᴛᴄʜ',
                                  command=fc_clean)
button3.pack()
button3.place(relx=0.175, rely=0.55)

button4 = customtkinter.CTkButton(master=fra0,
                                  width=200,
                                  height=45,
                                  text='ᴄʟᴇᴀɴ ʙɪɴ',
                                  command=rb_clean)
button4.pack()
button4.place(relx=0.175, rely=0.75)

popup_background = customtkinter.CTkImage(light_image=Image.open('you need to do that also here with mywhitepattern.jpg'),
                                       dark_image=Image.open('even here but use this file image myblackpattern.jpg'),
                                       size=(800, 500))

lab1 = customtkinter.CTkLabel(master=cleaner,
                              text='',
                              image=popup_background)
lab1.pack()
lab1.place(x=0, y=0)

fra2 = customtkinter.CTkFrame(master=lab1,
                              width=220,
                              height=120)
fra2.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

lab2 = customtkinter.CTkLabel(master=fra2,
                              text='sᴏᴜʀᴄᴇ ᴄʟᴇᴀɴᴇʀ ɪs ᴘʀᴏᴠɪᴅᴇᴅ\n ʙʏ ғ⁴⁴, ᴀɴᴅ ᴡʜᴇɴ ʏᴏᴜ ᴜsᴇ ɪᴛ\n ʏᴏᴜ ᴡɪʟʟ sᴇᴇ ᴡʜᴀᴛ ɪᴛ ᴅᴏᴇs',
                              justify=CENTER)
lab2.pack()
lab2.place(relx=0.49, rely=0.4, anchor=customtkinter.CENTER)


def stpopup_destroy():
    lab1.destroy()


button_desok = customtkinter.CTkButton(master=fra2,
                                       text='ᴏᴋ',
                                       hover_color='grey',
                                       fg_color='black',
                                       command=stpopup_destroy,
                                       width=220,
                                       height=30)
button_desok.pack_slaves()
button_desok.place(relx=0, rely=0.775)

cleaner.mainloop()

# YOU CAN ALSO REMOVE IMAGES AND MODIFY THE CODE
# File license | GPL v3.0
