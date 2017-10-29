class labirynt():

    def __init__(self):
        self.done = False
        self.data= self.map_provider()[1]

    def map_provider(self):
        """create map from labirynt files"""

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
        """search for end and start point """

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

        return (where_start_is,where_end_is)

    def chceck_point_its_not_dead_end(self,data,pkt):
        """check that point don't have more way than 1 return True or False"""

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




    def find_way(self):
        """Looking for end way and slap them and find way from start to end"""
        data = self.data
        check_map_change = True
        stara = data[:]

        while check_map_change == True:
            for i in range(0, len(data[0])):
                for j in range(0, len(data)):
                    if self.chceck_point_its_not_dead_end(data, (j, i)) == True \
                            and data[j][i] != "#" and data[j][i] != "$" and data[j][i] != "@":
                        data[j]=data[j][0:i]+"A"+data[j][i+1:]

            if stara == data:
                check_map_change = False
            else:
                stara = data[:]


        start_end = self.start_and_end_provider()

        way = self.way_provider(start_end[1], data)

        return way

    def way_provider(self, position, data, way=[]):
        """provide way from end to start and draw them on map"""

        if data[position[0]][position[1]] == '$':
            self.done = True
            self.data = data
            return way

        if data[position[0]][position[1]] != '@':
           data[position[0]] = data[position[0]][0:position[1]] + '*' +data[position[0]][position[1]+1:]

        if (((data[position[0] + 1][position[1]] == ' ') or (data[position[0] + 1][position[1]] == '$'))
            and self.done == False):
            way.append([position[0] + 1, position[1]])
            self.way_provider([position[0] + 1, position[1]], data)

        if (((data[position[0]][position[1] + 1] == ' ') or (data[position[0]][position[1] + 1] == '$'))
            and self.done == False):
            way.append([position[0], position[1] + 1])
            self.way_provider([position[0], position[1] + 1], data)

        if (((data[position[0] - 1][position[1]] == ' ') or (data[position[0] - 1][position[1]] == '$'))
            and self.done == False):
            way.append([position[0] - 1, position[1]])
            self.way_provider([position[0] - 1, position[1]], data)

        if (((data[position[0]][position[1] - 1] == ' ') or (data[position[0]][position[1] - 1] == '$'))
            and self.done == False):
            way.append([position[0], position[1] - 1])
            self.way_provider([position[0], position[1] - 1], data)
        return way


    def __str__(self):
        data =self.data
        for i in data[0:-1]:
            print i
        return data[-1]


new = labirynt()

print new.find_way()

print new
