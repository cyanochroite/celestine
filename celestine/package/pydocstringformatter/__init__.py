"""A tool to automatically format Python docstrings.

It tries to follow. recommendations from PEP 8 and PEP 257.
"""

import pydocstringformatter

from celestine.package import run


def main():
    """"""

    def function():
        pydocstringformatter.run_docstring_formatter()

    argument = [
        "-w",
        "--max-summary-lines 1",
        "--max-line-length 72",
        "--style pep257",
        "--strip-whitespaces",
        "--split-summary-body",
        "--no-numpydoc-section-order",
        "--no-numpydoc-name-type-spacing",
        "--no-numpydoc-section-spacing",
        "--no-numpydoc-section-hyphen-length",
        "--beginning-quotes",
        "--closing-quotes",
        "--capitalize-first-letter",
        "--final-period",
        "--quotes-type",
        "--linewrap-full-docstring",
    ]

    run(function, argument)
