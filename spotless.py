# Spotless
import os
from pathlib import Path
from datetime import datetime

def main():
    # Set paths - desktop & new path
    # Include trailing slash '/'
    initial_path = os.path.expanduser("~/Desktop/")
    new_path = initial_path + "Desktop/"

    # File count for stats
    file_count = 0

    for desktop_items in os.listdir(initial_path):
        # Exclude '. files' & new folder if created on desktop
        if not desktop_items.startswith('.') and not desktop_items == os.path.basename(os.path.normpath(new_path)):
            # Get modification time of file
            mod_epoch = os.stat('{}{}'.format(initial_path, desktop_items)).st_mtime

            # Format date from epoch YYYY-MM-DD
            mod_date = datetime.fromtimestamp(mod_epoch).strftime("%Y-%m-%d")

            # Check if new_path exists - if not, create it
            if not os.path.exists("{}".format(new_path)):
                os.mkdir('{}'.format(new_path))

            # Create new folder with date if folder does not exist
            if not os.path.exists("{}/{}".format(new_path, mod_date)):
                os.mkdir('{}/{}'.format(new_path, mod_date))

            # Move files to new folder with mod date
            Path('{}{}'.format(initial_path, desktop_items)).rename('{}{}/{}'.format(new_path, mod_date, desktop_items))

            # Update moved file count
            file_count += 1

    print("Files moved: {}".format(str(file_count)))


if __name__ == '__main__':
    main()
