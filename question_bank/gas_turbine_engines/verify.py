"""Reproduce bank numbers: python3 question_bank/gas_turbine_engines/verify.py.
SI units throughout; constant-cp, 298 K reference (Topic 8 pp.35–36).
No Cohen-chart values are inferred. Outputs are also useful intermediate states.
"""
from math import pi, sqrt, sin, cos, tan, atan, radians, degrees
import json

# Aide Tables 1–2 (p.1), Table 11 (p.5), reference data (p.6).
# Hot-product CG/GG remain lecture approximations: not tabulated in the aide.
CA, CG, GA, GG, R, LHV, TR = 1005., 1148., 1.4, 1.333, 287., 43100000., 298.
DECANE_LHV = 44602000.  # Table 11 n-decane; never substitute Jet A1 in Q28B.
# Historical rounded exam ISA retained except Q04's direct aide 6.5 km row.
ATM = {0:(288.15,101325.,1.225,340.29),5:(255.65,54019.9,.7361,320.52),
       6.5:(245.9,44034.8461,.6238,314.3579),7:(242.65,41060.7,.5895,312.27),
       10:(223.15,26436.2,.4127,299.46),20:(216.65,5474.88,.088,295.06)}

def intake(T,p,V,eta=.95):
    return T+V*V/(2*CA), p*(1+eta*V*V/(2*CA*T))**(GA/(GA-1))

def compressor(T,p,r,eta):
    return T*(1+(r**((GA-1)/GA)-1)/eta), p*r

def fuel(Tin,Tout,eta=.98,cpin=CA):
    return (CG*(Tout-TR)-cpin*(Tin-TR))/(eta*LHV-CG*(Tout-TR))

def burner(Tin,f,eta=.98,cpin=CA,lhv=LHV):
    return TR+(cpin*(Tin-TR)+f*eta*lhv)/((1+f)*CG)

def turbine_work(T,p,w,eta=.9):
    Tout=T-w/CG
    return Tout,p*(1-(T-Tout)/(eta*T))**(GG/(GG-1))

def turbine_pressure(T,p,pout,eta=.9):
    return T*(1-eta*(1-(pout/p)**((GG-1)/GG))),pout

def nozzle(T,p,pa,eta=.95,hot=True,cd=False):
    cp,g=(CG,GG) if hot else (CA,GA)
    critical=(1-(g-1)/(eta*(g+1)))**(-g/(g-1))
    choked=p/pa>=critical and not cd
    if choked:
        Te=2*T/(g+1); pe=p/critical; V=sqrt(g*R*Te)
    else:
        pe=pa; Te=T*(1-eta*(1-(pe/p)**((g-1)/g))); V=sqrt(2*cp*(T-Te))
    rho=pe/(R*Te)
    return dict(Te=Te,pe=pe,Ve=V,rho=rho,flux=rho*V,critical=critical,choked=choked)

def thrust(ma,f,V,n):
    A=ma*(1+f)/n['flux']
    momentum=ma*((1+f)*n['Ve']-V)
    pressure=A*(n['pe']-n.get('pa',0)) if 'pa' in n else 0
    return A,momentum+pressure,pressure

def jet(T,p,pa,ma,f,V,eta=.95,cd=False):
    n=nozzle(T,p,pa,eta,cd=cd); n['pa']=pa
    A,F,P=thrust(ma,f,V,n)
    return dict(**n,A=A,F=F,pressure_thrust=P,TSFC=3600000*ma*f/F)

def shock(M):
    m2=sqrt((1+.2*M*M)/(1.4*M*M-.2))
    pr=1+2*GA/(GA+1)*(M*M-1)
    dr=(GA+1)*M*M/((GA-1)*M*M+2)
    p0r=((GA+1)*M*M/((GA-1)*M*M+2))**(GA/(GA-1))*((GA+1)/(2*GA*M*M-(GA-1)))**(1/(GA-1))
    return m2,pr,pr/dr,p0r

