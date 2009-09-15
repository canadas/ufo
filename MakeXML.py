from math import *
def convertFlux(flux100,emin,emax,idx):
    flux_emin= flux100*(pow(emin,-idx+1)-pow(emax,-idx+1))/(pow(100.0,-idx+1))
    if (idx<1):
        flux_emin=-flux_emin
    print flux100 , flux_emin
    return 1e4 *flux_emin

fin=file('gll_psc11month_v1b.txt','r')
fout=file('source11mnth.xml','w')
lines=fin.readlines()
txt= "<source_library title=\"ElevenMonthSourceLib\">"
print txt
fout.writelines(txt)
s=[]
EMIN=20
EMAX=600000
for line in lines:
    pars=line.split()
    try:
        name     = pars[2]
        name=name.replace('+','p')
        name=name.replace('-','m')
        ra       = float(pars[3])
        dec      = float(pars[4])
        flux     = float(pars[12])
        index    = float(pars[16])
        s.append(name)
        txt='''
    <source flux="%.7f" name="%s"> 
    \t<spectrum escale="MeV">
    \t\t<particle name="gamma">
    \t\t\t<power_law emin="%.2f" emax="%.2f" gamma="%.2f" />
    \t\t</particle>
    \t\t<celestial_dir ra="%.3f" dec="%.3f" />
    \t</spectrum> 
    </source>''' %(convertFlux(flux,EMIN,EMAX,index),name,EMIN,EMAX,index,ra,dec)
        print txt
        fout.writelines(txt)
    except:
        pass
    pass
    
txt= "\n\n\n<source name=\"ElevenMonthsSources\">\n"
print txt
fout.writelines(txt)

print 'there are %s sources' %(len(s))
for so in s:
    txt="    <nestedSource sourceRef=\"%s\" />\n" % so
    # print txt
    fout.writelines(txt)
    pass

txt='''
\t</source>
</source_library>'''
print txt
fout.writelines(txt)

