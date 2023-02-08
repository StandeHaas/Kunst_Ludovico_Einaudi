import numpy as np 
import matplotlib.pyplot as plt
import scipy as sp
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
from numpy import random
import math
import time
import os
from matplotlib import font_manager as fm, rcParams #https://jonathansoma.com/lede/data-studio/matplotlib/list-all-fonts-available-in-matplotlib-plus-samples/
from IPython.core.display import HTML

fpath = os.path.join(r"C:\Users\Stan\Downloads\Cormorant\static\Cormorant-BoldItalic.ttf")
prop = fm.FontProperties(fname=fpath)


# sorting all phase portraits for a,b,c,d in [-10,10]
spiral_sink = list()
spiral_source = list()
center = list()
degenerate_sink = list()
star_sink = list()
degenerate_source = list()
star_source = list()
sink = list()
source = list()
line_stabble = list()
line_unstabble = list()
saddle = list()
for a in range(-4,4):
    for b in range(-4,4):
        for c in range(-4, 4):
            for d in range(-4,4):
                det = a*d - b*c 
                tr = a + d           
                if det > tr**2/4:
                    if tr < 0:
                        spiral_sink.append([a,b,c,d])
                    elif tr == 0:
                        center.append([a,b,c,d])
                    elif tr > 0:
                        spiral_source.append([a,b,c,d])                  
                elif det == tr**2/4:
                    if tr < 0:
                        if a == d:
                            star_sink.append([a,b,c,d]) 
                        else:
                            degenerate_sink.append([a,b,c,d])  
                    elif tr > 0:
                        if a == d:
                            star_source.append([a,b,c,d]) 
                        else:
                            degenerate_source.append([a,b,c,d])                          
                elif det < tr**2/4:
                    if tr < 0:
                        if det > 0:
                            sink.append([a,b,c,d])  
                        elif det == 0:
                            line_stabble.append([a,b,c,d])  
                        elif det < 0:
                            saddle.append([a,b,c,d])  
                    elif tr > 0:
                        if det > 0:
                            source.append([a,b,c,d])  
                        elif det == 0:
                            line_unstabble.append([a,b,c,d])  
                        elif det < 0:
                            saddle.append([a,b,c,d])  
                    elif tr == 0:
                        if det < 0:
                            saddle.append([a,b,c,d])  

# defining certain color options
def get_color(color_code, gamma, beta):
    if color_code == 'rgo':
        color_code = np.random.choice(['red', 'green', 'yellow','red', 'green', 'yellow', 'purple'])
    if color_code == 'random': 
        r = np.round(np.random.rand(),1)
        g = np.round(np.random.rand(),1)
        b = np.round(np.random.rand(),1)
        return (r,g,b)
    if color_code == 'blue':
        r = np.random.randint(0,4)/10
        g = np.random.randint(0,5)/10
        b = np.random.randint(3,10)/10
        return (r,g,b)
    if color_code == 'red':
        r = np.random.randint(4,10)/10
        g = np.random.randint(0,5)/10
        b = np.random.randint(0,2)/10
        return (r,g,b)
    if color_code == 'green':
        r = np.random.randint(0,4)/10
        g = np.random.randint(4,10)/10
        b = np.random.randint(0,2)/10
        return (r,g,b)
    if color_code == 'purple':
        r = np.random.randint(5,10)/10
        g = np.random.randint(0,4)/10
        b = np.random.randint(2,5)/10
        return (r,g,b)
    if color_code == 'yellow':
        r = np.random.randint(6,10)/10
        g = np.random.randint(7,10)/10
        b = np.random.randint(1,5)/10
        return (r,g,b)
    if color_code == 'orange':
        r = np.random.randint(3,10)/10
        g = np.random.randint(0,4)/10
        b = np.random.randint(3,10)/10
        return (r,g,b)
    if color_code == 'white':
        return str(np.random.randint(6,10)/10)
    if color_code == 'light_grey':
        return str(np.random.randint(2,6)/10)
    if color_code == 'dark_grey':
        return str(np.random.randint(1,5)/10)
    if color_code == 'black':
        return str(np.random.randint(0,3)/10)
    if color_code == 'black_2':
        return str(np.random.randint(0,2)/10)
    if color_code == 'white_1':
        return white_lst[gamma][beta]
    if color_code == 'light_grey_1':
        return light_grey_lst[gamma][beta]
    if color_code == 'light_grey_2':
        return light_grey_lst_2[gamma][beta]

# color_list
white_lst = []
for _ in range (5):
    lst = [str(np.random.randint(2,6)/10) for _ in range (5)]
    white_lst.append(lst)
light_grey_lst = []
for _ in range (5):
    lst = [str(np.random.randint(0,5)/10) for _ in range (5)]
    light_grey_lst.append(lst)
light_grey_lst_2 = []
for _ in range (5):
    lst = [str(0.6) for _ in range (5)]
    light_grey_lst_2.append(lst)
