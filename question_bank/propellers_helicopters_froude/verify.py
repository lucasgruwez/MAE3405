"""Check question format, local links and numerical answers: python3 verify.py."""
from math import pi, sqrt
from pathlib import Path
import re
from urllib.parse import unquote


def close(actual, expected, tolerance):
    assert abs(actual - expected) < tolerance, (actual, expected)


def check_files():
    folder = Path(__file__).resolve().parent
    aide = '../../MAE3405%20Aide%20Memoire.pdf'
    for prefix in ('question', 'answer'):
        assert len(list(folder.glob(f'{prefix}_*.md'))) == 11
        for number in range(1, 12):
            path = folder / f'{prefix}_{number:02}.md'
            text = path.read_text()
            assert '\\boxed' not in text, path
            if prefix == 'question':
                assert '[Ans:' not in text and '[Answer:' not in text, path
                assert re.search(r'^Source: \[.+\]\(.+#page=\d+\)\.', text, re.M), path
                assert not re.search(r'^\s*(?:#{1,6}\s*|\*\*)?Provided\b', text, re.I | re.M), path
                # Source page metadata is allowed; lookup directions are not.
                body = re.sub(r'^Source:.*$', '', text, flags=re.M)
                assert not re.search(
                    r'\b(?:aide|cheat\s*sheet|lecture|adaptation|adapted|near[- ]duplicate|'
                    r'hint|quartic|trial|root bracket)\b|\b(?:table|page)\s+\d|\bp\.\s*\d',
                    body, re.I,
                ), path
                assert not re.search(
                    r'\b(?:see|consult|look\s+up|refer\s+to|use|from)\b[^\n.]*'
                    r'\b(?:tables?|pages?|relations?|equations?|formulas?)\b', body, re.I,
                ), path
                # Blade geometry and unit-conversion givens remain valid equations.
                assert not re.search(
                    r'\\(?:rho|Omega|sqrt|dot|eta)\b|\b(?:v_i|u_r)\s*[=^]|'
                    r'\b[PT]\s*=|\bideal\s+(?:disk|rotor)', body, re.I,
                ), path
            elif number != 4:  # The electrical motor answer needs no aide data.
                assert aide + '#page=' in text, path
            for link in re.findall(r'\]\(([^)]+)\)', text):
                if not link.startswith(('http:', 'https:')):
                    assert (folder / unquote(link.split('#')[0])).exists(), (path, link)
    manifest = (folder / 'manifest.md').read_text()
    for link in re.findall(r'\]\(([^)]+)\)', manifest):
        assert (folder / unquote(link.split('#')[0])).exists(), link


def root(f, lo, hi):
    assert f(lo) * f(hi) <= 0
    for _ in range(100):
        mid = (lo + hi) / 2
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


def forward(m, rho, area, cd, u):
    b = m * 9.81 / (2 * rho * area)
    f = lambda v: v**4 - v*v*u*u - cd*u**3*v/2 - cd**2*u**4/16 - b*b
    v = root(f, u, u + sqrt(b) + 100)
    drag = rho * area * cd * u*u/2
    thrust = sqrt((m*9.81)**2 + drag**2)
    vi = thrust/(2*rho*area*v)
    power = thrust*vi + drag*u
    assert abs(f(v)) < 1e-6
    close(thrust, 2*rho*area*v*vi, 1e-8)
    return dict(relative=v, drag=drag, thrust=thrust, induced=vi, power=power)


def otto(r, t1, p1, nc, stroke, rpm, ev, af, ec, em):
    cvr, cvp, gas = .768, 1.199, .287
    t2 = t1*r**(gas/cvr)
    q = ec*43700/(af+1)
    t3 = 298 + (q+cvr*(t2-298))/cvp
    t4 = t3/r**(gas/cvp)
    work = cvp*(t3-t4)-cvr*(t2-t1)
    swept = nc*pi*.1**2/4*stroke*rpm/120
    air = ev*p1/(287*t1)*swept
    fuel = air/af
    charge = air + fuel
    power = em*charge*work*1000
    assert abs(cvp*(t3-298)-cvr*(t2-298)-q)<1e-9
    return dict(t1=t1,t2=t2,t3=t3,t4=t4,q=q,work=work,swept=swept,charge=charge,fuel=fuel,litres=fuel*3600/.7082,power=power)


