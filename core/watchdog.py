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
        self.folder_destination = ''
        self._priority = None

