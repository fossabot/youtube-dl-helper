from __future__ import unicode_literals
import wx
import youtube_dl


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='youtube-helper')
        panel = wx.Panel(self)
        available_formats = ["mp3", "video"]
        form_sizer = wx.BoxSizer(wx.VERTICAL)
        self.text_ctrl = wx.TextCtrl(panel)
        self.status_label = wx.StaticText(panel, label="Waiting for user input...")
        self.status_label.Wrap(210)
        form_sizer.Add(self.status_label, 0, wx.ALL | wx.CENTER, 5)
        form_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        download_button = wx.Button(panel, label='Download video')
        download_button.Bind(wx.EVT_BUTTON, self.on_press)
        form_sizer.Add(download_button, 0, wx.ALL | wx.CENTER, 5)
        self.format_selection = wx.Choice(panel, choices=available_formats, pos=(50, 10))
        self.format_selection.SetSelection(0)
        form_sizer.Add(self.format_selection, 0, wx.ALL | wx.CENTER, 20)
        panel.SetSizer(form_sizer)
        self.Show()

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
            wx.MessageBox('Nothing was entered in the box', 'Error', wx.OK)
        else:
            print("Downloading and converting. Be patient.")
            self.status_label.SetLabel("Downloading")
            format_choice = self.format_selection.GetSelection()
            format_configuration = [ydl_opts_audio, ydl_opts_video]
            with youtube_dl.YoutubeDL(format_configuration[format_choice]) as ydl:
                ydl.download([value])
            self.status_label.SetLabel("Waiting for user input...")
            resp = wx.MessageBox('Download has finished, would you like to exit?', 'Download complete', wx.YES_NO)
            if resp == wx.YES:
                self.Destroy()
            elif resp == wx.NO:
                return


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
