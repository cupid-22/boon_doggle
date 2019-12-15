import time
from os import listdir
from os.path import join


class FileHandler:

    def on_modified(self, event):
        for filename in listdir(source_to_track):
            src = join(source_to_track, '', filename)
            final_destination = join(folder_destination)
