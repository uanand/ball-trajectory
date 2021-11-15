import numpy

def defPitchParametersLimit():
    x_lim = [-0.5,0.5]
    y_lim = [18,19]
    z_lim = [1.5,2]
    
    v_x_lim = [-0.1,0.1]
    v_y_lim = [-40,-20]
    v_z_lim = [0,2]
    
    w_lim = [1000,2500]
    theta_lim = [0,180]
    phi_lim = [0,360]
    
    return x_lim,y_lim,z_lim,v_x_lim,v_y_lim,v_z_lim,w_lim,theta_lim,phi_lim

def randomPitchParameters(x_lim,y_lim,z_lim,v_x_lim,v_y_lim,v_z_lim,w_lim,theta_lim,phi_lim):
    x = numpy.random.rand()*(x_lim[1]-x_lim[0]) + x_lim[0]
    y = numpy.random.rand()*(y_lim[1]-y_lim[0]) + y_lim[0]
    z = numpy.random.rand()*(z_lim[1]-z_lim[0]) + z_lim[0]
    
    v_x = numpy.random.rand()*(v_x_lim[1]-v_x_lim[0]) + v_x_lim[0]
    v_y = numpy.random.rand()*(v_y_lim[1]-v_y_lim[0]) + v_y_lim[0]
    v_z = numpy.random.rand()*(v_z_lim[1]-v_z_lim[0]) + v_z_lim[0]
    
    w = numpy.random.rand()*(w_lim[1]-w_lim[0]) + w_lim[0]
    theta = numpy.random.rand()*(theta_lim[1]-theta_lim[0]) + theta_lim[0]
    phi = numpy.random.rand()*(phi_lim[1]-phi_lim[0]) + phi_lim[0]
    
    return x,y,z,v_x,v_y,v_z,w,theta,phi
