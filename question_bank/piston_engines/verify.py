"""Recompute bank results and check local Markdown; standard library only.
Run: python3 question_bank/piston_engines/verify.py
"""
from math import pi, sqrt, isclose
from pathlib import Path
import json
import re
from urllib.parse import unquote


def cycle(t1, r, af, lhv, combustion=1, cvr=None, cvp=None, gr=None, gp=None):
    if cvr is None:
        rr, rp = 8.314 / 28.9, 8.314 / 28
        cvr, cvp = 1.055 - rr, 1.486 - rp
        gr, gp = 1.055 / cvr, 1.486 / cvp
    q = combustion * lhv / (af + 1)
    t2 = t1 * r ** (gr - 1)
    t3 = 298 + (q + cvr * (t2 - 298)) / cvp
    t4 = t3 / r ** (gp - 1)
    wc, we = cvr * (t2 - t1), cvp * (t3 - t4)
    w = we - wc
    return dict(t1=t1, t2=t2, t3=t3, t4=t4, q=q, wc=wc, we=we,
                w=w, eta=w / (lhv / (af + 1)), eta_released=w / q)


def bisect(f, a, b):
    assert f(a) * f(b) < 0
    for _ in range(90):
        m = (a + b) / 2
        if f(a) * f(m) <= 0:
            b = m
        else:
            a = m
    return (a + b) / 2


