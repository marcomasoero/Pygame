import pygame
import random

class Car:
    """classe macchina, dove definisco le variabili per la posizione ed il colore"""
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        
    def draw(self, screen):
        """disegno la macchina con draw"""
        pygame.draw.rect(screen, self.color, [self.x + 10, self.y + 4, 60, 16])
        pygame.draw.rect(screen, self.color, [self.x + 27.5, self.y + 10, 25, 80])
        pygame.draw.rect(screen, self.color, [self.x, self.y + 90, 80, 16])
        pygame.draw.rect(screen, (0, 0, 0), [self.x + 18.5, self.y + 24, 10, 20])
        pygame.draw.rect(screen, (0, 0, 0), [self.x + 18.5, self.y + 60, 10, 20])
        pygame.draw.rect(screen, (0, 0, 0), [self.x + 50, self.y + 24, 10, 20])
        pygame.draw.rect(screen, (0, 0, 0), [self.x + 50, self.y + 60, 10, 20])
        
class Traffic:
    """classe traffico, dove definisco le variabili per la posizione ed il colore"""
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        
    def draw(self, screen):
        """disegno il traffico con draw"""
        pygame.draw.rect(screen, (self.color), [self.x, self.y + 4, 80, 16])
        pygame.draw.rect(screen, (self.color), [self.x + 27.5, self.y + 20, 25, 80])
        pygame.draw.rect(screen, (self.color), [self.x + 10, self.y + 90, 60, 16])
        pygame.draw.rect(screen, (0, 0, 0), [self.x + 18.5, self.y + 24, 10, 20])
        pygame.draw.rect(screen, (0, 0, 0), [self.x + 18.5, self.y + 60, 10, 20])
        pygame.draw.rect(screen, (0, 0, 0), [self.x + 50, self.y + 24, 10, 20])
        pygame.draw.rect(screen, (0, 0, 0), [self.x + 50, self.y + 60, 10, 20])
        
class Game:
    """la classe più corposa, che funge anche da main, è quella di gioco"""
    
    def __init__(self):
        """definisco tutti gli elementi che mi servono come variabili o costanti per il gioco"""
        pygame.init()
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 600, 600
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Maso F1")
        
        self.BLACK = (0, 0, 0)
        self.GREY = (128, 128, 128)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        
    def draw_track(self):
        """disegno il circuito"""
        pygame.draw.rect(self.screen, self.GREY, (0, 0, self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.draw.line(self.screen, self.WHITE, (40, 0), (40, self.SCREEN_HEIGHT), 10)
        pygame.draw.line(self.screen, self.WHITE, (self.SCREEN_WIDTH // 2, 0), (self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT), 10)
        pygame.draw.line(self.screen, self.WHITE, (self.SCREEN_WIDTH - 50, 0), (self.SCREEN_WIDTH - 50, self.SCREEN_HEIGHT), 10)
        pygame.draw.line(self.screen, self.GREEN, (0, 0), (0, self.SCREEN_HEIGHT), 70)
        pygame.draw.line(self.screen, self.GREEN, (self.SCREEN_WIDTH - 20, 0), (self.SCREEN_WIDTH - 20, self.SCREEN_HEIGHT), 50)
        
    def show_score(self, score):
        """mostro a schermo lo score, che incrementa ogni qual volta si schiva una macchina del traffico"""
        """assegno alla variabile score_written ciò che voglio appaia e la mostro nella posizione che desidero"""
        score_written = self.font.render("Score: " + str(score), True, self.WHITE)
        self.screen.blit(score_written, [430, 10])
    
    def show_best(self, best):
        """mostro a schermo il best"""
        """assegno alla variabile best_written ciò che voglio appaia e la mostro nella posizione che desidero"""
        best_written = self.font.render("Best: " + str(best), True, self.WHITE)
        self.screen.blit(best_written, [50, 10])
    
    def save_best(self, best, file_name):
        """se lo score del nuovo game risulta essere maggiore di quello precedente, salvo sul file il nuovo risultato"""
        with open(file_name, 'w') as file:
            file.write(str(best))
    
    def read_best(self, file_name):
        """leggo il best score da file"""
        with open(file_name, 'r') as file:
            best = int(file.read())
        return best
    
    def menu(self):
        """definisco il menu come oggetto della classe game"""
        self.screen.fill(self.BLUE)
        writing1 = self.font.render("Premi S Per Iniziare", True, self.WHITE)
        writing2 = self.font.render("Guida Più Che Puoi!!", True, self.WHITE)
        
        self.screen.blit(writing1, [self.SCREEN_WIDTH // 2 - 120, self.SCREEN_HEIGHT // 2 - 50])
        self.screen.blit(writing2, [self.SCREEN_WIDTH // 2 - 120, self.SCREEN_HEIGHT // 2])
        pygame.display.flip()
        
        wait = True
        while wait:
            """fino a che non si clicca su "s" il while resta in wait == true"""
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    wait = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
    
    def run(self):
        """tramite la chiamata a game.run faccio partire il gioco"""
        
        """passo per il menu di gioco"""
        self.menu()
        
        """definisco la posizione delle auto ed il colore"""
        x_car = self.SCREEN_WIDTH // 2
        y_car = self.SCREEN_HEIGHT - 120
        vel_car = 10
        
        """per il traffico la posizione è random"""
        x_traffic = random.randint(0, self.SCREEN_WIDTH - 100)
        y_traffic = -50
        vel_traffic = 10
        color_car = self.BLUE
        color_traffic = self.RED
        score = 0
        best = self.read_best('best.txt')

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            """definisco il movimento della macchina dando dei range"""
            """definisco il movimento tramite l'utilizzo delle freccette"""
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and x_car > 0:
                x_car -= vel_car
            if keys[pygame.K_RIGHT] and x_car < self.SCREEN_WIDTH - 50:
                x_car += vel_car
            
            """disegno il tracciato, la macchina e lo sfondo"""
            self.screen.fill(self.BLACK)
            self.draw_track()
            """passo come parametri la posizione ed il colore"""
            traffic = Traffic(x_traffic, y_traffic, color_traffic)
            traffic.draw(self.screen)
            y_traffic += vel_traffic
            """passo come parametri la posizione ed il colore"""
            car = Car(x_car, y_car, color_car)
            car.draw(self.screen)
            
            """mostro a schermo i valore dello score e del best"""
            self.show_score(score)
            self.show_best(best)
            
            """quando la macchina del traffico precedente raggiunge il fondo ne genero un'altra"""
            """azzero la y e assegno a x un valore random"""
            if y_traffic > self.SCREEN_HEIGHT:
                y_traffic = 0
                x_traffic = random.randint(0, self.SCREEN_WIDTH - 50)
                score += 10
                vel_traffic += 1
            
            """verifico l'eventuale collisione delle due macchine"""
            if y_car < (y_traffic + 112) and (y_car + 112) > y_traffic:
                if x_car < (x_traffic + 60) and (x_car + 60) > x_traffic:
                    self.menu()
                    """salvo il best se lo score è maggiore"""
                    if score > best:
                        best = score
                        self.save_best(best, 'best.txt')
                    """riporto le variabili ai valori standard"""
                    """la velocità aumenta ogni volta che si schiva un veicolo"""
                    vel_traffic = 10
                    """anche lo score aumenta ogni volta che si schiva un veicolo"""
                    score = 0
            
            """definisco un clock di aggiornamento dello schermo per il cambio di posizione degli elementi"""
            pygame.display.update()
            self.clock.tick(30)

if __name__ == "__main__":
    game = Game()
    game.run()