from cgitb import text
from datetime import datetime, timedelta
import tkinter
import time
from turtle import width
import customtkinter
from github import Github
from datetime import date

class Dialog:
    def __init__(self,
                 master=None,
                 title="CTkDialog",
                 text="CTkDialog",
                 fg_color="default_theme",
                 hover_color="default_theme",
                 border_color="default_theme"):

        self.appearance_mode = customtkinter.AppearanceModeTracker.get_mode()  # 0: "Light" 1: "Dark"
        self.master = master

        self.user_input = None
        self.running = False

        self.height = len(text.split("\n"))*30 + 60

        self.text = text
        self.window_bg_color = customtkinter.ThemeManager.theme["color"]["window_bg_color"]
        self.fg_color = customtkinter.ThemeManager.theme["color"]["button"] if fg_color == "default_theme" else fg_color
        self.hover_color = customtkinter.ThemeManager.theme["color"]["button_hover"] if hover_color == "default_theme" else hover_color
        self.border_color = customtkinter.ThemeManager.theme["color"]["button_hover"] if border_color == "default_theme" else border_color

        self.top = customtkinter.CTkToplevel()
        self.top.geometry(f"{300}x{self.height}")
        self.top.minsize(300, self.height)
        self.top.maxsize(300, self.height)
        self.top.title(title)
        self.top.lift()
        self.top.focus_force()
        self.top.grab_set()

        self.top.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.top.after(10, self.create_widgets)  # create widgets with slight delay, to avoid white flickering of background

    def create_widgets(self):
    
        
        frame = customtkinter.CTkFrame(master=self.top,width=300,height=self.height, fg_color=None)
        frame.pack(padx=0, pady=(0,20))
      
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure((0, 1), weight=1)
        
        self.myLabel = customtkinter.CTkTextbox(master=frame,
                                fg_color="#212325",
                                width=250,
                                text_color="white",
                                height=125,
                                
                                )
        self.myLabel.grid(row=0, column=0, columnspan=2)
        self.myLabel.insert("0.0", self.text)

        self.ok_button = customtkinter.CTkButton(master=frame,
                                   text='Ok',
                                   width=100,
                                   command=self.ok_event,
                                   fg_color=self.fg_color,
                                   hover_color=self.hover_color,
                                   border_color=self.border_color,)
        self.ok_button.grid(row=1, column=0)

        self.cancel_button = customtkinter.CTkButton(master=frame,
                                       text='Cancel',
                                       width=100,
                                       command=self.cancel_event,
                                       fg_color="white",
                                       text_color="black",
                                       hover_color="#cccccc",
                                       border_color=self.border_color)
        self.cancel_button.grid(row=1, column=1)


    def ok_event(self, event=None):
        self.user_input = True
        self.running = False

    def on_closing(self):
        self.running = False

    def cancel_event(self):
        self.user_input = False
        self.running = False
        

    def get_input(self):
        self.running = True

        while self.running:
            try:
                self.top.update()
            except Exception:
                return self.user_input
            finally:
                time.sleep(0.01)

        time.sleep(0.05)
        self.top.destroy()
        return self.user_input
