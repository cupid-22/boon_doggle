from core.runner import Runner, logging

if __name__ == '__main__':
    try:

        StarWorld = Runner()
        StarWorld.tracker()

    except FileNotFoundError as B:
        logging.exception(msg=' Watchdog exited with return code 0 ({0})'.format(str(B.args[1])), exc_info=True)
    except BaseException as B:
        logging.exception(msg=' Watchdog exited with return code 0 ({0})'.format(str(B)), exc_info=True)

# TODO:
#  Collective:
#       # Modify the folder creation during file checking.
#       # Sleep according to CPU count
#       # More detail in os.nice
#       # Add more workouts for Affirmation [Delayed]
#        ?
#       # Find out a proper documentation way for structure and watchdog README.md file.
#       # More Clear Imports and final documentation of Inheritance and structure
#  Next:
#       + Make more robust file handling {{ decision making in certain situation }}
#       + Understand and change logging overall
#  Cleared
#       $ Resolve Circular import {{ URGENT }} -- CLEARED
#       # Clear Out Code Structure
#       # if __main__ code sanitation
