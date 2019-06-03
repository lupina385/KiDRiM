import numpy as np
import math as m

def shifts(lengths, sav2): #P
    try:
        if __name__ == '__main__':
            l = lengths
            sav = sav2
        else:
            l = []
            for length in lengths:
                l.append(float(length.get_value()))
            sav = []
            for i in sav2:
                sav.append(float(i.get_value()))
        P = []
        P.append(np.matrix([[0],
                            [0],
                            [l[0]] ])) # O to A [0]
        P.append(np.matrix([[0.0],
                            [0.0],
                            [0.0] ]))
        P.append(np.matrix([[l[1]],
                            [0.0],
                            [0.0] ])) # A to B [2]
        P.append(np.matrix([[l[2]-sav[0]],
                            [0],
                            [0] ]))   # B to S [3]
        P.append(np.matrix([[0],
                            [sav[0]],
                            [0] ]))  # S to C [4]
        P.append(np.matrix([[0.0],
                            [0.0],
                            [0.0] ]))
        P.append(np.matrix([[l[3]],
                            [0],
                            [0] ])) # C to D [6]
        return P

    except ValueError:
        return 'error'

def rotations(angles): #R
    """This function returns a rotations matricies from Denavit-Hattenberg notation based on given angles"""
    try:
        if __name__ == '__main__':
            a = angles
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

def omega_matrix(R, omegas): #o
    """This function returns a list of matricies of angle velocities"""
    try:
        if __name__ == '__main__':
            o = []
            for om in omegas:
                o.append(om)
        else:
            o=[]
            for om in omegas:
                o.append(float(om.get_value()))
        o[1] = -o[1]
        Z = np.matrix([[0],
                       [0],
                       [1] ])
        omega = []
        omega.append(np.matrix([ [0],
                                 [0],
                                 [0] ]))       #omega0
        omega.append((R[0]*omega[0]))           #omega1
        omega.append((R[1]*omega[1]) + (o[0]*Z))#omega2
        omega.append((R[2]*omega[2]) + (o[1]*Z))#omega3
        omega.append((R[3]*omega[3]))           #omega4
        omega.append((R[4]*omega[4]))           #omega5
        omega.append((R[5]*omega[5]) + (o[2]*Z))#omega6
        omega.append((R[6]*omega[6]))           #omega7

        return omega

    except ValueError:
        return 'error'

def epsilon_matrix(R, o_m, epsilons, o_v): #e
    try:
        if __name__ == '__main__':
            e = []
            o_values = []
            for eps in epsilons:
                e.append(eps)
            for o in omegas:
                o_values.append(o)
        else:
            e = []
            o_values = []
            for eps in epsilons:
                e.append(float(eps.get_value()))
            for o in o_v:
                o_values.append(float(o.get_value()))
        e[0] = -e[0]
        o_values[2] = -o_values[2]
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

def tensors_of_inertia(lengths, sav2): #toi
    try:
        if __name__ == '__main__':
            l = lengths
            sav = sav2
        else:
            l = []
            for length in lengths:
                l.append(float(length.get_value()))
            sav = []
            for i in sav2:
                sav.append(float(i.get_value()))
        I = []
        I.append(np.matrix([ [m.pow(l[0], 3)/12, 0, 0],
                             [0, m.pow(l[0], 3)/12, 0],
                             [0, 0, 0] ]))
        I.append(np.matrix([ [0, 0, 0],
                             [0, m.pow(l[1], 3)/12, 0],
                             [0, 0, m.pow(l[1], 3)/12] ]))
        I.append(np.matrix([ [0, 0, 0],
                             [0, m.pow(l[2]-sav[0], 3)/12, 0],
                             [0, 0, m.pow(l[2]-sav[0], 3)/12] ]))
        I.append(np.matrix([ [0, 0, 0],
                             [0, m.pow(sav[0], 3)/12, 0],
                             [0, 0, m.pow(sav[0], 3)/12] ]))
        I.append(np.matrix([ [0, 0, 0],
                             [0, m.pow(l[3], 3)/12, 0],
                             [0, 0, m.pow(l[3], 3)/12] ]))

        return I
    except ValueError:
        return 'error'

