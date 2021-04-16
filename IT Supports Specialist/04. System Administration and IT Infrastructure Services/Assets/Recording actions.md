# Recording actions

A common practice for system administrators that work with bug queues or ticketing systems is to include the commands executed and the output obtained in the corresponding bug or ticket. This is recommended if the commands that need to be executed are few and straightforward.

## Script

```
script session.log
```

This will write the contents of session to the session.log file. To stop recording, you can write exit or press `Ctrl-D`. The generated file will be in ANSI format which includes the colors that were displayed on screen. In order to read them, you can use commands like ansi2txt or ansi2html to convert it to plain text or HTML respectively.

## Start-Transcript

```
Start-Transcript -Path C:\Transcript.txt
```

This will write the contents of the session to C:\Transcript.txt. To stop recording call `Stop-Transcript`. The file created is a plain text file where the commands executed and their outputs are stored.

# Recording Graphical Sessions

Performing system administration actions through a Graphical user interface is less common (as it’s harder to automate and to perform remotely), but it’s still something that may happen sometimes.

If you are going to be performing an action that needs to be done graphically and you can document what you are doing, you can use a specialized tool like [recordMyDesktop](http://recordmydesktop.sourceforge.net/about.php) for Linux, or general video tools like [OBS](https://obsproject.com/) or [VLC](https://www.videolan.org/vlc/index.html).