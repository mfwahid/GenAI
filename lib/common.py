import datetime


def get_new_filename(prefix, type):
    # Get the current date and time
    now = datetime.datetime.now()

    # Convert the date and time to a string
    date_string = now.strftime("%Y-%m-%d-%H-%M-%S")

    # Append the string to the file name
    file_name = prefix + "-" + date_string + "." + type

    return file_name
