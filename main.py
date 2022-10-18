############################################################
# LITERATURE USED
# Impact of the Drag Force and the Magnus Effect on the Trajectory of a Baseball
# DOI - 10.4236/wjm.2015.54006
############################################################

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.art3d as art3d
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Circle
plt.style.use('uanand')

import trajectory
import utils
import plot

def inch2m(x):
    return x*0.0254;

############################################################
# PITCH PARAMETERS (SI SYSTEM)
# RIGHT HANDED COORDINATE SYSTEM
# ORIGIN IS AT THE TIP OF HOME PLATE
# X-AXIS IS TOWARDS THE LEFT OF HOME PLATE
# Y-AXIS IS FROM THE HOME PLATE TO THE PITCHER
# Z-AXIS IS VERTICALLY UP
totalTime = 1
fps = 220
numPitches = 1000
probHit = 0.8

for i in range(1000):
    x_lim,y_lim,z_lim,v_x_lim,v_y_lim,v_z_lim,w_lim,theta_lim,phi_lim = utils.defPitchParametersLimit()
    x,y,z,v_x,v_y,v_z,w,theta,phi = utils.randomPitchParameters(x_lim,y_lim,z_lim,v_x_lim,v_y_lim,v_z_lim,w_lim,theta_lim,phi_lim)
    pitch = trajectory.pitch(x,y,z,v_x,v_y,v_z,w,theta,phi,totalTime,fps,mode='gravity+drag+magnus')
    
    if (pitch.status=='strike'):
        if (numpy.random.rand()<=0.8):
            pitch_hit = trajectory.pitch_hit(x,y,z,v_x,v_y,v_z,w,theta,phi,totalTime,fps,mode='gravity+drag+magnus')
        
        
        
        
    # plot.plotTrajectory(throw.time,throw.x,throw.y,throw.z)
# x = 0
# y = 18.4
# z = 1
# v_x = 0
# v_y = -35
# v_z = 2

# w = 1800
# theta = 0
# phi = 270

# hitting = True
# THETA AND PHI CORRESPOND TO THE CONVENTIONAL SPHERICAL COORDINATE
# SYSTEM USED IN MATHEMATICS. POLAR ANGLE "PHI" (0,360) IS FROM THE Z-AXIS
# AND AZIMUTHAL ANGLE "THETA" (0,180) IS FROM THE X-AXIS.
# SPIN AXIS FOLLOWS THE RIGHT-HANDED COORDINATE SYSTEM
############################################################


############################################################
# SIMULATE A PITCH
# realThrow = trajectory.pitch(x,y,z,v_x,v_y,v_z,w,theta,phi,totalTime,fps,mode='gravity+drag+magnus')
# print (realThrow,status)
# idealThrow = trajectory.pitch(x,y,z,v_x,v_y,v_z,w,theta,phi,mode='gravity')
############################################################


# ############################################################
# # PLOTTING THE TRAJECTORY RESULTS
# # SOLID BLACK LINE CORRESPONDS TO THE REAL TRAJECTORY AND THE
# # DOTTED RED LINE SHOWS THE TRAJECTORY IN ABSENCE OF DRAG AND
# # MAGNUS FORCES

# # TOP-LEFT: PITCH PARAMETERS, AND BALL SPEED AS FUNCTION OF TIME
# # TOP-RIGHT: 3D TRAJECTORIES

# # MIDDLE ROW: X, Y, AND Z BALL POSITIONS AS FUNCTION OF TIME

# # BOTTOM ROW: X, Y, AND Z COMPONENTS OF BALL VELOCITY AS FUNCTION
# # OF TIME
# fig = plt.figure(figsize=(8,8))

