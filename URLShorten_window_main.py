import tkinter as tk
import pyshorteners
import URLShorten_window_saveURL
import datetime, logging
from tkinter import messagebox

def main():
    root = tk.Tk()
    root.title('URL Shortner App')
    root.geometry('500x500')

    def shorten():
        try:
            if shorty.get():
                shorty.delete(0, tk.END)

            if my_entry.get():
                # convert to tinyurl
                url = pyshorteners.Shortener().tinyurl.short(my_entry.get())
                # output to screen
                shorty.insert(tk.END, url)

                # reverse URL
                print(pyshorteners.Shortener().tinyurl.expand(url))
        except Exception as e:
            logging.exception("exception occured "+ str(e))

    def saveData():
        if shorty.get():
            try:
                shortURL = shorty.get().replace('https://tinyurl.com/', '')
                URLShorten_window_saveURL.saveURL(my_entry.get(), shortURL, datetime.datetime.now())

                logging.info("Data inserted to user_details table" + str(my_entry.get()))

            except Exception as e:
                logging.exception("exception occured "+ str(e))
        else: messagebox.showinfo("Message", "No shortURL to save")

    def clearFields():
        shorty.delete(0, tk.END)
        my_entry.delete(0, tk.END)

        messagebox.showinfo("Message", "All fields cleared")
        logging.info("User cleared the values in all fields")

    my_label = tk.Label(root, text = "Paste the link below", font = ("Helvetica", 20))
    my_label.pack(pady=20)

    my_entry = tk.Entry(root, font = ("Helvetica", 24))
    my_entry.pack(pady=10)

    my_button = tk.Button(root, text = "Shorten Link", command = shorten, font=("Helvetica", 20))
    my_button.pack(pady=10)

    shorty_label = tk.Label(root, text="Shortened Link:", font=("Helvetica", 14))
    shorty_label.place(x= 15 , y = 270)

    shorty = tk.Entry(root, font = ("Helvetica", 22), justify=tk.CENTER,
                      width=26, bd=0, bg="#ffffff")
    shorty.place(x= 15 , y = 300)

    save_button = tk.Button(root, text = " Save this data ", command = saveData, font=("Helvetica", 12))
    save_button.place(x= 50 , y = 400)

    clear_button = tk.Button(root, text = " Clear all fields ", command = clearFields, font=("Helvetica", 12))
    clear_button.place(x= 270 , y = 400)

    root.mainloop()

    return

# if __name__ == '__main__':
#     main()