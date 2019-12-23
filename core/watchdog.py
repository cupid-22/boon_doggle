import logging
import threading
import shutil
from time import sleep
from os import listdir, path, mkdir, nice
from os.path import join
from multiprocessing import cpu_count
import signal


# TODO:
#  Collective:
#        # Modify the folder creation during file checking.
#        # Sleep according to CPU count
#        # if __main__ code sanitation
#        # More detail in os.nice
#  Next:
#       # Add Description in selection Type for DeepRoots
#       # Add more workouts for Affirmation
#       # Clear Out atleast Affirmation and Gathering.

class FileHandler:

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
        self.source_to_track = path.expanduser(track)
        self.folder_destination = ''
        self._priority = None

    def tracker(self):
        """
        Notes: This function does initial setup of the program and then initiate the run.

        Raises: Error if any.
        """
        try:
            self.GatheringInfo()
            self.AffirmingSetting()

            if self.selection_type == 0:
                self.NormalMode()

            elif self.selection_type == 1:
                self.DeepRootMode()

            else:
                exit('!! No Selection Captured !!')

        except BaseException as B:
            logging.info(B)
            raise B

    def decider(self, file):
        try:
            ext = file.lower().strip().rpartition('.')[-1]
            if ext in ["pdf", 'txt', "docx", "doc", "odt", "rtf", "xlsx", "csv", 'gif', 'wps', 'wpd', 'ppt', 'pptx',
                       'xls']:
                self.folder_destination = path.expanduser('~/Documents/')
                # TODO Log here
            elif ext in ['sh', 'py', 'java']:
                self.folder_destination = path.expanduser('~/Documents/ProjectFile/')
                # TODO Log here
            elif ext in ['zip', 'tar', '7z']:
                self.folder_destination = path.expanduser('~/Documents/Compressed/')
                # TODO Log here
            elif ext in ["png", "jpg", "jpeg", 'gif', 'bmp', 'ico', 'ps', 'svg']:
                self.folder_destination = path.expanduser('~/Pictures/')
                # TODO Log here
            elif ext in ["3g2", "3gp", "avi", "flv", "h264", "m4v", "mkv", "mov", "mp4", "mpg", 'mpeg', 'wmv', 'mov', ]:
                self.folder_destination = path.expanduser('~/Videos/')
                # TODO Log here
            elif ext in ["m4a", "mid", "mp3", "mpa", "wav", "wma", ]:
                self.folder_destination = path.expanduser('~/Music/')
                # TODO Log here
            else:
                # TODO Log here
                pass

        except FileNotFoundError:
            mkdir(self.folder_destination, mode=777)
            return True

        except BaseException as B:
            raise B

    def DeepRootMode(self):
        """
            Notes:
                #  what: this is DeepRoot selection mode which include
                # * Deeper Folder traversal Depth [Default: Two folder].
                # * Above Avg cpu overhead with check_call at 8 sec [ Has to check in deeper nodes ].
                # * MultiThreading for each check_call.
                # * considerable above priority over other process.
        """

        for filename in listdir(self.source_to_track):
            try:
                self.decider(file=str(filename))
                if path.isdir(filename):
                    continue
                if self.folder_destination != '':
                    shutil.move(join(self.source_to_track, filename), join(self.folder_destination, filename))
                    self.folder_destination = ''
                print('Sleeping for 5 sec')
                sleep(5)
                print('Awaken')

            except FileNotFoundError:
                mkdir(self.folder_destination)
                continue

            except BaseException as B:
                print('error encountered', B)
                pass

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

    def AffirmingSetting(self):
        """
        Notes: This function makes final settings opted by user, all this setting are then passed and utilized during
                file catching process.

        Returns: Nothing

        """

        # what :- Setting the nice(Priority) value to the program [Default = 10]
        # why :- this is done to make the code more or less persistent over the base system
        # how :- value of niceness is decided by program according to the mode of selection.
        nice(self._priority)

    def GatheringInfo(self):

        if self.mode == 0:
            print(cpu_count())
            logging.info('... Working Under Normal Mode (Default) ...')
            self._priority = 10

        elif self.mode == 1:
            logging.info('... Working Under Daemon Mode ...')
            self._priority = -15

        elif self.mode == 2:
            logging.info('... Working Under Super Persistent Mode ...')
            self._priority = -18

        elif self.mode == 3:
            logging.info('... Working Under Power Saving Mode ...')
            self._priority = 12

        else:
            logging.info('No mode found switching to default Normal Mode')
            self._priority = -3


def validateParams(s_user, s_mode, s_track):
    try:
        # Folder Validation
        if not isinstance(str, s_track):
            raise AssertionError('Folder should be provided as string')
        if not path.exists(s_track):
            resp = bool(input('Folder is out of sight would you like to create it (0/1) ?'))
            if resp:
                try:
                    mkdir(s_track)
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


if __name__ == '__main__':
    try:

        try:

            def handler(signum, frame):
                raise TimeoutError("Couldn't fetch response!")


            signal.signal(signal.SIGALRM, handler)

            signal.alarm(1)
            prompt_available = input('Would you like to go with defaults (0/1): ')
            signal.alarm(0)

        except TimeoutError as S:
            prompt_available = 1

        if prompt_available == 0:
            selection_user = int(input('Enter the selection type: '))
            selection_mode = int(input('Enter the execution mode: '))
            selection_track = str(input('Enter folder to track: '))

            try:
                validateParams(selection_user, selection_mode, selection_track)

            except TypeError as E:
                logging.error('Assertion Failed for param {0}'.format(E.args[0]))
                exit('watchdog exited with code 0')

            except AssertionError as A:
                logging.error('Assertion Failed for param {0}'.format(A.args[0]))
                exit('watchdog exited with code 0')

            Handler = FileHandler(selection=selection_user, mode=selection_mode, track=selection_track)
            threading.Thread(target=Handler.tracker())
        else:

            Handler = FileHandler()

            log_format = "%(asctime)s: %(message)s"
            logging.basicConfig(format=log_format, level=logging.INFO, datefmt="%H:%M:%S")

            threading.Thread(target=Handler.tracker())

    except BaseException as B:
        logging.critical(msg='\nwatchdog exited with return code 0\n' + str(B))
