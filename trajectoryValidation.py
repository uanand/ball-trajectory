import numpy
import matplotlib.pyplot as plt

plt.style.use("uanand")

r_ref = 16.0
v_ref = 25.0
a_ref = -5.0
t_ref = 0.15

t_0 = 0.05
r_0 = r_ref + v_ref * (t_0 - t_ref) + 1.0 / 2.0 * a_ref * (t_0 - t_ref) * (t_0 - t_ref)
v_0 =         v_ref                 +             a_ref * (t_0 - t_ref)
a_0 =                                             a_ref

t_1 = 0.70
r_1_method1 = r_0 + v_0 * (t_1 - t_0) + 1.0 / 2.0 * a_0 * (t_1 - t_0) * (t_1 - t_0)
v_1_method1 =       v_0               +             a_0 * (t_1 - t_0)
a_1_method1 =                                       a_0

r_1_method2 = r_ref + v_ref * (t_1 - t_ref) + 1.0 / 2.0 * a_ref * (t_1 - t_ref) * (t_1 - t_ref)
v_1_method2 =         v_ref                 +             a_ref * (t_1 - t_ref)
a_1_method2 =                                             a_ref

print (r_1_method1, v_1_method1, a_1_method1)
print (r_1_method2, v_1_method2, a_1_method2)