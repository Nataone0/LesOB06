class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        print("Игра 'Битва героев' началась!")
        print("Ваши характеристики:",
              f"Имя: {self.player.name}, Здоровье: {self.player.health}, Сила удара: {self.player.attack_power}")
        print("Характеристики противника:",
              f"Имя: {self.computer.name}, Здоровье: {self.computer.health}, Сила удара: {self.computer.attack_power}\n")

        turn = 0
        while self.player.is_alive() and self.computer.is_alive():
            self.print_turn(turn)
            if turn % 2 == 0:  # Ход игрока
                self.player_turn()
            else:  # Ход компьютера
                self.computer_turn()
            turn += 1

        self.declare_winner()
        self.play_again()

    def player_turn(self):
        input("Нажмите Enter, чтобы атаковать!")
        self.player.attack(self.computer)
        self.display_status(self.computer)

    def computer_turn(self):
        print("Компьютер атакует...")
        self.computer.attack(self.player)
        self.display_status(self.player)

    def display_status(self, hero):
        if hero.is_alive():
            print(f"{hero.name} имеет {hero.health} здоровья.")
        else:
            print(f"{hero.name} пал в бою!")

    def declare_winner(self):
        if self.player.is_alive():
            print("\nПоздравляем! Вы победили!")
        else:
            print("\nК сожалению, вы проиграли. Попробуйте снова!")

    def play_again(self):
        response = input("\nХотите сыграть ещё раз? (да/нет): ")
        if response.lower() == 'да':
            self.player.health = 100  # Сброс здоровья
            self.computer.health = 100
            self.start()
        else:
            print("Спасибо за игру!")

    def print_turn(self, turn):
        if turn % 2 == 0:
            print("\nВаш ход")
        else:
            print("\nХод противника")


# Создание героев и запуск игры
if __name__ == "__main__":
    player_hero = Hero("Герой Игрока")
    computer_hero = Hero("Герой Компьютера")

    game = Game(player_hero, computer_hero)
    game.start()

