from core.runner import Runner, logging

if __name__ == '__main__':
    try:

        StarWorld = Runner()
        StarWorld.tracker()

    except FileNotFoundError as B:
        logging.critical(msg=' Watchdog exited with return code 0 ({0})'.format(str(B.args[1])))
    except BaseException as B:
        logging.critical(msg=' Watchdog exited with return code 0 ({0})'.format(str(B)))

# TODO:
#  Collective:
#        # Modify the folder creation during file checking.
#        # Sleep according to CPU count
#        # More detail in os.nice
#        # Add more workouts for Affirmation [Delayed]
#        ?
#        # Find out a proper documentation way for structure and watchdog README.md file.
#        # More Clear Imports and final documentation of Inheritance and structure
#  Next:
#       & Make More robust file handling {{ catch cases as replace or not file in normal mode ...}}
#  Cleared
#       $ Resolve Circular import {{ URGENT }} -- CLEARED
#       # Clear Out Code Structure
#       # if __main__ code sanitation
