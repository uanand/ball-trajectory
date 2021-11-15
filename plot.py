import matplotlib.pyplot as plt
plt.style.use('uanand')


def plotTrajectory(t,x,y,z):
    fig = plt.figure(figsize=(8,3))
    
    ax1 = fig.add_subplot(131)
    ax2 = fig.add_subplot(132)
    ax3 = fig.add_subplot(133)
    
    ax1.plot(t,x)
    ax1.set_xlabel('t (s)')
    ax1.set_ylabel('x (m)')
    
    ax2.plot(t,y)
    ax2.set_xlabel('t (s)')
    ax2.set_ylabel('y (m)')
    
    ax3.plot(t,z)
    ax3.set_xlabel('t (s)')
    ax3.set_ylabel('z (m)')
    
    plt.show()