rgo_list_1 = [get_color(np.random.choice(['red', 'green', 'yellow','red', 'green', 'yellow', 'purple']),0,0) for _ in range(100)] 
rgo_list_2 = [get_color(np.random.choice(['red', 'green', 'yellow','red', 'green', 'yellow', 'purple']),0,0) for _ in range(100)] 
rgo_list_3 = [get_color(np.random.choice(['red', 'green', 'yellow','red', 'green', 'yellow', 'purple']),0,0) for _ in range(100)] 
rgo_list_4 = [get_color(np.random.choice(['red', 'green', 'yellow','red', 'green', 'yellow', 'purple']),0,0) for _ in range(100)] 
rgo_list_5 = [get_color(np.random.choice(['red', 'green', 'yellow','red', 'green', 'yellow', 'purple']),0,0) for _ in range(100)] 
# different options for phase portraits
def cd_number(n):
    number = '#' + str(np.random.randint(1, 10**n)) 
    return number

def randomiser(a,b,c,d,e,f,randomise):
    a += randomise*np.random.choice((-1,1))*np.random.rand()
    b += randomise*np.random.choice((-1,1))*np.random.rand()
    c += randomise*np.random.choice((-1,1))*np.random.rand()
    d += randomise*np.random.choice((-1,1))*np.random.rand()
    e += randomise*np.random.choice((-1,1))*np.random.rand()
    f += randomise*np.random.choice((-1,1))*np.random.rand()
    return a,b,c,d,e,f

# displayment system
def DE(system, i=0,e=0,f=0, color_code=random, width = 1, alpha = 1, delta = 1, dt = 0.5, randomise=0, minimize=0, r=0):
    a = system[0]
    b = system[1]
    c = system[2]
    d = system[3]
    sol_ = list()

    n = 0 
    for gamma in range(-i, i+1):
        for beta in range (-i, i+1):
            if color_code == rgo_list_4:
                color = rgo_list_4[n]
                n += 1
            else:       
                color = get_color(color_code, gamma, beta)
            if randomise != 0:
                a,b,c,d,e,f = randomiser(a,b,c,d,e,f, randomise)

            def dSdt(t, S):
                x, y = S
                return [a*x + b*y, 
                       c*x + d*y]

            x0 = delta * gamma
            y0 = delta * beta
            S_0 = (x0, y0)

            t = np.linspace(0, dt, 10000)
            sol = odeint(dSdt, y0=S_0, t=t, tfirst=True)
            x_sol = sol.T[0]
            y_sol = sol.T[1]              
            if minimize != 0:
                x_sol = [_/minimize for _ in x_sol]   
                y_sol = [_/minimize for _ in y_sol]
            
            if r != 0:
                q = 0
                circle(x_sol, y_sol, color, width, alpha,r,e,f,q)
            else:               
                x_sol = [x + e for x in x_sol]
                y_sol = [y + f for y in y_sol]  
                plt.plot(x_sol, y_sol, c=color, linewidth = width, alpha = alpha)
                sol_.append([x_sol,y_sol])
    return sol_, t

def circle(x_sol, y_sol, color, width, alpha,r,e,f,q, _=0, dis =0):
    x_list = []
    y_list = []
    v_2 = [0,0]
    while _ < len(x_sol):
        dis_old = dis
        v_1 = [x_sol[_],y_sol[_]]   
        dis = math.dist(v_1, v_2)
        if dis < r:
            x_list.append(x_sol[_])
            y_list.append(y_sol[_])
        elif dis > r and dis_old < r:
            x_list = [x + e for x in x_list]
            y_list = [y + f for y in y_list]
            plt.plot(x_list, y_list, c=color, linewidth = width, alpha = alpha) 
            q += 1
            if q >= 1:
                _ += 10000000000000
            circle(x_sol, y_sol, color, width, alpha, r,e,f,q, _ + 1, dis)
        _ += 1


random = [np.random.choice([0,0,0,0,0,1,1,1,2,3]) for _ in range(200)]
def system(sys):
    systems = [sys[np.random.randint(0, len(sys))] for _ in range(200)]
    return systems

def DE_on_DE(sol_, t, t_start, t_end, systems, color=0, width=1, alpha=1, delta=1, minimize = 20, r = 5):
    dt = 250
    n = 0 
    for sol in sol_:
        if random[n] != 0:
            t_s = t_start
            while t_s < t_end*len(t):
                DE(systems[n], i=2, e=sol[0][t_s], f = sol[1][t_s], color_code=color, width=width, alpha=alpha, delta=delta, dt = 10, minimize=minimize, r = r)
                t_s += dt
                n += 1
        n += 1

def rotation(system,sol,t_s):
    S = [system[0]*sol[0][t_s] + system[1]*sol[1][t_s], 
         system[2]*sol[0][t_s] + system[3]*sol[1][t_s]]
    if S[0] == 0:
        if S[1] > 0:
            rotation = 90
        else: 
            rotation = -90
    else:
        rotation = np.arctan(S[1]/S[0])*180/np.pi
    return rotation, S

