from enum import Enum

class RegularizationType(Enum):
    NONE = "none"
    L1 = "l1"
    L2 = "l2"
    TV = "tv"
    TGV = "tgv"
