import pygame
import math
from random import randint
from sklearn.cluster import KMeans

def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


pygame.init()
screen = pygame.display.set_mode((1200, 658))  #   1280x658

pygame.display.set_caption('K-Means App')

clock = pygame.time.Clock()

# color
BACKGROUND = (200, 200, 200)
BLACK = (0,0,0)
WHITE = (255,255,255)
BACKGROUND_PANEL = (255,255,255) # = WHITE

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (147,152,35)
PURPLE = (255,0,255)
SKY = (0,255,255)
ORANGE = (255,125,25)
GRAPE = (100,25,125)
GRASS = (55,155,65)

COLOR = [RED,GREEN,BLUE,YELLOW,PURPLE,SKY,ORANGE,GRAPE,GRASS,BLACK]  # 10 colors

font = pygame.font.SysFont('sans', 40)
font_small = pygame.font.SysFont('sans', 15) # vẽ tọa độ chuột
text_plus = font.render('+', True, WHITE)
text_minus = font.render('-', True, WHITE)
text_run = font.render('Run', True, WHITE)
text_random = font.render('Random', True, WHITE)
text_algorithm = font.render('Algorithm', True, WHITE)
text_reset = font.render('Reset', True, WHITE)

running = True
k = 0
error = 0
points = []
clusters = []
labels = []

while running:
    clock.tick(60)
    screen.fill(BACKGROUND)
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # draw interface
    # draw panel
    pygame.draw.rect(screen, RED, (50,50,700,500))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (55,55,690,490))

    # draw k+ button
    pygame.draw.rect(screen, BLACK, (850,50,50,50))
    screen.blit(text_plus, (865,50))

    # draw k- button
    pygame.draw.rect(screen, BLACK, (950,50,50,50))
    screen.blit(text_minus, (970,50))

    # k value
    text_k = font.render('k = ' + str(k), True, BLACK)
    screen.blit(text_k, (1050, 50))

    # draw 'run' button
    pygame.draw.rect(screen, BLACK, (850,150,100,50))
    screen.blit(text_run, (870,150))

    # draw 'random' button
    pygame.draw.rect(screen, BLACK, (850,250,150,50))
    screen.blit(text_random, (863,250))

    # draw 'error' button
    # text_error = font.render('error = '+str(error), True, BLACK)
    # screen.blit(text_error, (850, 350))

    # draw 'algorithm' button
    pygame.draw.rect(screen, BLACK, (850,450,150,50))
    screen.blit(text_algorithm, (855,450))

    # draw 'reset' button
    pygame.draw.rect(screen, BLACK, (850,550,100,50))
    screen.blit(text_reset, (856,550))

    # draw mouse position when mouse is in the panel
    if 50 < mouse_x < 750 and 50 < mouse_y < 550:
        text_mouse = font_small.render('(' + str(mouse_x - 50) + ',' + str(mouse_y - 50) + ')', True, BLACK)
        screen.blit(text_mouse, (mouse_x + 10, mouse_y + 10))

    # end interface


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # create point on panel
            if 50 < mouse_x < 750 and 50 < mouse_y < 550:
                labels = []
                points.append([mouse_x-50, mouse_y-50])
                print(points)
            # press k+
            if 850<mouse_x<900 and 50<mouse_y<100:
                if k <= 9:
                    k += 1

            # press k-
            if 950<mouse_x<1000 and 50<mouse_y<100:
                if k>0:
                    k -= 1


            # run press
            if 850<mouse_x<950 and 150<mouse_y<200:
                labels = []

                if clusters != []:
                    # gán các điểm vào các cụm gần nhất
                    for pt in points:
                        distances_to_cluster = []
                        for c in clusters:
                            temp = distance(pt, c)
                            distances_to_cluster.append(temp)

                        min_distance = min(distances_to_cluster)
                        label = distances_to_cluster.index(min_distance) # 0,1,2,...len(clusters)
                        labels.append(label)

                    # update clusters
                    for i in range(len(clusters)):
                        sum_x, sum_y, count = 0, 0, 0
                        for j in range(len(points)):
                            if labels[j] == i:
                                sum_x += points[j][0]
                                sum_y += points[j][1]
                                count += 1

                        if count!=0:
                            clusters[i][0] = sum_x/count
                            clusters[i][1] = sum_y/count

                print("run press")

            # random button
            if 850<mouse_x<1000 and 250<mouse_y<300:
                clusters = []
                labels = [] # when puts random button-> all points are WHITE and error = 0
                for i in range(k):
                    rand_point = [randint(0,700), randint(0,500)]
                    clusters.append(rand_point)

            # algorithm button
            if 850<mouse_x<1000 and 450<mouse_y<500:
                if k == 0:
                    continue

                kmeans = KMeans(n_clusters=k).fit(points)
                labels = kmeans.predict(points)
                clusters = kmeans.cluster_centers_

            # reset button
            if 850<mouse_x<950 and 550<mouse_y<600:
                points, clusters, labels = [], [], []
                k = 0

    # draw random points
    for i in range(len(clusters)):
        pygame.draw.circle(screen, COLOR[i], (clusters[i][0]+50, clusters[i][1]+50), 5)

    # draw points
    for i in range(len(points)):
        pygame.draw.circle(screen, BLACK, (points[i][0]+50, points[i][1]+50), 3)
        if labels == []:
            pygame.draw.circle(screen, WHITE, (points[i][0]+50, points[i][1]+50), 2)
        else:
            # if len(labels)<len(points):
            #     if i<len(labels): # old
            #         pygame.draw.circle(screen, COLOR[labels[i]], (points[i][0]+50, points[i][1]+50), 3)
            #     else: # new
            #         pygame.draw.circle(screen, WHITE, (points[i][0]+50, points[i][1]+50), 2)
            # else:
            #     pygame.draw.circle(screen, COLOR[labels[i]], (points[i][0]+50, points[i][1]+50), 3)
            pygame.draw.circle(screen, COLOR[labels[i]], (points[i][0]+50, points[i][1]+50), 3)

    # calculate error
    error = 0
    if clusters != [] and labels != []:
        for i in range(len(points)):
            error += distance(points[i], clusters[labels[i]])
    
    text_error = font.render('error = '+str(int(error)), True, BLACK)
    screen.blit(text_error, (850, 350))

    pygame.display.flip()

pygame.quit()
