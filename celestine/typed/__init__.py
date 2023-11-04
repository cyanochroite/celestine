""""""

import importlib
import sys
from typing import TypeAlias as TA

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
I = _module.I
J = _module.J
K = _module.K
L = _module.L
M = _module.M
N: TA = None
O = _module.O
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
GI = _module.GI
GP = _module.GP
GS = _module.GS

OB = _module.OB
OF = _module.OF
OI = _module.OI
OP = _module.OP
OS = _module.OS

LB = _module.LB
LF = _module.LF
LI = _module.LI
LP = _module.LP
LS = _module.LS


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

override = _module.override
Ring = _module.Ring
R = _module.R
