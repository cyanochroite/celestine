""""""


from celestine import bank
from celestine.session import begin_session
from celestine.typed import (
    LS,
    B,
    N,
    R,
)


def main(argument_list: LS, exit_on_error: B, **star: R) -> N:
    """Run the main program."""
    begin_session(argument_list, exit_on_error, **star)

    with bank.window:
        for name, function in bank.code.items():
            bank.window.code[name] = function

        for name, function in bank.view.items():
            view = bank.window.drop(name)
            function(view)
            bank.window.view[name] = view