# ax_text = plt.subplot2grid(shape=(5,3),loc=(0,0),colspan=1,fig=fig)
# ax_v = plt.subplot2grid(shape=(5,3),loc=(1,0),colspan=1,fig=fig)
# ax_3d = plt.subplot2grid(shape=(5,3),loc=(0,1),colspan=2,rowspan=3,fig=fig,projection='3d')
# ax_x = plt.subplot2grid(shape=(5,3),loc=(3,0),colspan=1,fig=fig)
# ax_y = plt.subplot2grid(shape=(5,3),loc=(3,1),colspan=1,fig=fig)
# ax_z = plt.subplot2grid(shape=(5,3),loc=(3,2),colspan=1,fig=fig)
# ax_vx = plt.subplot2grid(shape=(5,3),loc=(4,0),colspan=1,fig=fig)
# ax_vy = plt.subplot2grid(shape=(5,3),loc=(4,1),colspan=1,fig=fig)
# ax_vz = plt.subplot2grid(shape=(5,3),loc=(4,2),colspan=1,fig=fig)

# ax_text.text(0.1,0.8,s='(x, y, z) = (%.1f, %.1f, %.1f)' %(x,y,z),fontsize=8)
# ax_text.text(0.1,0.5,s=r'($v_x$, $v_y$, $v_z$) = (%.1f, %.1f, %.1f)' %(v_x,v_y,v_z),fontsize=8)
# ax_text.text(0.1,0.2,s=r'(w, $\theta$, $\phi$) = (%.1f, %.1f, %.1f)' %(w,theta,phi),fontsize=8)
# ax_text.set_xticks([])
# ax_text.set_yticks([])

# ax_v.plot(idealThrow.time,idealThrow.speed,c='r',ls='dashed')
# ax_v.plot(realThrow.time,realThrow.speed,c='k')
# ax_v.set_xlabel('t (s)')
# ax_v.set_ylabel('speed (m/s)')

# circle = Circle((0,0),0.2,facecolor='#BBBBBB',edgecolor='k')
# ax_3d.add_patch(circle)
# art3d.pathpatch_2d_to_3d(circle,z=0,zdir='z')
# circle = Circle((0,18.6),0.5,facecolor='#BBBBBB',edgecolor='k')
# ax_3d.add_patch(circle)
# art3d.pathpatch_2d_to_3d(circle,z=inch2m(10),zdir='z')
# ax_3d.plot(idealThrow.x,idealThrow.y,idealThrow.z,c='r',ls='dashed',label='Vacuum')
# ax_3d.plot(realThrow.x,realThrow.y,realThrow.z,c='k',label='Air')
# ax_3d.legend()
# ax_3d.set_xlim(-5,5)
# ax_3d.set_ylim(-1,20)
# ax_3d.set_zlim(-0.5,4)
# ax_3d.set_xlabel('x (m)')
# ax_3d.set_ylabel('y (m)')
# ax_3d.set_zlabel('z (m)')

# ax_x.plot(idealThrow.time,idealThrow.x,c='r',ls='dashed')
# ax_x.plot(realThrow.time,realThrow.x,c='k')
# ax_x.set_xticklabels([])
# ax_x.set_ylabel('r (m)')
# ax_x.set_title('x')

# ax_y.plot(idealThrow.time,idealThrow.y,c='r',ls='dashed')
# ax_y.plot(realThrow.time,realThrow.y,c='k')
# ax_y.set_xticklabels([])
# ax_y.set_title('y')

# ax_z.plot(idealThrow.time,idealThrow.z,c='r',ls='dashed')
# ax_z.plot(realThrow.time,realThrow.z,c='k')
# ax_z.set_xticklabels([])
# ax_z.set_title('z')

# ax_vx.plot(idealThrow.time,idealThrow.v_x,c='r',ls='dashed')
# ax_vx.plot(realThrow.time,realThrow.v_x,c='k')
# ax_vx.set_xlabel('t (s)')
# ax_vx.set_ylabel('v (m/s)')

# ax_vy.plot(idealThrow.time,idealThrow.v_y,c='r',ls='dashed')
# ax_vy.plot(realThrow.time,realThrow.v_y,c='k')
# ax_vy.set_xlabel('t (s)')

# ax_vz.plot(idealThrow.time,idealThrow.v_z,c='r',ls='dashed')
# ax_vz.plot(realThrow.time,realThrow.v_z,c='k')
# ax_vz.set_xlabel('t (s)')

# plt.savefig('ballTrajectory.png',format='png')
# plt.close()
# ############################################################
