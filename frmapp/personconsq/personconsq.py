import personconsq.warningtime as pw
import personconsq.rescued as pr
import personconsq.smokestairtime as ps
import firespread.approxnorm as fs

# num of ppl poss to rescue:
def nrescued(layout):

    if layout == 1:
        i = 0
    elif layout == 2:
        i = 1
    elif layout == 3:
        i = 3
    elif layout == 4:
        i = 6

    return i

def travel(nres, ntot, stw):
    p(1) = (ntot - nres(1))/(stw - 0.3)
    p(2) = (ntot - nres(2+i))/(stw - 0.3)
    p(3) = (ntot - nres(3+2*i))/(stw - 0.3)
    p(4) = (ntot - nres(4+3*i))/(stw - 0.3)

    sigma_move = 0.26
    t1 = 0.68 + 0.081 * (p(1))**0.73
    t2 = 0.68 + 0.081 * (p(2))**0.73
    t3 = 0.68 + 0.081 * (p(3))**0.73
    t4 = 0.68 + 0.081 * (p(4))**0.73

    mu_move(1) = fs.appnorm(t1, 0.0001, sigma_move)
    mu_move(2) = fs.appnorm(t2, 0.0001, sigma_move)
    mu_move(3) = fs.appnorm(t3, 0.0001, sigma_move)
    mu_move(4) = fs.appnorm(t4, 0.0001, sigma_move)

