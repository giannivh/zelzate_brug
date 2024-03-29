"""zelzate_brug utils."""
from __future__ import annotations

from .const import ZB_HTML_TAGS

import re


def try_parse_int_or_default(input, default_value) -> int:
    """Try to parse the given input to an int, or return default value when the given input cannot be parsed."""
    try:
        return int(input)
    except ValueError:
        return default_value

def verify_index_or_default(index, length, default_value) -> int:
    """Return the index if it does not exceed the length, otherwise return default value."""
    if index >= length:
        return default_value
    return index

def remove_html_tags(input) -> str:
    """Remove all HTML tags from the given input."""
    return re.sub(ZB_HTML_TAGS, '', input)

def extract_match_or_default(input, pattern, default_value, prefix = "") -> str:
    """Extract the given pattern from the input, optionally prepending with a prefix."""
    matches = re.search(pattern, input)
    if matches:
        return prefix + matches.group()
    return default_value
