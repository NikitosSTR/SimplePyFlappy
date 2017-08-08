import string

from pygame import *

from bird import *
from ground import *
from platform import *

# Объявляем переменные
from score_label import Score_lable

# Ширина создаваемого окна
WIN_WIDTH = 640
# Высота
WIN_HEIGHT = 480
# Группируем ширину и высоту в одну переменную
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
# Цвет
BACKGROUND_COLOR = "#5fb1e1"


def main():
    # Инициация PyGame, обязательная строчка
    pygame.init()
    # Создаем оконо
    screen = pygame.display.set_mode(DISPLAY)
    # Пишем в шапку
    pygame.display.set_caption("Flappy bird")
    # Создание видимой поверхности
    bg = Surface((WIN_WIDTH,WIN_HEIGHT))

    play = False
    game_over = False
    score = 0
    jump = False
    pause = False

    timer = pygame.time.Clock()

    ground = Ground()

    platform1 = Platform(0)
    platform2 = Platform(400)

    bird = Bird()
                                                # будем использовать как фон
    bg.fill(Color(BACKGROUND_COLOR))            # Заливаем поверхность сплошным цветом

    entities = pygame.sprite.Group()
    platforms = []

    platforms.append(platform1)
    platforms.append(platform2)


    scr = Score_lable()

    scr.draw("Нажмите enter", screen)

    while 1: # Основной цикл программы

        timer.tick(60)

        for e in pygame.event.get():            # Обрабатываем события
            if e.type == QUIT:
                raise SystemExit(QUIT)

            if e.type == KEYDOWN and e.key == K_SPACE and not game_over:
                jump = True

            if e.type == KEYUP and e.key == K_SPACE:
                jump = False

            if e.type == KEYDOWN and e.key == K_p:
                pause = not pause

            if e.type == KEYDOWN and e.key == K_RETURN:
                game_over = False
                play = True
                score = 0
                bird = Bird()
                platform1 = Platform(0)
                platform2 = Platform(400)

                entities = pygame.sprite.Group()
                platforms = []
                platforms.append(platform1)
                platforms.append(platform2)

        if not pause:
            if play:
                game_over = bird.update(jump, platforms, ground)
            platform1.update()
            platform2.update()

            if game_over and play:
                score += 1
                print(score, '\n')


            screen.blit(bg, (0,0))                  # Каждую итерацию необходимо всё перерисовывать
            platform1.draw(screen)
            platform2.draw(screen)
            ground.draw(screen)

            if play:
                scr.draw(str(score), screen)
                bird.draw(screen)

            pygame.display.update()                 # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    main()