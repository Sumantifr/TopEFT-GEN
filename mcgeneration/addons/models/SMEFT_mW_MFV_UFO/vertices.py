# This file was automatically created by FeynRules 2.3.24
# Mathematica version: 10.2.0 for Mac OS X x86 (64-bit) (July 29, 2015)
# Date: Mon 5 Feb 2018 20:17:34


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1, L.SSSS2 ],
             couplings = {(0,0):C.GC_1916,(0,1):C.GC_74})

V_2 = Vertex(name = 'V_2',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_1550})

V_3 = Vertex(name = 'V_3',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_1918})

V_4 = Vertex(name = 'V_4',
             particles = [ P.H, P.H, P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSSSS1 ],
             couplings = {(0,0):C.GC_763})

V_5 = Vertex(name = 'V_5',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1, L.SSS2 ],
             couplings = {(0,0):C.GC_1551,(0,1):C.GC_1817})

V_6 = Vertex(name = 'V_6',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_2015})

V_7 = Vertex(name = 'V_7',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_1777})

V_8 = Vertex(name = 'V_8',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_2017})

V_9 = Vertex(name = 'V_9',
             particles = [ P.H, P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSSS1 ],
             couplings = {(0,0):C.GC_1711})

V_10 = Vertex(name = 'V_10',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS2 ],
              couplings = {(0,1):C.GC_1704,(0,0):C.GC_1697})

V_11 = Vertex(name = 'V_11',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS2 ],
              couplings = {(0,1):C.GC_1911,(0,0):C.GC_1907})

V_12 = Vertex(name = 'V_12',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_1909})

V_13 = Vertex(name = 'V_13',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_2019})

V_14 = Vertex(name = 'V_14',
              particles = [ P.a, P.a, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS2 ],
              couplings = {(0,1):C.GC_1699,(0,0):C.GC_1693})

V_15 = Vertex(name = 'V_15',
              particles = [ P.a, P.a, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_1696})

V_16 = Vertex(name = 'V_16',
              particles = [ P.a, P.a, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_2011})

V_17 = Vertex(name = 'V_17',
              particles = [ P.a, P.a, P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSSSS1 ],
              couplings = {(0,0):C.GC_1703})

V_18 = Vertex(name = 'V_18',
              particles = [ P.a, P.a, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSSS1 ],
              couplings = {(0,0):C.GC_1915})

V_19 = Vertex(name = 'V_19',
              particles = [ P.g, P.g, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_1706})

V_20 = Vertex(name = 'V_20',
              particles = [ P.g, P.g, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVS2 ],
              couplings = {(0,0):C.GC_1712})

V_21 = Vertex(name = 'V_21',
              particles = [ P.g, P.g, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVSS2 ],
              couplings = {(0,0):C.GC_764})

V_22 = Vertex(name = 'V_22',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS2 ],
              couplings = {(0,1):C.GC_765,(0,0):C.GC_34})

V_23 = Vertex(name = 'V_23',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_37})

V_24 = Vertex(name = 'V_24',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_1917})

V_25 = Vertex(name = 'V_25',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS2 ],
              couplings = {(0,1):C.GC_1713,(0,0):C.GC_40})

V_26 = Vertex(name = 'V_26',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_1709})

V_27 = Vertex(name = 'V_27',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_1710})

V_28 = Vertex(name = 'V_28',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_2016})

V_29 = Vertex(name = 'V_29',
              particles = [ P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVV2, L.VVV3, L.VVV4 ],
              couplings = {(0,2):C.GC_1564,(0,0):C.GC_1995,(0,1):C.GC_1797})

V_30 = Vertex(name = 'V_30',
              particles = [ P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVV2 ],
              couplings = {(0,0):C.GC_1556})

V_31 = Vertex(name = 'V_31',
              particles = [ P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVV2 ],
              couplings = {(0,0):C.GC_1561})

V_32 = Vertex(name = 'V_32',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS2 ],
              couplings = {(0,1):C.GC_1705,(0,0):C.GC_1695})

V_33 = Vertex(name = 'V_33',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS2 ],
              couplings = {(0,1):C.GC_1912,(0,0):C.GC_1906})

V_34 = Vertex(name = 'V_34',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_1908})

V_35 = Vertex(name = 'V_35',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_2020})

V_36 = Vertex(name = 'V_36',
              particles = [ P.a, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS2 ],
              couplings = {(0,1):C.GC_1700,(0,0):C.GC_1692})

V_37 = Vertex(name = 'V_37',
              particles = [ P.a, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_1694})

V_38 = Vertex(name = 'V_38',
              particles = [ P.a, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_2013})

V_39 = Vertex(name = 'V_39',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS2 ],
              couplings = {(0,1):C.GC_1698,(0,0):C.GC_2010})

V_40 = Vertex(name = 'V_40',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_1689})

V_41 = Vertex(name = 'V_41',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_1690})

V_42 = Vertex(name = 'V_42',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS2 ],
              couplings = {(0,1):C.GC_1910,(0,0):C.GC_1691})

V_43 = Vertex(name = 'V_43',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_2018})

V_44 = Vertex(name = 'V_44',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_1904})

V_45 = Vertex(name = 'V_45',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_1905})

V_46 = Vertex(name = 'V_46',
              particles = [ P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVV1, L.VVV2, L.VVV4 ],
              couplings = {(0,2):C.GC_1134,(0,1):C.GC_15,(0,0):C.GC_1816})

V_47 = Vertex(name = 'V_47',
              particles = [ P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVV2 ],
              couplings = {(0,0):C.GC_33})

V_48 = Vertex(name = 'V_48',
              particles = [ P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVV2 ],
              couplings = {(0,0):C.GC_2008})

V_49 = Vertex(name = 'V_49',
              particles = [ P.g, P.g, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV2, L.VVV4 ],
              couplings = {(0,1):C.GC_762,(0,0):C.GC_17})

V_50 = Vertex(name = 'V_50',
              particles = [ P.ghG, P.ghG__tilde__, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_17})

V_51 = Vertex(name = 'V_51',
              particles = [ P.g, P.g, P.g, P.H, P.H ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVSS3 ],
              couplings = {(0,0):C.GC_1136})

V_52 = Vertex(name = 'V_52',
              particles = [ P.g, P.g, P.g, P.H ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVS3 ],
              couplings = {(0,0):C.GC_1707})

V_53 = Vertex(name = 'V_53',
              particles = [ P.g, P.g, P.g, P.H ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVS3 ],
              couplings = {(0,0):C.GC_1714})

V_54 = Vertex(name = 'V_54',
              particles = [ P.g, P.g, P.g, P.g, P.H, P.H ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVVSS1, L.VVVVSS3, L.VVVVSS4 ],
              couplings = {(1,1):C.GC_1139,(0,0):C.GC_1139,(2,2):C.GC_1139})

V_55 = Vertex(name = 'V_55',
              particles = [ P.g, P.g, P.g, P.g, P.H ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVVS1, L.VVVVS3, L.VVVVS4 ],
              couplings = {(1,1):C.GC_1708,(0,0):C.GC_1708,(2,2):C.GC_1708})

V_56 = Vertex(name = 'V_56',
              particles = [ P.g, P.g, P.g, P.g, P.H ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVVS1, L.VVVVS3, L.VVVVS4 ],
              couplings = {(1,1):C.GC_1715,(0,0):C.GC_1715,(2,2):C.GC_1715})

V_57 = Vertex(name = 'V_57',
              particles = [ P.g, P.g, P.g, P.g ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV2, L.VVVV4, L.VVVV5, L.VVVV7, L.VVVV8 ],
              couplings = {(0,1):C.GC_1135,(1,5):C.GC_1135,(2,4):C.GC_1135,(1,2):C.GC_18,(0,0):C.GC_18,(2,3):C.GC_18})

V_58 = Vertex(name = 'V_58',
              particles = [ P.g, P.g, P.g, P.g, P.g ],
              color = [ 'f(-2,1,2)*f(-1,-2,3)*f(4,5,-1)', 'f(-2,1,2)*f(-1,-2,4)*f(3,5,-1)', 'f(-2,1,2)*f(-1,-2,5)*f(3,4,-1)', 'f(-2,1,3)*f(-1,-2,2)*f(4,5,-1)', 'f(-2,1,3)*f(-1,-2,4)*f(2,5,-1)', 'f(-2,1,3)*f(-1,-2,5)*f(2,4,-1)', 'f(-2,1,4)*f(-1,-2,2)*f(3,5,-1)', 'f(-2,1,4)*f(-1,-2,3)*f(2,5,-1)', 'f(-2,1,4)*f(-1,-2,5)*f(2,3,-1)', 'f(-2,1,5)*f(-1,-2,2)*f(3,4,-1)', 'f(-2,1,5)*f(-1,-2,3)*f(2,4,-1)', 'f(-2,1,5)*f(-1,-2,4)*f(2,3,-1)', 'f(-2,2,3)*f(-1,-2,1)*f(4,5,-1)', 'f(-2,2,3)*f(-1,-2,4)*f(1,5,-1)', 'f(-2,2,3)*f(-1,-2,5)*f(1,4,-1)', 'f(-2,2,4)*f(-1,-2,1)*f(3,5,-1)', 'f(-2,2,4)*f(-1,-2,3)*f(1,5,-1)', 'f(-2,2,4)*f(-1,-2,5)*f(1,3,-1)', 'f(-2,2,5)*f(-1,-2,1)*f(3,4,-1)', 'f(-2,2,5)*f(-1,-2,3)*f(1,4,-1)', 'f(-2,2,5)*f(-1,-2,4)*f(1,3,-1)', 'f(-2,3,4)*f(-1,-2,1)*f(2,5,-1)', 'f(-2,3,4)*f(-1,-2,2)*f(1,5,-1)', 'f(-2,3,4)*f(-1,-2,5)*f(1,2,-1)', 'f(-2,3,5)*f(-1,-2,1)*f(2,4,-1)', 'f(-2,3,5)*f(-1,-2,2)*f(1,4,-1)', 'f(-2,3,5)*f(-1,-2,4)*f(1,2,-1)', 'f(-2,4,5)*f(-1,-2,1)*f(2,3,-1)', 'f(-2,4,5)*f(-1,-2,2)*f(1,3,-1)', 'f(-2,4,5)*f(-1,-2,3)*f(1,2,-1)' ],
              lorentz = [ L.VVVVV1, L.VVVVV10, L.VVVVV11, L.VVVVV12, L.VVVVV13, L.VVVVV14, L.VVVVV15, L.VVVVV17, L.VVVVV18, L.VVVVV2, L.VVVVV4, L.VVVVV5, L.VVVVV6, L.VVVVV7, L.VVVVV8 ],
              couplings = {(24,11):C.GC_1138,(21,12):C.GC_1137,(18,12):C.GC_1138,(15,11):C.GC_1137,(28,9):C.GC_1138,(22,2):C.GC_1138,(9,2):C.GC_1137,(3,9):C.GC_1137,(29,10):C.GC_1138,(16,3):C.GC_1138,(10,3):C.GC_1137,(0,10):C.GC_1137,(26,6):C.GC_1137,(20,5):C.GC_1137,(4,5):C.GC_1138,(1,6):C.GC_1138,(25,1):C.GC_1138,(6,1):C.GC_1137,(19,4):C.GC_1138,(7,4):C.GC_1137,(23,8):C.GC_1137,(17,7):C.GC_1137,(5,7):C.GC_1138,(2,8):C.GC_1138,(27,0):C.GC_1138,(12,0):C.GC_1137,(13,13):C.GC_1138,(11,13):C.GC_1137,(14,14):C.GC_1137,(8,14):C.GC_1138})

V_59 = Vertex(name = 'V_59',
              particles = [ P.g, P.g, P.g, P.g, P.g, P.g ],
              color = [ 'f(-3,1,2)*f(-2,3,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,2)*f(-2,3,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,2)*f(-2,3,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,2)*f(-2,4,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,2)*f(-2,4,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,2)*f(-2,5,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,3)*f(-2,2,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,3)*f(-2,2,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,3)*f(-2,2,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,3)*f(-2,4,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,3)*f(-2,4,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,3)*f(-2,5,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,4)*f(-2,2,3)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,4)*f(-2,2,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,4)*f(-2,2,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,4)*f(-2,3,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,4)*f(-2,3,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,4)*f(-2,5,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,1,5)*f(-2,2,3)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,5)*f(-2,2,4)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,5)*f(-2,2,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,5)*f(-2,3,4)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,5)*f(-2,3,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,5)*f(-2,4,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,1,6)*f(-2,2,3)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,6)*f(-2,2,4)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,6)*f(-2,2,5)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,6)*f(-2,3,4)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,6)*f(-2,3,5)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,6)*f(-2,4,5)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,2,3)*f(-2,1,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,2,3)*f(-2,1,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,2,3)*f(-2,1,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,2,3)*f(-2,4,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,3)*f(-2,4,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,3)*f(-2,5,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,4)*f(-2,1,3)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,2,4)*f(-2,1,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,2,4)*f(-2,1,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,2,4)*f(-2,3,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,4)*f(-2,3,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,4)*f(-2,5,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,2,5)*f(-2,1,3)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,2,5)*f(-2,1,4)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,2,5)*f(-2,1,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,2,5)*f(-2,3,4)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,5)*f(-2,3,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,5)*f(-2,4,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,2,6)*f(-2,1,3)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,2,6)*f(-2,1,4)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,2,6)*f(-2,1,5)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,2,6)*f(-2,3,4)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,6)*f(-2,3,5)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,6)*f(-2,4,5)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,3,4)*f(-2,1,2)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,3,4)*f(-2,1,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,3,4)*f(-2,1,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,3,4)*f(-2,2,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,3,4)*f(-2,2,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,3,4)*f(-2,5,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,3,5)*f(-2,1,2)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,3,5)*f(-2,1,4)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,3,5)*f(-2,1,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,3,5)*f(-2,2,4)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,3,5)*f(-2,2,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,3,5)*f(-2,4,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,3,6)*f(-2,1,2)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,3,6)*f(-2,1,4)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,3,6)*f(-2,1,5)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,3,6)*f(-2,2,4)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,3,6)*f(-2,2,5)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,3,6)*f(-2,4,5)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,4,5)*f(-2,1,2)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,4,5)*f(-2,1,3)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,4,5)*f(-2,1,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,4,5)*f(-2,2,3)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,4,5)*f(-2,2,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,4,5)*f(-2,3,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,4,6)*f(-2,1,2)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,4,6)*f(-2,1,3)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,4,6)*f(-2,1,5)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,4,6)*f(-2,2,3)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,4,6)*f(-2,2,5)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,4,6)*f(-2,3,5)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,5,6)*f(-2,1,2)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,5,6)*f(-2,1,3)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,5,6)*f(-2,1,4)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,5,6)*f(-2,2,3)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,5,6)*f(-2,2,4)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,5,6)*f(-2,3,4)*f(-1,-2,-3)*f(1,2,-1)' ],
              lorentz = [ L.VVVVVV1, L.VVVVVV10, L.VVVVVV11, L.VVVVVV12, L.VVVVVV13, L.VVVVVV14, L.VVVVVV15, L.VVVVVV16, L.VVVVVV2, L.VVVVVV3, L.VVVVVV4, L.VVVVVV5, L.VVVVVV6, L.VVVVVV7, L.VVVVVV9 ],
              couplings = {(65,10):C.GC_1140,(71,12):C.GC_1141,(77,12):C.GC_1140,(83,10):C.GC_1141,(41,8):C.GC_1140,(53,2):C.GC_1140,(76,2):C.GC_1141,(88,8):C.GC_1141,(35,9):C.GC_1140,(52,5):C.GC_1140,(64,5):C.GC_1141,(87,9):C.GC_1141,(34,4):C.GC_1141,(40,3):C.GC_1141,(69,3):C.GC_1140,(81,4):C.GC_1140,(17,9):C.GC_1141,(23,4):C.GC_1140,(80,4):C.GC_1141,(86,9):C.GC_1140,(11,8):C.GC_1141,(22,3):C.GC_1140,(68,3):C.GC_1141,(85,8):C.GC_1140,(9,2):C.GC_1141,(15,5):C.GC_1141,(61,5):C.GC_1140,(73,2):C.GC_1140,(4,10):C.GC_1141,(14,5):C.GC_1140,(49,5):C.GC_1141,(78,10):C.GC_1140,(3,12):C.GC_1140,(19,3):C.GC_1141,(37,3):C.GC_1140,(72,12):C.GC_1141,(2,12):C.GC_1141,(8,2):C.GC_1140,(48,2):C.GC_1141,(66,12):C.GC_1140,(1,10):C.GC_1140,(18,4):C.GC_1141,(31,4):C.GC_1140,(60,10):C.GC_1141,(6,8):C.GC_1140,(12,9):C.GC_1140,(30,9):C.GC_1141,(36,8):C.GC_1141,(47,14):C.GC_1140,(82,14):C.GC_1141,(46,6):C.GC_1140,(70,6):C.GC_1141,(33,7):C.GC_1141,(39,1):C.GC_1141,(63,1):C.GC_1140,(75,7):C.GC_1140,(29,7):C.GC_1140,(74,7):C.GC_1141,(28,1):C.GC_1140,(62,1):C.GC_1141,(10,14):C.GC_1141,(16,6):C.GC_1141,(67,6):C.GC_1140,(79,14):C.GC_1140,(25,1):C.GC_1141,(38,1):C.GC_1140,(13,6):C.GC_1140,(43,6):C.GC_1141,(24,7):C.GC_1141,(32,7):C.GC_1140,(7,14):C.GC_1140,(42,14):C.GC_1141,(59,0):C.GC_1140,(89,0):C.GC_1141,(51,11):C.GC_1140,(58,11):C.GC_1141,(21,11):C.GC_1141,(55,11):C.GC_1140,(5,0):C.GC_1141,(20,11):C.GC_1140,(50,11):C.GC_1141,(84,0):C.GC_1140,(0,0):C.GC_1140,(54,0):C.GC_1141,(45,13):C.GC_1141,(57,13):C.GC_1140,(27,13):C.GC_1140,(56,13):C.GC_1141,(26,13):C.GC_1141,(44,13):C.GC_1140})