def text_on_DE(sol_, t, t_start, t_end, system, systems, color, width, alpha, delta, minimize, r):
    songs = ['Uno', 'Divenire', 'Monday', 'Andare', 'Rose', 'Primavera', 'Oltremare', 'Fly', 'Ascolta', 'Ritornare', 'Svanire', 'Luce']
    q = 4
    n = 0
    d_t = 250
    c = 0
    for sol in sol_:
        if q > 0:
            q -= 1
            if random[n] != 0:
                t_s = 0
                while t_s < t_end*len(t):
                    DE(systems[n], i=2, e=sol[0][t_s], f = sol[1][t_s], color_code=color, width=width, alpha=alpha, delta=delta, dt = 10, minimize=minimize, r = r)
                    t_s += d_t
                    n += 1
            n += 1
        else:
            q = np.random.choice([4])
            dt = int(0.005*10000)
            t_s = int(t_start*10000)
            if len(songs) > 0:
                txt = songs.pop()
                angle, S = rotation(system, sol, 0)
                if S[0] < 0:
                    txt = txt[::-1]
                n = 0
                for _ in txt:
                    angle, S = rotation(system, sol,t_s)
                    plt.text(sol[0][t_s]-5,sol[1][t_s]-5,_, color=rgo_list_5[c],fontsize=26,fontproperties= prop, fontweight = 950, rotation = angle)
                    dt = int(dt * 1.2)
                    t_s += dt
                    n += 1
                    c += 1

def repeat(reps):
    plt.ion()
    figure,ax = plt.subplots()
    k = 100
    plt.xlim([-k,k])
    plt.ylim([-k,k])
    random_number_1 = np.random.randint(0, len(sink))
    random_number_2 = np.random.randint(0, len(sink))
    random_number_3 = np.random.randint(0, len(sink))
    txt = cd_number(7) 
    systems = system(spiral_source)
    for i in range(reps):
        DE(sink[random_number_1],3, color_code = 'light_grey_2', width = 100, delta = 33, dt = 5, alpha = 1)
        DE(sink[random_number_2],3, color_code = 'white_1', width = 1, delta = 33, dt = 5, alpha = 1)
        DE(sink[random_number_3],2, color_code = 'white_1', width = 1, delta = 33, dt = 5, alpha = 1)
        DE(sink[random_number_1],3, color_code = 'light_grey_1', width = 60, delta = 33, dt = 5, alpha = 0.3)
        DE(sink[random_number_1],3, color_code = 'white_1', width = 2, delta = 33, dt = 5, alpha = 1)
        sol_, t = DE(sink[random_number_1],3, color_code = 'light_grey_1', width = 20, delta = 33, dt = 5, alpha = 0.6)
        DE_on_DE(sol_, t, 0,0.05, systems, color=rgo_list_4, width=2, alpha=0.9, delta=1, minimize=5, r = 0.000000000001 + 0.7*i)
        x_pos = -97
        n = 0
        for _ in 'L u d o v ic o  E in a u d i':
            plt.text(x_pos,80,_, color=rgo_list_2[n],fontsize=28,fontproperties= prop, fontweight = 950)
            x_pos += 4
            n += 1
        x_pos = 63
        n = 0 
        for _ in txt:
            plt.text(x_pos,-94,_, color=rgo_list_3[n],fontsize=19,fontproperties= prop, fontweight = 950)
            x_pos += 4.2
            n += 1
        y_pos = -88
        n = 0 
        for _ in 'Di v e ni r e'[::-1]:
            plt.text(-102,y_pos,_, color=rgo_list_4[n],fontsize=32,fontproperties= prop, fontweight = 950, rotation = -90)
            y_pos += 5.4
            n += 1
        

        plt.axis('off')      
        figure.canvas.draw()
        figure.canvas.flush_events()
        plt.savefig('cd_14 {}'.format(i))

#repeat(20)

def repeat(reps):
    plt.ion()
    figure,ax = plt.subplots()
    k = 100
    plt.xlim([-k,k])
    plt.ylim([-k,k])
    random_number_1 = np.random.randint(0, len(sink))
    random_number_2 = np.random.randint(0, len(sink))
    random_number_3 = np.random.randint(0, len(sink))
    systems = system(spiral_source)
    for i in range(reps):   
        DE(sink[random_number_1],3, color_code = 'light_grey_2', width = 100, delta = 33, dt = 5, alpha = 1)
        DE(sink[random_number_2],3, color_code = 'white_1', width = 1, delta = 33, dt = 5, alpha = 1)
        DE(sink[random_number_3],2, color_code = 'white_1', width = 1, delta = 33, dt = 5, alpha = 1)
        DE(sink[random_number_1],3, color_code = 'light_grey_1', width = 60, delta = 33, dt = 5, alpha = 0.3)
        DE(sink[random_number_1],3, color_code = 'white_1', width = 2, delta = 33, dt = 5, alpha = 1)
        sol_, t = DE(sink[random_number_1],3, color_code = 'light_grey_1', width = 20, delta = 33, dt = 5, alpha = 0.6)

        text_on_DE(sol_, t, 0.005, 0.05, sink[random_number_1], systems, color=rgo_list_4, width=2, alpha=0.9, delta=1, minimize=5, r = 0.000000000001 + 0.7*i)
    

        plt.axis('off')
        figure.canvas.draw()
        figure.canvas.flush_events()
        plt.savefig('cd_back_2 {}'.format(i))
  
repeat(20)
