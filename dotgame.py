import math
import sys

import pygame

pygame.init()
scr = pygame.display

x = y = 500
boxes = (x / 50 - 2) ** 2
n = 0
temp_line = False
drag = False
connected_obj = []
selected_obj = ''
rival = False
s1, s2 = 0, 0
box = []

red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

screen = scr.set_mode((x, y + 20))
scr.set_caption("Dot Game")

dot_obj = [pygame.draw.circle(screen, red, (i, j), 10, 1) for i in range(50, x, 50) for j in range(50, y, 50)]
score = pygame.font.SysFont("monospace", 16)


def update_score(score1, score2, font):
    sc1 = font.render(str(score1), 1, green, black)
    sc2 = font.render(str(score2), 1, green, black)
    screen.blit(sc1, ((x / 100) * 33.33, x))
    screen.blit(sc2, ((x / 100) * 66.66, x))


while True:
    mx, my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for obj in dot_obj:
                if obj.collidepoint(mx, my):
                    drag = True
                    selected_obj = obj
        elif event.type == pygame.MOUSEBUTTONUP and selected_obj:
            drag = False
            for obj in dot_obj:
                if obj.collidepoint(mx, my):
                    dist = math.dist(obj.center, selected_obj.center)
                    if dist == 50:
                        c = [selected_obj.center, obj.center]
                        c.sort()

                        if c not in connected_obj:
                            connected_obj.append(c)
                        else:
                            print("Already connected !!")
                            break

                        if rival:
                            rival = False
                        else:
                            rival = True

                        if rival:
                            pygame.draw.line(screen, red, selected_obj.center, obj.center, 3)
                        else:
                            pygame.draw.line(screen, green, selected_obj.center, obj.center, 3)

                        selected_obj = ''

                        a = [obj.center, tuple(map(lambda i, j: i + j, obj.center, (50, 0)))]
                        a.sort()
                        b = [obj.center, tuple(map(lambda i, j: i + j, obj.center, (0, 50)))]
                        b.sort()
                        c = [tuple(map(lambda i, j: i + j, obj.center, (0, 50))),
                             tuple(map(lambda i, j: i + j, obj.center, (50, 50)))]
                        c.sort()
                        d = [tuple(map(lambda i, j: i + j, obj.center, (50, 50))),
                             tuple(map(lambda i, j: i + j, obj.center, (50, 0)))]
                        d.sort()
                        e = [tuple(map(lambda i, j: i + j, obj.center, (50, 0))),
                             tuple(map(lambda i, j: i + j, obj.center, (50, -50)))]
                        e.sort()
                        f = [tuple(map(lambda i, j: i + j, obj.center, (50, -50))),
                             tuple(map(lambda i, j: i + j, obj.center, (0, -50)))]
                        f.sort()
                        g = [tuple(map(lambda i, j: i + j, obj.center, (0, -50))),
                             obj.center]
                        g.sort()
                        h = [obj.center,
                             tuple(map(lambda i, j: i + j, obj.center, (-50, 0)))]
                        h.sort()
                        i = [tuple(map(lambda i, j: i + j, obj.center, (-50, 0))),
                             tuple(map(lambda i, j: i + j, obj.center, (-50, -50)))]
                        i.sort()
                        j = [tuple(map(lambda i, j: i + j, obj.center, (-50, -50))),
                             tuple(map(lambda i, j: i + j, obj.center, (0, -50)))]
                        j.sort()
                        k = [tuple(map(lambda i, j: i + j, obj.center, (-50, 0))),
                             tuple(map(lambda i, j: i + j, obj.center, (-50, 50)))]
                        k.sort()
                        m = [tuple(map(lambda i, j: i + j, obj.center, (-50, 50))),
                             tuple(map(lambda i, j: i + j, obj.center, (0, 50)))]
                        m.sort()

                        if a in connected_obj and b in connected_obj and c in connected_obj and d in connected_obj:
                            _box = [a, b, c, d]
                            _box.sort()
                            if _box not in box:
                                n += 1
                            box.append(_box)

                        if a in connected_obj and e in connected_obj and f in connected_obj and g in connected_obj:
                            _box = [a, e, f, g]
                            _box.sort()
                            if _box not in box:
                                n += 1
                            box.append(_box)

                        if h in connected_obj and i in connected_obj and j in connected_obj and g in connected_obj:
                            _box = [h, i, j, g]
                            _box.sort()
                            if _box not in box:
                                n += 1
                            box.append(_box)

                        if h in connected_obj and k in connected_obj and m in connected_obj and b in connected_obj:
                            _box = [h, k, m, b]
                            _box.sort()
                            if _box not in box:
                                n += 1
                            box.append(_box)

                        if rival:
                            s2 = s2 + n
                        else:
                            s1 = s1 + n

                        n = 0

                        update_score(s1, s2, score)
                        if s1 + s2 == boxes:
                            if s1 > s2:
                                update_score("WIN", "lose", score)
                            elif s2 > s1:
                                update_score("lose", "WIN", score)
                            else:
                                update_score("TIE", "TIE", score)

        if event.type == pygame.QUIT:
            sys.exit()
    scr.update()
