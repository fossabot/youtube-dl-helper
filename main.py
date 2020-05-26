from __future__ import unicode_literals
import wx
import youtube_dl
from pathlib import Path

class HelperFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='youtube-dl-helper')
        ffmpeg_file = Path("ffmpeg.exe")
        panel = wx.Panel(self)
        available_formats = ["audio only", "video and audio", "video only"]
        quality_formats = ["144p", "240p", "360p", "480p", "720p", "1080p"]
        self.text_ctrl = wx.TextCtrl(panel, size=(360, -1))
        self.text_ctrl.SetPosition((10, 60))
        self.status_label = wx.StaticText(panel, label="Waiting for user input")
        directory_information = wx.StaticText(panel, label="""Leave box blank to save to program directory.""")
        directory_information.SetPosition((10, 118))
        ffmpeg_check = wx.StaticText(panel, label="Check pending...")
        ffmpeg_check.SetPosition(((245, 0)))
        self.directory_output = wx.DirPickerCtrl(panel, size=(360, -1))
        self.directory_output.SetPosition((10, 135))
        self.format_selection = wx.Choice(panel, choices=available_formats, pos=(10, 30))
        self.format_selection.SetSelection(1)
        self.quality_selection = wx.Choice(panel, choices=quality_formats, pos=(140, 30))
        self.quality_selection.SetSelection(5)
        self.subtitle_box = wx.CheckBox(panel, label="Subtitles?", pos=(210, 33))
        download_button = wx.Button(panel, label='Download')
        download_button.Bind(wx.EVT_BUTTON, self.on_press)
        download_button.SetPosition((150, 170))
        ffmpeg_check.SetLabel("ffmpeg found") if ffmpeg_file.is_file() else ffmpeg_check.SetLabel("ffmpeg not found!")
        self.Show()

    def download_hook(self, d):
        if d['status'] == 'downloading':
            self.status_label.SetLabel("Downloading...")

        elif d['status'] == 'finished':
            self.status_label.SetLabel("Converting")

    def on_press(self, _event_):
        file_output = self.directory_output.GetPath()
        if not file_output:
            file_output = "%(title)s.%(ext)s"
        else:
            file_output = file_output + "/%(title)s.%(ext)s"

        quality_choice = self.quality_selection.GetSelection()
        quality_selection = ["144", "240", "360", "480", "720", "1080"]
        ydl_opts_audio = {
            'format': 'bestaudio/best',
            'outtmpl': file_output,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'progress_hooks': [self.download_hook]
        }

        ydl_opts_video_audio = {
            'format': 'bestvideo[height<={}]+bestaudio'.format(quality_selection[quality_choice]),
            'writesubtitles': self.subtitle_box.IsChecked(),
            'outtmpl': file_output,
            'progress_hooks': [self.download_hook]
        }

        ydl_opts_video_noaudio = {
            'format': 'bestvideo[height<={}]'.format(quality_selection[quality_choice]),
            'writesubtitles': self.subtitle_box.IsChecked(),
            'outtmpl': file_output,
            'progress_hooks': [self.download_hook]

        }

        value = self.text_ctrl.GetValue()
        if not value:
            wx.MessageBox('Nothing was entered in the box. Please enter a valid link', 'Error', wx.OK | wx.ICON_HAND)
        else:
            try:
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
            except youtube_dl.utils.DownloadError as download_error:
                self.status_label.SetLabel("Waiting for user input...")
                wx.MessageBox(f'{download_error}',
                              'Error', wx.OK)


if __name__ == '__main__':
    helper_app = wx.App()
    helper_frame = HelperFrame()
    helper_app.MainLoop()
