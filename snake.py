import random

class Snake:
    def win(self):
        return self.score == self.maxScore
    
    def genApp(self):
        while True:
            i = random.randint(0, self.NROW-1)
            j = random.randint(0, self.NCOLUMN-1)
            if self.map[i][j] == '.':
                self.map[i][j] = 'M'
                break
        
    def init_map(self,Nrow:int,Ncolum:int)->list[list]:
        ret = []
        
        if Nrow <= 0 or Ncolum <= 0:
            return None

        for i in range(0,Nrow+1):
            ret.append([])
            for j in range(0,Ncolum+1):
                ret[i].append(".")

        return ret

    def __init__(self,sizex:int=0,sizey:int=0,maxScore:int=10)->None:
        #punteggi
        self.score = 0
        self.maxScore = maxScore
        #costanti per la dimensione standard della mappa
        DEFAULTX = 40
        DEFAULTY = 40

        #Posizione attuale nelle cordinate x
        self.head_x = 1
        #posizione attuale nelle cordinate y
        self.head_y = 0

        #inizializzazione della mappa
        if sizex <= 0 or sizey <= 0:
            self.NROW = DEFAULTX
            self.NCOLUMN = DEFAULTY
            self.map = self.init_map(DEFAULTX,DEFAULTY)
        else:
            self.NROW = int(sizex/10)#dividere per la dimensione del diametro del cerchio
            self.NCOLUMN = int(sizey/10)
            self.map = self.init_map(sizex,sizey)
        
        self.genApp()
        self.map[self.head_y][self.head_x] = "D"
        self.body = [(self.head_y,self.head_x-1)]

        #inizializzazione dei commandi
        self.up =    "w"
        self.down =  "s"
        self.left =  "a"
        self.right = "d"
        self.dir =   "s"

    def draw(self, drawFunc):
        for i in range(self.NROW):
            for j in range(self.NCOLUMN):
                drawFunc(i,j,self.map[i][j])

    def direction(self, dir):
        if dir not in (self.up, self.down, self.left, self.right): return False
        # lista delle direzioni opposte
        opposite = [(self.up, self.down), (self.left, self.right),
                    (self.down, self.up), (self.right, self.left)]
        if (dir, self.dir) in opposite:
            return False
        self.dir = dir
        return True
        
    def move(self):
        
        self.body.insert(0, (self.head_y, self.head_x))
        
        if self.dir == self.left:
            self.head_x = self.head_x-1
            if self.head_x == -1:
                return False
        elif self.dir == self.up:
            self.head_y = self.head_y-1
            if self.head_y == -1:
                return False
        elif self.dir == self.right:
            self.head_x = self.head_x+1
            if self.head_x == self.NCOLUMN:
                return False
        elif self.dir == self.down:
            self.head_y = self.head_y + 1
            if self.head_y == self.NROW:
                return False


        eat = self.map[self.head_y][self.head_x] == "M"
        if eat:
            self.score += 1
            self.genApp()
        else:
            y,x = self.body.pop()
            self.map[y][x] = "."
        death = self.map[self.head_y][self.head_x] == "T"
        if death:
            return False
        
        self.map[self.head_y][self.head_x] = "D"
        for y,x in self.body:
            self.map[y][x] = "T"
        return True
            
    
    

    
