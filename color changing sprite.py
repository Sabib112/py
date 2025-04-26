import pygame

def main():
    pygame.init()
    screen_width, screen_height = 500,500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Color Changing Sprite")

    
    colors ={
        'red': pygame.Color('red'),
        'green': pygame.Color('green'),
        'blue': pygame.Color('blue'),
        'yellow': pygame.Color('yellow'),
        'purple': pygame.Color('purple')
    }
    current_color = colors['red']

    x, y= 30,30
    sprite_width, sprite_height = 60, 60

    clock = pygame.time.Clock()
    
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill((255, 255, 255))

        # Draw the sprite
        pygame.draw.rect(screen, current_color, (x, y, sprite_width, sprite_height))

        # Update the display
        pygame.display.flip()

        # Change color every 500 milliseconds
        current_color = colors[list(colors.keys())[pygame.time.get_ticks() // 500 % len(colors)]]

        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()