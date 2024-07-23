from tts import TTS
from tkinter import *
from tkinter import filedialog
from pdf import PDF
import pygame



#Function that centres the widgets
# def center_widget(num):
#     for i in range(num):
#         root.columnconfigure(i,weight=1)
#         root.rowconfigure(i,weight=1)

#Function to get the text from pdf file
def text():
    text=PDF()
    pdf_text=text.reader("".join(path_list))
    return pdf_text

#function to open the dialoguebox
def upload_pdf():
    global path_list,convert_button
    path_list=[]
    file_path=filedialog.askopenfile(filetypes=[("PDF Files","*.pdf")])
    if file_path:
        path=file_path.name
        path_list.append(path)
        file_location.delete(0,END)
        file_location.insert(0,path)
        convert_button=Button(text="Convert To Speech",command=convert_speech)
        convert_button.grid(column=1,row=4,columnspan=2,pady=20)
        add_pdf.destroy()
        reset_button=Button(text="New PDF",command=reset)
        reset_button.grid(row=2,column=1,columnspan=2)

#Function to convert the text to speech 
def convert_speech():
    tts=TTS()
    tts.to_speech(text())
    convert_button.destroy()
    play_button=Button(text="Play",command=play,width=20)
    play_button.grid(column=1,row=4,columnspan=2,pady=20)
    stop_button=Button(text="Stop",command=stop,width=20)
    stop_button.grid(column=1,row=5,columnspan=2)

#pygame fucntion to play the audio
def play():
    path=f"{text().split()[0]}.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
#Function to stop the audio
def stop():
    pygame.mixer.music.stop()

#Function to reset the tkinter gui
def reset():
    pygame.mixer.music.stop()
    root.destroy()
    create_gui()

#Main function that get initialized when the program is run
def create_gui():
    global root,canvas,main_info,add_pdf,file_location,path_list
    path_list=[]
    root=Tk()
    root.title("SoundOn")
    root.geometry("500x500")
    root.config(padx=150,pady=50)
    # center_widget(3)
    canvas=Canvas(width=200,height=200)
    img=PhotoImage(file="tts.png")
    canvas.create_image(90,90,image=img)
    canvas.grid(column=1,row=0,columnspan=2)

    main_info=Label(text="Click on the button below to upload a pdf file.")
    main_info.grid(row=1,column=1,columnspan=2)
    add_pdf=Button(text="SELECT PDF",command=upload_pdf)
    add_pdf.grid(row=2,column=1,columnspan=2)
    file_location=Entry(width=40)
    file_location.grid(row=3,column=1,pady=10,columnspan=2)
    root.mainloop()

if __name__=="__main__":
    create_gui()