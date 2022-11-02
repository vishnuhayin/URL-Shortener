import tkinter as tk
import sqlite3
import logging
from URLShorten_database import insertData

def saveURL(actualURL, shortURL, time):
    root = tk.Tk()
    root.title('Saving URL...')
    root.geometry('550x400')

    def saveUserDetails():
        try:
            connection_1 = sqlite3.connect('url_shortner.db')
            cursor_1 = connection_1.cursor()

            cursor_1.execute(insertData('user_details',[id_entry.get(), name_entry.get(), actualURL, shortURL, time]))

            connection_1.commit()
            connection_1.close()

            tk.messagebox.showinfo("Message", "Data saved")
            logging.info("\nsaved data with ID >> " + id_entry.get())
            root.destroy()

        except Exception as e:
            logging.exception("exception occured "+ str(e))


    id_label = tk.Label(root, text="Enter User ID     :", font=("Helvetica", 12))
    id_label.place(x= 10 , y = 10)

    id_entry = tk.Entry(root, width=41, font=("Helvetica", 12))
    id_entry.place(x= 200 , y = 10)

    name_label = tk.Label(root, text="Enter User Name   :", font=("Helvetica", 12))
    name_label.place(x=10, y=50)

    name_entry = tk.Entry(root, width=41, font=("Helvetica", 12))
    name_entry.place(x=200, y=50)

    actualURL_label = tk.Label(root, text="Actual URL        :", font=("Helvetica", 12))
    actualURL_label.place(x=10, y=90)

    actualURL_entry = tk.Label(root, width=41, text=actualURL, bg='#ffffff', font=("Helvetica", 12))
    actualURL_entry.place(x=200, y=90)

    my_label = tk.Label(root, text="Short URL         :", font=("Helvetica", 12))
    my_label.place(x=10, y=130)

    my_label = tk.Label(root, text=shortURL, bg='#ffffff', width=41, font=("Helvetica", 12))
    my_label.place(x=200, y=130)

    my_label = tk.Label(root, text="Time of Creation  :", font=("Helvetica", 12))
    my_label.place(x=10, y=170)

    my_label = tk.Label(root, text=time, bg='#ffffff', width=41, font=("Helvetica", 12))
    my_label.place(x=200, y=170)

    my_button = tk.Button(root, text=" Save Details ", command= saveUserDetails, font=("Helvetica", 16))
    my_button.place(x= 180 , y = 270)

    root.mainloop()

    return

# if __name__ == '__main__':
#     main()