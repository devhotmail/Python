from thinkbayes import Pmf
import Pmf
# pmf = Pmf()
#
#
#
# pmf.Set('Bowl 1', 0.5)
# pmf.Set('Bowl 2', 0.5)
# pmf.Incr(2, 0.2)
#
# pmf.Mult('Bowl 1', 0.75)
# pmf.Mult('Bowl 2', 0.5)
#
# pmf.Normalize()
# print (pmf.Prob('Bowl 1'))

hist = Pmf.MakeHistFromList([1, 2, 2, 3, 5])
print(hist.Freq(2))
print("end")

for val in sorted(hist.Values()):
    print (val, hist.Freq(val))