""""""

import importlib
import sys
import typing

_version = sys.version.split(".")
_major = _version[0]
_minor = _version[1]
_name = f"celestine.typed.python_{_major}_{_minor}"
_module = importlib.import_module(_name)

A = _module.A
B = _module.B
C = _module.C
D = _module.D
E = _module.E
F = _module.F
G = _module.G
H = _module.H
# I = _module.I  # Ambiguous variable name.
J = _module.J
K = _module.K
L = _module.L
M = _module.M
N: typing.TypeAlias = None
# O = _module.O  # Ambiguous variable name.
P = _module.P
Q = _module.Q
R = _module.R
S = _module.S
T = _module.T
U = _module.U
V = _module.V
W = _module.W
X = _module.X
Y = _module.Y
Z = _module.Z

GB = _module.GB
GF = _module.GF
GZ = _module.GZ
GP = _module.GP
GS = _module.GS

OB = _module.OB
OF = _module.OF
OZ = _module.OZ
OM = _module.OM
OP = _module.OP
OS = _module.OS

LB = _module.LB
LF = _module.LF
LZ = _module.LZ
LP = _module.LP
LS = _module.LS


PATH = _module.PATH

FN = _module.FN
AXIS = _module.AXIS
FILE = _module.FILE
AT = _module.AT
TYPE = _module.TYPE
IMAGE = _module.IMAGE
APD = _module.APD
LZMA = _module.LZMA
TABLE = _module.TABLE
BOX = _module.BOX
PAIR = _module.PAIR
AD = _module.AD
AI = _module.AI

SS = _module.SS
MS = _module.MS

ignore = _module.ignore
override = _module.override
string = _module.string
