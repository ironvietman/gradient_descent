# Implementation of gradient descent using
# E(u,v) = (u*exp(v) - 2*v*exp(-u))^2
from decimal import Decimal


def delta_u(u, v):
    return Decimal(2)*(Decimal.exp(v) + Decimal(2)*v*Decimal.exp(-u)) * \
            (u*Decimal.exp(v) - Decimal(2)*v*Decimal.exp(-u))


def delta_v(u, v):
    return Decimal(2)*(u*v*Decimal.exp(v) - Decimal(2)*Decimal.exp(-u)) * \
           (u*Decimal.exp(v) - Decimal(2)*v*Decimal.exp(-u))

print 'gradient decent'
eta = Decimal(0.1)       # learning rate
u = Decimal(1)           # weight component
v = Decimal(1)           # weight component
for i in range(1, 20):
    Ein = (u*Decimal.exp(v) - 2*v*Decimal.exp(-u))**2
    print 'Error:', i, Ein
    if (Ein < 10**-14):
        print '({}, {})'.format(u, v)
        break
    temp_u = u - eta * delta_u(u, v)
    v = v - eta * delta_v(u, v)
    u = temp_u

print 'coordinate decent'
eta = Decimal(0.1)       # learning rate
u = Decimal(1)           # weight component
v = Decimal(1)           # weight component
for i in range(1, 15):
    temp_u = u - eta * delta_u(u, v)
    Ein_u = (temp_u*Decimal.exp(v) - 2*v*Decimal.exp(-temp_u))**2
    temp_v = v - eta * delta_v(u, v)
    Ein_v = (temp_u*Decimal.exp(v) - 2*v*Decimal.exp(-temp_u))**2
    if(Ein_u < Ein_v):
        u = temp_u;
    else:
        v = temp_v;

Ein = (u*Decimal.exp(v) - 2*v*Decimal.exp(-u))**2
print 'Error:', Ein
