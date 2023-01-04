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
    'puzzle',
    'rank',
    'solver',
    'time',
    'date',
    'program',
]
COLUMNS_INFO = {
    'puzzle': ("Puzzle", ':---'),
    'rank': ("Rank", '---:'),
    'solver': ("Name", ':--:'),
    'time': ("Time", '---:'),
    'date': ("Date", ':--:'),
    'program': ("Program", ':--:'),
}


def get_template(filename):
    with open(f'docs/leaderboards/templates/{filename}') as f:
        return f.read()


def format_time(duration: timedelta) -> str:
    def unit(s):
        return f'<small>{s}</small>'

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

    return f"{hours}{unit('h')} {minutes_str} {seconds_str} {millis_str}"


class Solve:
    def __init__(self,
                 date: str,
                 link: str,
                 time: str,
                 puzzle: str,
                 solver: str,
                 program: str = '-') -> None:
        self.date = date
        self.link = link and f'https://youtu.be/{link}'
        self.time = parse_time(time)
        self.puzzle = puzzles[puzzle]
        self.solver = solvers[solver]
        self.program = program
        self.solver.solves_by_puzzle[self.puzzle.puz_id].append(self)
        self.rank = None
        formatted_time = format_time(self.time)
        self._cell_contents = {
            'date': self.date,
            'time': f'[{formatted_time}]({self.link})' if link else formatted_time,
            'puzzle': self.puzzle.name,
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
                emoji = ':trophy: '
            return emoji + str(self.rank)
        else:
            return self._cell_contents[header]


class Puzzle:
    def __init__(self, puz_id: str, name: str) -> None:
        self.puz_id = puz_id
        self.name = name
        self.best_solves = []
        self.has_tab = False

    @property
    def file_path(self):
        return 'leaderboards/' + self.relative_file_path

    @property
    def relative_file_path(self):
        return f'puzzle/{self.puz_id}.md'


class Solver:
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name
        self.solves_by_puzzle = defaultdict(list)

    def get_best_solve_of(self, puzzle: Puzzle) -> Optional[Solve]:
        solves_list = self.solves_by_puzzle[puzzle.puz_id]
        if solves_list:
            return min(self.solves_by_puzzle[puzzle.puz_id], key=lambda s: s.time)
        else:
            return None

    @property
    def file_path(self):
        return 'leaderboards/' + self.relative_file_path

    @property
    def relative_file_path(self):
        return f'user/{self.user_id}.md'


# Load solvers from YAML
with open('docs/leaderboards/solvers.yml') as file:
    solvers = {user_id: Solver(user_id, name)
               for user_id, name in yaml.load(file.read(), Loader=yaml.Loader).items()}


# Load puzzles from YAML
with open('docs/leaderboards/puzzles.yml') as file:
    puzzles = {puz_id: Puzzle(puz_id, name)
               for puz_id, name in yaml.load(file.read(), Loader=yaml.Loader).items()}


def parse_time(s):
    m = re.match(r'(?:(\d+)h\s*)?(?:(\d+)m\s*)?(?:(\d+(?:\.\d+)?)s)', s)
    return timedelta(
        hours=int(m[1] or '0'),
        minutes=int(m[2] or '0'),
        seconds=float(m[3]),
    )


# Load solves from CSV
with open('docs/leaderboards/solves.csv') as file:
    reader = csv.reader(file)
    headers = next(reader)
    all_solves = [Solve(**dict(zip(headers, map(str.strip, line))))
                  for line in reader]


# For each puzzle, get the best solve from each solver and compute ranks.
for puzzle in puzzles.values():
    for solver in solvers.values():
        s = solver.get_best_solve_of(puzzle)
        if s:
            puzzle.best_solves.append(s)
    puzzle.best_solves.sort(key=lambda s: s.time)
    for i, s in enumerate(puzzle.best_solves):
        s.rank = i + 1


def make_table(rows, *, indent):
    return '\n'.join(f"{' ' * indent}| {' | '.join(row)} |" for row in rows) + '\n\n'


def make_solves_table(solves, *, indent, exclude=None):
    if not solves:
        return ''

    columns = COLUMNS_ORDER.copy()
    if exclude:
        for col in exclude:
            columns.remove(col)
    header_rows = [
        [COLUMNS_INFO[col][0] for col in columns],
        [COLUMNS_INFO[col][1] for col in columns],
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
        tab_name = tab.get('name') or puzzles[tab['puz']].name
        if 'contents' in tab:
            tab_contents = make_tabbed_leaderboards(
                tab['contents'],
                make_tab_contents,
                indent=indent,
            )
        elif 'puz' in tab:
            tab_contents = make_tab_contents(tab, indent=indent)
        else:
            raise Exception("missing 'contents' or 'puz' in tab "
                            + repr(tab['name']))

        if not tab_contents:
            continue

        # If a puzzle name has any special characters, we might have to escape it
        # better here. For now just surrounding it with double quotes is fine.
        s += f'{pre}=== "{tab_name}"\n\n{tab_contents}'
    return s


def make_solvers_list(*, indent=0) -> str:
    pre = ' ' * indent
    s = ''
    for solver in sorted(solvers.values(), key=lambda s: s.name):
        s += f'{pre}- [{solver.name}]({solver.relative_file_path})\n'
    return s + '\n'


def make_solver_page(solver: Solver, tab_config) -> str:
    s = f'---\ntitle: {solver.name}\n---\n\n'
    s += '## Rankings\n\n'
    solves = [solver.get_best_solve_of(puzzle)
              for puzzle in puzzles.values()]
    s += make_solves_table(
        [s for s in solves if s],
        indent=0,
        exclude=['solver'],
    )
    s += '## History\n\n'

    def make_solver_tab_contents(tab, *, indent=0):
        puzzle = puzzles[tab['puz']]
        exclude = ['solver', 'puzzle'] + tab.get('exclude', [])
        return make_solves_table(
            solver.solves_by_puzzle[puzzle.puz_id][::-1],
            indent=indent,
            exclude=exclude,
        )

    s += make_tabbed_leaderboards(
        tab_config,
        make_solver_tab_contents,
    )
    return s


def create_mkdocs_file_from_template(path: str, template: str, contents: str):
    with mkdocs_gen_files.open(path, 'w') as out_file:
        print(get_template(template) + '\n' + contents, file=out_file)


# Load tabs from YAML
with open('docs/leaderboards/tabs.yml') as tabs_file:
    tab_config = yaml.load(tabs_file.read(), Loader=yaml.Loader)


def make_main_leaderboard_tab_contents(tab, *, indent=0):
    puzzle = puzzles[tab['puz']]
    exclude = ['puzzle'] + tab.get('exclude', [])
    return make_solves_table(
        puzzle.best_solves,
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

# Generate solver list
create_mkdocs_file_from_template(
    'leaderboards/solvers.md',
    'solvers.md',
    make_solvers_list(),
)

# Generate solver pages
for solver in solvers.values():
    with mkdocs_gen_files.open(solver.file_path, 'w') as out_file:
        print(
            make_solver_page(solver, tab_config),
            file=out_file,
            end='',
        )

# Generate puzzle pages
# for puzzle in
