#!/usr/bin/env python3

"""
A simple_helper_function
"""
from typing import Tuple


def index_range(page, page_size):
  """Returns a tuple of size two containing a start index and an end index
     corresponding to the range of indexes to return in a list for those 
     particular pagination parameters.

  Args:
    page: The page number, 1-indexed.
    page_size: The size of each page.

  Returns:
    A tuple of size two containing the start index and the end index.
  """

  end_index = page * page_size
  start_index = end_index - page_size
  return (start_index, end_index)
