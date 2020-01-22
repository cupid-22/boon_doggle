from core.watchdog import Organiser, nice, logging


class Checker(Organiser):
    def __init__(self):
        super().__init__()

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
