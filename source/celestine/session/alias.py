""""""

from argparse import ArgumentParser as AP
from argparse import _ArgumentGroup as AG
from typing import TypeAlias as TA
from typing import Dict as D
from typing import Type as T
from typing import Union as U

from celestine.session.argument import Argument as A


Magic: TA = D[U[A, T[A]], U[AP, AG]]
