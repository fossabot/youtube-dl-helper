from __future__ import unicode_literals
import wx
import youtube_dl


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='youtube-helper')
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        self.text_ctrl = wx.TextCtrl(panel)
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        my_btn = wx.Button(panel, label='Download video')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def on_press(self, event):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }
        value = self.text_ctrl.GetValue()
        if not value:
            print("You didn't enter anything!")
        else:
            print("Downloading and converting. Be patient.")
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([value])
            resp = wx.MessageBox('Download has finished, are you done?', 'Finished!', wx.YES_NO)
            if resp == wx.YES:
                quit()
            elif resp == wx.NO:
                return


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
