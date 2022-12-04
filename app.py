import customtkinter

class app(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Encryptor")
        
        tabview = customtkinter.CTkTabview(self)
        self.tabview.add("Encryption")  # add tab at the end
        self.tabview.add("Decryption")  # add tab at the end
        self.tabview.add("Keygen")  # add tab at the end
        self.tabview.set("Encryption")  # set currently visible tab
        
        self.button_1 = customtkinter.Button(tabview.tab("tab 1"))
        
        