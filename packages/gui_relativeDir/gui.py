from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
#
# def browse_button():
#     # Allow user to select a directory and store it in global var
#     # called folder_path
#     global folder_path
#     filename = tkFileDialog.askdirectory()
#     filename = tkFileDialog.askopenfilename(initialdir="/", title="Select file",
#                                                  filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
#     print (root.filename)
#
#     folder_path.set(filename)
#     print(filename)
#
#
# root = Tk()
# folder_path = StringVar()
# lbl1 = Label(master=root,textvariable=folder_path)
# lbl1.grid(row=0, column=1)
# button2 = Button(text="Browse", command=browse_button)
# button2.grid(row=0, column=3)
#
# mainloop()

#======== Select a directory:
#
# import Tkinter, tkFileDialog
#
# root = Tkinter.Tk()
# dirname = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
# if len(dirname ) > 0:
#     print "You chose %s" % dirname


# ======== Select a file for opening:
import Tkinter,tkFileDialog

root = Tkinter.Tk()
file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
if file != None:
    data = file.read()
    file.close()
    print "I got %d bytes from this file." % len(data)


# ======== "Save as" dialog:
# import Tkinter,tkFileDialog
#
# myFormats = [
#     ('Windows Bitmap','*.bmp'),
#     ('Portable Network Graphics','*.png'),
#     ('JPEG / JFIF','*.jpg'),
#     ('CompuServer GIF','*.gif'),
#     ]
#
# root = Tkinter.Tk()
# fileName = tkFileDialog.asksaveasfilename(parent=root,filetypes=myFormats ,title="Save the image as...")
# if len(fileName ) > 0:
#     print "Now saving under %s" % nomFichier

# #--------------------------------------------------------------------------------------------------------------------------
# from tkFileDialog import askopenfilename
# # import paramiko
# #
# # client = paramiko.SSHClient()
# # client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # client.connect('192.168.2.34', username='pi', password='raspberry')
#
# checkdir = "/home/pi/python"
# name1= askopenfilename(title = "Select File For Removal", initialdir = checkdir)
# stdin, stdout, stderr = client.exec_command('ls -l')
# for line in stdout:
#    print '... ' + line.strip('\n')
# client.close()