V_60 = Vertex(name = 'V_60',
              particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF5, L.FFFF6 ],
              couplings = {(0,5):C.GC_621,(1,3):C.GC_198,(1,4):C.GC_1156,(1,2):C.GC_834,(2,2):C.GC_879,(1,0):C.GC_1157,(2,0):C.GC_1238,(1,1):C.GC_1041,(2,1):C.GC_1086})

V_61 = Vertex(name = 'V_61',
              particles = [ P.c__tilde__, P.d, P.d__tilde__, P.u ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
              couplings = {(1,3):C.GC_199,(0,4):C.GC_622,(1,2):C.GC_843,(2,2):C.GC_888,(1,0):C.GC_1158,(2,0):C.GC_1239,(1,1):C.GC_1050,(2,1):C.GC_1095})

V_62 = Vertex(name = 'V_62',
              particles = [ P.t__tilde__, P.d, P.d__tilde__, P.u ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
              couplings = {(1,3):C.GC_200,(0,4):C.GC_623,(1,2):C.GC_846,(2,2):C.GC_891,(1,0):C.GC_1159,(2,0):C.GC_1240,(1,1):C.GC_1053,(2,1):C.GC_1098})

V_63 = Vertex(name = 'V_63',
              particles = [ P.u__tilde__, P.d, P.d__tilde__, P.c ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
              couplings = {(1,3):C.GC_201,(0,4):C.GC_624,(1,2):C.GC_849,(2,2):C.GC_894,(1,0):C.GC_1160,(2,0):C.GC_1241,(1,1):C.GC_1056,(2,1):C.GC_1101})

V_64 = Vertex(name = 'V_64',
              particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF5, L.FFFF6 ],
              couplings = {(1,3):C.GC_202,(0,5):C.GC_625,(1,4):C.GC_1154,(1,2):C.GC_852,(2,2):C.GC_897,(1,0):C.GC_1161,(2,0):C.GC_1242,(1,1):C.GC_1059,(2,1):C.GC_1104})

V_65 = Vertex(name = 'V_65',
              particles = [ P.t__tilde__, P.d, P.d__tilde__, P.c ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
              couplings = {(1,3):C.GC_203,(0,4):C.GC_626,(1,2):C.GC_861,(2,2):C.GC_906,(1,0):C.GC_1162,(2,0):C.GC_1243,(1,1):C.GC_1068,(2,1):C.GC_1113})

V_66 = Vertex(name = 'V_66',
              particles = [ P.u__tilde__, P.d, P.d__tilde__, P.t ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
              couplings = {(1,3):C.GC_204,(0,4):C.GC_627,(1,2):C.GC_864,(2,2):C.GC_909,(1,0):C.GC_1163,(2,0):C.GC_1244,(1,1):C.GC_1071,(2,1):C.GC_1116})

V_67 = Vertex(name = 'V_67',
              particles = [ P.c__tilde__, P.d, P.d__tilde__, P.t ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
              couplings = {(1,3):C.GC_205,(0,4):C.GC_628,(1,2):C.GC_867,(2,2):C.GC_912,(1,0):C.GC_1164,(2,0):C.GC_1245,(1,1):C.GC_1074,(2,1):C.GC_1119})

V_68 = Vertex(name = 'V_68',
              particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
              couplings = {(1,3):C.GC_206,(0,4):C.GC_629,(1,2):C.GC_870,(2,2):C.GC_915,(1,0):C.GC_1165,(2,0):C.GC_1246,(1,1):C.GC_1077,(2,1):C.GC_1122})

V_69 = Vertex(name = 'V_69',
              particles = [ P.u__tilde__, P.d, P.s__tilde__, P.u ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
              couplings = {(1,3):C.GC_207,(0,4):C.GC_630,(1,2):C.GC_835,(2,2):C.GC_880,(1,0):C.GC_1166,(2,0):C.GC_1247,(1,1):C.GC_1042,(2,1):C.GC_1087})

V_70 = Vertex(name = 'V_70',
              particles = [ P.c__tilde__, P.d, P.s__tilde__, P.u ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
              couplings = {(1,1):C.GC_208,(0,2):C.GC_631,(1,0):C.GC_1167,(2,0):C.GC_1248})

V_71 = Vertex(name = 'V_71',
              particles = [ P.t__tilde__, P.d, P.s__tilde__, P.u ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
              couplings = {(1,1):C.GC_209,(0,2):C.GC_632,(1,0):C.GC_1168,(2,0):C.GC_1249})

V_72 = Vertex(name = 'V_72',
              particles = [ P.u__tilde__, P.d, P.s__tilde__, P.c ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
              couplings = {(1,1):C.GC_210,(0,2):C.GC_633,(1,0):C.GC_1169,(2,0):C.GC_1250})

V_73 = Vertex(name = 'V_73',
              particles = [ P.c__tilde__, P.d, P.s__tilde__, P.c ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
              couplings = {(1,3):C.GC_211,(0,4):C.GC_634,(1,2):C.GC_853,(2,2):C.GC_898,(1,0):C.GC_1170,(2,0):C.GC_1251,(1,1):C.GC_1060,(2,1):C.GC_1105})

V_74 = Vertex(name = 'V_74',
              particles = [ P.t__tilde__, P.d, P.s__tilde__, P.c ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
              couplings = {(1,1):C.GC_212,(0,2):C.GC_635,(1,0):C.GC_1171,(2,0):C.GC_1252})

V_75 = Vertex(name = 'V_75',
              particles = [ P.u__tilde__, P.d, P.s__tilde__, P.t ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
              couplings = {(1,1):C.GC_213,(0,2):C.GC_636,(1,0):C.GC_1172,(2,0):C.GC_1253})

V_76 = Vertex(name = 'V_76',
              particles = [ P.c__tilde__, P.d, P.s__tilde__, P.t ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
              couplings = {(1,1):C.GC_214,(0,2):C.GC_637,(1,0):C.GC_1173,(2,0):C.GC_1254})

V_77 = Vertex(name = 'V_77',
              particles = [ P.t__tilde__, P.d, P.s__tilde__, P.t ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
              couplings = {(1,3):C.GC_215,(0,4):C.GC_638,(1,2):C.GC_871,(2,2):C.GC_916,(1,0):C.GC_1174,(2,0):C.GC_1255,(1,1):C.GC_1078,(2,1):C.GC_1123})

V_78 = Vertex(name = 'V_78',
              particles = [ P.u__tilde__, P.d, P.b__tilde__, P.u ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
              couplings = {(1,3):C.GC_216,(0,4):C.GC_639,(1,2):C.GC_836,(2,2):C.GC_881,(1,0):C.GC_1175,(2,0):C.GC_1256,(1,1):C.GC_1043,(2,1):C.GC_1088})

V_79 = Vertex(name = 'V_79',
              particles = [ P.c__tilde__, P.d, P.b__tilde__, P.u ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
              couplings = {(1,1):C.GC_217,(0,2):C.GC_640,(1,0):C.GC_1176,(2,0):C.GC_1257})

V_80 = Vertex(name = 'V_80',
              particles = [ P.t__tilde__, P.d, P.b__tilde__, P.u ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
              couplings = {(1,1):C.GC_218,(0,2):C.GC_641,(1,0):C.GC_1177,(2,0):C.GC_1258})

V_81 = Vertex(name = 'V_81',
              particles = [ P.u__tilde__, P.d, P.b__tilde__, P.c ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
              couplings = {(1,1):C.GC_219,(0,2):C.GC_642,(1,0):C.GC_1178,(2,0):C.GC_1259})

V_82 = Vertex(name = 'V_82',
              particles = [ P.c__tilde__, P.d, P.b__tilde__, P.c ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
              couplings = {(1,3):C.GC_220,(0,4):C.GC_643,(1,2):C.GC_854,(2,2):C.GC_899,(1,0):C.GC_1179,(2,0):C.GC_1260,(1,1):C.GC_1061,(2,1):C.GC_1106})

V_83 = Vertex(name = 'V_83',
              particles = [ P.t__tilde__, P.d, P.b__tilde__, P.c ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
              couplings = {(1,1):C.GC_221,(0,2):C.GC_644,(1,0):C.GC_1180,(2,0):C.GC_1261})

V_84 = Vertex(name = 'V_84',
              particles = [ P.u__tilde__, P.d, P.b__tilde__, P.t ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
              couplings = {(1,1):C.GC_222,(0,2):C.GC_645,(1,0):C.GC_1181,(2,0):C.GC_1262})

V_85 = Vertex(name = 'V_85',
              particles = [ P.c__tilde__, P.d, P.b__tilde__, P.t ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
              couplings = {(1,1):C.GC_223,(0,2):C.GC_646,(1,0):C.GC_1182,(2,0):C.GC_1263})

V_86 = Vertex(name = 'V_86',
              particles = [ P.t__tilde__, P.d, P.b__tilde__, P.t ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(1,3):C.GC_224,(0,4):C.GC_647,(1,2):C.GC_872,(3,2):C.GC_917,(1,0):C.GC_1183,(3,0):C.GC_1264,(1,1):C.GC_1079,(3,1):C.GC_1124,(1,5):C.GC_1535,(3,5):C.GC_1547,(0,6):C.GC_1442,(2,6):C.GC_1541})

V_87 = Vertex(name = 'V_87',
              particles = [ P.u__tilde__, P.s, P.d__tilde__, P.u ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
              couplings = {(1,3):C.GC_225,(0,4):C.GC_648,(1,2):C.GC_837,(2,2):C.GC_882,(1,0):C.GC_1184,(2,0):C.GC_1265,(1,1):C.GC_1044,(2,1):C.GC_1089})

V_88 = Vertex(name = 'V_88',
              particles = [ P.c__tilde__, P.s, P.d__tilde__, P.u ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
              couplings = {(1,1):C.GC_226,(0,2):C.GC_649,(1,0):C.GC_1185,(2,0):C.GC_1266})

V_89 = Vertex(name = 'V_89',
              particles = [ P.t__tilde__, P.s, P.d__tilde__, P.u ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
              couplings = {(1,1):C.GC_227,(0,2):C.GC_650,(1,0):C.GC_1186,(2,0):C.GC_1267})

V_90 = Vertex(name = 'V_90',
              particles = [ P.u__tilde__, P.s, P.d__tilde__, P.c ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
              couplings = {(1,1):C.GC_228,(0,2):C.GC_651,(1,0):C.GC_1187,(2,0):C.GC_1268})

V_91 = Vertex(name = 'V_91',
              particles = [ P.c__tilde__, P.s, P.d__tilde__, P.c ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
              couplings = {(1,3):C.GC_229,(0,4):C.GC_652,(1,2):C.GC_855,(2,2):C.GC_900,(1,0):C.GC_1188,(2,0):C.GC_1269,(1,1):C.GC_1062,(2,1):C.GC_1107})

V_92 = Vertex(name = 'V_92',
              particles = [ P.t__tilde__, P.s, P.d__tilde__, P.c ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
              couplings = {(1,1):C.GC_230,(0,2):C.GC_653,(1,0):C.GC_1189,(2,0):C.GC_1270})

V_93 = Vertex(name = 'V_93',
              particles = [ P.u__tilde__, P.s, P.d__tilde__, P.t ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
              couplings = {(1,1):C.GC_231,(0,2):C.GC_654,(1,0):C.GC_1190,(2,0):C.GC_1271})

V_94 = Vertex(name = 'V_94',
              particles = [ P.c__tilde__, P.s, P.d__tilde__, P.t ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
              couplings = {(1,1):C.GC_232,(0,2):C.GC_655,(1,0):C.GC_1191,(2,0):C.GC_1272})

V_95 = Vertex(name = 'V_95',
              particles = [ P.t__tilde__, P.s, P.d__tilde__, P.t ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
              couplings = {(1,3):C.GC_233,(0,4):C.GC_656,(1,2):C.GC_873,(2,2):C.GC_918,(1,0):C.GC_1192,(2,0):C.GC_1273,(1,1):C.GC_1080,(2,1):C.GC_1125})

V_96 = Vertex(name = 'V_96',
              particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
              couplings = {(1,3):C.GC_234,(0,4):C.GC_657,(1,2):C.GC_838,(2,2):C.GC_883,(1,0):C.GC_1193,(2,0):C.GC_1274,(1,1):C.GC_1045,(2,1):C.GC_1090})

V_97 = Vertex(name = 'V_97',
              particles = [ P.c__tilde__, P.s, P.s__tilde__, P.u ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
              couplings = {(1,3):C.GC_235,(0,4):C.GC_658,(1,2):C.GC_844,(2,2):C.GC_889,(1,0):C.GC_1194,(2,0):C.GC_1275,(1,1):C.GC_1051,(2,1):C.GC_1096})

V_98 = Vertex(name = 'V_98',
              particles = [ P.t__tilde__, P.s, P.s__tilde__, P.u ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
              couplings = {(1,3):C.GC_236,(0,4):C.GC_659,(1,2):C.GC_847,(2,2):C.GC_892,(1,0):C.GC_1195,(2,0):C.GC_1276,(1,1):C.GC_1054,(2,1):C.GC_1099})

V_99 = Vertex(name = 'V_99',
              particles = [ P.u__tilde__, P.s, P.s__tilde__, P.c ],
              color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
              lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
              couplings = {(1,3):C.GC_237,(0,4):C.GC_660,(1,2):C.GC_850,(2,2):C.GC_895,(1,0):C.GC_1196,(2,0):C.GC_1277,(1,1):C.GC_1057,(2,1):C.GC_1102})

V_100 = Vertex(name = 'V_100',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
               couplings = {(1,3):C.GC_238,(0,4):C.GC_661,(1,2):C.GC_856,(2,2):C.GC_901,(1,0):C.GC_1197,(2,0):C.GC_1278,(1,1):C.GC_1063,(2,1):C.GC_1108})

V_101 = Vertex(name = 'V_101',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
               couplings = {(1,3):C.GC_239,(0,4):C.GC_662,(1,2):C.GC_862,(2,2):C.GC_907,(1,0):C.GC_1198,(2,0):C.GC_1279,(1,1):C.GC_1069,(2,1):C.GC_1114})

V_102 = Vertex(name = 'V_102',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
               couplings = {(1,3):C.GC_240,(0,4):C.GC_663,(1,2):C.GC_865,(2,2):C.GC_910,(1,0):C.GC_1199,(2,0):C.GC_1280,(1,1):C.GC_1072,(2,1):C.GC_1117})

V_103 = Vertex(name = 'V_103',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
               couplings = {(1,3):C.GC_241,(0,4):C.GC_664,(1,2):C.GC_868,(2,2):C.GC_913,(1,0):C.GC_1200,(2,0):C.GC_1281,(1,1):C.GC_1075,(2,1):C.GC_1120})

V_104 = Vertex(name = 'V_104',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
               couplings = {(1,3):C.GC_242,(0,4):C.GC_665,(1,2):C.GC_874,(2,2):C.GC_919,(1,0):C.GC_1201,(2,0):C.GC_1282,(1,1):C.GC_1081,(2,1):C.GC_1126})

V_105 = Vertex(name = 'V_105',
               particles = [ P.u__tilde__, P.s, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
               couplings = {(1,3):C.GC_243,(0,4):C.GC_666,(1,2):C.GC_839,(2,2):C.GC_884,(1,0):C.GC_1202,(2,0):C.GC_1283,(1,1):C.GC_1046,(2,1):C.GC_1091})

V_106 = Vertex(name = 'V_106',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
               couplings = {(1,1):C.GC_244,(0,2):C.GC_667,(1,0):C.GC_1203,(2,0):C.GC_1284})

V_107 = Vertex(name = 'V_107',
               particles = [ P.t__tilde__, P.s, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
               couplings = {(1,1):C.GC_245,(0,2):C.GC_668,(1,0):C.GC_1204,(2,0):C.GC_1285})

V_108 = Vertex(name = 'V_108',
               particles = [ P.u__tilde__, P.s, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF4, L.FFFF5, L.FFFF6 ],
               couplings = {(1,1):C.GC_246,(0,3):C.GC_669,(1,2):C.GC_1155,(1,0):C.GC_1205,(2,0):C.GC_1286})

V_109 = Vertex(name = 'V_109',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
               couplings = {(1,3):C.GC_247,(0,4):C.GC_670,(1,2):C.GC_857,(2,2):C.GC_902,(1,0):C.GC_1206,(2,0):C.GC_1287,(1,1):C.GC_1064,(2,1):C.GC_1109})

V_110 = Vertex(name = 'V_110',
               particles = [ P.t__tilde__, P.s, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
               couplings = {(1,1):C.GC_248,(0,2):C.GC_671,(1,0):C.GC_1207,(2,0):C.GC_1288})

V_111 = Vertex(name = 'V_111',
               particles = [ P.u__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
               couplings = {(1,1):C.GC_249,(0,2):C.GC_672,(1,0):C.GC_1208,(2,0):C.GC_1289})

V_112 = Vertex(name = 'V_112',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
               couplings = {(1,1):C.GC_250,(0,2):C.GC_673,(1,0):C.GC_1209,(2,0):C.GC_1290})

V_113 = Vertex(name = 'V_113',
               particles = [ P.t__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(1,3):C.GC_251,(0,4):C.GC_674,(1,2):C.GC_875,(3,2):C.GC_920,(1,0):C.GC_1210,(3,0):C.GC_1291,(1,1):C.GC_1082,(3,1):C.GC_1127,(1,5):C.GC_1536,(3,5):C.GC_1548,(0,6):C.GC_1443,(2,6):C.GC_1542})

V_114 = Vertex(name = 'V_114',
               particles = [ P.u__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
               couplings = {(1,3):C.GC_252,(0,4):C.GC_675,(1,2):C.GC_840,(2,2):C.GC_885,(1,0):C.GC_1211,(2,0):C.GC_1292,(1,1):C.GC_1047,(2,1):C.GC_1092})

V_115 = Vertex(name = 'V_115',
               particles = [ P.c__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
               couplings = {(1,1):C.GC_253,(0,2):C.GC_676,(1,0):C.GC_1212,(2,0):C.GC_1293})

V_116 = Vertex(name = 'V_116',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
               couplings = {(1,1):C.GC_254,(0,2):C.GC_677,(1,0):C.GC_1213,(2,0):C.GC_1294})

V_117 = Vertex(name = 'V_117',
               particles = [ P.u__tilde__, P.b, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
               couplings = {(1,1):C.GC_255,(0,2):C.GC_678,(1,0):C.GC_1214,(2,0):C.GC_1295})

V_118 = Vertex(name = 'V_118',
               particles = [ P.c__tilde__, P.b, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
               couplings = {(1,3):C.GC_256,(0,4):C.GC_679,(1,2):C.GC_858,(2,2):C.GC_903,(1,0):C.GC_1215,(2,0):C.GC_1296,(1,1):C.GC_1065,(2,1):C.GC_1110})

V_119 = Vertex(name = 'V_119',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
               couplings = {(1,1):C.GC_257,(0,2):C.GC_680,(1,0):C.GC_1216,(2,0):C.GC_1297})

V_120 = Vertex(name = 'V_120',
               particles = [ P.u__tilde__, P.b, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
               couplings = {(1,1):C.GC_258,(0,2):C.GC_681,(1,0):C.GC_1217,(2,0):C.GC_1298})

V_121 = Vertex(name = 'V_121',
               particles = [ P.c__tilde__, P.b, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
               couplings = {(1,1):C.GC_259,(0,2):C.GC_682,(1,0):C.GC_1218,(2,0):C.GC_1299})

V_122 = Vertex(name = 'V_122',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF2, L.FFFF4, L.FFFF6 ],
               couplings = {(1,5):C.GC_260,(0,6):C.GC_683,(1,0):C.GC_1376,(3,0):C.GC_1544,(0,4):C.GC_1328,(2,4):C.GC_1538,(1,3):C.GC_876,(3,3):C.GC_921,(1,1):C.GC_1219,(3,1):C.GC_1300,(1,2):C.GC_1083,(3,2):C.GC_1128})

V_123 = Vertex(name = 'V_123',
               particles = [ P.u__tilde__, P.b, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
               couplings = {(1,3):C.GC_261,(0,4):C.GC_684,(1,2):C.GC_841,(2,2):C.GC_886,(1,0):C.GC_1220,(2,0):C.GC_1301,(1,1):C.GC_1048,(2,1):C.GC_1093})

V_124 = Vertex(name = 'V_124',
               particles = [ P.c__tilde__, P.b, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
               couplings = {(1,1):C.GC_262,(0,2):C.GC_685,(1,0):C.GC_1221,(2,0):C.GC_1302})

V_125 = Vertex(name = 'V_125',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
               couplings = {(1,1):C.GC_263,(0,2):C.GC_686,(1,0):C.GC_1222,(2,0):C.GC_1303})

V_126 = Vertex(name = 'V_126',
               particles = [ P.u__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
               couplings = {(1,1):C.GC_264,(0,2):C.GC_687,(1,0):C.GC_1223,(2,0):C.GC_1304})

V_127 = Vertex(name = 'V_127',
               particles = [ P.c__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
               couplings = {(1,3):C.GC_265,(0,4):C.GC_688,(1,2):C.GC_859,(2,2):C.GC_904,(1,0):C.GC_1224,(2,0):C.GC_1305,(1,1):C.GC_1066,(2,1):C.GC_1111})

V_128 = Vertex(name = 'V_128',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
               couplings = {(1,1):C.GC_266,(0,2):C.GC_689,(1,0):C.GC_1225,(2,0):C.GC_1306})

V_129 = Vertex(name = 'V_129',
               particles = [ P.u__tilde__, P.b, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
               couplings = {(1,1):C.GC_267,(0,2):C.GC_690,(1,0):C.GC_1226,(2,0):C.GC_1307})

V_130 = Vertex(name = 'V_130',
               particles = [ P.c__tilde__, P.b, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF4, L.FFFF6 ],
               couplings = {(1,1):C.GC_268,(0,2):C.GC_691,(1,0):C.GC_1227,(2,0):C.GC_1308})

V_131 = Vertex(name = 'V_131',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF2, L.FFFF4, L.FFFF6 ],
               couplings = {(1,5):C.GC_269,(0,6):C.GC_692,(1,0):C.GC_1377,(3,0):C.GC_1545,(0,4):C.GC_1329,(2,4):C.GC_1539,(1,3):C.GC_877,(3,3):C.GC_922,(1,1):C.GC_1228,(3,1):C.GC_1309,(1,2):C.GC_1084,(3,2):C.GC_1129})

V_132 = Vertex(name = 'V_132',
               particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
               couplings = {(1,3):C.GC_270,(0,4):C.GC_693,(1,2):C.GC_842,(2,2):C.GC_887,(1,0):C.GC_1229,(2,0):C.GC_1310,(1,1):C.GC_1049,(2,1):C.GC_1094})

V_133 = Vertex(name = 'V_133',
               particles = [ P.c__tilde__, P.b, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
               couplings = {(1,3):C.GC_271,(0,4):C.GC_694,(1,2):C.GC_845,(2,2):C.GC_890,(1,0):C.GC_1230,(2,0):C.GC_1311,(1,1):C.GC_1052,(2,1):C.GC_1097})

V_134 = Vertex(name = 'V_134',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
               couplings = {(1,3):C.GC_272,(0,4):C.GC_695,(1,2):C.GC_848,(2,2):C.GC_893,(1,0):C.GC_1231,(2,0):C.GC_1312,(1,1):C.GC_1055,(2,1):C.GC_1100})

V_135 = Vertex(name = 'V_135',
               particles = [ P.u__tilde__, P.b, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
               couplings = {(1,3):C.GC_273,(0,4):C.GC_696,(1,2):C.GC_851,(2,2):C.GC_896,(1,0):C.GC_1232,(2,0):C.GC_1313,(1,1):C.GC_1058,(2,1):C.GC_1103})

V_136 = Vertex(name = 'V_136',
               particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
               couplings = {(1,3):C.GC_274,(0,4):C.GC_697,(1,2):C.GC_860,(2,2):C.GC_905,(1,0):C.GC_1233,(2,0):C.GC_1314,(1,1):C.GC_1067,(2,1):C.GC_1112})

V_137 = Vertex(name = 'V_137',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
               couplings = {(1,3):C.GC_275,(0,4):C.GC_698,(1,2):C.GC_863,(2,2):C.GC_908,(1,0):C.GC_1234,(2,0):C.GC_1315,(1,1):C.GC_1070,(2,1):C.GC_1115})

V_138 = Vertex(name = 'V_138',
               particles = [ P.u__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
               couplings = {(1,3):C.GC_276,(0,4):C.GC_699,(1,2):C.GC_866,(2,2):C.GC_911,(1,0):C.GC_1235,(2,0):C.GC_1316,(1,1):C.GC_1073,(2,1):C.GC_1118})

V_139 = Vertex(name = 'V_139',
               particles = [ P.c__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
               couplings = {(1,3):C.GC_277,(0,4):C.GC_700,(1,2):C.GC_869,(2,2):C.GC_914,(1,0):C.GC_1236,(2,0):C.GC_1317,(1,1):C.GC_1076,(2,1):C.GC_1121})

V_140 = Vertex(name = 'V_140',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF2, L.FFFF4, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(1,5):C.GC_278,(0,6):C.GC_701,(1,0):C.GC_1378,(3,0):C.GC_1546,(0,4):C.GC_1330,(2,4):C.GC_1540,(1,3):C.GC_878,(3,3):C.GC_923,(1,1):C.GC_1237,(3,1):C.GC_1318,(1,2):C.GC_1085,(3,2):C.GC_1130,(1,7):C.GC_1537,(3,7):C.GC_1549,(0,8):C.GC_1444,(2,8):C.GC_1543})

V_141 = Vertex(name = 'V_141',
               particles = [ P.b__tilde__, P.b, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_2084,(0,1):C.GC_2023})

V_142 = Vertex(name = 'V_142',
               particles = [ P.b__tilde__, P.b, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_2085,(0,1):C.GC_2029})

V_143 = Vertex(name = 'V_143',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_2044})

V_144 = Vertex(name = 'V_144',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_2045})

V_145 = Vertex(name = 'V_145',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_2046})

V_146 = Vertex(name = 'V_146',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_2053})

V_147 = Vertex(name = 'V_147',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_2054})

V_148 = Vertex(name = 'V_148',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_2055})

V_149 = Vertex(name = 'V_149',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
               couplings = {(0,2):C.GC_2021,(0,0):C.GC_2086,(0,1):C.GC_2032})

V_150 = Vertex(name = 'V_150',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_2026})

V_151 = Vertex(name = 'V_151',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_2040})

V_152 = Vertex(name = 'V_152',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_2047})

V_153 = Vertex(name = 'V_153',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_2048})

V_154 = Vertex(name = 'V_154',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_2049})

V_155 = Vertex(name = 'V_155',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_2050})

V_156 = Vertex(name = 'V_156',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_2051})

V_157 = Vertex(name = 'V_157',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_2052})

V_158 = Vertex(name = 'V_158',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_2078})

V_159 = Vertex(name = 'V_159',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_2079})

V_160 = Vertex(name = 'V_160',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_2080})

V_161 = Vertex(name = 'V_161',
               particles = [ P.t__tilde__, P.t, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_2105,(0,1):C.GC_2058})

V_162 = Vertex(name = 'V_162',
               particles = [ P.t__tilde__, P.t, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_2106,(0,1):C.GC_2064})

V_163 = Vertex(name = 'V_163',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_2081})

V_164 = Vertex(name = 'V_164',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_2082})

V_165 = Vertex(name = 'V_165',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_2083})

V_166 = Vertex(name = 'V_166',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_2041})

V_167 = Vertex(name = 'V_167',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_2042})

V_168 = Vertex(name = 'V_168',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_2043})

V_169 = Vertex(name = 'V_169',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
               couplings = {(0,2):C.GC_2056,(0,0):C.GC_2107,(0,1):C.GC_2067})

V_170 = Vertex(name = 'V_170',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_2061})

V_171 = Vertex(name = 'V_171',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_2077})

V_172 = Vertex(name = 'V_172',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS3 ],
               couplings = {(0,0):C.GC_1146,(0,1):C.GC_1565})

V_173 = Vertex(name = 'V_173',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS3 ],
               couplings = {(0,0):C.GC_1720,(0,1):C.GC_1778})

V_174 = Vertex(name = 'V_174',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV10, L.VVVV3 ],
               couplings = {(0,0):C.GC_1586,(0,1):C.GC_2012})

V_175 = Vertex(name = 'V_175',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_1584})

V_176 = Vertex(name = 'V_176',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_1585})

V_177 = Vertex(name = 'V_177',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV6, L.VVVV9 ],
               couplings = {(0,1):C.GC_1567,(0,0):C.GC_2014})

V_178 = Vertex(name = 'V_178',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV6 ],
               couplings = {(0,0):C.GC_1562})

V_179 = Vertex(name = 'V_179',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV6 ],
               couplings = {(0,0):C.GC_1563})

V_180 = Vertex(name = 'V_180',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS2 ],
               couplings = {(0,0):C.GC_1587})

V_181 = Vertex(name = 'V_181',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS2 ],
               couplings = {(0,0):C.GC_1793})

V_182 = Vertex(name = 'V_182',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS2, L.VVVSS3 ],
               couplings = {(0,1):C.GC_1145,(0,0):C.GC_1566})

V_183 = Vertex(name = 'V_183',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS2, L.VVVS3 ],
               couplings = {(0,1):C.GC_1719,(0,0):C.GC_1779})

V_184 = Vertex(name = 'V_184',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVV3 ],
               couplings = {(0,0):C.GC_1590})

V_185 = Vertex(name = 'V_185',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV10, L.VVVV3 ],
               couplings = {(0,0):C.GC_1147,(0,1):C.GC_35})

V_186 = Vertex(name = 'V_186',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_38})

V_187 = Vertex(name = 'V_187',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV19 ],
               couplings = {(0,0):C.GC_1588})

V_188 = Vertex(name = 'V_188',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVV21 ],
               couplings = {(0,0):C.GC_1569})

V_189 = Vertex(name = 'V_189',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS2 ],
               couplings = {(0,0):C.GC_1149})

V_190 = Vertex(name = 'V_190',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS2 ],
               couplings = {(0,0):C.GC_1721})

V_191 = Vertex(name = 'V_191',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV8 ],
               couplings = {(0,0):C.GC_1589})

V_192 = Vertex(name = 'V_192',
               particles = [ P.a, P.Z, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS1 ],
               couplings = {(0,0):C.GC_1702})

V_193 = Vertex(name = 'V_193',
               particles = [ P.a, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1 ],
               couplings = {(0,0):C.GC_1914})

V_194 = Vertex(name = 'V_194',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV10, L.VVVV3 ],
               couplings = {(0,0):C.GC_1148,(0,1):C.GC_36})

V_195 = Vertex(name = 'V_195',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_39})

V_196 = Vertex(name = 'V_196',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV3 ],
               couplings = {(0,0):C.GC_2009})

V_197 = Vertex(name = 'V_197',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS5 ],
               couplings = {(0,0):C.GC_1568})

