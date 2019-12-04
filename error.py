
from manimlib.imports import *
import os
import pyclbr
from math import cos, sin, pi
from random import randrange

class Graphing(GraphScene):
    CONFIG = {
        "x_min": -1,
        "x_max": 5,
        "y_min": -1,
        "y_max": 5,
        "graph_origin": ORIGIN,
        "function_color": WHITE,
        "axes_color": BLUE,
        "graph_origin": 2 * DOWN + 0.5 * LEFT,
    }

    def construct(self):
        #Make graph
        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func_to_graph,self.function_color)
        graph_lab = TextMobject("$\\hat y = \\theta_0 + \\theta_1 * x $")
        graph_lab.next_to(func_graph, DOWN)

        func_graph_2=self.get_graph(self.func_to_graph_2,self.function_color)
        graph_lab_2 = self.get_graph_label(func_graph_2, label = "x^{3}")

        vert_line = self.get_vertical_line_to_graph(1,func_graph,color=YELLOW)

        x = self.coords_to_point(1, self.func_to_graph(1))
        y = self.coords_to_point(0, self.func_to_graph(1))
        horz_line = Line(x,y, color=YELLOW)

        points = []

        xs = [1  ,2  ,3  ,4  ]
        ys = [0.3,2.5,3.4,3]

        for i in range(len(ys)):
            points.append(Dot(self.coords_to_point((xs[i]),(ys[i]))))


        dots = VGroup(*points)
        self.play(FadeIn(dots))
        first_line = TextMobject("Que es un error $J( \\theta_{0} , \\theta_{1} )$?").scale(0.8)
        second_line = TextMobject("Con la regresion, lo que queremos").scale(0.8) 
        third_line = TextMobject("es adivinar (predecir) Y").scale(0.8)
        first_line.next_to(func_graph, LEFT)
        first_line.shift(3*UP)
        second_line.next_to(func_graph, LEFT)
        second_line.shift(3*UP)
        second_line.shift(1*RIGHT)
        third_line.next_to(second_line, DOWN)
        self.play(Write(first_line))
        self.wait(2)
        self.play(FadeOut(first_line), Write(second_line), Write(third_line))



        fourth_line = TextMobject("Entonces, el error").scale(0.8)
        fifth_line = TextMobject("es la diferencia entre").scale(0.8)
        sixth_line = TextMobject("la recta ($\\hat y$), y el punto ($y$)").scale(0.8)

        fourth_line.next_to(func_graph, LEFT)
        fourth_line.shift(3*UP)
        fifth_line.next_to(fourth_line, DOWN)
        sixth_line.next_to(fifth_line, DOWN)

        self.wait(1)

        self.play(ShowCreation(func_graph), Write(graph_lab))

        self.wait(1)
        self.play(FadeOut(second_line),FadeOut(third_line),Write(fourth_line),Write(fifth_line),Write(sixth_line))
        self.wait(2)
        self.play(FadeOut(fourth_line),FadeOut(fifth_line),FadeOut(sixth_line))
        sline = TextMobject("error", color = RED)
        line8 = TextMobject("$= (\\hat y - y)$")
        sline.next_to(func_graph, 9*LEFT)
        sline.shift(3*UP)
        line8.next_to(sline, RIGHT)
        x1 = (-0.5+xs[0])*2
        y1 = -2+ys[0]
        
        x2 = (-0.5+xs[1])*1.67
        y2 = -2+ys[1]

        x3 = (-0.5+xs[2])*1.60
        y3 = -2+ys[2]

        x4 = (-0.5+xs[3])*1.57
        y4 = -2+ys[3]


        line1=Line(np.array([x1,y1,0]),np.array([x1,-2+self.func_to_graph(xs[0]),0]), color = RED)
        line2=Line(np.array([x2, y2,0]),np.array([x2,-2+self.func_to_graph(xs[1]),0]), color = RED)
        line3=Line(np.array([x3,y3,0]),np.array([x3,-2+self.func_to_graph(xs[2]),0]), color = RED)
        line4=Line(np.array([x4,y4,0]),np.array([(-0.5+xs[3])*1.57,-2+self.func_to_graph(xs[3]),0]), color = RED)
        

        h1 = abs(y1-self.func_to_graph(xs[0]))-2
        h2 =abs(y2-self.func_to_graph(xs[1]))-2
        h3 =abs(y3-self.func_to_graph(xs[2]))-2
        h4 =abs(y4-self.func_to_graph(xs[3]))-2


        square1 = Rectangle(height=h1, width=h1, color=RED, fill_color = RED,fill_opacity=1)
        square1.next_to(line1,RIGHT)
        square1.shift(LEFT)

        square2 = Rectangle(height=h2, width=h2, color=RED, fill_color = RED,fill_opacity=1)
        square2.next_to(line2,RIGHT)
        square2.shift(LEFT*0.80)

        square3 = Rectangle(height=h3, width=h3, color=RED, fill_color = RED,fill_opacity=1)
        square3.next_to(line3,RIGHT)
        square3.shift(LEFT*0.70)

        square4 = Rectangle(height=h4, width=h4, color=RED, fill_color = RED,fill_opacity=1)
        square4.next_to(line4,RIGHT)
        square4.shift(LEFT*1.25)
        error_cuadrado = TextMobject("error cuadrado", color =RED)
        line9 = TextMobject("$= (\\hat y - y)^2$")
        error_cuadrado.next_to(func_graph, 7*LEFT)
        error_cuadrado.shift(3*UP)
        line9.next_to(error_cuadrado, RIGHT)

        self.play(Write(sline),Write(line8), FadeIn(line1),FadeIn(line2),FadeIn(line3),FadeIn(line4))
        self.wait(2)
        self.play(Transform(line8,line9),Transform(sline,error_cuadrado),Transform(line1, square1),Transform(line2, square2),Transform(line3, square3),Transform(line4, square4))
        self.wait(2)



        suma_error_cuadrado1 = TextMobject("suma del ", color =RED)
        suma_error_cuadrado1.shift(LEFT)
        suma_error_cuadrado2 = TextMobject("error cuadrado", color =RED)
        line10 = TextMobject("$= \\sum {(\\hat y - y)^2}$")
        suma_error_cuadrado1.next_to(func_graph, 7*LEFT)
        suma_error_cuadrado1.shift(3*UP)
        line10.next_to(suma_error_cuadrado1, RIGHT)
        suma_error_cuadrado2.next_to(suma_error_cuadrado1, DOWN)


        square01 = Rectangle(height=h1, width=h1, color=RED, fill_color = RED,fill_opacity=1)
        square01.next_to(line10,DOWN*4)
        square01.shift(LEFT*4)
        plus1 = TextMobject("$+$")
        plus1.next_to(square01, RIGHT)


        square02 = Rectangle(height=h2, width=h2, color=RED, fill_color = RED,fill_opacity=1)
        square02.next_to(plus1,RIGHT)

        plus2 = TextMobject("$+$")
        plus2.next_to(square02, RIGHT)


        square03 = Rectangle(height=h3, width=h3, color=RED, fill_color = RED,fill_opacity=1)
        square03.next_to(plus2,RIGHT)

        plus3 = TextMobject("$+$")
        plus3.next_to(square03, RIGHT)


        square04 = Rectangle(height=h4, width=h4, color=RED, fill_color = RED,fill_opacity=1)
        square04.next_to(plus3,RIGHT)

        self.wait(2)

        #square02 = Rectangle(height=h2, width=h2, color=RED, fill_color = RED,fill_opacity=1)
        #square02.next_to(square01,RIGHT)
        suma_error_cuadrado1.shift(LEFT)
        suma_error_cuadrado2.shift(LEFT*0.5)
        line10.shift(LEFT)

        self.play(Transform(square1, square01),Transform(square2, square02),Transform(square3, square03),Transform(square4, square04))
        self.play(FadeOut(line8),FadeOut(sline),FadeOut(line9),FadeOut(error_cuadrado), FadeOut(line1),FadeOut(line2),FadeOut(line3),FadeOut(line4))
        
        
        self.wait(1)
        self.play(Write(suma_error_cuadrado1),Write(suma_error_cuadrado2), Write(line10))
        self.play(Write(plus1),Write(plus2),Write(plus3))
        self.wait(3)

        h5 = np.sqrt(np.float_power(h1,2)+np.float_power(h2,2)+np.float_power(h3,2)+np.float_power(h4,2))
        print(h5)
        square05 = Rectangle(height=h5, width=h5, color=RED, fill_color = RED,fill_opacity=1)
        square05.next_to(line10, DOWN*5)
        square05.shift(LEFT*3)

        self.play(FadeOut(plus1),FadeOut(plus2),FadeOut(plus3),FadeOut(square1),FadeOut(square2),FadeOut(square3),FadeOut(square4),FadeOut(square01),FadeOut(square02),FadeOut(square03),FadeOut(square04))
        self.play(FadeIn(square05))
        self.wait(3)

        promedio = TextMobject("Promedio de la", color = RED)
        promedio.next_to(suma_error_cuadrado1, UP)
        promedio.shift(RIGHT*0.5)
        line11 = TextMobject("$=\\frac{\\sum {(\\hat y - y)^2}}{m}$")
        line11.next_to(suma_error_cuadrado1, RIGHT*2).scale(1.1)
        jota = TextMobject("$J( \\theta_{0} , \\theta_{1} )$", color = RED)
        jota.next_to(func_graph, 10*LEFT)
        jota.shift(3*UP)
        square06 = Rectangle(height=h5, width=h5, color=RED, fill_color = RED,fill_opacity=1).scale(0.25)
        square06.next_to(line11, DOWN*5)
        square06.shift(LEFT*3)
        self.play(FadeOut(line10))
        self.play(Write(promedio),Write(line11), Transform(square05,square06))
        self.wait(4)
        self.play(FadeOut(suma_error_cuadrado1),FadeOut(suma_error_cuadrado2),FadeOut(line11),FadeOut(promedio))
        

        line11.next_to(jota, RIGHT)
        self.play(Write(jota), Write(line11))

        self.wait(5)


    def func_to_graph(self, x):
        return (0.98939*x+0.02727)

    def func_to_graph_2(self, x):
        return(x**3)