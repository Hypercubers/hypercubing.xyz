from collections import defaultdict
from dataclasses import dataclass
from datetime import timedelta
from typing import List, Optional
import csv
import math
import mkdocs_gen_files
import re
import yaml

COLUMNS_ORDER = [
    'event',
    'rank',
    'solver',
    'time',
    'date',
    'program',
]


def COLUMNS_INFO(event): return {
    'event': ("Event", ':---'),
    'rank': ("Rank", '---:'),
    'solver': ("Name", ':--:'),
    'time': (formats[event.format]['header'], '---:'),
    'date': ("Date", ':--:'),
    'program': ("Program", ':--:'),
}


def recode(s):
    # return s.encode('cp1252').decode('utf8') # it worked on my machine :'
    return s


def get_template(filename):
    with open(f'leaderboards/templates/{filename}') as f:
        return f.read()


def format_time(duration) -> str:  # duration: timedelta | int
    # duration can be timedelta (time) or int (movecount for fmc)
    def unit(s):
        return f'<small>{s}</small>'

    if isinstance(duration, int):
        return f"{duration:,}".replace(',', '\u2009')

    millis = int(duration.total_seconds() * 1000)
    seconds, millis = divmod(millis, 1000)
    millis_str = f"{millis:03}{unit('ms')}"

    minutes, seconds = divmod(seconds, 60)
    if minutes == 0:
        return f"{seconds}{unit('s')} {millis_str}"
    seconds_str = f"{seconds:02}{unit('s')}"

    hours, minutes = divmod(int(minutes), 60)
    if hours == 0:
        return f"{minutes}{unit('m')} {seconds_str} {millis_str}"
    minutes_str = f"{minutes:02}{unit('m')}"

    days, hours = divmod(int(hours), 24)
    if days == 0:
        return f"{hours}{unit('h')} {minutes_str} {seconds_str} {millis_str}"
    hours_str = f"{minutes:02}{unit('h')}"

    return f"{days:,}{unit('d')} {hours_str} {minutes_str} {seconds_str} {millis_str}".replace(',', '\u2009')


class Solve:
    def __init__(self,
                 date: str,
                 link: str,
                 time: str,
                 puzzle: str,
                 format: str,
                 solver: str,
                 program: str = '-') -> None:
        self.date = date
        if link and 'http' not in link:
            self.link = f'https://youtu.be/{link}'
        else:
            self.link = link
        self.time = parse_time(time)
        # self.puzzle = puzzles[puzzle]
        # self.format = formats[format]
        self.event = puzzles[puzzle]['events'][format]
        self.solver = solvers[solver]
        self.program = program
        self.solver.solves_by_event[self.event.id].append(self)
        self.rank = None
        formatted_time = format_time(self.time)
        self._cell_contents = {
            'date': self.date,
            'time': f'[{formatted_time}]({self.link})' if link else formatted_time,
            'event': self.event.name,
            'program': self.program,
            'solver': f'[{self.solver.name}]({self.solver.relative_file_path})',
        }

    def cell_contents(self, header):
        if header == 'rank':
            if self.rank is None:
                return ''
            emoji = ''
            # if 1 <= self.rank <= 3:
            #     emoji = [
            #         ':first_place: ',
            #         ':second_place: ',
            #         ':third_place: ',
            #     ][self.rank-1]
            if self.rank == 1:
                emoji = ':trophy-gold-hypercube: '
            elif self.rank == 2:
                emoji = ':trophy-silver-hypercube: '
            elif self.rank == 3:
                emoji = ':trophy-bronze-hypercube: '
            return emoji + str(self.rank)
        else:
            return self._cell_contents[header]


class Event:
    def __init__(self, puzzle: str, format: str, name: str) -> None:
        self.puzzle = puzzle
        self.format = format
        self.name = name
        self.best_solves = []
        self.record_history = []
        self.has_tab = False

    @property
    def file_path(self):
        return 'leaderboards/' + self.relative_file_path

    @property
    def relative_file_path(self):
        return f'puzzle/{self.puz_id}/{self.format}.md'

    @property
    def id(self):
        return (self.puzzle, self.format)