def results():
    out = {}
    vs = 6 * pi / 4 * .1 ** 2 * .12 * 2700 / 120
    ma = 1.006 * .8 * vs
    c = cycle(275.15, 7, 14.7, 45000, .9)
    pb = .85 * ma * (1 + 1 / 14.7) * c['w']
    v = 150 * 1.85 / 3.6 * sqrt(1.225 / 1.006)
    out['01'] = dict(**c, vs=vs, ma=ma, mf=ma / 14.7, pb=pb, v=v,
                     drag=1000 * pb / (1.175 * v), litres_h=ma / 14.7 / 708.2 * 3.6e6)
    ta, pa, pr = 255.65, 54.0199, 1.5
    tc = ta + ta * (pr ** (2 / 7) - 1) / .8
    ti = ta + .5 * (tc - ta)
    vs = 6 * pi / 4 * .1 ** 2 * .12 * 2500 / 120
    rho = pa * pr / ((8.314 / 28.9) * ti)
    mr = rho * vs
    ma, mf = mr * 14.7 / 15.7, mr / 15.7
    c = cycle(ti, 7.5, 14.7, 43700, .95)
    pl = .88 * mr * c['w']
    pump = .88 * vs * pa * (pr - 1)
    sc = ma * 1.005 * (tc - ta) / .85
    out['02'] = dict(**c, tc=tc, ti=ti, rho=rho, vs=vs, mr=mr, ma=ma,
                     mf=mf, power_loop=pl, pumping=pump, sc=sc, pb=pl + pump - sc,
                     litres_h=mf / 708.2 * 3.6e6)
    af = (12.5 * 32 + 47 * 28) / 114
    vs = 4 * pi / 4 * .1 ** 2 * .12 * 2500 / 120
    ma = 1.006 * .8 * vs
    c = cycle(275.15, 8, af, 43700, .9)
    pb = .85 * ma * (1 + 1 / af) * c['w']
    v, area = 150 / 3.6, pi * 1.2 ** 2 / 4
    w = bisect(lambda w: 2 * 1.006 * area * w * (v + w) ** 2 - pb * 1000, 0, 100)
    drag = 2 * 1.006 * area * w * (v + w)
    out['03'] = dict(**c, af=af, vs=vs, ma=ma, mf=ma / af, pb=pb,
                     bsfc=ma / af * 3600 / pb, induced=w, drag=drag, eta_p=v / (v + w))
    # Aide Table 8: selected species CO2/N2/Ar/O2/CO/H2O; water 210 ppm.
    # Table 1 supplies M and cp except Ar, which is given in the source question.
    x0 = [.9532, .027, .016, .0013, .0008, 210e-6]
    m = [44.01, 28.013, 39.95, 32.01, 28.0, 18.015]
    cp = [.8418, 1.0416, .523, .9216, 1.0357, 1.8723]
    x = [a / sum(x0) for a in x0]
    mw = sum(a * b for a, b in zip(x, m))
    y = [a * b / mw for a, b in zip(x, m)]
    cpm = sum(a * b for a, b in zip(y, cp))
    rm = 8.314 / mw
    out['04'] = dict(total_percent=100 * sum(x0), mw=mw, mass_fractions=y,
                     cp=cpm, r=rm, cv=cpm-rm, gamma=cpm / (cpm - rm))
    cp = .65 * 1.0416 + .15 * .8418 + .2 * 1.8723
    rg = .65 * .29680 + .15 * .18892 + .2 * .46152
    ma, mf = .2 * 15 / 16, .2 / 16
    rhoe = 101325 / (rg * 1000 * 1173.15)
    vi = ma / (1.225 * pi * .125 ** 2 / 4)
    ve = .2 / (rhoe * pi * .15 ** 2 / 4)
    hout = .2 * cp * (1173.15 - 298.15)
    hin = ma * 1.005 * (288.15 - 298.15)
    kinetic = (.2 * ve ** 2 - ma * vi ** 2) / 2000
    pb = mf * 45000 - 15 + hin - hout - kinetic
    out['05'] = dict(cp=cp, r=rg, ma=ma, mf=mf, rhoe=rhoe, vi=vi, ve=ve,
                     hout=hout, hin=hin, kinetic=kinetic, pb=pb, eta=pb / (mf * 45000))
    t1, t3, cv = 288.15, 1673.15, .718
    t2 = t3 - 800 / cv
    r = (t2 / t1) ** 2.5
    out['06'] = dict(t2=t2, r=r, eta=1-t1/t2, pressure_ratio=r*t3/t1,
                     pmax=101.325*r*t3/t1, carnot=1-t1/t3)
    product_h = -393.52 - 2 * 241.83
    gas = (-201.17 - product_h) / 32 * 1000
    liquid = (-238.58 - product_h) / 32 * 1000
    out['07'] = dict(af=1.5*(32+3.76*28)/32, gas=gas, liquid=liquid,
                     reduction=100*(gas-liquid)/gas)
    lhv = (-208.45 + 8*393.52 + 9*241.83) / 114 * 1000
    c = cycle(288.15, 9.33, af, lhv, cvr=.8392, cvp=1.143, gr=1.327, gp=1.259)
    rr = 8.314 / ((114 + 12.5*32 + 47*28) / (1+12.5+47))
    v1 = .003 * 9.33 / 8.33
    mass = 101.325 * v1 / (rr * 288.15)
    out['08'] = dict(**c, lhv=lhv, af=af, rr=rr, v1=v1, mass=mass,
                     work_kj=mass*c['w'], mep_kpa=mass*c['w']/.003)
    xs = [.0914, .051, .137, .0231, 1-.0914-.051-.137-.0231]
    ms = [44, 28, 18, 2, 28]
    mw = sum(a*b for a,b in zip(xs,ms))
    flows = [.1*a*b/mw for a,b in zip(xs,ms)]
    carbon = xs[0]+xs[1]
    hydrogen = 2*(xs[2]+xs[3])
    mf = .1/mw * (12*carbon+hydrogen)
    afx = (.1-mf)/mf
    n = 2/(hydrogen/carbon-2)
    air_from_oxygen = (2*xs[0]+xs[1]+xs[2])/2
    out['09'] = dict(mw=mw, species_flows=flows, mf=mf, ma=.1-mf, af=afx,
                     h_c=hydrogen/carbon, n=n, n2_o2=xs[-1]/air_from_oxygen)
    vs = .0059
    flow = vs * 2700/120
    ma = 1.225*.85*flow
    out['10'] = dict(eta_air=1-8.5**(-.4), clearance_l=vs*1000/4/(8.5-1),
                     bmep_takeoff=134/flow, bmep_cruise=87.1/(vs*2400/120),
                     ma=ma,mf=ma/14.7, eta_brake=134/(ma/14.7*43700))
    vs = 4*pi/4*.1**2*.12*2500/120
    pb = .85*1000*vs
    ma = .9091*.78*vs
    out['11'] = dict(vs=vs, pi=1000*vs,pb=pb,ma=ma,mf=ma/14.8,
                     eta=pb/(ma/14.8*44425))
    vd = 4*pi/4*.0826**2*.102
    vs = vd*2000/120
    torque = 525*.381
    pb = torque*2*pi*2000/60/1000
    rho = 101300/(287*294.25)
    ma = rho*1.905/60
    mf = .210*708.2/60000
    out['12'] = dict(vd=vd, vs=vs,torque=torque,pb=pb,rho=rho,ma=ma,mf=mf,
                     bsfc=mf*3600/pb,bmep=pb/vs,eta_v=1.905/60/vs,
                     eta_b=pb/(mf*43700),af=ma/mf,phi=14.7/(ma/mf))
    pbtest = 506*.381*2*pi*2700/60/1000
    rho0 = 1.225
    # Q11 explicitly adopts the original approximation: measured power is SSL power.
    pb0 = pbtest
    veq = 150*1.85/3.6
    f = lambda s: .85*pb0*(1.132*s-.132)-350*veq/sqrt(s)/1000
    sigma = bisect(f,.3,1)
    # Aide-memoire Table 5: interpolate adjacent density rows, no extra ISA law.
    height = 3000 + 500 * (.9091 - rho0*sigma) / (.9091 - .8632)
    rows=[]
    for h, rho in ((2000,1.0065),(3000,.9091),(3500,.8632),(4000,.8191)):
        s=rho/rho0
        rows.append([h,s,pb0*(1.132*s-.132),350*veq/sqrt(s)/850])
    out['13'] = dict(pbtest=pbtest,pb0=pb0,power_2000=pb0*(1.132*1.0065/1.225-.132),
                     sigma=sigma,height=height,rows=rows,
                     ceiling_pb=pb0*(1.132*sigma-.132))
    dt = 275.15*(1.3**(2/7)-1)/.8
    ti = 275.15+.5*dt
    out['14'] = dict(delta_t=dt,tc=275.15+dt,sc=.1*1.005*dt/.9,
                     ti=ti,rho_ratio=1.3*275.15/ti,increase=100*(1.3*275.15/ti-1))
    vd = 6*pi/4*.075**2*.1
    vs = vd*2800/120
    dt = 288.15*(1.6**(2/7)-1)/.7
    tc = 288.15+dt
    ratio = 1.6*288.15/tc/.8
    pi0 = 110/.8
    ma = 1.225*1.6*288.15/tc*vs
    sc = ma*1.005*dt/.95
    power_new = .8*pi0*ratio-sc
    pumping = .8*vs*(1.6-1)*101.325
    out['15'] = dict(vd=vd,vs=vs,delta_t=dt,tc=tc,mass_ratio=ratio,ma=ma,
                     pi0=pi0,pi_new=pi0*ratio,sc=sc,pb_new=power_new,
                     increase=power_new-110,pumping=pumping,
                     increase_with_pumping=power_new+pumping-110)
    return out