def supersonic(M,beta=None,eta=.95):
    T,p,_,a=ATM[20]; V=M*a
    T0=T*(1+.2*M*M); p0=p*(1+.2*M*M)**3.5
    extra={}
    if beta is not None:
        b=radians(beta)
        theta=atan(2/tan(b)*(M*M*sin(b)**2-1)/(M*M*(GA+cos(2*b))+2))
        mn=M*sin(b); mn2,pr,tr,rec=shock(mn)
        M=mn2/sin(b-theta)
        p*=pr; T*=tr; p0*=rec
        extra=dict(theta=degrees(theta),Mn1=mn,M_after_oblique=M,oblique_recovery=rec)
    if M>1:
        M,pr,tr,rec=shock(M); p*=pr; T*=tr; p0*=rec
        extra.update(normal_recovery=rec)
    # Apply subsonic diffuser efficiency only to the remaining dynamic head.
    p01=p*(1+eta*.2*M*M)**3.5
    return dict(V=V,T0=T0,p0_after_shocks=p0,p01=p01,M_after_shocks=M,T_after_shocks=T,p_after_shocks=p,**extra)

def turbojet():
    T,p,rho,a=ATM[7]; V=260.; ma=15.
    T01,p01=intake(T,p,V); T02,p02=compressor(T01,p01,9,.87)
    f=fuel(T02,1250)
    T04,p04=turbine_work(1250,.94*p02,CA*(T02-T01)/(.99*(1+f)),.87)
    return dict(V=V,ma=ma,T01=T01,p01=p01,T02=T02,p02=p02,f=f,T04=T04,p04=p04,**jet(T04,p04,p,ma,f,V))

def turboprop(alt,V,A,r,f=None,T03=None,ec=.85,et=.9,ei=.95,loss=.03,pnpr=1.3,gear=.85,prop=.8,reheat=None,single=False):
    T,p,rho,a=ATM[alt]; ma=rho*V*A
    T01,p01=intake(T,p,V,ei); T02,p02=compressor(T01,p01,r,ec)
    if f is None: f=fuel(T02,T03)
    else: T03=burner(T02,f)
    p03=(1-loss)*p02; wc=CA*(T02-T01)
    T04,p04=turbine_work(T03,p03,wc/(.99*(1+f)),et)
    fr=0.; Tr,pr=T04,p04; ft=f
    if reheat is not None:
        fr=reheat; Tr=burner(T04,fr,cpin=CG); pr=.98*p04; ft=f+fr*(1+f)
    if single:
        T05,p05=turbine_pressure(T03,p03,pnpr*p,et)
        wt=ma*(1+f)*CG*(T03-T05)
        power=gear*(wt-ma*wc/.99)
    else:
        T05,p05=turbine_pressure(Tr,pr,pnpr*p,et)
        power=gear*ma*(1+ft)*CG*(Tr-T05)
    j=jet(T05,p05,p,ma,ft,V)
    return dict(ma=ma,T01=T01,p01=p01,T02=T02,p02=p02,f=f,T03=T03,p03=p03,T04=T04,p04=p04,fr=fr,ft=ft,Tr=Tr,pr=pr,T05=T05,p05=p05,shaft=power,TP=prop*power+V*j['F'],fuel_lph=3600000*ma*ft/793.,**j)

