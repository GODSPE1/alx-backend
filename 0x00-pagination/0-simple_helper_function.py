"""
This module defines a function named index_range that takes two
integer arguments page and page_size
"""


def index_range(page, page_size):
    """Return a tuple of size two containing a start index and an end index"""
    if page <= 0:
        return (0, 0)
    else:
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return (start_index, end_index)
