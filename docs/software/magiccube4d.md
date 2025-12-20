# Magic Cube 4D

Magic Cube 4D (MC4D) was one of the first ever programs capable of simulating higher dimensional twisty puzzles. It was first released in 1988 and was developed by Melinda Green, Don Hatch, Jay Berkenbilt, and Roice Nelson.

<figure markdown="span">
  ![3×3×3×3 puzzle in Magic Cube 4D](https://superliminal.com/cube/cube_transp.gif)
  <figcaption>3^4^ puzzle in Magic Cube 4D</figcaption>
</figure>

## Download and installation

Magic Cube 4D requires [Java](https://www.java.com/en/) to be installed. Once you have Java, go to the [Superliminal website](https://superliminal.com/cube/) and click on the `Click here to download MagicCube4D` button. Save the executable `mc4d-4-3-343.jar` file somewhere you will remember, as this file is how you open the program.

### Configuration

To change a puzzle's cell colors, you will have to add a facecolors.txt file to the same directory as the MC4D jar file and list colors within that file.
See the [MC4D FAQ](https://superliminal.com/cube/faq.html#Q16) or the [Hypercubing Message Archive](https://archive.hypercubing.xyz/messages/0730.html) for more details.

## Alternative versions

### Don's version

Don's version contains some 2D puzzles, many 3D puzzles, and some interesting 4D puzzles. It also has a menu for 5D and 6D puzzles, however they don't work when you select them. Don's version can be downloaded directly from his [GitHub release](https://github.com/donhatch/donhatchsw.jar/blob/master/java1.8/donhatchsw.jar).


## Troubleshooting

Try reading [MC4D's FAQ](https://superliminal.com/cube/faq.html) on the superliminal website. If you're still having an issue, try asking for help on the Discord server or mailing list.

??? warning "my computer wants to open the `.jar` file with notepad"
    This means that you haven't installed Java properly. Make sure to get the newest version from [Java's website](https://www.java.com/en/). After the installation, right click on the `mc4d-4-3-343.jar` file, and click `open with Java(TM) Platform SE Binary`.

??? warning "facecolors.txt doesn't change my colors"
    1. Try closing and reopening the program, and then reloading the puzzle using the menu.
    2. If you're on windows and you have show file extensions off in settings, then you may have accidentally named the file `facecolors.txt.txt`. Try renaming it to just `facecolors`. (Alternatively, enable show file extensions in settings)
