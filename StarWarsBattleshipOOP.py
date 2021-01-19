from random import randint as r
class Gemi:
    can = None
    kalkan = None
    hasar = None
    ismi = ""

    def __init__(self,_can,_kalkan,_hasar,_ismi):
        self.can = _can
        self.kalkan = _kalkan
        self.hasar = _hasar
        self.ismi = _ismi

    def __str__(self):
        return "Geminin Adı=>{}\nGeminin Sağlık Puanı=>{}\nGemi Kalkan Puanı=>{}\nGemi Maksimum Hasar Puanı=>{}".format(self.ismi,self.can,self.kalkan,self.hasar)

gemi1 = Gemi(500,1000,100,"Republic Frigate")
gemi2 = Gemi(500,1000,100,"Millenium Falcon")


while gemi1.can>0 and gemi2.can>0:
        hasar1 = r(1, 100)
        hasar2 = r(1, 100)
        print("{} Gemisinin Vurduğu Hasar=> {}, Kalkan Değeri=> {}, Can Değeri=> {}. {} Gemisinin Vurduğu Hasar=> {}, Kalkan Değeri=> {}, Can Değeri=> {}".format(gemi1.ismi,hasar1,gemi1.kalkan,gemi1.can,gemi2.ismi,hasar2,gemi2.kalkan,gemi2.can))
        gemi2.kalkan-=hasar1
        gemi1.kalkan-=hasar2
        


        if gemi1.kalkan<0:
            gemi1.can-=hasar2
            
            gemi1.kalkan = 0
        if gemi2.kalkan<0:
            gemi2.can-=hasar1
            gemi2.kalkan=0
            


if gemi1.can or gemi2.can <0:
    if gemi1.can<0:
        gemi1.can=0
        print("{}'in Sağlık Değeri; {}, {}'un Sağlık Değeri; {}".format(gemi1.ismi,gemi1.can,gemi2.ismi,gemi2.can))

        print("Oyunu {} gemisi kazandı!".format(gemi2.ismi))
    elif gemi2.can<0:
        gemi2.can = 0
        print("{}'un Sağlık Değeri; {}, {}'in Sağlık Değeri; {}".format(gemi2.ismi,gemi2.can,gemi1.ismi,gemi1.can))
        print("Oyunu {} gemisi kazandı!".format(gemi1.ismi))
