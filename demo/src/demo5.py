import media.video as video
import media.audio
import tkinter

video = video.Video()
# audio = audio.Audio()

root = tkinter.Tk()
root.frame = tkinter.Label(root)
root.frame.pack()

video.openfile("./../../image/04.mp4", 30)
# audio.openfile("[videofile_path]",)

# audio.play()
video.play()
root.mainloop()