V_198 = Vertex(name = 'V_198',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS5 ],
               couplings = {(0,0):C.GC_1780})

V_199 = Vertex(name = 'V_199',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV9 ],
               couplings = {(0,0):C.GC_1570})

V_200 = Vertex(name = 'V_200',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV16 ],
               couplings = {(0,0):C.GC_1151})

V_201 = Vertex(name = 'V_201',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV17 ],
               couplings = {(0,0):C.GC_1571})

V_202 = Vertex(name = 'V_202',
               particles = [ P.Z, P.Z, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS1 ],
               couplings = {(0,0):C.GC_1701})

V_203 = Vertex(name = 'V_203',
               particles = [ P.Z, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1 ],
               couplings = {(0,0):C.GC_1913})

V_204 = Vertex(name = 'V_204',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS2 ],
               couplings = {(0,0):C.GC_1150})

V_205 = Vertex(name = 'V_205',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS2 ],
               couplings = {(0,0):C.GC_1722})

V_206 = Vertex(name = 'V_206',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV8 ],
               couplings = {(0,0):C.GC_1153})

V_207 = Vertex(name = 'V_207',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV20 ],
               couplings = {(0,0):C.GC_1152})

V_208 = Vertex(name = 'V_208',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_1,(0,0):C.GC_1989,(0,1):C.GC_1931})

V_209 = Vertex(name = 'V_209',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,1):C.GC_19,(0,0):C.GC_1555})

V_210 = Vertex(name = 'V_210',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,1):C.GC_1978,(0,0):C.GC_1560})

V_211 = Vertex(name = 'V_211',
               particles = [ P.s__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1920,(0,1):C.GC_1933})

V_212 = Vertex(name = 'V_212',
               particles = [ P.b__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1922,(0,1):C.GC_1935})

V_213 = Vertex(name = 'V_213',
               particles = [ P.d__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1924,(0,1):C.GC_1937})

V_214 = Vertex(name = 'V_214',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_1,(0,0):C.GC_1990,(0,1):C.GC_1938})

V_215 = Vertex(name = 'V_215',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,1):C.GC_19,(0,0):C.GC_1555})

V_216 = Vertex(name = 'V_216',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,1):C.GC_1978,(0,0):C.GC_1560})

V_217 = Vertex(name = 'V_217',
               particles = [ P.b__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1926,(0,1):C.GC_1940})

V_218 = Vertex(name = 'V_218',
               particles = [ P.d__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1928,(0,1):C.GC_1942})

V_219 = Vertex(name = 'V_219',
               particles = [ P.s__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1930,(0,1):C.GC_1944})

V_220 = Vertex(name = 'V_220',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4, L.FFV5, L.FFV9 ],
               couplings = {(0,2):C.GC_1,(0,0):C.GC_1991,(0,1):C.GC_1945,(0,3):C.GC_2039})

V_221 = Vertex(name = 'V_221',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,1):C.GC_19,(0,0):C.GC_1555})

V_222 = Vertex(name = 'V_222',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,1):C.GC_1978,(0,0):C.GC_1560})

V_223 = Vertex(name = 'V_223',
               particles = [ P.d__tilde__, P.d, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1618,(0,1):C.GC_1636})

V_224 = Vertex(name = 'V_224',
               particles = [ P.s__tilde__, P.d, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1620,(0,1):C.GC_1638})

V_225 = Vertex(name = 'V_225',
               particles = [ P.b__tilde__, P.d, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1622,(0,1):C.GC_1640})

V_226 = Vertex(name = 'V_226',
               particles = [ P.d__tilde__, P.s, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1624,(0,1):C.GC_1642})

V_227 = Vertex(name = 'V_227',
               particles = [ P.s__tilde__, P.s, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1626,(0,1):C.GC_1644})

V_228 = Vertex(name = 'V_228',
               particles = [ P.b__tilde__, P.s, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1628,(0,1):C.GC_1646})

