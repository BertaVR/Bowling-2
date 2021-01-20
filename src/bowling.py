class Puntuacion_total_bolos:
    NULO = '-'
    SPARE = '/'
    STRIKE = 'X'
    MAX_BOLOS = 10
    MAX_TURNOS = 10
    
    def __init__(self, tabla_tiradas):
        self.tabla_tiradas = list(tabla_tiradas)
        self.puntuacion = 0
        self.total_tiradas= 0
        self.tiradas_por_turno = 0
        self.turnos = 1
        self.ultimo_numero = 0

    def equivalencias_puntuacion_simbolo(self, lista_tiradas):
        puntuacion = 0
        for tirada in lista_tiradas:
            if tirada == Puntuacion_total_bolos.NULO:
                puntuacion += 0
                self.ultimo_numero = 0
            if tirada.isdigit():
                puntuacion += int(tirada)
                self.ultimo_numero = tirada
            if tirada == Puntuacion_total_bolos.SPARE:
                puntuacion += Puntuacion_total_bolos.MAX_BOLOS - int(self.ultimo_numero) #int porque detrás de un spare solo puede ir un número (el numero de bolos que has tirado)
            if tirada == Puntuacion_total_bolos.STRIKE:
                puntuacion += Puntuacion_total_bolos.MAX_BOLOS
        return puntuacion



    def puntuacion_partida(self):
        for tirada in self.tabla_tiradas:
            if self.turnos < Puntuacion_total_bolos.MAX_TURNOS:
                if tirada.isdigit():
                    Puntuacion_total_bolos.puntuacion_open(self, tirada)
                if tirada == Puntuacion_total_bolos.NULO:
                    Puntuacion_total_bolos.puntuacion_nulo(self, tirada)
                if tirada == Puntuacion_total_bolos.SPARE:
                    self.puntuacion += Puntuacion_total_bolos.puntuacion_spare(self)
                if tirada == Puntuacion_total_bolos.STRIKE:
                    self.puntuacion += Puntuacion_total_bolos.puntuacion_strike(self)
            elif self.turnos == Puntuacion_total_bolos.MAX_TURNOS:
                    self.puntuacion += Puntuacion_total_bolos.puntuacion_tenth(self)
                    return self.puntuacion
            self.total_tiradas += 1


    
    def puntuacion_open(self, tirada):
        self.tiradas_por_turno += 1
        self.puntuacion += int(tirada)
        if self.tiradas_por_turno == 2:
            self.turnos += 1
            self.tiradas_por_turno = 0
        self.ultimo_numero = tirada

    def puntuacion_nulo(self, tirada):
        self.puntuacion += 0
        self.tiradas_por_turno += 1
        if self.tiradas_por_turno == 2:
            self.turnos += 1
            self.tiradas_por_turno = 0
        self.ultimo_numero = 0            

    
    def puntuacion_spare(self):
        lista_tiradas = self.tabla_tiradas[self.total_tiradas : self.total_tiradas + 2]
        self.turnos += 1
        self.tiradas_por_turno = 0  
        return Puntuacion_total_bolos.equivalencias_puntuacion_simbolo(self, lista_tiradas)


    def puntuacion_strike(self):
        lista_tiradas = self.tabla_tiradas[self.total_tiradas : self.total_tiradas + 3]
        self.turnos += 1
        return Puntuacion_total_bolos.equivalencias_puntuacion_simbolo(self, lista_tiradas)

    def puntuacion_tenth(self):
        lista_tiradas = self.tabla_tiradas[self.total_tiradas :]
        return Puntuacion_total_bolos.equivalencias_puntuacion_simbolo(self, lista_tiradas)
if __name__ == '__main__':
    assert Puntuacion_total_bolos("8/549-XX5/53639/9/X").puntuacion_partida() == 149