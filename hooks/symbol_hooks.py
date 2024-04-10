import re

def on_page_content(html, **kwargs):
    # if the × is (probably) between < and > it is probably alt text
    # temporarily replace it with this private use character
    old_html = ''
    while old_html != html:
        # do it multiple times to compensate for overlapping regexes
        old_html = html
        html = re.sub(r'(<[^>]*?)×([^>]*?>)', r'\1'+'\ue000'+r'\2', html)
    html = re.sub(r'×', '<span data-replace="&times;">x</span>', html)
    html = re.sub('\ue000', '&times;', html)
    return html
