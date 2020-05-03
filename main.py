from __future__ import unicode_literals
import wx
import youtube_dl


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='youtube-helper')
        panel = wx.Panel(self)
        availableTypes = ["mp3", "video"]
        userChoice = "mp3"
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        my_btn = wx.Button(panel, label='Download video')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
        self.combobox = wx.Choice(panel, choices=availableTypes, pos=(50,50))
        self.combobox.SetSelection(0)
        my_sizer.Add(self.combobox, 0, wx.ALL | wx.CENTER, 60)
        self.Bind(wx.EVT_CHOICE, self.OnCombo)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnCombo(self, event):
        print("Debug")

    def on_press(self, event):
        ydl_opts_audio = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

        ydl_opts_video = {
            'format': 'best'
        }

        value = self.text_ctrl.GetValue()
        if not value:
            nothingEntered = wx.MessageBox('Nothing was entered in the box', 'Error', wx.OK)
        else:
            print("Downloading and converting. Be patient.")
            userChoice = self.combobox.GetValue()
            if userChoice == "mp3":
                with youtube_dl.YoutubeDL(ydl_opts_audio) as ydl:
                    ydl.download([value])
            elif userChoice == "video":
                with youtube_dl.YoutubeDL(ydl_opts_video) as ydl:
                    ydl.download([value])
            resp = wx.MessageBox('Download has finished, are you done?', 'Finished!', wx.YES_NO)
            if resp == wx.YES:
                self.Destroy()
            elif resp == wx.NO:
                return

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