class Solver:
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = recode(name)
        self.solves_by_event = defaultdict(list)

    def get_best_solve_of(self, event: Event) -> Optional[Solve]:
        solves_list = self.solves_by_event[event.id]
        if solves_list:
            return min(self.solves_by_event[event.id], key=lambda s: s.time)
        else:
            return None

    @property
    def file_path(self):
        return 'leaderboards/' + self.relative_file_path

    @property
    def relative_file_path(self):
        return f'solvers/{self.user_id}.md'


# Load solvers from YAML
with open('leaderboards/solvers.yml') as file:
    solvers = {user_id: Solver(user_id, name)
               for user_id, name in yaml.load(file.read(), Loader=yaml.Loader).items()}

# Load formats from YAML
with open('leaderboards/formats.yml') as file:
    formats = yaml.load(file.read(), Loader=yaml.Loader)


def populate_puzzles(tab):
    if 'name' not in tab:
        raise Exception(f'tab {tab} has no name')
    if 'contents' in tab:
        for subtab in tab['contents']:
            populate_puzzles(subtab)
    elif 'puz' in tab:
        puzzles[tab['puz']] = {'name': recode(tab['name'])}
    else:
        raise Exception(f"missing 'contents' or 'puz' in tab {tab['name']}")


# Load tabs and puzzles from YAML and create events
with open('leaderboards/tabs.yml') as tabs_file:
    tab_config = yaml.load(tabs_file.read(), Loader=yaml.Loader)
    puzzles = {}
    for tab in tab_config:
        populate_puzzles(tab)
    for puzzle in puzzles:
        puzzles[puzzle]['events'] = {format: Event(puzzle, format, f'{puzzles[puzzle]["name"]} {
                                                   formats[format]["name"]}') for format, data in formats.items()}


def parse_time(s):
    if m := re.match(r'(\d+)mv', s):
        return int(m[1])
    m = re.match(
        r'(?:(\d+)d\s*)?(?:(\d+)h\s*)?(?:(\d+)m\s*)?(?:(\d+(?:\.\d+)?)s)', s)
    return timedelta(
        days=int(m[1] or '0'),
        hours=int(m[2] or '0'),
        minutes=int(m[3] or '0'),
        seconds=float(m[4]),
    )


# Load solves from CSV
with open('leaderboards/solves.csv') as file:
    reader = csv.reader(file)
    headers = [str.strip(s) for s in next(reader)]
    all_solves = [Solve(**dict(zip(headers, map(str.strip, line))))
                  for line in reader]


# For each puzzle, get the best solve from each solver and compute ranks.
for puzzle in puzzles.values():
    for event in puzzle['events'].values():
        for solver in solvers.values():
            s = solver.get_best_solve_of(event)
            if s:
                event.best_solves.append(s)
        event.best_solves.sort(key=lambda s: s.time)
        for i, s in enumerate(event.best_solves):
            s.rank = i + 1

for curSolve in all_solves:
    if len(curSolve.event.record_history) == 0:
        curSolve.event.record_history.insert(0, curSolve)
    elif curSolve.event.record_history[0].time > curSolve.time:
        curSolve.event.record_history.insert(0, curSolve)


def make_table(rows, *, indent):
    return '\n'.join(f"{' ' * indent}| {' | '.join(row)} |" for row in rows) + '\n\n'


def make_solves_table(solves, *, indent, exclude=None):
    if not solves:
        return ''

    columns = COLUMNS_ORDER.copy()
    columns_info = COLUMNS_INFO(solves[0].event)
    if exclude:
        for col in exclude:
            columns.remove(col)
    header_rows = [
        [columns_info[col][0] for col in columns],
        [columns_info[col][1] for col in columns],
    ]
    content_rows = [
        [solve.cell_contents(col) for col in columns]
        for solve in solves
    ]
    return make_table(header_rows + content_rows, indent=indent)


def make_tabbed_leaderboards(tab_config, make_tab_contents, *, indent=0) -> str:
    pre = ' ' * indent
    indent += 4
    s = ''
    for tab in tab_config:
        tab_name = tab.get('name')
        if 'contents' in tab:
            tab_contents = make_tabbed_leaderboards(
                tab['contents'],
                make_tab_contents,
                indent=indent,
            )
        elif 'format' in tab:
            tab_contents = make_tab_contents(tab, indent=indent)
        elif 'puz' in tab:
            subtabs = [{**tab, 'format': f, **format}
                       for f, format in formats.items()]
            tab_contents = make_tabbed_leaderboards(
                subtabs,
                make_tab_contents,
                indent=indent,
            )
        else:
            raise Exception(f'not a valid tab {tab}')

        if not tab_contents:
            continue

        # If a puzzle name has any special characters, we might have to escape it
        # better here. For now just surrounding it with double quotes is fine.
        # gotta escape!
        s += f'{pre}=== "{recode(tab_name)}"\n\n{tab_contents}'
    return s


def make_solvers_list(*, indent=0) -> str:
    pre = ' ' * indent
    s = ''
    for solver in sorted(solvers.values(), key=lambda s: s.name):
        s += f'{pre}- [{solver.name}]({solver.relative_file_path})\n'
    return s + '\n'


def make_solver_page_contents(solver: Solver, tab_config, *, indent=0) -> str:
    s = ''
    s += '## Rankings\n\n'
    solves = [solver.get_best_solve_of(event) for puzzle in puzzles.values()
              for event in puzzle['events'].values()]
    s += make_solves_table(
        [s for s in solves if s],
        indent=indent,
        exclude=['solver'],
    )
    s += '## History\n\n'

    def make_solver_tab_contents(tab, *, indent=0):
        event = puzzles[tab['puz']]['events'][tab['format']]
        exclude = ['solver', 'event'] + tab.get('exclude', [])
        return make_solves_table(
            solver.solves_by_event[event.id][::-1],
            indent=indent,
            exclude=exclude,
        )

    s += make_tabbed_leaderboards(
        tab_config,
        make_solver_tab_contents,
    )
    return s


def create_mkdocs_file_from_template(path: str, template: str, contents: str, **kwargs):
    with mkdocs_gen_files.open(path, 'w') as out_file:
        print(get_template(template).format(
            **kwargs) + '\n' + contents, file=out_file)


def make_main_leaderboard_tab_contents(tab, *, indent=0):
    event = puzzles[tab['puz']]['events'][tab['format']]
    exclude = ['event'] + tab.get('exclude', [])
    return make_solves_table(
        event.best_solves,
        indent=indent,
        exclude=exclude,
    )


# Generate main leaderboards page
create_mkdocs_file_from_template(
    path='leaderboards/index.md',
    template='leaderboards.md',
    contents=make_tabbed_leaderboards(
        tab_config, make_main_leaderboard_tab_contents),
)

# Generate solver list (not necessary because the nav does it automatically)
# create_mkdocs_file_from_template(
#     'leaderboards/solvers.md',
#     'solvers.md',
#     make_solvers_list(),
# )

# Generate solver pages
for solver in solvers.values():
    create_mkdocs_file_from_template(
        path=solver.file_path,
        template='solver.md',
        contents=make_solver_page_contents(solver, tab_config),
        name=solver.name,
    )


def make_history_leaderboard_tab_contents(tab, *, indent=0):
    event = puzzles[tab['puz']]['events'][tab['format']]
    exclude = ['rank', 'event'] + tab.get('exclude', [])
    return make_solves_table(
        event.record_history,
        indent=indent,
        exclude=exclude,
    )


create_mkdocs_file_from_template(
    path='leaderboards/history.md',
    template='history.md',
    contents=make_tabbed_leaderboards(
        tab_config, make_history_leaderboard_tab_contents),
)

WRs = []
for puzzle in puzzles:
    for format in formats:
        event = puzzles[puzzle]['events'][format]
        if event.best_solves:
            WRs.append(event.best_solves[0])

create_mkdocs_file_from_template(
    'leaderboards/records.md',
    'records.md',
    make_solves_table(WRs, indent=0, exclude=['rank']),
)
