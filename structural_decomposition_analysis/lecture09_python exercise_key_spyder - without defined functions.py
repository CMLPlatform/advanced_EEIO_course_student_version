#%%
import numpy as np
# Input data
# t=0 transaction matrix and final demand vector
Z_0 = np.array([
    [10, 20, 25],
    [15, 5, 30],
    [30, 40, 5]
])

f_0 = np.array([
    [45],
    [30],
    [25]
])

# t=1 transaction matrix and final demand vector
Z_1 = np.array([
    [12, 15, 35],
    [24, 11, 30],
    [36, 50, 8]
])

f_1 = np.array([
    [50],
    [35],
    [26]
])

#%%
# Calculate total requirements matrix



x_0 = Z_0.sum(axis=1, keepdims=True) + f_0
A_0 = Z_0 /x_0.transpose()
L_0 = np.linalg.inv(np.eye(3) - A_0)  


x_1 = Z_1.sum(axis=1, keepdims=True) + f_1
A_1 = Z_1 /x_1.transpose()
L_1 = np.linalg.inv(np.eye(3) - A_1)


# All input data for our SDA is now complete.
# Start decomposing the effect of technology change and final demand change on the
# total output. A two factor decomposition.

#%%
# change in the total requirements matrix
L_delta = L_1 - L_0
# change in the final demand
f_delta = f_1 - f_0
# change in total output - used as check
x_delta = x_1 - x_0
#%%
# decomposition (eq 13.3)
tech_change = L_delta.dot(f_0)
fd_change = L_1.dot(f_delta)

# check if our result is complete
tot_change = tech_change + fd_change
check = x_delta - tot_change

if np.isclose(check, np.zeros(check.shape), atol=1E-6).all():
    print('Decomposition correct')
else:
    print('ERROR - check your decomposition')

result = {"13.3": [tech_change, fd_change]}

print(f"\n13.3:\ntech_change: {tech_change}\nfd_change: {fd_change}")

#%%
# decomposition (eq 13.4)
tech_change = np.dot(L_delta, f_1)
fd_change = np.dot(L_0, f_delta)

# check if our resul is complete
tot_change = tech_change + fd_change
check = x_delta - tot_change

if np.isclose(check, np.zeros(check.shape), atol=1E-6).all():
    print('Decomposition correct')
else:
    print('ERROR - check your decomposition')

result["13.4"] = [tech_change, fd_change]

print(f"\n13.4:\ntech_change: {tech_change}\nfd_change: {fd_change}")

#%%
# decomposition (eq 13.5)
tech_change = np.dot(L_delta, f_0)
fd_change = np.dot(L_0, f_delta)
interaction = np.dot(L_delta, f_delta)

# check if our result is complete
tot_change = tech_change + fd_change + interaction
check = x_delta - tot_change

if np.isclose(check, np.zeros(check.shape), atol=1E-6).all():
    print('Decomposition correct')
else:
    print('ERROR - check your decomposition')

result["13.5"] = [tech_change, fd_change, interaction]

print(
    (f"\n13.5:\ntech_change: {tech_change}\nfd_change: {fd_change}"
    f"\ninteraction: {interaction}")
)

#%%
# decomposition (eq 13.6)
tech_change = np.dot(L_delta, f_1)
fd_change = np.dot(L_1, f_delta)
interaction = np.dot(L_delta, f_delta)

# check if our result is complete
tot_change = tech_change + fd_change - interaction
check = x_delta - tot_change

if np.isclose(check, np.zeros(check.shape), atol=1E-6).all():
    print('Decomposition correct')
else:
    print('ERROR - check your decomposition')

result["13.6"] = [tech_change, fd_change, interaction]

print(
    (f"\n13.6:\ntech_change: {tech_change}\nfd_change: {fd_change}"
    f"\ninteraction: {interaction}")
)

#%%
# decomposition (eq 13.7)
tech_change = 0.5 * np.dot(L_delta, f_0 + f_1)
fd_change = 0.5 * np.dot(L_0 + L_1, f_delta)

# check if our result is complete
tot_change = tech_change + fd_change
check = x_delta - tot_change

if np.isclose(check, np.zeros(check.shape), atol=1E-6).all():
    print('Decomposition correct')
else:
    print('ERROR - check your decomposition')

result["13.7"] = [tech_change, fd_change]

print(f"\n13.7:\ntech_change: {tech_change}\nfd_change: {fd_change}")

#%%