#!/usr/bin/env python3

from glob import glob
from os import path
import re

LINK_PATTERN = re.compile(r'\]\(([^()]*)\)')

IGNORE_PREFIXES = [
    'http',  # don't try to validate external links
    '/leaderboards',  # don't try to validate leaderboard links
    '/assets/',  # don't try to validate asset links
]

found_broken = False


def warn(filename, link_target, msg):
    global found_broken
    found_broken = True
    warning = f"In file {filename}, the link to {link_target!r}"


for filename in glob("docs/**.md", recursive=True):
    with open(filename, 'r') as f:
        for m in LINK_PATTERN.finditer(f.read()):
            link_target = m.group(1)

            if any(link_target.startswith(s) for s in IGNORE_PREFIXES):
                continue

            if '\\' in link_target:
                warn(filename, link_target, "should use `/` instead of `\`")
            elif not link_target.startswith('/'):
                warn(filename, link_target, "should start with `/`")
            elif link_target.endswith('.md'):
                warn(filename, link_target, "doesn't need to end with `.md`")
            else:
                dir_exists = path.isfile(f'docs{link_target}/index.md')
                file_exists = path.isfile(f'docs{link_target}.md')
                if not dir_exists and not file_exists:
                    warn(filename, link_target, "is broken")

if not found_broken:
    print("All links look good!")