#Functions above are only for functions below to be able to calculate certain values
#They are not for displaying any informations for user
#Everything below is later outputted onto the screen

def positions(angles, lengths):
    """This function calculates positions of each points of a robot, based on given angles and lengths"""
    try:
        if __name__ == '__main__':
            a = angles
            l = lengths
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

def velocities(angles, lengths, omegas, sav2): #v
    """This functions calculates vectors of velocities of the points of the robot"""
    if __name__ == '__main__':
        a = angles
        o = omegas
        l = lengths
        R = rotations(a)
        o = omega_matrix(R, o)
        P = shifts(l, sav2)
        v2 = sav2[1]
    else:
        R = rotations(angles)
        o = omega_matrix(R, omegas)
        P = shifts(lengths, sav2)
        v2 = float(sav2[1].get_value())
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
            v.append(np.round(R[i-1] * (v[i-1] + np.cross(o_fixed[i-1], P_fixed[i-1]).reshape(3, 1)) + v2*Z, 3))
        else:
            v.append(np.round(R[i-1] * (v[i-1] + np.cross(o_fixed[i-1], P_fixed[i-1]).reshape(3,1)), 3))
    return v

def accelerations(angles, lengths, omegas, epsilons, sav2): #a
    """This functions calculates vectors of accelerations of the points of the robot"""
    if __name__=='__main__':
        v2 = sav2[1]
        a2 = sav2[2]
    else:
        try:
            v2 = float(sav2[1].get_value())
            a2 = float(sav2[2].get_value())
        except ValueError:
            return 'error'
    R = rotations(angles)
    o = omega_matrix(R, omegas)
    e = epsilon_matrix(R, o, epsilons, omegas)
    P = shifts(lengths, sav2)
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
    v2_Z_fixed = (v2*Z).reshape(1, 3)
    for omega in o:
        o_fixed.append(omega.reshape(1, 3))
    for shift in P:
        P_fixed.append(shift.reshape(1, 3))
    for epsilon in e:
        e_fixed.append(epsilon.reshape(1, 3))
    for i in range(1, 8):
        if i == 5:
            a.append(np.round(R[i-1]*(a[i-1] + np.cross(o_fixed[i-1], np.cross(o_fixed[i-1], P_fixed[i-1])).reshape(3, 1) + np.cross(e_fixed[i-1], P_fixed[i-1]).reshape(3, 1))
                    + (np.cross(2*o_fixed[i-1], v2_Z_fixed).reshape(3, 1) + a2*Z), 3))
        else:
            a.append(np.round(R[i-1] * (a[i-1] + np.cross(o_fixed[i-1], np.cross(o_fixed[i-1], P_fixed[i-1])).reshape(3, 1) + np.cross(e_fixed[i-1], P_fixed[i-1]).reshape(3, 1)), 3))
    return a

