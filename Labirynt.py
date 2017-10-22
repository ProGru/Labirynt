class labirynt():
    def __init__(self):
        return

    def map_provider(self):
        text = open('labirynt').readline()
        wys_szer = []

        for i in range(0, len(text)):
            if text[i] == " ":
                wys_szer.append(int(text[0:i]))
                wys_szer.append(int(text[i:-1]))

        wszystko_z_pliku = open('labirynt').readlines()
        plansza = []

        for i in wszystko_z_pliku:
            plansza.append(i[0:-1])

        plansza = plansza[1:]
        plansza[-1] = plansza[-1] + "#"

        return wys_szer, plansza

    def start_and_end_provider(self):
        data = self.map_provider()[1]
        size = self.map_provider()[0]

        where_start_is =(0,0)
        where_end_is = (0,0)

        for i in range(0, len(data)):
            for j in range(0, size[1]):
                if data[i][j]=="$":
                    where_start_is = (i,j)
                elif data[i][j]=="@":
                    where_end_is = (i,j)

        way=[]
        new = self.find_way(where_start_is,where_end_is,way,data)
        return new

    def chceck_point_its_not_dead_end(self,data,pkt):
        if data[pkt[0]][pkt[1]]=="#":
            return True
        how_much = 0
        if data[pkt[0]-1][pkt[1]]==" " or data[pkt[0]-1][pkt[1]]=="@" or data[pkt[0]-1][pkt[1]]=="$":
            how_much += 1
        if data[pkt[0]+1][pkt[1]]==" " or data[pkt[0]+1][pkt[1]]=="@" or data[pkt[0]+1][pkt[1]]=="$":
            how_much += 1
        if data[pkt[0]][pkt[1]+1]==" " or data[pkt[0]][pkt[1]+1]=="@" or data[pkt[0]][pkt[1]+1]=="$":
            how_much += 1
        if data[pkt[0]][pkt[1]-1]==" " or data[pkt[0]][pkt[1]-1]=="@" or data[pkt[0]][pkt[1]-1]=="$":
            how_much += 1
        if how_much >=2:
            return False
        else:
            return True


    def find_way(self,start,end,way,data):
        x = True
        stara = data[:]
        while x==True:
            for i in range(0,len(data[0])):
                for j in range(0,len(data)):
                    if self.chceck_point_its_not_dead_end(data,(j,i))==True and data[j][i] != "#" and data[j][i] != "$" and data[j][i] != "@":
                        data[j]=data[j][0:i]+"A"+data[j][i+1:]
            if stara == data:
                x = False
            else:
                stara = data[:]

        for i in data[0:-1]:
            print i
        return data[-1]

    def __str__(self):
        data = self.map_provider()[1]
        for i in data[0:-1]:
            print i
        return data[-1]


new = labirynt()
print new.start_and_end_provider()
print new

zmienna = "12345678"
print zmienna[0:3]+"A"+zmienna[3+1:]