def calculations():
    out={}
    # 01 aft fan: independent capture areas, power turbine sets fan work, not FPR.
    T,p,rho,a=ATM[10]; V=.8*a; mh=rho*V*.5; mc=rho*V*2.5
    d=turboprop(10,V,.5,15,f=.02,pnpr=1.2,gear=1,prop=1)
    Tfan=d['T01']+d['shaft']/(mc*CA)
    fpr=(1+.85*(Tfan/d['T01']-1))**3.5
    nc=nozzle(Tfan,d['p01']*fpr,p,hot=False)
    Ac=mc/nc['flux']; Fc=mc*(nc['Ve']-V)+Ac*(nc['pe']-p)
    out['01']=dict(**d,mc=mc,Tfan=Tfan,FPR=fpr,cold_nozzle=nc,Ac=Ac,Fcold=Fc,Ftotal=Fc+d['F'])
    # 02 aft fan ramjet, fuel neglected as specifically instructed.
    s=supersonic(1.7,50); V=s['V']; T01=s['T0']; p01=s['p01']
    Tf,pf=compressor(T01,p01,1.8,.85); nc=nozzle(Tf,pf,ATM[20][1],hot=False)
    mc=.5*nc['flux']; mh=mc/3
    Th,ph=turbine_work(1900,.96*p01,3*CA*(Tf-T01))
    j=jet(Th,ph,ATM[20][1],mh,0,V)
    Fc=mc*(nc['Ve']-V)+.5*(nc['pe']-ATM[20][1])
    out['02']=dict(**s,Tfan=Tf,pfan=pf,cold_nozzle=nc,mc=mc,mh=mh,Tturb=Th,pturb=ph,Fcold=Fc,Ftotal=Fc+j['F'],hot_nozzle=j)
    out['03']=turboprop(7,.6*ATM[7][3],.2,12,f=.02)
    # 04: aide Table 5 has a direct 6500 m row; do not interpolate 6/7 km.
    T,p,rho,a=ATM[6.5]
    V=.398*a; ma=rho*V*pi*.3**2/4; Ve=950/3.6
    me=p/(250*(250+273.15))*Ve*pi*.285**2/4
    f=(me-ma)/ma; F=me*Ve-ma*V
    out['04']=dict(T=T,p=p,rho=rho,a=a,V=V,ma=ma,me=me,f=f,F=F,TSFC=3600*(me-ma)/F,ram_percent=100*ma*V/(me*Ve))
    # 05 ideal equal-cp air-standard turbojet; converging nozzle.
    out['05']=[]
    for alt,M in [(10,.8),(5,.4)]:
        T,p,rho,a=ATM[alt]; V=M*a; T01,p01=intake(T,p,V,1)
        T02,p02=compressor(T01,p01,20,1); T04=1400-(T02-T01)
        p04=p02*(T04/1400)**3.5
        n=nozzle(T04,p04,p,1,hot=False); A=1/n['flux']
        F=n['Ve']-V+A*(n['pe']-p); f=CA*(1400-T02)/LHV
        Ve_cd=sqrt(2*CA*T04*(1-(p/p04)**((GA-1)/GA)))
        out['05'].append(dict(alt=alt,M=M,V=V,T01=T01,p01=p01,T02=T02,p02=p02,T04=T04,p04=p04,f=f,Fs=F,TSFC=3600*f/F,nozzle=n,Ve_cd=Ve_cd,Fs_cd=Ve_cd-V,TSFC_cd=3600*f/(Ve_cd-V)))
    d=turbojet(); out['06']=d
    fr=fuel(d['T04'],2000,cpin=CG); ft=d['f']+(1+d['f'])*fr
    j=jet(2000,.97*d['p04'],ATM[7][1],15,ft,260)
    out['07']=dict(fr=fr,ft=ft,**j,increase_A=100*(j['A']/d['A']-1),increase_F=100*(j['F']/d['F']-1),increase_fuel=100*(ft/d['f']-1),increase_TSFC=100*(j['TSFC']/d['TSFC']-1))
    out['08']=turboprop(5,125,.1,8,T03=1200,ec=.87,ei=.93,loss=.04,gear=.90,prop=.85,single=True)
    out['09']=turboprop(0,75*1.85/3.6,.2,10,f=.015,reheat=.005,pnpr=1.2,gear=.85,prop=.85)
    # 10 fan processes all air, OPR includes fan.
    T,p,rho,a=ATM[10]; V=.8*a; T01,p01=intake(T,p,V)
    Tf,pf=compressor(T01,p01,1.7,.9); T02,p02=compressor(Tf,pf,20/1.7,.9)
    f=fuel(T02,1300); Th,ph=turbine_work(1300,.96*p02,CA*(T02-Tf)/(.99*(1+f)))
    Tl,pl=turbine_work(Th,ph,5*CA*(Tf-T01)/(.99*(1+f)))
    nc=nozzle(Tf,pf,p,hot=False); mc=.8*nc['flux']; mh=mc/4
    j=jet(Tl,pl,p,mh,f,V); Fc=mc*(nc['Ve']-V)+.8*(nc['pe']-p)
    F=Fc+j['F']
    out['10']=dict(T01=T01,p01=p01,Tfan=Tf,pfan=pf,T02=T02,p02=p02,f=f,THP=Th,pHP=ph,TLP=Tl,pLP=pl,cold_nozzle=nc,mc=mc,mh=mh,hot_nozzle=j,Fcold=Fc,Ftotal=F,TSFC=3600000*mh*f/F)
    for ID,cd in [('11',False),('12',True)]:
        s=supersonic(1.75); f=fuel(s['T0'],2200,eta=1)
        j=jet(2200,.99*s['p01'],ATM[20][1],1,f,s['V'],eta=1 if cd else .95,cd=cd)
        out[ID]=dict(**s,f=f,**j)
    out['12_endpoints']=[]
    for M in [1,5]:
        s=supersonic(M); p03=.99*s['p01']; pe=ATM[20][1]
        Me=sqrt(2/(GG-1)*((p03/pe)**((GG-1)/GG)-1))
        ratio=1/Me*(2/(GG+1)*(1+(GG-1)/2*Me**2))**((GG+1)/(2*(GG-1)))
        out['12_endpoints'].append(dict(M=M,p03=p03,T03=2200,Me=Me,A_ratio=ratio))
    s=supersonic(2.5,30,eta=.95); T03=burner(s['T0'],.03,eta=.95,lhv=DECANE_LHV)
    out['13']=dict(**s,T03=T03,**jet(T03,.95*s['p01'],ATM[20][1],1,.03,s['V'],eta=.95,cd=True))
    return out

