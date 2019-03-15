"""
The code is an original design of Denniel Luis S. Sadian
September 16, 2017
"""

import pygame
import sys
import os
from math import *


def load_png(name):
    fullname = os.path.join(name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error:
        raise SystemExit(f'Cannot load image: {fullname}')
    return image, image.get_rect()


class Brain:

    def __init__(self):
        self.calculation = ''
        self.result = '0'
        self.black = (0, 0, 0)
        self.grey = (195, 195, 195)
        self.words = 'fact sin cos tan exp mod dms deg sqrt Math Error' \
                     ' Divided by Zero Overflow Syntax Error fmod ( ) ** /'

    def receive_input(self, key):
        try:
            # numbers
            if key.name in '0123456789':
                if self.result == '0' or self.result in self.words:
                    self.result = key.name
                else:
                    self.result += key.name
            if key.name == '.':
                if '.' not in self.result:
                    self.result += key.name
            if key.name == 'π':
                self.result = str(pi)
            # backspace
            if key.name == '<=' and self.result != '0':
                self.result = self.result[:-1]
                if self.result == '':
                    self.result = '0'
            # cancel
            if key.name == 'C':
                self.calculation = ''
                self.result = '0'
            # cancel equation
            if key.name == 'CE':
                for i in self.words.split():
                    if i in self.calculation:
                        self.result = '0'
                        self.calculation = ''
                self.result = '0'

            # plus
            if key.name == '+':
                if '(' in self.calculation:
                    self.calculation += ' + '
                    self.result = '0'
                else:
                    self.calculation += self.result + ' + '
                    self.result = '0'
            # minus
            if key.name == '-':
                if '(' in self.calculation:
                    self.calculation += ' - '
                    self.result = '0'
                else:
                    self.calculation += self.result + ' - '
                    self.result = '0'
            # multiply
            if key.name == 'x':
                if '(' in self.calculation:
                    self.calculation += ' * '
                    self.result = '0'
                else:
                    self.calculation += self.result + ' * '
                    self.result = '0'
            # divide
            if key.name == '÷':
                if '(' in self.calculation:
                    self.calculation += ' / '
                    self.result = '0'
                else:
                    self.calculation += self.result + ' / '
                    self.result = '0'
            # open | close parenthesis
            if key.name == '(':
                self.result = '(' + self.result
            if key.name == ')':
                self.result += ')'
            # negative | positive
            if key.name == '+/-' and self.result != '0':
                if '-' in self.result:
                    self.result = self.result[1:]
                else:
                    self.result = '-' + self.result
            # factorial
            if key.name == 'n!':
                self.calculation += f'factorial({self.result})'
                self.result = str(eval(self.calculation))
            # sin
            if key.name == 'sin':
                if rad.rad_keep_pressed:
                    self.calculation += f'sin({self.result})'
                elif deg_.deg_keep_pressed:
                    self.calculation += f'sin(radians({self.result}))'
                self.result = str(round(eval(self.calculation), 2))
            # tan
            if key.name == 'tan':
                if rad.rad_keep_pressed:
                    self.calculation += f'tan({self.result})'
                elif deg_.deg_keep_pressed:
                    self.calculation += f'tan(radians({self.result}))'
                self.result = str(round(eval(self.calculation), 2))
            # cos
            if key.name == 'cos':
                if rad.rad_keep_pressed:
                    self.calculation += f'cos({self.result})'
                elif deg_.deg_keep_pressed:
                    self.calculation += f'cos(radians({self.result}))'
                self.result = str(round(eval(self.calculation), 2))
            # sin^-1
            if key.name == 'sin^-1':
                if rad.rad_keep_pressed:
                    self.calculation += f'asin({self.result})'
                elif deg_.deg_keep_pressed:
                    self.calculation += f'degrees(asin({self.result}))'
                self.result = str(round(eval(self.calculation), 2))
            # tan^-1
            if key.name == 'tan^-1':
                if rad.rad_keep_pressed:
                    self.calculation += f'atan({self.result})'
                elif deg_.deg_keep_pressed:
                    self.calculation += f'degrees(atan({self.result}))'
                self.result = str(round(eval(self.calculation), 2))
            # cos^-1
            if key.name == 'cos^-1':
                if rad.rad_keep_pressed:
                    self.calculation += f'acos({self.result})'
                elif deg_.deg_keep_pressed:
                    self.calculation += f'degrees(acos({self.result}))'
                self.result = str(round(eval(self.calculation), 2))
            # sinh
            if key.name == 'sinh':
                self.calculation += f'sinh({self.result})'
                self.result = str(round(eval(self.calculation), 2))
            # cosh
            if key.name == 'cosh':
                self.calculation += f'cosh({self.result})'
                self.result = str(round(eval(self.calculation), 2))
            # tanh
            if key.name == 'tanh':
                self.calculation += f'tanh({self.result})'
                self.result = str(round(eval(self.calculation), 2))
            # sinh^-1
            if key.name == 'sinh^-1':
                self.calculation += f'asinh({self.result})'
                self.result = str(round(eval(self.calculation), 2))
            # cosh^-1
            if key.name == 'cosh^-1':
                self.calculation += f'acosh({self.result})'
                self.result = str(round(eval(self.calculation), 2))
            # tanh^-1
            if key.name == 'tanh^-1':
                self.calculation += f'atanh({self.result})'
                self.result = str(round(eval(self.calculation), 2))
            # ln
            if key.name == 'ln':
                self.calculation += f'log({self.result})'
                self.result = str(round(eval(self.calculation), 2))
            # log
            if key.name == 'log':
                self.calculation += f'log10({self.result})'
                self.result = str(round(eval(self.calculation), 2))
            # deg
            if key.name == 'deg':
                self.calculation += f'radians(degrees({self.result}))'
                self.result = str(round(eval(self.calculation), 2))
            # y root x
            if key.name == 'y√x':
                self.calculation += f'{self.result} ** (1 / '
                self.result = '0'
            # dms
            if key.name == 'dms':
                is_positive = float(self.result) >= 0
                dd = abs(float(self.result))
                minutes, seconds = divmod(dd * 3600, 60)
                degrees0, minutes = divmod(minutes, 60)
                degrees1 = degrees0 if is_positive else -degrees0
                self.calculation = f'dms({self.result})'
                self.result = f'({degrees1}, {minutes}, {round(seconds, 2)})'
            # square root
            if key.name == '√':
                self.calculation += f'sqrt({self.result})'
                self.result = str(eval(self.calculation))
            # 10 **
            if key.name == '10**':
                self.calculation += f'(10**{self.result})'
                if float(self.result) >= 10000:
                    self.result = 'Overflow'
                else:
                    self.result = str(eval(self.calculation))
            # Exp
            if key.name == 'Exp':
                self.calculation = self.result + 'e+'
            # Mod
            if key.name == 'Mod':
                self.calculation += f'fmod({self.result}, '
                self.result = '0'
            # sqr
            if key.name == 'x^2':
                self.calculation += f'({self.result} ** 2)'
                self.result = str(eval(self.calculation))
            # x^y
            if key.name == 'x^y':
                self.calculation += f'{self.result} **'
                self.result = '0'
            # 1/x
            if key.name == '1/x':
                self.calculation = f'1 / {self.result}'
                self.result = str(eval(self.calculation))
            # e^x
            if key.name == 'e^x':
                self.calculation += f'exp({self.result})'
                self.result = str(eval(self.calculation))
            # equals
            if key.name == '=':
                if 'fmod' in self.calculation or ' ** (' in self.calculation:
                    self.calculation += self.result + ')'
                    self.result = str(round(eval(self.calculation), 2))
                else:
                    self.calculation += self.result
                    self.result = str(eval(self.calculation))
                self.calculation = ''
        except ZeroDivisionError:
                self.result = 'Divided by Zero'
        except ValueError:
            self.result = 'Math Error'
        except SyntaxError:
            self.result = 'Syntax Error'

    def show_calculation(self):
        try:
            screen.blit(small_font.render(self.calculation, True, self.grey),
                        (5, 40))
            if len(self.result) <= 12:
                screen.blit(medium_font.render(self.result, True,
                                               self.black), (1, 80))
            else:
                screen.blit(small_font.render(self.result, True,
                                              self.black), (2, 100))
            if not rad.rad_keep_pressed and not deg_.deg_keep_pressed:
                deg_.deg_keep_pressed = True
        except pygame.error:
            self.result = 'Overflow'


class Key:

    def __init__(self, name, xy, bg=None):
        self.name = name
        self.xy = tuple(xy)
        if bg is 'grey':
            self.bg = (240, 240, 240)
        if bg is None:
            self.bg = (255, 255, 255)
        if self.name == 'shift':
            self.shifted = False
        if self.name == 'HYP':
            self.hyp_keep_pressed = False
        if self.name == 'DEG':
            self.deg_keep_pressed = True
        if self.name == 'RAD':
            self.rad_keep_pressed = False
        self.green = (34, 177, 76)
        self.grey = (195, 195, 195)
        self.black = (0, 0, 0)
        self.name_surface, self.name_rect = self.text_object(self.name,
                                                             self.black)
        self.mouse = ()
        self.click = 0
        self.clicked = False
        self.sent = False
        self.time = 0

    def text_object(self, text, color):
        self.name_surface = small_font.render(text, True, color)
        return self.name_surface, self.name_surface.get_rect()

    def text(self):
        self.name_rect.center = (self.xy[0]+80 / 2), (self.xy[1]+40 / 2)
        screen.blit(self.name_surface, self.name_rect)

    def display(self):
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        if self.xy[0]+80 > self.mouse[0] > self.xy[0] and self.xy[1]+40 > self.mouse[1] > self.xy[1]:
            pygame.draw.rect(screen, self.grey, (self.xy[0],
                                                 self.xy[1], 80, 40))
            if self.click[0] == 1:
                pygame.draw.rect(screen, self.green, (self.xy[0],
                                                      self.xy[1], 80, 40))
                self.time += 1
                if not self.sent and self.time >= 9:
                    self.clicked = True
                    self.time = 0
                if self.name is 'shift' and not self.shifted:
                    self.shifted = True
                else:
                    self.shifted = False
                if self.name is 'HYP' and not self.hyp_keep_pressed:
                    self.hyp_keep_pressed = True
                else:
                    self.hyp_keep_pressed = False
                if self.name is 'DEG' and not self.deg_keep_pressed:
                    self.deg_keep_pressed = True
                    rad.rad_keep_pressed = False
                else:
                    self.deg_keep_pressed = False
                if self.name is 'RAD' and not self.rad_keep_pressed:
                    deg_.deg_keep_pressed = False
                    self.rad_keep_pressed = True
                else:
                    self.rad_keep_pressed = False
        else:
            pygame.draw.rect(screen, self.bg, (self.xy[0],
                                               self.xy[1], 80, 40))
        if self.clicked:
            pygame.draw.rect(screen, self.green, (self.xy[0],
                                                  self.xy[1], 80, 40))
            self.clicked = False
            self.sent = False
            brain.receive_input(self)
        if self.name is 'shift' and self.shifted:
            pygame.draw.rect(screen, self.green, (self.xy[0],
                                                  self.xy[1], 80, 40))
        if self.name is 'HYP' and self.hyp_keep_pressed:
            pygame.draw.rect(screen, self.green, (self.xy[0],
                                                  self.xy[1], 80, 40))
        if self.name is 'DEG' and self.deg_keep_pressed:
            pygame.draw.rect(screen, self.green, (self.xy[0],
                                                  self.xy[1], 80, 40))
        if self.name is 'RAD' and self.rad_keep_pressed:
            pygame.draw.rect(screen, self.green, (self.xy[0],
                                                  self.xy[1], 80, 40))
        self.text()


pygame.init()
width = 400
height = 600
screen = pygame.display.set_mode((width, height))
small_font = pygame.font.SysFont('verdana', 18)
medium_font = pygame.font.SysFont('verdana', 50)
icon = pygame.image.load('cal1.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Scientific Calculator')
clock = pygame.time.Clock()

brain = Brain()

open_parenthesis = Key('(', (0, 560), 'grey')
close_parenthesis = Key(')', (80, 560), 'grey')
zero = Key('0', (160, 560), 'grey')
point = Key('.', (240, 560), 'grey')
equals = Key('=', (320, 560), 'grey')

pos_neg = Key('+/-', (0, 520), 'grey')
one = Key('1', (80, 520), 'grey')
two = Key('2', (160, 520), 'grey')
three = Key('3', (240, 520), 'grey')
plus = Key('+', (320, 520), 'grey')

_factorial = Key('n!', (0, 480), 'grey')
four = Key('4', (80, 480), 'grey')
five = Key('5', (160, 480), 'grey')
six = Key('6', (240, 480), 'grey')
minus = Key('-', (320, 480), 'grey')

_pi = Key('π', (0, 440), 'grey')
seven = Key('7', (80, 440), 'grey')
eight = Key('8', (160, 440), 'grey')
nine = Key('9', (240, 440), 'grey')
times = Key('x', (320, 440), 'grey')

shift = Key('shift', (0, 400), 'grey')
ce = Key('CE', (80, 400), 'grey')
c = Key('C', (160, 400), 'grey')
back = Key('<=', (240, 400), 'grey')
divide = Key('÷', (320, 400), 'grey')

square_root = Key('√', (0, 360))
ten_raised = Key('10**', (80, 360))
_log = Key('log', (160, 360))
_exp = Key('Exp', (240, 360))
_mod = Key('Mod', (320, 360))

x_raised_2 = Key('x^2', (0, 320))
x_raised_y = Key('x^y', (80, 320))
_sin = Key('sin', (160, 320))
_cos = Key('cos', (240, 320))
_tan = Key('tan', (320, 320))

one_slash_x = Key('1/x', (0, 360))
e_raised_x = Key('e^x', (80, 360))
_ln = Key('ln', (160, 360))
_dms = Key('dms', (240, 360))
_deg = Key('deg', (320, 360))

x_raised_3 = Key('x^3', (0, 320))
y_sqr_x = Key('y√x', (80, 320))
sin_neg_one = Key('sin^-1', (160, 320))
cos_neg_one = Key('cos^-1', (240, 320))
tan_neg_one = Key('tan^-1', (320, 320))

hyp = Key('HYP', (0, 280))
_sinh = Key('sinh', (160, 320))
_cosh = Key('cosh', (240, 320))
_tanh = Key('tanh', (320, 320))
sinh_neg_one = Key('sinh^-1', (160, 320))
cosh_neg_one = Key('cosh^-1', (240, 320))
tanh_neg_one = Key('tanh^-1', (320, 320))

deg_ = Key('DEG', (80, 280))
rad = Key('RAD', (160, 280))

bars = load_png('bars.png')
about = load_png('about.png')


def calculation_loop():

    x = -400
    show_ = False

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    one.clicked = True
                if event.key == pygame.K_2:
                    two.clicked = True
                if event.key == pygame.K_3:
                    three.clicked = True
                if event.key == pygame.K_4:
                    four.clicked = True
                if event.key == pygame.K_5:
                    five.clicked = True
                if event.key == pygame.K_6:
                    six.clicked = True
                if event.key == pygame.K_7:
                    seven.clicked = True
                if event.key == pygame.K_8:
                    eight.clicked = True
                if event.key == pygame.K_9:
                    nine.clicked = True
                if event.key == pygame.K_0:
                    zero.clicked = True
                if event.key == pygame.K_PERIOD:
                    point.clicked = True
                if event.key == pygame.K_BACKSPACE:
                    back.clicked = True
                if event.key == pygame.K_DELETE:
                    ce.clicked = True
                if event.key == pygame.K_KP_DIVIDE:
                    divide.clicked = True
                if event.key == pygame.K_EQUALS:
                    equals.clicked = True
                if event.key == event.key == pygame.K_RETURN:
                    equals.clicked = True
                if event.key == pygame.K_KP_MINUS:
                    minus.clicked = True
                if event.key == pygame.K_KP_MULTIPLY:
                    times.clicked = True
                if event.key == pygame.K_KP_PLUS:
                    plus.clicked = True

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        screen.fill((255, 255, 255))
        screen.blit(small_font.render('SCIENTIFIC', True,
                                      (0, 0, 0)), (50, 10))
        if 8 + 30 > mouse[0] > 8 and 8 + 30 > mouse[1] > 8:
            if click[0] == 1:
                if x <= -400:
                    show_ = True
                elif x >= 0:
                    show_ = False
        if show_:
            x += 30
            if x >= 0:
                x = 0
        if not show_:
            x -= 25
            if x <= -400:
                x = -400
        open_parenthesis.display()
        close_parenthesis.display()
        zero.display()
        point.display()
        equals.display()
        equals.display()
        pos_neg.display()
        one.display()
        two.display()
        three.display()
        plus.display()
        _factorial.display()
        four.display()
        five.display()
        six.display()
        minus.display()
        _pi.display()
        seven.display()
        eight.display()
        nine.display()
        times.display()
        shift.display()
        ce.display()
        c.display()
        back.display()
        divide.display()
        if not shift.shifted:
            square_root.display()
            ten_raised.display()
            _log.display()
            _exp.display()
            _mod.display()
            x_raised_2.display()
            x_raised_y.display()
            if not hyp.hyp_keep_pressed:
                _sin.display()
                _cos.display()
                _tan.display()
            else:
                _sinh.display()
                _cosh.display()
                _tanh.display()
        if shift.shifted:
            one_slash_x.display()
            e_raised_x.display()
            _ln.display()
            _dms.display()
            _deg.display()
            x_raised_3.display()
            y_sqr_x.display()
            if not hyp.hyp_keep_pressed:
                sin_neg_one.display()
                cos_neg_one.display()
                tan_neg_one.display()
            else:
                sinh_neg_one.display()
                cosh_neg_one.display()
                tanh_neg_one.display()
        hyp.display()
        deg_.display()
        rad.display()
        pygame.draw.rect(screen, (34, 177, 76), (0, 320, 400, 2))
        pygame.draw.rect(screen, (34, 177, 76), (0, 280, 400, 2))
        brain.show_calculation()
        screen.blit(about[0], (x, 0))
        screen.blit(bars[0], (8, 8))

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    calculation_loop()
