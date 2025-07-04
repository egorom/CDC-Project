# rk4_models.py

def rk4_sir(n, beta, gamma, s0, i0, r0, dt):
    def dsdt(s, i): return -beta * s * i
    def didt(s, i): return beta * s * i - gamma * i

    S, I, R = [s0], [i0], [r0]
    for i in range(n):
        s, i_ = S[-1], I[-1]

        sk1, ik1 = dsdt(s, i_), didt(s, i_)
        sk2, ik2 = dsdt(s + dt/2*sk1, i_ + dt/2*ik1), didt(s + dt/2*sk1, i_ + dt/2*ik1)
        sk3, ik3 = dsdt(s + dt/2*sk2, i_ + dt/2*ik2), didt(s + dt/2*sk2, i_ + dt/2*ik2)
        sk4, ik4 = dsdt(s + dt*sk3, i_ + dt*ik3), didt(s + dt*sk3, i_ + dt*ik3)

        S.append(s + dt/6*(sk1 + 2*sk2 + 2*sk3 + sk4))
        I.append(i_ + dt/6*(ik1 + 2*ik2 + 2*ik3 + ik4))
        R.append(1 - S[-1] - I[-1])

    return S, I, R

def rk4_sir_demog(n, beta, gamma, mu, s0, i0, r0, dt):
    def dsdt(s, i): return mu - beta * s * i - mu * s
    def didt(s, i): return beta * s * i - gamma * i - mu * i

    S, I, R = [s0], [i0], [r0]
    for i in range(n):
        s, i_ = S[-1], I[-1]

        sk1, ik1 = dsdt(s, i_), didt(s, i_)
        sk2, ik2 = dsdt(s + dt/2*sk1, i_ + dt/2*ik1), didt(s + dt/2*sk1, i_ + dt/2*ik1)
        sk3, ik3 = dsdt(s + dt/2*sk2, i_ + dt/2*ik2), didt(s + dt/2*sk2, i_ + dt/2*ik2)
        sk4, ik4 = dsdt(s + dt*sk3, i_ + dt*ik3), didt(s + dt*sk3, i_ + dt*ik3)

        S.append(s + dt/6*(sk1 + 2*sk2 + 2*sk3 + sk4))
        I.append(i_ + dt/6*(ik1 + 2*ik2 + 2*ik3 + ik4))
        R.append(1 - S[-1] - I[-1])

    return S, I, R

def rk4_seir(n, beta, gamma, sigma, s0, e0, i0, r0, dt):
    def dsdt(s, i): return -beta * s * i
    def dedt(s, e, i): return beta * s * i - sigma * e
    def didt(e, i): return sigma * e - gamma * i

    S, E, I, R = [s0], [e0], [i0], [r0]
    for _ in range(n):
        s, e, i_ = S[-1], E[-1], I[-1]

        sk1, ek1, ik1 = dsdt(s, i_), dedt(s, e, i_), didt(e, i_)
        sk2 = dsdt(s + dt/2*sk1, i_ + dt/2*ik1)
        ek2 = dedt(s + dt/2*sk1, e + dt/2*ek1, i_ + dt/2*ik1)
        ik2 = didt(e + dt/2*ek1, i_ + dt/2*ik1)

        sk3 = dsdt(s + dt/2*sk2, i_ + dt/2*ik2)
        ek3 = dedt(s + dt/2*sk2, e + dt/2*ek2, i_ + dt/2*ik2)
        ik3 = didt(e + dt/2*ek2, i_ + dt/2*ik2)

        sk4 = dsdt(s + dt*sk3, i_ + dt*ik3)
        ek4 = dedt(s + dt*sk3, e + dt*ek3, i_ + dt*ik3)
        ik4 = didt(e + dt*ek3, i_ + dt*ik3)

        S.append(s + dt/6*(sk1 + 2*sk2 + 2*sk3 + sk4))
        E.append(e + dt/6*(ek1 + 2*ek2 + 2*ek3 + ek4))
        I.append(i_ + dt/6*(ik1 + 2*ik2 + 2*ik3 + ik4))
        R.append(1 - S[-1] - E[-1] - I[-1])

    return S, E, I, R

def rk4_seir_demog(n, beta, gamma, mu, sigma, s0, e0, i0, r0, dt):
    def dsdt(s, i): return mu - (beta * i + mu) * s
    def dedt(s, e, i): return beta * s * i - (mu + sigma) * e
    def didt(e, i): return sigma * e - (mu + gamma) * i

    S, E, I, R = [s0], [e0], [i0], [r0]
    for _ in range(n):
        s, e, i_ = S[-1], E[-1], I[-1]

        sk1, ek1, ik1 = dsdt(s, i_), dedt(s, e, i_), didt(e, i_)
        sk2 = dsdt(s + dt/2*sk1, i_ + dt/2*ik1)
        ek2 = dedt(s + dt/2*sk1, e + dt/2*ek1, i_ + dt/2*ik1)
        ik2 = didt(e + dt/2*ek1, i_ + dt/2*ik1)

        sk3 = dsdt(s + dt/2*sk2, i_ + dt/2*ik2)
        ek3 = dedt(s + dt/2*sk2, e + dt/2*ek2, i_ + dt/2*ik2)
        ik3 = didt(e + dt/2*ek2, i_ + dt/2*ik2)

        sk4 = dsdt(s + dt*sk3, i_ + dt*ik3)
        ek4 = dedt(s + dt*sk3, e + dt*ek3, i_ + dt*ik3)
        ik4 = didt(e + dt*ek3, i_ + dt*ik3)

        S.append(s + dt/6*(sk1 + 2*sk2 + 2*sk3 + sk4))
        E.append(e + dt/6*(ek1 + 2*ek2 + 2*ek3 + ek4))
        I.append(i_ + dt/6*(ik1 + 2*ik2 + 2*ik3 + ik4))
        R.append(1 - S[-1] - E[-1] - I[-1])

    return S, E, I, R