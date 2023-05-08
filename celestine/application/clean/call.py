"""Run a bunch of auto formaters."""


from celestine.package import run


def clean(**star):
    """"""

    run("isort")
    run("black")
    return

    black()

    pyupgrade()

    pydocstringformatter()

    autoflake()

    isort()

    black()

    print("I am a talking cow.")