V_229 = Vertex(name = 'V_229',
               particles = [ P.d__tilde__, P.b, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1630,(0,1):C.GC_1648})

V_230 = Vertex(name = 'V_230',
               particles = [ P.s__tilde__, P.b, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1632,(0,1):C.GC_1650})

V_231 = Vertex(name = 'V_231',
               particles = [ P.b__tilde__, P.b, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1634,(0,1):C.GC_1652})

V_232 = Vertex(name = 'V_232',
               particles = [ P.d__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1833,(0,1):C.GC_1851})

V_233 = Vertex(name = 'V_233',
               particles = [ P.s__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1835,(0,1):C.GC_1853})

V_234 = Vertex(name = 'V_234',
               particles = [ P.b__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1837,(0,1):C.GC_1855})

V_235 = Vertex(name = 'V_235',
               particles = [ P.d__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1839,(0,1):C.GC_1857})

V_236 = Vertex(name = 'V_236',
               particles = [ P.s__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1841,(0,1):C.GC_1859})

V_237 = Vertex(name = 'V_237',
               particles = [ P.b__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1843,(0,1):C.GC_1861})

V_238 = Vertex(name = 'V_238',
               particles = [ P.d__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1845,(0,1):C.GC_1863})

V_239 = Vertex(name = 'V_239',
               particles = [ P.s__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1847,(0,1):C.GC_1865})

V_240 = Vertex(name = 'V_240',
               particles = [ P.b__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4, L.FFVS5, L.FFVS6 ],
               couplings = {(0,0):C.GC_1849,(0,3):C.GC_1867,(0,2):C.GC_2035,(0,5):C.GC_2035,(0,1):C.GC_2036,(0,4):C.GC_2036})

V_241 = Vertex(name = 'V_241',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1596,(0,1):C.GC_3})

V_242 = Vertex(name = 'V_242',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1602,(0,1):C.GC_21})

V_243 = Vertex(name = 'V_243',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1992,(0,1):C.GC_1982})

V_244 = Vertex(name = 'V_244',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1596,(0,1):C.GC_3})

V_245 = Vertex(name = 'V_245',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1602,(0,1):C.GC_21})

V_246 = Vertex(name = 'V_246',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1993,(0,1):C.GC_1982})

V_247 = Vertex(name = 'V_247',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1596,(0,1):C.GC_3})

V_248 = Vertex(name = 'V_248',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1602,(0,1):C.GC_21})

V_249 = Vertex(name = 'V_249',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1994,(0,1):C.GC_1982})

V_250 = Vertex(name = 'V_250',
               particles = [ P.e__plus__, P.e__minus__, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1612,(0,1):C.GC_1610})

V_251 = Vertex(name = 'V_251',
               particles = [ P.mu__plus__, P.mu__minus__, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1614,(0,1):C.GC_1610})

V_252 = Vertex(name = 'V_252',
               particles = [ P.ta__plus__, P.ta__minus__, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1616,(0,1):C.GC_1610})

V_253 = Vertex(name = 'V_253',
               particles = [ P.e__plus__, P.e__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1827,(0,1):C.GC_1825})

V_254 = Vertex(name = 'V_254',
               particles = [ P.mu__plus__, P.mu__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1829,(0,1):C.GC_1825})

V_255 = Vertex(name = 'V_255',
               particles = [ P.ta__plus__, P.ta__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1831,(0,1):C.GC_1825})

V_256 = Vertex(name = 'V_256',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1594,(0,1):C.GC_2})

V_257 = Vertex(name = 'V_257',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1600,(0,1):C.GC_20})

V_258 = Vertex(name = 'V_258',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1983,(0,1):C.GC_1979})

V_259 = Vertex(name = 'V_259',
               particles = [ P.c__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1947,(0,1):C.GC_1960})

V_260 = Vertex(name = 'V_260',
               particles = [ P.t__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1949,(0,1):C.GC_1962})

V_261 = Vertex(name = 'V_261',
               particles = [ P.u__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1951,(0,1):C.GC_1964})

V_262 = Vertex(name = 'V_262',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1594,(0,1):C.GC_2})

V_263 = Vertex(name = 'V_263',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1600,(0,1):C.GC_20})

V_264 = Vertex(name = 'V_264',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1984,(0,1):C.GC_1980})

V_265 = Vertex(name = 'V_265',
               particles = [ P.t__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1953,(0,1):C.GC_1967})

V_266 = Vertex(name = 'V_266',
               particles = [ P.u__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1955,(0,1):C.GC_1969})

V_267 = Vertex(name = 'V_267',
               particles = [ P.c__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1957,(0,1):C.GC_1971})

V_268 = Vertex(name = 'V_268',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4, L.FFV7, L.FFV8 ],
               couplings = {(0,0):C.GC_1594,(0,3):C.GC_2,(0,2):C.GC_2076,(0,5):C.GC_2076,(0,1):C.GC_2075,(0,4):C.GC_2075})

V_269 = Vertex(name = 'V_269',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1600,(0,1):C.GC_20})

V_270 = Vertex(name = 'V_270',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1985,(0,1):C.GC_1981})

V_271 = Vertex(name = 'V_271',
               particles = [ P.u__tilde__, P.u, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1654,(0,1):C.GC_1672})

V_272 = Vertex(name = 'V_272',
               particles = [ P.c__tilde__, P.u, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1656,(0,1):C.GC_1674})

V_273 = Vertex(name = 'V_273',
               particles = [ P.t__tilde__, P.u, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1658,(0,1):C.GC_1676})

V_274 = Vertex(name = 'V_274',
               particles = [ P.u__tilde__, P.c, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1660,(0,1):C.GC_1678})

V_275 = Vertex(name = 'V_275',
               particles = [ P.c__tilde__, P.c, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1662,(0,1):C.GC_1680})

V_276 = Vertex(name = 'V_276',
               particles = [ P.t__tilde__, P.c, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1664,(0,1):C.GC_1682})

V_277 = Vertex(name = 'V_277',
               particles = [ P.u__tilde__, P.t, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1666,(0,1):C.GC_1684})

V_278 = Vertex(name = 'V_278',
               particles = [ P.c__tilde__, P.t, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1668,(0,1):C.GC_1686})

V_279 = Vertex(name = 'V_279',
               particles = [ P.t__tilde__, P.t, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1670,(0,1):C.GC_1688})

V_280 = Vertex(name = 'V_280',
               particles = [ P.u__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1869,(0,1):C.GC_1887})

V_281 = Vertex(name = 'V_281',
               particles = [ P.c__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1871,(0,1):C.GC_1889})

V_282 = Vertex(name = 'V_282',
               particles = [ P.t__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1873,(0,1):C.GC_1891})

V_283 = Vertex(name = 'V_283',
               particles = [ P.u__tilde__, P.c, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1875,(0,1):C.GC_1893})

V_284 = Vertex(name = 'V_284',
               particles = [ P.c__tilde__, P.c, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1877,(0,1):C.GC_1895})

V_285 = Vertex(name = 'V_285',
               particles = [ P.t__tilde__, P.c, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1879,(0,1):C.GC_1897})

V_286 = Vertex(name = 'V_286',
               particles = [ P.u__tilde__, P.t, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1881,(0,1):C.GC_1899})

V_287 = Vertex(name = 'V_287',
               particles = [ P.c__tilde__, P.t, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1883,(0,1):C.GC_1901})

V_288 = Vertex(name = 'V_288',
               particles = [ P.t__tilde__, P.t, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4, L.FFVS5, L.FFVS6 ],
               couplings = {(0,0):C.GC_1885,(0,3):C.GC_1903,(0,2):C.GC_2073,(0,5):C.GC_2073,(0,1):C.GC_2072,(0,4):C.GC_2072})

V_289 = Vertex(name = 'V_289',
               particles = [ P.ve__tilde__, P.ve, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1595})

V_290 = Vertex(name = 'V_290',
               particles = [ P.ve__tilde__, P.ve, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1601})

V_291 = Vertex(name = 'V_291',
               particles = [ P.ve__tilde__, P.ve, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1986})

V_292 = Vertex(name = 'V_292',
               particles = [ P.vm__tilde__, P.vm, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1595})

V_293 = Vertex(name = 'V_293',
               particles = [ P.vm__tilde__, P.vm, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1601})

V_294 = Vertex(name = 'V_294',
               particles = [ P.vm__tilde__, P.vm, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1987})

V_295 = Vertex(name = 'V_295',
               particles = [ P.vt__tilde__, P.vt, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1595})

V_296 = Vertex(name = 'V_296',
               particles = [ P.vt__tilde__, P.vt, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1601})

V_297 = Vertex(name = 'V_297',
               particles = [ P.vt__tilde__, P.vt, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1988})

V_298 = Vertex(name = 'V_298',
               particles = [ P.ve__tilde__, P.ve, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1611})

V_299 = Vertex(name = 'V_299',
               particles = [ P.vm__tilde__, P.vm, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1613})

V_300 = Vertex(name = 'V_300',
               particles = [ P.vt__tilde__, P.vt, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1615})

V_301 = Vertex(name = 'V_301',
               particles = [ P.ve__tilde__, P.ve, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1826})

V_302 = Vertex(name = 'V_302',
               particles = [ P.vm__tilde__, P.vm, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1828})

V_303 = Vertex(name = 'V_303',
               particles = [ P.vt__tilde__, P.vt, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1830})

V_304 = Vertex(name = 'V_304',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_16})

V_305 = Vertex(name = 'V_305',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_16})

V_306 = Vertex(name = 'V_306',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4, L.FFV7, L.FFV8 ],
               couplings = {(0,0):C.GC_16,(0,3):C.GC_16,(0,2):C.GC_2028,(0,5):C.GC_2028,(0,1):C.GC_2027,(0,4):C.GC_2027})

V_307 = Vertex(name = 'V_307',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_16})

V_308 = Vertex(name = 'V_308',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_16})

V_309 = Vertex(name = 'V_309',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4, L.FFV7, L.FFV8 ],
               couplings = {(0,0):C.GC_16,(0,3):C.GC_16,(0,2):C.GC_2063,(0,5):C.GC_2063,(0,1):C.GC_2062,(0,4):C.GC_2062})

V_310 = Vertex(name = 'V_310',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5})

V_311 = Vertex(name = 'V_311',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_23})

V_312 = Vertex(name = 'V_312',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1798})

V_313 = Vertex(name = 'V_313',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_6})

V_314 = Vertex(name = 'V_314',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_24})

V_315 = Vertex(name = 'V_315',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1799})

V_316 = Vertex(name = 'V_316',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV7, L.FFV8 ],
               couplings = {(0,2):C.GC_1742,(0,1):C.GC_1741,(0,0):C.GC_7})

V_317 = Vertex(name = 'V_317',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_25})

V_318 = Vertex(name = 'V_318',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1800})

V_319 = Vertex(name = 'V_319',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_8})

V_320 = Vertex(name = 'V_320',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_26})

V_321 = Vertex(name = 'V_321',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1801})

V_322 = Vertex(name = 'V_322',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_9})

V_323 = Vertex(name = 'V_323',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_27})

V_324 = Vertex(name = 'V_324',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1802})

V_325 = Vertex(name = 'V_325',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV7, L.FFV8 ],
               couplings = {(0,2):C.GC_1745,(0,1):C.GC_1744,(0,0):C.GC_10})

V_326 = Vertex(name = 'V_326',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_28})

V_327 = Vertex(name = 'V_327',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1803})

V_328 = Vertex(name = 'V_328',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
               couplings = {(0,2):C.GC_1733,(0,1):C.GC_1732,(0,0):C.GC_11})

V_329 = Vertex(name = 'V_329',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_29})

V_330 = Vertex(name = 'V_330',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1804})

V_331 = Vertex(name = 'V_331',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
               couplings = {(0,2):C.GC_1736,(0,1):C.GC_1735,(0,0):C.GC_12})

V_332 = Vertex(name = 'V_332',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_30})

V_333 = Vertex(name = 'V_333',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1805})

V_334 = Vertex(name = 'V_334',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4, L.FFV7, L.FFV8 ],
               couplings = {(0,2):C.GC_1739,(0,5):C.GC_1748,(0,1):C.GC_1738,(0,4):C.GC_1747,(0,0):C.GC_13,(0,3):C.GC_2070})

V_335 = Vertex(name = 'V_335',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_31})

V_336 = Vertex(name = 'V_336',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1806})

V_337 = Vertex(name = 'V_337',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1319})

V_338 = Vertex(name = 'V_338',
               particles = [ P.s__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1320})

V_339 = Vertex(name = 'V_339',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1321})

V_340 = Vertex(name = 'V_340',
               particles = [ P.d__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1322})

V_341 = Vertex(name = 'V_341',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1323})

V_342 = Vertex(name = 'V_342',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1324})

V_343 = Vertex(name = 'V_343',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1325})

V_344 = Vertex(name = 'V_344',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1326})

V_345 = Vertex(name = 'V_345',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1327,(0,1):C.GC_2068})

V_346 = Vertex(name = 'V_346',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1723})

V_347 = Vertex(name = 'V_347',
               particles = [ P.s__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1724})

V_348 = Vertex(name = 'V_348',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5, L.FFVS6 ],
               couplings = {(0,2):C.GC_1341,(0,1):C.GC_1340,(0,0):C.GC_1725})

V_349 = Vertex(name = 'V_349',
               particles = [ P.d__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1726})

V_350 = Vertex(name = 'V_350',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1727})

V_351 = Vertex(name = 'V_351',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5, L.FFVS6 ],
               couplings = {(0,2):C.GC_1344,(0,1):C.GC_1343,(0,0):C.GC_1728})

V_352 = Vertex(name = 'V_352',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3 ],
               couplings = {(0,2):C.GC_1332,(0,1):C.GC_1331,(0,0):C.GC_1729})

V_353 = Vertex(name = 'V_353',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3 ],
               couplings = {(0,2):C.GC_1335,(0,1):C.GC_1334,(0,0):C.GC_1730})

V_354 = Vertex(name = 'V_354',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4, L.FFVS5, L.FFVS6 ],
               couplings = {(0,2):C.GC_1338,(0,5):C.GC_1347,(0,1):C.GC_1337,(0,4):C.GC_1346,(0,0):C.GC_1731,(0,3):C.GC_2069})

V_355 = Vertex(name = 'V_355',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4})

V_356 = Vertex(name = 'V_356',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_22})

V_357 = Vertex(name = 'V_357',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1794})

V_358 = Vertex(name = 'V_358',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4})

V_359 = Vertex(name = 'V_359',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_22})

V_360 = Vertex(name = 'V_360',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1795})

V_361 = Vertex(name = 'V_361',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4})

V_362 = Vertex(name = 'V_362',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_22})

V_363 = Vertex(name = 'V_363',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1796})

V_364 = Vertex(name = 'V_364',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1142})

V_365 = Vertex(name = 'V_365',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1143})

V_366 = Vertex(name = 'V_366',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1144})

V_367 = Vertex(name = 'V_367',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1716})

V_368 = Vertex(name = 'V_368',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1717})

V_369 = Vertex(name = 'V_369',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1718})

V_370 = Vertex(name = 'V_370',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1807})

V_371 = Vertex(name = 'V_371',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2087})

V_372 = Vertex(name = 'V_372',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2088})

V_373 = Vertex(name = 'V_373',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1808})

V_374 = Vertex(name = 'V_374',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2093})

V_375 = Vertex(name = 'V_375',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2094})

V_376 = Vertex(name = 'V_376',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV7, L.FFV8 ],
               couplings = {(0,2):C.GC_1769,(0,1):C.GC_1768,(0,0):C.GC_1809})

V_377 = Vertex(name = 'V_377',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2099})

V_378 = Vertex(name = 'V_378',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2100})

V_379 = Vertex(name = 'V_379',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1810})

V_380 = Vertex(name = 'V_380',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2089})

V_381 = Vertex(name = 'V_381',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2090})

V_382 = Vertex(name = 'V_382',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1811})

V_383 = Vertex(name = 'V_383',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2095})

V_384 = Vertex(name = 'V_384',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2096})

V_385 = Vertex(name = 'V_385',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV7, L.FFV8 ],
               couplings = {(0,2):C.GC_1772,(0,1):C.GC_1771,(0,0):C.GC_1812})

V_386 = Vertex(name = 'V_386',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2101})

V_387 = Vertex(name = 'V_387',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2102})

V_388 = Vertex(name = 'V_388',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
               couplings = {(0,2):C.GC_1760,(0,1):C.GC_1759,(0,0):C.GC_1813})

V_389 = Vertex(name = 'V_389',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2091})

V_390 = Vertex(name = 'V_390',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2092})

V_391 = Vertex(name = 'V_391',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
               couplings = {(0,2):C.GC_1763,(0,1):C.GC_1762,(0,0):C.GC_1814})

V_392 = Vertex(name = 'V_392',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2097})

V_393 = Vertex(name = 'V_393',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2098})

V_394 = Vertex(name = 'V_394',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4, L.FFV7, L.FFV8 ],
               couplings = {(0,2):C.GC_1766,(0,5):C.GC_1775,(0,1):C.GC_1765,(0,4):C.GC_1774,(0,0):C.GC_1815,(0,3):C.GC_2070})

V_395 = Vertex(name = 'V_395',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2103})

V_396 = Vertex(name = 'V_396',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2104})

V_397 = Vertex(name = 'V_397',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1349})

V_398 = Vertex(name = 'V_398',
               particles = [ P.c__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1350})

V_399 = Vertex(name = 'V_399',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1351})

V_400 = Vertex(name = 'V_400',
               particles = [ P.u__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1352})

V_401 = Vertex(name = 'V_401',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1353})

V_402 = Vertex(name = 'V_402',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1354})

V_403 = Vertex(name = 'V_403',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1355})

V_404 = Vertex(name = 'V_404',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1356})

