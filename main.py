import matplotlib.pyplot as plt
import pandas as pd
import customtkinter as ctk
from tkinter import messagebox

class GraphGenerator():
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry('500x500')
        self.root.resizable(False, False)
        self.root.title('Graph Generator')
        self.Linear()
        self.root.mainloop()

    def Linear(self):
        def Gen(link):
            Gra(link)

        self.Frame = ctk.CTkFrame(master=self.root,
                                  height=490,
                                  width=490)

        self.Frame.place(relx = 0.5,
                         rely = 0.5,
                         anchor = 'center')

        self.Label = ctk.CTkLabel(master=self.Frame,
                                  text='Paste Fİle Directory',
                                  text_color="grey",
                                  font=('Arial', 18)
                                  )

        self.Label.place(relx = 0.5,
                         rely = 0.2,
                         anchor = 'center')


        self.entry = ctk.CTkEntry(master=self.Frame,
                                  width=390,
                                  height=25)
        self.entry.place(relx = 0.5,
                         rely = 0.3,
                         anchor = 'center')

        def pr():
            Gen(self.entry.get())

        self.button = ctk.CTkButton(master=self.Frame,
                                    text='Generate',
                                    fg_color="grey",
                                    text_color="black",
                                    command=pr
                                    )


        self.button.place(relx = 0.5,
                          rely = 0.7,
                          anchor = 'center')

class Gra(object):

    def __init__(self,data0):
        self.data0 = data0
        col_list = []
        try:
            data = pd.read_excel(data0)
            for i in range(0, len(data.columns)):
                col_list.append(data.iloc[:, i:i + 1])

            colors = [u'#FFB6C1', u'#FFC0CB', u'#DC143C', u'#FFF0F5', u'#DB7093', u'#FF69B4', u'#FF1493', u'#C71585',
                      u'#DA70D6', u'#D8BFD8', u'#DDA0DD', u'#EE82EE', u'#FF00FF', u'#FF00FF', u'#8B008B', u'#800080',
                      u'#BA55D3', u'#9400D3', u'#9932CC', u'#4B0082', u'#8A2BE2', u'#9370DB', u'#7B68EE', u'#6A5ACD',
                      u'#483D8B', u'#F8F8FF', u'#E6E6FA', u'#0000FF', u'#0000CD', u'#00008B', u'#000080', u'#191970',
                      u'#4169E1', u'#6495ED', u'#B0C4DE', u'#778899', u'#708090', u'#1E90FF', u'#F0F8FF', u'#4682B4',
                      u'#87CEFA', u'#87CEEB', u'#00BFFF', u'#ADD8E6', u'#B0E0E6', u'#5F9EA0', u'#00CED1', u'#F0FFFF',
                      u'#E0FFFF', u'#AFEEEE', u'#00FFFF', u'#00FFFF', u'#008B8B', u'#008080', u'#2F4F4F', u'#48D1CC',
                      u'#20B2AA', u'#40E0D0', u'#7FFFD4', u'#66CDAA', u'#00FA9A', u'#F5FFFA', u'#00FF7F', u'#3CB371',
                      u'#2E8B57', u'#F0FFF0', u'#8FBC8F', u'#98FB98', u'#90EE90', u'#32CD32', u'#00FF00', u'#228B22',
                      u'#008000', u'#006400', u'#7CFC00', u'#7FFF00', u'#ADFF2F', u'#556B2F', u'#9ACD32', u'#6B8E23',
                      u'#FFFFF0', u'#F5F5DC', u'#FFFFE0', u'#FAFAD2', u'#FFFF00', u'#808000', u'#BDB76B', u'#EEE8AA',
                      u'#FFFACD', u'#F0E68C', u'#FFD700', u'#FFF8DC', u'#DAA520', u'#B8860B', u'#FFFAF0', u'#FDF5E6',
                      u'#F5DEB3', u'#FFA500', u'#FFE4B5', u'#FFEFD5', u'#FFEBCD', u'#FFDEAD', u'#FAEBD7', u'#D2B48C',
                      u'#DEB887', u'#FF8C00', u'#FFE4C4', u'#FAF0E6', u'#CD853F', u'#FFDAB9', u'#F4A460', u'#D2691E',
                      u'#8B4513', u'#FFF5EE', u'#A0522D', u'#FFA07A', u'#FF7F50', u'#FF4500', u'#E9967A', u'#FF6347',
                      u'#FA8072', u'#FFE4E1', u'#F08080', u'#FFFAFA', u'#BC8F8F', u'#CD5C5C', u'#FF0000', u'#A52A2A',
                      u'#B22222', u'#8B0000', u'#800000', u'#FFFFFF', u'#F5F5F5', u'#DCDCDC', u'#D3D3D3', u'#C0C0C0',
                      u'#A9A9A9', u'#808080', u'#696969', u'#000000']
            for i in range(0,len(data.columns)):
                fig = plt.figure(figsize = (10,10))
                plt.plot(col_list[0],col_list[i] ,color = colors[i])
                plt.title(f"Graph{i+1}")
                plt.xlabel("X Axis")
                plt.ylabel("Y Axis")
                plt.show()

                fig.savefig(f"Graph_Linear{i}.png")
        except:
            messagebox.showinfo(title="Error", message="Please add the file extension in the appropriate "
                                                       "format or make sure you entered the file name correctly....")

if __name__ == '__main__':
    GraphGenerator()
