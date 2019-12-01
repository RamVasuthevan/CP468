from simple_genetic_algorithm import SGA

ALNUM = ["0", "1"]
MAX_A_INDEX = 41
MAX_B_INDEX = 41
VAR_STRING_LEN = (MAX_A_INDEX+MAX_B_INDEX+2)*8
NUMBER_OF_VARIABLES = MAX_A_INDEX+MAX_B_INDEX+2
VARIABLE_LEN = int(VAR_STRING_LEN / NUMBER_OF_VARIABLES)
PROBABILITY_OF_MUTATION = 0.05
POP_SIZE = 40
NUM_GENERATIONS = 100
DOMAIN_MIN = -15
DOMAIN_MAX = 15

#TODO docstring
def decoder(*M):
    M = list(M)
    return func(**{chr(ind//42+ord("a"))+str(ind%42):val for ind, val in enumerate(M)})

def func(args):
    of = abs(a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12+a13+a14+a15+a16+a17+a18+a19+a20+a21+a22+a23+a24+a25+a26+a27+a28+a29+a30+a31+a32+a33+a34+a35+a36+a37+a38+a39+a40+a41-1)

    of = of + abs(b1+b2+b3+b4+b5+b6+b7+b8+b9+b10+b11+b12+b13+b14+b15+b16+b17+b18+b19+b20+b21+b22+b23+b24+b25+b26+b27+b28+b29+b30+b31+b32+b33+b34+b35+b36+b37+b38+b39+b40+b41-1)

    of = of + abs(a1*a21+a1*a22+a2*a22+a2*a23+a3*a23+a3*a24+a4*a24+a4*a25+a5*a25+a5*a26+a6*a26+a6*a27+a7*a27+a7*a28+a8*a28+a8*a29+a9*a29+a9*a30+a10*a30+a10*a31+a11*a31+a11*a32+a12*a32+a12*a33+a13*a33+a13*a34+a14*a34+a14*a35+a15*a35+a15*a36+a16*a36+a16*a37+a17*a37+a17*a38+a18*a38+a18*a39+a19*a39+a19*a40+a20*a40+a20*a41+a21*a41+b1*b21+b1*b22+b2*b22+b2*b23+b3*b23+b3*b24+b4*b24+b4*b25+b5*b25+b5*b26+b6*b26+b6*b27+b7*b27+b7*b28+b8*b28+b8*b29+b9*b29+b9*b30+b10*b30+b10*b31+b11*b31+b11*b32+b12*b32+b12*b33+b13*b33+b13*b34+b14*b34+b14*b35+b15*b35+b15*b36+b16*b36+b16*b37+b17*b37+b17*b38+b18*b38+b18*b39+b19*b39+b19*b40+b20*b40+b20*b41+b21*b41+2)

    of = of + abs(a1*a20+a1*a23+a2*a21+a2*a24+a3*a22+a3*a25+a4*a23+a4*a26+a5*a24+a5*a27+a6*a25+a6*a28+a7*a26+a7*a29+a8*a27+a8*a30+a9*a28+a9*a31+a10*a29+a10*a32+a11*a30+a11*a33+a12*a31+a12*a34+a13*a32+a13*a35+a14*a33+a14*a36+a15*a34+a15*a37+a16*a35+a16*a38+a17*a36+a17*a39+a18*a37+a18*a40+a19*a38+a19*a41+a20*a39+a21*a40+a22*a41+b1*b20+b1*b23+b2*b21+b2*b24+b3*b22+b3*b25+b4*b23+b4*b26+b5*b24+b5*b27+b6*b25+b6*b28+b7*b26+b7*b29+b8*b27+b8*b30+b9*b28+b9*b31+b10*b29+b10*b32+b11*b30+b11*b33+b12*b31+b12*b34+b13*b32+b13*b35+b14*b33+b14*b36+b15*b34+b15*b37+b16*b35+b16*b38+b17*b36+b17*b39+b18*b37+b18*b40+b19*b38+b19*b41+b20*b39+b21*b40+b22*b41+2)

    of = of + abs(a1*a19+a1*a24+a2*a20+a2*a25+a3*a21+a3*a26+a4*a22+a4*a27+a5*a23+a5*a28+a6*a24+a6*a29+a7*a25+a7*a30+a8*a26+a8*a31+a9*a27+a9*a32+a10*a28+a10*a33+a11*a29+a11*a34+a12*a30+a12*a35+a13*a31+a13*a36+a14*a32+a14*a37+a15*a33+a15*a38+a16*a34+a16*a39+a17*a35+a17*a40+a18*a36+a18*a41+a19*a37+a20*a38+a21*a39+a22*a40+a23*a41+b1*b19+b1*b24+b2*b20+b2*b25+b3*b21+b3*b26+b4*b22+b4*b27+b5*b23+b5*b28+b6*b24+b6*b29+b7*b25+b7*b30+b8*b26+b8*b31+b9*b27+b9*b32+b10*b28+b10*b33+b11*b29+b11*b34+b12*b30+b12*b35+b13*b31+b13*b36+b14*b32+b14*b37+b15*b33+b15*b38+b16*b34+b16*b39+b17*b35+b17*b40+b18*b36+b18*b41+b19*b37+b20*b38+b21*b39+b22*b40+b23*b41+2)

    of = of + abs(a1*a17+a1*a26+a2*a18+a2*a27+a3*a19+a3*a28+a4*a20+a4*a29+a5*a21+a5*a30+a6*a22+a6*a31+a7*a23+a7*a32+a8*a24+a8*a33+a9*a25+a9*a34+a10*a26+a10*a35+a11*a27+a11*a36+a12*a28+a12*a37+a13*a29+a13*a38+a14*a30+a14*a39+a15*a31+a15*a40+a16*a32+a16*a41+a17*a33+a18*a34+a19*a35+a20*a36+a21*a37+a22*a38+a23*a39+a24*a40+a25*a41+b1*b17+b1*b26+b2*b18+b2*b27+b3*b19+b3*b28+b4*b20+b4*b29+b5*b21+b5*b30+b6*b22+b6*b31+b7*b23+b7*b32+b8*b24+b8*b33+b9*b25+b9*b34+b10*b26+b10*b35+b11*b27+b11*b36+b12*b28+b12*b37+b13*b29+b13*b38+b14*b30+b14*b39+b15*b31+b15*b40+b16*b32+b16*b41+b17*b33+b18*b34+b19*b35+b20*b36+b21*b37+b22*b38+b23*b39+b24*b40+b25*b41+2)

    of = of + abs(a1*a18+a1*a25+a2*a19+a2*a26+a3*a20+a3*a27+a4*a21+a4*a28+a5*a22+a5*a29+a6*a23+a6*a30+a7*a24+a7*a31+a8*a25+a8*a32+a9*a26+a9*a33+a10*a27+a10*a34+a11*a28+a11*a35+a12*a29+a12*a36+a13*a30+a13*a37+a14*a31+a14*a38+a15*a32+a15*a39+a16*a33+a16*a40+a17*a34+a17*a41+a18*a35+a19*a36+a20*a37+a21*a38+a22*a39+a23*a40+a24*a41+b1*b18+b1*b25+b2*b19+b2*b26+b3*b20+b3*b27+b4*b21+b4*b28+b5*b22+b5*b29+b6*b23+b6*b30+b7*b24+b7*b31+b8*b25+b8*b32+b9*b26+b9*b33+b10*b27+b10*b34+b11*b28+b11*b35+b12*b29+b12*b36+b13*b30+b13*b37+b14*b31+b14*b38+b15*b32+b15*b39+b16*b33+b16*b40+b17*b34+b17*b41+b18*b35+b19*b36+b20*b37+b21*b38+b22*b39+b23*b40+b24*b41+2)

    of = of + abs(a1*a16+a1*a27+a2*a17+a2*a28+a3*a18+a3*a29+a4*a19+a4*a30+a5*a20+a5*a31+a6*a21+a6*a32+a7*a22+a7*a33+a8*a23+a8*a34+a9*a24+a9*a35+a10*a25+a10*a36+a11*a26+a11*a37+a12*a27+a12*a38+a13*a28+a13*a39+a14*a29+a14*a40+a15*a30+a15*a41+a16*a31+a17*a32+a18*a33+a19*a34+a20*a35+a21*a36+a22*a37+a23*a38+a24*a39+a25*a40+a26*a41+b1*b16+b1*b27+b2*b17+b2*b28+b3*b18+b3*b29+b4*b19+b4*b30+b5*b20+b5*b31+b6*b21+b6*b32+b7*b22+b7*b33+b8*b23+b8*b34+b9*b24+b9*b35+b10*b25+b10*b36+b11*b26+b11*b37+b12*b27+b12*b38+b13*b28+b13*b39+b14*b29+b14*b40+b15*b30+b15*b41+b16*b31+b17*b32+b18*b33+b19*b34+b20*b35+b21*b36+b22*b37+b23*b38+b24*b39+b25*b40+b26*b41+2)

    of = of + abs(a1*a14+a1*a29+a2*a15+a2*a30+a3*a16+a3*a31+a4*a17+a4*a32+a5*a18+a5*a33+a6*a19+a6*a34+a7*a20+a7*a35+a8*a21+a8*a36+a9*a22+a9*a37+a10*a23+a10*a38+a11*a24+a11*a39+a12*a25+a12*a40+a13*a26+a13*a41+a14*a27+a15*a28+a16*a29+a17*a30+a18*a31+a19*a32+a20*a33+a21*a34+a22*a35+a23*a36+a24*a37+a25*a38+a26*a39+a27*a40+a28*a41+b1*b14+b1*b29+b2*b15+b2*b30+b3*b16+b3*b31+b4*b17+b4*b32+b5*b18+b5*b33+b6*b19+b6*b34+b7*b20+b7*b35+b8*b21+b8*b36+b9*b22+b9*b37+b10*b23+b10*b38+b11*b24+b11*b39+b12*b25+b12*b40+b13*b26+b13*b41+b14*b27+b15*b28+b16*b29+b17*b30+b18*b31+b19*b32+b20*b33+b21*b34+b22*b35+b23*b36+b24*b37+b25*b38+b26*b39+b27*b40+b28*b41+2)

    of = of + abs(a1*a15+a1*a28+a2*a16+a2*a29+a3*a17+a3*a30+a4*a18+a4*a31+a5*a19+a5*a32+a6*a20+a6*a33+a7*a21+a7*a34+a8*a22+a8*a35+a9*a23+a9*a36+a10*a24+a10*a37+a11*a25+a11*a38+a12*a26+a12*a39+a13*a27+a13*a40+a14*a28+a14*a41+a15*a29+a16*a30+a17*a31+a18*a32+a19*a33+a20*a34+a21*a35+a22*a36+a23*a37+a24*a38+a25*a39+a26*a40+a27*a41+b1*b15+b1*b28+b2*b16+b2*b29+b3*b17+b3*b30+b4*b18+b4*b31+b5*b19+b5*b32+b6*b20+b6*b33+b7*b21+b7*b34+b8*b22+b8*b35+b9*b23+b9*b36+b10*b24+b10*b37+b11*b25+b11*b38+b12*b26+b12*b39+b13*b27+b13*b40+b14*b28+b14*b41+b15*b29+b16*b30+b17*b31+b18*b32+b19*b33+b20*b34+b21*b35+b22*b36+b23*b37+b24*b38+b25*b39+b26*b40+b27*b41+2)

    of = of + abs(a1*a13+a1*a30+a2*a14+a2*a31+a3*a15+a3*a32+a4*a16+a4*a33+a5*a17+a5*a34+a6*a18+a6*a35+a7*a19+a7*a36+a8*a20+a8*a37+a9*a21+a9*a38+a10*a22+a10*a39+a11*a23+a11*a40+a12*a24+a12*a41+a13*a25+a14*a26+a15*a27+a16*a28+a17*a29+a18*a30+a19*a31+a20*a32+a21*a33+a22*a34+a23*a35+a24*a36+a25*a37+a26*a38+a27*a39+a28*a40+a29*a41+b1*b13+b1*b30+b2*b14+b2*b31+b3*b15+b3*b32+b4*b16+b4*b33+b5*b17+b5*b34+b6*b18+b6*b35+b7*b19+b7*b36+b8*b20+b8*b37+b9*b21+b9*b38+b10*b22+b10*b39+b11*b23+b11*b40+b12*b24+b12*b41+b13*b25+b14*b26+b15*b27+b16*b28+b17*b29+b18*b30+b19*b31+b20*b32+b21*b33+b22*b34+b23*b35+b24*b36+b25*b37+b26*b38+b27*b39+b28*b40+b29*b41+2)

    of = of + abs(a1*a11+a1*a32+a2*a12+a2*a33+a3*a13+a3*a34+a4*a14+a4*a35+a5*a15+a5*a36+a6*a16+a6*a37+a7*a17+a7*a38+a8*a18+a8*a39+a9*a19+a9*a40+a10*a20+a10*a41+a11*a21+a12*a22+a13*a23+a14*a24+a15*a25+a16*a26+a17*a27+a18*a28+a19*a29+a20*a30+a21*a31+a22*a32+a23*a33+a24*a34+a25*a35+a26*a36+a27*a37+a28*a38+a29*a39+a30*a40+a31*a41+b1*b11+b1*b32+b2*b12+b2*b33+b3*b13+b3*b34+b4*b14+b4*b35+b5*b15+b5*b36+b6*b16+b6*b37+b7*b17+b7*b38+b8*b18+b8*b39+b9*b19+b9*b40+b10*b20+b10*b41+b11*b21+b12*b22+b13*b23+b14*b24+b15*b25+b16*b26+b17*b27+b18*b28+b19*b29+b20*b30+b21*b31+b22*b32+b23*b33+b24*b34+b25*b35+b26*b36+b27*b37+b28*b38+b29*b39+b30*b40+b31*b41+2)

    of = of + abs(a1*a12+a1*a31+a2*a13+a2*a32+a3*a14+a3*a33+a4*a15+a4*a34+a5*a16+a5*a35+a6*a17+a6*a36+a7*a18+a7*a37+a8*a19+a8*a38+a9*a20+a9*a39+a10*a21+a10*a40+a11*a22+a11*a41+a12*a23+a13*a24+a14*a25+a15*a26+a16*a27+a17*a28+a18*a29+a19*a30+a20*a31+a21*a32+a22*a33+a23*a34+a24*a35+a25*a36+a26*a37+a27*a38+a28*a39+a29*a40+a30*a41+b1*b12+b1*b31+b2*b13+b2*b32+b3*b14+b3*b33+b4*b15+b4*b34+b5*b16+b5*b35+b6*b17+b6*b36+b7*b18+b7*b37+b8*b19+b8*b38+b9*b20+b9*b39+b10*b21+b10*b40+b11*b22+b11*b41+b12*b23+b13*b24+b14*b25+b15*b26+b16*b27+b17*b28+b18*b29+b19*b30+b20*b31+b21*b32+b22*b33+b23*b34+b24*b35+b25*b36+b26*b37+b27*b38+b28*b39+b29*b40+b30*b41+2)

    of = of + abs(a1*a10+a1*a33+a2*a11+a2*a34+a3*a12+a3*a35+a4*a13+a4*a36+a5*a14+a5*a37+a6*a15+a6*a38+a7*a16+a7*a39+a8*a17+a8*a40+a9*a18+a9*a41+a10*a19+a11*a20+a12*a21+a13*a22+a14*a23+a15*a24+a16*a25+a17*a26+a18*a27+a19*a28+a20*a29+a21*a30+a22*a31+a23*a32+a24*a33+a25*a34+a26*a35+a27*a36+a28*a37+a29*a38+a30*a39+a31*a40+a32*a41+b1*b10+b1*b33+b2*b11+b2*b34+b3*b12+b3*b35+b4*b13+b4*b36+b5*b14+b5*b37+b6*b15+b6*b38+b7*b16+b7*b39+b8*b17+b8*b40+b9*b18+b9*b41+b10*b19+b11*b20+b12*b21+b13*b22+b14*b23+b15*b24+b16*b25+b17*b26+b18*b27+b19*b28+b20*b29+b21*b30+b22*b31+b23*b32+b24*b33+b25*b34+b26*b35+b27*b36+b28*b37+b29*b38+b30*b39+b31*b40+b32*b41+2)

    of = of + abs(a1*a9+a1*a34+a2*a10+a2*a35+a3*a11+a3*a36+a4*a12+a4*a37+a5*a13+a5*a38+a6*a14+a6*a39+a7*a15+a7*a40+a8*a16+a8*a41+a9*a17+a10*a18+a11*a19+a12*a20+a13*a21+a14*a22+a15*a23+a16*a24+a17*a25+a18*a26+a19*a27+a20*a28+a21*a29+a22*a30+a23*a31+a24*a32+a25*a33+a26*a34+a27*a35+a28*a36+a29*a37+a30*a38+a31*a39+a32*a40+a33*a41+b1*b9+b1*b34+b2*b10+b2*b35+b3*b11+b3*b36+b4*b12+b4*b37+b5*b13+b5*b38+b6*b14+b6*b39+b7*b15+b7*b40+b8*b16+b8*b41+b9*b17+b10*b18+b11*b19+b12*b20+b13*b21+b14*b22+b15*b23+b16*b24+b17*b25+b18*b26+b19*b27+b20*b28+b21*b29+b22*b30+b23*b31+b24*b32+b25*b33+b26*b34+b27*b35+b28*b36+b29*b37+b30*b38+b31*b39+b32*b40+b33*b41+2)

    of = of + abs(a1*a8+a1*a35+a2*a9+a2*a36+a3*a10+a3*a37+a4*a11+a4*a38+a5*a12+a5*a39+a6*a13+a6*a40+a7*a14+a7*a41+a8*a15+a9*a16+a10*a17+a11*a18+a12*a19+a13*a20+a14*a21+a15*a22+a16*a23+a17*a24+a18*a25+a19*a26+a20*a27+a21*a28+a22*a29+a23*a30+a24*a31+a25*a32+a26*a33+a27*a34+a28*a35+a29*a36+a30*a37+a31*a38+a32*a39+a33*a40+a34*a41+b1*b8+b1*b35+b2*b9+b2*b36+b3*b10+b3*b37+b4*b11+b4*b38+b5*b12+b5*b39+b6*b13+b6*b40+b7*b14+b7*b41+b8*b15+b9*b16+b10*b17+b11*b18+b12*b19+b13*b20+b14*b21+b15*b22+b16*b23+b17*b24+b18*b25+b19*b26+b20*b27+b21*b28+b22*b29+b23*b30+b24*b31+b25*b32+b26*b33+b27*b34+b28*b35+b29*b36+b30*b37+b31*b38+b32*b39+b33*b40+b34*b41+2)

    of = of + abs(a1*a7+a1*a36+a2*a8+a2*a37+a3*a9+a3*a38+a4*a10+a4*a39+a5*a11+a5*a40+a6*a12+a6*a41+a7*a13+a8*a14+a9*a15+a10*a16+a11*a17+a12*a18+a13*a19+a14*a20+a15*a21+a16*a22+a17*a23+a18*a24+a19*a25+a20*a26+a21*a27+a22*a28+a23*a29+a24*a30+a25*a31+a26*a32+a27*a33+a28*a34+a29*a35+a30*a36+a31*a37+a32*a38+a33*a39+a34*a40+a35*a41+b1*b7+b1*b36+b2*b8+b2*b37+b3*b9+b3*b38+b4*b10+b4*b39+b5*b11+b5*b40+b6*b12+b6*b41+b7*b13+b8*b14+b9*b15+b10*b16+b11*b17+b12*b18+b13*b19+b14*b20+b15*b21+b16*b22+b17*b23+b18*b24+b19*b25+b20*b26+b21*b27+b22*b28+b23*b29+b24*b30+b25*b31+b26*b32+b27*b33+b28*b34+b29*b35+b30*b36+b31*b37+b32*b38+b33*b39+b34*b40+b35*b41+2)

    of = of + abs(a1*a6+a1*a37+a2*a7+a2*a38+a3*a8+a3*a39+a4*a9+a4*a40+a5*a10+a5*a41+a6*a11+a7*a12+a8*a13+a9*a14+a10*a15+a11*a16+a12*a17+a13*a18+a14*a19+a15*a20+a16*a21+a17*a22+a18*a23+a19*a24+a20*a25+a21*a26+a22*a27+a23*a28+a24*a29+a25*a30+a26*a31+a27*a32+a28*a33+a29*a34+a30*a35+a31*a36+a32*a37+a33*a38+a34*a39+a35*a40+a36*a41+b1*b6+b1*b37+b2*b7+b2*b38+b3*b8+b3*b39+b4*b9+b4*b40+b5*b10+b5*b41+b6*b11+b7*b12+b8*b13+b9*b14+b10*b15+b11*b16+b12*b17+b13*b18+b14*b19+b15*b20+b16*b21+b17*b22+b18*b23+b19*b24+b20*b25+b21*b26+b22*b27+b23*b28+b24*b29+b25*b30+b26*b31+b27*b32+b28*b33+b29*b34+b30*b35+b31*b36+b32*b37+b33*b38+b34*b39+b35*b40+b36*b41+2)

    of = of + abs(a1*a4+a1*a39+a2*a5+a2*a40+a3*a6+a3*a41+a4*a7+a5*a8+a6*a9+a7*a10+a8*a11+a9*a12+a10*a13+a11*a14+a12*a15+a13*a16+a14*a17+a15*a18+a16*a19+a17*a20+a18*a21+a19*a22+a20*a23+a21*a24+a22*a25+a23*a26+a24*a27+a25*a28+a26*a29+a27*a30+a28*a31+a29*a32+a30*a33+a31*a34+a32*a35+a33*a36+a34*a37+a35*a38+a36*a39+a37*a40+a38*a41+b1*b4+b1*b39+b2*b5+b2*b40+b3*b6+b3*b41+b4*b7+b5*b8+b6*b9+b7*b10+b8*b11+b9*b12+b10*b13+b11*b14+b12*b15+b13*b16+b14*b17+b15*b18+b16*b19+b17*b20+b18*b21+b19*b22+b20*b23+b21*b24+b22*b25+b23*b26+b24*b27+b25*b28+b26*b29+b27*b30+b28*b31+b29*b32+b30*b33+b31*b34+b32*b35+b33*b36+b34*b37+b35*b38+b36*b39+b37*b40+b38*b41+2)

    of = of + abs(a1*a5+a1*a38+a2*a6+a2*a39+a3*a7+a3*a40+a4*a8+a4*a41+a5*a9+a6*a10+a7*a11+a8*a12+a9*a13+a10*a14+a11*a15+a12*a16+a13*a17+a14*a18+a15*a19+a16*a20+a17*a21+a18*a22+a19*a23+a20*a24+a21*a25+a22*a26+a23*a27+a24*a28+a25*a29+a26*a30+a27*a31+a28*a32+a29*a33+a30*a34+a31*a35+a32*a36+a33*a37+a34*a38+a35*a39+a36*a40+a37*a41+b1*b5+b1*b38+b2*b6+b2*b39+b3*b7+b3*b40+b4*b8+b4*b41+b5*b9+b6*b10+b7*b11+b8*b12+b9*b13+b10*b14+b11*b15+b12*b16+b13*b17+b14*b18+b15*b19+b16*b20+b17*b21+b18*b22+b19*b23+b20*b24+b21*b25+b22*b26+b23*b27+b24*b28+b25*b29+b26*b30+b27*b31+b28*b32+b29*b33+b30*b34+b31*b35+b32*b36+b33*b37+b34*b38+b35*b39+b36*b40+b37*b41+2)

    of = of + abs(a1*a3+a1*a40+a2*a4+a2*a41+a3*a5+a4*a6+a5*a7+a6*a8+a7*a9+a8*a10+a9*a11+a10*a12+a11*a13+a12*a14+a13*a15+a14*a16+a15*a17+a16*a18+a17*a19+a18*a20+a19*a21+a20*a22+a21*a23+a22*a24+a23*a25+a24*a26+a25*a27+a26*a28+a27*a29+a28*a30+a29*a31+a30*a32+a31*a33+a32*a34+a33*a35+a34*a36+a35*a37+a36*a38+a37*a39+a38*a40+a39*a41+b1*b3+b1*b40+b2*b4+b2*b41+b3*b5+b4*b6+b5*b7+b6*b8+b7*b9+b8*b10+b9*b11+b10*b12+b11*b13+b12*b14+b13*b15+b14*b16+b15*b17+b16*b18+b17*b19+b18*b20+b19*b21+b20*b22+b21*b23+b22*b24+b23*b25+b24*b26+b25*b27+b26*b28+b27*b29+b28*b30+b29*b31+b30*b32+b31*b33+b32*b34+b33*b35+b34*b36+b35*b37+b36*b38+b37*b39+b38*b40+b39*b41+2)

    of = of + abs(a1*a2+a1*a41+a2*a3+a3*a4+a4*a5+a5*a6+a6*a7+a7*a8+a8*a9+a9*a10+a10*a11+a11*a12+a12*a13+a13*a14+a14*a15+a15*a16+a16*a17+a17*a18+a18*a19+a19*a20+a20*a21+a21*a22+a22*a23+a23*a24+a24*a25+a25*a26+a26*a27+a27*a28+a28*a29+a29*a30+a30*a31+a31*a32+a32*a33+a33*a34+a34*a35+a35*a36+a36*a37+a37*a38+a38*a39+a39*a40+a40*a41+b1*b2+b1*b41+b2*b3+b3*b4+b4*b5+b5*b6+b6*b7+b7*b8+b8*b9+b9*b10+b10*b11+b11*b12+b12*b13+b13*b14+b14*b15+b15*b16+b16*b17+b17*b18+b18*b19+b19*b20+b20*b21+b21*b22+b22*b23+b23*b24+b24*b25+b25*b26+b26*b27+b27*b28+b28*b29+b29*b30+b30*b31+b31*b32+b32*b33+b33*b34+b34*b35+b35*b36+b36*b37+b37*b38+b38*b39+b39*b40+b40*b41+2)
    return of

print("Running Simple Genetic Algorithm")
SGA(decoder, POP_SIZE, ALNUM, VAR_STRING_LEN, VARIABLE_LEN, DOMAIN_MIN, DOMAIN_MAX, NUM_GENERATIONS,PROBABILITY_OF_MUTATION)

#print(",".join(["a"+str(i) for i in range(MAX_A_INDEX+1)])+","+",".join(["b"+str(i) for i in range(MAX_B_INDEX+1)]))