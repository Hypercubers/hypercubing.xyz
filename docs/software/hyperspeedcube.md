# Hyperspeedcube

[Hyperspeedcube](https://ajfarkas.dev/hyperspeedcube/) (HSC) is a modern, beginner-friendly 3D and 4D Rubik’s cube simulator with customizable mouse and keyboard controls and advanced features for speedsolving. It’s been used to break numerous speedsolving records and runs on all major operating systems plus the web. Hyperspeedcube was first released in early 2022 and is developed by Andrew Farkas (a.k.a. HactarCE).

![3×3×3×3 with the far cell mid-twist](https://assets.hypercubing.xyz/img/virt/hsc/mid_twist.png){ width="32%" }
![3×3×3×3 near the end of F2L-b with many tools and settings windows open](https://assets.hypercubing.xyz/img/virt/hsc/tools.png){ width="32%" }
![Solved 2×2×2](https://assets.hypercubing.xyz/img/virt/hsc/solved_2x2x2.png){ width="32%" }

## Download/installation [![Release badge]][Release link]

<div class="grid cards" markdown>

-   [:material-microsoft-windows:{.lg .middle}:material-linux:{.lg .middle}:material-apple:{.lg .middle} **Download Hyperspeedcube**][hsc-download]

-   [:material-web:{.lg .middle} **Use Hyperspeedcube online**][hsc-web]

</div>

[Release badge]: https://img.shields.io/github/v/release/HactarCE/Hyperspeedcube
[Release link]: https://github.com/HactarCE/Hyperspeedcube/releases/latest
[hsc-download]: https://ajfarkas.dev/hyperspeedcube/
[hsc-web]: https://hypercubing.xyz/hyperspeedcube/

HSC does not have an installer. On Windows, open `hyperspeedcube_win64.zip` and move `hyperspeedcube.exe` out of  to a folder on your computer.

!!! warning "Features missing from the web version"

    - Saving & loading logs to file (can still save/load via clipboard)
    - Awareness of alternate keyboard layouts
    - Antialiasing

### Troubleshooting

If none of the instructions below help, join the [Hypercubers Discord server][discord] and start a thread in the `#❓help` forum. Mention in your post that you've read the FAQ.

[discord]: https://discord.gg/xxFvfyx89p

#### Windows

??? failure "My antivirus thinks Hyperspeedcube is malicious"

    Try opening the Windows Security app, and digging around in the settings there to disable it, then try the download again.

??? failure ""Windows protected your PC""

    > Microsoft Defender SmartScreen prevented an unrecognized app from starting. Running this app might put your PC at risk.

    Click **More info** and then **Run anyway**.

    In order to prevent that message from appearing, Hactar would have to spend a lot of money to buy a Microsoft developer license and go through a lot of hassle every time there is a new release of HSC. You'll only have to click through the warnings once.

??? failure ""The program can't start because VCRUNTIME140.dll is missing from your computer.""

    You need to install the [Microsoft Visual C++ Redistributable](https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist). Here is a [direct download](https://aka.ms/vs/17/release/vc_redist.x64.exe).

??? failure ""Hyperspeedcube crashed. A crash report has been saved to ...""

    First, make sure your graphics drivers are up-to-date! This is the most common cause of Hyperespeedcube crashes. Here is a [video tutorial](https://www.youtube.com/watch?v=rkZvrzr5yKM) if you don't know how to do that.

    If you still get an error message, then follow these steps:

    1. Press <kbd>:material-microsoft-windows:</kbd>+<kbd>R</kbd>, type `%LocalAppData%`, and press <kbd>Enter</kbd>
    2. Open the `Temp` folder
    3. Find the file named in the error message and send it to Hactar either in a [GitHub issue](https://github.com/HactarCE/Hyperspeedcube/issues/new) or a new thread in the `#❓help` forum on [Discord][discord]

#### macOS

??? failure ""'Hyperspeedcube.app' cannot be opened because the developer cannot be verified.""

    > macOS cannot verify that this app is free from malware.

    Go to **System Settings** → **Privacy & Security**, then scroll down to **Security**. Select **App Store and identified developers**, then click **Open Anyway**.

    In order to prevent that message from appearing, Hactar would have to spend a lot of money to buy an Apple developer license and go through a lot of hassle every time there is a new release of HSC.

#### Linux

Check that you have up-to-date graphics drivers installed. If that doesn't help, you're on your own.

If there's any changes you make to the Hyperspeedcube source code to get it working, [please open an issue or PR on GitHub](https://github.com/HactarCE/Hyperspeedcube). If you're able to make an package for HSC for your package manager, please let me know either on Discord or GitHub Issues.

## History

### 1.0

On April 24th, 2020, Hactar wrote a small program called Keyboard Speedcube that simulated a 3^3^ using keybinds inspired by [Ryan Heise's Rubik's Cube Simulator](https://www.ryanheise.com/cube/speed.html). In October 2021, rudimentary 4D support was added and [a screenshot was posted on the Hypercubers Discord server](https://discord.com/channels/852389089268858922/871460012390748241/902389508262228008). A month later, Rowan Fortier asked Hactar if he could receive an early version of the program, and showcased it in a [YouTube video](https://www.youtube.com/watch?v=Wn1y-3EMREQ). Shortly before the video's release, the project was renamed to Hyperspeedcube.

![first mention](https://assets.hypercubing.xyz/img/virt/hsc/keyboard_speedcube.png){width="49%"}
![Early build](https://assets.hypercubing.xyz/img/virt/hsc/face_focus.gif){width="49%"}

The first official release was v0.1.0 in January 2022, featuring customizable keybinds and support for the 3^3^ and 3^4^. Over the next year, many community-requested features were added, including mouse controls and more n^3^ and n^4^ puzzles. (See the [changelog](https://github.com/HactarCE/Hyperspeedcube/blob/main/CHANGELOG.md) for a complete list of releases and changes.)

Hyperspeedcube began to see widespread use after the addition of mouse controls and more advanced piece filters in August 2022, kickstarting the [hyperspeedsolving revolution](/history.md#2022-present-the-hyperspeedsolving-revolution). The web version was released in January 2023.

Shortly after the web version was released, Hactar and Luna began reading the [MPU](/software/magicpuzzleultimate.md) source code, intending to make a tool to ease the process of writing MPU puzzle definitions. Instead, they were able to replicate MPU's puzzle generation algorithms, and Hactar set to work on a new puzzle simulator using this backend. Over the next year, they adapted the algorithm to use [Conformal Geometric Algebra][cga] in the hopes of supporting curved cuts, but this proved too challenging in higher dimensions. Together with Milo, they built a puzzle definition system using [Lua][lua], since it is a well-known programming language with a simple type system that is easy to embed, sandbox, and extend with custom types.

[cga]: https://en.wikipedia.org/wiki/Conformal_geometric_algebra
[lua]: https://en.wikipedia.org/wiki/Lua_(programming_language)

The first dev build of the new version, Hyperspeedcube v2.0.0-pre.1, was released on July 16th, 2023, and supported Lua shape definitions but not twists. As of mid-2024, HSC 2.0 is still in active development.

### 2.0

HSC 2.0 is the next major update in the works, with no set release date as of yet. Below is a list of upcoming features:

- Build nearly any puzzle in 3D to 7D space
- Complete overhaul of the graphics engine
- Built-in timer for speedsolves, including a configurable autosplitter
- Timeline of progress during solve
- More piece filter customization

See [Hactar's website](https://ajfarkas.dev/hyperspeedcube/#future-plans) for more details.

### Development screenshots

#### Early shape generation and twisting prototypes (late 2022)

![Hypercuboid twisted in an incorrect way (2022-10-13)](https://assets.hypercubing.xyz/img/virt/hsc/history/2022-10-13_janky_cuboid.png?width=817&height=671){width="24.5%"}
![3D Jing's pyraminx puzzle, with a popup saying that the program crashed (2022-10-13)](https://assets.hypercubing.xyz/img/virt/hsc/history/2022-10-13_jing_crash.png){width="24.5%"}
![{3}×{5} duoprism (2022-10-13)](https://assets.hypercubing.xyz/img/virt/hsc/history/2022-11-18_duoprism.png){width="24.5%"}
![Uncolored 120-cell puzzle](https://assets.hypercubing.xyz/img/virt/hsc/history/2022-11-18_120_cell.png){width="24.5%"}

#### Graphics debugging (early 2024)

![](https://assets.hypercubing.xyz/img/virt/hsc/history/2024-01-08_debug1.png?width=817&height=671){width="19.5%"}
![](https://assets.hypercubing.xyz/img/virt/hsc/history/2024-02-06_debug2.png){width="19.5%"}
![](https://assets.hypercubing.xyz/img/virt/hsc/history/2024-02-07_debug3.png){width="19.5%"}
![](https://assets.hypercubing.xyz/img/virt/hsc/history/2024-02-17_debug4.png){width="19.5%"}
![](https://assets.hypercubing.xyz/img/virt/hsc/history/2024-02-20_debug5.png){width="19.5%"}

#### UI development (mid 2024)

![Prototype of the global color palette (2024-06-27)](https://assets.hypercubing.xyz/img/virt/hsc/history/2024-06-27_color_palette_prototype.png){width="38%"}
![Concept sketch of the piece filters UI (2024-08-05)](https://assets.hypercubing.xyz/img/virt/hsc/history/2024-08-05_ui_sketch.png){width="26%"}
![First puzzle loaded from a Lua file (2024-08-27)](https://assets.hypercubing.xyz/img/virt/hsc/history/2024-08-27_lua_loading.png){width="33%"}
