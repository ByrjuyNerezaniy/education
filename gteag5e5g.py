class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        slovar = {}
        slovar1 = {}
        setd = set(d)
        for i in setd:
            c = d.count(i)
            slovar[i]=c
        print(slovar)

        sets = set(s)
        for i in sets:
            f = s.count(i)
            slovar1[i]=f
        print(slovar1)

        return slovar == slovar1
