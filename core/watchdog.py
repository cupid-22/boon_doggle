import logging
from os.path import expanduser


class Organiser(object):

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
        self.folder_destination = None
        self._priority = None

    def Logger(self, warning=None, error=None):
        try:
            # Create a custom logger
            logger = logging.getLogger(__name__)

            # Create handlers
            c_handler = logging.StreamHandler()
            f_handler = logging.FileHandler('file.log')
            c_handler.setLevel(logging.WARNING)
            f_handler.setLevel(logging.ERROR)

            # Create formatters and add it to handlers
            c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
            f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            c_handler.setFormatter(c_format)
            f_handler.setFormatter(f_format)

            # Add handlers to the logger
            logger.addHandler(c_handler)
            logger.addHandler(f_handler)
            if warning:
                logger.warning(warning)
            elif error:
                logger.error(error)
        except BaseException as A:
            logger.error(A)