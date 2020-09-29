import re


def cleanup_string(q: str) -> str:
    """ Performs initial cleanup removing superfluous characters """
    pattern = '[^a-zA-Z0-9" ]+'
    return re.sub(pattern, '', q).strip().casefold()
