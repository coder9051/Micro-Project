import calendar
import tkinter as tk
from tkinter import *
from datetime import date

def CreateWidgets():
    root.calLabel = Label(root, bg="purple4", fg="white", font=('Comic Sans MS',20))
    root.calLabel.grid(row=1, column=1, padx=10, pady=10, columnspan=3)

    root.calendarTxt = Text(root, bg="MediumPurple1", borderwidth=5, relief="raised", width=75, height=30)
    root.calendarTxt.grid(row=2, column=1, padx=25, pady=10, columnspan=2)

    root.calendarEntry = Entry(root, width=30, textvariable=year, justify="center")
    root.calendarEntry.grid(row=3, column=5, padx=10, pady=10)

    root.getCalendarButton = Button(root, width=20, text="DISPLAY CALENDAR", command=getCalendar)
    root.getCalendarButton.grid(row=3, column=2, padx=10, pady=10)

    onStartUp()

def onStartUp():

    current_year = date.today().year
    calendar_text = calendar.calendar(current_year)
    root.calLabel.config(text=str(current_year)+" CALENDAR")
    root.calendarTxt.insert(0.0, calendar_text)

def getCalendar():
    calendar_year = int(year.get()
    calendar_text = calendar.calendar(calendar_year)
    root.calLabel.config(text=str(calendar_year)+" CALENDAR")
    root.calendarTxt.insert(0.0, calendar_text)

root = tk.Tk()
root.title("PythonCalendar")
root.geometry("670x650")
root.resizable(False, False)
root.configure(background = "royalblue4")
year = StringVar()
CreateWidgets()
root.mainloop()

