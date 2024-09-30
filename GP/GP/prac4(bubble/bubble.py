import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600

WHITE = (255, 255, 255)
PINK = (255, 192, 203)

balloonPath = "balloon.png"
archerPath = "archer.png"
arrowPath = "arrow.png"

font = pygame.font.Font('freesansbold.ttf', 20)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balloon Archer")

clock = pygame.time.Clock()
FPS = 30
class Archer:
    def __init__(self, width, height, speed):
        self.width = width
        self.height = height
        self.speed = speed

        self.archer = pygame.transform.scale(
            pygame.image.load(archerPath), (self.width, self.height))
        self.archerRect = self.archer.get_rect()

        self.archerRect.x, self.archerRect.y = 100, HEIGHT//2

    def display(self):
        screen.blit(self.archer, self.archerRect)

    def update(self, xFac, yFac):
        self.archerRect.x += xFac*self.speed
        self.archerRect.y += yFac*self.speed

        if self.archerRect.x <= 0:
            self.archerRect.x = 0
        elif self.archerRect.x >= WIDTH//2 - self.archerRect.w:
            self.archerRect.x = WIDTH//2 - self.archerRect.w
        if self.archerRect.y <= 0:
            self.archerRect.y = 0
        elif self.archerRect.y >= HEIGHT-self.archerRect.h:
            self.archerRect.y = HEIGHT - self.archerRect.h

class Balloon:
    def __init__(self, posx, posy, width, height, speed):
        self.width, self.height = width, height
        self.speed = speed

        self.balloonImg = pygame.image.load(balloonPath)
        self.balloon = pygame.transform.scale(
            self.balloonImg, (self.width, self.height))
        self.balloonRect = self.balloon.get_rect()

        self.balloonRect.x, self.balloonRect.y = posx, posy

    def display(self):
        screen.blit(self.balloon, self.balloonRect)

    def update(self):
        self.balloonRect.y -= self.speed

        if self.balloonRect.y < 0:
            self.balloonRect.y = HEIGHT + 10

class Arrow:
    def __init__(self, posx, posy, width, height, speed):
        self.width, self.height = width, height
        self.speed = speed
        self.hit = 0

        self.arrow = pygame.transform.scale(
            pygame.image.load(arrowPath), (width, height))
        self.arrowRect = self.arrow.get_rect()

        self.arrowRect.x, self.arrowRect.y = posx, posy

    def display(self):
        screen.blit(self.arrow, self.arrowRect)

    def update(self):
        self.arrowRect.x += self.speed

    def updateHit(self):
        self.hit = 1

    def getHit(self):
        return self.hit

def populateBalloons(bWidth, bHeight, bSpeed, bCount):
    listOfBalloons = []

    for _ in range(bCount):
        listOfBalloons.append(Balloon(random.randint(
            WIDTH//2, WIDTH-bWidth), random.randint(0, HEIGHT),
            bWidth, bHeight, bSpeed))

    return listOfBalloons

def gameOver():
    gameOver = True

    while gameOver:
        gameOverText = font.render("GAME OVER", True, WHITE)
        retryText = font.render("R - Replay    Q - Quit", True, WHITE)

        screen.blit(gameOverText, (WIDTH//2-200, HEIGHT//2-100))
        screen.blit(retryText, (WIDTH//2-200, HEIGHT//2-80))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True
                if event.key == pygame.K_q:
                    return False

        pygame.display.update()

def main():
    score = 0
    lives = 5
    running = True

    archer = Archer(60, 60, 7)
    xFac, yFac = 0, 0

    numBalloons = 10

    listOfBalloons = populateBalloons(30, 40, 5, numBalloons)
    listOfArrows = []

    while running:
        screen.fill(PINK)

        for i in range(lives):
            screen.blit(pygame.transform.rotate(pygame.transform.scale(
                pygame.image.load(arrowPath), (20, 30)), 45), (i*30, 10))

        scoreText = font.render(f"Score: {score}", True, WHITE)
        screen.blit(scoreText, (10, HEIGHT-50))

        if len(listOfBalloons) == 0:
            listOfBalloons = populateBalloons(30, 40, 5, numBalloons)

        if lives <= 0:
            running = gameOver()

            listOfBalloons.clear()
            listOfArrows.clear()

            lives = 5
            score = 0
            listOfBalloons = populateBalloons(30, 40, 5, numBalloons)

        for balloon in listOfBalloons:
            balloon.update()
            balloon.display()

        for arrow in listOfArrows:
            arrow.update()
            arrow.display()

        archer.display()
        archer.update(xFac, yFac)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    listOfBalloons = populateBalloons(30, 40, 5, numBalloons)
                    score = 0
                if event.key == pygame.K_RIGHT:
                    xFac = 1
                if event.key == pygame.K_LEFT:
                    xFac = -1
                if event.key == pygame.K_DOWN:
                    yFac = 1
                if event.key == pygame.K_UP:
                    yFac = -1
                if event.key == pygame.K_SPACE:
                    listOfArrows.append(Arrow(
                        archer.archerRect.x,
                        archer.archerRect.y+archer.archerRect.h/2-15, 60, 30, 10))

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    xFac = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    yFac = 0

        for arrow in listOfArrows:
            for balloon in listOfBalloons:
                if pygame.Rect.colliderect(arrow.arrowRect, balloon.balloonRect):
                    arrow.updateHit()
                    listOfBalloons.pop(listOfBalloons.index(balloon))
                    score += 1

        for arrow in listOfArrows:
            if arrow.arrowRect.x > WIDTH:
                if not arrow.getHit():
                    lives -= 1
                listOfArrows.pop(listOfArrows.index(arrow))

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
    pygame.quit()
