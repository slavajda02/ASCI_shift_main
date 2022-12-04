import customtkinter
import tkinter

class app(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Encryptor")
        
        self.tabview = customtkinter.CTkTabview(self, command = self.tabChange)
        self.tabview.add("Encryption")  # add tab at the end
        self.tabview.add("Decryption")  # add tab at the end
        self.tabview.add("Keygen")  # add tab at the end
        self.tabview.set("Encryption")  # set currently visible tab
        self.geometry("450x350")
        
        self.grid_rowconfigure((0,1), weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.tabview.tab("Encryption").grid_rowconfigure((0, 1) ,weight = 1)
        self.tabview.tab("Encryption").grid_columnconfigure(0 ,weight = 1)
        
        self.tabview.tab("Decryption").grid_rowconfigure((0, 1) ,weight = 1)
        self.tabview.tab("Decryption").grid_columnconfigure(0 ,weight = 1)
        
        self.tabview.tab("Keygen").grid_rowconfigure((0,1) ,weight = 1)
        self.tabview.tab("Keygen").grid_columnconfigure(0 ,weight = 1)
        
        #Elements declaration
        self.wordEntryEc = customtkinter.CTkEntry(
            self.tabview.tab("Encryption"), placeholder_text="Text") # entry input field field in encryption tab
        self.keyEntryEc = customtkinter.CTkEntry(
            self.tabview.tab("Encryption"), placeholder_text="Key") # entry input field for encryption key in encryption tab
        
        self.wordEntryDec = customtkinter.CTkEntry(
            self.tabview.tab("Decryption"),placeholder_text="Text") # entry input field field in decryption tab
        self.keyEntryDec = customtkinter.CTkEntry(
            self.tabview.tab("Decryption"),placeholder_text="Key") # entry input field for encryption key in decryption tab
        
        self.keyGenOut = customtkinter.CTkEntry(
            self.tabview.tab("Keygen"), state="readonly") # output field for encryption key in keygen
        self.keyLabel = customtkinter.CTkLabel(
            self.tabview.tab("Keygen"), text = "Your generated key")
        
        self.goButton = customtkinter.CTkButton(
            self, text = "Encrypt", command="", state="disabled") # button starting encrypt functions
        
        #Elements placement
        #Main window
        self.tabview.grid(row = 0, column = 0, padx = 20)
        self.tabview.grid_configure(sticky = "nsew")
        self.goButton.grid(row = 1, column = 0)
        
        #Individual tabs
        self.wordEntryEc.grid(row = 0, column = 0, sticky = tkinter.S, pady = 10)
        self.keyEntryEc.grid(row = 1, column = 0, sticky = tkinter.N, pady = 10)
        
        self.wordEntryDec.grid(row = 0, column = 0, sticky = tkinter.S, pady = 10)
        self.keyEntryDec.grid(row = 1, column = 0, sticky = tkinter.N, pady = 10)
        
        self.keyLabel.grid(row = 0, column = 0, sticky = tkinter.S, pady = 5)
        self.keyGenOut.grid(row = 1, column = 0, sticky = tkinter.N)
        
    #Function for dynamic UI
        
    #Change button and entry field according to selected tab
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
        
        
App = app()
App.mainloop()
        