def check(out):
    # Regression against the rounded results printed in the worked answers.
    expected = {
        '01': {'Ftotal':44876.11, 'FPR':2.109955, 'shaft':17492291.68},
        '02': {'Ftotal':9436.412, 'mc':43.88593, 'theta':11.895627},
        '03': {'TP':4930200.62, 'fuel_lph':2005.6476},
        # Q04: direct aide Table 5 6.5 km row replaces 6/7 km interpolation.
        '04': {'f':.02741461, 'F':805.49790, 'TSFC':.67593574, 'ram_percent':46.14670},
        '06': {'A':.06434261, 'F':8871.536, 'TSFC':123.66945},
        '07': {'A':.09599607, 'F':14464.629, 'increase_A':49.19517,
               'increase_F':63.04537, 'increase_fuel':141.73709, 'increase_TSFC':48.26370},
        '08': {'TP':1817566.13, 'shaft':1849319.60},
        '09': {'TP':1382637.97, 'Tr':1011.5161},
        '10': {'Ftotal':29207.34, 'TSFC':73.79371},
        '11': {'F':751.53492, 'TSFC':249.58578},
        '12': {'F':794.00332, 'TSFC':236.23633},
        # Q28B: aide Table 11 decane LHV replaces the former Jet A1 surrogate.
        '13': {'T03':1534.06002, 'F':512.20023},
    }
    for ID, values in expected.items():
        for key, value in values.items():
            assert abs(out[ID][key]-value) <= max(1e-7,abs(value)*2e-6), (ID,key)
    for x, fs, fs_cd, tsfc, tsfc_cd in zip(
            out['05'],[711.28659,784.52341],[794.45374,840.11069],
            [.0953114,.0833607],[.0853338,.0778450]):
        assert abs(x['Fs']-fs)<1e-4
        assert abs(x['Fs_cd']-fs_cd)<1e-4
        assert abs(x['TSFC']-tsfc)<5e-8
        assert abs(x['TSFC_cd']-tsfc_cd)<5e-8
    assert abs(2*out['03']['fuel_lph']-4011.2952)<.001
    # Independent mass, energy and work identities (not just result fixtures).
    for ID in ['01','03','08','09']:
        d=out[ID]
        assert abs((1+d['f'])*CG*(d['T03']-TR)-CA*(d['T02']-TR)-d['f']*.98*LHV)<1e-7
    d=out['01']
    assert abs(d['shaft']-d['mc']*CA*(d['Tfan']-d['T01']))<1e-6
    d=out['04']
    assert (d['T'],d['p'],d['rho'],d['a'])==(245.9,44034.8461,.6238,314.3579)
    assert abs(d['me']-d['ma']*(1+d['f']))<1e-12
    d=out['13']
    # Independent burner balance must use decane, not the default Jet A1 LHV.
    released=(1.03*CG*(d['T03']-TR)-CA*(d['T0']-TR))/(.03*.95)
    assert abs(released-44602000.)<1e-7
    assert abs(released-LHV)>1e6
    for ID in ['06','07','11']:
        d=out[ID]
        assert d['choked'] and d['pressure_thrust']>0
        assert abs(d['Ve']/sqrt(GG*R*d['Te'])-1)<1e-12
    for ID in ['12','13']:
        assert out[ID]['pe']==ATM[20][1] and out[ID]['pressure_thrust']==0
    for key in ['increase_A','increase_F','increase_fuel','increase_TSFC']:
        assert out['07'][key]>0
    assert abs((1+out['07']['increase_fuel']/100)/(1+out['07']['increase_F']/100)
               -(1+out['07']['increase_TSFC']/100))<1e-12
    first,last=out['12_endpoints']
    for endpoint, pressure in [(first,9963.78),(last,175955.84)]:
        assert endpoint['T03']==2200 and abs(endpoint['p03']-pressure)<.01
    assert first['Me']<1 and 1<first['A_ratio']<1.001
    assert abs(last['A_ratio']-4.220366)<1e-6
    original=nozzle(2200,first['p03'],ATM[20][1])
    assert not original['choked']
    alternate=turboprop(0,75*1.85/3.6,.2,10,f=.015,reheat=.005/1.015,pnpr=1.2,gear=.85,prop=.85)
    assert abs(alternate['TP']-1379012.32)<.01
    # Preserve every question's numerical conditions, including source tables/marks.
    # Source metadata is excluded so PDF page numbers do not mask lost givens.
    question_numbers = {
        1: '3 0.8 10,000 30 15 3 1.2 1.005 0.02 1.4 1.148 85 1.333 90 0.287 95 2.5 95 0.5 99 1 98',
        2: '3 1.7 20,000 50 35 1.8 4 1900 1.005 1.4 85 1.148 90 1.333 95 0.287 95 0.5 98 1 3',
        3: '3 2 30 5 35 12 1.005 0.02 1.4 1.148 85 1.333 90 0.287 95 0.2 95 85 99 1 98 7000 3 0.6 1.3 80',
        4: '6500 0.398 0.300 0.285 950 250 250 850',
        5: '20 1400 1 0.8 10,000 0.4 5000',
        6: '1 9.0 1.005 1250 1.4 1.148 87 1.333 87 0.287 95 15 95 260 99 7000 98 6',
        7: '2000 1 3 98 9.0 1.005 1250 1.4 1.148 87 1.333 87 0.287 95 15 95 260 99 7000 98 6',
        8: '85 1.3 8.0 4 1200 1.005 1.4 87 1.148 90 1.333 93 0.287 95 0.1 99 5000 98 125 90 1',
        9: '0.005 75 85 10 1.005 0.015 1.4 1.148 85 1.333 90 0.287 95 0.2 95 0.005 99 98 98 2 3 85 1.2 1',
        10: '1 20.0 1.005 1300 1.4 1.7 1.148 90 1.333 95 0.287 95 0.8 99 10,000 98 0.8 4 4',
        11: '1.75 20,000 2200 1 1 100 1.148 1.333 1 95 95',
        12: '20,000 2200 1 100 1 1.148 1.333 1 95 95 1 1 1 9.96378 5 175.95584 1.75 1 5 1 5',
        13: '10 22 0.03 30 95 5 1 1.148 1.333 95 2.5 20,000',
    }
    # Check every paired document and every local Markdown link, without writes.
    from pathlib import Path
    import re
    from urllib.parse import unquote
    root=Path(__file__).resolve().parent
    for kind in ['question','answer']:
        assert len(list(root.glob(kind+'_*.md')))==13
        for i in range(1,14):
            path=root/f'{kind}_{i:02d}.md'
            text=path.read_text()
            assert '\\boxed' not in text
            assert 'Source:' in text if kind=='question' else 'Verification:' in text or 'verify.py' in text
            if kind=='question':
                body=text.split('## Question\n\n',1)[1]
                assert len(re.findall(r'^#+ ',text,re.M))==2, path
                assert not re.search(
                    r'\bprovided\b|\bgivens?\b|\baide\b|\bcheat\s*sheet\b|\blecture\b|'
                    r'look[ -]?up|refer to|consult|interpolat|trial|\bhint\b|adaptation|'
                    r'\bCohen\b|\bTable\s+\d|#page=|supplement|'
                    r'(?:source|printed|official) answer|worked (?:formula|example)',
                    text,re.I), path
                assert all(token not in body for token in [r'\[',r'\(', '$', '0.020317']), path
                numbers=' '.join(re.findall(r'[0-9]+(?:[.,][0-9]+)*',body))
                assert numbers==question_numbers[i], (path,'numeric conditions changed')
                if i<=3:
                    marks={1:'[30 Marks]',2:'[35 Marks]',3:'[30+5=35 Marks]'}
                    assert marks[i] in body, (path,'exam marks')
                    assert len(body.strip().split('\n\n'))==2, (path,'appended exam assumptions')
                for part in {3:['(a)','(b)'],4:['(a)','(b)','(c)'],
                             5:['(i)','(ii)'],7:['(i)','(ii)','(iii)']}.get(i,[]):
                    assert part in body, (path,part)
                if i in [1,2,3,4,6,7,8,9,10,12]:
                    assert '| Quantity |' in body or '| Flight Mach |' in body, path
                if i==7:
                    # Q22 must not depend on opening Q21; retain its complete engine table.
                    base=(root/'question_06.md').read_text()
                    rows=[line for line in base.splitlines() if line.startswith('|')]
                    assert all(line.replace('Engine Mass Flow','Engine air Mass Flow') in body
                               for line in rows), path
                    assert body.index('| Quantity |')<body.index('Calculate:'), path
                if i in [6,7,11,12,13]:
                    assert 'constant-property combustion model' in body, path
                if i in [11,12,13]:
                    assert '1.148' in body and '1.333' in body, path
                if i==12:
                    assert 'Mach 1.75' in body and 'Mach 1 and Mach 5' in body
                    assert 'fixed or variable nozzle geometry' in body
                if i==13:
                    assert '44602' not in body and '44.602' not in body  # Student finds decane LHV.
            if kind=='answer' and i in [2,13]:
                assert '**downstream** normal component' in text
                assert 'S2%20Err.PDF' in text
            if i==13:
                if kind=='answer':
                    assert 'Table 11' in text and '../../MAE3405%20Aide%20Memoire.pdf#page=5' in text
                    assert '44602' in text
                assert '1497.85776' not in text and '497.36458' not in text
            for link in re.findall(r'\]\(([^)]+)\)',text):
                assert (path.parent/unquote(link.split('#')[0])).exists(), (path,link)
    manifest=(root/'manifest.md').read_text()
    assert len(re.findall(r'^\| \d{2} \|',manifest,re.M))==13
    assert '512.2' not in manifest and '805.5' not in manifest  # Keep the index spoiler-free.
    for link in re.findall(r'\]\(([^)]+)\)',manifest):
        assert (root/unquote(link.split('#')[0])).exists(), link

if __name__=='__main__':
    out=calculations()
    check(out)
    print('PASS: 13 question/answer pairs; numeric regressions, balances, choking, question conditions/marks, no supplements/lookups, and local links.')
    print(json.dumps(out,indent=2))
