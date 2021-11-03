import numpy as np
import random


class Tablero:
    def __init__(self) -> None:
        self._board = np.array([["-", "-", "-"],
                                ["-", "-", "-"],
                                ["-", "-", "-"]], dtype=str)  
        self._jugador = "O"

    def getTablero(self) -> np.ndarray:
        return self._board

    def getJugadorActual(self) -> str:
        return self._jugador
    
    def setJugadorActual(self, jugador: str):
        self._jugador = jugador

    def setMovimiento(self, fila: int, columna: int, valor: str) -> bool: #True si estaba libre la casilla
        self._board[fila][columna] = valor
        print("\nEl jugador " + str(valor) + " ha movido en la casilla (" + str(fila) + ", " + str(columna) + ")\n")
    
    def isCasillasLibres(self) -> bool: #True si quedan casillas con "-"
        casillaLibre = 0
        for i in range(len(self._board)):
            for j in range(len(self._board[i])):
                if self._board[i][j] == '-':
                    casillaLibre += 1
        
        return casillaLibre > 0
    
    def comprobarLinea(self, jugador):
        win = None

        n = len(self._board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self._board[i][j] != self._jugador:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self._board[j][i] != self._jugador:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self._board[i][i] != self._jugador:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self._board[i][n - 1 - i] != self._jugador:
                win = False
                break
        if win:
            return win
        return False

        for row in self._board:
            for item in row:
                if item == '-':
                    return False
        return True

    def jugarPartida(self):
        while board.isCasillasLibres() and not board.comprobarLinea(board.getJugadorActual()):
            fila = random.choice(range(0, 3))
            col = random.choice(range(0, 3))
            if(board.getJugadorActual() == "O"):
                valor = "X"
                board.setJugadorActual("X")
            else:
                valor = "O"
                board.setJugadorActual("O")
            if(board.getTablero()[fila, col]) != valor:
                board.setMovimiento(fila, col, valor)
        print(board.getTablero())
        print("Ha ganado el jugador " + self._jugador)


board = Tablero()
board.jugarPartida()