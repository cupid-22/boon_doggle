import logging
import shutil
from time import sleep
from os import listdir, mkdir, nice, makedirs
from os.path import join, expanduser, exists, isdir


class Organiser:

    def __init__(self, track='~/Downloads/', selection=0, mode=0):
        """
        Notes:
            Watchdog is specifically designed to keep a constant eye on a folder (currently), could work
            under daemon, battery saver and super persistent mode ( Only on Linux ) and works
            on default normal execution mode which takes gaps to maintain a low search overhead on low end machines.

        Args:
            track: Specifies the folder that needs to be kept under constant track is kept by default at Downloads folder.
            selection: Used to change the tracking mode for watchdog current only default extension sorting is available.
            mode: Flag that makes watchdog to run under different executable mode.

        Returns:
            No Return is there for class everything is logged all along the way.
        """
        self.mode = mode
        self.selection_type = selection
        self.source_to_track = expanduser(track)
        self.folder_destination = ''
        self._priority = None

    def DeepRootMode(self):
        """
            Notes:
                #  What: this is DeepRoot selection mode which include
                # * Deeper Folder traversal Depth [Default: Two folder].
                # * Above Avg cpu overhead with check_call at 8 sec [ Has to check in deeper nodes ].
                # * MultiThreading for each check_call.
                # * Considerable above priority over other process.
        """

        for filename in listdir(self.source_to_track):
            try:
                self.decider(file=str(filename))
                if isdir(filename):
                    continue
                if self.folder_destination != '':
                    shutil.move(join(self.source_to_track, filename), join(self.folder_destination, filename))
                    self.folder_destination = ''
                print('Sleeping for 5 sec')
                sleep(5)
                print('Awaken')

            except BaseException as B:
                print('error encountered', B)
                continue

    def NormalMode(self):
        """
            Notes:
                #  what: this is Default selection which include
                # * No Deeper Folder traversal.
                # * Avg cpu overhead with check_call at 10 sec.
                # * MultiThreading for each check_call.
                # * considerable priority over other process.
        """
        while True:

            for filename in listdir(self.source_to_track):
                try:
                    self.decider(file=str(filename))

                    if self.folder_destination != '':
                        print('Moving ', filename, 'to', self.folder_destination)
                        shutil.move(join(self.source_to_track, filename),
                                    join(self.folder_destination, filename))
                        self.folder_destination = ''

                except FileNotFoundError:
                    mkdir(self.folder_destination)
                    continue

                except BaseException as B:
                    logging.error(B)
                    continue
            sleep(20)
