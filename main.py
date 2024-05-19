import pygame
import subprocess
import os

# Initialize Pygame
pygame.init()




# Screen dimensions
WIDTH, HEIGHT = 900, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Home Page")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (204, 153, 102)
TEAL = (255, 255, 255)
LIGHT_GRAY = (160, 160, 160)

# Load background image
background = pygame.image.load('background2.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Load traditional-looking fonts
font_large = pygame.font.SysFont('Times New Roman', 60)
font_lesslarge = pygame.font.SysFont('Times New Roman',35)
font_medium = pygame.font.SysFont('Times New Roman', 25)
font_small = pygame.font.SysFont('Times New Roman', 20)

# Button settings
button_width, button_height = 300, 70
button_padding = 20
link_padding = 30

# Text positions
heading_y = 50
heading_x = 100
button_x = (WIDTH - button_width) // 2
button_y_start = heading_y + 100

# Load images
images = {
    "pallankuzhi_rules": pygame.image.load('pallankuzhi_rules.jpg'),
    "pallankuzhi_history": pygame.image.load('pallankuzhi_history.jpg'),
    "ludo_rules": pygame.image.load('ludo_rules.jpg'),
    "ludo_history": pygame.image.load('ludo_history.jpg'),
    "tiger_and_lambs_rules": pygame.image.load('tiger_and_lambs_rules.jpg'),
    "tiger_and_lambs_history": pygame.image.load('tiger_and_lambs_history.png')
}

def draw_text(screen, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def draw_button(screen, text, x, y, width, height):
    pygame.draw.rect(screen, GRAY, (x, y, width, height), border_radius=5)
    text_surface = font_medium.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

def draw_link(screen, text, x, y):
    text_surface = font_small.render(text, True, TEAL)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def main_menu():
    running = True
    while running:
        screen.blit(background, (0, 0))
        
        # Draw heading
        draw_text(screen, "PUNARUTTHAAN", font_large, BLACK, WIDTH // 2, heading_y)
        draw_text(screen, "key to ancient games", font_lesslarge, BLACK, WIDTH // 2, heading_x)

        
        # Draw game buttons and links
        draw_button(screen, "Pallankuzhi (Bot)", button_x, button_y_start, button_width, button_height)
        draw_link(screen, "Rules", button_x + button_width // 4, button_y_start + button_height + 20)
        draw_link(screen, "History", button_x + 3 * button_width // 4, button_y_start + button_height + 20)

        draw_button(screen, "Pagade(Multiplayer)", button_x, button_y_start + 2 * (button_height + button_padding), button_width, button_height)
        draw_link(screen, "Rules", button_x + button_width // 4, button_y_start + 3 * button_height + 2 * button_padding + 20)
        draw_link(screen, "History", button_x + 3 * button_width // 4, button_y_start + 3 * button_height + 2 * button_padding + 20)

        draw_button(screen, "Aadu Puli Aatam(Multiplayer)", button_x, button_y_start + 4 * (button_height + button_padding), button_width, button_height)
        draw_link(screen, "Rules", button_x + button_width // 4, button_y_start + 5 * button_height + 4 * button_padding + 20)
        draw_link(screen, "History", button_x + 3 * button_width // 4, button_y_start + 5 * button_height + 4 * button_padding + 20)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if button_x <= mouse_x <= button_x + button_width:
                    if button_y_start <= mouse_y <= button_y_start + button_height:
                        launch_game("Pallankuzhi")
                    elif button_y_start + 2 * (button_height + button_padding) <= mouse_y <= button_y_start + 3 * button_height + 2 * button_padding:
                        launch_game("Pagade")
                    elif button_y_start + 4 * (button_height + button_padding) <= mouse_y <= button_y_start + 5 * button_height + 4 * button_padding:
                        launch_game("Lambs-and-Tigers")
                # Link clicks
                if button_y_start + button_height <= mouse_y <= button_y_start + button_height + link_padding:
                    if button_x + button_width // 4 - 30 <= mouse_x <= button_x + button_width // 4 + 30:
                        display_image('pallankuzhi_rules')
                    elif button_x + 3 * button_width // 4 - 30 <= mouse_x <= button_x + 3 * button_width // 4 + 30:
                        display_image('pallankuzhi_history')
                elif button_y_start + 3 * button_height + 2 * button_padding <= mouse_y <= button_y_start + 3 * button_height + 2 * button_padding + link_padding:
                    if button_x + button_width // 4 - 30 <= mouse_x <= button_x + button_width // 4 + 30:
                        display_image('ludo_rules')
                    elif button_x + 3 * button_width // 4 - 30 <= mouse_x <= button_x + 3 * button_width // 4 + 30:
                        display_image('ludo_history')
                elif button_y_start + 5 * button_height + 4 * button_padding <= mouse_y <= button_y_start + 5 * button_height + 4 * button_padding + link_padding:
                    if button_x + button_width // 4 - 30 <= mouse_x <= button_x + button_width // 4 + 30:
                        display_image('tiger_and_lambs_rules')
                    elif button_x + 3 * button_width // 4 - 30 <= mouse_x <= button_x + 3 * button_width // 4 + 30:
                        display_image('tiger_and_lambs_history')

    pygame.quit()

def launch_game(game_name):
    print(f"Current working directory: {os.getcwd()}")
    if game_name == "Pagade":
        game_dir = os.path.join(os.getcwd(), "Ludo-Python-game-")
        game_path = os.path.join(game_dir, "Ludogame.py")
    else:
        game_dir = os.path.join(os.getcwd(), game_name)
        game_path = os.path.join(game_dir, f"{game_name}.py")
    
    print(f"Attempting to launch game at path: {game_path}")
    if os.path.isfile(game_path):
        # Run the game in a separate process and change the working directory
        subprocess.run(["python", game_path], cwd=game_dir)
    else:
        print(f"File not found: {game_path}")

def launch_game(game_name):
    print(f"Current working directory: {os.getcwd()}")
    if game_name == "Aadu Puli Aatam":
        game_dir = os.path.join(os.getcwd(), "Lambs-and-Tigers")
        game_path = os.path.join(game_dir, "Tiger.py")
    else:
        game_dir = os.path.join(os.getcwd(), game_name)
        game_path = os.path.join(game_dir, f"{game_name}.py")
    
    print(f"Attempting to launch game at path: {game_path}")
    if os.path.isfile(game_path):
        # Run the game in a separate process and change the working directory
        subprocess.run(["python", game_path], cwd=game_dir)
    else:
        print(f"File not found: {game_path}")







def launch_game(game_name):
    print(f"Current working directory: {os.getcwd()}")
    if game_name == "Pallankuzhi":
        game_dir = os.path.join(os.getcwd(), "pallankuzhi20000")
        game_path = os.path.join(game_dir, "pallankuzhi.py")
    else:
        game_dir = os.path.join(os.getcwd(), game_name)
        game_path = os.path.join(game_dir, f"{game_name}.py")
    
    print(f"Attempting to launch game at path: {game_path}")
    if os.path.isfile(game_path):
        # Run the game in a separate process and change the working directory
        subprocess.run(["python", game_path], cwd=game_dir)
    else:
        print(f"File not found: {game_path}")

def display_image(image_name):
    running = True
    image = images[image_name]
    while running:
        screen.fill(WHITE)
        screen.blit(image, ((WIDTH - image.get_width()) // 2, (HEIGHT - image.get_height()) // 2))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False


if __name__ == "__main__":
    main_menu()
    
