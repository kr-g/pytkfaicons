from pytkfaicons import REFTAG
from pytkfaicons.conv import build

reftag=REFTAG
reftag = "6.12"

build(reftag=reftag, callb=print)  # this uses global .pygg_credits file
