import customtkinter
import tkinter
from core import *

class app(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Encryptor")
        
        self.tabview = customtkinter.CTkTabview(self, command = self.tabChange)
        self.tabview.add("Encryption")  
        self.tabview.add("Decryption")  
        self.tabview.add("Keygen")  
        self.tabview.set("Encryption")  # set currently visible tab
        self.geometry("450x350")
        self.eval('tk::PlaceWindow . center')
        self.resizable(False,False)
        
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.tabview.tab("Encryption").grid_rowconfigure((0, 1, 2, 3),weight = 1)
        self.tabview.tab("Encryption").grid_columnconfigure(0 ,weight = 1)
        
        self.tabview.tab("Decryption").grid_rowconfigure((0, 1, 2, 3) ,weight = 1)
        self.tabview.tab("Decryption").grid_columnconfigure(0 ,weight = 1)
        
        self.tabview.tab("Keygen").grid_rowconfigure((0,1) ,weight = 1)
        self.tabview.tab("Keygen").grid_columnconfigure(0 ,weight = 1)
        
        # Elements declaration
        self.labelWordsEntryEc = customtkinter.CTkLabel(
            self.tabview.tab("Encryption"), text = "Words to encrypt", font=("", 13))
        self.labelKeyEntryEc = customtkinter.CTkLabel(
            self.tabview.tab("Encryption"), text = "Key", font=("", 13))
        self.wordEntryEc = customtkinter.CTkEntry(
            self.tabview.tab("Encryption"), placeholder_text="Text") # entry input field field in encryption tab
        self.keyEntryEc = customtkinter.CTkEntry(
            self.tabview.tab("Encryption")) # entry input field for encryption key in encryption tab
        
        self.labelWordsEntryDec = customtkinter.CTkLabel(
            self.tabview.tab("Decryption"), text = "Words to decrypt", font=("", 13))
        self.labelKeyEntryDec = customtkinter.CTkLabel(
            self.tabview.tab("Decryption"), text = "Key", font=("", 13))
        self.wordEntryDec = customtkinter.CTkEntry(
            self.tabview.tab("Decryption"),placeholder_text="Text") # entry input field field in decryption tab
        self.keyEntryDec = customtkinter.CTkEntry(
            self.tabview.tab("Decryption")) # entry input field for encryption key in decryption tab
        
        self.keyGenOut = customtkinter.CTkEntry(
            self.tabview.tab("Keygen"), state="normal") # output field for encryption key in keygen
        self.keyLabel = customtkinter.CTkLabel(
            self.tabview.tab("Keygen"), text = "Your generated key", font=("", 13))
        self.goButton = customtkinter.CTkButton(
            self, text = "Encrypt", command=self.buttonPress, state="disabled") # button starting encrypt functions
        
        # Binding entry field to buttonStateChange and buttonPress functions
        self.wordEntryEc.bind("<KeyRelease>", self.buttonStateChange)
        self.wordEntryEc.bind("<Return>", self.buttonPress)
        self.wordEntryDec.bind("<KeyRelease>", self.buttonStateChange)
        self.wordEntryDec.bind("<Return>", self.buttonPress)
        self.keyEntryEc.bind("<KeyRelease>", self.buttonStateChange)
        self.keyEntryEc.bind("<Return>", self.buttonPress)
        self.keyEntryDec.bind("<KeyRelease>", self.buttonStateChange)
        self.keyEntryDec.bind("<Return>", self.buttonPress)
        
        
        # Elements placement
        # Main window
        self.tabview.grid(row = 0, column = 0, padx = 20)
        self.tabview.grid_configure(sticky = "nsew")
        self.goButton.grid(row = 1, column = 0)
        
        # Individual tabs
        self.labelWordsEntryEc.grid(row = 0, column = 0, sticky = tkinter.S, pady = 0)
        self.wordEntryEc.grid(row = 1, column = 0, sticky = tkinter.N, pady = 0)
        self.labelKeyEntryEc.grid(row = 2, column = 0, sticky = tkinter.S, pady = 0)
        self.keyEntryEc.grid(row = 3, column = 0, sticky = tkinter.N, pady = 0)
        
        self.labelWordsEntryDec.grid(row = 0, column = 0, sticky = tkinter.S, pady = 0)
        self.wordEntryDec.grid(row = 1, column = 0, sticky = tkinter.N, pady = 0)
        self.labelKeyEntryDec.grid(row = 2, column = 0, sticky = tkinter.S, pady = 0)
        self.keyEntryDec.grid(row = 3, column = 0, sticky = tkinter.N, pady = 0)
        
        self.keyLabel.grid(row = 0, column = 0, sticky = tkinter.S, pady = 0)
        self.keyGenOut.grid(row = 1, column = 0, sticky = tkinter.N)
        
    # Functions for dynamic UI   
    # Change button and entry field according to selected tab
    def tabChange(self):
        currTab = self.tabview.get()
        
        if currTab == "Encryption":
            self.goButton.configure(text = "Encrypt")
            self.goButton.configure(state = "disabled")
            #self.wordEntryEc.configure(textvariable = tkinter.StringVar(value = self.wordEntryDec.get()))
        elif currTab == "Decryption":
            self.goButton.configure(text = "Decrypt")
            self.goButton.configure(state = "disabled")
            #self.wordEntryDec.configure(textvariable = tkinter.StringVar(value = self.wordEntryEc.get()))
        elif currTab == "Keygen":
            self.goButton.configure(text = "Generate") 
            self.goButton.configure(state = "enabled")
            
        self.buttonStateChange()           
            
    # Chaning buttonState according to entry
    def buttonStateChange(self, properties = None):
        currTab = self.tabview.get()
        
        if currTab == "Encryption":   
            if self.wordEntryEc.get() and self.keyEntryEc.get():
                self.goButton.configure(state = "enabled")
            else:
                self.goButton.configure(state = "disabled")
        
        if currTab == "Decryption":
            if self.wordEntryDec.get() and self.keyEntryDec.get():
                self.goButton.configure(state = "enabled")
            else:
                self.goButton.configure(state = "disabled")
    
    # Functions for calling core functions and outputing their results
    def buttonPress(self, properties = None):
        currTab = self.tabview.get()
        if currTab == "Encryption":
            output = encrypt(self.wordEntryEc.get(), self.keyEntryEc.get())
            if output == "WRONG_FORMAT" or output == "TOO_SHORT":
                self.keyEntryEc.configure(textvariable = tkinter.StringVar(value = ""))
                return
            self.wordEntryEc.configure(
            textvariable = tkinter.StringVar(value = output))
        
        currTab = self.tabview.get()
        if currTab == "Decryption":
            output = decrypt(self.wordEntryDec.get(), self.keyEntryDec.get())
            if output == "WRONG_FORMAT" or output == "TOO_SHORT":
                self.keyEntryDec.configure(textvariable = tkinter.StringVar(value = ""))
                return
            self.wordEntryDec.configure(
                textvariable = tkinter.StringVar(value = output))
        
        if currTab == "Keygen":
            key = keyGenerator()
            self.keyGenOut.configure(textvariable = tkinter.StringVar(value= key))
            self.keyEntryDec.configure(textvariable = tkinter.StringVar(value = key))
            self.keyEntryEc.configure(textvariable = tkinter.StringVar(value = key))

App = app()
App.mainloop()
