import logging
import shutil
from time import sleep
from os import listdir, mkdir
from os.path import join, isdir, isfile

from .judge import Organiser, Porter


class Moper(Organiser):
    def __init__(self):
        super().__init__()
        self.PorterObj = Porter()

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
                self.PorterObj.decider(file=str(filename))
                if self.PorterObj.folder_destination != '':
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

            for filename in listdir(self.PorterObj.source_to_track):
                try:
                    if not isfile(join(self.PorterObj.source_to_track, filename)):
                        self.PorterObj.Logger(error='{0} is skipped as its not a file'.format(
                            join(self.PorterObj.source_to_track, filename)))
                        continue

                    self.PorterObj.decider(file=str(filename))

                    if self.PorterObj.folder_destination:
                        logging.info('Moving {0} to {1}'.format(filename, self.PorterObj.folder_destination))
                        shutil.move(join(self.PorterObj.source_to_track, filename),
                                    join(self.PorterObj.folder_destination, filename))
                        del self.PorterObj.folder_destination

                except FileNotFoundError:
                    mkdir(self.PorterObj.folder_destination)
                    continue

                except BaseException as B:
                    logging.error(B)
                    continue
            sleep(20)
