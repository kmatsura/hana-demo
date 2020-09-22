import tkinter
import cv2
import PIL.Image, PIL.ImageTk


class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        self.vcap = cv2.VideoCapture(0)
        self.width = self.vcap.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        # カメラモジュールの映像を表示するキャンバスを用意する
        self.canvas = tkinter.Canvas(window, width=self.width, height=self.height)
        self.canvas.pack()

        # Closeボタン
        self.close_btn = tkinter.Button(window, text="Close")
        self.close_btn.pack()
        self.close_btn.configure(command=self.destructor)

        # update()関数を15ミリ秒ごとに呼び出し、
        # キャンバスの映像を更新する
        self.delay = 15
        self.update()

        self.window.mainloop()

    # キャンバスに表示されているカメラモジュールの映像を
    # 15ミリ秒ごとに更新する
    def update(self):
        _, frame = self.vcap.read()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
        self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)

        self.window.after(self.delay, self.update)

    # Closeボタンの処理
    def destructor(self):
        self.window.destroy()
        self.vcap.release()

App(tkinter.Tk(), "Tkinter & Camera module")