V_405 = Vertex(name = 'V_405',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1357,(0,1):C.GC_2068})

V_406 = Vertex(name = 'V_406',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1750})

V_407 = Vertex(name = 'V_407',
               particles = [ P.c__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1751})

V_408 = Vertex(name = 'V_408',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5, L.FFVS6 ],
               couplings = {(0,2):C.GC_1368,(0,1):C.GC_1367,(0,0):C.GC_1752})

V_409 = Vertex(name = 'V_409',
               particles = [ P.u__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1753})

V_410 = Vertex(name = 'V_410',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1754})

V_411 = Vertex(name = 'V_411',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS5, L.FFVS6 ],
               couplings = {(0,2):C.GC_1371,(0,1):C.GC_1370,(0,0):C.GC_1755})

V_412 = Vertex(name = 'V_412',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3 ],
               couplings = {(0,2):C.GC_1359,(0,1):C.GC_1358,(0,0):C.GC_1756})

V_413 = Vertex(name = 'V_413',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3 ],
               couplings = {(0,2):C.GC_1362,(0,1):C.GC_1361,(0,0):C.GC_1757})

V_414 = Vertex(name = 'V_414',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4, L.FFVS5, L.FFVS6 ],
               couplings = {(0,2):C.GC_1365,(0,5):C.GC_1374,(0,1):C.GC_1364,(0,4):C.GC_1373,(0,0):C.GC_1758,(0,3):C.GC_2069})

V_415 = Vertex(name = 'V_415',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4})

V_416 = Vertex(name = 'V_416',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_22})

V_417 = Vertex(name = 'V_417',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1794})

V_418 = Vertex(name = 'V_418',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4})

V_419 = Vertex(name = 'V_419',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_22})

V_420 = Vertex(name = 'V_420',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1795})

V_421 = Vertex(name = 'V_421',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4})

V_422 = Vertex(name = 'V_422',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_22})

V_423 = Vertex(name = 'V_423',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1796})

V_424 = Vertex(name = 'V_424',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1142})

V_425 = Vertex(name = 'V_425',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1143})

V_426 = Vertex(name = 'V_426',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1144})

V_427 = Vertex(name = 'V_427',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1716})

V_428 = Vertex(name = 'V_428',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1717})

V_429 = Vertex(name = 'V_429',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1718})

V_430 = Vertex(name = 'V_430',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1591,(0,1):C.GC_1974})

V_431 = Vertex(name = 'V_431',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1597,(0,1):C.GC_1553})

V_432 = Vertex(name = 'V_432',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_2002,(0,1):C.GC_1558})

V_433 = Vertex(name = 'V_433',
               particles = [ P.s__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1919,(0,1):C.GC_1932})

V_434 = Vertex(name = 'V_434',
               particles = [ P.b__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1921,(0,1):C.GC_1934})

V_435 = Vertex(name = 'V_435',
               particles = [ P.d__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1923,(0,1):C.GC_1936})

V_436 = Vertex(name = 'V_436',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1591,(0,1):C.GC_1975})

V_437 = Vertex(name = 'V_437',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1597,(0,1):C.GC_1553})

V_438 = Vertex(name = 'V_438',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_2003,(0,1):C.GC_1558})

V_439 = Vertex(name = 'V_439',
               particles = [ P.b__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1925,(0,1):C.GC_1939})

V_440 = Vertex(name = 'V_440',
               particles = [ P.d__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1927,(0,1):C.GC_1941})

V_441 = Vertex(name = 'V_441',
               particles = [ P.s__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1929,(0,1):C.GC_1943})

V_442 = Vertex(name = 'V_442',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV2, L.FFV3, L.FFV4, L.FFV7, L.FFV8 ],
               couplings = {(0,0):C.GC_1591,(0,3):C.GC_1976,(0,2):C.GC_2037,(0,5):C.GC_2037,(0,1):C.GC_2038,(0,4):C.GC_2038})

V_443 = Vertex(name = 'V_443',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1597,(0,1):C.GC_1553})

V_444 = Vertex(name = 'V_444',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_2004,(0,1):C.GC_1558})

V_445 = Vertex(name = 'V_445',
               particles = [ P.d__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1617,(0,1):C.GC_1635})

V_446 = Vertex(name = 'V_446',
               particles = [ P.s__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1619,(0,1):C.GC_1637})

V_447 = Vertex(name = 'V_447',
               particles = [ P.b__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1621,(0,1):C.GC_1639})

V_448 = Vertex(name = 'V_448',
               particles = [ P.d__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1623,(0,1):C.GC_1641})

V_449 = Vertex(name = 'V_449',
               particles = [ P.s__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1625,(0,1):C.GC_1643})

V_450 = Vertex(name = 'V_450',
               particles = [ P.b__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1627,(0,1):C.GC_1645})

V_451 = Vertex(name = 'V_451',
               particles = [ P.d__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1629,(0,1):C.GC_1647})

V_452 = Vertex(name = 'V_452',
               particles = [ P.s__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1631,(0,1):C.GC_1649})

V_453 = Vertex(name = 'V_453',
               particles = [ P.b__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1633,(0,1):C.GC_1651})

V_454 = Vertex(name = 'V_454',
               particles = [ P.d__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1832,(0,1):C.GC_1850})

V_455 = Vertex(name = 'V_455',
               particles = [ P.s__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1834,(0,1):C.GC_1852})

V_456 = Vertex(name = 'V_456',
               particles = [ P.b__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1836,(0,1):C.GC_1854})

V_457 = Vertex(name = 'V_457',
               particles = [ P.d__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1838,(0,1):C.GC_1856})

V_458 = Vertex(name = 'V_458',
               particles = [ P.s__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1840,(0,1):C.GC_1858})

V_459 = Vertex(name = 'V_459',
               particles = [ P.b__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1842,(0,1):C.GC_1860})

V_460 = Vertex(name = 'V_460',
               particles = [ P.d__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1844,(0,1):C.GC_1862})

V_461 = Vertex(name = 'V_461',
               particles = [ P.s__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1846,(0,1):C.GC_1864})

V_462 = Vertex(name = 'V_462',
               particles = [ P.b__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS4, L.FFVS5, L.FFVS6 ],
               couplings = {(0,0):C.GC_1848,(0,3):C.GC_1866,(0,2):C.GC_2033,(0,5):C.GC_2033,(0,1):C.GC_2034,(0,4):C.GC_2034})

V_463 = Vertex(name = 'V_463',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1593,(0,1):C.GC_1977})

V_464 = Vertex(name = 'V_464',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1599,(0,1):C.GC_1554})

V_465 = Vertex(name = 'V_465',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_2005,(0,1):C.GC_1559})

V_466 = Vertex(name = 'V_466',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1593,(0,1):C.GC_1977})

V_467 = Vertex(name = 'V_467',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1599,(0,1):C.GC_1554})

V_468 = Vertex(name = 'V_468',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_2006,(0,1):C.GC_1559})

V_469 = Vertex(name = 'V_469',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1593,(0,1):C.GC_1977})

V_470 = Vertex(name = 'V_470',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1599,(0,1):C.GC_1554})

V_471 = Vertex(name = 'V_471',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_2007,(0,1):C.GC_1559})

V_472 = Vertex(name = 'V_472',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1605,(0,1):C.GC_1603})

V_473 = Vertex(name = 'V_473',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1607,(0,1):C.GC_1603})

V_474 = Vertex(name = 'V_474',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1609,(0,1):C.GC_1603})

V_475 = Vertex(name = 'V_475',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1820,(0,1):C.GC_1818})

V_476 = Vertex(name = 'V_476',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1822,(0,1):C.GC_1818})

V_477 = Vertex(name = 'V_477',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1824,(0,1):C.GC_1818})

V_478 = Vertex(name = 'V_478',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4, L.FFV6 ],
               couplings = {(0,0):C.GC_14,(0,2):C.GC_1973,(0,1):C.GC_1958})

V_479 = Vertex(name = 'V_479',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV6 ],
               couplings = {(0,0):C.GC_32,(0,1):C.GC_1552})

V_480 = Vertex(name = 'V_480',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV6 ],
               couplings = {(0,0):C.GC_1996,(0,1):C.GC_1557})

V_481 = Vertex(name = 'V_481',
               particles = [ P.c__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1946,(0,1):C.GC_1959})

V_482 = Vertex(name = 'V_482',
               particles = [ P.t__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1948,(0,1):C.GC_1961})

V_483 = Vertex(name = 'V_483',
               particles = [ P.u__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1950,(0,1):C.GC_1963})

V_484 = Vertex(name = 'V_484',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4, L.FFV6 ],
               couplings = {(0,0):C.GC_14,(0,2):C.GC_1973,(0,1):C.GC_1965})

V_485 = Vertex(name = 'V_485',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV6 ],
               couplings = {(0,0):C.GC_32,(0,1):C.GC_1552})

V_486 = Vertex(name = 'V_486',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV6 ],
               couplings = {(0,0):C.GC_1997,(0,1):C.GC_1557})

V_487 = Vertex(name = 'V_487',
               particles = [ P.t__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1952,(0,1):C.GC_1966})

V_488 = Vertex(name = 'V_488',
               particles = [ P.u__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1954,(0,1):C.GC_1968})

V_489 = Vertex(name = 'V_489',
               particles = [ P.c__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,0):C.GC_1956,(0,1):C.GC_1970})

V_490 = Vertex(name = 'V_490',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV4, L.FFV6, L.FFV9 ],
               couplings = {(0,0):C.GC_14,(0,2):C.GC_1973,(0,1):C.GC_1972,(0,3):C.GC_2074})

V_491 = Vertex(name = 'V_491',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV6 ],
               couplings = {(0,0):C.GC_32,(0,1):C.GC_1552})

V_492 = Vertex(name = 'V_492',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV6 ],
               couplings = {(0,0):C.GC_1998,(0,1):C.GC_1557})

V_493 = Vertex(name = 'V_493',
               particles = [ P.u__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1653,(0,1):C.GC_1671})

V_494 = Vertex(name = 'V_494',
               particles = [ P.c__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1655,(0,1):C.GC_1673})

V_495 = Vertex(name = 'V_495',
               particles = [ P.t__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1657,(0,1):C.GC_1675})

V_496 = Vertex(name = 'V_496',
               particles = [ P.u__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1659,(0,1):C.GC_1677})

V_497 = Vertex(name = 'V_497',
               particles = [ P.c__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1661,(0,1):C.GC_1679})

V_498 = Vertex(name = 'V_498',
               particles = [ P.t__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1663,(0,1):C.GC_1681})

V_499 = Vertex(name = 'V_499',
               particles = [ P.u__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1665,(0,1):C.GC_1683})

V_500 = Vertex(name = 'V_500',
               particles = [ P.c__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1667,(0,1):C.GC_1685})

V_501 = Vertex(name = 'V_501',
               particles = [ P.t__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_1669,(0,1):C.GC_1687})

V_502 = Vertex(name = 'V_502',
               particles = [ P.u__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1868,(0,1):C.GC_1886})

V_503 = Vertex(name = 'V_503',
               particles = [ P.c__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1870,(0,1):C.GC_1888})

V_504 = Vertex(name = 'V_504',
               particles = [ P.t__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1872,(0,1):C.GC_1890})

V_505 = Vertex(name = 'V_505',
               particles = [ P.u__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1874,(0,1):C.GC_1892})

V_506 = Vertex(name = 'V_506',
               particles = [ P.c__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1876,(0,1):C.GC_1894})

V_507 = Vertex(name = 'V_507',
               particles = [ P.t__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1878,(0,1):C.GC_1896})

V_508 = Vertex(name = 'V_508',
               particles = [ P.u__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1880,(0,1):C.GC_1898})

V_509 = Vertex(name = 'V_509',
               particles = [ P.c__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4 ],
               couplings = {(0,0):C.GC_1882,(0,1):C.GC_1900})

V_510 = Vertex(name = 'V_510',
               particles = [ P.t__tilde__, P.t, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS7 ],
               couplings = {(0,0):C.GC_1884,(0,1):C.GC_1902,(0,2):C.GC_2071})

V_511 = Vertex(name = 'V_511',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1592})

V_512 = Vertex(name = 'V_512',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1598})

V_513 = Vertex(name = 'V_513',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1999})

V_514 = Vertex(name = 'V_514',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1592})

V_515 = Vertex(name = 'V_515',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1598})

V_516 = Vertex(name = 'V_516',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2000})

V_517 = Vertex(name = 'V_517',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1592})

V_518 = Vertex(name = 'V_518',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_1598})

V_519 = Vertex(name = 'V_519',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_2001})

V_520 = Vertex(name = 'V_520',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1604})

V_521 = Vertex(name = 'V_521',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1606})

V_522 = Vertex(name = 'V_522',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_1608})

V_523 = Vertex(name = 'V_523',
               particles = [ P.ve__tilde__, P.ve, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1819})

V_524 = Vertex(name = 'V_524',
               particles = [ P.vm__tilde__, P.vm, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1821})

V_525 = Vertex(name = 'V_525',
               particles = [ P.vt__tilde__, P.vt, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_1823})

V_526 = Vertex(name = 'V_526',
               particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_288,(0,6):C.GC_279,(0,7):C.GC_1397,(2,7):C.GC_1406,(1,2):C.GC_1379,(3,2):C.GC_1388,(1,0):C.GC_1433,(3,0):C.GC_1445,(1,1):C.GC_702,(0,3):C.GC_1415,(2,3):C.GC_1424,(0,4):C.GC_702})

V_527 = Vertex(name = 'V_527',
               particles = [ P.s__tilde__, P.d, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_289,(0,6):C.GC_293,(0,7):C.GC_351,(2,7):C.GC_369,(1,2):C.GC_353,(3,2):C.GC_371,(1,0):C.GC_423,(3,0):C.GC_495,(1,1):C.GC_41,(0,3):C.GC_431,(2,3):C.GC_503,(0,4):C.GC_41})

V_528 = Vertex(name = 'V_528',
               particles = [ P.b__tilde__, P.d, P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_290,(0,6):C.GC_298,(0,7):C.GC_352,(2,7):C.GC_370,(1,2):C.GC_355,(3,2):C.GC_373,(1,0):C.GC_424,(3,0):C.GC_496,(1,1):C.GC_42,(0,3):C.GC_439,(2,3):C.GC_511,(0,4):C.GC_42})

V_529 = Vertex(name = 'V_529',
               particles = [ P.d__tilde__, P.d, P.d__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_291,(0,6):C.GC_303,(0,7):C.GC_447,(2,7):C.GC_519,(1,2):C.GC_393,(3,2):C.GC_411,(1,0):C.GC_425,(3,0):C.GC_497,(1,1):C.GC_43,(0,3):C.GC_387,(2,3):C.GC_405,(0,4):C.GC_43})

V_530 = Vertex(name = 'V_530',
               particles = [ P.s__tilde__, P.d, P.d__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_310,(0,6):C.GC_304,(0,7):C.GC_448,(2,7):C.GC_520,(1,2):C.GC_455,(3,2):C.GC_527,(1,0):C.GC_426,(3,0):C.GC_498,(1,1):C.GC_46,(0,3):C.GC_433,(2,3):C.GC_505,(0,4):C.GC_44})

V_531 = Vertex(name = 'V_531',
               particles = [ P.b__tilde__, P.d, P.d__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_317,(0,6):C.GC_305,(1,0):C.GC_427,(3,0):C.GC_499,(1,1):C.GC_50,(0,3):C.GC_441,(2,3):C.GC_513,(0,4):C.GC_45,(0,7):C.GC_449,(2,7):C.GC_521,(1,2):C.GC_463,(3,2):C.GC_535})

V_532 = Vertex(name = 'V_532',
               particles = [ P.d__tilde__, P.d, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_292,(0,6):C.GC_324,(0,7):C.GC_471,(2,7):C.GC_543,(1,2):C.GC_399,(3,2):C.GC_417,(1,0):C.GC_428,(3,0):C.GC_500,(1,1):C.GC_53,(0,3):C.GC_388,(2,3):C.GC_406,(0,4):C.GC_53})

V_533 = Vertex(name = 'V_533',
               particles = [ P.s__tilde__, P.d, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_333,(0,6):C.GC_325,(0,7):C.GC_472,(2,7):C.GC_544,(1,2):C.GC_479,(3,2):C.GC_551,(1,0):C.GC_429,(3,0):C.GC_501,(1,1):C.GC_58,(0,3):C.GC_436,(2,3):C.GC_508,(0,4):C.GC_54})

V_534 = Vertex(name = 'V_534',
               particles = [ P.b__tilde__, P.d, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_342,(0,6):C.GC_326,(0,7):C.GC_473,(2,7):C.GC_545,(1,2):C.GC_487,(3,2):C.GC_559,(1,0):C.GC_430,(3,0):C.GC_502,(1,1):C.GC_63,(0,3):C.GC_444,(2,3):C.GC_516,(0,4):C.GC_55})

V_535 = Vertex(name = 'V_535',
               particles = [ P.s__tilde__, P.d, P.s__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF13, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,3):C.GC_294,(0,4):C.GC_280,(0,5):C.GC_1398,(2,5):C.GC_1407,(1,1):C.GC_1380,(3,1):C.GC_1389,(1,0):C.GC_1434,(3,0):C.GC_1446,(0,2):C.GC_1416,(2,2):C.GC_1425})

V_536 = Vertex(name = 'V_536',
               particles = [ P.b__tilde__, P.d, P.s__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF13, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,3):C.GC_295,(0,4):C.GC_299,(0,5):C.GC_354,(2,5):C.GC_372,(1,1):C.GC_356,(3,1):C.GC_374,(1,0):C.GC_432,(3,0):C.GC_504,(0,2):C.GC_440,(2,2):C.GC_512})

