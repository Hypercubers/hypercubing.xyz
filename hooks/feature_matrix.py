import re


MISSING_ICON = ':material-close:'

FEATURES = [
    [
        "No mouse controls",
        ('m', "Mouse controls", ':material-mouse:'),
    ],
    [
        "No keyboard controls",
        ('k', "Keyboard controls", ':material-keyboard:'),
        ('K', "Customizable keyboard controls", ':material-keyboard-settings:'),
    ],
    [
        "No piece finding by color",
        ('s', "Piece finding by color", ':material-magnify:'),
    ],
    [
        "No piece filters",
        ('f', "Piece filters", ':material-eye:'),
    ],
    [
        "No timer",
        ('t', "Timer", ':material-timer:'),
    ],
    [
        "No macros",
        ('M', "Macros", ':material-script-text-play:'),
    ],
    [
        "No text input for moves",
        ('T', "Text input for moves", ':material-form-textbox:'),
    ],
    [
        "No color customization",
        ('c', "Color customization", ':material-palette-swatch:'),
    ],
    [
        "No custom puzzles",
        ('p', "Custom puzzles", ':material-pencil-plus:'),
    ],
    [
        "No VR support",
        ('v', "VR support", ':material-virtual-reality:'),
    ],
]

PLATFORMS = [
    [
        "Does not run on Windows",
        ('w', "Runs on Windows", ':material-microsoft-windows:'),
    ],
    [
        "Does not run on Linux",
        ('l', "Runs on Linux", ':material-linux:'),
    ],
    [
        "Does not run on macOS",
        ('a', "Runs on macOS", ':material-apple:'),
    ],
    [
        "Does not run in browser",
        ('b', "Runs in browser", ':material-web:'),
    ],
]


def capitalize(s):
    return s[0].upper() + s[1:]


def make_feature_row(feature_set):
    def repl(m):
        out = ''
        this = m.group(1)
        if len(this) != len(feature_set):
            raise Exception(f"expected {this!r} to have {len(feature_set)}"
                            f" chars but it has {len(this)}")
        for this_char, feature_options in zip(this, feature_set):
            for feat_char, feat_name, feat_icon in feature_options[1:]:
                if this_char == feat_char:
                    out += ' ' + feat_icon + \
                        f'{{title="{feat_name}"}}'
                    break
            else:
                feat_chars = [c for c, _, _ in feature_options[1:]]
                if this_char == '_':
                    out += ' ' + MISSING_ICON + \
                        f'{{.hidden title="{feature_options[0]}"}}'
                else:
                    raise Exception(f"expected one of {feat_chars!r}"
                                    f" or '_'; got {this_char!r}")
        return out

    return repl


def on_page_markdown(md, *, page, **kwargs):
    if page.title == 'Software':
        md = re.sub(r'%features{([a-zA-Z_-]*)}',
                    make_feature_row(FEATURES), md)
        md = re.sub(r'%platforms{([a-zA-Z_-]*)}',
                    make_feature_row(PLATFORMS), md)
    return md
    # # if the × is (probably) between < and > it is probably alt text
    # # temporarily replace it with this private use character
    # old_html = ''
    # while old_html != html:
    #     # do it multiple times to compensate for overlapping regexes
    #     old_html = html
    #     html = re.sub(r'(<[^>]*?)×([^>]*?>)', r'\1'+'\ue000'+r'\2', html)
    # html = re.sub(r'×', '<span data-replace="&times;">x</span>', html)
    # html = re.sub('\ue000', '&times;', html)
    # return html
