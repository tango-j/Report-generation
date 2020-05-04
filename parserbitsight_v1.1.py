import xml.etree.ElementTree as ET
import glob
import xlwt

wbk = xlwt.Workbook()

sheet = wbk.add_sheet('report')
sheet.write(0,0,'IP Address')
sheet.write(0,1,'User Agent')
sheet.write(0,2,'infection')
sheet.write(0,3,'risktype')
sheet.write(0,4,'Service')

row = 1 #counter for rows

filename = (glob.glob("*.xml"))

for i in filename:
    #print i
    root = ET.parse(i).getroot()
    hostip = root.findall(".//host_ip")
    useragent = root.findall(".//user_agent")
    infection = root.findall(".//infection")
    risktype = root.findall(".//risk_type")
    listitem = root.findall(".//list-item")
    for a in hostip:
        ip = str(a.text)
        #print ip
        sheet.write(row,0,ip)
        break
    for b in useragent:
        ua = str(b.text)
        #print ua
        sheet.write(row,1,ua)
        break

    for c in infection:
        infec = str(c.text)
        #print infec
        sheet.write(row,2,infec)
        break

    for d in risktype:
        risk = str(d.text)
        #print risk
        sheet.write(row,3,risk)
        break
    if "open_ports" in str(risk):
        #print risk
        for e in listitem:
            #print e.text
            if str(e.text) != "None":
                #print str(ip) +" and "+ str(e.text)
                item = str(e.text)
                sheet.write(row,4,item)
                break

            
    row = row + 1

wbk.save('Cyber-hygiene report.xls')
print "                     "
print "###################Cyber-hygiene Report saved Successfully#################################"

