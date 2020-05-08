from __future__ import unicode_literals
import wx
import youtube_dl


class HelperFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='youtube-dl-helper')
        panel = wx.Panel(self)
        available_formats = ["audio-hq", "video-hq + audio", "video-hq + no audio"]
        form_sizer = wx.BoxSizer(wx.VERTICAL)
        self.text_ctrl = wx.TextCtrl(panel)
        self.status_label = wx.StaticText(panel, label="Waiting for user input...")
        form_sizer.Add(self.status_label, 0, wx.ALL | wx.TOP, 5)
        form_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        download_button = wx.Button(panel, label='Download')
        download_button.Bind(wx.EVT_BUTTON, self.on_press)
        form_sizer.Add(download_button, 0, wx.ALL | wx.CENTER, 5)
        self.format_selection = wx.Choice(panel, choices=available_formats, pos=(50, 10))
        self.format_selection.SetSelection(0)
        form_sizer.Add(self.format_selection, 0, wx.ALL | wx.CENTER, 20)
        panel.SetSizer(form_sizer)
        self.Show()

    def download_hook(self, d):
        if d['status'] == 'downloading':
            self.status_label.SetLabel("Downloading...")

        elif d['status'] == 'finished':
            self.status_label.SetLabel("Converting")

    def on_press(self, _event_):
        ydl_opts_audio = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'progress_hooks': [self.download_hook]
        }

        ydl_opts_video_audio = {
            'format': 'bestvideo+bestaudio'
        }

        ydl_opts_video_noaudio = {
            'format': 'bestvideo'
        }

        value = self.text_ctrl.GetValue()
        if not value:
            wx.MessageBox('Nothing was entered in the box. Please enter a valid link', 'Error', wx.OK)
        else:
            try:
                print("Downloading and converting. Be patient.")
                self.status_label.SetLabel("Preparing to download...")
                format_choice = self.format_selection.GetSelection()
                format_configuration = [ydl_opts_audio, ydl_opts_video_audio, ydl_opts_video_noaudio]
                with youtube_dl.YoutubeDL(format_configuration[format_choice]) as ydl:
                    ydl.download([value])
                self.status_label.SetLabel("Waiting for user input...")
                download_finished_message = wx.MessageBox('Download has finished, would you like to exit?',
                                                          'Download complete', wx.YES_NO)
                if download_finished_message == wx.YES:
                    self.Destroy()
                elif download_finished_message == wx.NO:
                    return
            except youtube_dl.utils.DownloadError:
                self.status_label.SetLabel("Waiting for user input...")
                wx.MessageBox('Error whilst attempting to download. Check your link as it may be broken!',
                              'Error', wx.OK)


if __name__ == '__main__':
    helper_app = wx.App()
    helper_frame = HelperFrame()
    helper_app.MainLoop()
