from .runner import Runner, logging

if __name__ == '__main__':
    try:

        StarWorld = Runner()
        StarWorld.tracker()

    except BaseException as B:
        logging.critical(msg='\nWatchdog exited with return code 0\n' + str(B))

# TODO:
#  Collective:
#        # Modify the folder creation during file checking.
#        # Sleep according to CPU count
#        # if __main__ code sanitation
#        # More detail in os.nice
#        # Add more workouts for Affirmation [Delayed]
#  Next:
#       # Clear Out Code Structure
#       # Find out a proper documentation way for structure and watchdog README.md file.
