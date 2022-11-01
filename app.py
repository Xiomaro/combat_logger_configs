from configparser import ConfigParser
from datetime import date, datetime
import os
import tkinter
import customtkinter
from typing import TypedDict
import urllib.request
from config_dialog import Dialog


class Config(TypedDict):
        patch: str
        days_since_update: int
        ips: list[str]
        identifier: str
        guild_offset: int
        player_one_offset: int
        player_two_offset: int
        kill_offset: int
        log_length: int
        name_length: int

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.check_for_updates()
        

        self.geometry("275x225")
        self.title("Combat Logger")
        self.resizable(False,False)

        # create 2x2 grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        
        
        frame_1 = customtkinter.CTkFrame(master=self, fg_color="#212325")
        frame_1.grid(row=0, rowspan=1, column=0, columnspan=1,padx=20, pady=10, sticky="nsew")
        
        label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text="Combat Logger")
        label_1.pack(pady=(0,12), padx=10)


        button_1 = customtkinter.CTkButton(master=frame_1, text="Start logging")
        button_1.pack(pady=(0,6), padx=10)
        
        button_2 = customtkinter.CTkButton(master=frame_1, text="Start recording")
        button_2.pack(pady=(0,6), padx=10)
        
        button_3 = customtkinter.CTkButton(master=frame_1, text="Open file")
        button_3.pack(pady=(0,12), padx=10)
        
        
        """ checkbox = customtkinter.CTkCheckBox(master=frame_1, text="Config loaded",  state="disabled",  width=20, height=20, text_color_disabled="white")
        checkbox.select()
        checkbox.pack(padx=20, pady=10) """
        age_label_text = "Config Loaded" 
        if self.logger_config["days_since_update"] < 7:
            age_label_text = "Config is older than 7 days.\nIt might not work anymore!\nIf unsure: use the recording option."
            
        age_label = customtkinter.CTkLabel(master=frame_1, text=age_label_text)     
        age_label.pack()


    
        
    def load_config(self) -> Config:
        # load config
        config_parser = ConfigParser()
        config_parser.read('config.ini')
        config = dict(config_parser)
        
        config_date = config["GENERAL"]["patch"]

        # get ip addresses
        ips = list((config["IP"]).values())

        # get package informations
        package_config = config["PACKAGE"]
        identifier = package_config["identifier"]
        guild_offset = int(package_config["guild"])
        player_one_offset = int(package_config["player_one"])
        player_two_offset = int(package_config["player_two"])
        kill_offset = int(package_config["kill"])
        log_length = int(package_config["log_length"])
        name_length = int(package_config["name_length"])
        
        config_date = datetime.strptime(config_date, "%d.%m.%Y")
        config_date = config_date.replace(hour=12, minute=0)
        difference = (datetime.today() - config_date).days
        
        return {"patch":config_date,"days_since_update": difference, "ips":ips, "identifier": identifier, "guild_offset":guild_offset, "player_one_offset":player_one_offset, "player_two_offset":player_two_offset, "kill_offset":kill_offset, "log_length":log_length, "name_length":name_length }
        
        
    def check_for_updates(self):
        error_text = ""
        try:
            st=os.stat('./config.ini')
            self.logger_config = self.load_config()
            
            if self.logger_config["days_since_update"] >= 7:
                raise Exception("Outdated Config")
        except FileNotFoundError as error:
            print(error)
            error_text = "No Config file found. Download config?"
        except Exception as error:
            print(error)
            error_text = "The config file is older than 7 days and\nmight not work anymore.\nDownload latest config?"
        
        if len(error_text) > 0:
            dialog = Dialog(master=None, text=error_text, title="Config Error")
            reply = dialog.get_input()
            if reply:
                urllib.request.urlretrieve("https://raw.githubusercontent.com/sch-28/combat_logger/main/config.ini", "config.ini")
                self.logger_config = self.load_config()
                

        
        
       

            



if __name__ == "__main__":
    app = App()
    app.mainloop()