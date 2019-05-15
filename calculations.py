import numpy as np
import math as m

def positions(angles, lengths): #a1=angle1 and so on
    """This function calculates positions of each points of a robot, based on given angles and lengths"""
    try:
        a=[]
        for angle in angles:
            a.append(float(angle.get_value()))

        l=[]
        for length in lengths:
            l.append(float(length.get_value()))

        if a[0]<-60 or a[0]>60 or a[1]<-30 or a[1]>45 or a[2]<-45 or a[2]>30:
            return 'error'

        coordinates = {} #it has key that is a symbol of a point and its value is stored as list: [x,y]
        coordinates['A'] = [0, l[0]]
        coordinates['B'] = [-round(m.sin(m.radians(a[0]))*l[1], 3), round(0.3+m.cos(m.radians(a[0]))*l[1], 3)]
        coordinates['C'] = [-round(-coordinates['B'][0]+m.sin(m.radians(a[0]+a[1]))*l[2], 3), round(coordinates['B'][1]+m.cos(m.radians(a[0]+a[1]))*l[2], 3)]
        coordinates['D'] = [-round(-coordinates['C'][0]+m.sin(m.radians(sum(a)))*l[3], 3), round(coordinates['C'][1]+m.cos(m.radians(sum(a)))*l[3], 3)]
        return coordinates

    except ValueError:
        return 'error'

def rotations(angles):
    """This function returns a rotations matricies from Denavit-Hattenberg notation based on given angles"""
    try:
        a=[]
        for angle in angles:
            if __name__ == '__main__':
                a.append(float(angle))
            else:
                a.append(float(angle.get_value()))

        if a[0]<-60 or a[0]>60 or a[1]<-30 or a[1]>45 or a[2]<-45 or a[2]>30:
            return 'error'
        alfa, teta = [], []
        for i in range(0, 7): #alfa angles
            if i==1 or i==4:
                alfa.append(m.radians(-90))
            elif i==5:
                alfa.append(m.radians(90))
            else:
                alfa.append(0)

        teta.append(0)                  #teta0
        teta.append(m.radians(a[0]-90)) #teta1
        teta.append(m.radians(a[1]))    #teta2
        teta.append(m.radians(-90))     #teta3
        teta.append(0)                  #teta4
        teta.append(m.radians(a[2]+90)) #teta5
        teta.append(0)                  #teta6

        R = []
        for a, t in zip(alfa, teta):
            rotz = np.matrix([ [round(m.cos(t), 3), round(-m.sin(t), 3), 0],
                               [round(m.sin(t), 3), round(m.cos(t), 3), 0],
                               [0, 0, 1] ])

            rotx = np.matrix([ [1, 0, 0],
                               [0, round(m.cos(a), 3), round(-m.sin(a), 3)],
                               [0, round(m.sin(a), 3), round(m.cos(a), 3)] ])

            R.append((rotx*rotz).transpose())
        return R

    except ValueError:
        return 'error'

def omega_matrix(R, omegas):
    """This function returns a list of matricies of angle velocities"""
    try:
        o=[]
        o.append(0)
        for om in omegas:
            if __name__ == '__main__':
                o.append(float(om))
            else:
                o.append(float(om.get_value()))

        omega = []
        omega.append(np.matrix([ [0],
                                 [0],
                                 [0] ]))       #omega0
        Z = np.matrix([[0],
                       [0],
                       [1] ])

        omega.append((R[0]*omega[0]))           #omega1
        omega.append((R[1]*omega[1]) + (o[1]*Z))#omega2
        omega.append((R[2]*omega[2]) + (o[2]*Z))#omega3
        omega.append((R[3]*omega[3]))           #omega4
        omega.append((R[4]*omega[4]))           #omega5
        omega.append((R[5]*omega[5]) + (o[3]*Z))#omega6
        omega.append((R[6]*omega[6]))           #omega7

        return omega

    except ValueError:
        return 'error-'

def shift(lengths):

    try:
        l = []
        for length in lengths:
            l.append(float(length.get_value()))
        P = []
        P.append(np.matrix([[0],
                            [0],
                            [l[0]] ]))
        P.append(np.matrix([[0],
                            [0],
                            [0] ]))
        P.append(np.matrix([[l[1]],
                            [0],
                            [0] ]))
        P.append(np.matrix([[l[2]*(2.0/3.0)],
                            [0],
                            [0] ]))
        P.append(np.matrix([[0],
                            [l[2]/3.0],
                            [0] ]))
        P.append(np.matrix([[0],
                            [0],
                            [0] ]))
        P.append(np.matrix([[l[3]],
                            [0],
                            [0] ]))
        return P
    except ValueError:
        return 'error'

def velocities(angles, lengths, omega):
    R = rotations(angles)
    o = omega_matrix(R, omega)
    P = shift(lengths)
    if R == 'error' or o == 'error' or P == 'error':
        return 'error'
    P_fixed = []
    o_fixed = []
    for matrix in P:
        P_fixed.append(matrix.reshape(1, 3))
    for matrix in o:
        o_fixed.append(matrix.reshape(1, 3))

    Z = np.matrix([[0],
                   [0],
                   [1] ])
    v=[]
    v.append(np.matrix([[0],
                        [0],
                        [0] ]))
    for i in range(1, 8):
        if i == 5:
            v.append(np.round(R[i-1] * (v[i-1] + np.cross(o_fixed[i-1], P_fixed[i-1]).reshape(3, 1)) + 0.02*Z, 3))
        else:
            v.append(np.round(R[i-1] * (v[i-1] + np.cross(o_fixed[i-1], P_fixed[i-1]).reshape(3,1)), 3))
    return v


if __name__ == '__main__':
    angle = [30, 30, -30]
    omega = [2, -3, 1]
    R = rotations(angle)
    o = omega_matrix(R, omega)
    for i in range(0, 8):
        if i>=1:
            print('Rot:')
            print(R[i-1])
        print('omega')
        print(o[i])
        print('++++++++++++++++++++++')