def accelerations_centre_mass(angles, lengths, omegas, epsilons, sav2): #acm
    """This functions calculates vectors of accelerations of the centre of masses of arms of the robot"""
    #^I do not speak london very much
    R = rotations(angles)
    P = shifts(lengths, sav2)
    o = omega_matrix(R, omegas)
    e = epsilon_matrix(R, o, epsilons, omegas)
    a = accelerations(angles, lengths, omegas, epsilons, sav2)
    o_fixed = []
    P_fixed = []
    e_fixed = []
    for omega in o:
        o_fixed.append(omega.reshape(1, 3))
    for shift in P:
        P_fixed.append(shift.reshape(1, 3))
    for epsilon in e:
        e_fixed.append(epsilon.reshape(1, 3))
    acm = []
    acm.append(np.round((a[0] + np.cross(o_fixed[0], np.cross(o_fixed[0], 0.5*P_fixed[0])).reshape(3, 1) + np.cross(e_fixed[0], 0.5*P_fixed[0]).reshape(3, 1)), 3))        #a01
    acm.append(np.round((a[2] + np.cross(o_fixed[2], np.cross(o_fixed[2], 0.5*P_fixed[2])).reshape(3, 1) + np.cross(e_fixed[2], 0.5*P_fixed[2]).reshape(3, 1)), 3))        #a23
    acm.append(np.round((a[3] + np.cross(o_fixed[3], np.cross(o_fixed[3], 0.5*P_fixed[3])).reshape(3, 1) + np.cross(e_fixed[3], 0.5*P_fixed[3]).reshape(3, 1)), 3))        #a34
    acm.append(np.round(R[4]*(a[4] + np.cross(o_fixed[4], np.cross(o_fixed[4], 0.5*P_fixed[4])).reshape(3, 1) + np.cross(e_fixed[4], 0.5*P_fixed[4]).reshape(3, 1)), 3))             #a45
    acm.append(np.round((a[6] + np.cross(o_fixed[6], np.cross(o_fixed[6], 0.5*P_fixed[6])).reshape(3, 1) + np.cross(e_fixed[6], 0.5*P_fixed[6]).reshape(3, 1)), 3))        #a67
    return acm

def fictitious_forces(lengths, angles, omegas, epsilons, sav2): #F
    """This functions calculates verticies of fictitious forces"""
    acm = accelerations_centre_mass(angles, lengths, omegas, epsilons, sav2)
    if __name__ == '__main__':
        l = lengths
        sav = sav2
    else:
        l = []
        for length in lengths:
            l.append(float(length.get_value()))
        sav = []
        for i in sav2:
            sav.append(float(i.get_value()))
    F = []
    F.append(np.round(l[0]*acm[0], 3))
    F.append(np.round(l[1]*acm[1], 3))
    F.append(np.round((l[2]-sav[0])*acm[2], 3))
    F.append(np.round(sav[0]*acm[3], 3))
    F.append(np.round(l[3]*acm[4], 3))
    return F

def torques(lengths, angles, omegas, epsilons, sav2): #N
    """This functions calcules verticies of torques"""
    R = rotations(angles)
    o = omega_matrix(R, omegas)
    e = epsilon_matrix(R, o, epsilons, omegas)
    toi = tensors_of_inertia(lengths, sav2)
    toi_o_fixed = []
    o_fixed = []
    for j in range(0, 5):
        if j == 0:
            toi_o_fixed.append((toi[j]*o[j+1]).reshape(1, 3))
        elif j == 4:
            toi_o_fixed.append((toi[j]*o[j+3]).reshape(1, 3))
        else:
            toi_o_fixed.append((toi[j]*o[j+2]).reshape(1, 3))
    for matrix in o:
        o_fixed.append(matrix.reshape(1, 3))
    N = []
    N.append(toi[0]*e[1] + np.cross(o_fixed[1], toi_o_fixed[0]).reshape(3, 1)) # N01
    N.append(toi[1]*e[3] + np.cross(o_fixed[3], toi_o_fixed[1]).reshape(3, 1)) # N23
    N.append(toi[2]*e[4] + np.cross(o_fixed[4], toi_o_fixed[2]).reshape(3, 1)) # N34
    N.append(toi[3]*e[5] + np.cross(o_fixed[5], toi_o_fixed[3]).reshape(3, 1)) # N45
    N.append(toi[4]*e[7] + np.cross(o_fixed[7], toi_o_fixed[4]).reshape(3, 1)) # N67
    return N

def forces_of_interactions(lengths, angles, omegas, epsilons, sav2): #f
    """This functions calculates verticies of interaction forces"""
    F = fictitious_forces(lengths, angles, omegas, epsilons, sav2)
    R = rotations(angles)
    #Making F list have 7 elements:
    F_help = F[4]
    F[4] = F[3]
    F[3] = F[2]
    F[2] = F[1]
    F[1] = np.matrix([ [0],
                       [0],
                       [0] ])
    F.append(np.matrix([ [0],
                         [0],
                         [0] ]))
    F.append(F_help)
    f = []
    f.append(np.matrix([ [0],
                         [0],
                         [0] ]))
    for i, j in zip(reversed(range(0, 7)), range(0,7)):
        if i == 4:
            f.append((R[i].transpose()*f[j]) + (R[i].transpose()*F[i]))
        else:
            f.append((R[i].transpose()*f[j]) + F[i])
    return f[::-1]

