class Hero:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.health: int = 100
        self.attack_power: int = 20

    @classmethod
    def attack(cls, other) -> None:
        if other.health > 20:
            other.health -= 20
        else:
            other.health = 0

    def is_alive(self) -> bool:
        if self.health > 0:
            return True
        else:
            return False


class Game:
    def __init__(self) -> None:
        self.player: Hero = Hero('Player')
        self.computer: Hero = Hero('Computer')
        print(f'Создан герой для игрока: {self.player.name}')
        print(f'Создан герой для компьютера: {self.computer.name}')

    def start(self) -> None:
        print('\nНачало игры!')
        while self.player.is_alive() or self.computer.is_alive():
            self.player.attack(self.computer)
            print(f'Игрок ударил {int((100 - self.computer.health) / 20)} раз, здоровье игрока: {self.player.health}')
            if not self.computer.is_alive():
                break

            self.computer.attack(self.player)
            print(f'Компьютер ударил {int((100 - self.computer.health) / 20)} раз, здоровье компьютера: {self.player.health}')
            if not self.player.is_alive():
                break

        if self.player.is_alive():
            print('\nВы победили. Компьютер повержен!')
        else:
            print('\nПобедил компьютер, Вы повержены!')


# Программа
if __name__ == '__main__':

    # Тестирование класса игрок
    new_hero = Hero('Мощный воин')
    print(new_hero.name)
    print(new_hero.health)
    print(new_hero.attack_power)
    print('Тест завершен\n')

    # Тестирование класса игра
    new_game = Game()
    new_game.start()