V_537 = Vertex(name = 'V_537',
               particles = [ P.s__tilde__, P.d, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_296,(0,6):C.GC_311,(0,7):C.GC_456,(2,7):C.GC_528,(1,2):C.GC_395,(3,2):C.GC_413,(1,0):C.GC_434,(3,0):C.GC_506,(1,1):C.GC_47,(0,3):C.GC_389,(2,3):C.GC_407,(0,4):C.GC_47})

V_538 = Vertex(name = 'V_538',
               particles = [ P.b__tilde__, P.d, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_318,(0,6):C.GC_312,(0,7):C.GC_457,(2,7):C.GC_529,(1,2):C.GC_464,(3,2):C.GC_536,(1,0):C.GC_435,(3,0):C.GC_507,(1,1):C.GC_51,(0,3):C.GC_442,(2,3):C.GC_514,(0,4):C.GC_48})

V_539 = Vertex(name = 'V_539',
               particles = [ P.s__tilde__, P.d, P.s__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF13, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,3):C.GC_297,(0,4):C.GC_334,(0,5):C.GC_480,(2,5):C.GC_552,(1,1):C.GC_401,(3,1):C.GC_419,(1,0):C.GC_437,(3,0):C.GC_509,(0,2):C.GC_390,(2,2):C.GC_408})

V_540 = Vertex(name = 'V_540',
               particles = [ P.b__tilde__, P.d, P.s__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_343,(0,6):C.GC_335,(0,7):C.GC_481,(2,7):C.GC_553,(1,2):C.GC_488,(3,2):C.GC_560,(1,0):C.GC_438,(3,0):C.GC_510,(1,1):C.GC_64,(0,3):C.GC_445,(2,3):C.GC_517,(0,4):C.GC_59})

V_541 = Vertex(name = 'V_541',
               particles = [ P.b__tilde__, P.d, P.b__tilde__, P.d ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF13, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,3):C.GC_300,(0,4):C.GC_281,(0,5):C.GC_1399,(2,5):C.GC_1408,(1,1):C.GC_1381,(3,1):C.GC_1390,(1,0):C.GC_1435,(3,0):C.GC_1447,(0,2):C.GC_1417,(2,2):C.GC_1426})

V_542 = Vertex(name = 'V_542',
               particles = [ P.b__tilde__, P.d, P.b__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF13, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,3):C.GC_301,(0,4):C.GC_319,(0,5):C.GC_465,(2,5):C.GC_537,(1,1):C.GC_397,(3,1):C.GC_415,(1,0):C.GC_443,(3,0):C.GC_515,(0,2):C.GC_391,(2,2):C.GC_409})

V_543 = Vertex(name = 'V_543',
               particles = [ P.b__tilde__, P.d, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_302,(0,6):C.GC_344,(0,7):C.GC_489,(2,7):C.GC_561,(1,2):C.GC_403,(3,2):C.GC_421,(1,0):C.GC_446,(3,0):C.GC_518,(1,1):C.GC_65,(0,3):C.GC_392,(2,3):C.GC_410,(0,4):C.GC_65})

V_544 = Vertex(name = 'V_544',
               particles = [ P.d__tilde__, P.s, P.d__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF13, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,3):C.GC_306,(0,4):C.GC_282,(0,5):C.GC_1400,(2,5):C.GC_1409,(1,1):C.GC_1382,(3,1):C.GC_1391,(1,0):C.GC_1436,(3,0):C.GC_1448,(0,2):C.GC_1418,(2,2):C.GC_1427})

V_545 = Vertex(name = 'V_545',
               particles = [ P.s__tilde__, P.s, P.d__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_307,(0,6):C.GC_313,(0,7):C.GC_357,(2,7):C.GC_375,(1,2):C.GC_359,(3,2):C.GC_377,(1,0):C.GC_450,(3,0):C.GC_522,(1,1):C.GC_49,(0,3):C.GC_458,(2,3):C.GC_530,(0,4):C.GC_49})

V_546 = Vertex(name = 'V_546',
               particles = [ P.b__tilde__, P.s, P.d__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF13, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,3):C.GC_308,(0,4):C.GC_320,(0,5):C.GC_358,(2,5):C.GC_376,(1,1):C.GC_361,(3,1):C.GC_379,(1,0):C.GC_451,(3,0):C.GC_523,(0,2):C.GC_466,(2,2):C.GC_538})

V_547 = Vertex(name = 'V_547',
               particles = [ P.d__tilde__, P.s, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF13, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,3):C.GC_309,(0,4):C.GC_327,(0,5):C.GC_474,(2,5):C.GC_546,(1,1):C.GC_400,(3,1):C.GC_418,(1,0):C.GC_452,(3,0):C.GC_524,(0,2):C.GC_394,(2,2):C.GC_412})

V_548 = Vertex(name = 'V_548',
               particles = [ P.s__tilde__, P.s, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_336,(0,6):C.GC_328,(0,7):C.GC_475,(2,7):C.GC_547,(1,2):C.GC_482,(3,2):C.GC_554,(1,0):C.GC_453,(3,0):C.GC_525,(1,1):C.GC_60,(0,3):C.GC_460,(2,3):C.GC_532,(0,4):C.GC_56})

V_549 = Vertex(name = 'V_549',
               particles = [ P.b__tilde__, P.s, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_345,(0,6):C.GC_329,(0,7):C.GC_476,(2,7):C.GC_548,(1,2):C.GC_490,(3,2):C.GC_562,(1,0):C.GC_454,(3,0):C.GC_526,(1,1):C.GC_66,(0,3):C.GC_468,(2,3):C.GC_540,(0,4):C.GC_57})

V_550 = Vertex(name = 'V_550',
               particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_314,(0,6):C.GC_283,(0,7):C.GC_1401,(2,7):C.GC_1410,(1,2):C.GC_1383,(3,2):C.GC_1392,(1,0):C.GC_1437,(3,0):C.GC_1449,(1,1):C.GC_703,(0,3):C.GC_1419,(2,3):C.GC_1428,(0,4):C.GC_703})

V_551 = Vertex(name = 'V_551',
               particles = [ P.b__tilde__, P.s, P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_315,(0,6):C.GC_321,(0,7):C.GC_360,(2,7):C.GC_378,(1,2):C.GC_362,(3,2):C.GC_380,(1,0):C.GC_459,(3,0):C.GC_531,(1,1):C.GC_52,(0,3):C.GC_467,(2,3):C.GC_539,(0,4):C.GC_52})

V_552 = Vertex(name = 'V_552',
               particles = [ P.s__tilde__, P.s, P.s__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_316,(0,6):C.GC_337,(0,7):C.GC_483,(2,7):C.GC_555,(1,2):C.GC_402,(3,2):C.GC_420,(1,0):C.GC_461,(3,0):C.GC_533,(1,1):C.GC_61,(0,3):C.GC_396,(2,3):C.GC_414,(0,4):C.GC_61})

V_553 = Vertex(name = 'V_553',
               particles = [ P.b__tilde__, P.s, P.s__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_346,(0,6):C.GC_338,(0,7):C.GC_484,(2,7):C.GC_556,(1,2):C.GC_491,(3,2):C.GC_563,(1,0):C.GC_462,(3,0):C.GC_534,(1,1):C.GC_67,(0,3):C.GC_469,(2,3):C.GC_541,(0,4):C.GC_62})

V_554 = Vertex(name = 'V_554',
               particles = [ P.b__tilde__, P.s, P.b__tilde__, P.s ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF13, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,3):C.GC_322,(0,4):C.GC_284,(0,5):C.GC_1402,(2,5):C.GC_1411,(1,1):C.GC_1384,(3,1):C.GC_1393,(1,0):C.GC_1438,(3,0):C.GC_1450,(0,2):C.GC_1420,(2,2):C.GC_1429})

V_555 = Vertex(name = 'V_555',
               particles = [ P.b__tilde__, P.s, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_323,(0,6):C.GC_347,(0,7):C.GC_492,(2,7):C.GC_564,(1,2):C.GC_404,(3,2):C.GC_422,(1,0):C.GC_470,(3,0):C.GC_542,(1,1):C.GC_68,(0,3):C.GC_398,(2,3):C.GC_416,(0,4):C.GC_68})

V_556 = Vertex(name = 'V_556',
               particles = [ P.d__tilde__, P.b, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF13, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,3):C.GC_330,(0,4):C.GC_285,(0,5):C.GC_1403,(2,5):C.GC_1412,(1,1):C.GC_1385,(3,1):C.GC_1394,(1,0):C.GC_1439,(3,0):C.GC_1451,(0,2):C.GC_1421,(2,2):C.GC_1430})

V_557 = Vertex(name = 'V_557',
               particles = [ P.s__tilde__, P.b, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF13, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,3):C.GC_331,(0,4):C.GC_339,(0,5):C.GC_363,(2,5):C.GC_381,(1,1):C.GC_365,(3,1):C.GC_383,(1,0):C.GC_477,(3,0):C.GC_549,(0,2):C.GC_485,(2,2):C.GC_557})

V_558 = Vertex(name = 'V_558',
               particles = [ P.b__tilde__, P.b, P.d__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_332,(0,6):C.GC_348,(0,7):C.GC_364,(2,7):C.GC_382,(1,2):C.GC_367,(3,2):C.GC_385,(1,0):C.GC_478,(3,0):C.GC_550,(1,1):C.GC_69,(0,3):C.GC_493,(2,3):C.GC_565,(0,4):C.GC_69})

V_559 = Vertex(name = 'V_559',
               particles = [ P.s__tilde__, P.b, P.s__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF13, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,3):C.GC_340,(0,4):C.GC_286,(0,5):C.GC_1404,(2,5):C.GC_1413,(1,1):C.GC_1386,(3,1):C.GC_1395,(1,0):C.GC_1440,(3,0):C.GC_1452,(0,2):C.GC_1422,(2,2):C.GC_1431})

V_560 = Vertex(name = 'V_560',
               particles = [ P.b__tilde__, P.b, P.s__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_341,(0,6):C.GC_349,(0,7):C.GC_366,(2,7):C.GC_384,(1,2):C.GC_368,(3,2):C.GC_386,(1,0):C.GC_486,(3,0):C.GC_558,(1,1):C.GC_70,(0,3):C.GC_494,(2,3):C.GC_566,(0,4):C.GC_70})

V_561 = Vertex(name = 'V_561',
               particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_350,(0,6):C.GC_287,(0,7):C.GC_1405,(2,7):C.GC_1414,(1,2):C.GC_1387,(3,2):C.GC_1396,(1,0):C.GC_1441,(3,0):C.GC_1453,(1,1):C.GC_704,(0,3):C.GC_1423,(2,3):C.GC_1432,(0,4):C.GC_704})

V_562 = Vertex(name = 'V_562',
               particles = [ P.d__tilde__, P.d, P.e__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_568,(0,3):C.GC_766,(0,0):C.GC_1454,(0,1):C.GC_705})

V_563 = Vertex(name = 'V_563',
               particles = [ P.d__tilde__, P.d, P.mu__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_570,(0,3):C.GC_775,(0,0):C.GC_1455,(0,1):C.GC_714})

V_564 = Vertex(name = 'V_564',
               particles = [ P.d__tilde__, P.d, P.ta__plus__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_572,(0,3):C.GC_784,(0,0):C.GC_1456,(0,1):C.GC_723})

V_565 = Vertex(name = 'V_565',
               particles = [ P.s__tilde__, P.d, P.e__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_574,(0,3):C.GC_767,(0,0):C.GC_1457,(0,1):C.GC_706})

V_566 = Vertex(name = 'V_566',
               particles = [ P.s__tilde__, P.d, P.mu__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_576,(0,3):C.GC_776,(0,0):C.GC_1458,(0,1):C.GC_715})

V_567 = Vertex(name = 'V_567',
               particles = [ P.s__tilde__, P.d, P.ta__plus__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_578,(0,3):C.GC_785,(0,0):C.GC_1459,(0,1):C.GC_724})

V_568 = Vertex(name = 'V_568',
               particles = [ P.b__tilde__, P.d, P.e__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_580,(0,3):C.GC_768,(0,0):C.GC_1460,(0,1):C.GC_707})

V_569 = Vertex(name = 'V_569',
               particles = [ P.b__tilde__, P.d, P.mu__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_582,(0,3):C.GC_777,(0,0):C.GC_1461,(0,1):C.GC_716})

V_570 = Vertex(name = 'V_570',
               particles = [ P.b__tilde__, P.d, P.ta__plus__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_584,(0,3):C.GC_786,(0,0):C.GC_1462,(0,1):C.GC_725})

V_571 = Vertex(name = 'V_571',
               particles = [ P.d__tilde__, P.s, P.e__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_586,(0,3):C.GC_769,(0,0):C.GC_1463,(0,1):C.GC_708})

V_572 = Vertex(name = 'V_572',
               particles = [ P.d__tilde__, P.s, P.mu__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_588,(0,3):C.GC_778,(0,0):C.GC_1464,(0,1):C.GC_717})

V_573 = Vertex(name = 'V_573',
               particles = [ P.d__tilde__, P.s, P.ta__plus__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_590,(0,3):C.GC_787,(0,0):C.GC_1465,(0,1):C.GC_726})

V_574 = Vertex(name = 'V_574',
               particles = [ P.s__tilde__, P.s, P.e__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_592,(0,3):C.GC_770,(0,0):C.GC_1466,(0,1):C.GC_709})

V_575 = Vertex(name = 'V_575',
               particles = [ P.s__tilde__, P.s, P.mu__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_594,(0,3):C.GC_779,(0,0):C.GC_1467,(0,1):C.GC_718})

V_576 = Vertex(name = 'V_576',
               particles = [ P.s__tilde__, P.s, P.ta__plus__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_596,(0,3):C.GC_788,(0,0):C.GC_1468,(0,1):C.GC_727})

V_577 = Vertex(name = 'V_577',
               particles = [ P.b__tilde__, P.s, P.e__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_598,(0,3):C.GC_771,(0,0):C.GC_1469,(0,1):C.GC_710})

V_578 = Vertex(name = 'V_578',
               particles = [ P.b__tilde__, P.s, P.mu__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_600,(0,3):C.GC_780,(0,0):C.GC_1470,(0,1):C.GC_719})

V_579 = Vertex(name = 'V_579',
               particles = [ P.b__tilde__, P.s, P.ta__plus__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_602,(0,3):C.GC_789,(0,0):C.GC_1471,(0,1):C.GC_728})

V_580 = Vertex(name = 'V_580',
               particles = [ P.d__tilde__, P.b, P.e__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_604,(0,3):C.GC_772,(0,0):C.GC_1472,(0,1):C.GC_711})

V_581 = Vertex(name = 'V_581',
               particles = [ P.d__tilde__, P.b, P.mu__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_606,(0,3):C.GC_781,(0,0):C.GC_1473,(0,1):C.GC_720})

V_582 = Vertex(name = 'V_582',
               particles = [ P.d__tilde__, P.b, P.ta__plus__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_608,(0,3):C.GC_790,(0,0):C.GC_1474,(0,1):C.GC_729})

V_583 = Vertex(name = 'V_583',
               particles = [ P.s__tilde__, P.b, P.e__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_610,(0,3):C.GC_773,(0,0):C.GC_1475,(0,1):C.GC_712})

V_584 = Vertex(name = 'V_584',
               particles = [ P.s__tilde__, P.b, P.mu__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_612,(0,3):C.GC_782,(0,0):C.GC_1476,(0,1):C.GC_721})

V_585 = Vertex(name = 'V_585',
               particles = [ P.s__tilde__, P.b, P.ta__plus__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_614,(0,3):C.GC_791,(0,0):C.GC_1477,(0,1):C.GC_730})

V_586 = Vertex(name = 'V_586',
               particles = [ P.b__tilde__, P.b, P.e__plus__, P.e__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_616,(0,3):C.GC_774,(0,0):C.GC_1478,(0,1):C.GC_713})

V_587 = Vertex(name = 'V_587',
               particles = [ P.b__tilde__, P.b, P.mu__plus__, P.mu__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_618,(0,3):C.GC_783,(0,0):C.GC_1479,(0,1):C.GC_722})

V_588 = Vertex(name = 'V_588',
               particles = [ P.b__tilde__, P.b, P.ta__plus__, P.ta__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_620,(0,3):C.GC_792,(0,0):C.GC_1480,(0,1):C.GC_731})

V_589 = Vertex(name = 'V_589',
               particles = [ P.e__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(0,5):C.GC_802,(0,6):C.GC_802,(0,7):C.GC_793,(0,2):C.GC_793,(0,0):C.GC_793,(0,1):C.GC_732,(0,3):C.GC_793,(0,4):C.GC_732})

V_590 = Vertex(name = 'V_590',
               particles = [ P.mu__plus__, P.e__minus__, P.e__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
               couplings = {(0,3):C.GC_76,(0,4):C.GC_75,(0,2):C.GC_796,(0,0):C.GC_794,(0,1):C.GC_71})

V_591 = Vertex(name = 'V_591',
               particles = [ P.ta__plus__, P.e__minus__, P.e__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
               couplings = {(0,3):C.GC_79,(0,4):C.GC_77,(0,2):C.GC_799,(0,0):C.GC_795,(0,1):C.GC_72})

V_592 = Vertex(name = 'V_592',
               particles = [ P.mu__plus__, P.mu__minus__, P.mu__plus__, P.mu__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(0,5):C.GC_804,(0,6):C.GC_804,(0,7):C.GC_797,(0,2):C.GC_797,(0,0):C.GC_797,(0,1):C.GC_733,(0,3):C.GC_797,(0,4):C.GC_733})

V_593 = Vertex(name = 'V_593',
               particles = [ P.ta__plus__, P.mu__minus__, P.mu__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF4, L.FFFF6 ],
               couplings = {(0,3):C.GC_80,(0,4):C.GC_78,(0,2):C.GC_800,(0,0):C.GC_798,(0,1):C.GC_73})

V_594 = Vertex(name = 'V_594',
               particles = [ P.ta__plus__, P.ta__minus__, P.ta__plus__, P.ta__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(0,5):C.GC_806,(0,6):C.GC_806,(0,7):C.GC_801,(0,2):C.GC_801,(0,0):C.GC_801,(0,1):C.GC_734,(0,3):C.GC_801,(0,4):C.GC_734})

V_595 = Vertex(name = 'V_595',
               particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_81,(0,3):C.GC_924,(0,0):C.GC_807,(0,1):C.GC_735})

V_596 = Vertex(name = 'V_596',
               particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_83,(0,3):C.GC_927,(0,0):C.GC_808,(0,1):C.GC_736})

