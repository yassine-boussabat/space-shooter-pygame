import sys
import pygame
import random

pygame.init()  # lezem bch t5adem pygame
pygame.mixer.init()  # lezem bch thot laswat

orth = 480
toul = 600
WINDOW_SIZE = (800, 600)
fps = 100

screen = pygame.display.set_mode((orth, toul))  # tasna3 escreen
clock = pygame.time.Clock()  # lezma llfps
pygame.display.set_caption("salem")

font_name = pygame.font.match_font('Public Pixel')


def lives(surf, x, y, lives, img):
    for i in range(lives):
        im_rect = img.get_rect()
        im_rect.y = y
        im_rect.x = x + 30 * i
        surf.blit(img, im_rect)


def text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text = font.render(text, True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text, text_rect)


def draw_shield(surf, x, y, prct):
    if prct < 0:
        prct = 0
    bar_toul = 100
    bar_erti = 20
    fill = (prct / 100) * bar_toul
    outline_rect = pygame.Rect(x, y, bar_toul, bar_erti)
    fill_rect = pygame.Rect(x, y, fill, bar_erti)
    pygame.draw.rect(surf, (0, 255, 0), fill_rect)
    pygame.draw.rect(surf, (255, 255, 255), outline_rect, 2)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("playerShip1_blue.png").convert()
        self.image = pygame.transform.scale(self.image, (50, 38))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = orth / 2
        self.rect.bottom = toul - 10
        self.speedx = 0
        self.shield = 100
        self.delait = 200
        self.last_shoot = pygame.time.get_ticks()
        self.live = 3
        self.hide = False
        self.hide_timer = pygame.time.get_ticks()

    def update(self):
        if self.hide == True and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hide = False
            self.rect.centerx = orth / 2
            self.rect.bottom = toul - 10
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -7
        if keystate[pygame.K_RIGHT]:
            self.speedx = 7
        if keystate[pygame.K_SPACE] and self.hide == False:
            self.shoot()
        self.rect.x += self.speedx
        if self.rect.right > orth:
            self.rect.right = orth
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shoot > self.delait:
            self.last_shoot = now
            bullet1 = Bullet(self.rect.right, self.rect.top)
            bullet2 = Bullet(self.rect.left, self.rect.top)
            all_sprites.add(bullet1)
            all_sprites.add(bullet2)
            bullets.add(bullet1)
            bullets.add(bullet2)
            shoot_sound.play()

    def hiden(self):
        self.hide = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (orth / 2, toul + 200)


class mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orrig = random.choice(naizakimage)
        # self.image_orrig=pygame.transform.scale(self.image_orrig, (30, 30))
        self.image_orrig.set_colorkey((0, 0, 0))
        self.image = self.image_orrig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .9 / 2)
        self.rect.x = random.randrange(orth - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 5)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orrig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.speedy = random.randrange(1, 8 + score // 1000)
        self.rotate()
        self.rect.y += self.speedy
        if self.rect.top > toul - 10:
            self.rect.x = random.randrange(orth - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("laserBlue01.png ").convert()
        self.image = pygame.transform.scale(self.image, (10, 20))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.speedy = -5
        self.rect.bottom = y
        self.rect.centerx = x

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


class Explotion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explotion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 30

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explotion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explotion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


def show_text():
    screen.blit(background, background_rect)
    text(screen, "ZLIBI", 50, orth / 2, toul / 4)
    text(screen, "arrow keys to move", 12, orth / 2, toul / 2)
    text(screen, "space to shoot!", 12, orth / 2, toul / 2 + 30)
    text(screen, "press enter to begun", 20, orth / 2, toul * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                waiting = False


explotion_anim = {}
explotion_anim['lg'] = []
explotion_anim['sm'] = []
explotion_anim['player'] = []
explotion_anim['players'] = []
for i in range(1, 7):
    file = '{}.png'.format(i)
    im = pygame.image.load(file).convert()
    im.set_colorkey((255, 255, 255))
    im_lg = pygame.transform.scale(im, (75, 75))
    explotion_anim['lg'].append(im_lg)
    im_sm = pygame.transform.scale(im, (32, 32))
    explotion_anim['sm'].append(im_sm)
    im_pl = pygame.transform.scale(im, (100, 100))
    explotion_anim['player'].append(im_pl)
    explotion_anim['players'].append(im_sm)

explotion2 = pygame.mixer.Sound("Explosion5.wav")
explotion2.set_volume(0.3)
pygame.mixer.music.load("tgfcoder-FrozenJam-SeamlessLoop.ogg")
pygame.mixer.music.set_volume(0.4)
shoot_sound = pygame.mixer.Sound("sfx_laser1.ogg")
shoot_sound.set_volume(0.5)
explotion = pygame.mixer.Sound("Explosion13.wav")
explotion.set_volume(0.3)
naizakimage = []
naizaklist = ["meteorGrey_big1.png", "meteorGrey_big2.png", "meteorGrey_big3.png", "meteorGrey_big4.png",
              "meteorGrey_med1.png", "meteorGrey_med2.png", "meteorGrey_small1.png", "meteorGrey_small2.png "]
for image in naizaklist:
    naizakimage.append(pygame.image.load(image).convert())
background = pygame.image.load("back.png").convert()
background_rect = background.get_rect()

pygame.mixer.music.play(loops=-1)
running = True
game_over = True
while running:
    if game_over:
        show_text()
        game_over = False
        all_sprites = pygame.sprite.Group()  # thot esprites el kol fi groupe
        mobs = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        player = Player()  # defini player bl class Player()
        player_mini = pygame.transform.scale(player.image, (25, 19))
        all_sprites.add(player)  # tzid lplayer llall sprites
        for i in range(8):
            m = mob()
            all_sprites.add(m)
            mobs.add(m)
        score = 0
    screen.fill((255, 250, 0))
    screen.blit(background, background_rect)
    clock.tick(fps)
    # update
    all_sprites.update()  # bch t5ali eli ysir fi ey sprite ysir fl kol
    all_sprites.draw(screen)
    text(screen, str(score), 20, orth / 2, 10)
    draw_shield(screen, 5, 5, player.shield)
    lives(screen, orth - 100, 5, player.live, player_mini)
    pygame.display.flip()  # thotha ba3ed kol tabdil fscreen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    for hit in hits:
        player.shield -= hit.radius * 1.5
        death_explotion = Explotion(player.rect.center, 'players')
        all_sprites.add(death_explotion)
        m = mob()
        all_sprites.add(m)
        mobs.add(m)
        explotion2.play()
        if player.shield <= 0:
            death_explotion = Explotion(player.rect.center, 'player')
            all_sprites.add(death_explotion)
            player.hiden()
            player.live -= 1
            player.shield = 100
    if player.live == 0 and not death_explotion.alive():
        game_over = True
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        score += abs(50 - int(hit.radius))
        expl = Explotion(hit.rect.center, "lg")
        all_sprites.add(expl)
        m = mob()
        all_sprites.add(m)
        mobs.add(m)
        explotion.play()
