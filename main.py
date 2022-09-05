class Map:
    def __init__(self, turn: int = 0):
        self.p: dict[str, str] = {f"p{x + 1}": f"P{x + 1}" for x in range(9)}
        self.turn: int = turn

    def return_map(self):
        return f"""Turno: {self.turn}

 {self.p.get("p1")} | {self.p.get("p2")} | {self.p.get("p3")}
----+----+----
 {self.p.get("p4")} | {self.p.get("p5")} | {self.p.get("p6")}
----+----+----
 {self.p.get("p7")} | {self.p.get("p8")} | {self.p.get("p9")}
""".replace("False", "x ").replace("True", "o ")


class Move(Map):
    def __init__(self) -> None:
        super().__init__()
        self.combos: list[int] = [1, 2, 3,
                                  4, 5, 6,
                                  7, 8, 9,
                                  1, 5, 9,
                                  3, 5, 7,
                                  1, 4, 7,
                                  2, 5, 8,
                                  3, 6, 9]

    def play(self, pos: str, t_f: bool) -> bool:
        if type(self.p.get(pos)) != str:
            return False
        else:
            self.p.pop(pos)
            self.p.update({str(pos): t_f})
            return True

    def next_move(self, pos: str, t_f: bool) -> bool:
        while True:
            try:
                test: bool = self.play(pos=pos, t_f=t_f)
                if test:
                    return True
                else:
                    print("Insira uma posição válida.")
                    return False
            except KeyError:
                return False

    def check_winner(self, t_f: bool) -> bool:
        for x in range(0, len(self.combos), 3):
            if (self.p.get(f"p{self.combos[x]}") == t_f
                    and self.p.get(f"p{self.combos[x + 1]}") == t_f
                    and self.p.get(f"p{self.combos[x + 2]}") == t_f):
                return True
            else:
                pass


if __name__ == "__main__":
    game: 'Move' = Move()
    t_f: bool = False
    player: str = ""

    for x in range(9 + 1):
        game.turn += 1
        print(game.return_map())  # Imprime a situação atual do mapa no console
        if game.turn % 2 == 0:
            t_f: bool = True
            player: str = "o"
        else:
            t_f: bool = False
            player: str = "x"

        choice: str = str(input(f"""Posição que você quer marcar com "{player}": """)).lower()
        while True:
            if game.next_move(pos=choice, t_f=t_f):
                break
            else:
                choice: str = str(input(f"""Posição que você quer marcar com "{player}": """)).lower()

        if game.check_winner(t_f=t_f):
            print("Entrou no if")
            print(f"{player} ganhou!")
            break

        else:
            pass
