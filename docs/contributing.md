# Contributing

Welcome! If you'd like to contribute, join the [#wiki](https://discord.com/channels/852389089268858922/1020129101614420081) channel on the Discord server and ask what you do to help or let us know what changes you want to make.

If you aren't familiar with creating pull requests on GitHub, see [this quick video tutorial](https://www.youtube.com/watch?v=jRLGobWwA3Y).

## Setup

1. [Install Python](https://www.python.org/downloads/) 3.9 or later
2. [Install Git](https://github.com/git-guides/install-git)
3. Clone the repository and install requirements:

```sh
git clone https://github.com/Hypercubers/hypercubing.xyz
cd hypercubing.xyz
python3 -m pip install -r requirements.txt --user
```

Run `python3 -m mkdocs serve` and go to <http://127.0.0.1:8000/> in your web browser. As you edit files, the page will automatically refresh to show your changes.

## File layout

Markdown files should have lowercase names, with hyphens to separate words. Choose shorter names when possible.

### `.pages`

Some folders have a `.pages` file in them, which changes the order of pages in the navigation sidebar on the left. This uses the [mkdocs-awesome-pages-plugin](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin). Most of the time, you shouldn't have to worry about this.

## Syntax

This site uses [Markdown](https://www.markdownguide.org/basic-syntax/).

For linking between files within the site, use an absolute link like this with no trailing `.md`:

```md
[Melinda's physical 2^4^](/puzzles/physical/2x2x2x2) was the first 4D puzzle to have a 3D physical design.
```

This site uses the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme; in particular, this gives us [admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/), [tables](https://squidfunk.github.io/mkdocs-material/reference/data-tables/), [footnotes](https://squidfunk.github.io/mkdocs-material/reference/footnotes/), and [subscripts & superscripts](https://squidfunk.github.io/mkdocs-material/reference/formatting/#sub-and-superscripts). We also have MathJax, which uses `$` symbols:

```
The $n$th Fibonacci number is given by $F_n = F_{n-1} + F_{n-2}$.
```

The $n$th Fibonacci number is given by $F_n = F_{n-1} + F_{n-2}$.

## Adding images

Right now, we don't have a good solution for hosting images. You have a few options:

- For small images, add them in `docs/assets/images/`.
- For videos or larger images, use an external host or [GitHub's CDN](https://gist.github.com/NawalJAhmed/2168f7659c08b6a033e7f6daf8db69a6).

When including any image, be sure to include a brief text description of the image for screen readers. For example:

```md
![Erno Rubik inspecting Melinda's 2x2x2x2](/assets/images/ErnoInspects2222.jpg)
```

## Abbreviations

Abbreviations are listed in `includes/abbreviations.md`. Be careful adding new ones, lest you create another [Grant Standingslice incident](/jokes#grant-standingslice).
