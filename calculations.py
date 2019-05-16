import numpy as np
import math as m

if __name__ == '__main__':
    angles, lengths, omega, epsilon = 0, 0, 0, 0

def shifts(lengths):
    try:
        if __name__ == '__main__':
            l = [0.3, 0.2, 0.15, 0.15]
        else:
            l = []
            for length in lengths:
                l.append(float(length.get_value()))
        P = []
        P.append(np.matrix([[0],
                            [0],
                            [l[0]] ]))
        P.append(np.matrix([[0.0],
                            [0.0],
                            [0.0] ]))
        P.append(np.matrix([[l[1]],
                            [0.0],
                            [0.0] ]))
        P.append(np.matrix([[l[2]*(2.0/3.0)],
                            [0],
                            [0] ]))
        P.append(np.matrix([[0],
                            [l[2]/3.0],
                            [0] ]))
        P.append(np.matrix([[0.0],
                            [0.0],
                            [0.0] ]))
        P.append(np.matrix([[l[3]],
                            [0],
                            [0] ]))
        return P

    except ValueError:
        return 'error'

def rotations(angles):
    """This function returns a rotations matricies from Denavit-Hattenberg notation based on given angles"""
    try:
        if __name__ == '__main__':
            a = [30.0, 30.0, -30.0]
        else:
            a=[]
            for angle in angles:
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
        if __name__ == '__main__':
            o = [0.0, 2.0, -3.0, 1.0]
        else:
            o=[]
            o.append(0)
            for om in omegas:
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
        return 'error'

def epsilon_matrix(R, o_m, epsilons, o_v):
    try:
        if __name__ == '__main__':
            e = [-1.0, 1.5, 2.5]
            o_values = [0.0, 2.0, -3.0, 1.0]
        else:
            e = []
            o_values = []
            for eps in epsilons:
                e.append(float(eps.get_value()))
            for o in o_v:
                o_values.append(float(o.get_value()))
        R_om_fixed = []
        ov_Z_fixed = []
        Z = np.matrix([ [0],
                        [0],
                        [1] ])
        for i in range(1, 7):
            R_om_fixed.append((R[i-1]*o_m[i-1]).reshape(1, 3))
        for o in o_values:
            ov_Z_fixed.append((o*Z).reshape(1, 3))
        epsilon = []
        epsilon.append(np.matrix([ [0],
                                   [0],
                                   [0] ]))
        epsilon.append(R[0]*epsilon[0])
        epsilon.append((R[1]*epsilon[1]) + (np.cross(R_om_fixed[1], ov_Z_fixed[0]).reshape(3, 1) + (Z*e[0])))
        epsilon.append((R[2]*epsilon[2]) + (np.cross(R_om_fixed[2], ov_Z_fixed[1]).reshape(3, 1) + (Z*e[1])))
        epsilon.append(R[3]*epsilon[3])
        epsilon.append(R[4]*epsilon[4])
        epsilon.append((R[5]*epsilon[5]) + (np.cross(R_om_fixed[5], ov_Z_fixed[2]).reshape(3, 1) + Z*e[2]))
        epsilon.append(R[6]*epsilon[6])

        return epsilon

    except ValueError:
        return 'error'

def positions(angles, lengths):
    """This function calculates positions of each points of a robot, based on given angles and lengths"""
    try:
        if __name__ == '__main__':
            a = [30.0, 30.0, -30.0]
            l = [0.3, 0.2, 0.15, 0.15]
        else:
            a = []
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

def velocities(angles, lengths, omega):
    d4 = 0.02
    if __name__ == '__main__':
        a = [30.0, 30.0, -30.0]
        o = [0.0, 2.0, -3.0, 1.0]
        l = [0.3, 0.2, 0.15, 0.15]
        R = rotations(a)
        o = omega_matrix(R, o)
        P = shifts(l)
    else:
        R = rotations(angles)
        o = omega_matrix(R, omega)
        P = shifts(lengths)
    if R == 'error' or o == 'error' or P == 'error':
        return 'error'
    P_fixed = []
    o_fixed = []
    for matrix in P:
        P_fixed.append(matrix.reshape(1, 3))
    for matrix in o:
        o_fixed.append(matrix.reshape(1, 3))

    Z = np.matrix([[0.0],
                   [0.0],
                   [1.0] ])
    v=[]
    v.append(np.matrix([[0.0],
                        [0.0],
                        [0.0] ]))
    for i in range(1, 8):
        if i == 5:
            v.append(np.round(R[i-1] * (v[i-1] + np.cross(o_fixed[i-1], P_fixed[i-1]).reshape(3, 1)) + d4*Z, 3))
        else:
            v.append(np.round(R[i-1] * (v[i-1] + np.cross(o_fixed[i-1], P_fixed[i-1]).reshape(3,1)), 3))
    return v

def accelerations(angles, lengths, omega, epsilon):
    d4 = 0.02
    e4 = 0.02
    R = rotations(angles)
    o = omega_matrix(R, omega)
    e = epsilon_matrix(R, o, epsilon, omega)
    P = shifts(lengths)
    a = []
    a.append(np.matrix([ [0.0],
                         [0.0],
                         [9.81] ]))
    Z = np.matrix([[0.0],
                   [0.0],
                   [1.0] ])
    o_fixed = []
    P_fixed = []
    e_fixed = []
    d4_Z_fixed = (d4*Z).reshape(1, 3)
    for omega in o:
        o_fixed.append(omega.reshape(1, 3))
    for shift in P:
        P_fixed.append(shift.reshape(1, 3))
    for epsilon in e:
        e_fixed.append(epsilon.reshape(1, 3))

    for i in range(1, 8):
        if i == 5:
            a.append(np.round(R[i-1]*(a[i-1] + np.cross(o_fixed[i-1], np.cross(o_fixed[i-1], P_fixed[i-1])).reshape(3, 1) + np.cross(e_fixed[i-1], P_fixed[i-1]).reshape(3, 1))
                    + (np.cross(2*o_fixed[i-1], d4_Z_fixed).reshape(3, 1) + e4*Z), 3))
        else:
            a.append(np.round(R[i-1] * (a[i-1] + np.cross(o_fixed[i-1], np.cross(o_fixed[i-1], P_fixed[i-1])).reshape(3, 1) + np.cross(e_fixed[i-1], P_fixed[i-1]).reshape(3, 1)), 3))


    return a

if __name__ == '__main__':
    print(accelerations(angles, lengths, omega, epsilon))
    print('============= V: ============')
    print(velocities(angles, lengths, omega))
