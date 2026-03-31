import pygame
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Secretman Newspaper")

# Colors
PAPER = (244, 241, 232)
BLACK = (0, 0, 0)

# Fonts
title_font = pygame.font.SysFont("timesnewroman", 50, bold=True)
subtitle_font = pygame.font.SysFont("timesnewroman", 24, italic=True)
text_font = pygame.font.SysFont("timesnewroman", 20)

# Text content
title = title_font.render("THE SECRET TIMES", True, BLACK)
headline = subtitle_font.render("Mysterious Man Goes Missing...", True, BLACK)

article_lines = [
    "A man known only as 'Secretman' has vanished without a trace.",
    "Witnesses claim he was last seen carrying a newspaper.",
    "Strangely, reports describe a baby calmly reading the article",
    "shortly after his disappearance.",
    "",
    "Authorities remain confused as no clues have been found.",
    "The baby, unharmed, continues to stare at the paper silently.",
    "",
    "Who is Secretman? And what does the child know?"
]

clock = pygame.time.Clock()

while True:
    screen.fill(PAPER)

    # Draw title
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))
    pygame.draw.line(screen, BLACK, (50, 90), (850, 90), 2)

    # Draw headline
    screen.blit(headline, (60, 110))

    # Draw article text
    y_offset = 160
    for line in article_lines:
        text = text_font.render(line, True, BLACK)
        screen.blit(text, (60, y_offset))
        y_offset += 30

    # Draw simple "baby reading" visual (stick figure)
    pygame.draw.circle(screen, BLACK, (750, 350), 20)  # head
    pygame.draw.line(screen, BLACK, (750, 370), (750, 430), 3)  # body
    pygame.draw.line(screen, BLACK, (750, 390), (720, 410), 3)  # left arm
    pygame.draw.line(screen, BLACK, (750, 390), (780, 410), 3)  # right arm

    # Newspaper in baby's hands
    pygame.draw.rect(screen, BLACK, (720, 410, 60, 40), 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)