V_597 = Vertex(name = 'V_597',
               particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_85,(0,3):C.GC_930,(0,0):C.GC_809,(0,1):C.GC_737})

V_598 = Vertex(name = 'V_598',
               particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_87,(0,3):C.GC_933,(0,0):C.GC_810,(0,1):C.GC_738})

V_599 = Vertex(name = 'V_599',
               particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_89,(0,3):C.GC_936,(0,0):C.GC_811,(0,1):C.GC_739})

V_600 = Vertex(name = 'V_600',
               particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_91,(0,3):C.GC_939,(0,0):C.GC_812,(0,1):C.GC_740})

V_601 = Vertex(name = 'V_601',
               particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_93,(0,3):C.GC_942,(0,0):C.GC_813,(0,1):C.GC_741})

V_602 = Vertex(name = 'V_602',
               particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_95,(0,3):C.GC_945,(0,0):C.GC_814,(0,1):C.GC_742})

V_603 = Vertex(name = 'V_603',
               particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_97,(0,3):C.GC_948,(0,0):C.GC_815,(0,1):C.GC_743})

V_604 = Vertex(name = 'V_604',
               particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_99,(0,3):C.GC_925,(0,0):C.GC_816,(0,1):C.GC_744})

V_605 = Vertex(name = 'V_605',
               particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_101,(0,3):C.GC_928,(0,0):C.GC_817,(0,1):C.GC_745})

V_606 = Vertex(name = 'V_606',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_103,(0,3):C.GC_931,(0,0):C.GC_818,(0,1):C.GC_746})

V_607 = Vertex(name = 'V_607',
               particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_105,(0,3):C.GC_934,(0,0):C.GC_819,(0,1):C.GC_747})

V_608 = Vertex(name = 'V_608',
               particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_107,(0,3):C.GC_937,(0,0):C.GC_820,(0,1):C.GC_748})

V_609 = Vertex(name = 'V_609',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_109,(0,3):C.GC_940,(0,0):C.GC_821,(0,1):C.GC_749})

V_610 = Vertex(name = 'V_610',
               particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_111,(0,3):C.GC_943,(0,0):C.GC_822,(0,1):C.GC_750})

V_611 = Vertex(name = 'V_611',
               particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_113,(0,3):C.GC_946,(0,0):C.GC_823,(0,1):C.GC_751})

V_612 = Vertex(name = 'V_612',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_115,(0,3):C.GC_949,(0,0):C.GC_824,(0,1):C.GC_752})

V_613 = Vertex(name = 'V_613',
               particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_117,(0,3):C.GC_926,(0,0):C.GC_825,(0,1):C.GC_753})

V_614 = Vertex(name = 'V_614',
               particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_119,(0,3):C.GC_929,(0,0):C.GC_826,(0,1):C.GC_754})

V_615 = Vertex(name = 'V_615',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_121,(0,3):C.GC_932,(0,0):C.GC_827,(0,1):C.GC_755})

V_616 = Vertex(name = 'V_616',
               particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_123,(0,3):C.GC_935,(0,0):C.GC_828,(0,1):C.GC_756})

V_617 = Vertex(name = 'V_617',
               particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_125,(0,3):C.GC_938,(0,0):C.GC_829,(0,1):C.GC_757})

V_618 = Vertex(name = 'V_618',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_127,(0,3):C.GC_941,(0,0):C.GC_830,(0,1):C.GC_758})

V_619 = Vertex(name = 'V_619',
               particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_129,(0,3):C.GC_944,(0,0):C.GC_831,(0,1):C.GC_759})

V_620 = Vertex(name = 'V_620',
               particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_131,(0,3):C.GC_947,(0,0):C.GC_832,(0,1):C.GC_760})

V_621 = Vertex(name = 'V_621',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF14, L.FFFF6, L.FFFF9 ],
               couplings = {(0,2):C.GC_133,(0,3):C.GC_950,(0,0):C.GC_833,(0,1):C.GC_761})

V_622 = Vertex(name = 'V_622',
               particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_135,(0,6):C.GC_135,(0,7):C.GC_951,(2,7):C.GC_996,(1,2):C.GC_951,(3,2):C.GC_996,(1,0):C.GC_951,(3,0):C.GC_996,(1,1):C.GC_1131,(0,3):C.GC_951,(2,3):C.GC_996,(0,4):C.GC_1131})

V_623 = Vertex(name = 'V_623',
               particles = [ P.c__tilde__, P.u, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_136,(0,6):C.GC_136,(0,7):C.GC_952,(2,7):C.GC_997,(1,2):C.GC_960,(3,2):C.GC_1005,(1,0):C.GC_952,(3,0):C.GC_997,(1,1):C.GC_168,(0,3):C.GC_960,(2,3):C.GC_1005,(0,4):C.GC_168})

V_624 = Vertex(name = 'V_624',
               particles = [ P.t__tilde__, P.u, P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_137,(0,6):C.GC_137,(0,7):C.GC_953,(2,7):C.GC_998,(1,2):C.GC_963,(3,2):C.GC_1008,(1,0):C.GC_953,(3,0):C.GC_998,(1,1):C.GC_169,(0,3):C.GC_963,(2,3):C.GC_1008,(0,4):C.GC_169})

V_625 = Vertex(name = 'V_625',
               particles = [ P.u__tilde__, P.u, P.u__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_138,(0,6):C.GC_138,(0,7):C.GC_966,(2,7):C.GC_1011,(1,2):C.GC_966,(3,2):C.GC_1011,(1,0):C.GC_954,(3,0):C.GC_999,(1,1):C.GC_170,(0,3):C.GC_954,(2,3):C.GC_999,(0,4):C.GC_170})

V_626 = Vertex(name = 'V_626',
               particles = [ P.c__tilde__, P.u, P.u__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF4, L.FFFF6 ],
               couplings = {(1,4):C.GC_141,(0,5):C.GC_139,(1,2):C.GC_969,(2,2):C.GC_1014,(1,0):C.GC_955,(2,0):C.GC_1000,(1,1):C.GC_173,(0,3):C.GC_171})

V_627 = Vertex(name = 'V_627',
               particles = [ P.t__tilde__, P.u, P.u__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF4, L.FFFF6 ],
               couplings = {(1,4):C.GC_146,(0,5):C.GC_140,(1,2):C.GC_978,(2,2):C.GC_1023,(1,0):C.GC_956,(2,0):C.GC_1001,(1,1):C.GC_177,(0,3):C.GC_172})

V_628 = Vertex(name = 'V_628',
               particles = [ P.u__tilde__, P.u, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_149,(0,6):C.GC_149,(0,7):C.GC_981,(2,7):C.GC_1026,(1,2):C.GC_981,(3,2):C.GC_1026,(1,0):C.GC_957,(3,0):C.GC_1002,(1,1):C.GC_180,(0,3):C.GC_957,(2,3):C.GC_1002,(0,4):C.GC_180})

V_629 = Vertex(name = 'V_629',
               particles = [ P.c__tilde__, P.u, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF4, L.FFFF6 ],
               couplings = {(1,4):C.GC_154,(0,5):C.GC_150,(1,2):C.GC_984,(2,2):C.GC_1029,(1,0):C.GC_958,(2,0):C.GC_1003,(1,1):C.GC_185,(0,3):C.GC_181})

V_630 = Vertex(name = 'V_630',
               particles = [ P.t__tilde__, P.u, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF4, L.FFFF6 ],
               couplings = {(1,4):C.GC_159,(0,5):C.GC_151,(1,2):C.GC_987,(2,2):C.GC_1032,(1,0):C.GC_959,(2,0):C.GC_1004,(1,1):C.GC_190,(0,3):C.GC_182})

V_631 = Vertex(name = 'V_631',
               particles = [ P.c__tilde__, P.u, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_142,(0,6):C.GC_142,(0,7):C.GC_970,(2,7):C.GC_1015,(1,2):C.GC_970,(3,2):C.GC_1015,(1,0):C.GC_961,(3,0):C.GC_1006,(1,1):C.GC_174,(0,3):C.GC_961,(2,3):C.GC_1006,(0,4):C.GC_174})

V_632 = Vertex(name = 'V_632',
               particles = [ P.t__tilde__, P.u, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,3):C.GC_147,(0,4):C.GC_143,(0,5):C.GC_971,(2,5):C.GC_1016,(1,0):C.GC_178,(0,1):C.GC_964,(2,1):C.GC_1009,(0,2):C.GC_175})

V_633 = Vertex(name = 'V_633',
               particles = [ P.t__tilde__, P.u, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF4, L.FFFF6 ],
               couplings = {(1,4):C.GC_160,(0,5):C.GC_155,(1,2):C.GC_988,(2,2):C.GC_1033,(1,0):C.GC_962,(2,0):C.GC_1007,(1,1):C.GC_191,(0,3):C.GC_186})

V_634 = Vertex(name = 'V_634',
               particles = [ P.t__tilde__, P.u, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_161,(0,6):C.GC_161,(0,7):C.GC_989,(2,7):C.GC_1034,(1,2):C.GC_989,(3,2):C.GC_1034,(1,0):C.GC_965,(3,0):C.GC_1010,(1,1):C.GC_192,(0,3):C.GC_965,(2,3):C.GC_1010,(0,4):C.GC_192})

V_635 = Vertex(name = 'V_635',
               particles = [ P.c__tilde__, P.c, P.u__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_144,(0,6):C.GC_144,(0,7):C.GC_967,(2,7):C.GC_1012,(1,2):C.GC_972,(3,2):C.GC_1017,(1,0):C.GC_967,(3,0):C.GC_1012,(1,1):C.GC_176,(0,3):C.GC_972,(2,3):C.GC_1017,(0,4):C.GC_176})

V_636 = Vertex(name = 'V_636',
               particles = [ P.c__tilde__, P.c, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)' ],
               lorentz = [ L.FFFF11, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,3):C.GC_156,(0,4):C.GC_152,(0,5):C.GC_982,(2,5):C.GC_1027,(1,0):C.GC_187,(0,1):C.GC_975,(2,1):C.GC_1020,(0,2):C.GC_183})

V_637 = Vertex(name = 'V_637',
               particles = [ P.t__tilde__, P.c, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF4, L.FFFF6 ],
               couplings = {(1,4):C.GC_162,(0,5):C.GC_153,(1,2):C.GC_990,(2,2):C.GC_1035,(1,0):C.GC_968,(2,0):C.GC_1013,(1,1):C.GC_193,(0,3):C.GC_184})

V_638 = Vertex(name = 'V_638',
               particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_145,(0,6):C.GC_145,(0,7):C.GC_973,(2,7):C.GC_1018,(1,2):C.GC_973,(3,2):C.GC_1018,(1,0):C.GC_973,(3,0):C.GC_1018,(1,1):C.GC_1132,(0,3):C.GC_973,(2,3):C.GC_1018,(0,4):C.GC_1132})

V_639 = Vertex(name = 'V_639',
               particles = [ P.t__tilde__, P.c, P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_148,(0,6):C.GC_148,(0,7):C.GC_974,(2,7):C.GC_1019,(1,2):C.GC_979,(3,2):C.GC_1024,(1,0):C.GC_974,(3,0):C.GC_1019,(1,1):C.GC_179,(0,3):C.GC_979,(2,3):C.GC_1024,(0,4):C.GC_179})

V_640 = Vertex(name = 'V_640',
               particles = [ P.c__tilde__, P.c, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_157,(0,6):C.GC_157,(0,7):C.GC_985,(2,7):C.GC_1030,(1,2):C.GC_985,(3,2):C.GC_1030,(1,0):C.GC_976,(3,0):C.GC_1021,(1,1):C.GC_188,(0,3):C.GC_976,(2,3):C.GC_1021,(0,4):C.GC_188})

V_641 = Vertex(name = 'V_641',
               particles = [ P.t__tilde__, P.c, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF14, L.FFFF4, L.FFFF6 ],
               couplings = {(1,4):C.GC_163,(0,5):C.GC_158,(1,2):C.GC_991,(2,2):C.GC_1036,(1,0):C.GC_977,(2,0):C.GC_1022,(1,1):C.GC_194,(0,3):C.GC_189})

V_642 = Vertex(name = 'V_642',
               particles = [ P.t__tilde__, P.c, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_164,(0,6):C.GC_164,(0,7):C.GC_992,(2,7):C.GC_1037,(1,2):C.GC_992,(3,2):C.GC_1037,(1,0):C.GC_980,(3,0):C.GC_1025,(1,1):C.GC_195,(0,3):C.GC_980,(2,3):C.GC_1025,(0,4):C.GC_195})

V_643 = Vertex(name = 'V_643',
               particles = [ P.t__tilde__, P.t, P.u__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_165,(0,6):C.GC_165,(0,7):C.GC_983,(2,7):C.GC_1028,(1,2):C.GC_993,(3,2):C.GC_1038,(1,0):C.GC_983,(3,0):C.GC_1028,(1,1):C.GC_196,(0,3):C.GC_993,(2,3):C.GC_1038,(0,4):C.GC_196})

V_644 = Vertex(name = 'V_644',
               particles = [ P.t__tilde__, P.t, P.c__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_166,(0,6):C.GC_166,(0,7):C.GC_986,(2,7):C.GC_1031,(1,2):C.GC_994,(3,2):C.GC_1039,(1,0):C.GC_986,(3,0):C.GC_1031,(1,1):C.GC_197,(0,3):C.GC_994,(2,3):C.GC_1039,(0,4):C.GC_197})

V_645 = Vertex(name = 'V_645',
               particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF10, L.FFFF11, L.FFFF12, L.FFFF13, L.FFFF14, L.FFFF4, L.FFFF6, L.FFFF9 ],
               couplings = {(1,5):C.GC_167,(0,6):C.GC_167,(0,7):C.GC_995,(2,7):C.GC_1040,(1,2):C.GC_995,(3,2):C.GC_1040,(1,0):C.GC_995,(3,0):C.GC_1040,(1,1):C.GC_1133,(0,3):C.GC_995,(2,3):C.GC_1040,(0,4):C.GC_1133})

V_646 = Vertex(name = 'V_646',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1481})

V_647 = Vertex(name = 'V_647',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1482})

V_648 = Vertex(name = 'V_648',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1483})

V_649 = Vertex(name = 'V_649',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1484})

V_650 = Vertex(name = 'V_650',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1485})

V_651 = Vertex(name = 'V_651',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1486})

V_652 = Vertex(name = 'V_652',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1487})

V_653 = Vertex(name = 'V_653',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1488})

V_654 = Vertex(name = 'V_654',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1489})

V_655 = Vertex(name = 'V_655',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1490})

V_656 = Vertex(name = 'V_656',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1491})

V_657 = Vertex(name = 'V_657',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1492})

V_658 = Vertex(name = 'V_658',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1493})

V_659 = Vertex(name = 'V_659',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1494})

V_660 = Vertex(name = 'V_660',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1495})

V_661 = Vertex(name = 'V_661',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF3 ],
               couplings = {(0,0):C.GC_1496})

V_662 = Vertex(name = 'V_662',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1497})

V_663 = Vertex(name = 'V_663',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1498})

V_664 = Vertex(name = 'V_664',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1499})

V_665 = Vertex(name = 'V_665',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1500})

V_666 = Vertex(name = 'V_666',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1501})

V_667 = Vertex(name = 'V_667',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1502})

V_668 = Vertex(name = 'V_668',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1503})

V_669 = Vertex(name = 'V_669',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1504})

V_670 = Vertex(name = 'V_670',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1505})

V_671 = Vertex(name = 'V_671',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1506})

V_672 = Vertex(name = 'V_672',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1507})

V_673 = Vertex(name = 'V_673',
               particles = [ P.u__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1508})

V_674 = Vertex(name = 'V_674',
               particles = [ P.c__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1509})

V_675 = Vertex(name = 'V_675',
               particles = [ P.t__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1510})

V_676 = Vertex(name = 'V_676',
               particles = [ P.u__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1511})

V_677 = Vertex(name = 'V_677',
               particles = [ P.c__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1512})

V_678 = Vertex(name = 'V_678',
               particles = [ P.t__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1513})

V_679 = Vertex(name = 'V_679',
               particles = [ P.u__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1514})

V_680 = Vertex(name = 'V_680',
               particles = [ P.c__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1515})

V_681 = Vertex(name = 'V_681',
               particles = [ P.t__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1516})

V_682 = Vertex(name = 'V_682',
               particles = [ P.u__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1517})

V_683 = Vertex(name = 'V_683',
               particles = [ P.c__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1518})

V_684 = Vertex(name = 'V_684',
               particles = [ P.t__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1519})

V_685 = Vertex(name = 'V_685',
               particles = [ P.u__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1520})

V_686 = Vertex(name = 'V_686',
               particles = [ P.c__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1521})

V_687 = Vertex(name = 'V_687',
               particles = [ P.t__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1522})

