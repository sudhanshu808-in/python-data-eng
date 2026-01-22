# Import the 'logger' object from the loguru library.
# Loguru is a Python library aimed at making logging simple and enjoyable.
from loguru import logger

# --- Logger Configuration ---
# It's a good practice to configure the logger at the beginning of the script.

# The remove() method is called to remove the default handler that Loguru automatically adds.
# This gives you full control over the logging setup.
logger.remove()

# Add a new handler to log messages to a file named "file.log".
# - format: Defines the structure of the log messages.
# - level: Sets the minimum level of messages to be logged by this handler (e.g., "INFO", "DEBUG", "ERROR").
logger.add(
    "file.log",
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
    level="INFO"
)

# Add another handler to print log messages to the console (stdout).
# - lambda msg: print(msg, end=''): A simple function to output the message without an extra newline.
# - format: This format uses special tags for colors (e.g., <green>, <level>) to make the output more readable.
# - level: Also set to "INFO" for this handler.
logger.add(
    lambda msg: print(msg, end=''),
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO"
)


def process_value(val):
    """
    Processes the integer value and logs messages based on its range.
    This function demonstrates logging at different levels (ERROR, INFO, WARNING).
    """
    # Check if the value is None, which indicates a failure in input conversion.
    if val is None:
        logger.error("Processing cannot continue because the value was not a valid integer.")
        return

    # Log different messages based on the value's range.
    if 0 <= val < 1000:
        logger.info(f"The value {val} is within the valid range (0-999).")
    elif val >= 1000:
        logger.info(f"The value {val} is greater than or equal to 1000.")
    else:
        # A 'warning' is appropriate for unexpected but non-critical situations.
        logger.warning(f"The value {val} is negative, which is unexpected.")


def main():
    """
    Main function to get user input and run the processing logic.
    """
    val = None  # Initialize val to ensure it exists outside the try block
    try:
        # Prompt the user for an integer value.
        val_input = input("Please enter an integer value: ")
        # Convert the user's input string to an integer.
        val = int(val_input)
    except ValueError:
        # If int() fails, it raises a ValueError.
        # This is the correct place to log an error about invalid input.
        logger.error(f"Invalid input: '{val_input}' is not a valid integer.")

    # Call the processing function with the (potentially None) value.
    process_value(val)


# The __name__ == "__main__" block is standard Python practice.
# It ensures that the code inside it only runs when the script is executed directly
# (not when it's imported as a module into another script).
if __name__ == "__main__":
    logger.info("Starting the script execution.")
    main() # Execute the main logic of the script.
    logger.info("Script has finished its execution.")