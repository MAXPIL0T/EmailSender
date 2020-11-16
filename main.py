from tkinter import *
import smtplib

def mainWindow():
    origin_mail = origin_mail_form.get()
    origin_pword = origin_pword_form.get()
    pre_root.destroy()

    root = Tk()
    root.title("Send Mail")
    root.wm_iconbitmap("./icon.ico")

    def SendEmail():
        recipient = recipient_form.get()
        subject = subject_form.get()
        message = message_form.get("1.0", "end-1c")

        email_text = "From: {}\nTo: {}\nSubject: {}\n\n{}".format(origin_mail, recipient, subject, message)

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(origin_mail, origin_pword)
            server.sendmail(origin_mail, recipient, email_text)
            server.close()
            Label(root, text="Email Sent!").pack()
        except Exception as e:
            Label(root, text="Something went wrong, check console.").pack()
            print(e)
        recipient_form.delete(0, END)
        subject_form.delete(0, END)
        message_form.delete("1.0", "end-1c")
        recipient_form.insert(0, "Recipient Adress")
        subject_form.insert(0, "Email Subject")

    recipient_form = Entry(root, width=50)
    subject_form = Entry(root, width=50)
    message_form = Text(root, width=50)
    send_button = Button(root, text="Send", command=SendEmail)

    recipient_form.pack()
    subject_form.pack()
    message_form.pack()
    send_button.pack()

    recipient_form.insert(0, "Recipient Adress")
    subject_form.insert(0, "Email Subject")

    root.mainloop()

pre_root = Tk()
pre_root.title("Login")
pre_root.wm_iconbitmap("./icon.ico")

origin_mail_form = Entry(pre_root, width=50)
origin_pword_form = Entry(pre_root, width=50)
login_button = Button(pre_root, text="Login", command=mainWindow)
warning_label = Label(pre_root, text="Less secure apps have to be enabled\nin your google account.")

origin_mail_form.pack()
origin_pword_form.pack()
login_button.pack()
warning_label.pack()

origin_mail_form.insert(0, "Gmail Username")
origin_pword_form.insert(0, "Gmail Password")

pre_root.mainloop()