def driving_forces(lengths, angles, omegas, epsilons, sav2): #df
    """This functions calculates values of driving forces"""
    f = forces_of_interactions(lengths, angles, omegas, epsilons, sav2)
    Z = np.matrix([ [0.0],
                    [0.0],
                    [1.0] ])
    df = []
    for forces in f:
        df.append(float(forces.transpose()*Z))
    return df

def moments_of_impact(lengths, angles, omegas, epsilons, sav2): #n
    """This functions calculates vectors of moments of impact"""
    R = rotations(angles)
    N = torques(lengths, angles, omegas, epsilons, sav2)
    P = shifts(lengths, sav2)
    F = fictitious_forces(lengths, angles, omegas, epsilons, sav2)
    f = forces_of_interactions(lengths, angles, omegas, epsilons, sav2)
    for i in range(0, 7):
        R[i] = R[i].transpose()
    #Making F list have 7 elements:
    F_help = F[4]
    F[4] = F[3]
    F[3] = F[2]
    F[2] = F[1]
    F[1] = np.matrix([ [0],
                       [0],
                       [0] ])
    F.append(np.matrix([ [0],
                         [0],
                         [0] ]))
    F.append(F_help)
    #Making N list have 7 elements:
    N_help = N[4]
    N[4] = N[3]
    N[3] = N[2]
    N[2] = N[1]
    N[1] = np.matrix([ [0],
                       [0],
                       [0] ])
    N.append(np.matrix([ [0],
                         [0],
                         [0] ]))
    N.append(N_help)
    P_fixed = []
    for shift in P:
        P_fixed.append(shift.reshape(1, 3))
    R_f_fixed = []
    for i, j in zip(range(0, 7), range(1, 8)):
        R_f_fixed.append((R[i]*f[j]).reshape(1, 3))
    F_fixed = []
    for force in F:
        F_fixed.append(force.reshape(1, 3))
    n = []
    n.append(np.matrix([ [0],
                         [0],
                         [0] ]))
    for i, j in zip(reversed(range(0, 7)), range(0, 7)):
        if j == 2:
            n.append(R[i]*N[i] + R[i]*n[j] + np.cross(0.5*P_fixed[i], (R[i]*F[i]).reshape(1, 3)).reshape(3, 1) + np.cross(P_fixed[i], R_f_fixed[i]).reshape(3, 1))
        else:
            n.append(N[i] + R[i]*n[j] + np.cross(0.5*P_fixed[i], F_fixed[i]).reshape(3, 1) + np.cross(P_fixed[i], R_f_fixed[i]).reshape(3, 1))
    return n[::-1]

def driving_moments(lengths, angles, omegas, epsilons, sav2): #dm
    """This functions calculates values of driving moments"""
    n = moments_of_impact(lengths, angles, omegas, epsilons, sav2)
    Z = np.matrix([ [0.0],
                    [0.0],
                    [1.0] ])
    dm = []
    for moments in n:
        dm.append(float(moments.transpose()*Z))
    return dm

if __name__ == '__main__':
    angles = [60.0, 45.0, -45.0]
    lengths = [0.3, 0.2, 0.15, 0.15]
    omegas = [2.0, 3.0, 1.0]
    epsilons = [1.0, 1.5, 2.5]
    sav2 = [0.05, 0.02, 0.02]

    a = accelerations(angles, lengths, omegas, epsilons, sav2)
    for i, acc in enumerate(a, 0):
        print(i, acc)

    # acm = accelerations_centre_mass(angles, lengths, omegas, epsilons, sav2)
    # for i, acc in enumerate(acm, 0):
    #     print(i, acc)
