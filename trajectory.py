import numpy
from numpy import cos,sin,deg2rad,pi,sqrt,exp

class pitch:
    ########################################################
    def __init__(self,x,y,z,v_x,v_y,v_z,w,theta,phi,mode):
        '''
        CONVERT 'W' FROM RPM TO RAD/S
        CONVERT 'THETA' FROM DEGREE TO RAD
        CONVERT 'PHI' FROM DEGREE TO RAD
        INITIALIZA VARIOUS CONSTANTS
        CREATE A LIST WITH TIME, BALL POSITION, VELOCITY, AND SPEED
        CONVERT LIST TO ARRAY
        
        USAGE:
        class_object = pitch(x,y,z,v_x,v_y,v_z,w,theta,phi,mode)
        
        PARAMETERS:
        x     - X POSITION OF THE BALL AT TIME = 0
        y     - Y POSITION OF THE BALL AT TIME = 0
        z     - Z POSITION OF THE BALL AT TIME = 0
        v_x   - X COMPONENT OF THE BALL VELOCITY AT TIME = 0 
        v_y   - Y COMPONENT OF THE BALL VELOCITY AT TIME = 0
        v_z   - Z COMPONENT OF THE BALL VELOCITY AT TIME = 0
        w     - SPIN RATE IN RPM
        theta - AZIMUTH ANGLE OF THE SPIN AXIS IN DEGREES
        phi   - POLAR ANGLE OF THE SPIN AXIS IN DEGREES
        mode  - 'gravity+drag+magnus', 'gravity+drag', OR 'gravity' 
                DEPENDING ON WHAT FORCES NEED TO BE CONSIDERED
                
        RETURNS: NONE
        TIME, BALL POSITION, AND VELOCITY CAN BE ACCESSED USING CLASS OBJECT
        class_object.time
        class_object.x
        class_object.y
        class_object.z
        class_object.v_x
        class_object.v_y
        class_object.v_z
        class_object.speed
        '''
        w = w*pi/30
        theta = deg2rad(theta)
        phi = deg2rad(phi)
        
        self.dt = 1e-4
        self.g = 9.81
        self.v_d = 35
        self.delta = 5
        self.B = 4.1e-4
        
        self.time = [0]
        self.x,self.y,self.z = [x],[y],[z]
        self.v_x,self.v_y,self.v_z = [v_x],[v_y],[v_z]
        self.speed = [sqrt(v_x**2 + v_y**2 + v_z**2)]
        
        self.findTrajectory(x,y,z,v_x,v_y,v_z,w,theta,phi,mode)
        
        self.time = numpy.asarray(self.time)
        self.x = numpy.asarray(self.x)
        self.y = numpy.asarray(self.y)
        self.z = numpy.asarray(self.z)
        self.v_x = numpy.asarray(self.v_x)
        self.v_y = numpy.asarray(self.v_y)
        self.v_z = numpy.asarray(self.v_z)
        self.speed = numpy.asarray(self.speed)
    ########################################################
    
    ########################################################
    def findTrajectory(self,x_0,y_0,z_0,v_x_0,v_y_0,v_z_0,w,theta,phi,mode):
        '''
        CALCULATE THE TRAJECTORY OF THE BALL BASED ON INITIAL POSITION,
        VELOCITY, AND SPIN
        '''
        counter = 1
        while (y_0>0 and z_0>0):
            x_1,y_1,z_1,v_x_1,v_y_1,v_z_1 = self.positionAfter_dt(x_0,y_0,z_0,v_x_0,v_y_0,v_z_0,w,theta,phi,mode)
            x_0,y_0,z_0 = x_1,y_1,z_1
            v_x_0,v_y_0,v_z_0 = v_x_1,v_y_1,v_z_1
            
            self.time.append(counter*self.dt)
            self.x.append(x_0)
            self.y.append(y_0)
            self.z.append(z_0)
            self.v_x.append(v_x_0)
            self.v_y.append(v_y_0)
            self.v_z.append(v_z_0)
            self.speed.append(sqrt(v_x_0**2 + v_y_0**2 + v_z_0**2))
            
            counter+=1
    ########################################################
    
    ########################################################
    def f(self,v):
        '''
        DYNAMIC DRAG COEFFICIENT FOR DIFFERENT BASEBALL SPEED
        '''
        f = 0.0039 + 0.0058/(1+exp((v-self.v_d)/self.delta))
        return f
    ########################################################
    
    ########################################################
    def positionAfter_dt(self,x_0,y_0,z_0,v_x_0,v_y_0,v_z_0,w,theta,phi,mode):
        '''
        CALCULATE THE BALL POSITION AFTER SMALL TIME dt
        '''
        v = sqrt(v_x_0**2 + v_y_0**2 + v_z_0**2)
        dt = self.dt
        g = self.g
        B = self.B
        
        X_0 = v_x_0
        Y_0 = v_y_0
        Z_0 = v_z_0
        
        if (mode=='gravity+drag+magnus'):
            AA =    -self.f(v)*v*X_0 + w*B*(                                    -cos(phi)*Y_0 +sin(phi)*sin(theta)*Z_0)
            BB =    -self.f(v)*v*Y_0 + w*B*(            cos(phi)*X_0                          -sin(phi)*cos(theta)*Z_0)
            CC = -g -self.f(v)*v*Z_0 + w*B*(-sin(phi)*sin(theta)*X_0 +sin(phi)*cos(theta)*Y_0                         )
        elif (mode=='gravity+drag'):
            AA =    -self.f(v)*v*X_0
            BB =    -self.f(v)*v*Y_0
            CC = -g -self.f(v)*v*Z_0
        elif (mode=='gravity'):
            AA = 0
            BB = 0
            CC = -g
        
        X_1 = AA*dt + X_0
        Y_1 = BB*dt + Y_0
        Z_1 = CC*dt + Z_0
        
        x_1 = x_0 + X_1*dt
        y_1 = y_0 + Y_1*dt
        z_1 = z_0 + Z_1*dt
        
        return x_1,y_1,z_1,X_1,Y_1,Z_1
    ########################################################
