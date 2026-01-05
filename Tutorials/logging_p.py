from loguru import logger

# Configure logger to provide clean and informative output.
# This removes the default loguru handler and adds a new one with a better format.
logger.remove()
logger.add(
    "file.log",
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
    level="INFO"
)
logger.add(
    lambda msg: print(msg, end=''),
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO"
)


def process_value(val):
    """
    Processes the integer value and logs messages based on its range.
    """
    if val is None:
        logger.error("Processing cannot continue because the value was not a valid integer.")
        return

    if 0 <= val < 1000:
        logger.info(f"The value {val} is within the valid range (0-999).")
    elif val >= 1000:
        logger.info(f"The value {val} is greater than or equal to 1000.")
    else:
        logger.warning(f"The value {val} is negative, which is unexpected.")


def main():
    """
    Main function to get user input and run the processing logic.
    """
    val = None  # Initialize val to ensure it exists outside the try block
    try:
        # Professional and clear prompt for user input
        val_input = input("Please enter an integer value: ")
        val = int(val_input)
    except ValueError:
        # Log a clear error message for invalid input
        logger.error(f"Invalid input: '{val_input}' is not a valid integer.")

    process_value(val)


if __name__ == "__main__":
    logger.info("Starting the script.")
    main()
    logger.info("Script finished.")
