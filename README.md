# Spotless
A simple script to unclutter your Mac desktop.

![Alt Text](https://media2.giphy.com/media/Y7zc8G30VFqyY7RZU8/giphy.gif)


By default, Spotless will create a `Desktop` folder witin the Desktop, reducing all your files and folders down to one. Witin the newly created folder, items moved from the desktop will be nested in another folder, ordered by date of modifcation.

```
Desktop
  -Desktop
    -2022-10-01
      -Image.png
    -2022-09-20
      -Video.mp4
```

If you'd like to change the path, you can update `new_path` in `spotless.py` with the directory where you would like to store your files.
```
new_path = "/YOUR/NEW/PATH/HERE/"
```

If you opt to have the script move all the files to a single folder on the desktop instead, that folder will be ignored. Files starting with a period will also be ignored.



Now all you need to do is run the script.

```
python spotless.py
```

Requires: Python 3
