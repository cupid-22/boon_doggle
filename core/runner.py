from .watchdog import Organiser
import signal
import threading
from support import assigner, vacuum, judge

import logging


class Runner(Organiser):
    def __init__(self):
        super().__init__()
        self.MoperObj = vacuum.Moper()

    def tracker(self):
        """
        Notes: This function does initial setup of the program and then initiate the run.

        Raises: Error if any.
        """
        try:
            Walrus = assigner.Checker()
            Walrus.GatheringInfo()
            Walrus.AffirmingSetting()

            if self.selection_type == 0:
                self.MoperObj.NormalMode()

            elif self.selection_type == 1:
                self.MoperObj.DeepRootMode()

            else:
                exit('!! No Selection Captured !!')

        except BaseException as B:
            logging.error(B)
            raise B

    def classifier(self):
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

                judge.Porter().validateParams(selection_user, selection_mode, selection_track)

                Organiser(selection=selection_user, mode=selection_mode, track=selection_track)
            else:

                log_format = "%(name)s - %(levelname)s - %(message)s"
                logging.basicConfig(format=log_format, level=logging.INFO, datefmt="%H:%M:%S", filename='error.log')
                logging.warning('This is the level1')
            threading.Thread(target=self.tracker())

        except TypeError as E:
            logging.error('Assertion Failed for param {0}'.format(E.args[0]))
            exit('watchdog exited with code 0')

        except AssertionError as A:
            logging.error('Assertion Failed for param {0}'.format(A.args[0]))
            exit('watchdog exited with code 0')