def check():
    r = results()
    assert len(r) == 15
    # Independently recorded, rounded final results for every source question.
    expected = {
        '01': {'drag': 914.2304, 'litres_h': 35.40969},
        '02': {'pb': 107.30815, 'litres_h': 39.02960},
        '03': {'bsfc': .2690843, 'drag': 1099.0686, 'eta_p': .8151434},
        '04': {'total_percent': 99.851, 'mw': 43.4784621, 'r': .191221115, 'cp': .840853399,
               'cv': .649632284, 'gamma': 1.294352851},
        '05': {'pb': 339.35163, 'eta': .6032918},
        '06': {'r': 5.2405146, 'eta': .4844742, 'pressure_ratio': 30.429176, 'carnot': .8277799},
        '07': {'af': 6.435, 'gas': 21125.3125, 'reduction': 5.5339418},
        '08': {'lhv': 44878.77193, 'eta': .4392473, 'mep_kpa': 1759.6412},
        '09': {'mf': .0073803825, 'af': 12.5494332, 'n': 8.0451977},
        '10': {'eta_air': .5751531, 'clearance_l': .1966667, 'bmep_takeoff': 1009.4162,
               'bmep_cruise': 738.1356, 'eta_brake': .3261003},
        '11': {'pb': 66.75884, 'eta': .3993438},
        '12': {'torque': 200.025, 'pb': 41.893138, 'bsfc': .21300195, 'bmep': 1149.6986,
               'eta_v': .8713344, 'eta_b': .3867564, 'af': 15.364939, 'phi': .9567236},
        '13': {'power_2000': 43.5029536, 'height': 3268.65135},
        '14': {'sc': 2.9896408, 'increase': 23.9687388},
        '15': {'increase': 66.2301017, 'increase_with_pumping': 69.2382434},
    }
    for local_id, values in expected.items():
        for key, value in values.items():
            assert isclose(r[local_id][key], value, rel_tol=1e-5, abs_tol=1e-7), (local_id, key)
    assert isclose(sum(r['04']['mass_fractions']), 1)
    assert isclose(r['04']['cp'] - r['04']['cv'], r['04']['r'])
    assert isclose(r['01']['w'],r['01']['q']-(1.486-8.314/28)*(r['01']['t4']-298)+(1.055-8.314/28.9)*(275.15-298))
    assert isclose(sum(r['09']['species_flows']), .1)
    assert isclose(r['09']['mf'] + r['09']['ma'], .1)
    assert abs(r['03']['drag'] * (150/3.6+r['03']['induced']) - r['03']['pb']*1000) < 1e-7
    assert abs(.85*r['13']['ceiling_pb']-350*(150*1.85/3.6)/sqrt(r['13']['sigma'])/1000) < 1e-9
    root = Path(__file__).parent
    for kind in ('question', 'answer'):
        assert len(list(root.glob(f'{kind}_*.md'))) == 15, kind
    for n in range(1,16):
        for kind in ('question','answer'):
            p = root / f'{kind}_{n:02d}.md'
            assert p.is_file(), p
            text=p.read_text()
            assert '\\boxed' not in text, p
            assert text.count('$$') % 2 == 0, p
            assert text.count('\\[') == text.count('\\]'), p
            assert 'Source:' in text, p
            if kind == 'question':
                assert '[Ans:' not in text and '[Answer:' not in text, p
                assert '**Results:' not in text and '## Verification' not in text, p
    for p in root.glob('*.md'):
        for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)', p.read_text()):
            if '://' not in link:
                target = unquote(link.split('#')[0])
                assert (p.parent / target).is_file(), (p, link)
    q1 = (root / 'question_01.md').read_text()
    q2 = (root / 'question_02.md').read_text()
    q3 = (root / 'question_03.md').read_text()
    assert '28.9kmol/kg' in q1  # Preserve the 2013 typo in the question.
    assert '28.9kg/kmole' in q3 and '114kg/kmole' in q3  # Official 2015 erratum.
    assert '[22+3=25 Marks]' in q1 and '[23+2=25 Marks]' in q2 and '[15+10=25 Marks]' in q3
    assert 'For this question, take Avgas LHV as **45.0 MJ/kg**.' in q1
    assert q1.index('45.0 MJ/kg') < q1.index('determine:')
    # Questions contain only source metadata, exercise givens and tasks.
    # Reference citations/guidance belong in the paired answers and manifest.
    questions = {n: (root / f'question_{n:02d}.md').read_text() for n in range(1, 16)}
    for n, text in questions.items():
        assert not re.search(r'(?im)^\s*(?:#{1,6}\s*|\*\*)provided\b', text), n
        assert not re.search(r'(?m)^#{2,6}\s', text), n  # No renamed data sections.
        assert not re.search(r'(?i)aide|cheat\s*sheet|lecture|appendix|look[ -]?up|\bnotes\b|\b(?:see|consult|refer to)\b|\btable\s+(?:[A-Z]\.)?\d', text), n
        assert not re.search(r'(?i)\b(?:adaptation|adapted|ambiguity|erratum|hint|solution|published)\b|historical override|\[Ans(?:wer)?:|\*\*Results:', text), n
        assert '| Altitude (Km) |' not in text and '| Fuel | Density' not in text, n
        assert '| Gas |' not in text and '| Species | Phase |' not in text, n
        assert '708.2' not in text and '43.7 MJ/kg' not in text, n
        assert not re.search(r'[-−](?:393\.52|241\.83|208\.45|201\.17|238\.58)', text), n
    q4 = questions[4]
    a4 = (root / 'answer_04.md').read_text()
    assert 'CO₂, N₂, Ar, O₂, CO and H₂O' in q4 and 'normalised' in q4
    assert '0.523' in q4 and '39.95' in q4  # Source-given Ar properties.
    assert 'replacement' not in q4 and 'unavailable' not in q4
    assert '43.47846' in a4 and '0.1912211' in a4 and '1.294353' in a4
    givens = {
        8: ('3.0 Litres', '9.33', '| Reactants | 0.8392 | 1.327 |',
            '| Products | 1.143 | 1.259 |', 'full bottom-dead-centre volume'),
        10: ('Four-stroke', '| Cylinders | 4 |', '5.90 L', '| Compression ratio | 8.5 |',
             '134 kW', '2700 RPM', '87.1 kW', '2400 RPM', '85%', '14.7'),
        11: ('liquid isooctane', 'ambient air', 'Neglect ram-pressure recovery',
             '1.0 MPa', '78%', '0.1 m', '85%', '0.12 m', '3000 m', '2500', '175 kph', '14.8'),
        12: ('14.7', '0.381 m', '21.1°C', '101.3 kPa', '82.6 mm', '102 mm',
             '| 2000 | 525 | 1905 | 0.210 |', '| 2700 | 506 | 2360 | 0.278 |',
             'net loads', 'test-cell conditions', '(viii) equivalence ratio'),
        13: ('2700 RPM', '506 N', '0.381 m', 'SSL reference power',
             '1.132', '0.132', '**2000 m**', '150 knots', '350 N', '85%'),
        14: ('1.3 (absolute pressure ratio)', '0.1 kg/s', '2000 m', '90%', '80%', '50%'),
        15: ('75 mm', '100 mm', '110 kW', '2800 RPM', '70%', '1.6', '100%',
             '95%', 'no intercooler', 'net indicated power'),
    }
    for n, values in givens.items():
        assert all(value in questions[n] for value in values), n
    assert '44.425' not in questions[11]  # Fuel reference data are not question givens.
    assert questions[12].index('| 2700 |') < questions[12].index('calculate:')
    assert questions[13].index('0.132') < questions[13].index('(i)')
    manifest = (root / 'manifest.md').read_text()
    aide = '../../MAE3405%20Aide%20Memoire.pdf#page='
    assert all(f'{aide}{page})' in manifest for page in range(1, 7))
    assert '**Results:' not in manifest and '[Answer:' not in manifest
    return r


if __name__ == '__main__':
    print(json.dumps(check(),indent=2))
    print('PASS: all 15 numerical result sets; mass and power balances; 15 complete pairs; local links; Markdown delimiters; exam marks, historical override and erratum; unaided question format, retained exercise givens and updated Mars properties.')
