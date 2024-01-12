

class muzik():
    def __init__(self):
        self.playlist=[]
        self.suankindex=0
        self.caliniyor=False
    def sarkiekle(self,sarki):
        self.playlist.append(sarki)
    def cal(self):
        if self.playlist:
            self.caliniyor=True
            print(f"{self.suanki()} caliyor")
        else:
            print("calma listesi bos")
    def duraklat(self):
        if self.caliniyor:
            print(f"{self.suanki()} çalıyor")
        else:
            print("muzık calmıyor")
    def sonraki(self):
        if self.playlist:
            if self.caliniyor:
                print(f"{self.suanki()} tamam sıradaki")
                self.suankindex+=1
                if self.suankindex<len(self.playlist):
                    self.cal()
                else:
                    self.caliniyor=False
                    print("clam listesi sona erdi")
            else:
                print(f"{self.suanki()} calmıyor")
        else:
            print("calma listesi bos")
    def suanki(self):
        if self.playlist and 0<=self.suankindex<len((self.playlist)):
            return  self.playlist[self.suankindex]
        else:
            return none

muzik=muzik()
muzik.sarkiekle("sarki1")
muzik.sarkiekle("sarki2")
muzik.sarkiekle("sarki3")

muzik.cal()
muzik.duraklat()
muzik.sonraki()













