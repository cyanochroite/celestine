"""Parse arguments."""
import argparse

def parser():
    parser = argparse.ArgumentParser(
        prog="celestine"
    )

    parser.add_argument(
        "-p, --package",
        choices=[
            "celestine",
            "curses",
            "dearpygui",
            "tkinter",
            "unittest"
        ],
        help="Choose a mode to opperate in.",
        dest="package"
    )

    parser.add_argument(
        "-l, --language",
        choices=[
            "english",
            "french",
            "german"
        ],
        help="Choose a language.",
        dest="language"
    )

    parser.add_argument(
        "-v, --version",
        choices=[
            "python_3_6",
            "python_3_7",
            "python_3_8",
            "python_3_9",
            "python_3_10",
            "python_3_11"
        ],
        help="Tell me which python version you are using.",
        dest="python"
    )

    return parser.parse_args()