def calculate():
    omega = sqrt(20*9.81/(.5*1.225*.25*(3.5**3-.4**3)/3))
    thrust = 80*9.81
    p1 = thrust*sqrt(thrust/(2*1.225*pi*3.5**2))
    close(omega*60/(2*pi), 90.4859, .0001)
    close(p1, 2264.19, .01)
    print('01',dict(omega=omega,rpm=omega*60/(2*pi),thrust=thrust,induced=p1/thrust,power=p1))
    rho=1.111; area=pi*5**2; thrust=2000*9.81
    vi=sqrt(thrust/(2*rho*area)); power=thrust*vi; omega=.5*336.43/5
    torque=power/omega; tailthrust=torque/6
    tailpower=tailthrust*sqrt(tailthrust/(2*rho*pi*.75**2))
    close(power, 208032.667, .01)
    close(torque, 6183.535, .01)
    close(tailpower, 16696.296, .01)
    print('02',dict(induced=vi,power=power,omega=omega,rpm=omega*60/(2*pi),torque=torque,tailthrust=tailthrust,tailpower=tailpower))
    area=pi*17.5**2; p0=8100000; main0=.8*p0
    total=(main0*sqrt(2*1.225*area))**(2/3)/9.81
    req0=(28000*9.81)**1.5/sqrt(2*1.225*area)
    sigma=root(lambda s:p0*s-.2*p0-req0/sqrt(s),.3,1)
    rho=1.225*sigma
    # Aide Table 5: adjacent 4.0/4.5 km density rows.
    assert .7768 < rho < .8191
    altitude=4000+500*(.8191-rho)/(.8191-.7768)
    print('03/10',dict(total=total,payload=total-28000,req0=req0,sigma=sigma,rho=rho,altitude=altitude))
    close(total, 47153.2554, .001)
    close(altitude, 4226.602, .01)
    close(p0*sigma-.2*p0, req0/sqrt(sigma), 1e-6)
    pin0=sqrt(3)*440*1.2*.3; pin=sqrt(3)*440*6.8*.78; pout=5*746
    close(pin0, 274.35685, .0001)
    close(pin, 4042.19089, .0001)
    close(pout/pin, .92276691, 1e-8)
    print('04',dict(pin0=pin0,pin=pin,pout=pout,loss=pin-pout,eff=pout/pin,reg=(1195-1150)/1150*100))
    a=otto(7.5,275.15,79495.2,4,.125,2700,.8,14.5,.99,.85)
    a['thrust']=(a['power']*sqrt(2*1.006*pi))**(2/3)
    close(a['power'], 67982.8343, .001)
    close(a['thrust'], 3079.8209, .001)
    print('05',a)
    af=(1+2.2/4)*(32+3.76*28)/(12+2.2)
    swept=6*pi*.1**2/4*.12*2500/120
    air=.85*89874.5/(287*281.65)*swept
    fuel=air/af
    charge=air+fuel
    main=750*9.81*sqrt(750*9.81/(2*1.111*pi*4**2)); totalpower=1.1*main
    close(fuel*3600/.7082, 37.76947, .0001)
    close(fuel*3600/(totalpower/1000), .40720738, 1e-8)
    close(totalpower/(.9*.98*fuel*43700000), .229370118, 1e-8)
    print('06',dict(af=af,swept=swept,charge=charge,fuel=fuel,litres=fuel*3600/.7082,mainpower=main,power=totalpower,bsfc=fuel*3600/(totalpower/1000),brake_eff=totalpower/(fuel*43700000),indicated_eff=totalpower/(.9*fuel*43700000)))
    # Aide Table 5: interpolate sea level to 500 m, rather than add an ISA model.
    h=200*.3048; rho=1.225+(1.1673-1.225)*h/500
    close(rho, 1.217965216, 1e-12)
    drone=forward(1.5,rho,4*pi*(.1016/2)**2,.75,10)
    drone.update(rho=rho,elecpower=drone['power']/.8,minutes=1.3*22.2/(drone['power']/.8)*60,rpm=1200*22.2*5/6)
    print('07',drone)
    omega=2700*2*pi/60
    integ=lambda x: .66*x**3-.615*x**4+.12*x**5
    integral=integ(1)-integ(.05)
    thrust=3/2*1.225*omega**2*.1*integral
    print('08',dict(integral=integral,thrust=thrust,induced=sqrt(thrust/(2*1.225*pi))))
    tc=288.15*(1+(1.3**(.4/1.4)-1)/.85); t1=288.15+.25*(tc-288.15)
    a=otto(7,t1,1.3*101325,4,.12,2500,1,14.5,.95,.9)
    a.update(tc=tc,thrust=(a['power']*sqrt(2*1.225*pi*.9**2))**(2/3))
    close(a['power'], 115013.606, .001)
    close(a['thrust'], 4352.77754, .001)
    print('09',a)
    heli=forward(600,1.111,pi*5**2,.35,25*1.85/3.6)
    print('11',heli)
    close(heli['power'], 49066.0316, .001)
    close(heli['relative'], 14.0783833, .000001)
    close(drone['minutes'], 7.41043, .00001)
    close(drone['rpm'], 22200, .0001)
    close(thrust, 2422.63997, .0001)
    close(sqrt(thrust/(2*1.225*pi)), 17.7413417, .000001)


if __name__ == '__main__':
    check_files()
    calculate()
    print('PASS: all 11 pairs, question format, source/answer-reference links and numerical checks.')
