from core.watchdog import Organiser
from os import makedirs
from os.path import expanduser, exists


class Porter(Organiser):
    def __init__(self):
        super().__init__()

    def decider(self, file):
        try:
            ext = file.lower().strip().rpartition('.')[-1]
            if ext in ["pdf", 'txt', "docx", "html", "doc", "odt", "rtf", "xlsx", "csv", 'gif', 'wps', 'wpd', 'ppt', 'pptx',
                       'xls']:
                self.folder_destination = expanduser('~/Documents/')
                # TODO Log here
            elif ext in ['sh', 'py', 'java']:
                self.folder_destination = expanduser('~/Documents/ProjectFile/')
                # TODO Log here
            elif ext in ['zip', 'tar', '7z']:
                self.folder_destination = expanduser('~/Documents/Compressed/')
                # TODO Log here
            elif ext in ["png", "jpg", "jpeg", 'gif', 'bmp', 'ico', 'ps', 'svg']:
                self.folder_destination = expanduser('~/Pictures/')
                # TODO Log here
            elif ext in ["3g2", "3gp", "avi", "flv", "h264", "m4v", "mkv", "mov", "mp4", "mpg", 'mpeg', 'wmv', 'mov', ]:
                self.folder_destination = expanduser('~/Videos/')
                # TODO Log here
            elif ext in ["m4a", "mid", "mp3", "mpa", "wav", "wma", ]:
                self.folder_destination = expanduser('~/Music/')
                # TODO Log here
            else:
                # TODO Log here
                pass

            if self.folder_destination != '' and not exists(self.folder_destination):
                makedirs(self.folder_destination)

        except BaseException as B:
            raise B

    def validateParams(self, s_user, s_mode, s_track):

        try:
            # Folder Validation
            if not isinstance(str, s_track):
                raise AssertionError('Folder should be provided as string')
            if not exists(s_track):
                resp = bool(input('Folder is out of sight would you like to create it (0/1) ?'))
                if resp:
                    try:
                        makedirs(s_track)
                    except FileExistsError:
                        print("Directory ", s_track, " already exists")
                else:
                    raise NotADirectoryError('Folder is out of sight please cross check')

            # execution mode validation
            if not isinstance(int, s_mode) or s_mode not in [0, 1, 2, 3]:
                raise AssertionError('Incorrect Mode Opted')

            # selection mode validation
            if not isinstance(int, s_user):
                raise AssertionError('selection mode is incorrect')

        except AssertionError as a:
            raise a