V_688 = Vertex(name = 'V_688',
               particles = [ P.u__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1523})

V_689 = Vertex(name = 'V_689',
               particles = [ P.c__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1524})

V_690 = Vertex(name = 'V_690',
               particles = [ P.t__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1525})

V_691 = Vertex(name = 'V_691',
               particles = [ P.u__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1526})

V_692 = Vertex(name = 'V_692',
               particles = [ P.c__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1527})

V_693 = Vertex(name = 'V_693',
               particles = [ P.t__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1528})

V_694 = Vertex(name = 'V_694',
               particles = [ P.u__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1529})

V_695 = Vertex(name = 'V_695',
               particles = [ P.c__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1530})

V_696 = Vertex(name = 'V_696',
               particles = [ P.t__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1531})

V_697 = Vertex(name = 'V_697',
               particles = [ P.u__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1532})

V_698 = Vertex(name = 'V_698',
               particles = [ P.c__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1533})

V_699 = Vertex(name = 'V_699',
               particles = [ P.t__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_1534})

V_700 = Vertex(name = 'V_700',
               particles = [ P.e__plus__, P.e__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_802,(0,1):C.GC_793})

V_701 = Vertex(name = 'V_701',
               particles = [ P.e__plus__, P.e__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_76,(0,1):C.GC_796})

V_702 = Vertex(name = 'V_702',
               particles = [ P.e__plus__, P.e__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF3, L.FFFF6, L.FFFF9 ],
               couplings = {(0,1):C.GC_803,(0,0):C.GC_805,(0,2):C.GC_799})

V_703 = Vertex(name = 'V_703',
               particles = [ P.mu__plus__, P.e__minus__, P.ve__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_75})

V_704 = Vertex(name = 'V_704',
               particles = [ P.ta__plus__, P.e__minus__, P.ve__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_77})

V_705 = Vertex(name = 'V_705',
               particles = [ P.e__plus__, P.mu__minus__, P.vm__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_75})

V_706 = Vertex(name = 'V_706',
               particles = [ P.mu__plus__, P.mu__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_76,(0,1):C.GC_794})

V_707 = Vertex(name = 'V_707',
               particles = [ P.mu__plus__, P.mu__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_804,(0,1):C.GC_797})

V_708 = Vertex(name = 'V_708',
               particles = [ P.mu__plus__, P.mu__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_80,(0,1):C.GC_800})

V_709 = Vertex(name = 'V_709',
               particles = [ P.ta__plus__, P.mu__minus__, P.vm__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_78})

V_710 = Vertex(name = 'V_710',
               particles = [ P.e__plus__, P.ta__minus__, P.vt__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_77})

V_711 = Vertex(name = 'V_711',
               particles = [ P.mu__plus__, P.ta__minus__, P.vt__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF6 ],
               couplings = {(0,0):C.GC_78})

V_712 = Vertex(name = 'V_712',
               particles = [ P.ta__plus__, P.ta__minus__, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_79,(0,1):C.GC_795})

V_713 = Vertex(name = 'V_713',
               particles = [ P.ta__plus__, P.ta__minus__, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_80,(0,1):C.GC_798})

V_714 = Vertex(name = 'V_714',
               particles = [ P.ta__plus__, P.ta__minus__, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_806,(0,1):C.GC_801})

V_715 = Vertex(name = 'V_715',
               particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_82,(0,1):C.GC_807})

V_716 = Vertex(name = 'V_716',
               particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_100,(0,1):C.GC_816})

V_717 = Vertex(name = 'V_717',
               particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_118,(0,1):C.GC_825})

V_718 = Vertex(name = 'V_718',
               particles = [ P.c__tilde__, P.u, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_84,(0,1):C.GC_808})

V_719 = Vertex(name = 'V_719',
               particles = [ P.c__tilde__, P.u, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_102,(0,1):C.GC_817})

V_720 = Vertex(name = 'V_720',
               particles = [ P.c__tilde__, P.u, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_120,(0,1):C.GC_826})

V_721 = Vertex(name = 'V_721',
               particles = [ P.t__tilde__, P.u, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_86,(0,1):C.GC_809})

V_722 = Vertex(name = 'V_722',
               particles = [ P.t__tilde__, P.u, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_104,(0,1):C.GC_818})

V_723 = Vertex(name = 'V_723',
               particles = [ P.t__tilde__, P.u, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_122,(0,1):C.GC_827})

V_724 = Vertex(name = 'V_724',
               particles = [ P.u__tilde__, P.c, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_88,(0,1):C.GC_810})

V_725 = Vertex(name = 'V_725',
               particles = [ P.u__tilde__, P.c, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_106,(0,1):C.GC_819})

V_726 = Vertex(name = 'V_726',
               particles = [ P.u__tilde__, P.c, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_124,(0,1):C.GC_828})

V_727 = Vertex(name = 'V_727',
               particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_90,(0,1):C.GC_811})

V_728 = Vertex(name = 'V_728',
               particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_108,(0,1):C.GC_820})

V_729 = Vertex(name = 'V_729',
               particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_126,(0,1):C.GC_829})

V_730 = Vertex(name = 'V_730',
               particles = [ P.t__tilde__, P.c, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_92,(0,1):C.GC_812})

V_731 = Vertex(name = 'V_731',
               particles = [ P.t__tilde__, P.c, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_110,(0,1):C.GC_821})

V_732 = Vertex(name = 'V_732',
               particles = [ P.t__tilde__, P.c, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_128,(0,1):C.GC_830})

V_733 = Vertex(name = 'V_733',
               particles = [ P.u__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_94,(0,1):C.GC_813})

V_734 = Vertex(name = 'V_734',
               particles = [ P.u__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_112,(0,1):C.GC_822})

V_735 = Vertex(name = 'V_735',
               particles = [ P.u__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_130,(0,1):C.GC_831})

V_736 = Vertex(name = 'V_736',
               particles = [ P.c__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_96,(0,1):C.GC_814})

V_737 = Vertex(name = 'V_737',
               particles = [ P.c__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_114,(0,1):C.GC_823})

V_738 = Vertex(name = 'V_738',
               particles = [ P.c__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_132,(0,1):C.GC_832})

V_739 = Vertex(name = 'V_739',
               particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_98,(0,1):C.GC_815})

V_740 = Vertex(name = 'V_740',
               particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_116,(0,1):C.GC_824})

V_741 = Vertex(name = 'V_741',
               particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_134,(0,1):C.GC_833})

V_742 = Vertex(name = 'V_742',
               particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_567,(0,1):C.GC_766})

V_743 = Vertex(name = 'V_743',
               particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_569,(0,1):C.GC_775})

V_744 = Vertex(name = 'V_744',
               particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_571,(0,1):C.GC_784})

V_745 = Vertex(name = 'V_745',
               particles = [ P.s__tilde__, P.d, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_573,(0,1):C.GC_767})

V_746 = Vertex(name = 'V_746',
               particles = [ P.s__tilde__, P.d, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_575,(0,1):C.GC_776})

V_747 = Vertex(name = 'V_747',
               particles = [ P.s__tilde__, P.d, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_577,(0,1):C.GC_785})

V_748 = Vertex(name = 'V_748',
               particles = [ P.b__tilde__, P.d, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_579,(0,1):C.GC_768})

V_749 = Vertex(name = 'V_749',
               particles = [ P.b__tilde__, P.d, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_581,(0,1):C.GC_777})

V_750 = Vertex(name = 'V_750',
               particles = [ P.b__tilde__, P.d, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_583,(0,1):C.GC_786})

V_751 = Vertex(name = 'V_751',
               particles = [ P.d__tilde__, P.s, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_585,(0,1):C.GC_769})

V_752 = Vertex(name = 'V_752',
               particles = [ P.d__tilde__, P.s, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_587,(0,1):C.GC_778})

V_753 = Vertex(name = 'V_753',
               particles = [ P.d__tilde__, P.s, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_589,(0,1):C.GC_787})

V_754 = Vertex(name = 'V_754',
               particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_591,(0,1):C.GC_770})

V_755 = Vertex(name = 'V_755',
               particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_593,(0,1):C.GC_779})

V_756 = Vertex(name = 'V_756',
               particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_595,(0,1):C.GC_788})

V_757 = Vertex(name = 'V_757',
               particles = [ P.b__tilde__, P.s, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_597,(0,1):C.GC_771})

V_758 = Vertex(name = 'V_758',
               particles = [ P.b__tilde__, P.s, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_599,(0,1):C.GC_780})

V_759 = Vertex(name = 'V_759',
               particles = [ P.b__tilde__, P.s, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_601,(0,1):C.GC_789})

V_760 = Vertex(name = 'V_760',
               particles = [ P.d__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_603,(0,1):C.GC_772})

V_761 = Vertex(name = 'V_761',
               particles = [ P.d__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_605,(0,1):C.GC_781})

V_762 = Vertex(name = 'V_762',
               particles = [ P.d__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_607,(0,1):C.GC_790})

V_763 = Vertex(name = 'V_763',
               particles = [ P.s__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_609,(0,1):C.GC_773})

V_764 = Vertex(name = 'V_764',
               particles = [ P.s__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_611,(0,1):C.GC_782})

V_765 = Vertex(name = 'V_765',
               particles = [ P.s__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_613,(0,1):C.GC_791})

V_766 = Vertex(name = 'V_766',
               particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_615,(0,1):C.GC_774})

V_767 = Vertex(name = 'V_767',
               particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_617,(0,1):C.GC_783})

V_768 = Vertex(name = 'V_768',
               particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF6, L.FFFF9 ],
               couplings = {(0,0):C.GC_619,(0,1):C.GC_792})

V_769 = Vertex(name = 'V_769',
               particles = [ P.ve__tilde__, P.ve, P.ve__tilde__, P.ve ],
               color = [ '1' ],
               lorentz = [ L.FFFF4, L.FFFF6 ],
               couplings = {(0,0):C.GC_802,(0,1):C.GC_802})

V_770 = Vertex(name = 'V_770',
               particles = [ P.vm__tilde__, P.ve, P.ve__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF4, L.FFFF6 ],
               couplings = {(0,0):C.GC_76,(0,1):C.GC_75})

V_771 = Vertex(name = 'V_771',
               particles = [ P.vt__tilde__, P.ve, P.ve__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF4, L.FFFF6 ],
               couplings = {(0,0):C.GC_79,(0,1):C.GC_77})

V_772 = Vertex(name = 'V_772',
               particles = [ P.vm__tilde__, P.vm, P.vm__tilde__, P.vm ],
               color = [ '1' ],
               lorentz = [ L.FFFF4, L.FFFF6 ],
               couplings = {(0,0):C.GC_804,(0,1):C.GC_804})

V_773 = Vertex(name = 'V_773',
               particles = [ P.vt__tilde__, P.vm, P.vm__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF4, L.FFFF6 ],
               couplings = {(0,0):C.GC_80,(0,1):C.GC_78})

V_774 = Vertex(name = 'V_774',
               particles = [ P.vt__tilde__, P.vt, P.vt__tilde__, P.vt ],
               color = [ '1' ],
               lorentz = [ L.FFFF4, L.FFFF6 ],
               couplings = {(0,0):C.GC_806,(0,1):C.GC_806})

V_775 = Vertex(name = 'V_775',
               particles = [ P.b__tilde__, P.b, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS7 ],
               couplings = {(0,0):C.GC_2022})

V_776 = Vertex(name = 'V_776',
               particles = [ P.t__tilde__, P.t, P.g, P.H ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFVS7 ],
               couplings = {(0,0):C.GC_2057})

V_777 = Vertex(name = 'V_777',
               particles = [ P.b__tilde__, P.b, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS3 ],
               couplings = {(0,0):C.GC_2024})

V_778 = Vertex(name = 'V_778',
               particles = [ P.b__tilde__, P.b, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV3 ],
               couplings = {(0,0):C.GC_2030})

V_779 = Vertex(name = 'V_779',
               particles = [ P.t__tilde__, P.t, P.g, P.g, P.H ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVVS3 ],
               couplings = {(0,0):C.GC_2059})

V_780 = Vertex(name = 'V_780',
               particles = [ P.t__tilde__, P.t, P.g, P.g ],
               color = [ 'f(-1,3,4)*T(-1,2,1)' ],
               lorentz = [ L.FFVV3 ],
               couplings = {(0,0):C.GC_2065})

V_781 = Vertex(name = 'V_781',
               particles = [ P.b__tilde__, P.u, P.a, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_1575})

V_782 = Vertex(name = 'V_782',
               particles = [ P.b__tilde__, P.c, P.a, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_1576})

V_783 = Vertex(name = 'V_783',
               particles = [ P.d__tilde__, P.t, P.a, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1 ],
               couplings = {(0,0):C.GC_1572})

V_784 = Vertex(name = 'V_784',
               particles = [ P.s__tilde__, P.t, P.a, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1 ],
               couplings = {(0,0):C.GC_1573})

V_785 = Vertex(name = 'V_785',
               particles = [ P.b__tilde__, P.t, P.a, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS2 ],
               couplings = {(0,0):C.GC_1574,(0,1):C.GC_1577})

V_786 = Vertex(name = 'V_786',
               particles = [ P.b__tilde__, P.u, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_1784})

V_787 = Vertex(name = 'V_787',
               particles = [ P.b__tilde__, P.c, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_1785})

V_788 = Vertex(name = 'V_788',
               particles = [ P.d__tilde__, P.t, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1 ],
               couplings = {(0,0):C.GC_1781})

V_789 = Vertex(name = 'V_789',
               particles = [ P.s__tilde__, P.t, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1 ],
               couplings = {(0,0):C.GC_1782})

V_790 = Vertex(name = 'V_790',
               particles = [ P.b__tilde__, P.t, P.a, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_1783,(0,1):C.GC_1786})

V_791 = Vertex(name = 'V_791',
               particles = [ P.t__tilde__, P.d, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_1581})

V_792 = Vertex(name = 'V_792',
               particles = [ P.t__tilde__, P.s, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_1582})

V_793 = Vertex(name = 'V_793',
               particles = [ P.u__tilde__, P.b, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1 ],
               couplings = {(0,0):C.GC_1578})

V_794 = Vertex(name = 'V_794',
               particles = [ P.c__tilde__, P.b, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1 ],
               couplings = {(0,0):C.GC_1579})

V_795 = Vertex(name = 'V_795',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS2 ],
               couplings = {(0,0):C.GC_1580,(0,1):C.GC_1583})

V_796 = Vertex(name = 'V_796',
               particles = [ P.t__tilde__, P.d, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_1790})

V_797 = Vertex(name = 'V_797',
               particles = [ P.t__tilde__, P.s, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_1791})

V_798 = Vertex(name = 'V_798',
               particles = [ P.u__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1 ],
               couplings = {(0,0):C.GC_1787})

V_799 = Vertex(name = 'V_799',
               particles = [ P.c__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1 ],
               couplings = {(0,0):C.GC_1788})

V_800 = Vertex(name = 'V_800',
               particles = [ P.t__tilde__, P.b, P.a, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_1789,(0,1):C.GC_1792})

V_801 = Vertex(name = 'V_801',
               particles = [ P.b__tilde__, P.b, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS3 ],
               couplings = {(0,0):C.GC_2025})

V_802 = Vertex(name = 'V_802',
               particles = [ P.b__tilde__, P.b, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV3 ],
               couplings = {(0,0):C.GC_2031})

V_803 = Vertex(name = 'V_803',
               particles = [ P.t__tilde__, P.t, P.W__minus__, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS3 ],
               couplings = {(0,0):C.GC_2060})

V_804 = Vertex(name = 'V_804',
               particles = [ P.t__tilde__, P.t, P.W__minus__, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV3 ],
               couplings = {(0,0):C.GC_2066})

V_805 = Vertex(name = 'V_805',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_1342})

V_806 = Vertex(name = 'V_806',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_1345})

V_807 = Vertex(name = 'V_807',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1 ],
               couplings = {(0,0):C.GC_1333})

V_808 = Vertex(name = 'V_808',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1 ],
               couplings = {(0,0):C.GC_1336})

V_809 = Vertex(name = 'V_809',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS2 ],
               couplings = {(0,0):C.GC_1339,(0,1):C.GC_1348})

V_810 = Vertex(name = 'V_810',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_1743})

V_811 = Vertex(name = 'V_811',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_1746})

V_812 = Vertex(name = 'V_812',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1 ],
               couplings = {(0,0):C.GC_1734})

V_813 = Vertex(name = 'V_813',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1 ],
               couplings = {(0,0):C.GC_1737})

V_814 = Vertex(name = 'V_814',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_1740,(0,1):C.GC_1749})

V_815 = Vertex(name = 'V_815',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_1369})

V_816 = Vertex(name = 'V_816',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS2 ],
               couplings = {(0,0):C.GC_1372})

V_817 = Vertex(name = 'V_817',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1 ],
               couplings = {(0,0):C.GC_1360})

V_818 = Vertex(name = 'V_818',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1 ],
               couplings = {(0,0):C.GC_1363})

V_819 = Vertex(name = 'V_819',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVVS1, L.FFVVS2 ],
               couplings = {(0,0):C.GC_1366,(0,1):C.GC_1375})

V_820 = Vertex(name = 'V_820',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_1770})

V_821 = Vertex(name = 'V_821',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV2 ],
               couplings = {(0,0):C.GC_1773})

V_822 = Vertex(name = 'V_822',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1 ],
               couplings = {(0,0):C.GC_1761})

V_823 = Vertex(name = 'V_823',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1 ],
               couplings = {(0,0):C.GC_1764})

V_824 = Vertex(name = 'V_824',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVV1, L.FFVV2 ],
               couplings = {(0,0):C.GC_1767,(0,1):C.GC_1776})

