import time
from os import listdir
from os.path import join


class FileHandler:

    def __init__(self):
        self.selection_type = 0
        self.source_to_track = 0
        self.folder_destination = 0

    def tracker(self, event):
        try:
            self.selection_type = event

            if self.selection_type == 0:
                for filename in listdir(self.source_to_track):
                    src = join(self.source_to_track, '', filename)
                    final_destination = join(self.folder_destination)
            else:
                exit('Not Inside')

        except BaseException as B:
            raise B

    @staticmethod
    def decider(file):
        try:
            ext = file.lower().rpartition('.')[-1]
            if ext in ["pdf", "docx", "jpg", "jpeg", "xls", "xlsx", "doc", "docx", "csv", "txt", 'gif']:
                raise AttributeError('Not Supported File Format {}'.format(ext))
            elif ext in ["pdf", "png", "jpg", "jpeg", "xls", "xlsx", "doc", "docx", "csv", "txt", 'gif']:
                raise AttributeError('Not Supported File Format {}'.format(ext))
            elif ext in ["pdf", "png", "jpg", "jpeg", "xls", "xlsx", "doc", "docx", "csv", "txt", 'gif']:
                raise AttributeError('Not Supported File Format {}'.format(ext))
            elif ext in ["pdf", "png", "jpg", "jpeg", "xls", "xlsx", "doc", "docx", "csv", "txt", 'gif']:
                raise AttributeError('Not Supported File Format {}'.format(ext))
            elif ext in ["pdf", "png", "jpg", "jpeg", "xls", "xlsx", "doc", "docx", "csv", "txt", 'gif']:
                raise AttributeError('Not Supported File Format {}'.format(ext))
            elif ext in ["pdf", "png", "jpg", "jpeg", "xls", "xlsx", "doc", "docx", "csv", "txt", 'gif']:
                raise AttributeError('Not Supported File Format {}'.format(ext))
        except BaseException as B:
            raise B


if __name__ == '__main__':
    selection_user = input('Enter the selection type: ')
    FileHandler().tracker(event=selection_user)
