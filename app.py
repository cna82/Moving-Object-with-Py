import pygame
import sys

# رنگ‌ها
Dark = (45, 45, 45)
lime_accent = (198, 255, 0)

# شروع pygame
pygame.init()

# تنظیمات صفحه
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("حرکت دایره")

# مشخصات دایره
circle_x = 350
circle_y = 250
circle_radius = 20
circle_speed_x = 2
circle_speed_y = 2

# حلقه اصلی
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # منطق حرکت
    circle_x += circle_speed_x
    circle_y += circle_speed_y

    # برخورد با لبه‌ها
    if circle_x > 700 - circle_radius or circle_x < circle_radius:
        circle_speed_x = -circle_speed_x
    if circle_y > 500 - circle_radius or circle_y < circle_radius:
        circle_speed_y = -circle_speed_y

    # رسم
    screen.fill(Dark)
    pygame.draw.circle(screen, lime_accent, (circle_x, circle_y), circle_radius)
    pygame.display.flip()

    # کنترل فریم‌ها
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
