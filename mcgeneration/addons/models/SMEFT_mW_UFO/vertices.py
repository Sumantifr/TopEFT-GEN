# This file was automatically created by FeynRules 2.3.24
# Mathematica version: 10.2.0 for Mac OS X x86 (64-bit) (July 29, 2015)
# Date: Mon 5 Feb 2018 23:25:27


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1, L.SSSS2 ],
             couplings = {(0,0):C.GC_5184,(0,1):C.GC_109})

V_2 = Vertex(name = 'V_2',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_4360})

V_3 = Vertex(name = 'V_3',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_5186})

V_4 = Vertex(name = 'V_4',
             particles = [ P.H, P.H, P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSSSS1 ],
             couplings = {(0,0):C.GC_1217})

V_5 = Vertex(name = 'V_5',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1, L.SSS2 ],
             couplings = {(0,0):C.GC_4361,(0,1):C.GC_4997})

V_6 = Vertex(name = 'V_6',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_5287})

V_7 = Vertex(name = 'V_7',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_4878})

V_8 = Vertex(name = 'V_8',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_5289})

V_9 = Vertex(name = 'V_9',
             particles = [ P.H, P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSSS1 ],
             couplings = {(0,0):C.GC_4687})

V_10 = Vertex(name = 'V_10',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS3, L.VVS4 ],
              couplings = {(0,0):C.GC_5180,(0,2):C.GC_4644,(0,1):C.GC_4634})

V_11 = Vertex(name = 'V_11',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3, L.VVS4 ],
              couplings = {(0,1):C.GC_5177,(0,0):C.GC_5172})

V_12 = Vertex(name = 'V_12',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_5174})

V_13 = Vertex(name = 'V_13',
              particles = [ P.a, P.a, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_5291})

V_14 = Vertex(name = 'V_14',
              particles = [ P.a, P.a, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2, L.VVSS3, L.VVSS4 ],
              couplings = {(0,0):C.GC_4640,(0,2):C.GC_4637,(0,1):C.GC_4630})

V_15 = Vertex(name = 'V_15',
              particles = [ P.a, P.a, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_4633})

V_16 = Vertex(name = 'V_16',
              particles = [ P.a, P.a, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_5283})

V_17 = Vertex(name = 'V_17',
              particles = [ P.a, P.a, P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSSSS1 ],
              couplings = {(0,0):C.GC_4643})

V_18 = Vertex(name = 'V_18',
              particles = [ P.a, P.a, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSSS1 ],
              couplings = {(0,0):C.GC_5183})

V_19 = Vertex(name = 'V_19',
              particles = [ P.g, P.g, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVS2, L.VVS4 ],
              couplings = {(0,0):C.GC_4689,(0,1):C.GC_4646})

V_20 = Vertex(name = 'V_20',
              particles = [ P.g, P.g, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVS4 ],
              couplings = {(0,0):C.GC_4688})

V_21 = Vertex(name = 'V_21',
              particles = [ P.g, P.g, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.VVSS2, L.VVSS4 ],
              couplings = {(0,0):C.GC_1219,(0,1):C.GC_1218})

V_22 = Vertex(name = 'V_22',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS3, L.VVSS4 ],
              couplings = {(0,0):C.GC_1221,(0,2):C.GC_1220,(0,1):C.GC_30})

V_23 = Vertex(name = 'V_23',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_33})

V_24 = Vertex(name = 'V_24',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_5185})

V_25 = Vertex(name = 'V_25',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS3, L.VVS4 ],
              couplings = {(0,0):C.GC_4691,(0,2):C.GC_4690,(0,1):C.GC_36})

V_26 = Vertex(name = 'V_26',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_4649})

V_27 = Vertex(name = 'V_27',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_4650})

V_28 = Vertex(name = 'V_28',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_5288})

V_29 = Vertex(name = 'V_29',
              particles = [ P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVV1, L.VVV3, L.VVV5, L.VVV6, L.VVV7, L.VVV9 ],
              couplings = {(0,0):C.GC_4974,(0,1):C.GC_4996,(0,5):C.GC_4378,(0,4):C.GC_4377,(0,2):C.GC_5267,(0,3):C.GC_4973})

V_30 = Vertex(name = 'V_30',
              particles = [ P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVV5 ],
              couplings = {(0,0):C.GC_4367})

V_31 = Vertex(name = 'V_31',
              particles = [ P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVV5 ],
              couplings = {(0,0):C.GC_4373})

V_32 = Vertex(name = 'V_32',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS3, L.VVS4 ],
              couplings = {(0,0):C.GC_5179,(0,2):C.GC_4645,(0,1):C.GC_4632})

V_33 = Vertex(name = 'V_33',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3, L.VVS4 ],
              couplings = {(0,1):C.GC_5178,(0,0):C.GC_5171})

V_34 = Vertex(name = 'V_34',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_5173})

V_35 = Vertex(name = 'V_35',
              particles = [ P.a, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_5292})

V_36 = Vertex(name = 'V_36',
              particles = [ P.a, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS3, L.VVSS4 ],
              couplings = {(0,0):C.GC_4639,(0,2):C.GC_4638,(0,1):C.GC_4629})

V_37 = Vertex(name = 'V_37',
              particles = [ P.a, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_4631})

V_38 = Vertex(name = 'V_38',
              particles = [ P.a, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_5285})

V_39 = Vertex(name = 'V_39',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2, L.VVSS3, L.VVSS4 ],
              couplings = {(0,0):C.GC_4636,(0,2):C.GC_4635,(0,1):C.GC_5282})

V_40 = Vertex(name = 'V_40',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_4626})

V_41 = Vertex(name = 'V_41',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3 ],
              couplings = {(0,0):C.GC_4627})

V_42 = Vertex(name = 'V_42',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS2, L.VVS3, L.VVS4 ],
              couplings = {(0,0):C.GC_5176,(0,2):C.GC_5175,(0,1):C.GC_4628})

V_43 = Vertex(name = 'V_43',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_5290})

V_44 = Vertex(name = 'V_44',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_5169})

V_45 = Vertex(name = 'V_45',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS3 ],
              couplings = {(0,0):C.GC_5170})

V_46 = Vertex(name = 'V_46',
              particles = [ P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVV2, L.VVV3, L.VVV4, L.VVV5, L.VVV7, L.VVV9 ],
              couplings = {(0,1):C.GC_4975,(0,0):C.GC_4995,(0,5):C.GC_2396,(0,4):C.GC_2395,(0,3):C.GC_13,(0,2):C.GC_4994})

V_47 = Vertex(name = 'V_47',
              particles = [ P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVV5 ],
              couplings = {(0,0):C.GC_29})

V_48 = Vertex(name = 'V_48',
              particles = [ P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVV5 ],
              couplings = {(0,0):C.GC_5280})

V_49 = Vertex(name = 'V_49',
              particles = [ P.g, P.g, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV3, L.VVV5, L.VVV7, L.VVV8 ],
              couplings = {(0,0):C.GC_4957,(0,3):C.GC_1216,(0,2):C.GC_1215,(0,1):C.GC_15})

V_50 = Vertex(name = 'V_50',
              particles = [ P.ghG, P.ghG__tilde__, P.g ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.UUV1 ],
              couplings = {(0,0):C.GC_15})

V_51 = Vertex(name = 'V_51',
              particles = [ P.g, P.g, P.g, P.H, P.H ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVSS3, L.VVVSS6 ],
              couplings = {(0,0):C.GC_2410,(0,1):C.GC_2409})

V_52 = Vertex(name = 'V_52',
              particles = [ P.g, P.g, P.g, P.H ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVS3, L.VVVS6 ],
              couplings = {(0,0):C.GC_4720,(0,1):C.GC_4647})

V_53 = Vertex(name = 'V_53',
              particles = [ P.g, P.g, P.g, P.H ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVVS6 ],
              couplings = {(0,0):C.GC_4719})

V_54 = Vertex(name = 'V_54',
              particles = [ P.g, P.g, P.g, P.g, P.H, P.H ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVVSS1, L.VVVVSS3, L.VVVVSS4 ],
              couplings = {(1,1):C.GC_2424,(0,0):C.GC_2424,(2,2):C.GC_2424})

V_55 = Vertex(name = 'V_55',
              particles = [ P.g, P.g, P.g, P.g, P.H ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVVS1, L.VVVVS3, L.VVVVS4 ],
              couplings = {(1,1):C.GC_4648,(0,0):C.GC_4648,(2,2):C.GC_4648})

V_56 = Vertex(name = 'V_56',
              particles = [ P.g, P.g, P.g, P.g, P.H ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVVS1, L.VVVVS3, L.VVVVS4 ],
              couplings = {(1,1):C.GC_4730,(0,0):C.GC_4730,(2,2):C.GC_4730})

V_57 = Vertex(name = 'V_57',
              particles = [ P.g, P.g, P.g, P.g ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV10, L.VVVV12, L.VVVV13, L.VVVV2, L.VVVV3, L.VVVV4, L.VVVV6, L.VVVV9 ],
              couplings = {(0,7):C.GC_2408,(1,6):C.GC_2407,(2,5):C.GC_2407,(0,4):C.GC_2406,(1,3):C.GC_2406,(2,2):C.GC_2406,(1,8):C.GC_16,(0,0):C.GC_16,(2,1):C.GC_16})

V_58 = Vertex(name = 'V_58',
              particles = [ P.g, P.g, P.g, P.g, P.g ],
              color = [ 'f(-2,1,2)*f(-1,-2,3)*f(4,5,-1)', 'f(-2,1,2)*f(-1,-2,4)*f(3,5,-1)', 'f(-2,1,2)*f(-1,-2,5)*f(3,4,-1)', 'f(-2,1,3)*f(-1,-2,2)*f(4,5,-1)', 'f(-2,1,3)*f(-1,-2,4)*f(2,5,-1)', 'f(-2,1,3)*f(-1,-2,5)*f(2,4,-1)', 'f(-2,1,4)*f(-1,-2,2)*f(3,5,-1)', 'f(-2,1,4)*f(-1,-2,3)*f(2,5,-1)', 'f(-2,1,4)*f(-1,-2,5)*f(2,3,-1)', 'f(-2,1,5)*f(-1,-2,2)*f(3,4,-1)', 'f(-2,1,5)*f(-1,-2,3)*f(2,4,-1)', 'f(-2,1,5)*f(-1,-2,4)*f(2,3,-1)', 'f(-2,2,3)*f(-1,-2,1)*f(4,5,-1)', 'f(-2,2,3)*f(-1,-2,4)*f(1,5,-1)', 'f(-2,2,3)*f(-1,-2,5)*f(1,4,-1)', 'f(-2,2,4)*f(-1,-2,1)*f(3,5,-1)', 'f(-2,2,4)*f(-1,-2,3)*f(1,5,-1)', 'f(-2,2,4)*f(-1,-2,5)*f(1,3,-1)', 'f(-2,2,5)*f(-1,-2,1)*f(3,4,-1)', 'f(-2,2,5)*f(-1,-2,3)*f(1,4,-1)', 'f(-2,2,5)*f(-1,-2,4)*f(1,3,-1)', 'f(-2,3,4)*f(-1,-2,1)*f(2,5,-1)', 'f(-2,3,4)*f(-1,-2,2)*f(1,5,-1)', 'f(-2,3,4)*f(-1,-2,5)*f(1,2,-1)', 'f(-2,3,5)*f(-1,-2,1)*f(2,4,-1)', 'f(-2,3,5)*f(-1,-2,2)*f(1,4,-1)', 'f(-2,3,5)*f(-1,-2,4)*f(1,2,-1)', 'f(-2,4,5)*f(-1,-2,1)*f(2,3,-1)', 'f(-2,4,5)*f(-1,-2,2)*f(1,3,-1)', 'f(-2,4,5)*f(-1,-2,3)*f(1,2,-1)' ],
              lorentz = [ L.VVVVV1, L.VVVVV10, L.VVVVV11, L.VVVVV12, L.VVVVV13, L.VVVVV14, L.VVVVV15, L.VVVVV17, L.VVVVV18, L.VVVVV19, L.VVVVV2, L.VVVVV20, L.VVVVV21, L.VVVVV22, L.VVVVV23, L.VVVVV24, L.VVVVV25, L.VVVVV28, L.VVVVV29, L.VVVVV3, L.VVVVV30, L.VVVVV31, L.VVVVV33, L.VVVVV34, L.VVVVV35, L.VVVVV36, L.VVVVV37, L.VVVVV4, L.VVVVV40, L.VVVVV41, L.VVVVV42, L.VVVVV43, L.VVVVV44, L.VVVVV46, L.VVVVV47, L.VVVVV48, L.VVVVV49, L.VVVVV5, L.VVVVV50, L.VVVVV51, L.VVVVV53, L.VVVVV54, L.VVVVV6, L.VVVVV7, L.VVVVV9 ],
              couplings = {(27,37):C.GC_2422,(24,8):C.GC_2423,(21,12):C.GC_2422,(18,11):C.GC_2423,(15,9):C.GC_2422,(12,27):C.GC_2422,(28,42):C.GC_2422,(25,15):C.GC_2423,(22,14):C.GC_2422,(9,16):C.GC_2422,(6,13):C.GC_2423,(3,43):C.GC_2423,(29,0):C.GC_2423,(19,20):C.GC_2422,(16,18):C.GC_2423,(10,17):C.GC_2422,(7,21):C.GC_2423,(0,44):C.GC_2422,(26,10):C.GC_2422,(20,1):C.GC_2423,(13,24):C.GC_2422,(11,2):C.GC_2423,(4,22):C.GC_2422,(1,23):C.GC_2422,(23,19):C.GC_2423,(17,4):C.GC_2422,(14,25):C.GC_2423,(8,3):C.GC_2422,(5,28):C.GC_2423,(2,26):C.GC_2423,(24,29):C.GC_2421,(21,30):C.GC_2420,(18,30):C.GC_2421,(15,29):C.GC_2420,(28,6):C.GC_2421,(22,34):C.GC_2421,(9,34):C.GC_2420,(3,6):C.GC_2420,(29,7):C.GC_2421,(16,35):C.GC_2421,(10,35):C.GC_2420,(0,7):C.GC_2420,(26,39):C.GC_2420,(20,38):C.GC_2420,(4,38):C.GC_2421,(1,39):C.GC_2421,(25,33):C.GC_2421,(6,33):C.GC_2420,(19,36):C.GC_2421,(7,36):C.GC_2420,(23,41):C.GC_2420,(17,40):C.GC_2420,(5,40):C.GC_2421,(2,41):C.GC_2421,(27,5):C.GC_2421,(12,5):C.GC_2420,(13,31):C.GC_2421,(11,31):C.GC_2420,(14,32):C.GC_2420,(8,32):C.GC_2421})

V_59 = Vertex(name = 'V_59',
              particles = [ P.g, P.g, P.g, P.g, P.g, P.g ],
              color = [ 'f(-3,1,2)*f(-2,3,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,2)*f(-2,3,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,2)*f(-2,3,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,2)*f(-2,4,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,2)*f(-2,4,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,2)*f(-2,5,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,3)*f(-2,2,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,3)*f(-2,2,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,3)*f(-2,2,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,3)*f(-2,4,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,3)*f(-2,4,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,3)*f(-2,5,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,4)*f(-2,2,3)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,1,4)*f(-2,2,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,4)*f(-2,2,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,4)*f(-2,3,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,4)*f(-2,3,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,4)*f(-2,5,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,1,5)*f(-2,2,3)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,1,5)*f(-2,2,4)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,1,5)*f(-2,2,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,5)*f(-2,3,4)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,1,5)*f(-2,3,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,5)*f(-2,4,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,1,6)*f(-2,2,3)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,1,6)*f(-2,2,4)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,1,6)*f(-2,2,5)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,1,6)*f(-2,3,4)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,1,6)*f(-2,3,5)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,1,6)*f(-2,4,5)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,2,3)*f(-2,1,4)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,2,3)*f(-2,1,5)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,2,3)*f(-2,1,6)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,2,3)*f(-2,4,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,3)*f(-2,4,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,3)*f(-2,5,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,4)*f(-2,1,3)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,2,4)*f(-2,1,5)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,2,4)*f(-2,1,6)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,2,4)*f(-2,3,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,4)*f(-2,3,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,4)*f(-2,5,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,2,5)*f(-2,1,3)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,2,5)*f(-2,1,4)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,2,5)*f(-2,1,6)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,2,5)*f(-2,3,4)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,2,5)*f(-2,3,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,5)*f(-2,4,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,2,6)*f(-2,1,3)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,2,6)*f(-2,1,4)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,2,6)*f(-2,1,5)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,2,6)*f(-2,3,4)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,2,6)*f(-2,3,5)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,2,6)*f(-2,4,5)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,3,4)*f(-2,1,2)*f(-1,-2,-3)*f(5,6,-1)', 'f(-3,3,4)*f(-2,1,5)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,3,4)*f(-2,1,6)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,3,4)*f(-2,2,5)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,3,4)*f(-2,2,6)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,3,4)*f(-2,5,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,3,5)*f(-2,1,2)*f(-1,-2,-3)*f(4,6,-1)', 'f(-3,3,5)*f(-2,1,4)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,3,5)*f(-2,1,6)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,3,5)*f(-2,2,4)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,3,5)*f(-2,2,6)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,3,5)*f(-2,4,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,3,6)*f(-2,1,2)*f(-1,-2,-3)*f(4,5,-1)', 'f(-3,3,6)*f(-2,1,4)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,3,6)*f(-2,1,5)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,3,6)*f(-2,2,4)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,3,6)*f(-2,2,5)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,3,6)*f(-2,4,5)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,4,5)*f(-2,1,2)*f(-1,-2,-3)*f(3,6,-1)', 'f(-3,4,5)*f(-2,1,3)*f(-1,-2,-3)*f(2,6,-1)', 'f(-3,4,5)*f(-2,1,6)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,4,5)*f(-2,2,3)*f(-1,-2,-3)*f(1,6,-1)', 'f(-3,4,5)*f(-2,2,6)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,4,5)*f(-2,3,6)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,4,6)*f(-2,1,2)*f(-1,-2,-3)*f(3,5,-1)', 'f(-3,4,6)*f(-2,1,3)*f(-1,-2,-3)*f(2,5,-1)', 'f(-3,4,6)*f(-2,1,5)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,4,6)*f(-2,2,3)*f(-1,-2,-3)*f(1,5,-1)', 'f(-3,4,6)*f(-2,2,5)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,4,6)*f(-2,3,5)*f(-1,-2,-3)*f(1,2,-1)', 'f(-3,5,6)*f(-2,1,2)*f(-1,-2,-3)*f(3,4,-1)', 'f(-3,5,6)*f(-2,1,3)*f(-1,-2,-3)*f(2,4,-1)', 'f(-3,5,6)*f(-2,1,4)*f(-1,-2,-3)*f(2,3,-1)', 'f(-3,5,6)*f(-2,2,3)*f(-1,-2,-3)*f(1,4,-1)', 'f(-3,5,6)*f(-2,2,4)*f(-1,-2,-3)*f(1,3,-1)', 'f(-3,5,6)*f(-2,3,4)*f(-1,-2,-3)*f(1,2,-1)' ],
              lorentz = [ L.VVVVVV1, L.VVVVVV10, L.VVVVVV11, L.VVVVVV12, L.VVVVVV13, L.VVVVVV14, L.VVVVVV15, L.VVVVVV16, L.VVVVVV17, L.VVVVVV18, L.VVVVVV19, L.VVVVVV2, L.VVVVVV20, L.VVVVVV21, L.VVVVVV22, L.VVVVVV23, L.VVVVVV24, L.VVVVVV25, L.VVVVVV26, L.VVVVVV27, L.VVVVVV28, L.VVVVVV29, L.VVVVVV3, L.VVVVVV30, L.VVVVVV31, L.VVVVVV32, L.VVVVVV33, L.VVVVVV34, L.VVVVVV35, L.VVVVVV36, L.VVVVVV37, L.VVVVVV38, L.VVVVVV39, L.VVVVVV4, L.VVVVVV40, L.VVVVVV41, L.VVVVVV42, L.VVVVVV43, L.VVVVVV44, L.VVVVVV45, L.VVVVVV46, L.VVVVVV47, L.VVVVVV48, L.VVVVVV49, L.VVVVVV5, L.VVVVVV50, L.VVVVVV51, L.VVVVVV52, L.VVVVVV54, L.VVVVVV55, L.VVVVVV56, L.VVVVVV57, L.VVVVVV58, L.VVVVVV59, L.VVVVVV6, L.VVVVVV60, L.VVVVVV61, L.VVVVVV7, L.VVVVVV8, L.VVVVVV9 ],
              couplings = {(41,58):C.GC_2428,(47,59):C.GC_2427,(53,7):C.GC_2428,(35,57):C.GC_2427,(46,14):C.GC_2428,(52,17):C.GC_2427,(34,2):C.GC_2428,(40,10):C.GC_2427,(51,37):C.GC_2428,(33,4):C.GC_2427,(39,21):C.GC_2428,(45,30):C.GC_2427,(17,57):C.GC_2428,(23,2):C.GC_2427,(29,4):C.GC_2428,(11,58):C.GC_2427,(22,10):C.GC_2428,(28,21):C.GC_2427,(10,59):C.GC_2428,(16,14):C.GC_2427,(27,30):C.GC_2428,(9,7):C.GC_2427,(15,17):C.GC_2428,(21,37):C.GC_2427,(59,0):C.GC_2428,(65,11):C.GC_2427,(71,44):C.GC_2428,(64,12):C.GC_2428,(70,23):C.GC_2427,(58,16):C.GC_2427,(69,31):C.GC_2428,(57,19):C.GC_2428,(63,39):C.GC_2427,(5,0):C.GC_2427,(20,16):C.GC_2428,(26,19):C.GC_2427,(4,11):C.GC_2428,(14,12):C.GC_2427,(25,39):C.GC_2428,(3,44):C.GC_2427,(13,23):C.GC_2428,(19,31):C.GC_2427,(77,22):C.GC_2427,(83,33):C.GC_2428,(76,1):C.GC_2428,(82,8):C.GC_2427,(81,40):C.GC_2428,(75,35):C.GC_2427,(2,22):C.GC_2428,(8,1):C.GC_2427,(24,35):C.GC_2428,(1,33):C.GC_2427,(7,8):C.GC_2428,(18,40):C.GC_2427,(89,54):C.GC_2428,(88,6):C.GC_2427,(87,25):C.GC_2428,(0,54):C.GC_2427,(6,6):C.GC_2428,(12,25):C.GC_2427,(62,15):C.GC_2428,(68,18):C.GC_2427,(56,13):C.GC_2427,(67,38):C.GC_2428,(55,24):C.GC_2428,(61,32):C.GC_2427,(44,13):C.GC_2428,(50,24):C.GC_2427,(38,15):C.GC_2427,(49,32):C.GC_2428,(37,18):C.GC_2428,(43,38):C.GC_2427,(74,3):C.GC_2428,(80,5):C.GC_2427,(79,34):C.GC_2428,(73,42):C.GC_2427,(32,3):C.GC_2427,(48,42):C.GC_2428,(31,5):C.GC_2428,(42,34):C.GC_2427,(86,9):C.GC_2427,(85,20):C.GC_2428,(30,9):C.GC_2428,(36,20):C.GC_2427,(78,41):C.GC_2428,(72,36):C.GC_2427,(66,36):C.GC_2428,(60,41):C.GC_2427,(65,43):C.GC_2425,(71,46):C.GC_2426,(77,46):C.GC_2425,(83,43):C.GC_2426,(41,28):C.GC_2425,(53,50):C.GC_2425,(76,50):C.GC_2426,(88,28):C.GC_2426,(35,29):C.GC_2425,(52,53):C.GC_2425,(64,53):C.GC_2426,(87,29):C.GC_2426,(34,52):C.GC_2426,(40,51):C.GC_2426,(69,51):C.GC_2425,(81,52):C.GC_2425,(17,29):C.GC_2426,(23,52):C.GC_2425,(80,52):C.GC_2426,(86,29):C.GC_2425,(11,28):C.GC_2426,(22,51):C.GC_2425,(68,51):C.GC_2426,(85,28):C.GC_2425,(9,50):C.GC_2426,(15,53):C.GC_2426,(61,53):C.GC_2425,(73,50):C.GC_2425,(4,43):C.GC_2426,(14,53):C.GC_2425,(49,53):C.GC_2426,(78,43):C.GC_2425,(3,46):C.GC_2425,(19,51):C.GC_2426,(37,51):C.GC_2425,(72,46):C.GC_2426,(2,46):C.GC_2426,(8,50):C.GC_2425,(48,50):C.GC_2426,(66,46):C.GC_2425,(1,43):C.GC_2425,(18,52):C.GC_2426,(31,52):C.GC_2425,(60,43):C.GC_2426,(6,28):C.GC_2425,(12,29):C.GC_2425,(30,29):C.GC_2426,(36,28):C.GC_2426,(47,48):C.GC_2425,(82,48):C.GC_2426,(46,55):C.GC_2425,(70,55):C.GC_2426,(33,56):C.GC_2426,(39,49):C.GC_2426,(63,49):C.GC_2425,(75,56):C.GC_2425,(29,56):C.GC_2425,(74,56):C.GC_2426,(28,49):C.GC_2425,(62,49):C.GC_2426,(10,48):C.GC_2426,(16,55):C.GC_2426,(67,55):C.GC_2425,(79,48):C.GC_2425,(25,49):C.GC_2426,(38,49):C.GC_2425,(13,55):C.GC_2425,(43,55):C.GC_2426,(24,56):C.GC_2426,(32,56):C.GC_2425,(7,48):C.GC_2425,(42,48):C.GC_2426,(84,26):C.GC_2428,(54,26):C.GC_2427,(59,27):C.GC_2425,(89,27):C.GC_2426,(51,45):C.GC_2425,(58,45):C.GC_2426,(21,45):C.GC_2426,(55,45):C.GC_2425,(5,27):C.GC_2426,(20,45):C.GC_2425,(50,45):C.GC_2426,(84,27):C.GC_2425,(0,27):C.GC_2425,(54,27):C.GC_2426,(45,47):C.GC_2426,(57,47):C.GC_2425,(27,47):C.GC_2425,(56,47):C.GC_2426,(26,47):C.GC_2426,(44,47):C.GC_2425})

V_60 = Vertex(name = 'V_60',
              particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF14, L.FFFF15, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,11):C.GC_5942,(0,9):C.GC_5941,(0,10):C.GC_5941,(0,8):C.GC_146,(0,3):C.GC_5860,(0,1):C.GC_1719,(0,4):C.GC_1125,(0,7):C.GC_1547,(0,5):C.GC_1546,(0,6):C.GC_1546,(0,2):C.GC_1962,(0,0):C.GC_1465})

V_61 = Vertex(name = 'V_61',
              particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_148,(0,11):C.GC_5948,(0,9):C.GC_5947,(0,10):C.GC_5947,(0,3):C.GC_5863,(0,1):C.GC_1971,(0,2):C.GC_1720,(0,4):C.GC_1126,(0,7):C.GC_1549,(0,5):C.GC_1548,(0,6):C.GC_1548,(0,0):C.GC_1466})

V_62 = Vertex(name = 'V_62',
              particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF22, L.FFFF23, L.FFFF25, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_150,(0,11):C.GC_5954,(0,9):C.GC_5953,(0,10):C.GC_5953,(0,3):C.GC_5866,(0,5):C.GC_1550,(0,1):C.GC_1980,(0,2):C.GC_1721,(0,4):C.GC_1127,(0,6):C.GC_1551,(0,7):C.GC_1550,(0,0):C.GC_1467})

V_63 = Vertex(name = 'V_63',
              particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_152,(0,11):C.GC_5944,(0,9):C.GC_5943,(0,10):C.GC_5943,(0,3):C.GC_5861,(0,1):C.GC_1989,(0,2):C.GC_1722,(0,4):C.GC_1128,(0,7):C.GC_1553,(0,5):C.GC_1552,(0,6):C.GC_1552,(0,0):C.GC_1468})

V_64 = Vertex(name = 'V_64',
              particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_154,(0,11):C.GC_5950,(0,9):C.GC_5949,(0,10):C.GC_5949,(0,3):C.GC_5864,(0,1):C.GC_1998,(0,2):C.GC_1723,(0,4):C.GC_1129,(0,7):C.GC_1555,(0,5):C.GC_1554,(0,6):C.GC_1554,(0,0):C.GC_1469})

V_65 = Vertex(name = 'V_65',
              particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_156,(0,11):C.GC_5956,(0,9):C.GC_5955,(0,10):C.GC_5955,(0,3):C.GC_5867,(0,1):C.GC_2007,(0,2):C.GC_1724,(0,4):C.GC_1130,(0,7):C.GC_1557,(0,5):C.GC_1556,(0,6):C.GC_1556,(0,0):C.GC_1470})

V_66 = Vertex(name = 'V_66',
              particles = [ P.e__plus__, P.e__minus__, P.u__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_158,(0,11):C.GC_5946,(0,9):C.GC_5945,(0,10):C.GC_5945,(0,3):C.GC_5862,(0,1):C.GC_2016,(0,2):C.GC_1725,(0,4):C.GC_1131,(0,7):C.GC_1559,(0,5):C.GC_1558,(0,6):C.GC_1558,(0,0):C.GC_1471})

V_67 = Vertex(name = 'V_67',
              particles = [ P.e__plus__, P.e__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_160,(0,11):C.GC_5952,(0,9):C.GC_5951,(0,10):C.GC_5951,(0,3):C.GC_5865,(0,1):C.GC_2025,(0,2):C.GC_1726,(0,4):C.GC_1132,(0,7):C.GC_1561,(0,5):C.GC_1560,(0,6):C.GC_1560,(0,0):C.GC_1472})

V_68 = Vertex(name = 'V_68',
              particles = [ P.e__plus__, P.e__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_162,(0,11):C.GC_5958,(0,9):C.GC_5957,(0,10):C.GC_5957,(0,3):C.GC_5868,(0,1):C.GC_2034,(0,2):C.GC_1727,(0,4):C.GC_1133,(0,7):C.GC_1563,(0,5):C.GC_1562,(0,6):C.GC_1562,(0,0):C.GC_1473})

V_69 = Vertex(name = 'V_69',
              particles = [ P.mu__plus__, P.e__minus__, P.u__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_164,(0,11):C.GC_5996,(0,9):C.GC_5995,(0,10):C.GC_5995,(0,3):C.GC_5887,(0,1):C.GC_1963,(0,2):C.GC_1728,(0,4):C.GC_1134,(0,7):C.GC_1565,(0,5):C.GC_1564,(0,6):C.GC_1564,(0,0):C.GC_1474})

V_70 = Vertex(name = 'V_70',
              particles = [ P.mu__plus__, P.e__minus__, P.c__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_166,(0,11):C.GC_6002,(0,9):C.GC_6001,(0,10):C.GC_6001,(0,3):C.GC_5890,(0,1):C.GC_1972,(0,2):C.GC_1729,(0,4):C.GC_1135,(0,7):C.GC_1567,(0,5):C.GC_1566,(0,6):C.GC_1566,(0,0):C.GC_1475})

V_71 = Vertex(name = 'V_71',
              particles = [ P.mu__plus__, P.e__minus__, P.t__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_168,(0,11):C.GC_6008,(0,9):C.GC_6007,(0,10):C.GC_6007,(0,3):C.GC_5893,(0,1):C.GC_1981,(0,2):C.GC_1730,(0,4):C.GC_1136,(0,7):C.GC_1569,(0,5):C.GC_1568,(0,6):C.GC_1568,(0,0):C.GC_1476})

V_72 = Vertex(name = 'V_72',
              particles = [ P.mu__plus__, P.e__minus__, P.u__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_170,(0,11):C.GC_5998,(0,9):C.GC_5997,(0,10):C.GC_5997,(0,3):C.GC_5888,(0,1):C.GC_1990,(0,2):C.GC_1731,(0,4):C.GC_1137,(0,7):C.GC_1571,(0,5):C.GC_1570,(0,6):C.GC_1570,(0,0):C.GC_1477})

V_73 = Vertex(name = 'V_73',
              particles = [ P.mu__plus__, P.e__minus__, P.c__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_172,(0,11):C.GC_6004,(0,9):C.GC_6003,(0,10):C.GC_6003,(0,3):C.GC_5891,(0,1):C.GC_1999,(0,2):C.GC_1732,(0,4):C.GC_1138,(0,7):C.GC_1573,(0,5):C.GC_1572,(0,6):C.GC_1572,(0,0):C.GC_1478})

V_74 = Vertex(name = 'V_74',
              particles = [ P.mu__plus__, P.e__minus__, P.t__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_174,(0,11):C.GC_6010,(0,9):C.GC_6009,(0,10):C.GC_6009,(0,3):C.GC_5894,(0,1):C.GC_2008,(0,2):C.GC_1733,(0,4):C.GC_1139,(0,7):C.GC_1575,(0,5):C.GC_1574,(0,6):C.GC_1574,(0,0):C.GC_1479})

V_75 = Vertex(name = 'V_75',
              particles = [ P.mu__plus__, P.e__minus__, P.u__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_176,(0,11):C.GC_6000,(0,9):C.GC_5999,(0,10):C.GC_5999,(0,3):C.GC_5889,(0,1):C.GC_2017,(0,2):C.GC_1734,(0,4):C.GC_1140,(0,7):C.GC_1577,(0,5):C.GC_1576,(0,6):C.GC_1576,(0,0):C.GC_1480})

V_76 = Vertex(name = 'V_76',
              particles = [ P.mu__plus__, P.e__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_178,(0,11):C.GC_6006,(0,9):C.GC_6005,(0,10):C.GC_6005,(0,3):C.GC_5892,(0,1):C.GC_2026,(0,2):C.GC_1735,(0,4):C.GC_1141,(0,7):C.GC_1579,(0,5):C.GC_1578,(0,6):C.GC_1578,(0,0):C.GC_1481})

V_77 = Vertex(name = 'V_77',
              particles = [ P.mu__plus__, P.e__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_180,(0,11):C.GC_6012,(0,9):C.GC_6011,(0,10):C.GC_6011,(0,3):C.GC_5895,(0,1):C.GC_2035,(0,2):C.GC_1736,(0,4):C.GC_1142,(0,7):C.GC_1581,(0,5):C.GC_1580,(0,6):C.GC_1580,(0,0):C.GC_1482})

V_78 = Vertex(name = 'V_78',
              particles = [ P.ta__plus__, P.e__minus__, P.u__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_182,(0,11):C.GC_6050,(0,9):C.GC_6049,(0,10):C.GC_6049,(0,3):C.GC_5914,(0,1):C.GC_1964,(0,2):C.GC_1737,(0,4):C.GC_1143,(0,7):C.GC_1583,(0,5):C.GC_1582,(0,6):C.GC_1582,(0,0):C.GC_1483})

V_79 = Vertex(name = 'V_79',
              particles = [ P.ta__plus__, P.e__minus__, P.c__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_184,(0,11):C.GC_6056,(0,9):C.GC_6055,(0,10):C.GC_6055,(0,3):C.GC_5917,(0,1):C.GC_1973,(0,2):C.GC_1738,(0,4):C.GC_1144,(0,7):C.GC_1585,(0,5):C.GC_1584,(0,6):C.GC_1584,(0,0):C.GC_1484})

V_80 = Vertex(name = 'V_80',
              particles = [ P.ta__plus__, P.e__minus__, P.t__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_186,(0,11):C.GC_6062,(0,9):C.GC_6061,(0,10):C.GC_6061,(0,3):C.GC_5920,(0,1):C.GC_1982,(0,2):C.GC_1739,(0,4):C.GC_1145,(0,7):C.GC_1587,(0,5):C.GC_1586,(0,6):C.GC_1586,(0,0):C.GC_1485})

V_81 = Vertex(name = 'V_81',
              particles = [ P.ta__plus__, P.e__minus__, P.u__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_188,(0,11):C.GC_6052,(0,9):C.GC_6051,(0,10):C.GC_6051,(0,3):C.GC_5915,(0,1):C.GC_1991,(0,2):C.GC_1740,(0,4):C.GC_1146,(0,7):C.GC_1589,(0,5):C.GC_1588,(0,6):C.GC_1588,(0,0):C.GC_1486})

V_82 = Vertex(name = 'V_82',
              particles = [ P.ta__plus__, P.e__minus__, P.c__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_190,(0,11):C.GC_6058,(0,9):C.GC_6057,(0,10):C.GC_6057,(0,3):C.GC_5918,(0,1):C.GC_2000,(0,2):C.GC_1741,(0,4):C.GC_1147,(0,7):C.GC_1591,(0,5):C.GC_1590,(0,6):C.GC_1590,(0,0):C.GC_1487})

V_83 = Vertex(name = 'V_83',
              particles = [ P.ta__plus__, P.e__minus__, P.t__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_192,(0,11):C.GC_6064,(0,9):C.GC_6063,(0,10):C.GC_6063,(0,3):C.GC_5921,(0,1):C.GC_2009,(0,2):C.GC_1742,(0,4):C.GC_1148,(0,7):C.GC_1593,(0,5):C.GC_1592,(0,6):C.GC_1592,(0,0):C.GC_1488})

V_84 = Vertex(name = 'V_84',
              particles = [ P.ta__plus__, P.e__minus__, P.u__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_194,(0,11):C.GC_6054,(0,9):C.GC_6053,(0,10):C.GC_6053,(0,3):C.GC_5916,(0,1):C.GC_2018,(0,2):C.GC_1743,(0,4):C.GC_1149,(0,7):C.GC_1595,(0,5):C.GC_1594,(0,6):C.GC_1594,(0,0):C.GC_1489})

V_85 = Vertex(name = 'V_85',
              particles = [ P.ta__plus__, P.e__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_196,(0,11):C.GC_6060,(0,9):C.GC_6059,(0,10):C.GC_6059,(0,3):C.GC_5919,(0,1):C.GC_2027,(0,2):C.GC_1744,(0,4):C.GC_1150,(0,7):C.GC_1597,(0,5):C.GC_1596,(0,6):C.GC_1596,(0,0):C.GC_1490})

V_86 = Vertex(name = 'V_86',
              particles = [ P.ta__plus__, P.e__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_198,(0,11):C.GC_6066,(0,9):C.GC_6065,(0,10):C.GC_6065,(0,3):C.GC_5922,(0,1):C.GC_2036,(0,2):C.GC_1745,(0,4):C.GC_1151,(0,7):C.GC_1599,(0,5):C.GC_1598,(0,6):C.GC_1598,(0,0):C.GC_1491})

V_87 = Vertex(name = 'V_87',
              particles = [ P.e__plus__, P.mu__minus__, P.u__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_200,(0,11):C.GC_5960,(0,9):C.GC_5959,(0,10):C.GC_5959,(0,3):C.GC_5869,(0,1):C.GC_1965,(0,2):C.GC_1746,(0,4):C.GC_1152,(0,7):C.GC_1601,(0,5):C.GC_1600,(0,6):C.GC_1600,(0,0):C.GC_1492})

V_88 = Vertex(name = 'V_88',
              particles = [ P.e__plus__, P.mu__minus__, P.c__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_202,(0,11):C.GC_5966,(0,9):C.GC_5965,(0,10):C.GC_5965,(0,3):C.GC_5872,(0,1):C.GC_1974,(0,2):C.GC_1747,(0,4):C.GC_1153,(0,7):C.GC_1603,(0,5):C.GC_1602,(0,6):C.GC_1602,(0,0):C.GC_1493})

V_89 = Vertex(name = 'V_89',
              particles = [ P.e__plus__, P.mu__minus__, P.t__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF9 ],
              couplings = {(0,9):C.GC_5971,(0,10):C.GC_5971,(0,8):C.GC_204,(0,11):C.GC_5972,(0,3):C.GC_5875,(0,7):C.GC_1605,(0,5):C.GC_1604,(0,6):C.GC_1604,(0,1):C.GC_1983,(0,2):C.GC_1748,(0,4):C.GC_1154,(0,0):C.GC_1494})

V_90 = Vertex(name = 'V_90',
              particles = [ P.e__plus__, P.mu__minus__, P.u__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_206,(0,11):C.GC_5962,(0,9):C.GC_5961,(0,10):C.GC_5961,(0,3):C.GC_5870,(0,1):C.GC_1992,(0,2):C.GC_1749,(0,4):C.GC_1155,(0,7):C.GC_1607,(0,5):C.GC_1606,(0,6):C.GC_1606,(0,0):C.GC_1495})

V_91 = Vertex(name = 'V_91',
              particles = [ P.e__plus__, P.mu__minus__, P.c__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_208,(0,11):C.GC_5968,(0,9):C.GC_5967,(0,10):C.GC_5967,(0,3):C.GC_5873,(0,1):C.GC_2001,(0,2):C.GC_1750,(0,4):C.GC_1156,(0,7):C.GC_1609,(0,5):C.GC_1608,(0,6):C.GC_1608,(0,0):C.GC_1496})

V_92 = Vertex(name = 'V_92',
              particles = [ P.e__plus__, P.mu__minus__, P.t__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_210,(0,11):C.GC_5974,(0,9):C.GC_5973,(0,10):C.GC_5973,(0,3):C.GC_5876,(0,1):C.GC_2010,(0,2):C.GC_1751,(0,4):C.GC_1157,(0,7):C.GC_1611,(0,5):C.GC_1610,(0,6):C.GC_1610,(0,0):C.GC_1497})

V_93 = Vertex(name = 'V_93',
              particles = [ P.e__plus__, P.mu__minus__, P.u__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_212,(0,11):C.GC_5964,(0,9):C.GC_5963,(0,10):C.GC_5963,(0,3):C.GC_5871,(0,1):C.GC_2019,(0,2):C.GC_1752,(0,4):C.GC_1158,(0,7):C.GC_1613,(0,5):C.GC_1612,(0,6):C.GC_1612,(0,0):C.GC_1498})

V_94 = Vertex(name = 'V_94',
              particles = [ P.e__plus__, P.mu__minus__, P.c__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_214,(0,11):C.GC_5970,(0,9):C.GC_5969,(0,10):C.GC_5969,(0,3):C.GC_5874,(0,1):C.GC_2028,(0,2):C.GC_1753,(0,4):C.GC_1159,(0,7):C.GC_1615,(0,5):C.GC_1614,(0,6):C.GC_1614,(0,0):C.GC_1499})

V_95 = Vertex(name = 'V_95',
              particles = [ P.e__plus__, P.mu__minus__, P.t__tilde__, P.t ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_216,(0,11):C.GC_5976,(0,9):C.GC_5975,(0,10):C.GC_5975,(0,3):C.GC_5877,(0,1):C.GC_2037,(0,2):C.GC_1754,(0,4):C.GC_1160,(0,7):C.GC_1617,(0,5):C.GC_1616,(0,6):C.GC_1616,(0,0):C.GC_1500})

V_96 = Vertex(name = 'V_96',
              particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_218,(0,11):C.GC_6014,(0,9):C.GC_6013,(0,10):C.GC_6013,(0,3):C.GC_5896,(0,1):C.GC_1966,(0,2):C.GC_1755,(0,4):C.GC_1161,(0,7):C.GC_1619,(0,5):C.GC_1618,(0,6):C.GC_1618,(0,0):C.GC_1501})

V_97 = Vertex(name = 'V_97',
              particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_220,(0,11):C.GC_6020,(0,9):C.GC_6019,(0,10):C.GC_6019,(0,3):C.GC_5899,(0,1):C.GC_1975,(0,2):C.GC_1756,(0,4):C.GC_1162,(0,7):C.GC_1621,(0,5):C.GC_1620,(0,6):C.GC_1620,(0,0):C.GC_1502})

V_98 = Vertex(name = 'V_98',
              particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.u ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_222,(0,11):C.GC_6026,(0,9):C.GC_6025,(0,10):C.GC_6025,(0,3):C.GC_5902,(0,1):C.GC_1984,(0,2):C.GC_1757,(0,4):C.GC_1163,(0,7):C.GC_1623,(0,5):C.GC_1622,(0,6):C.GC_1622,(0,0):C.GC_1503})

V_99 = Vertex(name = 'V_99',
              particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.c ],
              color = [ 'Identity(3,4)' ],
              lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
              couplings = {(0,8):C.GC_224,(0,11):C.GC_6016,(0,9):C.GC_6015,(0,10):C.GC_6015,(0,3):C.GC_5897,(0,1):C.GC_1993,(0,2):C.GC_1758,(0,4):C.GC_1164,(0,7):C.GC_1625,(0,5):C.GC_1624,(0,6):C.GC_1624,(0,0):C.GC_1504})

V_100 = Vertex(name = 'V_100',
               particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_226,(0,11):C.GC_6022,(0,9):C.GC_6021,(0,10):C.GC_6021,(0,3):C.GC_5900,(0,1):C.GC_2002,(0,2):C.GC_1759,(0,4):C.GC_1165,(0,7):C.GC_1627,(0,5):C.GC_1626,(0,6):C.GC_1626,(0,0):C.GC_1505})

V_101 = Vertex(name = 'V_101',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_228,(0,11):C.GC_6028,(0,9):C.GC_6027,(0,10):C.GC_6027,(0,3):C.GC_5903,(0,1):C.GC_2011,(0,2):C.GC_1760,(0,4):C.GC_1166,(0,7):C.GC_1629,(0,5):C.GC_1628,(0,6):C.GC_1628,(0,0):C.GC_1506})

V_102 = Vertex(name = 'V_102',
               particles = [ P.mu__plus__, P.mu__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_230,(0,11):C.GC_6018,(0,9):C.GC_6017,(0,10):C.GC_6017,(0,3):C.GC_5898,(0,1):C.GC_2020,(0,2):C.GC_1761,(0,4):C.GC_1167,(0,7):C.GC_1631,(0,5):C.GC_1630,(0,6):C.GC_1630,(0,0):C.GC_1507})

V_103 = Vertex(name = 'V_103',
               particles = [ P.mu__plus__, P.mu__minus__, P.c__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_232,(0,11):C.GC_6024,(0,9):C.GC_6023,(0,10):C.GC_6023,(0,3):C.GC_5901,(0,1):C.GC_2029,(0,2):C.GC_1762,(0,4):C.GC_1168,(0,7):C.GC_1633,(0,5):C.GC_1632,(0,6):C.GC_1632,(0,0):C.GC_1508})

V_104 = Vertex(name = 'V_104',
               particles = [ P.mu__plus__, P.mu__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_234,(0,11):C.GC_6030,(0,9):C.GC_6029,(0,10):C.GC_6029,(0,3):C.GC_5904,(0,1):C.GC_2038,(0,2):C.GC_1763,(0,4):C.GC_1169,(0,7):C.GC_1635,(0,5):C.GC_1634,(0,6):C.GC_1634,(0,0):C.GC_1509})

V_105 = Vertex(name = 'V_105',
               particles = [ P.ta__plus__, P.mu__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_236,(0,11):C.GC_6068,(0,9):C.GC_6067,(0,10):C.GC_6067,(0,3):C.GC_5923,(0,1):C.GC_1967,(0,2):C.GC_1764,(0,4):C.GC_1170,(0,7):C.GC_1637,(0,5):C.GC_1636,(0,6):C.GC_1636,(0,0):C.GC_1510})

V_106 = Vertex(name = 'V_106',
               particles = [ P.ta__plus__, P.mu__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_238,(0,11):C.GC_6074,(0,9):C.GC_6073,(0,10):C.GC_6073,(0,3):C.GC_5926,(0,1):C.GC_1976,(0,2):C.GC_1765,(0,4):C.GC_1171,(0,7):C.GC_1639,(0,5):C.GC_1638,(0,6):C.GC_1638,(0,0):C.GC_1511})

V_107 = Vertex(name = 'V_107',
               particles = [ P.ta__plus__, P.mu__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_240,(0,11):C.GC_6080,(0,9):C.GC_6079,(0,10):C.GC_6079,(0,3):C.GC_5929,(0,1):C.GC_1985,(0,2):C.GC_1766,(0,4):C.GC_1172,(0,7):C.GC_1641,(0,5):C.GC_1640,(0,6):C.GC_1640,(0,0):C.GC_1512})

V_108 = Vertex(name = 'V_108',
               particles = [ P.ta__plus__, P.mu__minus__, P.u__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_242,(0,11):C.GC_6070,(0,9):C.GC_6069,(0,10):C.GC_6069,(0,3):C.GC_5924,(0,1):C.GC_1994,(0,2):C.GC_1767,(0,4):C.GC_1173,(0,7):C.GC_1643,(0,5):C.GC_1642,(0,6):C.GC_1642,(0,0):C.GC_1513})

V_109 = Vertex(name = 'V_109',
               particles = [ P.ta__plus__, P.mu__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_244,(0,11):C.GC_6076,(0,9):C.GC_6075,(0,10):C.GC_6075,(0,3):C.GC_5927,(0,1):C.GC_2003,(0,2):C.GC_1768,(0,4):C.GC_1174,(0,7):C.GC_1645,(0,5):C.GC_1644,(0,6):C.GC_1644,(0,0):C.GC_1514})

V_110 = Vertex(name = 'V_110',
               particles = [ P.ta__plus__, P.mu__minus__, P.t__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_246,(0,11):C.GC_6082,(0,9):C.GC_6081,(0,10):C.GC_6081,(0,3):C.GC_5930,(0,1):C.GC_2012,(0,2):C.GC_1769,(0,4):C.GC_1175,(0,7):C.GC_1647,(0,5):C.GC_1646,(0,6):C.GC_1646,(0,0):C.GC_1515})

V_111 = Vertex(name = 'V_111',
               particles = [ P.ta__plus__, P.mu__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_248,(0,11):C.GC_6072,(0,9):C.GC_6071,(0,10):C.GC_6071,(0,3):C.GC_5925,(0,1):C.GC_2021,(0,2):C.GC_1770,(0,4):C.GC_1176,(0,7):C.GC_1649,(0,5):C.GC_1648,(0,6):C.GC_1648,(0,0):C.GC_1516})

V_112 = Vertex(name = 'V_112',
               particles = [ P.ta__plus__, P.mu__minus__, P.c__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_250,(0,11):C.GC_6078,(0,9):C.GC_6077,(0,10):C.GC_6077,(0,3):C.GC_5928,(0,1):C.GC_2030,(0,2):C.GC_1771,(0,4):C.GC_1177,(0,7):C.GC_1651,(0,5):C.GC_1650,(0,6):C.GC_1650,(0,0):C.GC_1517})

V_113 = Vertex(name = 'V_113',
               particles = [ P.ta__plus__, P.mu__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_252,(0,11):C.GC_6084,(0,9):C.GC_6083,(0,10):C.GC_6083,(0,3):C.GC_5931,(0,1):C.GC_2039,(0,2):C.GC_1772,(0,4):C.GC_1178,(0,7):C.GC_1653,(0,5):C.GC_1652,(0,6):C.GC_1652,(0,0):C.GC_1518})

V_114 = Vertex(name = 'V_114',
               particles = [ P.e__plus__, P.ta__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_254,(0,11):C.GC_5978,(0,9):C.GC_5977,(0,10):C.GC_5977,(0,3):C.GC_5878,(0,1):C.GC_1968,(0,2):C.GC_1773,(0,4):C.GC_1179,(0,7):C.GC_1655,(0,5):C.GC_1654,(0,6):C.GC_1654,(0,0):C.GC_1519})

V_115 = Vertex(name = 'V_115',
               particles = [ P.e__plus__, P.ta__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_256,(0,11):C.GC_5984,(0,9):C.GC_5983,(0,10):C.GC_5983,(0,3):C.GC_5881,(0,1):C.GC_1977,(0,2):C.GC_1774,(0,4):C.GC_1180,(0,7):C.GC_1657,(0,5):C.GC_1656,(0,6):C.GC_1656,(0,0):C.GC_1520})

V_116 = Vertex(name = 'V_116',
               particles = [ P.e__plus__, P.ta__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_258,(0,11):C.GC_5990,(0,9):C.GC_5989,(0,10):C.GC_5989,(0,3):C.GC_5884,(0,1):C.GC_1986,(0,2):C.GC_1775,(0,4):C.GC_1181,(0,7):C.GC_1659,(0,5):C.GC_1658,(0,6):C.GC_1658,(0,0):C.GC_1521})

V_117 = Vertex(name = 'V_117',
               particles = [ P.e__plus__, P.ta__minus__, P.u__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_260,(0,11):C.GC_5980,(0,9):C.GC_5979,(0,10):C.GC_5979,(0,3):C.GC_5879,(0,1):C.GC_1995,(0,2):C.GC_1776,(0,4):C.GC_1182,(0,7):C.GC_1661,(0,5):C.GC_1660,(0,6):C.GC_1660,(0,0):C.GC_1522})

V_118 = Vertex(name = 'V_118',
               particles = [ P.e__plus__, P.ta__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_262,(0,11):C.GC_5986,(0,9):C.GC_5985,(0,10):C.GC_5985,(0,3):C.GC_5882,(0,1):C.GC_2004,(0,2):C.GC_1777,(0,4):C.GC_1183,(0,7):C.GC_1663,(0,5):C.GC_1662,(0,6):C.GC_1662,(0,0):C.GC_1523})

V_119 = Vertex(name = 'V_119',
               particles = [ P.e__plus__, P.ta__minus__, P.t__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_264,(0,11):C.GC_5992,(0,9):C.GC_5991,(0,10):C.GC_5991,(0,3):C.GC_5885,(0,1):C.GC_2013,(0,2):C.GC_1778,(0,4):C.GC_1184,(0,7):C.GC_1665,(0,5):C.GC_1664,(0,6):C.GC_1664,(0,0):C.GC_1524})

V_120 = Vertex(name = 'V_120',
               particles = [ P.e__plus__, P.ta__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_266,(0,11):C.GC_5982,(0,9):C.GC_5981,(0,10):C.GC_5981,(0,3):C.GC_5880,(0,1):C.GC_2022,(0,2):C.GC_1779,(0,4):C.GC_1185,(0,7):C.GC_1667,(0,5):C.GC_1666,(0,6):C.GC_1666,(0,0):C.GC_1525})

V_121 = Vertex(name = 'V_121',
               particles = [ P.e__plus__, P.ta__minus__, P.c__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_268,(0,11):C.GC_5988,(0,9):C.GC_5987,(0,10):C.GC_5987,(0,3):C.GC_5883,(0,1):C.GC_2031,(0,2):C.GC_1780,(0,4):C.GC_1186,(0,7):C.GC_1669,(0,5):C.GC_1668,(0,6):C.GC_1668,(0,0):C.GC_1526})

V_122 = Vertex(name = 'V_122',
               particles = [ P.e__plus__, P.ta__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_270,(0,11):C.GC_5994,(0,9):C.GC_5993,(0,10):C.GC_5993,(0,3):C.GC_5886,(0,1):C.GC_2040,(0,2):C.GC_1781,(0,4):C.GC_1187,(0,7):C.GC_1671,(0,5):C.GC_1670,(0,6):C.GC_1670,(0,0):C.GC_1527})

V_123 = Vertex(name = 'V_123',
               particles = [ P.mu__plus__, P.ta__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_272,(0,11):C.GC_6032,(0,9):C.GC_6031,(0,10):C.GC_6031,(0,3):C.GC_5905,(0,1):C.GC_1969,(0,2):C.GC_1782,(0,4):C.GC_1188,(0,7):C.GC_1673,(0,5):C.GC_1672,(0,6):C.GC_1672,(0,0):C.GC_1528})

V_124 = Vertex(name = 'V_124',
               particles = [ P.mu__plus__, P.ta__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_274,(0,11):C.GC_6038,(0,9):C.GC_6037,(0,10):C.GC_6037,(0,3):C.GC_5908,(0,1):C.GC_1978,(0,2):C.GC_1783,(0,4):C.GC_1189,(0,7):C.GC_1675,(0,5):C.GC_1674,(0,6):C.GC_1674,(0,0):C.GC_1529})

V_125 = Vertex(name = 'V_125',
               particles = [ P.mu__plus__, P.ta__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_276,(0,11):C.GC_6044,(0,9):C.GC_6043,(0,10):C.GC_6043,(0,3):C.GC_5911,(0,1):C.GC_1987,(0,2):C.GC_1784,(0,4):C.GC_1190,(0,7):C.GC_1677,(0,5):C.GC_1676,(0,6):C.GC_1676,(0,0):C.GC_1530})

V_126 = Vertex(name = 'V_126',
               particles = [ P.mu__plus__, P.ta__minus__, P.u__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_278,(0,11):C.GC_6034,(0,9):C.GC_6033,(0,10):C.GC_6033,(0,3):C.GC_5906,(0,1):C.GC_1996,(0,2):C.GC_1785,(0,4):C.GC_1191,(0,7):C.GC_1679,(0,5):C.GC_1678,(0,6):C.GC_1678,(0,0):C.GC_1531})

V_127 = Vertex(name = 'V_127',
               particles = [ P.mu__plus__, P.ta__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_280,(0,11):C.GC_6040,(0,9):C.GC_6039,(0,10):C.GC_6039,(0,3):C.GC_5909,(0,1):C.GC_2005,(0,2):C.GC_1786,(0,4):C.GC_1192,(0,7):C.GC_1681,(0,5):C.GC_1680,(0,6):C.GC_1680,(0,0):C.GC_1532})

V_128 = Vertex(name = 'V_128',
               particles = [ P.mu__plus__, P.ta__minus__, P.t__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_282,(0,11):C.GC_6046,(0,9):C.GC_6045,(0,10):C.GC_6045,(0,3):C.GC_5912,(0,1):C.GC_2014,(0,2):C.GC_1787,(0,4):C.GC_1193,(0,7):C.GC_1683,(0,5):C.GC_1682,(0,6):C.GC_1682,(0,0):C.GC_1533})

V_129 = Vertex(name = 'V_129',
               particles = [ P.mu__plus__, P.ta__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_284,(0,11):C.GC_6036,(0,9):C.GC_6035,(0,10):C.GC_6035,(0,3):C.GC_5907,(0,1):C.GC_2023,(0,2):C.GC_1788,(0,4):C.GC_1194,(0,7):C.GC_1685,(0,5):C.GC_1684,(0,6):C.GC_1684,(0,0):C.GC_1534})

V_130 = Vertex(name = 'V_130',
               particles = [ P.mu__plus__, P.ta__minus__, P.c__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_286,(0,11):C.GC_6042,(0,9):C.GC_6041,(0,10):C.GC_6041,(0,3):C.GC_5910,(0,1):C.GC_2032,(0,2):C.GC_1789,(0,4):C.GC_1195,(0,7):C.GC_1687,(0,5):C.GC_1686,(0,6):C.GC_1686,(0,0):C.GC_1535})

V_131 = Vertex(name = 'V_131',
               particles = [ P.mu__plus__, P.ta__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_288,(0,11):C.GC_6048,(0,9):C.GC_6047,(0,10):C.GC_6047,(0,3):C.GC_5913,(0,1):C.GC_2041,(0,2):C.GC_1790,(0,4):C.GC_1196,(0,7):C.GC_1689,(0,5):C.GC_1688,(0,6):C.GC_1688,(0,0):C.GC_1536})

V_132 = Vertex(name = 'V_132',
               particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_290,(0,11):C.GC_6086,(0,9):C.GC_6085,(0,10):C.GC_6085,(0,3):C.GC_5932,(0,1):C.GC_1970,(0,2):C.GC_1791,(0,4):C.GC_1197,(0,7):C.GC_1691,(0,5):C.GC_1690,(0,6):C.GC_1690,(0,0):C.GC_1537})

V_133 = Vertex(name = 'V_133',
               particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_292,(0,11):C.GC_6092,(0,9):C.GC_6091,(0,10):C.GC_6091,(0,3):C.GC_5935,(0,1):C.GC_1979,(0,2):C.GC_1792,(0,4):C.GC_1198,(0,7):C.GC_1693,(0,5):C.GC_1692,(0,6):C.GC_1692,(0,0):C.GC_1538})

V_134 = Vertex(name = 'V_134',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_294,(0,11):C.GC_6098,(0,9):C.GC_6097,(0,10):C.GC_6097,(0,3):C.GC_5938,(0,1):C.GC_1988,(0,2):C.GC_1793,(0,4):C.GC_1199,(0,7):C.GC_1695,(0,5):C.GC_1694,(0,6):C.GC_1694,(0,0):C.GC_1539})

V_135 = Vertex(name = 'V_135',
               particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_296,(0,11):C.GC_6088,(0,9):C.GC_6087,(0,10):C.GC_6087,(0,3):C.GC_5933,(0,1):C.GC_1997,(0,2):C.GC_1794,(0,4):C.GC_1200,(0,7):C.GC_1697,(0,5):C.GC_1696,(0,6):C.GC_1696,(0,0):C.GC_1540})

V_136 = Vertex(name = 'V_136',
               particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_298,(0,11):C.GC_6094,(0,9):C.GC_6093,(0,10):C.GC_6093,(0,3):C.GC_5936,(0,1):C.GC_2006,(0,2):C.GC_1795,(0,4):C.GC_1201,(0,7):C.GC_1699,(0,5):C.GC_1698,(0,6):C.GC_1698,(0,0):C.GC_1541})

V_137 = Vertex(name = 'V_137',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_300,(0,11):C.GC_6100,(0,9):C.GC_6099,(0,10):C.GC_6099,(0,3):C.GC_5939,(0,1):C.GC_2015,(0,2):C.GC_1796,(0,4):C.GC_1202,(0,7):C.GC_1701,(0,5):C.GC_1700,(0,6):C.GC_1700,(0,0):C.GC_1542})

V_138 = Vertex(name = 'V_138',
               particles = [ P.ta__plus__, P.ta__minus__, P.u__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_302,(0,11):C.GC_6090,(0,9):C.GC_6089,(0,10):C.GC_6089,(0,3):C.GC_5934,(0,1):C.GC_2024,(0,2):C.GC_1797,(0,4):C.GC_1203,(0,7):C.GC_1703,(0,5):C.GC_1702,(0,6):C.GC_1702,(0,0):C.GC_1543})

V_139 = Vertex(name = 'V_139',
               particles = [ P.ta__plus__, P.ta__minus__, P.c__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_304,(0,11):C.GC_6096,(0,9):C.GC_6095,(0,10):C.GC_6095,(0,3):C.GC_5937,(0,1):C.GC_2033,(0,2):C.GC_1798,(0,4):C.GC_1204,(0,7):C.GC_1705,(0,5):C.GC_1704,(0,6):C.GC_1704,(0,0):C.GC_1544})

V_140 = Vertex(name = 'V_140',
               particles = [ P.ta__plus__, P.ta__minus__, P.t__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF13, L.FFFF15, L.FFFF19, L.FFFF2, L.FFFF20, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,8):C.GC_305,(0,11):C.GC_6102,(0,9):C.GC_6101,(0,10):C.GC_6101,(0,3):C.GC_5940,(0,1):C.GC_2042,(0,2):C.GC_1799,(0,4):C.GC_1205,(0,7):C.GC_1707,(0,5):C.GC_1706,(0,6):C.GC_1706,(0,0):C.GC_1545})

V_141 = Vertex(name = 'V_141',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_388,(0,8):C.GC_918,(1,0):C.GC_3631,(3,0):C.GC_4198,(0,6):C.GC_2981,(2,6):C.GC_4036,(1,5):C.GC_1800,(3,5):C.GC_1881,(1,3):C.GC_2495,(3,3):C.GC_2576,(1,4):C.GC_2205,(3,4):C.GC_2286,(1,1):C.GC_3937,(3,1):C.GC_4279,(0,2):C.GC_3802,(2,2):C.GC_4117})

V_142 = Vertex(name = 'V_142',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_389,(0,8):C.GC_919,(1,0):C.GC_3632,(3,0):C.GC_4199,(0,6):C.GC_2982,(2,6):C.GC_4037,(1,5):C.GC_1809,(3,5):C.GC_1890,(1,3):C.GC_2496,(3,3):C.GC_2577,(1,4):C.GC_2214,(3,4):C.GC_2295,(1,1):C.GC_3938,(3,1):C.GC_4280,(0,2):C.GC_3803,(2,2):C.GC_4118})

V_143 = Vertex(name = 'V_143',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_390,(0,8):C.GC_920,(1,0):C.GC_3633,(3,0):C.GC_4200,(0,6):C.GC_2983,(2,6):C.GC_4038,(1,5):C.GC_1818,(3,5):C.GC_1899,(1,3):C.GC_2497,(3,3):C.GC_2578,(1,4):C.GC_2223,(3,4):C.GC_2304,(1,1):C.GC_3939,(3,1):C.GC_4281,(0,2):C.GC_3804,(2,2):C.GC_4119})

V_144 = Vertex(name = 'V_144',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_391,(0,8):C.GC_921,(1,0):C.GC_3634,(3,0):C.GC_4201,(0,6):C.GC_2984,(2,6):C.GC_4039,(1,5):C.GC_1827,(3,5):C.GC_1908,(1,3):C.GC_2498,(3,3):C.GC_2579,(1,4):C.GC_2232,(3,4):C.GC_2313,(1,1):C.GC_3940,(3,1):C.GC_4282,(0,2):C.GC_3805,(2,2):C.GC_4120})

V_145 = Vertex(name = 'V_145',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_392,(0,8):C.GC_922,(1,0):C.GC_3635,(3,0):C.GC_4202,(0,6):C.GC_2985,(2,6):C.GC_4040,(1,5):C.GC_1836,(3,5):C.GC_1917,(1,3):C.GC_2499,(3,3):C.GC_2580,(1,4):C.GC_2241,(3,4):C.GC_2322,(1,1):C.GC_3941,(3,1):C.GC_4283,(0,2):C.GC_3806,(2,2):C.GC_4121})

V_146 = Vertex(name = 'V_146',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_393,(0,8):C.GC_923,(1,0):C.GC_3636,(3,0):C.GC_4203,(0,6):C.GC_2986,(2,6):C.GC_4041,(1,5):C.GC_1845,(3,5):C.GC_1926,(1,3):C.GC_2500,(3,3):C.GC_2581,(1,4):C.GC_2250,(3,4):C.GC_2331,(1,1):C.GC_3942,(3,1):C.GC_4284,(0,2):C.GC_3807,(2,2):C.GC_4122})

V_147 = Vertex(name = 'V_147',
               particles = [ P.u__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_394,(0,8):C.GC_924,(1,0):C.GC_3637,(3,0):C.GC_4204,(0,6):C.GC_2987,(2,6):C.GC_4042,(1,5):C.GC_1854,(3,5):C.GC_1935,(1,3):C.GC_2501,(3,3):C.GC_2582,(1,4):C.GC_2259,(3,4):C.GC_2340,(1,1):C.GC_3943,(3,1):C.GC_4285,(0,2):C.GC_3808,(2,2):C.GC_4123})

V_148 = Vertex(name = 'V_148',
               particles = [ P.c__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_395,(0,8):C.GC_925,(1,0):C.GC_3638,(3,0):C.GC_4205,(0,6):C.GC_2988,(2,6):C.GC_4043,(1,5):C.GC_1863,(3,5):C.GC_1944,(1,3):C.GC_2502,(3,3):C.GC_2583,(1,4):C.GC_2268,(3,4):C.GC_2349,(1,1):C.GC_3944,(3,1):C.GC_4286,(0,2):C.GC_3809,(2,2):C.GC_4124})

V_149 = Vertex(name = 'V_149',
               particles = [ P.t__tilde__, P.d, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_396,(0,8):C.GC_926,(1,0):C.GC_3639,(3,0):C.GC_4206,(0,6):C.GC_2989,(2,6):C.GC_4044,(1,5):C.GC_1872,(3,5):C.GC_1953,(1,3):C.GC_2503,(3,3):C.GC_2584,(1,4):C.GC_2277,(3,4):C.GC_2358,(1,1):C.GC_3945,(3,1):C.GC_4287,(0,2):C.GC_3810,(2,2):C.GC_4125})

V_150 = Vertex(name = 'V_150',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_397,(0,8):C.GC_927,(1,0):C.GC_3640,(3,0):C.GC_4207,(0,6):C.GC_2990,(2,6):C.GC_4045,(1,5):C.GC_1801,(3,5):C.GC_1882,(1,3):C.GC_2504,(3,3):C.GC_2585,(1,4):C.GC_2206,(3,4):C.GC_2287,(1,1):C.GC_3946,(3,1):C.GC_4288,(0,2):C.GC_3811,(2,2):C.GC_4126})

V_151 = Vertex(name = 'V_151',
               particles = [ P.c__tilde__, P.d, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_398,(0,8):C.GC_928,(1,0):C.GC_3641,(3,0):C.GC_4208,(0,6):C.GC_2991,(2,6):C.GC_4046,(1,5):C.GC_1810,(3,5):C.GC_1891,(1,3):C.GC_2505,(3,3):C.GC_2586,(1,4):C.GC_2215,(3,4):C.GC_2296,(1,1):C.GC_3947,(3,1):C.GC_4289,(0,2):C.GC_3812,(2,2):C.GC_4127})

V_152 = Vertex(name = 'V_152',
               particles = [ P.t__tilde__, P.d, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_399,(0,8):C.GC_929,(1,0):C.GC_3642,(3,0):C.GC_4209,(0,6):C.GC_2992,(2,6):C.GC_4047,(1,5):C.GC_1819,(3,5):C.GC_1900,(1,3):C.GC_2506,(3,3):C.GC_2587,(1,4):C.GC_2224,(3,4):C.GC_2305,(1,1):C.GC_3948,(3,1):C.GC_4290,(0,2):C.GC_3813,(2,2):C.GC_4128})

V_153 = Vertex(name = 'V_153',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_400,(0,8):C.GC_930,(1,0):C.GC_3643,(3,0):C.GC_4210,(0,6):C.GC_2993,(2,6):C.GC_4048,(1,5):C.GC_1828,(3,5):C.GC_1909,(1,3):C.GC_2507,(3,3):C.GC_2588,(1,4):C.GC_2233,(3,4):C.GC_2314,(1,1):C.GC_3949,(3,1):C.GC_4291,(0,2):C.GC_3814,(2,2):C.GC_4129})

V_154 = Vertex(name = 'V_154',
               particles = [ P.c__tilde__, P.d, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_401,(0,8):C.GC_931,(1,0):C.GC_3644,(3,0):C.GC_4211,(0,6):C.GC_2994,(2,6):C.GC_4049,(1,5):C.GC_1837,(3,5):C.GC_1918,(1,3):C.GC_2508,(3,3):C.GC_2589,(1,4):C.GC_2242,(3,4):C.GC_2323,(1,1):C.GC_3950,(3,1):C.GC_4292,(0,2):C.GC_3815,(2,2):C.GC_4130})

V_155 = Vertex(name = 'V_155',
               particles = [ P.t__tilde__, P.d, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_402,(0,8):C.GC_932,(1,0):C.GC_3645,(3,0):C.GC_4212,(0,6):C.GC_2995,(2,6):C.GC_4050,(1,5):C.GC_1846,(3,5):C.GC_1927,(1,3):C.GC_2509,(3,3):C.GC_2590,(1,4):C.GC_2251,(3,4):C.GC_2332,(1,1):C.GC_3951,(3,1):C.GC_4293,(0,2):C.GC_3816,(2,2):C.GC_4131})

V_156 = Vertex(name = 'V_156',
               particles = [ P.u__tilde__, P.d, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_403,(0,8):C.GC_933,(1,0):C.GC_3646,(3,0):C.GC_4213,(0,6):C.GC_2996,(2,6):C.GC_4051,(1,5):C.GC_1855,(3,5):C.GC_1936,(1,3):C.GC_2510,(3,3):C.GC_2591,(1,4):C.GC_2260,(3,4):C.GC_2341,(1,1):C.GC_3952,(3,1):C.GC_4294,(0,2):C.GC_3817,(2,2):C.GC_4132})

V_157 = Vertex(name = 'V_157',
               particles = [ P.c__tilde__, P.d, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_404,(0,8):C.GC_934,(1,0):C.GC_3647,(3,0):C.GC_4214,(0,6):C.GC_2997,(2,6):C.GC_4052,(1,5):C.GC_1864,(3,5):C.GC_1945,(1,3):C.GC_2511,(3,3):C.GC_2592,(1,4):C.GC_2269,(3,4):C.GC_2350,(1,1):C.GC_3953,(3,1):C.GC_4295,(0,2):C.GC_3818,(2,2):C.GC_4133})

V_158 = Vertex(name = 'V_158',
               particles = [ P.t__tilde__, P.d, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_405,(0,8):C.GC_935,(1,0):C.GC_3648,(3,0):C.GC_4215,(0,6):C.GC_2998,(2,6):C.GC_4053,(1,5):C.GC_1873,(3,5):C.GC_1954,(1,3):C.GC_2512,(3,3):C.GC_2593,(1,4):C.GC_2278,(3,4):C.GC_2359,(1,1):C.GC_3954,(3,1):C.GC_4296,(0,2):C.GC_3819,(2,2):C.GC_4134})

V_159 = Vertex(name = 'V_159',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_406,(0,8):C.GC_936,(1,0):C.GC_3649,(3,0):C.GC_4216,(0,6):C.GC_2999,(2,6):C.GC_4054,(1,5):C.GC_1802,(3,5):C.GC_1883,(1,3):C.GC_2513,(3,3):C.GC_2594,(1,4):C.GC_2207,(3,4):C.GC_2288,(1,1):C.GC_3955,(3,1):C.GC_4297,(0,2):C.GC_3820,(2,2):C.GC_4135})

V_160 = Vertex(name = 'V_160',
               particles = [ P.c__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_407,(0,8):C.GC_937,(1,0):C.GC_3650,(3,0):C.GC_4217,(0,6):C.GC_3000,(2,6):C.GC_4055,(1,5):C.GC_1811,(3,5):C.GC_1892,(1,3):C.GC_2514,(3,3):C.GC_2595,(1,4):C.GC_2216,(3,4):C.GC_2297,(1,1):C.GC_3956,(3,1):C.GC_4298,(0,2):C.GC_3821,(2,2):C.GC_4136})

V_161 = Vertex(name = 'V_161',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_408,(0,8):C.GC_938,(1,0):C.GC_3651,(3,0):C.GC_4218,(0,6):C.GC_3001,(2,6):C.GC_4056,(1,5):C.GC_1820,(3,5):C.GC_1901,(1,3):C.GC_2515,(3,3):C.GC_2596,(1,4):C.GC_2225,(3,4):C.GC_2306,(1,1):C.GC_3957,(3,1):C.GC_4299,(0,2):C.GC_3822,(2,2):C.GC_4137})

V_162 = Vertex(name = 'V_162',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_409,(0,8):C.GC_939,(1,0):C.GC_3652,(3,0):C.GC_4219,(0,6):C.GC_3002,(2,6):C.GC_4057,(1,5):C.GC_1829,(3,5):C.GC_1910,(1,3):C.GC_2516,(3,3):C.GC_2597,(1,4):C.GC_2234,(3,4):C.GC_2315,(1,1):C.GC_3958,(3,1):C.GC_4300,(0,2):C.GC_3823,(2,2):C.GC_4138})

V_163 = Vertex(name = 'V_163',
               particles = [ P.c__tilde__, P.d, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_410,(0,8):C.GC_940,(1,0):C.GC_3653,(3,0):C.GC_4220,(0,6):C.GC_3003,(2,6):C.GC_4058,(1,5):C.GC_1838,(3,5):C.GC_1919,(1,3):C.GC_2517,(3,3):C.GC_2598,(1,4):C.GC_2243,(3,4):C.GC_2324,(1,1):C.GC_3959,(3,1):C.GC_4301,(0,2):C.GC_3824,(2,2):C.GC_4139})

V_164 = Vertex(name = 'V_164',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_411,(0,8):C.GC_941,(1,0):C.GC_3654,(3,0):C.GC_4221,(0,6):C.GC_3004,(2,6):C.GC_4059,(1,5):C.GC_1847,(3,5):C.GC_1928,(1,3):C.GC_2518,(3,3):C.GC_2599,(1,4):C.GC_2252,(3,4):C.GC_2333,(1,1):C.GC_3960,(3,1):C.GC_4302,(0,2):C.GC_3825,(2,2):C.GC_4140})

V_165 = Vertex(name = 'V_165',
               particles = [ P.u__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_412,(0,8):C.GC_942,(1,0):C.GC_3655,(3,0):C.GC_4222,(0,6):C.GC_3005,(2,6):C.GC_4060,(1,5):C.GC_1856,(3,5):C.GC_1937,(1,3):C.GC_2519,(3,3):C.GC_2600,(1,4):C.GC_2261,(3,4):C.GC_2342,(1,1):C.GC_3961,(3,1):C.GC_4303,(0,2):C.GC_3826,(2,2):C.GC_4141})

V_166 = Vertex(name = 'V_166',
               particles = [ P.c__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_413,(0,8):C.GC_943,(1,0):C.GC_3656,(3,0):C.GC_4223,(0,6):C.GC_3006,(2,6):C.GC_4061,(1,5):C.GC_1865,(3,5):C.GC_1946,(1,3):C.GC_2520,(3,3):C.GC_2601,(1,4):C.GC_2270,(3,4):C.GC_2351,(1,1):C.GC_3962,(3,1):C.GC_4304,(0,2):C.GC_3827,(2,2):C.GC_4142})

V_167 = Vertex(name = 'V_167',
               particles = [ P.t__tilde__, P.d, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_414,(0,8):C.GC_944,(1,0):C.GC_3657,(3,0):C.GC_4224,(0,6):C.GC_3007,(2,6):C.GC_4062,(1,5):C.GC_1874,(3,5):C.GC_1955,(1,3):C.GC_2521,(3,3):C.GC_2602,(1,4):C.GC_2279,(3,4):C.GC_2360,(1,1):C.GC_3963,(3,1):C.GC_4305,(0,2):C.GC_3828,(2,2):C.GC_4143})

V_168 = Vertex(name = 'V_168',
               particles = [ P.u__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_415,(0,8):C.GC_945,(1,0):C.GC_3658,(3,0):C.GC_4225,(0,6):C.GC_3008,(2,6):C.GC_4063,(1,5):C.GC_1803,(3,5):C.GC_1884,(1,3):C.GC_2522,(3,3):C.GC_2603,(1,4):C.GC_2208,(3,4):C.GC_2289,(1,1):C.GC_3964,(3,1):C.GC_4306,(0,2):C.GC_3829,(2,2):C.GC_4144})

V_169 = Vertex(name = 'V_169',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_416,(0,8):C.GC_946,(1,0):C.GC_3659,(3,0):C.GC_4226,(0,6):C.GC_3009,(2,6):C.GC_4064,(1,5):C.GC_1812,(3,5):C.GC_1893,(1,3):C.GC_2523,(3,3):C.GC_2604,(1,4):C.GC_2217,(3,4):C.GC_2298,(1,1):C.GC_3965,(3,1):C.GC_4307,(0,2):C.GC_3830,(2,2):C.GC_4145})

V_170 = Vertex(name = 'V_170',
               particles = [ P.t__tilde__, P.s, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_417,(0,8):C.GC_947,(1,0):C.GC_3660,(3,0):C.GC_4227,(0,6):C.GC_3010,(2,6):C.GC_4065,(1,5):C.GC_1821,(3,5):C.GC_1902,(1,3):C.GC_2524,(3,3):C.GC_2605,(1,4):C.GC_2226,(3,4):C.GC_2307,(1,1):C.GC_3966,(3,1):C.GC_4308,(0,2):C.GC_3831,(2,2):C.GC_4146})

V_171 = Vertex(name = 'V_171',
               particles = [ P.u__tilde__, P.s, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_418,(0,8):C.GC_948,(1,0):C.GC_3661,(3,0):C.GC_4228,(0,6):C.GC_3011,(2,6):C.GC_4066,(1,5):C.GC_1830,(3,5):C.GC_1911,(1,3):C.GC_2525,(3,3):C.GC_2606,(1,4):C.GC_2235,(3,4):C.GC_2316,(1,1):C.GC_3967,(3,1):C.GC_4309,(0,2):C.GC_3832,(2,2):C.GC_4147})

V_172 = Vertex(name = 'V_172',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_419,(0,8):C.GC_949,(1,0):C.GC_3662,(3,0):C.GC_4229,(0,6):C.GC_3012,(2,6):C.GC_4067,(1,5):C.GC_1839,(3,5):C.GC_1920,(1,3):C.GC_2526,(3,3):C.GC_2607,(1,4):C.GC_2244,(3,4):C.GC_2325,(1,1):C.GC_3968,(3,1):C.GC_4310,(0,2):C.GC_3833,(2,2):C.GC_4148})

V_173 = Vertex(name = 'V_173',
               particles = [ P.t__tilde__, P.s, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_420,(0,8):C.GC_950,(1,0):C.GC_3663,(3,0):C.GC_4230,(0,6):C.GC_3013,(2,6):C.GC_4068,(1,5):C.GC_1848,(3,5):C.GC_1929,(1,3):C.GC_2527,(3,3):C.GC_2608,(1,4):C.GC_2253,(3,4):C.GC_2334,(1,1):C.GC_3969,(3,1):C.GC_4311,(0,2):C.GC_3834,(2,2):C.GC_4149})

V_174 = Vertex(name = 'V_174',
               particles = [ P.u__tilde__, P.s, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_421,(0,8):C.GC_951,(1,0):C.GC_3664,(3,0):C.GC_4231,(0,6):C.GC_3014,(2,6):C.GC_4069,(1,5):C.GC_1857,(3,5):C.GC_1938,(1,3):C.GC_2528,(3,3):C.GC_2609,(1,4):C.GC_2262,(3,4):C.GC_2343,(1,1):C.GC_3970,(3,1):C.GC_4312,(0,2):C.GC_3835,(2,2):C.GC_4150})

V_175 = Vertex(name = 'V_175',
               particles = [ P.c__tilde__, P.s, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_422,(0,8):C.GC_952,(1,0):C.GC_3665,(3,0):C.GC_4232,(0,6):C.GC_3015,(2,6):C.GC_4070,(1,5):C.GC_1866,(3,5):C.GC_1947,(1,3):C.GC_2529,(3,3):C.GC_2610,(1,4):C.GC_2271,(3,4):C.GC_2352,(1,1):C.GC_3971,(3,1):C.GC_4313,(0,2):C.GC_3836,(2,2):C.GC_4151})

V_176 = Vertex(name = 'V_176',
               particles = [ P.t__tilde__, P.s, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_423,(0,8):C.GC_953,(1,0):C.GC_3666,(3,0):C.GC_4233,(0,6):C.GC_3016,(2,6):C.GC_4071,(1,5):C.GC_1875,(3,5):C.GC_1956,(1,3):C.GC_2530,(3,3):C.GC_2611,(1,4):C.GC_2280,(3,4):C.GC_2361,(1,1):C.GC_3972,(3,1):C.GC_4314,(0,2):C.GC_3837,(2,2):C.GC_4152})

V_177 = Vertex(name = 'V_177',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_424,(0,8):C.GC_954,(1,0):C.GC_3667,(3,0):C.GC_4234,(0,6):C.GC_3017,(2,6):C.GC_4072,(1,5):C.GC_1804,(3,5):C.GC_1885,(1,3):C.GC_2531,(3,3):C.GC_2612,(1,4):C.GC_2209,(3,4):C.GC_2290,(1,1):C.GC_3973,(3,1):C.GC_4315,(0,2):C.GC_3838,(2,2):C.GC_4153})

V_178 = Vertex(name = 'V_178',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_425,(0,8):C.GC_955,(1,0):C.GC_3668,(3,0):C.GC_4235,(0,6):C.GC_3018,(2,6):C.GC_4073,(1,5):C.GC_1813,(3,5):C.GC_1894,(1,3):C.GC_2532,(3,3):C.GC_2613,(1,4):C.GC_2218,(3,4):C.GC_2299,(1,1):C.GC_3974,(3,1):C.GC_4316,(0,2):C.GC_3839,(2,2):C.GC_4154})

V_179 = Vertex(name = 'V_179',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_426,(0,8):C.GC_956,(1,0):C.GC_3669,(3,0):C.GC_4236,(0,6):C.GC_3019,(2,6):C.GC_4074,(1,5):C.GC_1822,(3,5):C.GC_1903,(1,3):C.GC_2533,(3,3):C.GC_2614,(1,4):C.GC_2227,(3,4):C.GC_2308,(1,1):C.GC_3975,(3,1):C.GC_4317,(0,2):C.GC_3840,(2,2):C.GC_4155})

V_180 = Vertex(name = 'V_180',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_427,(0,8):C.GC_957,(1,0):C.GC_3670,(3,0):C.GC_4237,(0,6):C.GC_3020,(2,6):C.GC_4075,(1,5):C.GC_1831,(3,5):C.GC_1912,(1,3):C.GC_2534,(3,3):C.GC_2615,(1,4):C.GC_2236,(3,4):C.GC_2317,(1,1):C.GC_3976,(3,1):C.GC_4318,(0,2):C.GC_3841,(2,2):C.GC_4156})

V_181 = Vertex(name = 'V_181',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_428,(0,8):C.GC_958,(1,0):C.GC_3671,(3,0):C.GC_4238,(0,6):C.GC_3021,(2,6):C.GC_4076,(1,5):C.GC_1840,(3,5):C.GC_1921,(1,3):C.GC_2535,(3,3):C.GC_2616,(1,4):C.GC_2245,(3,4):C.GC_2326,(1,1):C.GC_3977,(3,1):C.GC_4319,(0,2):C.GC_3842,(2,2):C.GC_4157})

V_182 = Vertex(name = 'V_182',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_429,(0,8):C.GC_959,(1,0):C.GC_3672,(3,0):C.GC_4239,(0,6):C.GC_3022,(2,6):C.GC_4077,(1,5):C.GC_1849,(3,5):C.GC_1930,(1,3):C.GC_2536,(3,3):C.GC_2617,(1,4):C.GC_2254,(3,4):C.GC_2335,(1,1):C.GC_3978,(3,1):C.GC_4320,(0,2):C.GC_3843,(2,2):C.GC_4158})

V_183 = Vertex(name = 'V_183',
               particles = [ P.u__tilde__, P.s, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_430,(0,8):C.GC_960,(1,0):C.GC_3673,(3,0):C.GC_4240,(0,6):C.GC_3023,(2,6):C.GC_4078,(1,5):C.GC_1858,(3,5):C.GC_1939,(1,3):C.GC_2537,(3,3):C.GC_2618,(1,4):C.GC_2263,(3,4):C.GC_2344,(1,1):C.GC_3979,(3,1):C.GC_4321,(0,2):C.GC_3844,(2,2):C.GC_4159})

V_184 = Vertex(name = 'V_184',
               particles = [ P.c__tilde__, P.s, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_431,(0,8):C.GC_961,(1,0):C.GC_3674,(3,0):C.GC_4241,(0,6):C.GC_3024,(2,6):C.GC_4079,(1,5):C.GC_1867,(3,5):C.GC_1948,(1,3):C.GC_2538,(3,3):C.GC_2619,(1,4):C.GC_2272,(3,4):C.GC_2353,(1,1):C.GC_3980,(3,1):C.GC_4322,(0,2):C.GC_3845,(2,2):C.GC_4160})

V_185 = Vertex(name = 'V_185',
               particles = [ P.t__tilde__, P.s, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_432,(0,8):C.GC_962,(1,0):C.GC_3675,(3,0):C.GC_4242,(0,6):C.GC_3025,(2,6):C.GC_4080,(1,5):C.GC_1876,(3,5):C.GC_1957,(1,3):C.GC_2539,(3,3):C.GC_2620,(1,4):C.GC_2281,(3,4):C.GC_2362,(1,1):C.GC_3981,(3,1):C.GC_4323,(0,2):C.GC_3846,(2,2):C.GC_4161})

V_186 = Vertex(name = 'V_186',
               particles = [ P.u__tilde__, P.s, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_433,(0,8):C.GC_963,(1,0):C.GC_3676,(3,0):C.GC_4243,(0,6):C.GC_3026,(2,6):C.GC_4081,(1,5):C.GC_1805,(3,5):C.GC_1886,(1,3):C.GC_2540,(3,3):C.GC_2621,(1,4):C.GC_2210,(3,4):C.GC_2291,(1,1):C.GC_3982,(3,1):C.GC_4324,(0,2):C.GC_3847,(2,2):C.GC_4162})

V_187 = Vertex(name = 'V_187',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_434,(0,8):C.GC_964,(1,0):C.GC_3677,(3,0):C.GC_4244,(0,6):C.GC_3027,(2,6):C.GC_4082,(1,5):C.GC_1814,(3,5):C.GC_1895,(1,3):C.GC_2541,(3,3):C.GC_2622,(1,4):C.GC_2219,(3,4):C.GC_2300,(1,1):C.GC_3983,(3,1):C.GC_4325,(0,2):C.GC_3848,(2,2):C.GC_4163})

V_188 = Vertex(name = 'V_188',
               particles = [ P.t__tilde__, P.s, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_435,(0,8):C.GC_965,(1,0):C.GC_3678,(3,0):C.GC_4245,(0,6):C.GC_3028,(2,6):C.GC_4083,(1,5):C.GC_1823,(3,5):C.GC_1904,(1,3):C.GC_2542,(3,3):C.GC_2623,(1,4):C.GC_2228,(3,4):C.GC_2309,(1,1):C.GC_3984,(3,1):C.GC_4326,(0,2):C.GC_3849,(2,2):C.GC_4164})

V_189 = Vertex(name = 'V_189',
               particles = [ P.u__tilde__, P.s, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_436,(0,8):C.GC_966,(1,0):C.GC_3679,(3,0):C.GC_4246,(0,6):C.GC_3029,(2,6):C.GC_4084,(1,5):C.GC_1832,(3,5):C.GC_1913,(1,3):C.GC_2543,(3,3):C.GC_2624,(1,4):C.GC_2237,(3,4):C.GC_2318,(1,1):C.GC_3985,(3,1):C.GC_4327,(0,2):C.GC_3850,(2,2):C.GC_4165})

V_190 = Vertex(name = 'V_190',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_437,(0,8):C.GC_967,(1,0):C.GC_3680,(3,0):C.GC_4247,(0,6):C.GC_3030,(2,6):C.GC_4085,(1,5):C.GC_1841,(3,5):C.GC_1922,(1,3):C.GC_2544,(3,3):C.GC_2625,(1,4):C.GC_2246,(3,4):C.GC_2327,(1,1):C.GC_3986,(3,1):C.GC_4328,(0,2):C.GC_3851,(2,2):C.GC_4166})

V_191 = Vertex(name = 'V_191',
               particles = [ P.t__tilde__, P.s, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_438,(0,8):C.GC_968,(1,0):C.GC_3681,(3,0):C.GC_4248,(0,6):C.GC_3031,(2,6):C.GC_4086,(1,5):C.GC_1850,(3,5):C.GC_1931,(1,3):C.GC_2545,(3,3):C.GC_2626,(1,4):C.GC_2255,(3,4):C.GC_2336,(1,1):C.GC_3987,(3,1):C.GC_4329,(0,2):C.GC_3852,(2,2):C.GC_4167})

V_192 = Vertex(name = 'V_192',
               particles = [ P.u__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_439,(0,8):C.GC_969,(1,0):C.GC_3682,(3,0):C.GC_4249,(0,6):C.GC_3032,(2,6):C.GC_4087,(1,5):C.GC_1859,(3,5):C.GC_1940,(1,3):C.GC_2546,(3,3):C.GC_2627,(1,4):C.GC_2264,(3,4):C.GC_2345,(1,1):C.GC_3988,(3,1):C.GC_4330,(0,2):C.GC_3853,(2,2):C.GC_4168})

V_193 = Vertex(name = 'V_193',
               particles = [ P.c__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_440,(0,8):C.GC_970,(1,0):C.GC_3683,(3,0):C.GC_4250,(0,6):C.GC_3033,(2,6):C.GC_4088,(1,5):C.GC_1868,(3,5):C.GC_1949,(1,3):C.GC_2547,(3,3):C.GC_2628,(1,4):C.GC_2273,(3,4):C.GC_2354,(1,1):C.GC_3989,(3,1):C.GC_4331,(0,2):C.GC_3854,(2,2):C.GC_4169})

V_194 = Vertex(name = 'V_194',
               particles = [ P.t__tilde__, P.s, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_441,(0,8):C.GC_971,(1,0):C.GC_3684,(3,0):C.GC_4251,(0,6):C.GC_3034,(2,6):C.GC_4089,(1,5):C.GC_1877,(3,5):C.GC_1958,(1,3):C.GC_2548,(3,3):C.GC_2629,(1,4):C.GC_2282,(3,4):C.GC_2363,(1,1):C.GC_3990,(3,1):C.GC_4332,(0,2):C.GC_3855,(2,2):C.GC_4170})

V_195 = Vertex(name = 'V_195',
               particles = [ P.u__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_442,(0,8):C.GC_972,(1,0):C.GC_3685,(3,0):C.GC_4252,(0,6):C.GC_3035,(2,6):C.GC_4090,(1,5):C.GC_1806,(3,5):C.GC_1887,(1,3):C.GC_2549,(3,3):C.GC_2630,(1,4):C.GC_2211,(3,4):C.GC_2292,(1,1):C.GC_3991,(3,1):C.GC_4333,(0,2):C.GC_3856,(2,2):C.GC_4171})

V_196 = Vertex(name = 'V_196',
               particles = [ P.c__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_443,(0,8):C.GC_973,(1,0):C.GC_3686,(3,0):C.GC_4253,(0,6):C.GC_3036,(2,6):C.GC_4091,(1,5):C.GC_1815,(3,5):C.GC_1896,(1,3):C.GC_2550,(3,3):C.GC_2631,(1,4):C.GC_2220,(3,4):C.GC_2301,(1,1):C.GC_3992,(3,1):C.GC_4334,(0,2):C.GC_3857,(2,2):C.GC_4172})

V_197 = Vertex(name = 'V_197',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_444,(0,8):C.GC_974,(1,0):C.GC_3687,(3,0):C.GC_4254,(0,6):C.GC_3037,(2,6):C.GC_4092,(1,5):C.GC_1824,(3,5):C.GC_1905,(1,3):C.GC_2551,(3,3):C.GC_2632,(1,4):C.GC_2229,(3,4):C.GC_2310,(1,1):C.GC_3993,(3,1):C.GC_4335,(0,2):C.GC_3858,(2,2):C.GC_4173})

V_198 = Vertex(name = 'V_198',
               particles = [ P.u__tilde__, P.b, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_445,(0,8):C.GC_975,(1,0):C.GC_3688,(3,0):C.GC_4255,(0,6):C.GC_3038,(2,6):C.GC_4093,(1,5):C.GC_1833,(3,5):C.GC_1914,(1,3):C.GC_2552,(3,3):C.GC_2633,(1,4):C.GC_2238,(3,4):C.GC_2319,(1,1):C.GC_3994,(3,1):C.GC_4336,(0,2):C.GC_3859,(2,2):C.GC_4174})

V_199 = Vertex(name = 'V_199',
               particles = [ P.c__tilde__, P.b, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_446,(0,8):C.GC_976,(1,0):C.GC_3689,(3,0):C.GC_4256,(0,6):C.GC_3039,(2,6):C.GC_4094,(1,5):C.GC_1842,(3,5):C.GC_1923,(1,3):C.GC_2553,(3,3):C.GC_2634,(1,4):C.GC_2247,(3,4):C.GC_2328,(1,1):C.GC_3995,(3,1):C.GC_4337,(0,2):C.GC_3860,(2,2):C.GC_4175})

V_200 = Vertex(name = 'V_200',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_447,(0,8):C.GC_977,(1,0):C.GC_3690,(3,0):C.GC_4257,(0,6):C.GC_3040,(2,6):C.GC_4095,(1,5):C.GC_1851,(3,5):C.GC_1932,(1,3):C.GC_2554,(3,3):C.GC_2635,(1,4):C.GC_2256,(3,4):C.GC_2337,(1,1):C.GC_3996,(3,1):C.GC_4338,(0,2):C.GC_3861,(2,2):C.GC_4176})

V_201 = Vertex(name = 'V_201',
               particles = [ P.u__tilde__, P.b, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_448,(0,8):C.GC_978,(1,0):C.GC_3691,(3,0):C.GC_4258,(0,6):C.GC_3041,(2,6):C.GC_4096,(1,5):C.GC_1860,(3,5):C.GC_1941,(1,3):C.GC_2555,(3,3):C.GC_2636,(1,4):C.GC_2265,(3,4):C.GC_2346,(1,1):C.GC_3997,(3,1):C.GC_4339,(0,2):C.GC_3862,(2,2):C.GC_4177})

V_202 = Vertex(name = 'V_202',
               particles = [ P.c__tilde__, P.b, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_449,(0,8):C.GC_979,(1,0):C.GC_3692,(3,0):C.GC_4259,(0,6):C.GC_3042,(2,6):C.GC_4097,(1,5):C.GC_1869,(3,5):C.GC_1950,(1,3):C.GC_2556,(3,3):C.GC_2637,(1,4):C.GC_2274,(3,4):C.GC_2355,(1,1):C.GC_3998,(3,1):C.GC_4340,(0,2):C.GC_3863,(2,2):C.GC_4178})

V_203 = Vertex(name = 'V_203',
               particles = [ P.t__tilde__, P.b, P.d__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_450,(0,8):C.GC_980,(1,0):C.GC_3693,(3,0):C.GC_4260,(0,6):C.GC_3043,(2,6):C.GC_4098,(1,5):C.GC_1878,(3,5):C.GC_1959,(1,3):C.GC_2557,(3,3):C.GC_2638,(1,4):C.GC_2283,(3,4):C.GC_2364,(1,1):C.GC_3999,(3,1):C.GC_4341,(0,2):C.GC_3864,(2,2):C.GC_4179})

V_204 = Vertex(name = 'V_204',
               particles = [ P.u__tilde__, P.b, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_451,(0,8):C.GC_981,(1,0):C.GC_3694,(3,0):C.GC_4261,(0,6):C.GC_3044,(2,6):C.GC_4099,(1,5):C.GC_1807,(3,5):C.GC_1888,(1,3):C.GC_2558,(3,3):C.GC_2639,(1,4):C.GC_2212,(3,4):C.GC_2293,(1,1):C.GC_4000,(3,1):C.GC_4342,(0,2):C.GC_3865,(2,2):C.GC_4180})

V_205 = Vertex(name = 'V_205',
               particles = [ P.c__tilde__, P.b, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_452,(0,8):C.GC_982,(1,0):C.GC_3695,(3,0):C.GC_4262,(0,6):C.GC_3045,(2,6):C.GC_4100,(1,5):C.GC_1816,(3,5):C.GC_1897,(1,3):C.GC_2559,(3,3):C.GC_2640,(1,4):C.GC_2221,(3,4):C.GC_2302,(1,1):C.GC_4001,(3,1):C.GC_4343,(0,2):C.GC_3866,(2,2):C.GC_4181})

V_206 = Vertex(name = 'V_206',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_453,(0,8):C.GC_983,(1,0):C.GC_3696,(3,0):C.GC_4263,(0,6):C.GC_3046,(2,6):C.GC_4101,(1,5):C.GC_1825,(3,5):C.GC_1906,(1,3):C.GC_2560,(3,3):C.GC_2641,(1,4):C.GC_2230,(3,4):C.GC_2311,(1,1):C.GC_4002,(3,1):C.GC_4344,(0,2):C.GC_3867,(2,2):C.GC_4182})

V_207 = Vertex(name = 'V_207',
               particles = [ P.u__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_454,(0,8):C.GC_984,(1,0):C.GC_3697,(3,0):C.GC_4264,(0,6):C.GC_3047,(2,6):C.GC_4102,(1,5):C.GC_1834,(3,5):C.GC_1915,(1,3):C.GC_2561,(3,3):C.GC_2642,(1,4):C.GC_2239,(3,4):C.GC_2320,(1,1):C.GC_4003,(3,1):C.GC_4345,(0,2):C.GC_3868,(2,2):C.GC_4183})

V_208 = Vertex(name = 'V_208',
               particles = [ P.c__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_455,(0,8):C.GC_985,(1,0):C.GC_3698,(3,0):C.GC_4265,(0,6):C.GC_3048,(2,6):C.GC_4103,(1,5):C.GC_1843,(3,5):C.GC_1924,(1,3):C.GC_2562,(3,3):C.GC_2643,(1,4):C.GC_2248,(3,4):C.GC_2329,(1,1):C.GC_4004,(3,1):C.GC_4346,(0,2):C.GC_3869,(2,2):C.GC_4184})

V_209 = Vertex(name = 'V_209',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_456,(0,8):C.GC_986,(1,0):C.GC_3699,(3,0):C.GC_4266,(0,6):C.GC_3049,(2,6):C.GC_4104,(1,5):C.GC_1852,(3,5):C.GC_1933,(1,3):C.GC_2563,(3,3):C.GC_2644,(1,4):C.GC_2257,(3,4):C.GC_2338,(1,1):C.GC_4005,(3,1):C.GC_4347,(0,2):C.GC_3870,(2,2):C.GC_4185})

V_210 = Vertex(name = 'V_210',
               particles = [ P.u__tilde__, P.b, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_457,(0,8):C.GC_987,(1,0):C.GC_3700,(3,0):C.GC_4267,(0,6):C.GC_3050,(2,6):C.GC_4105,(1,5):C.GC_1861,(3,5):C.GC_1942,(1,3):C.GC_2564,(3,3):C.GC_2645,(1,4):C.GC_2266,(3,4):C.GC_2347,(1,1):C.GC_4006,(3,1):C.GC_4348,(0,2):C.GC_3871,(2,2):C.GC_4186})

V_211 = Vertex(name = 'V_211',
               particles = [ P.c__tilde__, P.b, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_458,(0,8):C.GC_988,(1,0):C.GC_3701,(3,0):C.GC_4268,(0,6):C.GC_3051,(2,6):C.GC_4106,(1,5):C.GC_1870,(3,5):C.GC_1951,(1,3):C.GC_2565,(3,3):C.GC_2646,(1,4):C.GC_2275,(3,4):C.GC_2356,(1,1):C.GC_4007,(3,1):C.GC_4349,(0,2):C.GC_3872,(2,2):C.GC_4187})

V_212 = Vertex(name = 'V_212',
               particles = [ P.t__tilde__, P.b, P.s__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_459,(0,8):C.GC_989,(1,0):C.GC_3702,(3,0):C.GC_4269,(0,6):C.GC_3052,(2,6):C.GC_4107,(1,5):C.GC_1879,(3,5):C.GC_1960,(1,3):C.GC_2566,(3,3):C.GC_2647,(1,4):C.GC_2284,(3,4):C.GC_2365,(1,1):C.GC_4008,(3,1):C.GC_4350,(0,2):C.GC_3873,(2,2):C.GC_4188})

V_213 = Vertex(name = 'V_213',
               particles = [ P.u__tilde__, P.b, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_460,(0,8):C.GC_990,(1,0):C.GC_3703,(3,0):C.GC_4270,(0,6):C.GC_3053,(2,6):C.GC_4108,(1,5):C.GC_1808,(3,5):C.GC_1889,(1,3):C.GC_2567,(3,3):C.GC_2648,(1,4):C.GC_2213,(3,4):C.GC_2294,(1,1):C.GC_4009,(3,1):C.GC_4351,(0,2):C.GC_3874,(2,2):C.GC_4189})

V_214 = Vertex(name = 'V_214',
               particles = [ P.c__tilde__, P.b, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_461,(0,8):C.GC_991,(1,0):C.GC_3704,(3,0):C.GC_4271,(0,6):C.GC_3054,(2,6):C.GC_4109,(1,5):C.GC_1817,(3,5):C.GC_1898,(1,3):C.GC_2568,(3,3):C.GC_2649,(1,4):C.GC_2222,(3,4):C.GC_2303,(1,1):C.GC_4010,(3,1):C.GC_4352,(0,2):C.GC_3875,(2,2):C.GC_4190})

V_215 = Vertex(name = 'V_215',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.u ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_462,(0,8):C.GC_992,(1,0):C.GC_3705,(3,0):C.GC_4272,(0,6):C.GC_3055,(2,6):C.GC_4110,(1,5):C.GC_1826,(3,5):C.GC_1907,(1,3):C.GC_2569,(3,3):C.GC_2650,(1,4):C.GC_2231,(3,4):C.GC_2312,(1,1):C.GC_4011,(3,1):C.GC_4353,(0,2):C.GC_3876,(2,2):C.GC_4191})

V_216 = Vertex(name = 'V_216',
               particles = [ P.u__tilde__, P.b, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_463,(0,8):C.GC_993,(1,0):C.GC_3706,(3,0):C.GC_4273,(0,6):C.GC_3056,(2,6):C.GC_4111,(1,5):C.GC_1835,(3,5):C.GC_1916,(1,3):C.GC_2570,(3,3):C.GC_2651,(1,4):C.GC_2240,(3,4):C.GC_2321,(1,1):C.GC_4012,(3,1):C.GC_4354,(0,2):C.GC_3877,(2,2):C.GC_4192})

V_217 = Vertex(name = 'V_217',
               particles = [ P.c__tilde__, P.b, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_464,(0,8):C.GC_994,(1,0):C.GC_3707,(3,0):C.GC_4274,(0,6):C.GC_3057,(2,6):C.GC_4112,(1,5):C.GC_1844,(3,5):C.GC_1925,(1,3):C.GC_2571,(3,3):C.GC_2652,(1,4):C.GC_2249,(3,4):C.GC_2330,(1,1):C.GC_4013,(3,1):C.GC_4355,(0,2):C.GC_3878,(2,2):C.GC_4193})

V_218 = Vertex(name = 'V_218',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.c ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_465,(0,8):C.GC_995,(1,0):C.GC_3708,(3,0):C.GC_4275,(0,6):C.GC_3058,(2,6):C.GC_4113,(1,5):C.GC_1853,(3,5):C.GC_1934,(1,3):C.GC_2572,(3,3):C.GC_2653,(1,4):C.GC_2258,(3,4):C.GC_2339,(1,1):C.GC_4014,(3,1):C.GC_4356,(0,2):C.GC_3879,(2,2):C.GC_4194})

V_219 = Vertex(name = 'V_219',
               particles = [ P.u__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_466,(0,8):C.GC_996,(1,0):C.GC_3709,(3,0):C.GC_4276,(0,6):C.GC_3059,(2,6):C.GC_4114,(1,5):C.GC_1862,(3,5):C.GC_1943,(1,3):C.GC_2573,(3,3):C.GC_2654,(1,4):C.GC_2267,(3,4):C.GC_2348,(1,1):C.GC_4015,(3,1):C.GC_4357,(0,2):C.GC_3880,(2,2):C.GC_4195})

V_220 = Vertex(name = 'V_220',
               particles = [ P.c__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_467,(0,8):C.GC_997,(1,0):C.GC_3710,(3,0):C.GC_4277,(0,6):C.GC_3060,(2,6):C.GC_4115,(1,5):C.GC_1871,(3,5):C.GC_1952,(1,3):C.GC_2574,(3,3):C.GC_2655,(1,4):C.GC_2276,(3,4):C.GC_2357,(1,1):C.GC_4016,(3,1):C.GC_4358,(0,2):C.GC_3881,(2,2):C.GC_4196})

V_221 = Vertex(name = 'V_221',
               particles = [ P.t__tilde__, P.b, P.b__tilde__, P.t ],
               color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
               lorentz = [ L.FFFF1, L.FFFF11, L.FFFF13, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF2, L.FFFF4, L.FFFF5 ],
               couplings = {(1,7):C.GC_468,(0,8):C.GC_998,(1,0):C.GC_3711,(3,0):C.GC_4278,(0,6):C.GC_3061,(2,6):C.GC_4116,(1,5):C.GC_1880,(3,5):C.GC_1961,(1,3):C.GC_2575,(3,3):C.GC_2656,(1,4):C.GC_2285,(3,4):C.GC_2366,(1,1):C.GC_4017,(3,1):C.GC_4359,(0,2):C.GC_3882,(2,2):C.GC_4197})

V_222 = Vertex(name = 'V_222',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2738,(0,5):C.GC_2820,(0,3):C.GC_2819,(0,4):C.GC_2819,(0,1):C.GC_2657,(0,0):C.GC_5779})

V_223 = Vertex(name = 'V_223',
               particles = [ P.vm__tilde__, P.e__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2739,(0,5):C.GC_2822,(0,3):C.GC_2821,(0,4):C.GC_2821,(0,1):C.GC_2658,(0,0):C.GC_5806})

V_224 = Vertex(name = 'V_224',
               particles = [ P.vt__tilde__, P.e__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2740,(0,5):C.GC_2824,(0,3):C.GC_2823,(0,4):C.GC_2823,(0,1):C.GC_2659,(0,0):C.GC_5833})

V_225 = Vertex(name = 'V_225',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2741,(0,5):C.GC_2826,(0,3):C.GC_2825,(0,4):C.GC_2825,(0,1):C.GC_2660,(0,0):C.GC_5780})

V_226 = Vertex(name = 'V_226',
               particles = [ P.vm__tilde__, P.e__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2742,(0,5):C.GC_2828,(0,3):C.GC_2827,(0,4):C.GC_2827,(0,1):C.GC_2661,(0,0):C.GC_5807})

V_227 = Vertex(name = 'V_227',
               particles = [ P.vt__tilde__, P.e__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2743,(0,5):C.GC_2830,(0,3):C.GC_2829,(0,4):C.GC_2829,(0,1):C.GC_2662,(0,0):C.GC_5834})

V_228 = Vertex(name = 'V_228',
               particles = [ P.ve__tilde__, P.e__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2744,(0,5):C.GC_2832,(0,3):C.GC_2831,(0,4):C.GC_2831,(0,1):C.GC_2663,(0,0):C.GC_5781})

V_229 = Vertex(name = 'V_229',
               particles = [ P.vm__tilde__, P.e__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2745,(0,5):C.GC_2834,(0,3):C.GC_2833,(0,4):C.GC_2833,(0,1):C.GC_2664,(0,0):C.GC_5808})

V_230 = Vertex(name = 'V_230',
               particles = [ P.vt__tilde__, P.e__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2746,(0,5):C.GC_2836,(0,3):C.GC_2835,(0,4):C.GC_2835,(0,1):C.GC_2665,(0,0):C.GC_5835})

V_231 = Vertex(name = 'V_231',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2747,(0,5):C.GC_2838,(0,3):C.GC_2837,(0,4):C.GC_2837,(0,1):C.GC_2666,(0,0):C.GC_5782})

V_232 = Vertex(name = 'V_232',
               particles = [ P.vm__tilde__, P.e__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2748,(0,5):C.GC_2840,(0,3):C.GC_2839,(0,4):C.GC_2839,(0,1):C.GC_2667,(0,0):C.GC_5809})

V_233 = Vertex(name = 'V_233',
               particles = [ P.vt__tilde__, P.e__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2749,(0,5):C.GC_2842,(0,3):C.GC_2841,(0,4):C.GC_2841,(0,1):C.GC_2668,(0,0):C.GC_5836})

V_234 = Vertex(name = 'V_234',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2750,(0,5):C.GC_2844,(0,3):C.GC_2843,(0,4):C.GC_2843,(0,1):C.GC_2669,(0,0):C.GC_5783})

V_235 = Vertex(name = 'V_235',
               particles = [ P.vm__tilde__, P.e__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2751,(0,5):C.GC_2846,(0,3):C.GC_2845,(0,4):C.GC_2845,(0,1):C.GC_2670,(0,0):C.GC_5810})

V_236 = Vertex(name = 'V_236',
               particles = [ P.vt__tilde__, P.e__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2752,(0,5):C.GC_2848,(0,3):C.GC_2847,(0,4):C.GC_2847,(0,1):C.GC_2671,(0,0):C.GC_5837})

V_237 = Vertex(name = 'V_237',
               particles = [ P.ve__tilde__, P.e__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2753,(0,5):C.GC_2850,(0,3):C.GC_2849,(0,4):C.GC_2849,(0,1):C.GC_2672,(0,0):C.GC_5784})

V_238 = Vertex(name = 'V_238',
               particles = [ P.vm__tilde__, P.e__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2754,(0,5):C.GC_2852,(0,3):C.GC_2851,(0,4):C.GC_2851,(0,1):C.GC_2673,(0,0):C.GC_5811})

V_239 = Vertex(name = 'V_239',
               particles = [ P.vt__tilde__, P.e__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2755,(0,5):C.GC_2854,(0,3):C.GC_2853,(0,4):C.GC_2853,(0,1):C.GC_2674,(0,0):C.GC_5838})

V_240 = Vertex(name = 'V_240',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2756,(0,5):C.GC_2856,(0,3):C.GC_2855,(0,4):C.GC_2855,(0,1):C.GC_2675,(0,0):C.GC_5785})

V_241 = Vertex(name = 'V_241',
               particles = [ P.vm__tilde__, P.e__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2757,(0,5):C.GC_2858,(0,3):C.GC_2857,(0,4):C.GC_2857,(0,1):C.GC_2676,(0,0):C.GC_5812})

V_242 = Vertex(name = 'V_242',
               particles = [ P.vt__tilde__, P.e__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2758,(0,5):C.GC_2860,(0,3):C.GC_2859,(0,4):C.GC_2859,(0,1):C.GC_2677,(0,0):C.GC_5839})

V_243 = Vertex(name = 'V_243',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2759,(0,5):C.GC_2862,(0,3):C.GC_2861,(0,4):C.GC_2861,(0,1):C.GC_2678,(0,0):C.GC_5786})

V_244 = Vertex(name = 'V_244',
               particles = [ P.vm__tilde__, P.e__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2760,(0,5):C.GC_2864,(0,3):C.GC_2863,(0,4):C.GC_2863,(0,1):C.GC_2679,(0,0):C.GC_5813})

V_245 = Vertex(name = 'V_245',
               particles = [ P.vt__tilde__, P.e__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2761,(0,5):C.GC_2866,(0,3):C.GC_2865,(0,4):C.GC_2865,(0,1):C.GC_2680,(0,0):C.GC_5840})

V_246 = Vertex(name = 'V_246',
               particles = [ P.ve__tilde__, P.e__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2762,(0,5):C.GC_2868,(0,3):C.GC_2867,(0,4):C.GC_2867,(0,1):C.GC_2681,(0,0):C.GC_5787})

V_247 = Vertex(name = 'V_247',
               particles = [ P.vm__tilde__, P.e__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2763,(0,5):C.GC_2870,(0,3):C.GC_2869,(0,4):C.GC_2869,(0,1):C.GC_2682,(0,0):C.GC_5814})

V_248 = Vertex(name = 'V_248',
               particles = [ P.vt__tilde__, P.e__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2764,(0,5):C.GC_2872,(0,3):C.GC_2871,(0,4):C.GC_2871,(0,1):C.GC_2683,(0,0):C.GC_5841})

V_249 = Vertex(name = 'V_249',
               particles = [ P.ve__tilde__, P.mu__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2765,(0,5):C.GC_2874,(0,3):C.GC_2873,(0,4):C.GC_2873,(0,1):C.GC_2684,(0,0):C.GC_5788})

V_250 = Vertex(name = 'V_250',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2766,(0,5):C.GC_2876,(0,3):C.GC_2875,(0,4):C.GC_2875,(0,1):C.GC_2685,(0,0):C.GC_5815})

V_251 = Vertex(name = 'V_251',
               particles = [ P.vt__tilde__, P.mu__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2767,(0,5):C.GC_2878,(0,3):C.GC_2877,(0,4):C.GC_2877,(0,1):C.GC_2686,(0,0):C.GC_5842})

V_252 = Vertex(name = 'V_252',
               particles = [ P.ve__tilde__, P.mu__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2768,(0,5):C.GC_2880,(0,3):C.GC_2879,(0,4):C.GC_2879,(0,1):C.GC_2687,(0,0):C.GC_5789})

V_253 = Vertex(name = 'V_253',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2769,(0,5):C.GC_2882,(0,3):C.GC_2881,(0,4):C.GC_2881,(0,1):C.GC_2688,(0,0):C.GC_5816})

V_254 = Vertex(name = 'V_254',
               particles = [ P.vt__tilde__, P.mu__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2770,(0,5):C.GC_2884,(0,3):C.GC_2883,(0,4):C.GC_2883,(0,1):C.GC_2689,(0,0):C.GC_5843})

V_255 = Vertex(name = 'V_255',
               particles = [ P.ve__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2771,(0,5):C.GC_2886,(0,3):C.GC_2885,(0,4):C.GC_2885,(0,1):C.GC_2690,(0,0):C.GC_5790})

V_256 = Vertex(name = 'V_256',
               particles = [ P.vm__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2772,(0,5):C.GC_2888,(0,3):C.GC_2887,(0,4):C.GC_2887,(0,1):C.GC_2691,(0,0):C.GC_5817})

V_257 = Vertex(name = 'V_257',
               particles = [ P.vt__tilde__, P.mu__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2773,(0,5):C.GC_2890,(0,3):C.GC_2889,(0,4):C.GC_2889,(0,1):C.GC_2692,(0,0):C.GC_5844})

V_258 = Vertex(name = 'V_258',
               particles = [ P.ve__tilde__, P.mu__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2774,(0,5):C.GC_2892,(0,3):C.GC_2891,(0,4):C.GC_2891,(0,1):C.GC_2693,(0,0):C.GC_5791})

V_259 = Vertex(name = 'V_259',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2775,(0,5):C.GC_2894,(0,3):C.GC_2893,(0,4):C.GC_2893,(0,1):C.GC_2694,(0,0):C.GC_5818})

V_260 = Vertex(name = 'V_260',
               particles = [ P.vt__tilde__, P.mu__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2776,(0,5):C.GC_2896,(0,3):C.GC_2895,(0,4):C.GC_2895,(0,1):C.GC_2695,(0,0):C.GC_5845})

V_261 = Vertex(name = 'V_261',
               particles = [ P.ve__tilde__, P.mu__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2777,(0,5):C.GC_2898,(0,3):C.GC_2897,(0,4):C.GC_2897,(0,1):C.GC_2696,(0,0):C.GC_5792})

V_262 = Vertex(name = 'V_262',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2778,(0,5):C.GC_2900,(0,3):C.GC_2899,(0,4):C.GC_2899,(0,1):C.GC_2697,(0,0):C.GC_5819})

V_263 = Vertex(name = 'V_263',
               particles = [ P.vt__tilde__, P.mu__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2779,(0,5):C.GC_2902,(0,3):C.GC_2901,(0,4):C.GC_2901,(0,1):C.GC_2698,(0,0):C.GC_5846})

V_264 = Vertex(name = 'V_264',
               particles = [ P.ve__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2780,(0,5):C.GC_2904,(0,3):C.GC_2903,(0,4):C.GC_2903,(0,1):C.GC_2699,(0,0):C.GC_5793})

V_265 = Vertex(name = 'V_265',
               particles = [ P.vm__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2781,(0,5):C.GC_2906,(0,3):C.GC_2905,(0,4):C.GC_2905,(0,1):C.GC_2700,(0,0):C.GC_5820})

V_266 = Vertex(name = 'V_266',
               particles = [ P.vt__tilde__, P.mu__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2782,(0,5):C.GC_2908,(0,3):C.GC_2907,(0,4):C.GC_2907,(0,1):C.GC_2701,(0,0):C.GC_5847})

V_267 = Vertex(name = 'V_267',
               particles = [ P.ve__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2783,(0,5):C.GC_2910,(0,3):C.GC_2909,(0,4):C.GC_2909,(0,1):C.GC_2702,(0,0):C.GC_5794})

V_268 = Vertex(name = 'V_268',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2784,(0,5):C.GC_2912,(0,3):C.GC_2911,(0,4):C.GC_2911,(0,1):C.GC_2703,(0,0):C.GC_5821})

V_269 = Vertex(name = 'V_269',
               particles = [ P.vt__tilde__, P.mu__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2785,(0,5):C.GC_2914,(0,3):C.GC_2913,(0,4):C.GC_2913,(0,1):C.GC_2704,(0,0):C.GC_5848})

V_270 = Vertex(name = 'V_270',
               particles = [ P.ve__tilde__, P.mu__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2786,(0,5):C.GC_2916,(0,3):C.GC_2915,(0,4):C.GC_2915,(0,1):C.GC_2705,(0,0):C.GC_5795})

V_271 = Vertex(name = 'V_271',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2787,(0,5):C.GC_2918,(0,3):C.GC_2917,(0,4):C.GC_2917,(0,1):C.GC_2706,(0,0):C.GC_5822})

V_272 = Vertex(name = 'V_272',
               particles = [ P.vt__tilde__, P.mu__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2788,(0,5):C.GC_2920,(0,3):C.GC_2919,(0,4):C.GC_2919,(0,1):C.GC_2707,(0,0):C.GC_5849})

V_273 = Vertex(name = 'V_273',
               particles = [ P.ve__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2789,(0,5):C.GC_2922,(0,3):C.GC_2921,(0,4):C.GC_2921,(0,1):C.GC_2708,(0,0):C.GC_5796})

V_274 = Vertex(name = 'V_274',
               particles = [ P.vm__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2790,(0,5):C.GC_2924,(0,3):C.GC_2923,(0,4):C.GC_2923,(0,1):C.GC_2709,(0,0):C.GC_5823})

V_275 = Vertex(name = 'V_275',
               particles = [ P.vt__tilde__, P.mu__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2791,(0,5):C.GC_2926,(0,3):C.GC_2925,(0,4):C.GC_2925,(0,1):C.GC_2710,(0,0):C.GC_5850})

V_276 = Vertex(name = 'V_276',
               particles = [ P.ve__tilde__, P.ta__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2792,(0,5):C.GC_2928,(0,3):C.GC_2927,(0,4):C.GC_2927,(0,1):C.GC_2711,(0,0):C.GC_5797})

V_277 = Vertex(name = 'V_277',
               particles = [ P.vm__tilde__, P.ta__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2793,(0,5):C.GC_2930,(0,3):C.GC_2929,(0,4):C.GC_2929,(0,1):C.GC_2712,(0,0):C.GC_5824})

V_278 = Vertex(name = 'V_278',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2794,(0,5):C.GC_2932,(0,3):C.GC_2931,(0,4):C.GC_2931,(0,1):C.GC_2713,(0,0):C.GC_5851})

V_279 = Vertex(name = 'V_279',
               particles = [ P.ve__tilde__, P.ta__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2795,(0,5):C.GC_2934,(0,3):C.GC_2933,(0,4):C.GC_2933,(0,1):C.GC_2714,(0,0):C.GC_5798})

V_280 = Vertex(name = 'V_280',
               particles = [ P.vm__tilde__, P.ta__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2796,(0,5):C.GC_2936,(0,3):C.GC_2935,(0,4):C.GC_2935,(0,1):C.GC_2715,(0,0):C.GC_5825})

V_281 = Vertex(name = 'V_281',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2797,(0,5):C.GC_2938,(0,3):C.GC_2937,(0,4):C.GC_2937,(0,1):C.GC_2716,(0,0):C.GC_5852})

V_282 = Vertex(name = 'V_282',
               particles = [ P.ve__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2798,(0,5):C.GC_2940,(0,3):C.GC_2939,(0,4):C.GC_2939,(0,1):C.GC_2717,(0,0):C.GC_5799})

V_283 = Vertex(name = 'V_283',
               particles = [ P.vm__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2799,(0,5):C.GC_2942,(0,3):C.GC_2941,(0,4):C.GC_2941,(0,1):C.GC_2718,(0,0):C.GC_5826})

V_284 = Vertex(name = 'V_284',
               particles = [ P.vt__tilde__, P.ta__minus__, P.d__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2800,(0,5):C.GC_2944,(0,3):C.GC_2943,(0,4):C.GC_2943,(0,1):C.GC_2719,(0,0):C.GC_5853})

V_285 = Vertex(name = 'V_285',
               particles = [ P.ve__tilde__, P.ta__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2801,(0,5):C.GC_2946,(0,3):C.GC_2945,(0,4):C.GC_2945,(0,1):C.GC_2720,(0,0):C.GC_5800})

V_286 = Vertex(name = 'V_286',
               particles = [ P.vm__tilde__, P.ta__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2802,(0,5):C.GC_2948,(0,3):C.GC_2947,(0,4):C.GC_2947,(0,1):C.GC_2721,(0,0):C.GC_5827})

V_287 = Vertex(name = 'V_287',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2803,(0,5):C.GC_2950,(0,3):C.GC_2949,(0,4):C.GC_2949,(0,1):C.GC_2722,(0,0):C.GC_5854})

V_288 = Vertex(name = 'V_288',
               particles = [ P.ve__tilde__, P.ta__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2804,(0,5):C.GC_2952,(0,3):C.GC_2951,(0,4):C.GC_2951,(0,1):C.GC_2723,(0,0):C.GC_5801})

V_289 = Vertex(name = 'V_289',
               particles = [ P.vm__tilde__, P.ta__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2805,(0,5):C.GC_2954,(0,3):C.GC_2953,(0,4):C.GC_2953,(0,1):C.GC_2724,(0,0):C.GC_5828})

V_290 = Vertex(name = 'V_290',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2806,(0,5):C.GC_2956,(0,3):C.GC_2955,(0,4):C.GC_2955,(0,1):C.GC_2725,(0,0):C.GC_5855})

V_291 = Vertex(name = 'V_291',
               particles = [ P.ve__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2807,(0,5):C.GC_2958,(0,3):C.GC_2957,(0,4):C.GC_2957,(0,1):C.GC_2726,(0,0):C.GC_5802})

V_292 = Vertex(name = 'V_292',
               particles = [ P.vm__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2808,(0,5):C.GC_2960,(0,3):C.GC_2959,(0,4):C.GC_2959,(0,1):C.GC_2727,(0,0):C.GC_5829})

V_293 = Vertex(name = 'V_293',
               particles = [ P.vt__tilde__, P.ta__minus__, P.s__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2809,(0,5):C.GC_2962,(0,3):C.GC_2961,(0,4):C.GC_2961,(0,1):C.GC_2728,(0,0):C.GC_5856})

V_294 = Vertex(name = 'V_294',
               particles = [ P.ve__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2810,(0,5):C.GC_2964,(0,3):C.GC_2963,(0,4):C.GC_2963,(0,1):C.GC_2729,(0,0):C.GC_5803})

V_295 = Vertex(name = 'V_295',
               particles = [ P.vm__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2811,(0,5):C.GC_2966,(0,3):C.GC_2965,(0,4):C.GC_2965,(0,1):C.GC_2730,(0,0):C.GC_5830})

V_296 = Vertex(name = 'V_296',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.u ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2812,(0,5):C.GC_2968,(0,3):C.GC_2967,(0,4):C.GC_2967,(0,1):C.GC_2731,(0,0):C.GC_5857})

V_297 = Vertex(name = 'V_297',
               particles = [ P.ve__tilde__, P.ta__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2813,(0,5):C.GC_2970,(0,3):C.GC_2969,(0,4):C.GC_2969,(0,1):C.GC_2732,(0,0):C.GC_5804})

V_298 = Vertex(name = 'V_298',
               particles = [ P.vm__tilde__, P.ta__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2814,(0,5):C.GC_2972,(0,3):C.GC_2971,(0,4):C.GC_2971,(0,1):C.GC_2733,(0,0):C.GC_5831})

V_299 = Vertex(name = 'V_299',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.c ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2815,(0,5):C.GC_2974,(0,3):C.GC_2973,(0,4):C.GC_2973,(0,1):C.GC_2734,(0,0):C.GC_5858})

V_300 = Vertex(name = 'V_300',
               particles = [ P.ve__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2816,(0,5):C.GC_2976,(0,3):C.GC_2975,(0,4):C.GC_2975,(0,1):C.GC_2735,(0,0):C.GC_5805})

V_301 = Vertex(name = 'V_301',
               particles = [ P.vm__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2817,(0,5):C.GC_2978,(0,3):C.GC_2977,(0,4):C.GC_2977,(0,1):C.GC_2736,(0,0):C.GC_5832})

V_302 = Vertex(name = 'V_302',
               particles = [ P.vt__tilde__, P.ta__minus__, P.b__tilde__, P.t ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF12, L.FFFF2, L.FFFF5, L.FFFF6, L.FFFF7, L.FFFF8 ],
               couplings = {(0,2):C.GC_2818,(0,5):C.GC_2980,(0,3):C.GC_2979,(0,4):C.GC_2979,(0,1):C.GC_2737,(0,0):C.GC_5859})

V_303 = Vertex(name = 'V_303',
               particles = [ P.d__tilde__, P.d, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_5356,(0,1):C.GC_1017})

V_304 = Vertex(name = 'V_304',
               particles = [ P.s__tilde__, P.d, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_5365,(0,1):C.GC_1018})

V_305 = Vertex(name = 'V_305',
               particles = [ P.b__tilde__, P.d, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_5374,(0,1):C.GC_1019})

V_306 = Vertex(name = 'V_306',
               particles = [ P.d__tilde__, P.s, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_5359,(0,1):C.GC_1020})

V_307 = Vertex(name = 'V_307',
               particles = [ P.s__tilde__, P.s, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_5368,(0,1):C.GC_1021})

V_308 = Vertex(name = 'V_308',
               particles = [ P.b__tilde__, P.s, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_5377,(0,1):C.GC_1022})

V_309 = Vertex(name = 'V_309',
               particles = [ P.d__tilde__, P.b, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_5362,(0,1):C.GC_1023})

V_310 = Vertex(name = 'V_310',
               particles = [ P.s__tilde__, P.b, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_5371,(0,1):C.GC_1024})

V_311 = Vertex(name = 'V_311',
               particles = [ P.b__tilde__, P.b, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_5380,(0,1):C.GC_1025})

V_312 = Vertex(name = 'V_312',
               particles = [ P.d__tilde__, P.d, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_5357,(0,1):C.GC_4660})

V_313 = Vertex(name = 'V_313',
               particles = [ P.s__tilde__, P.d, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_5366,(0,1):C.GC_4661})

V_314 = Vertex(name = 'V_314',
               particles = [ P.b__tilde__, P.d, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_5375,(0,1):C.GC_4662})

V_315 = Vertex(name = 'V_315',
               particles = [ P.d__tilde__, P.s, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_5360,(0,1):C.GC_4663})

V_316 = Vertex(name = 'V_316',
               particles = [ P.s__tilde__, P.s, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_5369,(0,1):C.GC_4664})

V_317 = Vertex(name = 'V_317',
               particles = [ P.b__tilde__, P.s, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_5378,(0,1):C.GC_4665})

V_318 = Vertex(name = 'V_318',
               particles = [ P.d__tilde__, P.b, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_5363,(0,1):C.GC_4666})

V_319 = Vertex(name = 'V_319',
               particles = [ P.s__tilde__, P.b, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_5372,(0,1):C.GC_4667})

V_320 = Vertex(name = 'V_320',
               particles = [ P.b__tilde__, P.b, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_5381,(0,1):C.GC_4668})

V_321 = Vertex(name = 'V_321',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
               couplings = {(0,2):C.GC_5299,(0,0):C.GC_5358,(0,1):C.GC_4930})

V_322 = Vertex(name = 'V_322',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_5300})

V_323 = Vertex(name = 'V_323',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_5301})

V_324 = Vertex(name = 'V_324',
               particles = [ P.s__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_5367,(0,1):C.GC_4931})

V_325 = Vertex(name = 'V_325',
               particles = [ P.b__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_5376,(0,1):C.GC_4932})

V_326 = Vertex(name = 'V_326',
               particles = [ P.d__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_5361,(0,1):C.GC_4933})

V_327 = Vertex(name = 'V_327',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
               couplings = {(0,2):C.GC_5308,(0,0):C.GC_5370,(0,1):C.GC_4934})

V_328 = Vertex(name = 'V_328',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_5309})

V_329 = Vertex(name = 'V_329',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_5310})

V_330 = Vertex(name = 'V_330',
               particles = [ P.b__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_5379,(0,1):C.GC_4935})

V_331 = Vertex(name = 'V_331',
               particles = [ P.d__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_5364,(0,1):C.GC_4936})

V_332 = Vertex(name = 'V_332',
               particles = [ P.s__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_5373,(0,1):C.GC_4937})

V_333 = Vertex(name = 'V_333',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
               couplings = {(0,2):C.GC_5293,(0,0):C.GC_5382,(0,1):C.GC_4938})

V_334 = Vertex(name = 'V_334',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_5294})

V_335 = Vertex(name = 'V_335',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_5295})

V_336 = Vertex(name = 'V_336',
               particles = [ P.e__plus__, P.e__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_5455,(0,1):C.GC_1116})

V_337 = Vertex(name = 'V_337',
               particles = [ P.mu__plus__, P.e__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_5464,(0,1):C.GC_1117})

V_338 = Vertex(name = 'V_338',
               particles = [ P.ta__plus__, P.e__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_5473,(0,1):C.GC_1118})

V_339 = Vertex(name = 'V_339',
               particles = [ P.e__plus__, P.mu__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_5458,(0,1):C.GC_1119})

V_340 = Vertex(name = 'V_340',
               particles = [ P.mu__plus__, P.mu__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_5467,(0,1):C.GC_1120})

V_341 = Vertex(name = 'V_341',
               particles = [ P.ta__plus__, P.mu__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_5476,(0,1):C.GC_1121})

V_342 = Vertex(name = 'V_342',
               particles = [ P.e__plus__, P.ta__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_5461,(0,1):C.GC_1122})

V_343 = Vertex(name = 'V_343',
               particles = [ P.mu__plus__, P.ta__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_5470,(0,1):C.GC_1123})

V_344 = Vertex(name = 'V_344',
               particles = [ P.ta__plus__, P.ta__minus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_5479,(0,1):C.GC_1124})

V_345 = Vertex(name = 'V_345',
               particles = [ P.e__plus__, P.e__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_5456,(0,1):C.GC_4669})

V_346 = Vertex(name = 'V_346',
               particles = [ P.mu__plus__, P.e__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_5465,(0,1):C.GC_4670})

V_347 = Vertex(name = 'V_347',
               particles = [ P.ta__plus__, P.e__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_5474,(0,1):C.GC_4671})

V_348 = Vertex(name = 'V_348',
               particles = [ P.e__plus__, P.mu__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_5459,(0,1):C.GC_4672})

V_349 = Vertex(name = 'V_349',
               particles = [ P.mu__plus__, P.mu__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_5468,(0,1):C.GC_4673})

V_350 = Vertex(name = 'V_350',
               particles = [ P.ta__plus__, P.mu__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_5477,(0,1):C.GC_4674})

V_351 = Vertex(name = 'V_351',
               particles = [ P.e__plus__, P.ta__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_5462,(0,1):C.GC_4675})

V_352 = Vertex(name = 'V_352',
               particles = [ P.mu__plus__, P.ta__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_5471,(0,1):C.GC_4676})

V_353 = Vertex(name = 'V_353',
               particles = [ P.ta__plus__, P.ta__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_5480,(0,1):C.GC_4677})

V_354 = Vertex(name = 'V_354',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
               couplings = {(0,2):C.GC_5302,(0,0):C.GC_5457,(0,1):C.GC_4939})

V_355 = Vertex(name = 'V_355',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_5303})

V_356 = Vertex(name = 'V_356',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_5304})

V_357 = Vertex(name = 'V_357',
               particles = [ P.mu__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_5466,(0,1):C.GC_4940})

V_358 = Vertex(name = 'V_358',
               particles = [ P.ta__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_5475,(0,1):C.GC_4941})

V_359 = Vertex(name = 'V_359',
               particles = [ P.e__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_5460,(0,1):C.GC_4942})

V_360 = Vertex(name = 'V_360',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
               couplings = {(0,2):C.GC_5305,(0,0):C.GC_5469,(0,1):C.GC_4943})

V_361 = Vertex(name = 'V_361',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_5306})

V_362 = Vertex(name = 'V_362',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_5307})

V_363 = Vertex(name = 'V_363',
               particles = [ P.ta__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_5478,(0,1):C.GC_4944})

V_364 = Vertex(name = 'V_364',
               particles = [ P.e__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_5463,(0,1):C.GC_4945})

V_365 = Vertex(name = 'V_365',
               particles = [ P.mu__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_5472,(0,1):C.GC_4946})

V_366 = Vertex(name = 'V_366',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
               couplings = {(0,2):C.GC_5314,(0,0):C.GC_5481,(0,1):C.GC_4947})

V_367 = Vertex(name = 'V_367',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_5315})

V_368 = Vertex(name = 'V_368',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_5316})

V_369 = Vertex(name = 'V_369',
               particles = [ P.u__tilde__, P.u, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_6139,(0,1):C.GC_2376})

V_370 = Vertex(name = 'V_370',
               particles = [ P.c__tilde__, P.u, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_6148,(0,1):C.GC_2377})

V_371 = Vertex(name = 'V_371',
               particles = [ P.t__tilde__, P.u, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_6157,(0,1):C.GC_2378})

V_372 = Vertex(name = 'V_372',
               particles = [ P.u__tilde__, P.c, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_6142,(0,1):C.GC_2379})

V_373 = Vertex(name = 'V_373',
               particles = [ P.c__tilde__, P.c, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_6151,(0,1):C.GC_2380})

V_374 = Vertex(name = 'V_374',
               particles = [ P.t__tilde__, P.c, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_6160,(0,1):C.GC_2381})

V_375 = Vertex(name = 'V_375',
               particles = [ P.u__tilde__, P.t, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_6145,(0,1):C.GC_2382})

V_376 = Vertex(name = 'V_376',
               particles = [ P.c__tilde__, P.t, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_6154,(0,1):C.GC_2383})

V_377 = Vertex(name = 'V_377',
               particles = [ P.t__tilde__, P.t, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSSS1, L.FFSSS2 ],
               couplings = {(0,0):C.GC_6163,(0,1):C.GC_2384})

V_378 = Vertex(name = 'V_378',
               particles = [ P.u__tilde__, P.u, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_6140,(0,1):C.GC_4701})

V_379 = Vertex(name = 'V_379',
               particles = [ P.c__tilde__, P.u, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_6149,(0,1):C.GC_4702})

V_380 = Vertex(name = 'V_380',
               particles = [ P.t__tilde__, P.u, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_6158,(0,1):C.GC_4703})

V_381 = Vertex(name = 'V_381',
               particles = [ P.u__tilde__, P.c, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_6143,(0,1):C.GC_4704})

V_382 = Vertex(name = 'V_382',
               particles = [ P.c__tilde__, P.c, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_6152,(0,1):C.GC_4705})

V_383 = Vertex(name = 'V_383',
               particles = [ P.t__tilde__, P.c, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_6161,(0,1):C.GC_4706})

V_384 = Vertex(name = 'V_384',
               particles = [ P.u__tilde__, P.t, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_6146,(0,1):C.GC_4707})

V_385 = Vertex(name = 'V_385',
               particles = [ P.c__tilde__, P.t, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_6155,(0,1):C.GC_4708})

V_386 = Vertex(name = 'V_386',
               particles = [ P.t__tilde__, P.t, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1, L.FFSS2 ],
               couplings = {(0,0):C.GC_6164,(0,1):C.GC_4709})

V_387 = Vertex(name = 'V_387',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
               couplings = {(0,2):C.GC_5317,(0,0):C.GC_6141,(0,1):C.GC_4948})

V_388 = Vertex(name = 'V_388',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_5318})

V_389 = Vertex(name = 'V_389',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_5319})

V_390 = Vertex(name = 'V_390',
               particles = [ P.c__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_6150,(0,1):C.GC_4949})

V_391 = Vertex(name = 'V_391',
               particles = [ P.t__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_6159,(0,1):C.GC_4950})

V_392 = Vertex(name = 'V_392',
               particles = [ P.u__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_6144,(0,1):C.GC_4951})

V_393 = Vertex(name = 'V_393',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
               couplings = {(0,2):C.GC_5296,(0,0):C.GC_6153,(0,1):C.GC_4952})

V_394 = Vertex(name = 'V_394',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_5297})

V_395 = Vertex(name = 'V_395',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_5298})

V_396 = Vertex(name = 'V_396',
               particles = [ P.t__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_6162,(0,1):C.GC_4953})

V_397 = Vertex(name = 'V_397',
               particles = [ P.u__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_6147,(0,1):C.GC_4954})

V_398 = Vertex(name = 'V_398',
               particles = [ P.c__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_6156,(0,1):C.GC_4955})

V_399 = Vertex(name = 'V_399',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
               couplings = {(0,2):C.GC_5311,(0,0):C.GC_6165,(0,1):C.GC_4956})

V_400 = Vertex(name = 'V_400',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_5312})

V_401 = Vertex(name = 'V_401',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3 ],
               couplings = {(0,0):C.GC_5313})

V_402 = Vertex(name = 'V_402',
               particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_470,(0,2):C.GC_3226,(0,3):C.GC_1222,(0,4):C.GC_1026,(0,0):C.GC_3143,(0,1):C.GC_3062})

V_403 = Vertex(name = 'V_403',
               particles = [ P.mu__plus__, P.e__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_472,(0,2):C.GC_3227,(0,3):C.GC_1231,(0,4):C.GC_1035,(0,0):C.GC_3144,(0,1):C.GC_3063})

V_404 = Vertex(name = 'V_404',
               particles = [ P.ta__plus__, P.e__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_474,(0,2):C.GC_3228,(0,3):C.GC_1240,(0,4):C.GC_1044,(0,0):C.GC_3145,(0,1):C.GC_3064})

V_405 = Vertex(name = 'V_405',
               particles = [ P.e__plus__, P.mu__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_476,(0,2):C.GC_3229,(0,3):C.GC_1249,(0,4):C.GC_1053,(0,0):C.GC_3146,(0,1):C.GC_3065})

V_406 = Vertex(name = 'V_406',
               particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_478,(0,2):C.GC_3230,(0,3):C.GC_1258,(0,4):C.GC_1062,(0,0):C.GC_3147,(0,1):C.GC_3066})

V_407 = Vertex(name = 'V_407',
               particles = [ P.ta__plus__, P.mu__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_479,(0,2):C.GC_3231,(0,3):C.GC_1267,(0,4):C.GC_1071,(0,0):C.GC_3148,(0,1):C.GC_3067})

V_408 = Vertex(name = 'V_408',
               particles = [ P.e__plus__, P.ta__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_481,(0,2):C.GC_3232,(0,3):C.GC_1276,(0,4):C.GC_1080,(0,0):C.GC_3149,(0,1):C.GC_3068})

V_409 = Vertex(name = 'V_409',
               particles = [ P.mu__plus__, P.ta__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_483,(0,2):C.GC_3233,(0,3):C.GC_1285,(0,4):C.GC_1089,(0,0):C.GC_3150,(0,1):C.GC_3069})

V_410 = Vertex(name = 'V_410',
               particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_485,(0,2):C.GC_3234,(0,3):C.GC_1294,(0,4):C.GC_1098,(0,0):C.GC_3151,(0,1):C.GC_3070})

V_411 = Vertex(name = 'V_411',
               particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_487,(0,2):C.GC_3235,(0,3):C.GC_1223,(0,4):C.GC_1027,(0,0):C.GC_3152,(0,1):C.GC_3071})

V_412 = Vertex(name = 'V_412',
               particles = [ P.mu__plus__, P.e__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_489,(0,2):C.GC_3236,(0,3):C.GC_1232,(0,4):C.GC_1036,(0,0):C.GC_3153,(0,1):C.GC_3072})

V_413 = Vertex(name = 'V_413',
               particles = [ P.ta__plus__, P.e__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_491,(0,2):C.GC_3237,(0,3):C.GC_1241,(0,4):C.GC_1045,(0,0):C.GC_3154,(0,1):C.GC_3073})

V_414 = Vertex(name = 'V_414',
               particles = [ P.e__plus__, P.mu__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_493,(0,2):C.GC_3238,(0,3):C.GC_1250,(0,4):C.GC_1054,(0,0):C.GC_3155,(0,1):C.GC_3074})

V_415 = Vertex(name = 'V_415',
               particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_495,(0,2):C.GC_3239,(0,3):C.GC_1259,(0,4):C.GC_1063,(0,0):C.GC_3156,(0,1):C.GC_3075})

V_416 = Vertex(name = 'V_416',
               particles = [ P.ta__plus__, P.mu__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_497,(0,2):C.GC_3240,(0,3):C.GC_1268,(0,4):C.GC_1072,(0,0):C.GC_3157,(0,1):C.GC_3076})

V_417 = Vertex(name = 'V_417',
               particles = [ P.e__plus__, P.ta__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_499,(0,2):C.GC_3241,(0,3):C.GC_1277,(0,4):C.GC_1081,(0,0):C.GC_3158,(0,1):C.GC_3077})

V_418 = Vertex(name = 'V_418',
               particles = [ P.mu__plus__, P.ta__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_501,(0,2):C.GC_3242,(0,3):C.GC_1286,(0,4):C.GC_1090,(0,0):C.GC_3159,(0,1):C.GC_3078})

V_419 = Vertex(name = 'V_419',
               particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_503,(0,2):C.GC_3243,(0,3):C.GC_1295,(0,4):C.GC_1099,(0,0):C.GC_3160,(0,1):C.GC_3079})

V_420 = Vertex(name = 'V_420',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_505,(0,2):C.GC_3244,(0,3):C.GC_1224,(0,4):C.GC_1028,(0,0):C.GC_3161,(0,1):C.GC_3080})

V_421 = Vertex(name = 'V_421',
               particles = [ P.mu__plus__, P.e__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_507,(0,2):C.GC_3245,(0,3):C.GC_1233,(0,4):C.GC_1037,(0,0):C.GC_3162,(0,1):C.GC_3081})

V_422 = Vertex(name = 'V_422',
               particles = [ P.ta__plus__, P.e__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_509,(0,2):C.GC_3246,(0,3):C.GC_1242,(0,4):C.GC_1046,(0,0):C.GC_3163,(0,1):C.GC_3082})

V_423 = Vertex(name = 'V_423',
               particles = [ P.e__plus__, P.mu__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_511,(0,2):C.GC_3247,(0,3):C.GC_1251,(0,4):C.GC_1055,(0,0):C.GC_3164,(0,1):C.GC_3083})

V_424 = Vertex(name = 'V_424',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_513,(0,2):C.GC_3248,(0,3):C.GC_1260,(0,4):C.GC_1064,(0,0):C.GC_3165,(0,1):C.GC_3084})

V_425 = Vertex(name = 'V_425',
               particles = [ P.ta__plus__, P.mu__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_515,(0,2):C.GC_3249,(0,3):C.GC_1269,(0,4):C.GC_1073,(0,0):C.GC_3166,(0,1):C.GC_3085})

V_426 = Vertex(name = 'V_426',
               particles = [ P.e__plus__, P.ta__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_517,(0,2):C.GC_3250,(0,3):C.GC_1278,(0,4):C.GC_1082,(0,0):C.GC_3167,(0,1):C.GC_3086})

V_427 = Vertex(name = 'V_427',
               particles = [ P.mu__plus__, P.ta__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_519,(0,2):C.GC_3251,(0,3):C.GC_1287,(0,4):C.GC_1091,(0,0):C.GC_3168,(0,1):C.GC_3087})

V_428 = Vertex(name = 'V_428',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.d ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_521,(0,2):C.GC_3252,(0,3):C.GC_1296,(0,4):C.GC_1100,(0,0):C.GC_3169,(0,1):C.GC_3088})

V_429 = Vertex(name = 'V_429',
               particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_523,(0,2):C.GC_3253,(0,3):C.GC_1225,(0,4):C.GC_1029,(0,0):C.GC_3170,(0,1):C.GC_3089})

V_430 = Vertex(name = 'V_430',
               particles = [ P.mu__plus__, P.e__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_525,(0,2):C.GC_3254,(0,3):C.GC_1234,(0,4):C.GC_1038,(0,0):C.GC_3171,(0,1):C.GC_3090})

V_431 = Vertex(name = 'V_431',
               particles = [ P.ta__plus__, P.e__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_527,(0,2):C.GC_3255,(0,3):C.GC_1243,(0,4):C.GC_1047,(0,0):C.GC_3172,(0,1):C.GC_3091})

V_432 = Vertex(name = 'V_432',
               particles = [ P.e__plus__, P.mu__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_529,(0,2):C.GC_1252,(0,4):C.GC_1056,(0,3):C.GC_3256,(0,0):C.GC_3173,(0,1):C.GC_3092})

V_433 = Vertex(name = 'V_433',
               particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_531,(0,2):C.GC_3257,(0,3):C.GC_1261,(0,4):C.GC_1065,(0,0):C.GC_3174,(0,1):C.GC_3093})

V_434 = Vertex(name = 'V_434',
               particles = [ P.ta__plus__, P.mu__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_533,(0,2):C.GC_3258,(0,3):C.GC_1270,(0,4):C.GC_1074,(0,0):C.GC_3175,(0,1):C.GC_3094})

V_435 = Vertex(name = 'V_435',
               particles = [ P.e__plus__, P.ta__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_535,(0,2):C.GC_3259,(0,3):C.GC_1279,(0,4):C.GC_1083,(0,0):C.GC_3176,(0,1):C.GC_3095})

V_436 = Vertex(name = 'V_436',
               particles = [ P.mu__plus__, P.ta__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_537,(0,2):C.GC_3260,(0,3):C.GC_1288,(0,4):C.GC_1092,(0,0):C.GC_3177,(0,1):C.GC_3096})

V_437 = Vertex(name = 'V_437',
               particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_539,(0,2):C.GC_3261,(0,3):C.GC_1297,(0,4):C.GC_1101,(0,0):C.GC_3178,(0,1):C.GC_3097})

V_438 = Vertex(name = 'V_438',
               particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_541,(0,2):C.GC_3262,(0,3):C.GC_1226,(0,4):C.GC_1030,(0,0):C.GC_3179,(0,1):C.GC_3098})

V_439 = Vertex(name = 'V_439',
               particles = [ P.mu__plus__, P.e__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_543,(0,2):C.GC_3263,(0,3):C.GC_1235,(0,4):C.GC_1039,(0,0):C.GC_3180,(0,1):C.GC_3099})

V_440 = Vertex(name = 'V_440',
               particles = [ P.ta__plus__, P.e__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_545,(0,2):C.GC_3264,(0,3):C.GC_1244,(0,4):C.GC_1048,(0,0):C.GC_3181,(0,1):C.GC_3100})

V_441 = Vertex(name = 'V_441',
               particles = [ P.e__plus__, P.mu__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF14, L.FFFF15, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_547,(0,2):C.GC_1253,(0,4):C.GC_1057,(0,3):C.GC_3265,(0,0):C.GC_3182,(0,1):C.GC_3101})

V_442 = Vertex(name = 'V_442',
               particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_549,(0,2):C.GC_3266,(0,3):C.GC_1262,(0,4):C.GC_1066,(0,0):C.GC_3183,(0,1):C.GC_3102})

V_443 = Vertex(name = 'V_443',
               particles = [ P.ta__plus__, P.mu__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_551,(0,2):C.GC_3267,(0,3):C.GC_1271,(0,4):C.GC_1075,(0,0):C.GC_3184,(0,1):C.GC_3103})

V_444 = Vertex(name = 'V_444',
               particles = [ P.e__plus__, P.ta__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_553,(0,2):C.GC_3268,(0,3):C.GC_1280,(0,4):C.GC_1084,(0,0):C.GC_3185,(0,1):C.GC_3104})

V_445 = Vertex(name = 'V_445',
               particles = [ P.mu__plus__, P.ta__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_555,(0,2):C.GC_3269,(0,3):C.GC_1289,(0,4):C.GC_1093,(0,0):C.GC_3186,(0,1):C.GC_3105})

V_446 = Vertex(name = 'V_446',
               particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_557,(0,2):C.GC_3270,(0,3):C.GC_1298,(0,4):C.GC_1102,(0,0):C.GC_3187,(0,1):C.GC_3106})

V_447 = Vertex(name = 'V_447',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_559,(0,2):C.GC_3271,(0,3):C.GC_1227,(0,4):C.GC_1031,(0,0):C.GC_3188,(0,1):C.GC_3107})

V_448 = Vertex(name = 'V_448',
               particles = [ P.mu__plus__, P.e__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_561,(0,2):C.GC_3272,(0,3):C.GC_1236,(0,4):C.GC_1040,(0,0):C.GC_3189,(0,1):C.GC_3108})

V_449 = Vertex(name = 'V_449',
               particles = [ P.ta__plus__, P.e__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_563,(0,2):C.GC_3273,(0,3):C.GC_1245,(0,4):C.GC_1049,(0,0):C.GC_3190,(0,1):C.GC_3109})

V_450 = Vertex(name = 'V_450',
               particles = [ P.e__plus__, P.mu__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_565,(0,2):C.GC_3274,(0,3):C.GC_1254,(0,4):C.GC_1058,(0,0):C.GC_3191,(0,1):C.GC_3110})

V_451 = Vertex(name = 'V_451',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_567,(0,2):C.GC_3275,(0,3):C.GC_1263,(0,4):C.GC_1067,(0,0):C.GC_3192,(0,1):C.GC_3111})

V_452 = Vertex(name = 'V_452',
               particles = [ P.ta__plus__, P.mu__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_569,(0,2):C.GC_3276,(0,3):C.GC_1272,(0,4):C.GC_1076,(0,0):C.GC_3193,(0,1):C.GC_3112})

V_453 = Vertex(name = 'V_453',
               particles = [ P.e__plus__, P.ta__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_571,(0,2):C.GC_3277,(0,3):C.GC_1281,(0,4):C.GC_1085,(0,0):C.GC_3194,(0,1):C.GC_3113})

V_454 = Vertex(name = 'V_454',
               particles = [ P.mu__plus__, P.ta__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_573,(0,2):C.GC_3278,(0,3):C.GC_1290,(0,4):C.GC_1094,(0,0):C.GC_3195,(0,1):C.GC_3114})

V_455 = Vertex(name = 'V_455',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.s ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_575,(0,2):C.GC_3279,(0,3):C.GC_1299,(0,4):C.GC_1103,(0,0):C.GC_3196,(0,1):C.GC_3115})

V_456 = Vertex(name = 'V_456',
               particles = [ P.e__plus__, P.e__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_577,(0,2):C.GC_3280,(0,3):C.GC_1228,(0,4):C.GC_1032,(0,0):C.GC_3197,(0,1):C.GC_3116})

V_457 = Vertex(name = 'V_457',
               particles = [ P.mu__plus__, P.e__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_579,(0,2):C.GC_3281,(0,3):C.GC_1237,(0,4):C.GC_1041,(0,0):C.GC_3198,(0,1):C.GC_3117})

V_458 = Vertex(name = 'V_458',
               particles = [ P.ta__plus__, P.e__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_581,(0,2):C.GC_3282,(0,3):C.GC_1246,(0,4):C.GC_1050,(0,0):C.GC_3199,(0,1):C.GC_3118})

V_459 = Vertex(name = 'V_459',
               particles = [ P.e__plus__, P.mu__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_583,(0,2):C.GC_3283,(0,3):C.GC_1255,(0,4):C.GC_1059,(0,0):C.GC_3200,(0,1):C.GC_3119})

V_460 = Vertex(name = 'V_460',
               particles = [ P.mu__plus__, P.mu__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_585,(0,2):C.GC_3284,(0,3):C.GC_1264,(0,4):C.GC_1068,(0,0):C.GC_3201,(0,1):C.GC_3120})

V_461 = Vertex(name = 'V_461',
               particles = [ P.ta__plus__, P.mu__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_587,(0,2):C.GC_3285,(0,3):C.GC_1273,(0,4):C.GC_1077,(0,0):C.GC_3202,(0,1):C.GC_3121})

V_462 = Vertex(name = 'V_462',
               particles = [ P.e__plus__, P.ta__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_589,(0,2):C.GC_3286,(0,3):C.GC_1282,(0,4):C.GC_1086,(0,0):C.GC_3203,(0,1):C.GC_3122})

V_463 = Vertex(name = 'V_463',
               particles = [ P.mu__plus__, P.ta__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_591,(0,2):C.GC_3287,(0,3):C.GC_1291,(0,4):C.GC_1095,(0,0):C.GC_3204,(0,1):C.GC_3123})

V_464 = Vertex(name = 'V_464',
               particles = [ P.ta__plus__, P.ta__minus__, P.d__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_593,(0,2):C.GC_3288,(0,3):C.GC_1300,(0,4):C.GC_1104,(0,0):C.GC_3205,(0,1):C.GC_3124})

V_465 = Vertex(name = 'V_465',
               particles = [ P.e__plus__, P.e__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_595,(0,2):C.GC_3289,(0,3):C.GC_1229,(0,4):C.GC_1033,(0,0):C.GC_3206,(0,1):C.GC_3125})

V_466 = Vertex(name = 'V_466',
               particles = [ P.mu__plus__, P.e__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_597,(0,2):C.GC_3290,(0,3):C.GC_1238,(0,4):C.GC_1042,(0,0):C.GC_3207,(0,1):C.GC_3126})

V_467 = Vertex(name = 'V_467',
               particles = [ P.ta__plus__, P.e__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_599,(0,2):C.GC_3291,(0,3):C.GC_1247,(0,4):C.GC_1051,(0,0):C.GC_3208,(0,1):C.GC_3127})

V_468 = Vertex(name = 'V_468',
               particles = [ P.e__plus__, P.mu__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_601,(0,2):C.GC_3292,(0,3):C.GC_1256,(0,4):C.GC_1060,(0,0):C.GC_3209,(0,1):C.GC_3128})

V_469 = Vertex(name = 'V_469',
               particles = [ P.mu__plus__, P.mu__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_603,(0,2):C.GC_3293,(0,3):C.GC_1265,(0,4):C.GC_1069,(0,0):C.GC_3210,(0,1):C.GC_3129})

V_470 = Vertex(name = 'V_470',
               particles = [ P.ta__plus__, P.mu__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_605,(0,2):C.GC_3294,(0,3):C.GC_1274,(0,4):C.GC_1078,(0,0):C.GC_3211,(0,1):C.GC_3130})

V_471 = Vertex(name = 'V_471',
               particles = [ P.e__plus__, P.ta__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_607,(0,2):C.GC_3295,(0,3):C.GC_1283,(0,4):C.GC_1087,(0,0):C.GC_3212,(0,1):C.GC_3131})

V_472 = Vertex(name = 'V_472',
               particles = [ P.mu__plus__, P.ta__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_609,(0,2):C.GC_3296,(0,3):C.GC_1292,(0,4):C.GC_1096,(0,0):C.GC_3213,(0,1):C.GC_3132})

V_473 = Vertex(name = 'V_473',
               particles = [ P.ta__plus__, P.ta__minus__, P.s__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_611,(0,2):C.GC_3297,(0,3):C.GC_1301,(0,4):C.GC_1105,(0,0):C.GC_3214,(0,1):C.GC_3133})

V_474 = Vertex(name = 'V_474',
               particles = [ P.e__plus__, P.e__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_613,(0,2):C.GC_3298,(0,3):C.GC_1230,(0,4):C.GC_1034,(0,0):C.GC_3215,(0,1):C.GC_3134})

V_475 = Vertex(name = 'V_475',
               particles = [ P.mu__plus__, P.e__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_615,(0,2):C.GC_3299,(0,3):C.GC_1239,(0,4):C.GC_1043,(0,0):C.GC_3216,(0,1):C.GC_3135})

V_476 = Vertex(name = 'V_476',
               particles = [ P.ta__plus__, P.e__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_617,(0,2):C.GC_3300,(0,3):C.GC_1248,(0,4):C.GC_1052,(0,0):C.GC_3217,(0,1):C.GC_3136})

V_477 = Vertex(name = 'V_477',
               particles = [ P.e__plus__, P.mu__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_619,(0,2):C.GC_3301,(0,3):C.GC_1257,(0,4):C.GC_1061,(0,0):C.GC_3218,(0,1):C.GC_3137})

V_478 = Vertex(name = 'V_478',
               particles = [ P.mu__plus__, P.mu__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_621,(0,2):C.GC_3302,(0,3):C.GC_1266,(0,4):C.GC_1070,(0,0):C.GC_3219,(0,1):C.GC_3138})

V_479 = Vertex(name = 'V_479',
               particles = [ P.ta__plus__, P.mu__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_623,(0,2):C.GC_3303,(0,3):C.GC_1275,(0,4):C.GC_1079,(0,0):C.GC_3220,(0,1):C.GC_3139})

V_480 = Vertex(name = 'V_480',
               particles = [ P.e__plus__, P.ta__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_625,(0,2):C.GC_3304,(0,3):C.GC_1284,(0,4):C.GC_1088,(0,0):C.GC_3221,(0,1):C.GC_3140})

V_481 = Vertex(name = 'V_481',
               particles = [ P.mu__plus__, P.ta__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_627,(0,2):C.GC_3305,(0,3):C.GC_1293,(0,4):C.GC_1097,(0,0):C.GC_3222,(0,1):C.GC_3141})

V_482 = Vertex(name = 'V_482',
               particles = [ P.ta__plus__, P.ta__minus__, P.b__tilde__, P.b ],
               color = [ 'Identity(3,4)' ],
               lorentz = [ L.FFFF10, L.FFFF12, L.FFFF15, L.FFFF19, L.FFFF20, L.FFFF5 ],
               couplings = {(0,5):C.GC_629,(0,2):C.GC_3306,(0,3):C.GC_1302,(0,4):C.GC_1106,(0,0):C.GC_3223,(0,1):C.GC_3142})

V_483 = Vertex(name = 'V_483',
               particles = [ P.u__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3388,(0,4):C.GC_3470,(0,2):C.GC_3469,(0,3):C.GC_3469,(0,0):C.GC_1384,(0,1):C.GC_3307})

V_484 = Vertex(name = 'V_484',
               particles = [ P.c__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3389,(0,4):C.GC_3472,(0,2):C.GC_3471,(0,3):C.GC_3471,(0,0):C.GC_1385,(0,1):C.GC_3308})

V_485 = Vertex(name = 'V_485',
               particles = [ P.t__tilde__, P.d, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3390,(0,4):C.GC_3474,(0,2):C.GC_3473,(0,3):C.GC_3473,(0,0):C.GC_1386,(0,1):C.GC_3309})

V_486 = Vertex(name = 'V_486',
               particles = [ P.u__tilde__, P.d, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3391,(0,4):C.GC_3476,(0,2):C.GC_3475,(0,3):C.GC_3475,(0,0):C.GC_1411,(0,1):C.GC_3310})

V_487 = Vertex(name = 'V_487',
               particles = [ P.c__tilde__, P.d, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3392,(0,4):C.GC_3478,(0,2):C.GC_3477,(0,3):C.GC_3477,(0,0):C.GC_1412,(0,1):C.GC_3311})

V_488 = Vertex(name = 'V_488',
               particles = [ P.t__tilde__, P.d, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3393,(0,4):C.GC_3480,(0,2):C.GC_3479,(0,3):C.GC_3479,(0,0):C.GC_1413,(0,1):C.GC_3312})

V_489 = Vertex(name = 'V_489',
               particles = [ P.u__tilde__, P.d, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3394,(0,4):C.GC_3482,(0,2):C.GC_3481,(0,3):C.GC_3481,(0,0):C.GC_1438,(0,1):C.GC_3313})

V_490 = Vertex(name = 'V_490',
               particles = [ P.c__tilde__, P.d, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3395,(0,4):C.GC_3484,(0,2):C.GC_3483,(0,3):C.GC_3483,(0,0):C.GC_1439,(0,1):C.GC_3314})

V_491 = Vertex(name = 'V_491',
               particles = [ P.t__tilde__, P.d, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3396,(0,4):C.GC_3486,(0,2):C.GC_3485,(0,3):C.GC_3485,(0,0):C.GC_1440,(0,1):C.GC_3315})

V_492 = Vertex(name = 'V_492',
               particles = [ P.u__tilde__, P.d, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3397,(0,4):C.GC_3488,(0,2):C.GC_3487,(0,3):C.GC_3487,(0,0):C.GC_1393,(0,1):C.GC_3316})

V_493 = Vertex(name = 'V_493',
               particles = [ P.c__tilde__, P.d, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3398,(0,4):C.GC_3490,(0,2):C.GC_3489,(0,3):C.GC_3489,(0,0):C.GC_1394,(0,1):C.GC_3317})

V_494 = Vertex(name = 'V_494',
               particles = [ P.t__tilde__, P.d, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3399,(0,4):C.GC_3492,(0,2):C.GC_3491,(0,3):C.GC_3491,(0,0):C.GC_1395,(0,1):C.GC_3318})

V_495 = Vertex(name = 'V_495',
               particles = [ P.u__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3400,(0,4):C.GC_3494,(0,2):C.GC_3493,(0,3):C.GC_3493,(0,0):C.GC_1420,(0,1):C.GC_3319})

V_496 = Vertex(name = 'V_496',
               particles = [ P.c__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3401,(0,4):C.GC_3496,(0,2):C.GC_3495,(0,3):C.GC_3495,(0,0):C.GC_1421,(0,1):C.GC_3320})

V_497 = Vertex(name = 'V_497',
               particles = [ P.t__tilde__, P.d, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3402,(0,4):C.GC_3498,(0,2):C.GC_3497,(0,3):C.GC_3497,(0,0):C.GC_1422,(0,1):C.GC_3321})

V_498 = Vertex(name = 'V_498',
               particles = [ P.u__tilde__, P.d, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3403,(0,4):C.GC_3500,(0,2):C.GC_3499,(0,3):C.GC_3499,(0,0):C.GC_1447,(0,1):C.GC_3322})

V_499 = Vertex(name = 'V_499',
               particles = [ P.c__tilde__, P.d, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3404,(0,4):C.GC_3502,(0,2):C.GC_3501,(0,3):C.GC_3501,(0,0):C.GC_1448,(0,1):C.GC_3323})

V_500 = Vertex(name = 'V_500',
               particles = [ P.t__tilde__, P.d, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3405,(0,4):C.GC_3504,(0,2):C.GC_3503,(0,3):C.GC_3503,(0,0):C.GC_1449,(0,1):C.GC_3324})

V_501 = Vertex(name = 'V_501',
               particles = [ P.u__tilde__, P.d, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3406,(0,4):C.GC_3506,(0,2):C.GC_3505,(0,3):C.GC_3505,(0,0):C.GC_1402,(0,1):C.GC_3325})

V_502 = Vertex(name = 'V_502',
               particles = [ P.c__tilde__, P.d, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3407,(0,4):C.GC_3508,(0,2):C.GC_3507,(0,3):C.GC_3507,(0,0):C.GC_1403,(0,1):C.GC_3326})

V_503 = Vertex(name = 'V_503',
               particles = [ P.t__tilde__, P.d, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3408,(0,4):C.GC_3510,(0,2):C.GC_3509,(0,3):C.GC_3509,(0,0):C.GC_1404,(0,1):C.GC_3327})

V_504 = Vertex(name = 'V_504',
               particles = [ P.u__tilde__, P.d, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3409,(0,4):C.GC_3512,(0,2):C.GC_3511,(0,3):C.GC_3511,(0,0):C.GC_1429,(0,1):C.GC_3328})

V_505 = Vertex(name = 'V_505',
               particles = [ P.c__tilde__, P.d, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3410,(0,4):C.GC_3514,(0,2):C.GC_3513,(0,3):C.GC_3513,(0,0):C.GC_1430,(0,1):C.GC_3329})

V_506 = Vertex(name = 'V_506',
               particles = [ P.t__tilde__, P.d, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3411,(0,4):C.GC_3516,(0,2):C.GC_3515,(0,3):C.GC_3515,(0,0):C.GC_1431,(0,1):C.GC_3330})

V_507 = Vertex(name = 'V_507',
               particles = [ P.u__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3412,(0,4):C.GC_3518,(0,2):C.GC_3517,(0,3):C.GC_3517,(0,0):C.GC_1456,(0,1):C.GC_3331})

V_508 = Vertex(name = 'V_508',
               particles = [ P.c__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3413,(0,4):C.GC_3520,(0,2):C.GC_3519,(0,3):C.GC_3519,(0,0):C.GC_1457,(0,1):C.GC_3332})

V_509 = Vertex(name = 'V_509',
               particles = [ P.t__tilde__, P.d, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3414,(0,4):C.GC_3522,(0,2):C.GC_3521,(0,3):C.GC_3521,(0,0):C.GC_1458,(0,1):C.GC_3333})

V_510 = Vertex(name = 'V_510',
               particles = [ P.u__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3415,(0,4):C.GC_3524,(0,2):C.GC_3523,(0,3):C.GC_3523,(0,0):C.GC_1387,(0,1):C.GC_3334})

V_511 = Vertex(name = 'V_511',
               particles = [ P.c__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3416,(0,4):C.GC_3526,(0,2):C.GC_3525,(0,3):C.GC_3525,(0,0):C.GC_1388,(0,1):C.GC_3335})

V_512 = Vertex(name = 'V_512',
               particles = [ P.t__tilde__, P.s, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3417,(0,4):C.GC_3528,(0,2):C.GC_3527,(0,3):C.GC_3527,(0,0):C.GC_1389,(0,1):C.GC_3336})

V_513 = Vertex(name = 'V_513',
               particles = [ P.u__tilde__, P.s, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3418,(0,4):C.GC_3530,(0,2):C.GC_3529,(0,3):C.GC_3529,(0,0):C.GC_1414,(0,1):C.GC_3337})

V_514 = Vertex(name = 'V_514',
               particles = [ P.c__tilde__, P.s, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3419,(0,4):C.GC_3532,(0,2):C.GC_3531,(0,3):C.GC_3531,(0,0):C.GC_1415,(0,1):C.GC_3338})

V_515 = Vertex(name = 'V_515',
               particles = [ P.t__tilde__, P.s, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3420,(0,4):C.GC_3534,(0,2):C.GC_3533,(0,3):C.GC_3533,(0,0):C.GC_1416,(0,1):C.GC_3339})

V_516 = Vertex(name = 'V_516',
               particles = [ P.u__tilde__, P.s, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3421,(0,4):C.GC_3536,(0,2):C.GC_3535,(0,3):C.GC_3535,(0,0):C.GC_1441,(0,1):C.GC_3340})

V_517 = Vertex(name = 'V_517',
               particles = [ P.c__tilde__, P.s, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF23, L.FFFF24, L.FFFF5 ],
               couplings = {(0,5):C.GC_3422,(0,3):C.GC_3538,(0,2):C.GC_3537,(0,4):C.GC_3537,(0,0):C.GC_1442,(0,1):C.GC_3341})

V_518 = Vertex(name = 'V_518',
               particles = [ P.t__tilde__, P.s, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3423,(0,4):C.GC_3540,(0,2):C.GC_3539,(0,3):C.GC_3539,(0,0):C.GC_1443,(0,1):C.GC_3342})

V_519 = Vertex(name = 'V_519',
               particles = [ P.u__tilde__, P.s, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3424,(0,4):C.GC_3542,(0,2):C.GC_3541,(0,3):C.GC_3541,(0,0):C.GC_1396,(0,1):C.GC_3343})

V_520 = Vertex(name = 'V_520',
               particles = [ P.c__tilde__, P.s, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3425,(0,4):C.GC_3544,(0,2):C.GC_3543,(0,3):C.GC_3543,(0,0):C.GC_1397,(0,1):C.GC_3344})

V_521 = Vertex(name = 'V_521',
               particles = [ P.t__tilde__, P.s, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3426,(0,4):C.GC_3546,(0,2):C.GC_3545,(0,3):C.GC_3545,(0,0):C.GC_1398,(0,1):C.GC_3345})

V_522 = Vertex(name = 'V_522',
               particles = [ P.u__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3427,(0,4):C.GC_3548,(0,2):C.GC_3547,(0,3):C.GC_3547,(0,0):C.GC_1423,(0,1):C.GC_3346})

V_523 = Vertex(name = 'V_523',
               particles = [ P.c__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3428,(0,4):C.GC_3550,(0,2):C.GC_3549,(0,3):C.GC_3549,(0,0):C.GC_1424,(0,1):C.GC_3347})

V_524 = Vertex(name = 'V_524',
               particles = [ P.t__tilde__, P.s, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3429,(0,4):C.GC_3552,(0,2):C.GC_3551,(0,3):C.GC_3551,(0,0):C.GC_1425,(0,1):C.GC_3348})

V_525 = Vertex(name = 'V_525',
               particles = [ P.u__tilde__, P.s, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3430,(0,4):C.GC_3554,(0,2):C.GC_3553,(0,3):C.GC_3553,(0,0):C.GC_1450,(0,1):C.GC_3349})

V_526 = Vertex(name = 'V_526',
               particles = [ P.c__tilde__, P.s, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3431,(0,4):C.GC_3556,(0,2):C.GC_3555,(0,3):C.GC_3555,(0,0):C.GC_1451,(0,1):C.GC_3350})

V_527 = Vertex(name = 'V_527',
               particles = [ P.t__tilde__, P.s, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3432,(0,4):C.GC_3558,(0,2):C.GC_3557,(0,3):C.GC_3557,(0,0):C.GC_1452,(0,1):C.GC_3351})

V_528 = Vertex(name = 'V_528',
               particles = [ P.u__tilde__, P.s, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3433,(0,4):C.GC_3560,(0,2):C.GC_3559,(0,3):C.GC_3559,(0,0):C.GC_1405,(0,1):C.GC_3352})

V_529 = Vertex(name = 'V_529',
               particles = [ P.c__tilde__, P.s, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3434,(0,4):C.GC_3562,(0,2):C.GC_3561,(0,3):C.GC_3561,(0,0):C.GC_1406,(0,1):C.GC_3353})

V_530 = Vertex(name = 'V_530',
               particles = [ P.t__tilde__, P.s, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3435,(0,4):C.GC_3564,(0,2):C.GC_3563,(0,3):C.GC_3563,(0,0):C.GC_1407,(0,1):C.GC_3354})

V_531 = Vertex(name = 'V_531',
               particles = [ P.u__tilde__, P.s, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3436,(0,4):C.GC_3566,(0,2):C.GC_3565,(0,3):C.GC_3565,(0,0):C.GC_1432,(0,1):C.GC_3355})

V_532 = Vertex(name = 'V_532',
               particles = [ P.c__tilde__, P.s, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3437,(0,4):C.GC_3568,(0,2):C.GC_3567,(0,3):C.GC_3567,(0,0):C.GC_1433,(0,1):C.GC_3356})

V_533 = Vertex(name = 'V_533',
               particles = [ P.t__tilde__, P.s, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3438,(0,4):C.GC_3570,(0,2):C.GC_3569,(0,3):C.GC_3569,(0,0):C.GC_1434,(0,1):C.GC_3357})

V_534 = Vertex(name = 'V_534',
               particles = [ P.u__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3439,(0,4):C.GC_3572,(0,2):C.GC_3571,(0,3):C.GC_3571,(0,0):C.GC_1459,(0,1):C.GC_3358})

V_535 = Vertex(name = 'V_535',
               particles = [ P.c__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3440,(0,4):C.GC_3574,(0,2):C.GC_3573,(0,3):C.GC_3573,(0,0):C.GC_1460,(0,1):C.GC_3359})

V_536 = Vertex(name = 'V_536',
               particles = [ P.t__tilde__, P.s, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3441,(0,4):C.GC_3576,(0,2):C.GC_3575,(0,3):C.GC_3575,(0,0):C.GC_1461,(0,1):C.GC_3360})

V_537 = Vertex(name = 'V_537',
               particles = [ P.u__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3442,(0,4):C.GC_3578,(0,2):C.GC_3577,(0,3):C.GC_3577,(0,0):C.GC_1390,(0,1):C.GC_3361})

V_538 = Vertex(name = 'V_538',
               particles = [ P.c__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3443,(0,4):C.GC_3580,(0,2):C.GC_3579,(0,3):C.GC_3579,(0,0):C.GC_1391,(0,1):C.GC_3362})

V_539 = Vertex(name = 'V_539',
               particles = [ P.t__tilde__, P.b, P.e__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3444,(0,4):C.GC_3582,(0,2):C.GC_3581,(0,3):C.GC_3581,(0,0):C.GC_1392,(0,1):C.GC_3363})

V_540 = Vertex(name = 'V_540',
               particles = [ P.u__tilde__, P.b, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3445,(0,4):C.GC_3584,(0,2):C.GC_3583,(0,3):C.GC_3583,(0,0):C.GC_1417,(0,1):C.GC_3364})

V_541 = Vertex(name = 'V_541',
               particles = [ P.c__tilde__, P.b, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3446,(0,4):C.GC_3586,(0,2):C.GC_3585,(0,3):C.GC_3585,(0,0):C.GC_1418,(0,1):C.GC_3365})

V_542 = Vertex(name = 'V_542',
               particles = [ P.t__tilde__, P.b, P.e__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3447,(0,4):C.GC_3588,(0,2):C.GC_3587,(0,3):C.GC_3587,(0,0):C.GC_1419,(0,1):C.GC_3366})

V_543 = Vertex(name = 'V_543',
               particles = [ P.u__tilde__, P.b, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3448,(0,4):C.GC_3590,(0,2):C.GC_3589,(0,3):C.GC_3589,(0,0):C.GC_1444,(0,1):C.GC_3367})

V_544 = Vertex(name = 'V_544',
               particles = [ P.c__tilde__, P.b, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3449,(0,4):C.GC_3592,(0,2):C.GC_3591,(0,3):C.GC_3591,(0,0):C.GC_1445,(0,1):C.GC_3368})

V_545 = Vertex(name = 'V_545',
               particles = [ P.t__tilde__, P.b, P.e__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3450,(0,4):C.GC_3594,(0,2):C.GC_3593,(0,3):C.GC_3593,(0,0):C.GC_1446,(0,1):C.GC_3369})

V_546 = Vertex(name = 'V_546',
               particles = [ P.u__tilde__, P.b, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3451,(0,4):C.GC_3596,(0,2):C.GC_3595,(0,3):C.GC_3595,(0,0):C.GC_1399,(0,1):C.GC_3370})

V_547 = Vertex(name = 'V_547',
               particles = [ P.c__tilde__, P.b, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3452,(0,4):C.GC_3598,(0,2):C.GC_3597,(0,3):C.GC_3597,(0,0):C.GC_1400,(0,1):C.GC_3371})

V_548 = Vertex(name = 'V_548',
               particles = [ P.t__tilde__, P.b, P.mu__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3453,(0,4):C.GC_3600,(0,2):C.GC_3599,(0,3):C.GC_3599,(0,0):C.GC_1401,(0,1):C.GC_3372})

V_549 = Vertex(name = 'V_549',
               particles = [ P.u__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3454,(0,4):C.GC_3602,(0,2):C.GC_3601,(0,3):C.GC_3601,(0,0):C.GC_1426,(0,1):C.GC_3373})

V_550 = Vertex(name = 'V_550',
               particles = [ P.c__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3455,(0,4):C.GC_3604,(0,2):C.GC_3603,(0,3):C.GC_3603,(0,0):C.GC_1427,(0,1):C.GC_3374})

V_551 = Vertex(name = 'V_551',
               particles = [ P.t__tilde__, P.b, P.mu__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3456,(0,4):C.GC_3606,(0,2):C.GC_3605,(0,3):C.GC_3605,(0,0):C.GC_1428,(0,1):C.GC_3375})

V_552 = Vertex(name = 'V_552',
               particles = [ P.u__tilde__, P.b, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3457,(0,4):C.GC_3608,(0,2):C.GC_3607,(0,3):C.GC_3607,(0,0):C.GC_1453,(0,1):C.GC_3376})

V_553 = Vertex(name = 'V_553',
               particles = [ P.c__tilde__, P.b, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3458,(0,4):C.GC_3610,(0,2):C.GC_3609,(0,3):C.GC_3609,(0,0):C.GC_1454,(0,1):C.GC_3377})

V_554 = Vertex(name = 'V_554',
               particles = [ P.t__tilde__, P.b, P.mu__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3459,(0,4):C.GC_3612,(0,2):C.GC_3611,(0,3):C.GC_3611,(0,0):C.GC_1455,(0,1):C.GC_3378})

V_555 = Vertex(name = 'V_555',
               particles = [ P.u__tilde__, P.b, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3460,(0,4):C.GC_3614,(0,2):C.GC_3613,(0,3):C.GC_3613,(0,0):C.GC_1408,(0,1):C.GC_3379})

V_556 = Vertex(name = 'V_556',
               particles = [ P.c__tilde__, P.b, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3461,(0,4):C.GC_3616,(0,2):C.GC_3615,(0,3):C.GC_3615,(0,0):C.GC_1409,(0,1):C.GC_3380})

V_557 = Vertex(name = 'V_557',
               particles = [ P.t__tilde__, P.b, P.ta__plus__, P.ve ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3462,(0,4):C.GC_3618,(0,2):C.GC_3617,(0,3):C.GC_3617,(0,0):C.GC_1410,(0,1):C.GC_3381})

V_558 = Vertex(name = 'V_558',
               particles = [ P.u__tilde__, P.b, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3463,(0,4):C.GC_3620,(0,2):C.GC_3619,(0,3):C.GC_3619,(0,0):C.GC_1435,(0,1):C.GC_3382})

V_559 = Vertex(name = 'V_559',
               particles = [ P.c__tilde__, P.b, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3464,(0,4):C.GC_3622,(0,2):C.GC_3621,(0,3):C.GC_3621,(0,0):C.GC_1436,(0,1):C.GC_3383})

V_560 = Vertex(name = 'V_560',
               particles = [ P.t__tilde__, P.b, P.ta__plus__, P.vm ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3465,(0,4):C.GC_3624,(0,2):C.GC_3623,(0,3):C.GC_3623,(0,0):C.GC_1437,(0,1):C.GC_3384})

V_561 = Vertex(name = 'V_561',
               particles = [ P.u__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3466,(0,4):C.GC_3626,(0,2):C.GC_3625,(0,3):C.GC_3625,(0,0):C.GC_1462,(0,1):C.GC_3385})

V_562 = Vertex(name = 'V_562',
               particles = [ P.c__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3467,(0,4):C.GC_3628,(0,2):C.GC_3627,(0,3):C.GC_3627,(0,0):C.GC_1463,(0,1):C.GC_3386})

V_563 = Vertex(name = 'V_563',
               particles = [ P.t__tilde__, P.b, P.ta__plus__, P.vt ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFFF12, L.FFFF13, L.FFFF21, L.FFFF22, L.FFFF23, L.FFFF5 ],
               couplings = {(0,5):C.GC_3468,(0,4):C.GC_3630,(0,2):C.GC_3629,(0,3):C.GC_3629,(0,0):C.GC_1464,(0,1):C.GC_3387})

V_564 = Vertex(name = 'V_564',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS3, L.VVVSS4, L.VVVSS6 ],
               couplings = {(0,0):C.GC_2482,(0,1):C.GC_4391,(0,2):C.GC_2481,(0,3):C.GC_4388})

V_565 = Vertex(name = 'V_565',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS3, L.VVVS4, L.VVVS6 ],
               couplings = {(0,0):C.GC_4784,(0,1):C.GC_4891,(0,2):C.GC_4783,(0,3):C.GC_4888})

V_566 = Vertex(name = 'V_566',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV15, L.VVVV5, L.VVVV8 ],
               couplings = {(0,1):C.GC_4439,(0,0):C.GC_4438,(0,2):C.GC_5284})

V_567 = Vertex(name = 'V_567',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_4436})

V_568 = Vertex(name = 'V_568',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_4437})

V_569 = Vertex(name = 'V_569',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV11, L.VVVV14, L.VVVV7 ],
               couplings = {(0,2):C.GC_4393,(0,1):C.GC_4392,(0,0):C.GC_5286})

V_570 = Vertex(name = 'V_570',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV11 ],
               couplings = {(0,0):C.GC_4374})

V_571 = Vertex(name = 'V_571',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV11 ],
               couplings = {(0,0):C.GC_4375})

V_572 = Vertex(name = 'V_572',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS2 ],
               couplings = {(0,0):C.GC_4440})

V_573 = Vertex(name = 'V_573',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS2 ],
               couplings = {(0,0):C.GC_4929})

V_574 = Vertex(name = 'V_574',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS2, L.VVVSS3, L.VVVSS5, L.VVVSS6 ],
               couplings = {(0,1):C.GC_2483,(0,0):C.GC_4390,(0,3):C.GC_2480,(0,2):C.GC_4389})

V_575 = Vertex(name = 'V_575',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS2, L.VVVS3, L.VVVS5, L.VVVS6 ],
               couplings = {(0,1):C.GC_4785,(0,0):C.GC_4890,(0,3):C.GC_4782,(0,2):C.GC_4889})

V_576 = Vertex(name = 'V_576',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVV16, L.VVVVV8 ],
               couplings = {(0,1):C.GC_4445,(0,0):C.GC_4444})

V_577 = Vertex(name = 'V_577',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV15, L.VVVV5, L.VVVV8 ],
               couplings = {(0,1):C.GC_2486,(0,0):C.GC_2484,(0,2):C.GC_31})

V_578 = Vertex(name = 'V_578',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_34})

V_579 = Vertex(name = 'V_579',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV26, L.VVVVV55 ],
               couplings = {(0,0):C.GC_4442,(0,1):C.GC_4441})

V_580 = Vertex(name = 'V_580',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVV32, L.VVVVV57 ],
               couplings = {(0,0):C.GC_4397,(0,1):C.GC_4395})

V_581 = Vertex(name = 'V_581',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS2 ],
               couplings = {(0,0):C.GC_2488})

V_582 = Vertex(name = 'V_582',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS2 ],
               couplings = {(0,0):C.GC_4786})

V_583 = Vertex(name = 'V_583',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV53 ],
               couplings = {(0,0):C.GC_4443})

V_584 = Vertex(name = 'V_584',
               particles = [ P.a, P.Z, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS1 ],
               couplings = {(0,0):C.GC_4642})

V_585 = Vertex(name = 'V_585',
               particles = [ P.a, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1 ],
               couplings = {(0,0):C.GC_5182})

V_586 = Vertex(name = 'V_586',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV15, L.VVVV5, L.VVVV8 ],
               couplings = {(0,1):C.GC_2487,(0,0):C.GC_2485,(0,2):C.GC_32})

V_587 = Vertex(name = 'V_587',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_35})

V_588 = Vertex(name = 'V_588',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_5281})

V_589 = Vertex(name = 'V_589',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS5 ],
               couplings = {(0,0):C.GC_4394})

V_590 = Vertex(name = 'V_590',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS5 ],
               couplings = {(0,0):C.GC_4892})

V_591 = Vertex(name = 'V_591',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV38, L.VVVVV45 ],
               couplings = {(0,0):C.GC_4398,(0,1):C.GC_4396})

V_592 = Vertex(name = 'V_592',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV27, L.VVVVV52 ],
               couplings = {(0,0):C.GC_2492,(0,1):C.GC_2490})

V_593 = Vertex(name = 'V_593',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV62 ],
               couplings = {(0,0):C.GC_4399})

V_594 = Vertex(name = 'V_594',
               particles = [ P.Z, P.Z, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS1 ],
               couplings = {(0,0):C.GC_4641})

V_595 = Vertex(name = 'V_595',
               particles = [ P.Z, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS1 ],
               couplings = {(0,0):C.GC_5181})

V_596 = Vertex(name = 'V_596',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS2 ],
               couplings = {(0,0):C.GC_2489})

V_597 = Vertex(name = 'V_597',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS2 ],
               couplings = {(0,0):C.GC_4787})

V_598 = Vertex(name = 'V_598',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV53 ],
               couplings = {(0,0):C.GC_2494})

V_599 = Vertex(name = 'V_599',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV39, L.VVVVV56 ],
               couplings = {(0,0):C.GC_2493,(0,1):C.GC_2491})

V_600 = Vertex(name = 'V_600',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5, L.FFV6 ],
               couplings = {(0,4):C.GC_1,(0,0):C.GC_5264,(0,3):C.GC_5205,(0,2):C.GC_5390,(0,1):C.GC_5016})

V_601 = Vertex(name = 'V_601',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV6 ],
               couplings = {(0,1):C.GC_17,(0,0):C.GC_4366})

V_602 = Vertex(name = 'V_602',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV6 ],
               couplings = {(0,1):C.GC_5253,(0,0):C.GC_4372})

V_603 = Vertex(name = 'V_603',
               particles = [ P.s__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,0):C.GC_5233,(0,3):C.GC_5206,(0,2):C.GC_5414,(0,1):C.GC_5017})

V_604 = Vertex(name = 'V_604',
               particles = [ P.b__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,0):C.GC_5235,(0,3):C.GC_5207,(0,2):C.GC_5438,(0,1):C.GC_5018})

V_605 = Vertex(name = 'V_605',
               particles = [ P.d__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,0):C.GC_5237,(0,3):C.GC_5622,(0,2):C.GC_5398,(0,1):C.GC_5019})

V_606 = Vertex(name = 'V_606',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5, L.FFV6 ],
               couplings = {(0,4):C.GC_1,(0,0):C.GC_5265,(0,3):C.GC_5208,(0,2):C.GC_5422,(0,1):C.GC_5020})

V_607 = Vertex(name = 'V_607',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV6 ],
               couplings = {(0,1):C.GC_17,(0,0):C.GC_4366})

V_608 = Vertex(name = 'V_608',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV6 ],
               couplings = {(0,1):C.GC_5253,(0,0):C.GC_4372})

V_609 = Vertex(name = 'V_609',
               particles = [ P.b__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,0):C.GC_5239,(0,3):C.GC_5209,(0,2):C.GC_5446,(0,1):C.GC_5021})

V_610 = Vertex(name = 'V_610',
               particles = [ P.d__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,0):C.GC_5241,(0,3):C.GC_5628,(0,2):C.GC_5406,(0,1):C.GC_5022})

V_611 = Vertex(name = 'V_611',
               particles = [ P.s__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,0):C.GC_5243,(0,3):C.GC_5634,(0,2):C.GC_5430,(0,1):C.GC_5023})

V_612 = Vertex(name = 'V_612',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5, L.FFV6 ],
               couplings = {(0,4):C.GC_1,(0,0):C.GC_5266,(0,3):C.GC_5210,(0,2):C.GC_5454,(0,1):C.GC_5024})

V_613 = Vertex(name = 'V_613',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV6 ],
               couplings = {(0,1):C.GC_17,(0,0):C.GC_4366})

V_614 = Vertex(name = 'V_614',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV6 ],
               couplings = {(0,1):C.GC_5253,(0,0):C.GC_4372})

V_615 = Vertex(name = 'V_615',
               particles = [ P.d__tilde__, P.d, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4609,(0,1):C.GC_4572})

V_616 = Vertex(name = 'V_616',
               particles = [ P.s__tilde__, P.d, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4611,(0,1):C.GC_4573})

V_617 = Vertex(name = 'V_617',
               particles = [ P.b__tilde__, P.d, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4613,(0,1):C.GC_4574})

V_618 = Vertex(name = 'V_618',
               particles = [ P.d__tilde__, P.s, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4615,(0,1):C.GC_5618})

V_619 = Vertex(name = 'V_619',
               particles = [ P.s__tilde__, P.s, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4617,(0,1):C.GC_4575})

V_620 = Vertex(name = 'V_620',
               particles = [ P.b__tilde__, P.s, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4619,(0,1):C.GC_4576})

V_621 = Vertex(name = 'V_621',
               particles = [ P.d__tilde__, P.b, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4621,(0,1):C.GC_5624})

V_622 = Vertex(name = 'V_622',
               particles = [ P.s__tilde__, P.b, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4623,(0,1):C.GC_5630})

V_623 = Vertex(name = 'V_623',
               particles = [ P.b__tilde__, P.b, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4625,(0,1):C.GC_4577})

V_624 = Vertex(name = 'V_624',
               particles = [ P.d__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,0):C.GC_5152,(0,2):C.GC_5115,(0,1):C.GC_5387,(0,3):C.GC_4474})

V_625 = Vertex(name = 'V_625',
               particles = [ P.s__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,0):C.GC_5154,(0,2):C.GC_5116,(0,1):C.GC_5411,(0,3):C.GC_4475})

V_626 = Vertex(name = 'V_626',
               particles = [ P.b__tilde__, P.d, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,0):C.GC_5156,(0,2):C.GC_5117,(0,1):C.GC_5435,(0,3):C.GC_4476})

V_627 = Vertex(name = 'V_627',
               particles = [ P.d__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,0):C.GC_5158,(0,2):C.GC_5620,(0,1):C.GC_5395,(0,3):C.GC_4477})

V_628 = Vertex(name = 'V_628',
               particles = [ P.s__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,0):C.GC_5160,(0,2):C.GC_5118,(0,1):C.GC_5419,(0,3):C.GC_4478})

V_629 = Vertex(name = 'V_629',
               particles = [ P.b__tilde__, P.s, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,0):C.GC_5162,(0,2):C.GC_5119,(0,1):C.GC_5443,(0,3):C.GC_4479})

V_630 = Vertex(name = 'V_630',
               particles = [ P.d__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,0):C.GC_5164,(0,2):C.GC_5626,(0,1):C.GC_5403,(0,3):C.GC_4480})

V_631 = Vertex(name = 'V_631',
               particles = [ P.s__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,0):C.GC_5166,(0,2):C.GC_5632,(0,1):C.GC_5427,(0,3):C.GC_4481})

V_632 = Vertex(name = 'V_632',
               particles = [ P.b__tilde__, P.b, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,0):C.GC_5168,(0,2):C.GC_5120,(0,1):C.GC_5451,(0,3):C.GC_4482})

V_633 = Vertex(name = 'V_633',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5, L.FFV8 ],
               couplings = {(0,4):C.GC_2,(0,0):C.GC_5261,(0,3):C.GC_5211,(0,2):C.GC_5496,(0,1):C.GC_5043})

V_634 = Vertex(name = 'V_634',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,1):C.GC_18,(0,0):C.GC_4366})

V_635 = Vertex(name = 'V_635',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,1):C.GC_5254,(0,0):C.GC_4372})

V_636 = Vertex(name = 'V_636',
               particles = [ P.mu__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,0):C.GC_5218,(0,3):C.GC_5212,(0,2):C.GC_5541,(0,1):C.GC_5044})

V_637 = Vertex(name = 'V_637',
               particles = [ P.ta__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,0):C.GC_5220,(0,3):C.GC_5213,(0,2):C.GC_5586,(0,1):C.GC_5045})

V_638 = Vertex(name = 'V_638',
               particles = [ P.e__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,0):C.GC_5667,(0,3):C.GC_5640,(0,2):C.GC_5511,(0,1):C.GC_5046})

V_639 = Vertex(name = 'V_639',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5, L.FFV8 ],
               couplings = {(0,4):C.GC_2,(0,0):C.GC_5262,(0,3):C.GC_5214,(0,2):C.GC_5556,(0,1):C.GC_5047})

V_640 = Vertex(name = 'V_640',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,1):C.GC_18,(0,0):C.GC_4366})

V_641 = Vertex(name = 'V_641',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,1):C.GC_5254,(0,0):C.GC_4372})

V_642 = Vertex(name = 'V_642',
               particles = [ P.ta__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,0):C.GC_5222,(0,3):C.GC_5215,(0,2):C.GC_5601,(0,1):C.GC_5048})

V_643 = Vertex(name = 'V_643',
               particles = [ P.e__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,0):C.GC_5682,(0,3):C.GC_5646,(0,2):C.GC_5526,(0,1):C.GC_5049})

V_644 = Vertex(name = 'V_644',
               particles = [ P.mu__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,0):C.GC_5697,(0,3):C.GC_5652,(0,2):C.GC_5571,(0,1):C.GC_5050})

V_645 = Vertex(name = 'V_645',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5, L.FFV8 ],
               couplings = {(0,4):C.GC_2,(0,0):C.GC_5263,(0,3):C.GC_5216,(0,2):C.GC_5616,(0,1):C.GC_5051})

V_646 = Vertex(name = 'V_646',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,1):C.GC_18,(0,0):C.GC_4366})

V_647 = Vertex(name = 'V_647',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV8 ],
               couplings = {(0,1):C.GC_5254,(0,0):C.GC_4372})

V_648 = Vertex(name = 'V_648',
               particles = [ P.e__plus__, P.e__minus__, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4585,(0,1):C.GC_4578})

V_649 = Vertex(name = 'V_649',
               particles = [ P.mu__plus__, P.e__minus__, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4587,(0,1):C.GC_4579})

V_650 = Vertex(name = 'V_650',
               particles = [ P.ta__plus__, P.e__minus__, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4589,(0,1):C.GC_4580})

V_651 = Vertex(name = 'V_651',
               particles = [ P.e__plus__, P.mu__minus__, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_5659,(0,1):C.GC_5636})

V_652 = Vertex(name = 'V_652',
               particles = [ P.mu__plus__, P.mu__minus__, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4591,(0,1):C.GC_4581})

V_653 = Vertex(name = 'V_653',
               particles = [ P.ta__plus__, P.mu__minus__, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4593,(0,1):C.GC_4582})

V_654 = Vertex(name = 'V_654',
               particles = [ P.e__plus__, P.ta__minus__, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_5674,(0,1):C.GC_5642})

V_655 = Vertex(name = 'V_655',
               particles = [ P.mu__plus__, P.ta__minus__, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_5689,(0,1):C.GC_5648})

V_656 = Vertex(name = 'V_656',
               particles = [ P.ta__plus__, P.ta__minus__, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4595,(0,1):C.GC_4583})

V_657 = Vertex(name = 'V_657',
               particles = [ P.e__plus__, P.e__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,0):C.GC_5128,(0,2):C.GC_5121,(0,1):C.GC_5493,(0,3):C.GC_4500})

V_658 = Vertex(name = 'V_658',
               particles = [ P.mu__plus__, P.e__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,0):C.GC_5130,(0,2):C.GC_5122,(0,1):C.GC_5538,(0,3):C.GC_4501})

V_659 = Vertex(name = 'V_659',
               particles = [ P.ta__plus__, P.e__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,0):C.GC_5132,(0,2):C.GC_5123,(0,1):C.GC_5583,(0,3):C.GC_4502})

V_660 = Vertex(name = 'V_660',
               particles = [ P.e__plus__, P.mu__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,0):C.GC_5663,(0,2):C.GC_5638,(0,1):C.GC_5508,(0,3):C.GC_4503})

V_661 = Vertex(name = 'V_661',
               particles = [ P.mu__plus__, P.mu__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,0):C.GC_5134,(0,2):C.GC_5124,(0,1):C.GC_5553,(0,3):C.GC_4504})

V_662 = Vertex(name = 'V_662',
               particles = [ P.ta__plus__, P.mu__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,0):C.GC_5136,(0,2):C.GC_5125,(0,1):C.GC_5598,(0,3):C.GC_4505})

V_663 = Vertex(name = 'V_663',
               particles = [ P.e__plus__, P.ta__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,0):C.GC_5678,(0,2):C.GC_5644,(0,1):C.GC_5523,(0,3):C.GC_4506})

V_664 = Vertex(name = 'V_664',
               particles = [ P.mu__plus__, P.ta__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,0):C.GC_5693,(0,2):C.GC_5650,(0,1):C.GC_5568,(0,3):C.GC_4507})

V_665 = Vertex(name = 'V_665',
               particles = [ P.ta__plus__, P.ta__minus__, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,0):C.GC_5138,(0,2):C.GC_5126,(0,1):C.GC_5613,(0,3):C.GC_4508})

V_666 = Vertex(name = 'V_666',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5, L.FFV9 ],
               couplings = {(0,4):C.GC_1,(0,0):C.GC_5255,(0,3):C.GC_5226,(0,2):C.GC_6173,(0,1):C.GC_5070})

V_667 = Vertex(name = 'V_667',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV9 ],
               couplings = {(0,1):C.GC_17,(0,0):C.GC_4365})

V_668 = Vertex(name = 'V_668',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV9 ],
               couplings = {(0,1):C.GC_5253,(0,0):C.GC_4371})

V_669 = Vertex(name = 'V_669',
               particles = [ P.c__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,0):C.GC_5223,(0,3):C.GC_5227,(0,2):C.GC_6197,(0,1):C.GC_5071})

V_670 = Vertex(name = 'V_670',
               particles = [ P.t__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,0):C.GC_5224,(0,3):C.GC_5228,(0,2):C.GC_6221,(0,1):C.GC_5072})

V_671 = Vertex(name = 'V_671',
               particles = [ P.u__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,0):C.GC_5703,(0,3):C.GC_5721,(0,2):C.GC_6181,(0,1):C.GC_5073})

V_672 = Vertex(name = 'V_672',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5, L.FFV9 ],
               couplings = {(0,4):C.GC_1,(0,0):C.GC_5256,(0,3):C.GC_5229,(0,2):C.GC_6205,(0,1):C.GC_5074})

V_673 = Vertex(name = 'V_673',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV9 ],
               couplings = {(0,1):C.GC_17,(0,0):C.GC_4365})

V_674 = Vertex(name = 'V_674',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV9 ],
               couplings = {(0,1):C.GC_5253,(0,0):C.GC_4371})

V_675 = Vertex(name = 'V_675',
               particles = [ P.t__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,0):C.GC_5225,(0,3):C.GC_5230,(0,2):C.GC_6229,(0,1):C.GC_5075})

V_676 = Vertex(name = 'V_676',
               particles = [ P.u__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,0):C.GC_5709,(0,3):C.GC_5727,(0,2):C.GC_6189,(0,1):C.GC_5076})

V_677 = Vertex(name = 'V_677',
               particles = [ P.c__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,0):C.GC_5715,(0,3):C.GC_5733,(0,2):C.GC_6213,(0,1):C.GC_5077})

V_678 = Vertex(name = 'V_678',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5, L.FFV9 ],
               couplings = {(0,4):C.GC_1,(0,0):C.GC_5257,(0,3):C.GC_5231,(0,2):C.GC_6237,(0,1):C.GC_5078})

V_679 = Vertex(name = 'V_679',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV9 ],
               couplings = {(0,1):C.GC_17,(0,0):C.GC_4365})

V_680 = Vertex(name = 'V_680',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV9 ],
               couplings = {(0,1):C.GC_5253,(0,0):C.GC_4371})

V_681 = Vertex(name = 'V_681',
               particles = [ P.u__tilde__, P.u, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4596,(0,1):C.GC_4602})

V_682 = Vertex(name = 'V_682',
               particles = [ P.c__tilde__, P.u, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4597,(0,1):C.GC_4603})

V_683 = Vertex(name = 'V_683',
               particles = [ P.t__tilde__, P.u, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4598,(0,1):C.GC_4604})

V_684 = Vertex(name = 'V_684',
               particles = [ P.u__tilde__, P.c, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_5699,(0,1):C.GC_5717})

V_685 = Vertex(name = 'V_685',
               particles = [ P.c__tilde__, P.c, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4599,(0,1):C.GC_4605})

V_686 = Vertex(name = 'V_686',
               particles = [ P.t__tilde__, P.c, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4600,(0,1):C.GC_4606})

V_687 = Vertex(name = 'V_687',
               particles = [ P.u__tilde__, P.t, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_5705,(0,1):C.GC_5723})

V_688 = Vertex(name = 'V_688',
               particles = [ P.c__tilde__, P.t, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_5711,(0,1):C.GC_5729})

V_689 = Vertex(name = 'V_689',
               particles = [ P.t__tilde__, P.t, P.a, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4601,(0,1):C.GC_4607})

V_690 = Vertex(name = 'V_690',
               particles = [ P.u__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,0):C.GC_5139,(0,2):C.GC_5145,(0,1):C.GC_6170,(0,3):C.GC_4527})

V_691 = Vertex(name = 'V_691',
               particles = [ P.c__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,0):C.GC_5140,(0,2):C.GC_5146,(0,1):C.GC_6194,(0,3):C.GC_4528})

V_692 = Vertex(name = 'V_692',
               particles = [ P.t__tilde__, P.u, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,0):C.GC_5141,(0,2):C.GC_5147,(0,1):C.GC_6218,(0,3):C.GC_4529})

V_693 = Vertex(name = 'V_693',
               particles = [ P.u__tilde__, P.c, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,0):C.GC_5701,(0,2):C.GC_5719,(0,1):C.GC_6178,(0,3):C.GC_4530})

V_694 = Vertex(name = 'V_694',
               particles = [ P.c__tilde__, P.c, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,0):C.GC_5142,(0,2):C.GC_5148,(0,1):C.GC_6202,(0,3):C.GC_4531})

V_695 = Vertex(name = 'V_695',
               particles = [ P.t__tilde__, P.c, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,0):C.GC_5143,(0,2):C.GC_5149,(0,1):C.GC_6226,(0,3):C.GC_4532})

V_696 = Vertex(name = 'V_696',
               particles = [ P.u__tilde__, P.t, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,0):C.GC_5707,(0,2):C.GC_5725,(0,1):C.GC_6186,(0,3):C.GC_4533})

V_697 = Vertex(name = 'V_697',
               particles = [ P.c__tilde__, P.t, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,0):C.GC_5713,(0,2):C.GC_5731,(0,1):C.GC_6210,(0,3):C.GC_4534})

V_698 = Vertex(name = 'V_698',
               particles = [ P.t__tilde__, P.t, P.a, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,0):C.GC_5144,(0,2):C.GC_5150,(0,1):C.GC_6234,(0,3):C.GC_4535})

V_699 = Vertex(name = 'V_699',
               particles = [ P.ve__tilde__, P.ve, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4450})

V_700 = Vertex(name = 'V_700',
               particles = [ P.ve__tilde__, P.ve, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4455})

V_701 = Vertex(name = 'V_701',
               particles = [ P.ve__tilde__, P.ve, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5258})

V_702 = Vertex(name = 'V_702',
               particles = [ P.vm__tilde__, P.ve, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5217})

V_703 = Vertex(name = 'V_703',
               particles = [ P.vt__tilde__, P.ve, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5219})

V_704 = Vertex(name = 'V_704',
               particles = [ P.ve__tilde__, P.vm, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5666})

V_705 = Vertex(name = 'V_705',
               particles = [ P.vm__tilde__, P.vm, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4450})

V_706 = Vertex(name = 'V_706',
               particles = [ P.vm__tilde__, P.vm, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4455})

V_707 = Vertex(name = 'V_707',
               particles = [ P.vm__tilde__, P.vm, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5259})

V_708 = Vertex(name = 'V_708',
               particles = [ P.vt__tilde__, P.vm, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5221})

V_709 = Vertex(name = 'V_709',
               particles = [ P.ve__tilde__, P.vt, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5681})

V_710 = Vertex(name = 'V_710',
               particles = [ P.vm__tilde__, P.vt, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5696})

V_711 = Vertex(name = 'V_711',
               particles = [ P.vt__tilde__, P.vt, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4450})

V_712 = Vertex(name = 'V_712',
               particles = [ P.vt__tilde__, P.vt, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4455})

V_713 = Vertex(name = 'V_713',
               particles = [ P.vt__tilde__, P.vt, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5260})

V_714 = Vertex(name = 'V_714',
               particles = [ P.ve__tilde__, P.ve, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_4584})

V_715 = Vertex(name = 'V_715',
               particles = [ P.vm__tilde__, P.ve, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_4586})

V_716 = Vertex(name = 'V_716',
               particles = [ P.vt__tilde__, P.ve, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_4588})

V_717 = Vertex(name = 'V_717',
               particles = [ P.ve__tilde__, P.vm, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_5658})

V_718 = Vertex(name = 'V_718',
               particles = [ P.vm__tilde__, P.vm, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_4590})

V_719 = Vertex(name = 'V_719',
               particles = [ P.vt__tilde__, P.vm, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_4592})

V_720 = Vertex(name = 'V_720',
               particles = [ P.ve__tilde__, P.vt, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_5673})

V_721 = Vertex(name = 'V_721',
               particles = [ P.vm__tilde__, P.vt, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_5688})

V_722 = Vertex(name = 'V_722',
               particles = [ P.vt__tilde__, P.vt, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_4594})

V_723 = Vertex(name = 'V_723',
               particles = [ P.ve__tilde__, P.ve, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_5127})

V_724 = Vertex(name = 'V_724',
               particles = [ P.vm__tilde__, P.ve, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_5129})

V_725 = Vertex(name = 'V_725',
               particles = [ P.vt__tilde__, P.ve, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_5131})

V_726 = Vertex(name = 'V_726',
               particles = [ P.ve__tilde__, P.vm, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_5662})

V_727 = Vertex(name = 'V_727',
               particles = [ P.vm__tilde__, P.vm, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_5133})

V_728 = Vertex(name = 'V_728',
               particles = [ P.vt__tilde__, P.vm, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_5135})

V_729 = Vertex(name = 'V_729',
               particles = [ P.ve__tilde__, P.vt, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_5677})

V_730 = Vertex(name = 'V_730',
               particles = [ P.vm__tilde__, P.vt, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_5692})

V_731 = Vertex(name = 'V_731',
               particles = [ P.vt__tilde__, P.vt, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1 ],
               couplings = {(0,0):C.GC_5137})

V_732 = Vertex(name = 'V_732',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV4, L.FFV7 ],
               couplings = {(0,2):C.GC_14,(0,1):C.GC_5322,(0,0):C.GC_4651})

V_733 = Vertex(name = 'V_733',
               particles = [ P.s__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV4 ],
               couplings = {(0,1):C.GC_5334,(0,0):C.GC_4652})

V_734 = Vertex(name = 'V_734',
               particles = [ P.b__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV4 ],
               couplings = {(0,1):C.GC_5346,(0,0):C.GC_4653})

V_735 = Vertex(name = 'V_735',
               particles = [ P.d__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV4 ],
               couplings = {(0,1):C.GC_5326,(0,0):C.GC_4654})

V_736 = Vertex(name = 'V_736',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV4, L.FFV7 ],
               couplings = {(0,2):C.GC_14,(0,1):C.GC_5338,(0,0):C.GC_4655})

V_737 = Vertex(name = 'V_737',
               particles = [ P.b__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV4 ],
               couplings = {(0,1):C.GC_5350,(0,0):C.GC_4656})

V_738 = Vertex(name = 'V_738',
               particles = [ P.d__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV4 ],
               couplings = {(0,1):C.GC_5330,(0,0):C.GC_4657})

V_739 = Vertex(name = 'V_739',
               particles = [ P.s__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV4 ],
               couplings = {(0,1):C.GC_5342,(0,0):C.GC_4658})

V_740 = Vertex(name = 'V_740',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV4, L.FFV7 ],
               couplings = {(0,2):C.GC_14,(0,1):C.GC_5354,(0,0):C.GC_4659})

V_741 = Vertex(name = 'V_741',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV4, L.FFV7 ],
               couplings = {(0,2):C.GC_14,(0,1):C.GC_6105,(0,0):C.GC_4692})

V_742 = Vertex(name = 'V_742',
               particles = [ P.c__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV4 ],
               couplings = {(0,1):C.GC_6117,(0,0):C.GC_4693})

V_743 = Vertex(name = 'V_743',
               particles = [ P.t__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV4 ],
               couplings = {(0,1):C.GC_6129,(0,0):C.GC_4694})

V_744 = Vertex(name = 'V_744',
               particles = [ P.u__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV4 ],
               couplings = {(0,1):C.GC_6109,(0,0):C.GC_4695})

V_745 = Vertex(name = 'V_745',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV4, L.FFV7 ],
               couplings = {(0,2):C.GC_14,(0,1):C.GC_6121,(0,0):C.GC_4696})

V_746 = Vertex(name = 'V_746',
               particles = [ P.t__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV4 ],
               couplings = {(0,1):C.GC_6133,(0,0):C.GC_4697})

V_747 = Vertex(name = 'V_747',
               particles = [ P.u__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV4 ],
               couplings = {(0,1):C.GC_6113,(0,0):C.GC_4698})

V_748 = Vertex(name = 'V_748',
               particles = [ P.c__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV4 ],
               couplings = {(0,1):C.GC_6125,(0,0):C.GC_4699})

V_749 = Vertex(name = 'V_749',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV12, L.FFV4, L.FFV7 ],
               couplings = {(0,2):C.GC_14,(0,1):C.GC_6137,(0,0):C.GC_4700})

V_750 = Vertex(name = 'V_750',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_4797,(0,1):C.GC_4815,(0,0):C.GC_4,(0,3):C.GC_4964})

V_751 = Vertex(name = 'V_751',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_20})

V_752 = Vertex(name = 'V_752',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4976})

V_753 = Vertex(name = 'V_753',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_4799,(0,1):C.GC_4817,(0,0):C.GC_5,(0,3):C.GC_4965})

V_754 = Vertex(name = 'V_754',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_21})

V_755 = Vertex(name = 'V_755',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4977})

V_756 = Vertex(name = 'V_756',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_4801,(0,1):C.GC_4819,(0,0):C.GC_6,(0,3):C.GC_4966})

V_757 = Vertex(name = 'V_757',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_22})

V_758 = Vertex(name = 'V_758',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4978})

V_759 = Vertex(name = 'V_759',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_4803,(0,1):C.GC_4821,(0,0):C.GC_7,(0,3):C.GC_4967})

V_760 = Vertex(name = 'V_760',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_23})

V_761 = Vertex(name = 'V_761',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4979})

V_762 = Vertex(name = 'V_762',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_4805,(0,1):C.GC_4823,(0,0):C.GC_8,(0,3):C.GC_4968})

V_763 = Vertex(name = 'V_763',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_24})

V_764 = Vertex(name = 'V_764',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4980})

V_765 = Vertex(name = 'V_765',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_4807,(0,1):C.GC_4825,(0,0):C.GC_9,(0,3):C.GC_4969})

V_766 = Vertex(name = 'V_766',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_25})

V_767 = Vertex(name = 'V_767',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4981})

V_768 = Vertex(name = 'V_768',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_4809,(0,1):C.GC_4827,(0,0):C.GC_10,(0,3):C.GC_4970})

V_769 = Vertex(name = 'V_769',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_26})

V_770 = Vertex(name = 'V_770',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4982})

V_771 = Vertex(name = 'V_771',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_4811,(0,1):C.GC_4829,(0,0):C.GC_11,(0,3):C.GC_4971})

V_772 = Vertex(name = 'V_772',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_27})

V_773 = Vertex(name = 'V_773',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4983})

V_774 = Vertex(name = 'V_774',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_4813,(0,1):C.GC_4831,(0,0):C.GC_12,(0,3):C.GC_4972})

V_775 = Vertex(name = 'V_775',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_28})

V_776 = Vertex(name = 'V_776',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4984})

V_777 = Vertex(name = 'V_777',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_3712,(0,1):C.GC_2453})

V_778 = Vertex(name = 'V_778',
               particles = [ P.s__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_3713,(0,1):C.GC_2454})

V_779 = Vertex(name = 'V_779',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_3714,(0,1):C.GC_2455})

V_780 = Vertex(name = 'V_780',
               particles = [ P.d__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_3715,(0,1):C.GC_2456})

V_781 = Vertex(name = 'V_781',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_3716,(0,1):C.GC_2457})

V_782 = Vertex(name = 'V_782',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_3717,(0,1):C.GC_2458})

V_783 = Vertex(name = 'V_783',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_3718,(0,1):C.GC_2459})

V_784 = Vertex(name = 'V_784',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_3719,(0,1):C.GC_2460})

V_785 = Vertex(name = 'V_785',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_3720,(0,1):C.GC_2461})

V_786 = Vertex(name = 'V_786',
               particles = [ P.d__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,1):C.GC_3721,(0,3):C.GC_3739,(0,0):C.GC_4788,(0,2):C.GC_4755})

V_787 = Vertex(name = 'V_787',
               particles = [ P.s__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,1):C.GC_3723,(0,3):C.GC_3741,(0,0):C.GC_4789,(0,2):C.GC_4756})

V_788 = Vertex(name = 'V_788',
               particles = [ P.b__tilde__, P.u, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,1):C.GC_3725,(0,3):C.GC_3743,(0,0):C.GC_4790,(0,2):C.GC_4757})

V_789 = Vertex(name = 'V_789',
               particles = [ P.d__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,1):C.GC_3727,(0,3):C.GC_3745,(0,0):C.GC_4791,(0,2):C.GC_4758})

V_790 = Vertex(name = 'V_790',
               particles = [ P.s__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,1):C.GC_3729,(0,3):C.GC_3747,(0,0):C.GC_4792,(0,2):C.GC_4759})

V_791 = Vertex(name = 'V_791',
               particles = [ P.b__tilde__, P.c, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,1):C.GC_3731,(0,3):C.GC_3749,(0,0):C.GC_4793,(0,2):C.GC_4760})

V_792 = Vertex(name = 'V_792',
               particles = [ P.d__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,1):C.GC_3733,(0,3):C.GC_3751,(0,0):C.GC_4794,(0,2):C.GC_4761})

V_793 = Vertex(name = 'V_793',
               particles = [ P.s__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,1):C.GC_3735,(0,3):C.GC_3753,(0,0):C.GC_4795,(0,2):C.GC_4762})

V_794 = Vertex(name = 'V_794',
               particles = [ P.b__tilde__, P.t, P.W__minus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,1):C.GC_3737,(0,3):C.GC_3755,(0,0):C.GC_4796,(0,2):C.GC_4763})

V_795 = Vertex(name = 'V_795',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV12 ],
               couplings = {(0,1):C.GC_4678,(0,0):C.GC_3})

V_796 = Vertex(name = 'V_796',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_19})

V_797 = Vertex(name = 'V_797',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4958})

V_798 = Vertex(name = 'V_798',
               particles = [ P.mu__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV12 ],
               couplings = {(0,1):C.GC_4679,(0,0):C.GC_4959})

V_799 = Vertex(name = 'V_799',
               particles = [ P.ta__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV12 ],
               couplings = {(0,1):C.GC_4680,(0,0):C.GC_4960})

V_800 = Vertex(name = 'V_800',
               particles = [ P.e__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV12 ],
               couplings = {(0,1):C.GC_4681,(0,0):C.GC_5655})

V_801 = Vertex(name = 'V_801',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV12 ],
               couplings = {(0,1):C.GC_4682,(0,0):C.GC_3})

V_802 = Vertex(name = 'V_802',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_19})

V_803 = Vertex(name = 'V_803',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4961})

V_804 = Vertex(name = 'V_804',
               particles = [ P.ta__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV12 ],
               couplings = {(0,1):C.GC_4683,(0,0):C.GC_4962})

V_805 = Vertex(name = 'V_805',
               particles = [ P.e__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV12 ],
               couplings = {(0,1):C.GC_4684,(0,0):C.GC_5670})

V_806 = Vertex(name = 'V_806',
               particles = [ P.mu__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV12 ],
               couplings = {(0,1):C.GC_4685,(0,0):C.GC_5685})

V_807 = Vertex(name = 'V_807',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV12 ],
               couplings = {(0,1):C.GC_4686,(0,0):C.GC_3})

V_808 = Vertex(name = 'V_808',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_19})

V_809 = Vertex(name = 'V_809',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4963})

V_810 = Vertex(name = 'V_810',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2447})

V_811 = Vertex(name = 'V_811',
               particles = [ P.mu__plus__, P.ve, P.W__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2448})

V_812 = Vertex(name = 'V_812',
               particles = [ P.ta__plus__, P.ve, P.W__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2449})

V_813 = Vertex(name = 'V_813',
               particles = [ P.e__plus__, P.vm, P.W__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_5653})

V_814 = Vertex(name = 'V_814',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2450})

V_815 = Vertex(name = 'V_815',
               particles = [ P.ta__plus__, P.vm, P.W__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2451})

V_816 = Vertex(name = 'V_816',
               particles = [ P.e__plus__, P.vt, P.W__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_5668})

V_817 = Vertex(name = 'V_817',
               particles = [ P.mu__plus__, P.vt, P.W__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_5683})

V_818 = Vertex(name = 'V_818',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2452})

V_819 = Vertex(name = 'V_819',
               particles = [ P.e__plus__, P.ve, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS9 ],
               couplings = {(0,1):C.GC_1206,(0,0):C.GC_4749})

V_820 = Vertex(name = 'V_820',
               particles = [ P.mu__plus__, P.ve, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS9 ],
               couplings = {(0,1):C.GC_1207,(0,0):C.GC_4750})

V_821 = Vertex(name = 'V_821',
               particles = [ P.ta__plus__, P.ve, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS9 ],
               couplings = {(0,1):C.GC_1208,(0,0):C.GC_4751})

V_822 = Vertex(name = 'V_822',
               particles = [ P.e__plus__, P.vm, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS9 ],
               couplings = {(0,1):C.GC_1209,(0,0):C.GC_5654})

V_823 = Vertex(name = 'V_823',
               particles = [ P.mu__plus__, P.vm, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS9 ],
               couplings = {(0,1):C.GC_1210,(0,0):C.GC_4752})

V_824 = Vertex(name = 'V_824',
               particles = [ P.ta__plus__, P.vm, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS9 ],
               couplings = {(0,1):C.GC_1211,(0,0):C.GC_4753})

V_825 = Vertex(name = 'V_825',
               particles = [ P.e__plus__, P.vt, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS9 ],
               couplings = {(0,1):C.GC_1212,(0,0):C.GC_5669})

V_826 = Vertex(name = 'V_826',
               particles = [ P.mu__plus__, P.vt, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS9 ],
               couplings = {(0,1):C.GC_1213,(0,0):C.GC_5684})

V_827 = Vertex(name = 'V_827',
               particles = [ P.ta__plus__, P.vt, P.W__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS9 ],
               couplings = {(0,1):C.GC_1214,(0,0):C.GC_4754})

V_828 = Vertex(name = 'V_828',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_4842,(0,1):C.GC_4860,(0,0):C.GC_4985,(0,3):C.GC_5736})

V_829 = Vertex(name = 'V_829',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5761})

V_830 = Vertex(name = 'V_830',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5762})

V_831 = Vertex(name = 'V_831',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_4844,(0,1):C.GC_4862,(0,0):C.GC_4986,(0,3):C.GC_5745})

V_832 = Vertex(name = 'V_832',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5767})

V_833 = Vertex(name = 'V_833',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5768})

V_834 = Vertex(name = 'V_834',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_4846,(0,1):C.GC_4864,(0,0):C.GC_4987,(0,3):C.GC_5754})

V_835 = Vertex(name = 'V_835',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5773})

V_836 = Vertex(name = 'V_836',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5774})

V_837 = Vertex(name = 'V_837',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_4848,(0,1):C.GC_4866,(0,0):C.GC_4988,(0,3):C.GC_5739})

V_838 = Vertex(name = 'V_838',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5763})

V_839 = Vertex(name = 'V_839',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5764})

V_840 = Vertex(name = 'V_840',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_4850,(0,1):C.GC_4868,(0,0):C.GC_4989,(0,3):C.GC_5748})

V_841 = Vertex(name = 'V_841',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5769})

V_842 = Vertex(name = 'V_842',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5770})

V_843 = Vertex(name = 'V_843',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_4852,(0,1):C.GC_4870,(0,0):C.GC_4990,(0,3):C.GC_5757})

V_844 = Vertex(name = 'V_844',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5775})

V_845 = Vertex(name = 'V_845',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5776})

V_846 = Vertex(name = 'V_846',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_4854,(0,1):C.GC_4872,(0,0):C.GC_4991,(0,3):C.GC_5742})

V_847 = Vertex(name = 'V_847',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5765})

V_848 = Vertex(name = 'V_848',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5766})

V_849 = Vertex(name = 'V_849',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_4856,(0,1):C.GC_4874,(0,0):C.GC_4992,(0,3):C.GC_5751})

V_850 = Vertex(name = 'V_850',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5771})

V_851 = Vertex(name = 'V_851',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5772})

V_852 = Vertex(name = 'V_852',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV12, L.FFV4, L.FFV5 ],
               couplings = {(0,2):C.GC_4858,(0,1):C.GC_4876,(0,0):C.GC_4993,(0,3):C.GC_5760})

V_853 = Vertex(name = 'V_853',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5777})

V_854 = Vertex(name = 'V_854',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_5778})

V_855 = Vertex(name = 'V_855',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_3757,(0,1):C.GC_5734})

V_856 = Vertex(name = 'V_856',
               particles = [ P.c__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_3758,(0,1):C.GC_5743})

V_857 = Vertex(name = 'V_857',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_3759,(0,1):C.GC_5752})

V_858 = Vertex(name = 'V_858',
               particles = [ P.u__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_3760,(0,1):C.GC_5737})

V_859 = Vertex(name = 'V_859',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_3761,(0,1):C.GC_5746})

V_860 = Vertex(name = 'V_860',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_3762,(0,1):C.GC_5755})

V_861 = Vertex(name = 'V_861',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_3763,(0,1):C.GC_5740})

V_862 = Vertex(name = 'V_862',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_3764,(0,1):C.GC_5749})

V_863 = Vertex(name = 'V_863',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_3765,(0,1):C.GC_5758})

V_864 = Vertex(name = 'V_864',
               particles = [ P.u__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,1):C.GC_3766,(0,3):C.GC_3784,(0,0):C.GC_4833,(0,2):C.GC_5735})

V_865 = Vertex(name = 'V_865',
               particles = [ P.c__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,1):C.GC_3768,(0,3):C.GC_3786,(0,0):C.GC_4834,(0,2):C.GC_5744})

V_866 = Vertex(name = 'V_866',
               particles = [ P.t__tilde__, P.d, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,1):C.GC_3770,(0,3):C.GC_3788,(0,0):C.GC_4835,(0,2):C.GC_5753})

V_867 = Vertex(name = 'V_867',
               particles = [ P.u__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,1):C.GC_3772,(0,3):C.GC_3790,(0,0):C.GC_4836,(0,2):C.GC_5738})

V_868 = Vertex(name = 'V_868',
               particles = [ P.c__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,1):C.GC_3774,(0,3):C.GC_3792,(0,0):C.GC_4837,(0,2):C.GC_5747})

V_869 = Vertex(name = 'V_869',
               particles = [ P.t__tilde__, P.s, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,1):C.GC_3776,(0,3):C.GC_3794,(0,0):C.GC_4838,(0,2):C.GC_5756})

V_870 = Vertex(name = 'V_870',
               particles = [ P.u__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,1):C.GC_3778,(0,3):C.GC_3796,(0,0):C.GC_4839,(0,2):C.GC_5741})

V_871 = Vertex(name = 'V_871',
               particles = [ P.c__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,1):C.GC_3780,(0,3):C.GC_3798,(0,0):C.GC_4840,(0,2):C.GC_5750})

V_872 = Vertex(name = 'V_872',
               particles = [ P.t__tilde__, P.b, P.W__plus__, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS4, L.FFVS6, L.FFVS9 ],
               couplings = {(0,1):C.GC_3782,(0,3):C.GC_3800,(0,0):C.GC_4841,(0,2):C.GC_5759})

V_873 = Vertex(name = 'V_873',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,1):C.GC_5487,(0,0):C.GC_3})

V_874 = Vertex(name = 'V_874',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_19})

V_875 = Vertex(name = 'V_875',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4958})

V_876 = Vertex(name = 'V_876',
               particles = [ P.vm__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,1):C.GC_5532,(0,0):C.GC_4959})

V_877 = Vertex(name = 'V_877',
               particles = [ P.vt__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,1):C.GC_5577,(0,0):C.GC_4960})

V_878 = Vertex(name = 'V_878',
               particles = [ P.ve__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,1):C.GC_5502,(0,0):C.GC_5655})

V_879 = Vertex(name = 'V_879',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,1):C.GC_5547,(0,0):C.GC_3})

V_880 = Vertex(name = 'V_880',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_19})

V_881 = Vertex(name = 'V_881',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4961})

V_882 = Vertex(name = 'V_882',
               particles = [ P.vt__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,1):C.GC_5592,(0,0):C.GC_4962})

V_883 = Vertex(name = 'V_883',
               particles = [ P.ve__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,1):C.GC_5517,(0,0):C.GC_5670})

V_884 = Vertex(name = 'V_884',
               particles = [ P.vm__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,1):C.GC_5562,(0,0):C.GC_5685})

V_885 = Vertex(name = 'V_885',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV4 ],
               couplings = {(0,1):C.GC_5607,(0,0):C.GC_3})

V_886 = Vertex(name = 'V_886',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_19})

V_887 = Vertex(name = 'V_887',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_4963})

V_888 = Vertex(name = 'V_888',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2447})

V_889 = Vertex(name = 'V_889',
               particles = [ P.vm__tilde__, P.e__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2448})

V_890 = Vertex(name = 'V_890',
               particles = [ P.vt__tilde__, P.e__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2449})

V_891 = Vertex(name = 'V_891',
               particles = [ P.ve__tilde__, P.mu__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_5653})

V_892 = Vertex(name = 'V_892',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2450})

V_893 = Vertex(name = 'V_893',
               particles = [ P.vt__tilde__, P.mu__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2451})

V_894 = Vertex(name = 'V_894',
               particles = [ P.ve__tilde__, P.ta__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_5668})

V_895 = Vertex(name = 'V_895',
               particles = [ P.vm__tilde__, P.ta__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_5683})

V_896 = Vertex(name = 'V_896',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1 ],
               couplings = {(0,0):C.GC_2452})

V_897 = Vertex(name = 'V_897',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS5 ],
               couplings = {(0,2):C.GC_5483,(0,1):C.GC_5482,(0,0):C.GC_4749})

V_898 = Vertex(name = 'V_898',
               particles = [ P.vm__tilde__, P.e__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3 ],
               couplings = {(0,2):C.GC_5528,(0,1):C.GC_5527,(0,0):C.GC_4750})

V_899 = Vertex(name = 'V_899',
               particles = [ P.vt__tilde__, P.e__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3 ],
               couplings = {(0,2):C.GC_5573,(0,1):C.GC_5572,(0,0):C.GC_4751})

V_900 = Vertex(name = 'V_900',
               particles = [ P.ve__tilde__, P.mu__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3 ],
               couplings = {(0,2):C.GC_5498,(0,1):C.GC_5497,(0,0):C.GC_5654})

V_901 = Vertex(name = 'V_901',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3 ],
               couplings = {(0,2):C.GC_5543,(0,1):C.GC_5542,(0,0):C.GC_4752})

V_902 = Vertex(name = 'V_902',
               particles = [ P.vt__tilde__, P.mu__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3 ],
               couplings = {(0,2):C.GC_5588,(0,1):C.GC_5587,(0,0):C.GC_4753})

V_903 = Vertex(name = 'V_903',
               particles = [ P.ve__tilde__, P.ta__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3 ],
               couplings = {(0,2):C.GC_5513,(0,1):C.GC_5512,(0,0):C.GC_5669})

V_904 = Vertex(name = 'V_904',
               particles = [ P.vm__tilde__, P.ta__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3 ],
               couplings = {(0,2):C.GC_5558,(0,1):C.GC_5557,(0,0):C.GC_5684})

V_905 = Vertex(name = 'V_905',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3 ],
               couplings = {(0,2):C.GC_5603,(0,1):C.GC_5602,(0,0):C.GC_4754})

V_906 = Vertex(name = 'V_906',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_4447,(0,5):C.GC_5244,(0,4):C.GC_5388,(0,2):C.GC_4998,(0,3):C.GC_5389,(0,1):C.GC_4999})

V_907 = Vertex(name = 'V_907',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,0):C.GC_4452,(0,1):C.GC_4362})

V_908 = Vertex(name = 'V_908',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,0):C.GC_5274,(0,1):C.GC_4368})

V_909 = Vertex(name = 'V_909',
               particles = [ P.s__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_5232,(0,5):C.GC_5187,(0,4):C.GC_5412,(0,2):C.GC_5000,(0,3):C.GC_5413,(0,1):C.GC_5001})

V_910 = Vertex(name = 'V_910',
               particles = [ P.b__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_5234,(0,5):C.GC_5188,(0,4):C.GC_5436,(0,2):C.GC_5002,(0,3):C.GC_5437,(0,1):C.GC_5003})

V_911 = Vertex(name = 'V_911',
               particles = [ P.d__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_5236,(0,5):C.GC_5621,(0,4):C.GC_5396,(0,2):C.GC_5004,(0,3):C.GC_5397,(0,1):C.GC_5005})

V_912 = Vertex(name = 'V_912',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_4447,(0,5):C.GC_5245,(0,4):C.GC_5420,(0,2):C.GC_5006,(0,3):C.GC_5421,(0,1):C.GC_5007})

V_913 = Vertex(name = 'V_913',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,0):C.GC_4452,(0,1):C.GC_4362})

V_914 = Vertex(name = 'V_914',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,0):C.GC_5275,(0,1):C.GC_4368})

V_915 = Vertex(name = 'V_915',
               particles = [ P.b__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_5238,(0,5):C.GC_5189,(0,4):C.GC_5444,(0,2):C.GC_5008,(0,3):C.GC_5445,(0,1):C.GC_5009})

V_916 = Vertex(name = 'V_916',
               particles = [ P.d__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_5240,(0,5):C.GC_5627,(0,4):C.GC_5404,(0,2):C.GC_5010,(0,3):C.GC_5405,(0,1):C.GC_5011})

V_917 = Vertex(name = 'V_917',
               particles = [ P.s__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_5242,(0,5):C.GC_5633,(0,4):C.GC_5428,(0,2):C.GC_5012,(0,3):C.GC_5429,(0,1):C.GC_5013})

V_918 = Vertex(name = 'V_918',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_4447,(0,5):C.GC_5246,(0,4):C.GC_5452,(0,2):C.GC_5014,(0,3):C.GC_5453,(0,1):C.GC_5015})

V_919 = Vertex(name = 'V_919',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,0):C.GC_4452,(0,1):C.GC_4362})

V_920 = Vertex(name = 'V_920',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,0):C.GC_5276,(0,1):C.GC_4368})

V_921 = Vertex(name = 'V_921',
               particles = [ P.d__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4608,(0,1):C.GC_4536})

V_922 = Vertex(name = 'V_922',
               particles = [ P.s__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4610,(0,1):C.GC_4537})

V_923 = Vertex(name = 'V_923',
               particles = [ P.b__tilde__, P.d, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4612,(0,1):C.GC_4538})

V_924 = Vertex(name = 'V_924',
               particles = [ P.d__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4614,(0,1):C.GC_5617})

V_925 = Vertex(name = 'V_925',
               particles = [ P.s__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4616,(0,1):C.GC_4539})

V_926 = Vertex(name = 'V_926',
               particles = [ P.b__tilde__, P.s, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4618,(0,1):C.GC_4540})

V_927 = Vertex(name = 'V_927',
               particles = [ P.d__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4620,(0,1):C.GC_5623})

V_928 = Vertex(name = 'V_928',
               particles = [ P.s__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4622,(0,1):C.GC_5629})

V_929 = Vertex(name = 'V_929',
               particles = [ P.b__tilde__, P.b, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4624,(0,1):C.GC_4541})

V_930 = Vertex(name = 'V_930',
               particles = [ P.d__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7, L.FFVS8 ],
               couplings = {(0,0):C.GC_5151,(0,3):C.GC_5079,(0,2):C.GC_5385,(0,5):C.GC_4456,(0,1):C.GC_5386,(0,4):C.GC_4457})

V_931 = Vertex(name = 'V_931',
               particles = [ P.s__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7, L.FFVS8 ],
               couplings = {(0,0):C.GC_5153,(0,3):C.GC_5080,(0,2):C.GC_5409,(0,5):C.GC_4458,(0,1):C.GC_5410,(0,4):C.GC_4459})

V_932 = Vertex(name = 'V_932',
               particles = [ P.b__tilde__, P.d, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7, L.FFVS8 ],
               couplings = {(0,0):C.GC_5155,(0,3):C.GC_5081,(0,2):C.GC_5433,(0,5):C.GC_4460,(0,1):C.GC_5434,(0,4):C.GC_4461})

V_933 = Vertex(name = 'V_933',
               particles = [ P.d__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7, L.FFVS8 ],
               couplings = {(0,0):C.GC_5157,(0,3):C.GC_5619,(0,2):C.GC_5393,(0,5):C.GC_4462,(0,1):C.GC_5394,(0,4):C.GC_4463})

V_934 = Vertex(name = 'V_934',
               particles = [ P.s__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7, L.FFVS8 ],
               couplings = {(0,0):C.GC_5159,(0,3):C.GC_5082,(0,2):C.GC_5417,(0,5):C.GC_4464,(0,1):C.GC_5418,(0,4):C.GC_4465})

V_935 = Vertex(name = 'V_935',
               particles = [ P.b__tilde__, P.s, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7, L.FFVS8 ],
               couplings = {(0,0):C.GC_5161,(0,3):C.GC_5083,(0,2):C.GC_5441,(0,5):C.GC_4466,(0,1):C.GC_5442,(0,4):C.GC_4467})

V_936 = Vertex(name = 'V_936',
               particles = [ P.d__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7, L.FFVS8 ],
               couplings = {(0,0):C.GC_5163,(0,3):C.GC_5625,(0,2):C.GC_5401,(0,5):C.GC_4468,(0,1):C.GC_5402,(0,4):C.GC_4469})

V_937 = Vertex(name = 'V_937',
               particles = [ P.s__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7, L.FFVS8 ],
               couplings = {(0,0):C.GC_5165,(0,3):C.GC_5631,(0,2):C.GC_5425,(0,5):C.GC_4470,(0,1):C.GC_5426,(0,4):C.GC_4471})

V_938 = Vertex(name = 'V_938',
               particles = [ P.b__tilde__, P.b, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7, L.FFVS8 ],
               couplings = {(0,0):C.GC_5167,(0,3):C.GC_5084,(0,2):C.GC_5449,(0,5):C.GC_4472,(0,1):C.GC_5450,(0,4):C.GC_4473})

V_939 = Vertex(name = 'V_939',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_4449,(0,5):C.GC_5250,(0,4):C.GC_5494,(0,2):C.GC_5025,(0,3):C.GC_5495,(0,1):C.GC_5026})

V_940 = Vertex(name = 'V_940',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,0):C.GC_4454,(0,1):C.GC_4364})

V_941 = Vertex(name = 'V_941',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,0):C.GC_5277,(0,1):C.GC_4370})

V_942 = Vertex(name = 'V_942',
               particles = [ P.mu__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_5194,(0,5):C.GC_5190,(0,4):C.GC_5539,(0,2):C.GC_5027,(0,3):C.GC_5540,(0,1):C.GC_5028})

V_943 = Vertex(name = 'V_943',
               particles = [ P.ta__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_5196,(0,5):C.GC_5191,(0,4):C.GC_5584,(0,2):C.GC_5029,(0,3):C.GC_5585,(0,1):C.GC_5030})

V_944 = Vertex(name = 'V_944',
               particles = [ P.e__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_5665,(0,5):C.GC_5639,(0,4):C.GC_5509,(0,2):C.GC_5031,(0,3):C.GC_5510,(0,1):C.GC_5032})

V_945 = Vertex(name = 'V_945',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_4449,(0,5):C.GC_5251,(0,4):C.GC_5554,(0,2):C.GC_5033,(0,3):C.GC_5555,(0,1):C.GC_5034})

V_946 = Vertex(name = 'V_946',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,0):C.GC_4454,(0,1):C.GC_4364})

V_947 = Vertex(name = 'V_947',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,0):C.GC_5278,(0,1):C.GC_4370})

V_948 = Vertex(name = 'V_948',
               particles = [ P.ta__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_5198,(0,5):C.GC_5192,(0,4):C.GC_5599,(0,2):C.GC_5035,(0,3):C.GC_5600,(0,1):C.GC_5036})

V_949 = Vertex(name = 'V_949',
               particles = [ P.e__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_5680,(0,5):C.GC_5645,(0,4):C.GC_5524,(0,2):C.GC_5037,(0,3):C.GC_5525,(0,1):C.GC_5038})

V_950 = Vertex(name = 'V_950',
               particles = [ P.mu__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_5695,(0,5):C.GC_5651,(0,4):C.GC_5569,(0,2):C.GC_5039,(0,3):C.GC_5570,(0,1):C.GC_5040})

V_951 = Vertex(name = 'V_951',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_4449,(0,5):C.GC_5252,(0,4):C.GC_5614,(0,2):C.GC_5041,(0,3):C.GC_5615,(0,1):C.GC_5042})

V_952 = Vertex(name = 'V_952',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,0):C.GC_4454,(0,1):C.GC_4364})

V_953 = Vertex(name = 'V_953',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,0):C.GC_5279,(0,1):C.GC_4370})

V_954 = Vertex(name = 'V_954',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4549,(0,1):C.GC_4542})

V_955 = Vertex(name = 'V_955',
               particles = [ P.mu__plus__, P.e__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4551,(0,1):C.GC_4543})

V_956 = Vertex(name = 'V_956',
               particles = [ P.ta__plus__, P.e__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4553,(0,1):C.GC_4544})

V_957 = Vertex(name = 'V_957',
               particles = [ P.e__plus__, P.mu__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_5657,(0,1):C.GC_5635})

V_958 = Vertex(name = 'V_958',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4555,(0,1):C.GC_4545})

V_959 = Vertex(name = 'V_959',
               particles = [ P.ta__plus__, P.mu__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4557,(0,1):C.GC_4546})

V_960 = Vertex(name = 'V_960',
               particles = [ P.e__plus__, P.ta__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_5672,(0,1):C.GC_5641})

V_961 = Vertex(name = 'V_961',
               particles = [ P.mu__plus__, P.ta__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_5687,(0,1):C.GC_5647})

V_962 = Vertex(name = 'V_962',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4559,(0,1):C.GC_4547})

V_963 = Vertex(name = 'V_963',
               particles = [ P.e__plus__, P.e__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7, L.FFVS8 ],
               couplings = {(0,0):C.GC_5092,(0,3):C.GC_5085,(0,2):C.GC_5491,(0,5):C.GC_4483,(0,1):C.GC_5492,(0,4):C.GC_4484})

V_964 = Vertex(name = 'V_964',
               particles = [ P.mu__plus__, P.e__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7, L.FFVS8 ],
               couplings = {(0,0):C.GC_5094,(0,3):C.GC_5086,(0,2):C.GC_5536,(0,5):C.GC_4485,(0,1):C.GC_5537,(0,4):C.GC_4486})

V_965 = Vertex(name = 'V_965',
               particles = [ P.ta__plus__, P.e__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7, L.FFVS8 ],
               couplings = {(0,0):C.GC_5096,(0,3):C.GC_5087,(0,2):C.GC_5581,(0,5):C.GC_4487,(0,1):C.GC_5582,(0,4):C.GC_4488})

V_966 = Vertex(name = 'V_966',
               particles = [ P.e__plus__, P.mu__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7, L.FFVS8 ],
               couplings = {(0,0):C.GC_5661,(0,3):C.GC_5637,(0,2):C.GC_5506,(0,5):C.GC_4489,(0,1):C.GC_5507,(0,4):C.GC_4490})

V_967 = Vertex(name = 'V_967',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS10, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7, L.FFVS8 ],
               couplings = {(0,0):C.GC_5098,(0,4):C.GC_5088,(0,3):C.GC_5551,(0,6):C.GC_4491,(0,1):C.GC_2394,(0,5):C.GC_4376,(0,2):C.GC_5552})

V_968 = Vertex(name = 'V_968',
               particles = [ P.ta__plus__, P.mu__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7, L.FFVS8 ],
               couplings = {(0,0):C.GC_5100,(0,3):C.GC_5089,(0,2):C.GC_5596,(0,5):C.GC_4492,(0,1):C.GC_5597,(0,4):C.GC_4493})

V_969 = Vertex(name = 'V_969',
               particles = [ P.e__plus__, P.ta__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7, L.FFVS8 ],
               couplings = {(0,0):C.GC_5676,(0,3):C.GC_5643,(0,2):C.GC_5521,(0,5):C.GC_4494,(0,1):C.GC_5522,(0,4):C.GC_4495})

V_970 = Vertex(name = 'V_970',
               particles = [ P.mu__plus__, P.ta__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7, L.FFVS8 ],
               couplings = {(0,0):C.GC_5691,(0,3):C.GC_5649,(0,2):C.GC_5566,(0,5):C.GC_4496,(0,1):C.GC_5567,(0,4):C.GC_4497})

V_971 = Vertex(name = 'V_971',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7, L.FFVS8 ],
               couplings = {(0,0):C.GC_5102,(0,3):C.GC_5090,(0,2):C.GC_5611,(0,5):C.GC_4498,(0,1):C.GC_5612,(0,4):C.GC_4499})

V_972 = Vertex(name = 'V_972',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_4446,(0,5):C.GC_5247,(0,4):C.GC_6172,(0,2):C.GC_5052,(0,3):C.GC_6171,(0,1):C.GC_5053})

V_973 = Vertex(name = 'V_973',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,0):C.GC_4451,(0,1):C.GC_4363})

V_974 = Vertex(name = 'V_974',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,0):C.GC_5268,(0,1):C.GC_4369})

V_975 = Vertex(name = 'V_975',
               particles = [ P.c__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_5199,(0,5):C.GC_5202,(0,4):C.GC_6196,(0,2):C.GC_5054,(0,3):C.GC_6195,(0,1):C.GC_5055})

V_976 = Vertex(name = 'V_976',
               particles = [ P.t__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_5200,(0,5):C.GC_5203,(0,4):C.GC_6220,(0,2):C.GC_5056,(0,3):C.GC_6219,(0,1):C.GC_5057})

V_977 = Vertex(name = 'V_977',
               particles = [ P.u__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_5702,(0,5):C.GC_5720,(0,4):C.GC_6180,(0,2):C.GC_5058,(0,3):C.GC_6179,(0,1):C.GC_5059})

V_978 = Vertex(name = 'V_978',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_4446,(0,5):C.GC_5248,(0,4):C.GC_6204,(0,2):C.GC_5060,(0,3):C.GC_6203,(0,1):C.GC_5061})

V_979 = Vertex(name = 'V_979',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,0):C.GC_4451,(0,1):C.GC_4363})

V_980 = Vertex(name = 'V_980',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,0):C.GC_5269,(0,1):C.GC_4369})

V_981 = Vertex(name = 'V_981',
               particles = [ P.t__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_5201,(0,5):C.GC_5204,(0,4):C.GC_6228,(0,2):C.GC_5062,(0,3):C.GC_6227,(0,1):C.GC_5063})

V_982 = Vertex(name = 'V_982',
               particles = [ P.u__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_5708,(0,5):C.GC_5726,(0,4):C.GC_6188,(0,2):C.GC_5064,(0,3):C.GC_6187,(0,1):C.GC_5065})

V_983 = Vertex(name = 'V_983',
               particles = [ P.c__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_5714,(0,5):C.GC_5732,(0,4):C.GC_6212,(0,2):C.GC_5066,(0,3):C.GC_6211,(0,1):C.GC_5067})

V_984 = Vertex(name = 'V_984',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV10, L.FFV11, L.FFV2, L.FFV3, L.FFV5 ],
               couplings = {(0,0):C.GC_4446,(0,5):C.GC_5249,(0,4):C.GC_6236,(0,2):C.GC_5068,(0,3):C.GC_6235,(0,1):C.GC_5069})

V_985 = Vertex(name = 'V_985',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,0):C.GC_4451,(0,1):C.GC_4363})

V_986 = Vertex(name = 'V_986',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1, L.FFV5 ],
               couplings = {(0,0):C.GC_5270,(0,1):C.GC_4369})

V_987 = Vertex(name = 'V_987',
               particles = [ P.u__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4560,(0,1):C.GC_4566})

V_988 = Vertex(name = 'V_988',
               particles = [ P.c__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4561,(0,1):C.GC_4567})

V_989 = Vertex(name = 'V_989',
               particles = [ P.t__tilde__, P.u, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4562,(0,1):C.GC_4568})

V_990 = Vertex(name = 'V_990',
               particles = [ P.u__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_5698,(0,1):C.GC_5716})

V_991 = Vertex(name = 'V_991',
               particles = [ P.c__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4563,(0,1):C.GC_4569})

V_992 = Vertex(name = 'V_992',
               particles = [ P.t__tilde__, P.c, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4564,(0,1):C.GC_4570})

V_993 = Vertex(name = 'V_993',
               particles = [ P.u__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_5704,(0,1):C.GC_5722})

V_994 = Vertex(name = 'V_994',
               particles = [ P.c__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_5710,(0,1):C.GC_5728})

V_995 = Vertex(name = 'V_995',
               particles = [ P.t__tilde__, P.t, P.Z, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVSS1, L.FFVSS2 ],
               couplings = {(0,0):C.GC_4565,(0,1):C.GC_4571})

V_996 = Vertex(name = 'V_996',
               particles = [ P.u__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7, L.FFVS8 ],
               couplings = {(0,0):C.GC_5103,(0,3):C.GC_5109,(0,2):C.GC_6169,(0,5):C.GC_4509,(0,1):C.GC_6168,(0,4):C.GC_4510})

V_997 = Vertex(name = 'V_997',
               particles = [ P.c__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7, L.FFVS8 ],
               couplings = {(0,0):C.GC_5104,(0,3):C.GC_5110,(0,2):C.GC_6193,(0,5):C.GC_4511,(0,1):C.GC_6192,(0,4):C.GC_4512})

V_998 = Vertex(name = 'V_998',
               particles = [ P.t__tilde__, P.u, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7, L.FFVS8 ],
               couplings = {(0,0):C.GC_5105,(0,3):C.GC_5111,(0,2):C.GC_6217,(0,5):C.GC_4513,(0,1):C.GC_6216,(0,4):C.GC_4514})

V_999 = Vertex(name = 'V_999',
               particles = [ P.u__tilde__, P.c, P.Z, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7, L.FFVS8 ],
               couplings = {(0,0):C.GC_5700,(0,3):C.GC_5718,(0,2):C.GC_6177,(0,5):C.GC_4515,(0,1):C.GC_6176,(0,4):C.GC_4516})

V_1000 = Vertex(name = 'V_1000',
                particles = [ P.c__tilde__, P.c, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7, L.FFVS8 ],
                couplings = {(0,0):C.GC_5106,(0,3):C.GC_5112,(0,2):C.GC_6201,(0,5):C.GC_4517,(0,1):C.GC_6200,(0,4):C.GC_4518})

V_1001 = Vertex(name = 'V_1001',
                particles = [ P.t__tilde__, P.c, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7, L.FFVS8 ],
                couplings = {(0,0):C.GC_5107,(0,3):C.GC_5113,(0,2):C.GC_6225,(0,5):C.GC_4519,(0,1):C.GC_6224,(0,4):C.GC_4520})

V_1002 = Vertex(name = 'V_1002',
                particles = [ P.u__tilde__, P.t, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7, L.FFVS8 ],
                couplings = {(0,0):C.GC_5706,(0,3):C.GC_5724,(0,2):C.GC_6185,(0,5):C.GC_4521,(0,1):C.GC_6184,(0,4):C.GC_4522})

V_1003 = Vertex(name = 'V_1003',
                particles = [ P.c__tilde__, P.t, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7, L.FFVS8 ],
                couplings = {(0,0):C.GC_5712,(0,3):C.GC_5730,(0,2):C.GC_6209,(0,5):C.GC_4523,(0,1):C.GC_6208,(0,4):C.GC_4524})

V_1004 = Vertex(name = 'V_1004',
                particles = [ P.t__tilde__, P.t, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVS1, L.FFVS2, L.FFVS3, L.FFVS6, L.FFVS7, L.FFVS8 ],
                couplings = {(0,0):C.GC_5108,(0,3):C.GC_5114,(0,2):C.GC_6233,(0,5):C.GC_4525,(0,1):C.GC_6232,(0,4):C.GC_4526})

V_1005 = Vertex(name = 'V_1005',
                particles = [ P.ve__tilde__, P.ve, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_4448})

V_1006 = Vertex(name = 'V_1006',
                particles = [ P.ve__tilde__, P.ve, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_4453})

V_1007 = Vertex(name = 'V_1007',
                particles = [ P.ve__tilde__, P.ve, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_5271})

V_1008 = Vertex(name = 'V_1008',
                particles = [ P.vm__tilde__, P.ve, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_5193})

V_1009 = Vertex(name = 'V_1009',
                particles = [ P.vt__tilde__, P.ve, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_5195})

V_1010 = Vertex(name = 'V_1010',
                particles = [ P.ve__tilde__, P.vm, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_5664})

V_1011 = Vertex(name = 'V_1011',
                particles = [ P.vm__tilde__, P.vm, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_4448})

V_1012 = Vertex(name = 'V_1012',
                particles = [ P.vm__tilde__, P.vm, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_4453})

V_1013 = Vertex(name = 'V_1013',
                particles = [ P.vm__tilde__, P.vm, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_5272})

V_1014 = Vertex(name = 'V_1014',
                particles = [ P.vt__tilde__, P.vm, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_5197})

V_1015 = Vertex(name = 'V_1015',
                particles = [ P.ve__tilde__, P.vt, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_5679})

V_1016 = Vertex(name = 'V_1016',
                particles = [ P.vm__tilde__, P.vt, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_5694})

V_1017 = Vertex(name = 'V_1017',
                particles = [ P.vt__tilde__, P.vt, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_4448})

V_1018 = Vertex(name = 'V_1018',
                particles = [ P.vt__tilde__, P.vt, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_4453})

V_1019 = Vertex(name = 'V_1019',
                particles = [ P.vt__tilde__, P.vt, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFV1 ],
                couplings = {(0,0):C.GC_5273})

V_1020 = Vertex(name = 'V_1020',
                particles = [ P.ve__tilde__, P.ve, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVSS1 ],
                couplings = {(0,0):C.GC_4548})

V_1021 = Vertex(name = 'V_1021',
                particles = [ P.vm__tilde__, P.ve, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVSS1 ],
                couplings = {(0,0):C.GC_4550})

V_1022 = Vertex(name = 'V_1022',
                particles = [ P.vt__tilde__, P.ve, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVSS1 ],
                couplings = {(0,0):C.GC_4552})

V_1023 = Vertex(name = 'V_1023',
                particles = [ P.ve__tilde__, P.vm, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVSS1 ],
                couplings = {(0,0):C.GC_5656})

V_1024 = Vertex(name = 'V_1024',
                particles = [ P.vm__tilde__, P.vm, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVSS1 ],
                couplings = {(0,0):C.GC_4554})

V_1025 = Vertex(name = 'V_1025',
                particles = [ P.vt__tilde__, P.vm, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVSS1 ],
                couplings = {(0,0):C.GC_4556})

V_1026 = Vertex(name = 'V_1026',
                particles = [ P.ve__tilde__, P.vt, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVSS1 ],
                couplings = {(0,0):C.GC_5671})

V_1027 = Vertex(name = 'V_1027',
                particles = [ P.vm__tilde__, P.vt, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVSS1 ],
                couplings = {(0,0):C.GC_5686})

V_1028 = Vertex(name = 'V_1028',
                particles = [ P.vt__tilde__, P.vt, P.Z, P.H, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVSS1 ],
                couplings = {(0,0):C.GC_4558})

V_1029 = Vertex(name = 'V_1029',
                particles = [ P.ve__tilde__, P.ve, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS1 ],
                couplings = {(0,0):C.GC_5091})

V_1030 = Vertex(name = 'V_1030',
                particles = [ P.vm__tilde__, P.ve, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS1 ],
                couplings = {(0,0):C.GC_5093})

V_1031 = Vertex(name = 'V_1031',
                particles = [ P.vt__tilde__, P.ve, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS1 ],
                couplings = {(0,0):C.GC_5095})

V_1032 = Vertex(name = 'V_1032',
                particles = [ P.ve__tilde__, P.vm, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS1 ],
                couplings = {(0,0):C.GC_5660})

V_1033 = Vertex(name = 'V_1033',
                particles = [ P.vm__tilde__, P.vm, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS1 ],
                couplings = {(0,0):C.GC_5097})

V_1034 = Vertex(name = 'V_1034',
                particles = [ P.vt__tilde__, P.vm, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS1 ],
                couplings = {(0,0):C.GC_5099})

V_1035 = Vertex(name = 'V_1035',
                particles = [ P.ve__tilde__, P.vt, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS1 ],
                couplings = {(0,0):C.GC_5675})

V_1036 = Vertex(name = 'V_1036',
                particles = [ P.vm__tilde__, P.vt, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS1 ],
                couplings = {(0,0):C.GC_5690})

V_1037 = Vertex(name = 'V_1037',
                particles = [ P.vt__tilde__, P.vt, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVS1 ],
                couplings = {(0,0):C.GC_5101})

V_1038 = Vertex(name = 'V_1038',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_639,(0,7):C.GC_630,(0,0):C.GC_3901,(2,0):C.GC_3910,(1,3):C.GC_3883,(3,3):C.GC_3892,(1,1):C.GC_4018,(3,1):C.GC_4027,(1,2):C.GC_999,(0,4):C.GC_3919,(2,4):C.GC_3928,(0,5):C.GC_999})

V_1039 = Vertex(name = 'V_1039',
                particles = [ P.s__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_640,(0,7):C.GC_644,(0,0):C.GC_702,(2,0):C.GC_720,(1,3):C.GC_704,(3,3):C.GC_722,(1,1):C.GC_774,(3,1):C.GC_846,(1,2):C.GC_37,(0,4):C.GC_782,(2,4):C.GC_854,(0,5):C.GC_37})

V_1040 = Vertex(name = 'V_1040',
                particles = [ P.b__tilde__, P.d, P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_641,(0,7):C.GC_649,(0,0):C.GC_703,(2,0):C.GC_721,(1,3):C.GC_706,(3,3):C.GC_724,(1,1):C.GC_775,(3,1):C.GC_847,(1,2):C.GC_38,(0,4):C.GC_790,(2,4):C.GC_862,(0,5):C.GC_38})

V_1041 = Vertex(name = 'V_1041',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_642,(0,7):C.GC_654,(0,0):C.GC_798,(2,0):C.GC_870,(1,3):C.GC_744,(3,3):C.GC_762,(1,1):C.GC_776,(3,1):C.GC_848,(1,2):C.GC_40,(0,4):C.GC_738,(2,4):C.GC_756,(0,5):C.GC_40})

V_1042 = Vertex(name = 'V_1042',
                particles = [ P.s__tilde__, P.d, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_661,(0,7):C.GC_655,(0,0):C.GC_799,(2,0):C.GC_871,(1,3):C.GC_806,(3,3):C.GC_878,(1,1):C.GC_777,(3,1):C.GC_849,(1,2):C.GC_43,(0,4):C.GC_784,(2,4):C.GC_856,(0,5):C.GC_41})

V_1043 = Vertex(name = 'V_1043',
                particles = [ P.b__tilde__, P.d, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_668,(0,7):C.GC_656,(0,0):C.GC_800,(2,0):C.GC_872,(1,3):C.GC_814,(3,3):C.GC_886,(1,1):C.GC_778,(3,1):C.GC_850,(1,2):C.GC_47,(0,4):C.GC_792,(2,4):C.GC_864,(0,5):C.GC_42})

V_1044 = Vertex(name = 'V_1044',
                particles = [ P.d__tilde__, P.d, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_643,(0,7):C.GC_675,(0,0):C.GC_822,(2,0):C.GC_894,(1,3):C.GC_750,(3,3):C.GC_768,(1,1):C.GC_779,(3,1):C.GC_851,(1,2):C.GC_52,(0,4):C.GC_739,(2,4):C.GC_757,(0,5):C.GC_52})

V_1045 = Vertex(name = 'V_1045',
                particles = [ P.s__tilde__, P.d, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_684,(0,7):C.GC_676,(0,0):C.GC_823,(2,0):C.GC_895,(1,3):C.GC_830,(3,3):C.GC_902,(1,1):C.GC_780,(3,1):C.GC_852,(1,2):C.GC_58,(0,4):C.GC_787,(2,4):C.GC_859,(0,5):C.GC_53})

V_1046 = Vertex(name = 'V_1046',
                particles = [ P.b__tilde__, P.d, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_693,(0,7):C.GC_677,(0,0):C.GC_824,(2,0):C.GC_896,(1,3):C.GC_838,(3,3):C.GC_910,(1,1):C.GC_781,(3,1):C.GC_853,(1,2):C.GC_65,(0,4):C.GC_795,(2,4):C.GC_867,(0,5):C.GC_54})

V_1047 = Vertex(name = 'V_1047',
                particles = [ P.s__tilde__, P.d, P.s__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_645,(0,7):C.GC_631,(0,0):C.GC_3902,(2,0):C.GC_3911,(1,3):C.GC_3884,(3,3):C.GC_3893,(1,1):C.GC_4019,(3,1):C.GC_4028,(1,2):C.GC_1000,(0,4):C.GC_3920,(2,4):C.GC_3929,(0,5):C.GC_1000})

V_1048 = Vertex(name = 'V_1048',
                particles = [ P.b__tilde__, P.d, P.s__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_646,(0,7):C.GC_650,(0,0):C.GC_705,(2,0):C.GC_723,(1,3):C.GC_707,(3,3):C.GC_725,(1,1):C.GC_783,(3,1):C.GC_855,(1,2):C.GC_39,(0,4):C.GC_791,(2,4):C.GC_863,(0,5):C.GC_39})

V_1049 = Vertex(name = 'V_1049',
                particles = [ P.s__tilde__, P.d, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_647,(0,7):C.GC_662,(0,0):C.GC_807,(2,0):C.GC_879,(1,3):C.GC_746,(3,3):C.GC_764,(1,1):C.GC_785,(3,1):C.GC_857,(1,2):C.GC_44,(0,4):C.GC_740,(2,4):C.GC_758,(0,5):C.GC_44})

V_1050 = Vertex(name = 'V_1050',
                particles = [ P.b__tilde__, P.d, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_669,(0,7):C.GC_663,(0,0):C.GC_808,(2,0):C.GC_880,(1,3):C.GC_815,(3,3):C.GC_887,(1,1):C.GC_786,(3,1):C.GC_858,(1,2):C.GC_48,(0,4):C.GC_793,(2,4):C.GC_865,(0,5):C.GC_45})

V_1051 = Vertex(name = 'V_1051',
                particles = [ P.s__tilde__, P.d, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_648,(0,7):C.GC_685,(0,0):C.GC_831,(2,0):C.GC_903,(1,3):C.GC_752,(3,3):C.GC_770,(1,1):C.GC_788,(3,1):C.GC_860,(1,2):C.GC_59,(0,4):C.GC_741,(2,4):C.GC_759,(0,5):C.GC_59})

V_1052 = Vertex(name = 'V_1052',
                particles = [ P.b__tilde__, P.d, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_694,(0,7):C.GC_686,(0,0):C.GC_832,(2,0):C.GC_904,(1,3):C.GC_839,(3,3):C.GC_911,(1,1):C.GC_789,(3,1):C.GC_861,(1,2):C.GC_66,(0,4):C.GC_796,(2,4):C.GC_868,(0,5):C.GC_60})

V_1053 = Vertex(name = 'V_1053',
                particles = [ P.b__tilde__, P.d, P.b__tilde__, P.d ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_651,(0,7):C.GC_632,(0,0):C.GC_3903,(2,0):C.GC_3912,(1,3):C.GC_3885,(3,3):C.GC_3894,(1,1):C.GC_4020,(3,1):C.GC_4029,(1,2):C.GC_1001,(0,4):C.GC_3921,(2,4):C.GC_3930,(0,5):C.GC_1001})

V_1054 = Vertex(name = 'V_1054',
                particles = [ P.b__tilde__, P.d, P.b__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_652,(0,7):C.GC_670,(0,0):C.GC_816,(2,0):C.GC_888,(1,3):C.GC_748,(3,3):C.GC_766,(1,1):C.GC_794,(3,1):C.GC_866,(1,2):C.GC_49,(0,4):C.GC_742,(2,4):C.GC_760,(0,5):C.GC_49})

V_1055 = Vertex(name = 'V_1055',
                particles = [ P.b__tilde__, P.d, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_653,(0,7):C.GC_695,(0,0):C.GC_840,(2,0):C.GC_912,(1,3):C.GC_754,(3,3):C.GC_772,(1,1):C.GC_797,(3,1):C.GC_869,(1,2):C.GC_67,(0,4):C.GC_743,(2,4):C.GC_761,(0,5):C.GC_67})

V_1056 = Vertex(name = 'V_1056',
                particles = [ P.d__tilde__, P.s, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_657,(0,7):C.GC_633,(0,0):C.GC_3904,(2,0):C.GC_3913,(1,3):C.GC_3886,(3,3):C.GC_3895,(1,1):C.GC_4021,(3,1):C.GC_4030,(1,2):C.GC_1002,(0,4):C.GC_3922,(2,4):C.GC_3931,(0,5):C.GC_1002})

V_1057 = Vertex(name = 'V_1057',
                particles = [ P.s__tilde__, P.s, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_658,(0,7):C.GC_664,(0,0):C.GC_708,(2,0):C.GC_726,(1,3):C.GC_710,(3,3):C.GC_728,(1,1):C.GC_801,(3,1):C.GC_873,(1,2):C.GC_46,(0,4):C.GC_809,(2,4):C.GC_881,(0,5):C.GC_46})

V_1058 = Vertex(name = 'V_1058',
                particles = [ P.b__tilde__, P.s, P.d__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_659,(0,7):C.GC_671,(0,0):C.GC_709,(2,0):C.GC_727,(1,3):C.GC_712,(3,3):C.GC_730,(1,1):C.GC_802,(3,1):C.GC_874,(1,2):C.GC_50,(0,4):C.GC_817,(2,4):C.GC_889,(0,5):C.GC_50})

V_1059 = Vertex(name = 'V_1059',
                particles = [ P.d__tilde__, P.s, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_660,(0,7):C.GC_678,(0,0):C.GC_825,(2,0):C.GC_897,(1,3):C.GC_751,(3,3):C.GC_769,(1,1):C.GC_803,(3,1):C.GC_875,(1,2):C.GC_55,(0,4):C.GC_745,(2,4):C.GC_763,(0,5):C.GC_55})

V_1060 = Vertex(name = 'V_1060',
                particles = [ P.s__tilde__, P.s, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_687,(0,7):C.GC_679,(0,0):C.GC_826,(2,0):C.GC_898,(1,3):C.GC_833,(3,3):C.GC_905,(1,1):C.GC_804,(3,1):C.GC_876,(1,2):C.GC_61,(0,4):C.GC_811,(2,4):C.GC_883,(0,5):C.GC_56})

V_1061 = Vertex(name = 'V_1061',
                particles = [ P.b__tilde__, P.s, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_696,(0,7):C.GC_680,(0,0):C.GC_827,(2,0):C.GC_899,(1,3):C.GC_841,(3,3):C.GC_913,(1,1):C.GC_805,(3,1):C.GC_877,(1,2):C.GC_68,(0,4):C.GC_819,(2,4):C.GC_891,(0,5):C.GC_57})

V_1062 = Vertex(name = 'V_1062',
                particles = [ P.s__tilde__, P.s, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_665,(0,7):C.GC_634,(0,0):C.GC_3905,(2,0):C.GC_3914,(1,3):C.GC_3887,(3,3):C.GC_3896,(1,1):C.GC_4022,(3,1):C.GC_4031,(1,2):C.GC_1003,(0,4):C.GC_3923,(2,4):C.GC_3932,(0,5):C.GC_1003})

V_1063 = Vertex(name = 'V_1063',
                particles = [ P.b__tilde__, P.s, P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_666,(0,7):C.GC_672,(0,0):C.GC_711,(2,0):C.GC_729,(1,3):C.GC_713,(3,3):C.GC_731,(1,1):C.GC_810,(3,1):C.GC_882,(1,2):C.GC_51,(0,4):C.GC_818,(2,4):C.GC_890,(0,5):C.GC_51})

V_1064 = Vertex(name = 'V_1064',
                particles = [ P.s__tilde__, P.s, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_667,(0,7):C.GC_688,(0,0):C.GC_834,(2,0):C.GC_906,(1,3):C.GC_753,(3,3):C.GC_771,(1,1):C.GC_812,(3,1):C.GC_884,(1,2):C.GC_62,(0,4):C.GC_747,(2,4):C.GC_765,(0,5):C.GC_62})

V_1065 = Vertex(name = 'V_1065',
                particles = [ P.b__tilde__, P.s, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_697,(0,7):C.GC_689,(0,0):C.GC_835,(2,0):C.GC_907,(1,3):C.GC_842,(3,3):C.GC_914,(1,1):C.GC_813,(3,1):C.GC_885,(1,2):C.GC_69,(0,4):C.GC_820,(2,4):C.GC_892,(0,5):C.GC_63})

V_1066 = Vertex(name = 'V_1066',
                particles = [ P.b__tilde__, P.s, P.b__tilde__, P.s ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_673,(0,7):C.GC_635,(0,0):C.GC_3906,(2,0):C.GC_3915,(1,3):C.GC_3888,(3,3):C.GC_3897,(1,1):C.GC_4023,(3,1):C.GC_4032,(1,2):C.GC_1004,(0,4):C.GC_3924,(2,4):C.GC_3933,(0,5):C.GC_1004})

V_1067 = Vertex(name = 'V_1067',
                particles = [ P.b__tilde__, P.s, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_674,(0,7):C.GC_698,(0,0):C.GC_843,(2,0):C.GC_915,(1,3):C.GC_755,(3,3):C.GC_773,(1,1):C.GC_821,(3,1):C.GC_893,(1,2):C.GC_70,(0,4):C.GC_749,(2,4):C.GC_767,(0,5):C.GC_70})

V_1068 = Vertex(name = 'V_1068',
                particles = [ P.d__tilde__, P.b, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_681,(0,7):C.GC_636,(0,0):C.GC_3907,(2,0):C.GC_3916,(1,3):C.GC_3889,(3,3):C.GC_3898,(1,1):C.GC_4024,(3,1):C.GC_4033,(1,2):C.GC_1005,(0,4):C.GC_3925,(2,4):C.GC_3934,(0,5):C.GC_1005})

V_1069 = Vertex(name = 'V_1069',
                particles = [ P.s__tilde__, P.b, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_682,(0,7):C.GC_690,(0,0):C.GC_714,(2,0):C.GC_732,(1,3):C.GC_716,(3,3):C.GC_734,(1,1):C.GC_828,(3,1):C.GC_900,(1,2):C.GC_64,(0,4):C.GC_836,(2,4):C.GC_908,(0,5):C.GC_64})

V_1070 = Vertex(name = 'V_1070',
                particles = [ P.b__tilde__, P.b, P.d__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_683,(0,7):C.GC_699,(0,0):C.GC_715,(2,0):C.GC_733,(1,3):C.GC_718,(3,3):C.GC_736,(1,1):C.GC_829,(3,1):C.GC_901,(1,2):C.GC_71,(0,4):C.GC_844,(2,4):C.GC_916,(0,5):C.GC_71})

V_1071 = Vertex(name = 'V_1071',
                particles = [ P.s__tilde__, P.b, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_691,(0,7):C.GC_637,(0,0):C.GC_3908,(2,0):C.GC_3917,(1,3):C.GC_3890,(3,3):C.GC_3899,(1,1):C.GC_4025,(3,1):C.GC_4034,(1,2):C.GC_1006,(0,4):C.GC_3926,(2,4):C.GC_3935,(0,5):C.GC_1006})

V_1072 = Vertex(name = 'V_1072',
                particles = [ P.b__tilde__, P.b, P.s__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_692,(0,7):C.GC_700,(0,0):C.GC_717,(2,0):C.GC_735,(1,3):C.GC_719,(3,3):C.GC_737,(1,1):C.GC_837,(3,1):C.GC_909,(1,2):C.GC_72,(0,4):C.GC_845,(2,4):C.GC_917,(0,5):C.GC_72})

V_1073 = Vertex(name = 'V_1073',
                particles = [ P.b__tilde__, P.b, P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_701,(0,7):C.GC_638,(0,0):C.GC_3909,(2,0):C.GC_3918,(1,3):C.GC_3891,(3,3):C.GC_3900,(1,1):C.GC_4026,(3,1):C.GC_4035,(1,2):C.GC_1007,(0,4):C.GC_3927,(2,4):C.GC_3936,(0,5):C.GC_1007})

V_1074 = Vertex(name = 'V_1074',
                particles = [ P.e__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_1708,(0,7):C.GC_1708,(0,0):C.GC_1303,(0,3):C.GC_1303,(0,1):C.GC_1303,(0,2):C.GC_1107,(0,4):C.GC_1303,(0,5):C.GC_1107})

V_1075 = Vertex(name = 'V_1075',
                particles = [ P.mu__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_110,(0,7):C.GC_110,(0,0):C.GC_1304,(0,3):C.GC_1312,(0,1):C.GC_1304,(0,2):C.GC_73,(0,4):C.GC_1312,(0,5):C.GC_73})

V_1076 = Vertex(name = 'V_1076',
                particles = [ P.ta__plus__, P.e__minus__, P.e__plus__, P.e__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_111,(0,7):C.GC_111,(0,0):C.GC_1305,(0,3):C.GC_1321,(0,1):C.GC_1305,(0,2):C.GC_74,(0,4):C.GC_1321,(0,5):C.GC_74})

V_1077 = Vertex(name = 'V_1077',
                particles = [ P.e__plus__, P.e__minus__, P.e__plus__, P.mu__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_113,(0,7):C.GC_113,(0,0):C.GC_1330,(0,3):C.GC_1330,(0,1):C.GC_1306,(0,2):C.GC_76,(0,4):C.GC_1306,(0,5):C.GC_76})

V_1078 = Vertex(name = 'V_1078',
                particles = [ P.mu__plus__, P.e__minus__, P.e__plus__, P.mu__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_116,(0,7):C.GC_114,(0,0):C.GC_1331,(0,3):C.GC_1339,(0,1):C.GC_1307,(0,2):C.GC_79,(0,4):C.GC_1315,(0,5):C.GC_77})

V_1079 = Vertex(name = 'V_1079',
                particles = [ P.ta__plus__, P.e__minus__, P.e__plus__, P.mu__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_120,(0,7):C.GC_115,(0,0):C.GC_1332,(0,3):C.GC_1348,(0,1):C.GC_1308,(0,2):C.GC_83,(0,4):C.GC_1324,(0,5):C.GC_78})

V_1080 = Vertex(name = 'V_1080',
                particles = [ P.e__plus__, P.e__minus__, P.e__plus__, P.ta__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_125,(0,7):C.GC_125,(0,0):C.GC_1357,(0,3):C.GC_1357,(0,1):C.GC_1309,(0,2):C.GC_88,(0,4):C.GC_1309,(0,5):C.GC_88})

V_1081 = Vertex(name = 'V_1081',
                particles = [ P.mu__plus__, P.e__minus__, P.e__plus__, P.ta__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_131,(0,7):C.GC_126,(0,0):C.GC_1358,(0,3):C.GC_1366,(0,1):C.GC_1310,(0,2):C.GC_94,(0,4):C.GC_1318,(0,5):C.GC_89})

V_1082 = Vertex(name = 'V_1082',
                particles = [ P.ta__plus__, P.e__minus__, P.e__plus__, P.ta__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_138,(0,7):C.GC_127,(0,0):C.GC_1359,(0,3):C.GC_1375,(0,1):C.GC_1311,(0,2):C.GC_101,(0,4):C.GC_1327,(0,5):C.GC_90})

V_1083 = Vertex(name = 'V_1083',
                particles = [ P.mu__plus__, P.e__minus__, P.mu__plus__, P.e__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_1709,(0,7):C.GC_1709,(0,0):C.GC_1313,(0,3):C.GC_1313,(0,1):C.GC_1313,(0,2):C.GC_1108,(0,4):C.GC_1313,(0,5):C.GC_1108})

V_1084 = Vertex(name = 'V_1084',
                particles = [ P.ta__plus__, P.e__minus__, P.mu__plus__, P.e__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_112,(0,7):C.GC_112,(0,0):C.GC_1314,(0,3):C.GC_1322,(0,1):C.GC_1314,(0,2):C.GC_75,(0,4):C.GC_1322,(0,5):C.GC_75})

V_1085 = Vertex(name = 'V_1085',
                particles = [ P.mu__plus__, P.e__minus__, P.mu__plus__, P.mu__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_117,(0,7):C.GC_117,(0,0):C.GC_1340,(0,3):C.GC_1340,(0,1):C.GC_1316,(0,2):C.GC_80,(0,4):C.GC_1316,(0,5):C.GC_80})

V_1086 = Vertex(name = 'V_1086',
                particles = [ P.ta__plus__, P.e__minus__, P.mu__plus__, P.mu__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_121,(0,7):C.GC_118,(0,0):C.GC_1341,(0,3):C.GC_1349,(0,1):C.GC_1317,(0,2):C.GC_84,(0,4):C.GC_1325,(0,5):C.GC_81})

V_1087 = Vertex(name = 'V_1087',
                particles = [ P.mu__plus__, P.e__minus__, P.mu__plus__, P.ta__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_132,(0,7):C.GC_132,(0,0):C.GC_1367,(0,3):C.GC_1367,(0,1):C.GC_1319,(0,2):C.GC_95,(0,4):C.GC_1319,(0,5):C.GC_95})

V_1088 = Vertex(name = 'V_1088',
                particles = [ P.ta__plus__, P.e__minus__, P.mu__plus__, P.ta__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_139,(0,7):C.GC_133,(0,0):C.GC_1368,(0,3):C.GC_1376,(0,1):C.GC_1320,(0,2):C.GC_102,(0,4):C.GC_1328,(0,5):C.GC_96})

V_1089 = Vertex(name = 'V_1089',
                particles = [ P.ta__plus__, P.e__minus__, P.ta__plus__, P.e__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_1710,(0,7):C.GC_1710,(0,0):C.GC_1323,(0,3):C.GC_1323,(0,1):C.GC_1323,(0,2):C.GC_1109,(0,4):C.GC_1323,(0,5):C.GC_1109})

V_1090 = Vertex(name = 'V_1090',
                particles = [ P.ta__plus__, P.e__minus__, P.ta__plus__, P.mu__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_122,(0,7):C.GC_122,(0,0):C.GC_1350,(0,3):C.GC_1350,(0,1):C.GC_1326,(0,2):C.GC_85,(0,4):C.GC_1326,(0,5):C.GC_85})

V_1091 = Vertex(name = 'V_1091',
                particles = [ P.ta__plus__, P.e__minus__, P.ta__plus__, P.ta__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_140,(0,7):C.GC_140,(0,0):C.GC_1377,(0,3):C.GC_1377,(0,1):C.GC_1329,(0,2):C.GC_103,(0,4):C.GC_1329,(0,5):C.GC_103})

V_1092 = Vertex(name = 'V_1092',
                particles = [ P.e__plus__, P.mu__minus__, P.e__plus__, P.mu__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_1711,(0,7):C.GC_1711,(0,0):C.GC_1333,(0,3):C.GC_1333,(0,1):C.GC_1333,(0,2):C.GC_1110,(0,4):C.GC_1333,(0,5):C.GC_1110})

V_1093 = Vertex(name = 'V_1093',
                particles = [ P.mu__plus__, P.mu__minus__, P.e__plus__, P.mu__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_119,(0,7):C.GC_119,(0,0):C.GC_1334,(0,3):C.GC_1342,(0,1):C.GC_1334,(0,2):C.GC_82,(0,4):C.GC_1342,(0,5):C.GC_82})

V_1094 = Vertex(name = 'V_1094',
                particles = [ P.ta__plus__, P.mu__minus__, P.e__plus__, P.mu__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_123,(0,7):C.GC_123,(0,0):C.GC_1335,(0,3):C.GC_1351,(0,1):C.GC_1335,(0,2):C.GC_86,(0,4):C.GC_1351,(0,5):C.GC_86})

V_1095 = Vertex(name = 'V_1095',
                particles = [ P.e__plus__, P.mu__minus__, P.e__plus__, P.ta__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_128,(0,7):C.GC_128,(0,0):C.GC_1360,(0,3):C.GC_1360,(0,1):C.GC_1336,(0,2):C.GC_91,(0,4):C.GC_1336,(0,5):C.GC_91})

V_1096 = Vertex(name = 'V_1096',
                particles = [ P.mu__plus__, P.mu__minus__, P.e__plus__, P.ta__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_134,(0,7):C.GC_129,(0,0):C.GC_1361,(0,3):C.GC_1369,(0,1):C.GC_1337,(0,2):C.GC_97,(0,4):C.GC_1345,(0,5):C.GC_92})

V_1097 = Vertex(name = 'V_1097',
                particles = [ P.ta__plus__, P.mu__minus__, P.e__plus__, P.ta__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_141,(0,7):C.GC_130,(0,0):C.GC_1362,(0,3):C.GC_1378,(0,1):C.GC_1338,(0,2):C.GC_104,(0,4):C.GC_1354,(0,5):C.GC_93})

V_1098 = Vertex(name = 'V_1098',
                particles = [ P.mu__plus__, P.mu__minus__, P.mu__plus__, P.mu__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_1712,(0,7):C.GC_1712,(0,0):C.GC_1343,(0,3):C.GC_1343,(0,1):C.GC_1343,(0,2):C.GC_1111,(0,4):C.GC_1343,(0,5):C.GC_1111})

V_1099 = Vertex(name = 'V_1099',
                particles = [ P.ta__plus__, P.mu__minus__, P.mu__plus__, P.mu__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_124,(0,7):C.GC_124,(0,0):C.GC_1344,(0,3):C.GC_1352,(0,1):C.GC_1344,(0,2):C.GC_87,(0,4):C.GC_1352,(0,5):C.GC_87})

V_1100 = Vertex(name = 'V_1100',
                particles = [ P.mu__plus__, P.mu__minus__, P.mu__plus__, P.ta__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_135,(0,7):C.GC_135,(0,0):C.GC_1370,(0,3):C.GC_1370,(0,1):C.GC_1346,(0,2):C.GC_98,(0,4):C.GC_1346,(0,5):C.GC_98})

V_1101 = Vertex(name = 'V_1101',
                particles = [ P.ta__plus__, P.mu__minus__, P.mu__plus__, P.ta__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_142,(0,7):C.GC_136,(0,0):C.GC_1371,(0,3):C.GC_1379,(0,1):C.GC_1347,(0,2):C.GC_105,(0,4):C.GC_1355,(0,5):C.GC_99})

V_1102 = Vertex(name = 'V_1102',
                particles = [ P.ta__plus__, P.mu__minus__, P.ta__plus__, P.mu__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_1713,(0,7):C.GC_1713,(0,0):C.GC_1353,(0,3):C.GC_1353,(0,1):C.GC_1353,(0,2):C.GC_1112,(0,4):C.GC_1353,(0,5):C.GC_1112})

V_1103 = Vertex(name = 'V_1103',
                particles = [ P.ta__plus__, P.mu__minus__, P.ta__plus__, P.ta__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_143,(0,7):C.GC_143,(0,0):C.GC_1380,(0,3):C.GC_1380,(0,1):C.GC_1356,(0,2):C.GC_106,(0,4):C.GC_1356,(0,5):C.GC_106})

V_1104 = Vertex(name = 'V_1104',
                particles = [ P.e__plus__, P.ta__minus__, P.e__plus__, P.ta__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_1714,(0,7):C.GC_1714,(0,0):C.GC_1363,(0,3):C.GC_1363,(0,1):C.GC_1363,(0,2):C.GC_1113,(0,4):C.GC_1363,(0,5):C.GC_1113})

V_1105 = Vertex(name = 'V_1105',
                particles = [ P.mu__plus__, P.ta__minus__, P.e__plus__, P.ta__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_137,(0,7):C.GC_137,(0,0):C.GC_1364,(0,3):C.GC_1372,(0,1):C.GC_1364,(0,2):C.GC_100,(0,4):C.GC_1372,(0,5):C.GC_100})

V_1106 = Vertex(name = 'V_1106',
                particles = [ P.ta__plus__, P.ta__minus__, P.e__plus__, P.ta__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_144,(0,7):C.GC_144,(0,0):C.GC_1365,(0,3):C.GC_1381,(0,1):C.GC_1365,(0,2):C.GC_107,(0,4):C.GC_1381,(0,5):C.GC_107})

V_1107 = Vertex(name = 'V_1107',
                particles = [ P.mu__plus__, P.ta__minus__, P.mu__plus__, P.ta__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_1715,(0,7):C.GC_1715,(0,0):C.GC_1373,(0,3):C.GC_1373,(0,1):C.GC_1373,(0,2):C.GC_1114,(0,4):C.GC_1373,(0,5):C.GC_1114})

V_1108 = Vertex(name = 'V_1108',
                particles = [ P.ta__plus__, P.ta__minus__, P.mu__plus__, P.ta__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_145,(0,7):C.GC_145,(0,0):C.GC_1374,(0,3):C.GC_1382,(0,1):C.GC_1374,(0,2):C.GC_108,(0,4):C.GC_1382,(0,5):C.GC_108})

V_1109 = Vertex(name = 'V_1109',
                particles = [ P.ta__plus__, P.ta__minus__, P.ta__plus__, P.ta__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(0,6):C.GC_1716,(0,7):C.GC_1716,(0,0):C.GC_1383,(0,3):C.GC_1383,(0,1):C.GC_1383,(0,2):C.GC_1115,(0,4):C.GC_1383,(0,5):C.GC_1115})

V_1110 = Vertex(name = 'V_1110',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_307,(0,7):C.GC_307,(0,0):C.GC_2043,(2,0):C.GC_2124,(1,3):C.GC_2043,(3,3):C.GC_2124,(1,1):C.GC_2043,(3,1):C.GC_2124,(1,2):C.GC_2385,(0,4):C.GC_2043,(2,4):C.GC_2124,(0,5):C.GC_2385})

V_1111 = Vertex(name = 'V_1111',
                particles = [ P.c__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_308,(0,7):C.GC_308,(0,0):C.GC_2044,(2,0):C.GC_2125,(1,3):C.GC_2052,(3,3):C.GC_2133,(1,1):C.GC_2044,(3,1):C.GC_2125,(1,2):C.GC_352,(0,4):C.GC_2052,(2,4):C.GC_2133,(0,5):C.GC_352})

V_1112 = Vertex(name = 'V_1112',
                particles = [ P.t__tilde__, P.u, P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_310,(0,7):C.GC_310,(0,0):C.GC_2045,(2,0):C.GC_2126,(1,3):C.GC_2061,(3,3):C.GC_2142,(1,1):C.GC_2045,(3,1):C.GC_2126,(1,2):C.GC_353,(0,4):C.GC_2061,(2,4):C.GC_2142,(0,5):C.GC_353})

V_1113 = Vertex(name = 'V_1113',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_313,(0,7):C.GC_313,(0,0):C.GC_2070,(2,0):C.GC_2151,(1,3):C.GC_2070,(3,3):C.GC_2151,(1,1):C.GC_2046,(3,1):C.GC_2127,(1,2):C.GC_355,(0,4):C.GC_2046,(2,4):C.GC_2127,(0,5):C.GC_355})

V_1114 = Vertex(name = 'V_1114',
                particles = [ P.c__tilde__, P.u, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_317,(0,7):C.GC_314,(0,0):C.GC_2071,(2,0):C.GC_2152,(1,3):C.GC_2079,(3,3):C.GC_2160,(1,1):C.GC_2047,(3,1):C.GC_2128,(1,2):C.GC_358,(0,4):C.GC_2055,(2,4):C.GC_2136,(0,5):C.GC_356})

V_1115 = Vertex(name = 'V_1115',
                particles = [ P.t__tilde__, P.u, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_322,(0,7):C.GC_315,(0,0):C.GC_2072,(2,0):C.GC_2153,(1,3):C.GC_2088,(3,3):C.GC_2169,(1,1):C.GC_2048,(3,1):C.GC_2129,(1,2):C.GC_362,(0,4):C.GC_2064,(2,4):C.GC_2145,(0,5):C.GC_357})

V_1116 = Vertex(name = 'V_1116',
                particles = [ P.u__tilde__, P.u, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_328,(0,7):C.GC_328,(0,0):C.GC_2097,(2,0):C.GC_2178,(1,3):C.GC_2097,(3,3):C.GC_2178,(1,1):C.GC_2049,(3,1):C.GC_2130,(1,2):C.GC_367,(0,4):C.GC_2049,(2,4):C.GC_2130,(0,5):C.GC_367})

V_1117 = Vertex(name = 'V_1117',
                particles = [ P.c__tilde__, P.u, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_335,(0,7):C.GC_329,(0,0):C.GC_2098,(2,0):C.GC_2179,(1,3):C.GC_2106,(3,3):C.GC_2187,(1,1):C.GC_2050,(3,1):C.GC_2131,(1,2):C.GC_373,(0,4):C.GC_2058,(2,4):C.GC_2139,(0,5):C.GC_368})

V_1118 = Vertex(name = 'V_1118',
                particles = [ P.t__tilde__, P.u, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_343,(0,7):C.GC_330,(0,0):C.GC_2099,(2,0):C.GC_2180,(1,3):C.GC_2115,(3,3):C.GC_2196,(1,1):C.GC_2051,(3,1):C.GC_2132,(1,2):C.GC_380,(0,4):C.GC_2067,(2,4):C.GC_2148,(0,5):C.GC_369})

V_1119 = Vertex(name = 'V_1119',
                particles = [ P.c__tilde__, P.u, P.c__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_309,(0,7):C.GC_309,(0,0):C.GC_2053,(2,0):C.GC_2134,(1,3):C.GC_2053,(3,3):C.GC_2134,(1,1):C.GC_2053,(3,1):C.GC_2134,(1,2):C.GC_2386,(0,4):C.GC_2053,(2,4):C.GC_2134,(0,5):C.GC_2386})

V_1120 = Vertex(name = 'V_1120',
                particles = [ P.t__tilde__, P.u, P.c__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_311,(0,7):C.GC_311,(0,0):C.GC_2054,(2,0):C.GC_2135,(1,3):C.GC_2062,(3,3):C.GC_2143,(1,1):C.GC_2054,(3,1):C.GC_2135,(1,2):C.GC_354,(0,4):C.GC_2062,(2,4):C.GC_2143,(0,5):C.GC_354})

V_1121 = Vertex(name = 'V_1121',
                particles = [ P.c__tilde__, P.u, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_318,(0,7):C.GC_318,(0,0):C.GC_2080,(2,0):C.GC_2161,(1,3):C.GC_2080,(3,3):C.GC_2161,(1,1):C.GC_2056,(3,1):C.GC_2137,(1,2):C.GC_359,(0,4):C.GC_2056,(2,4):C.GC_2137,(0,5):C.GC_359})

V_1122 = Vertex(name = 'V_1122',
                particles = [ P.t__tilde__, P.u, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_323,(0,7):C.GC_319,(0,0):C.GC_2081,(2,0):C.GC_2162,(1,3):C.GC_2089,(3,3):C.GC_2170,(1,1):C.GC_2057,(3,1):C.GC_2138,(1,2):C.GC_363,(0,4):C.GC_2065,(2,4):C.GC_2146,(0,5):C.GC_360})

V_1123 = Vertex(name = 'V_1123',
                particles = [ P.c__tilde__, P.u, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_336,(0,7):C.GC_336,(0,0):C.GC_2107,(2,0):C.GC_2188,(1,3):C.GC_2107,(3,3):C.GC_2188,(1,1):C.GC_2059,(3,1):C.GC_2140,(1,2):C.GC_374,(0,4):C.GC_2059,(2,4):C.GC_2140,(0,5):C.GC_374})

V_1124 = Vertex(name = 'V_1124',
                particles = [ P.t__tilde__, P.u, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_344,(0,7):C.GC_337,(0,0):C.GC_2108,(2,0):C.GC_2189,(1,3):C.GC_2116,(3,3):C.GC_2197,(1,1):C.GC_2060,(3,1):C.GC_2141,(1,2):C.GC_381,(0,4):C.GC_2068,(2,4):C.GC_2149,(0,5):C.GC_375})

V_1125 = Vertex(name = 'V_1125',
                particles = [ P.t__tilde__, P.u, P.t__tilde__, P.u ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_312,(0,7):C.GC_312,(0,0):C.GC_2063,(2,0):C.GC_2144,(1,3):C.GC_2063,(3,3):C.GC_2144,(1,1):C.GC_2063,(3,1):C.GC_2144,(1,2):C.GC_2387,(0,4):C.GC_2063,(2,4):C.GC_2144,(0,5):C.GC_2387})

V_1126 = Vertex(name = 'V_1126',
                particles = [ P.t__tilde__, P.u, P.t__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_324,(0,7):C.GC_324,(0,0):C.GC_2090,(2,0):C.GC_2171,(1,3):C.GC_2090,(3,3):C.GC_2171,(1,1):C.GC_2066,(3,1):C.GC_2147,(1,2):C.GC_364,(0,4):C.GC_2066,(2,4):C.GC_2147,(0,5):C.GC_364})

V_1127 = Vertex(name = 'V_1127',
                particles = [ P.t__tilde__, P.u, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_345,(0,7):C.GC_345,(0,0):C.GC_2117,(2,0):C.GC_2198,(1,3):C.GC_2117,(3,3):C.GC_2198,(1,1):C.GC_2069,(3,1):C.GC_2150,(1,2):C.GC_382,(0,4):C.GC_2069,(2,4):C.GC_2150,(0,5):C.GC_382})

V_1128 = Vertex(name = 'V_1128',
                particles = [ P.u__tilde__, P.c, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_316,(0,7):C.GC_316,(0,0):C.GC_2073,(2,0):C.GC_2154,(1,3):C.GC_2073,(3,3):C.GC_2154,(1,1):C.GC_2073,(3,1):C.GC_2154,(1,2):C.GC_2388,(0,4):C.GC_2073,(2,4):C.GC_2154,(0,5):C.GC_2388})

V_1129 = Vertex(name = 'V_1129',
                particles = [ P.c__tilde__, P.c, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_320,(0,7):C.GC_320,(0,0):C.GC_2074,(2,0):C.GC_2155,(1,3):C.GC_2082,(3,3):C.GC_2163,(1,1):C.GC_2074,(3,1):C.GC_2155,(1,2):C.GC_361,(0,4):C.GC_2082,(2,4):C.GC_2163,(0,5):C.GC_361})

V_1130 = Vertex(name = 'V_1130',
                particles = [ P.t__tilde__, P.c, P.u__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_325,(0,7):C.GC_325,(0,0):C.GC_2075,(2,0):C.GC_2156,(1,3):C.GC_2091,(3,3):C.GC_2172,(1,1):C.GC_2075,(3,1):C.GC_2156,(1,2):C.GC_365,(0,4):C.GC_2091,(2,4):C.GC_2172,(0,5):C.GC_365})

V_1131 = Vertex(name = 'V_1131',
                particles = [ P.u__tilde__, P.c, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_331,(0,7):C.GC_331,(0,0):C.GC_2100,(2,0):C.GC_2181,(1,3):C.GC_2100,(3,3):C.GC_2181,(1,1):C.GC_2076,(3,1):C.GC_2157,(1,2):C.GC_370,(0,4):C.GC_2076,(2,4):C.GC_2157,(0,5):C.GC_370})

V_1132 = Vertex(name = 'V_1132',
                particles = [ P.c__tilde__, P.c, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_338,(0,7):C.GC_332,(0,0):C.GC_2101,(2,0):C.GC_2182,(1,3):C.GC_2109,(3,3):C.GC_2190,(1,1):C.GC_2077,(3,1):C.GC_2158,(1,2):C.GC_376,(0,4):C.GC_2085,(2,4):C.GC_2166,(0,5):C.GC_371})

V_1133 = Vertex(name = 'V_1133',
                particles = [ P.t__tilde__, P.c, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_346,(0,7):C.GC_333,(0,0):C.GC_2102,(2,0):C.GC_2183,(1,3):C.GC_2118,(3,3):C.GC_2199,(1,1):C.GC_2078,(3,1):C.GC_2159,(1,2):C.GC_383,(0,4):C.GC_2094,(2,4):C.GC_2175,(0,5):C.GC_372})

V_1134 = Vertex(name = 'V_1134',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_321,(0,7):C.GC_321,(0,0):C.GC_2083,(2,0):C.GC_2164,(1,3):C.GC_2083,(3,3):C.GC_2164,(1,1):C.GC_2083,(3,1):C.GC_2164,(1,2):C.GC_2389,(0,4):C.GC_2083,(2,4):C.GC_2164,(0,5):C.GC_2389})

V_1135 = Vertex(name = 'V_1135',
                particles = [ P.t__tilde__, P.c, P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_326,(0,7):C.GC_326,(0,0):C.GC_2084,(2,0):C.GC_2165,(1,3):C.GC_2092,(3,3):C.GC_2173,(1,1):C.GC_2084,(3,1):C.GC_2165,(1,2):C.GC_366,(0,4):C.GC_2092,(2,4):C.GC_2173,(0,5):C.GC_366})

V_1136 = Vertex(name = 'V_1136',
                particles = [ P.c__tilde__, P.c, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_339,(0,7):C.GC_339,(0,0):C.GC_2110,(2,0):C.GC_2191,(1,3):C.GC_2110,(3,3):C.GC_2191,(1,1):C.GC_2086,(3,1):C.GC_2167,(1,2):C.GC_377,(0,4):C.GC_2086,(2,4):C.GC_2167,(0,5):C.GC_377})

V_1137 = Vertex(name = 'V_1137',
                particles = [ P.t__tilde__, P.c, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_347,(0,7):C.GC_340,(0,0):C.GC_2111,(2,0):C.GC_2192,(1,3):C.GC_2119,(3,3):C.GC_2200,(1,1):C.GC_2087,(3,1):C.GC_2168,(1,2):C.GC_384,(0,4):C.GC_2095,(2,4):C.GC_2176,(0,5):C.GC_378})

V_1138 = Vertex(name = 'V_1138',
                particles = [ P.t__tilde__, P.c, P.t__tilde__, P.c ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_327,(0,7):C.GC_327,(0,0):C.GC_2093,(2,0):C.GC_2174,(1,3):C.GC_2093,(3,3):C.GC_2174,(1,1):C.GC_2093,(3,1):C.GC_2174,(1,2):C.GC_2390,(0,4):C.GC_2093,(2,4):C.GC_2174,(0,5):C.GC_2390})

V_1139 = Vertex(name = 'V_1139',
                particles = [ P.t__tilde__, P.c, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_348,(0,7):C.GC_348,(0,0):C.GC_2120,(2,0):C.GC_2201,(1,3):C.GC_2120,(3,3):C.GC_2201,(1,1):C.GC_2096,(3,1):C.GC_2177,(1,2):C.GC_385,(0,4):C.GC_2096,(2,4):C.GC_2177,(0,5):C.GC_385})

V_1140 = Vertex(name = 'V_1140',
                particles = [ P.u__tilde__, P.t, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_334,(0,7):C.GC_334,(0,0):C.GC_2103,(2,0):C.GC_2184,(1,3):C.GC_2103,(3,3):C.GC_2184,(1,1):C.GC_2103,(3,1):C.GC_2184,(1,2):C.GC_2391,(0,4):C.GC_2103,(2,4):C.GC_2184,(0,5):C.GC_2391})

V_1141 = Vertex(name = 'V_1141',
                particles = [ P.c__tilde__, P.t, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_341,(0,7):C.GC_341,(0,0):C.GC_2104,(2,0):C.GC_2185,(1,3):C.GC_2112,(3,3):C.GC_2193,(1,1):C.GC_2104,(3,1):C.GC_2185,(1,2):C.GC_379,(0,4):C.GC_2112,(2,4):C.GC_2193,(0,5):C.GC_379})

V_1142 = Vertex(name = 'V_1142',
                particles = [ P.t__tilde__, P.t, P.u__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_349,(0,7):C.GC_349,(0,0):C.GC_2105,(2,0):C.GC_2186,(1,3):C.GC_2121,(3,3):C.GC_2202,(1,1):C.GC_2105,(3,1):C.GC_2186,(1,2):C.GC_386,(0,4):C.GC_2121,(2,4):C.GC_2202,(0,5):C.GC_386})

V_1143 = Vertex(name = 'V_1143',
                particles = [ P.c__tilde__, P.t, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_342,(0,7):C.GC_342,(0,0):C.GC_2113,(2,0):C.GC_2194,(1,3):C.GC_2113,(3,3):C.GC_2194,(1,1):C.GC_2113,(3,1):C.GC_2194,(1,2):C.GC_2392,(0,4):C.GC_2113,(2,4):C.GC_2194,(0,5):C.GC_2392})

V_1144 = Vertex(name = 'V_1144',
                particles = [ P.t__tilde__, P.t, P.c__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_350,(0,7):C.GC_350,(0,0):C.GC_2114,(2,0):C.GC_2195,(1,3):C.GC_2122,(3,3):C.GC_2203,(1,1):C.GC_2114,(3,1):C.GC_2195,(1,2):C.GC_387,(0,4):C.GC_2122,(2,4):C.GC_2203,(0,5):C.GC_387})

V_1145 = Vertex(name = 'V_1145',
                particles = [ P.t__tilde__, P.t, P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)*Identity(3,4)', 'Identity(1,4)*Identity(2,3)', 'T(-1,2,1)*T(-1,4,3)', 'T(-1,2,3)*T(-1,4,1)' ],
                lorentz = [ L.FFFF15, L.FFFF16, L.FFFF17, L.FFFF18, L.FFFF19, L.FFFF20, L.FFFF4, L.FFFF5 ],
                couplings = {(1,6):C.GC_351,(0,7):C.GC_351,(0,0):C.GC_2123,(2,0):C.GC_2204,(1,3):C.GC_2123,(3,3):C.GC_2204,(1,1):C.GC_2123,(3,1):C.GC_2204,(1,2):C.GC_2393,(0,4):C.GC_2123,(2,4):C.GC_2204,(0,5):C.GC_2393})

V_1146 = Vertex(name = 'V_1146',
                particles = [ P.e__plus__, P.e__minus__, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_1708,(0,0):C.GC_1303})

V_1147 = Vertex(name = 'V_1147',
                particles = [ P.e__plus__, P.e__minus__, P.vm__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_110,(0,0):C.GC_1312})

V_1148 = Vertex(name = 'V_1148',
                particles = [ P.e__plus__, P.e__minus__, P.vt__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_111,(0,0):C.GC_1321})

V_1149 = Vertex(name = 'V_1149',
                particles = [ P.e__plus__, P.e__minus__, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_113,(0,0):C.GC_1330})

V_1150 = Vertex(name = 'V_1150',
                particles = [ P.e__plus__, P.e__minus__, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_116,(0,0):C.GC_1339})

V_1151 = Vertex(name = 'V_1151',
                particles = [ P.e__plus__, P.e__minus__, P.vt__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_120,(0,0):C.GC_1348})

V_1152 = Vertex(name = 'V_1152',
                particles = [ P.e__plus__, P.e__minus__, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_125,(0,0):C.GC_1357})

V_1153 = Vertex(name = 'V_1153',
                particles = [ P.e__plus__, P.e__minus__, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_131,(0,0):C.GC_1366})

V_1154 = Vertex(name = 'V_1154',
                particles = [ P.e__plus__, P.e__minus__, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_138,(0,0):C.GC_1375})

V_1155 = Vertex(name = 'V_1155',
                particles = [ P.mu__plus__, P.e__minus__, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_110,(0,0):C.GC_1304})

V_1156 = Vertex(name = 'V_1156',
                particles = [ P.mu__plus__, P.e__minus__, P.vm__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_1709,(0,0):C.GC_1313})

V_1157 = Vertex(name = 'V_1157',
                particles = [ P.mu__plus__, P.e__minus__, P.vt__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_112,(0,0):C.GC_1322})

V_1158 = Vertex(name = 'V_1158',
                particles = [ P.mu__plus__, P.e__minus__, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_114,(0,0):C.GC_1331})

V_1159 = Vertex(name = 'V_1159',
                particles = [ P.mu__plus__, P.e__minus__, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_117,(0,0):C.GC_1340})

V_1160 = Vertex(name = 'V_1160',
                particles = [ P.mu__plus__, P.e__minus__, P.vt__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_121,(0,0):C.GC_1349})

V_1161 = Vertex(name = 'V_1161',
                particles = [ P.mu__plus__, P.e__minus__, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_126,(0,0):C.GC_1358})

V_1162 = Vertex(name = 'V_1162',
                particles = [ P.mu__plus__, P.e__minus__, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_132,(0,0):C.GC_1367})

V_1163 = Vertex(name = 'V_1163',
                particles = [ P.mu__plus__, P.e__minus__, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_139,(0,0):C.GC_1376})

V_1164 = Vertex(name = 'V_1164',
                particles = [ P.ta__plus__, P.e__minus__, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_111,(0,0):C.GC_1305})

V_1165 = Vertex(name = 'V_1165',
                particles = [ P.ta__plus__, P.e__minus__, P.vm__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_112,(0,0):C.GC_1314})

V_1166 = Vertex(name = 'V_1166',
                particles = [ P.ta__plus__, P.e__minus__, P.vt__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_1710,(0,0):C.GC_1323})

V_1167 = Vertex(name = 'V_1167',
                particles = [ P.ta__plus__, P.e__minus__, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_115,(0,0):C.GC_1332})

V_1168 = Vertex(name = 'V_1168',
                particles = [ P.ta__plus__, P.e__minus__, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_118,(0,0):C.GC_1341})

V_1169 = Vertex(name = 'V_1169',
                particles = [ P.ta__plus__, P.e__minus__, P.vt__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_122,(0,0):C.GC_1350})

V_1170 = Vertex(name = 'V_1170',
                particles = [ P.ta__plus__, P.e__minus__, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_127,(0,0):C.GC_1359})

V_1171 = Vertex(name = 'V_1171',
                particles = [ P.ta__plus__, P.e__minus__, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_133,(0,0):C.GC_1368})

V_1172 = Vertex(name = 'V_1172',
                particles = [ P.ta__plus__, P.e__minus__, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_140,(0,0):C.GC_1377})

V_1173 = Vertex(name = 'V_1173',
                particles = [ P.e__plus__, P.mu__minus__, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_113,(0,0):C.GC_1306})

V_1174 = Vertex(name = 'V_1174',
                particles = [ P.e__plus__, P.mu__minus__, P.vm__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_114,(0,0):C.GC_1315})

V_1175 = Vertex(name = 'V_1175',
                particles = [ P.e__plus__, P.mu__minus__, P.vt__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_115,(0,0):C.GC_1324})

V_1176 = Vertex(name = 'V_1176',
                particles = [ P.e__plus__, P.mu__minus__, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_1711,(0,0):C.GC_1333})

V_1177 = Vertex(name = 'V_1177',
                particles = [ P.e__plus__, P.mu__minus__, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_119,(0,0):C.GC_1342})

V_1178 = Vertex(name = 'V_1178',
                particles = [ P.e__plus__, P.mu__minus__, P.vt__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_123,(0,0):C.GC_1351})

V_1179 = Vertex(name = 'V_1179',
                particles = [ P.e__plus__, P.mu__minus__, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_128,(0,0):C.GC_1360})

V_1180 = Vertex(name = 'V_1180',
                particles = [ P.e__plus__, P.mu__minus__, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_134,(0,0):C.GC_1369})

V_1181 = Vertex(name = 'V_1181',
                particles = [ P.e__plus__, P.mu__minus__, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_141,(0,0):C.GC_1378})

V_1182 = Vertex(name = 'V_1182',
                particles = [ P.mu__plus__, P.mu__minus__, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_116,(0,0):C.GC_1307})

V_1183 = Vertex(name = 'V_1183',
                particles = [ P.mu__plus__, P.mu__minus__, P.vm__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_117,(0,0):C.GC_1316})

V_1184 = Vertex(name = 'V_1184',
                particles = [ P.mu__plus__, P.mu__minus__, P.vt__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_118,(0,0):C.GC_1325})

V_1185 = Vertex(name = 'V_1185',
                particles = [ P.mu__plus__, P.mu__minus__, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_119,(0,0):C.GC_1334})

V_1186 = Vertex(name = 'V_1186',
                particles = [ P.mu__plus__, P.mu__minus__, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_1712,(0,0):C.GC_1343})

V_1187 = Vertex(name = 'V_1187',
                particles = [ P.mu__plus__, P.mu__minus__, P.vt__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_124,(0,0):C.GC_1352})

V_1188 = Vertex(name = 'V_1188',
                particles = [ P.mu__plus__, P.mu__minus__, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_129,(0,0):C.GC_1361})

V_1189 = Vertex(name = 'V_1189',
                particles = [ P.mu__plus__, P.mu__minus__, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_135,(0,0):C.GC_1370})

V_1190 = Vertex(name = 'V_1190',
                particles = [ P.mu__plus__, P.mu__minus__, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_142,(0,0):C.GC_1379})

V_1191 = Vertex(name = 'V_1191',
                particles = [ P.ta__plus__, P.mu__minus__, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_120,(0,0):C.GC_1308})

V_1192 = Vertex(name = 'V_1192',
                particles = [ P.ta__plus__, P.mu__minus__, P.vm__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_121,(0,0):C.GC_1317})

V_1193 = Vertex(name = 'V_1193',
                particles = [ P.ta__plus__, P.mu__minus__, P.vt__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_122,(0,0):C.GC_1326})

V_1194 = Vertex(name = 'V_1194',
                particles = [ P.ta__plus__, P.mu__minus__, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_123,(0,0):C.GC_1335})

V_1195 = Vertex(name = 'V_1195',
                particles = [ P.ta__plus__, P.mu__minus__, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_124,(0,0):C.GC_1344})

V_1196 = Vertex(name = 'V_1196',
                particles = [ P.ta__plus__, P.mu__minus__, P.vt__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_1713,(0,0):C.GC_1353})

V_1197 = Vertex(name = 'V_1197',
                particles = [ P.ta__plus__, P.mu__minus__, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_130,(0,0):C.GC_1362})

V_1198 = Vertex(name = 'V_1198',
                particles = [ P.ta__plus__, P.mu__minus__, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_136,(0,0):C.GC_1371})

V_1199 = Vertex(name = 'V_1199',
                particles = [ P.ta__plus__, P.mu__minus__, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_143,(0,0):C.GC_1380})

V_1200 = Vertex(name = 'V_1200',
                particles = [ P.e__plus__, P.ta__minus__, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_125,(0,0):C.GC_1309})

V_1201 = Vertex(name = 'V_1201',
                particles = [ P.e__plus__, P.ta__minus__, P.vm__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_126,(0,0):C.GC_1318})

V_1202 = Vertex(name = 'V_1202',
                particles = [ P.e__plus__, P.ta__minus__, P.vt__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_127,(0,0):C.GC_1327})

V_1203 = Vertex(name = 'V_1203',
                particles = [ P.e__plus__, P.ta__minus__, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_128,(0,0):C.GC_1336})

V_1204 = Vertex(name = 'V_1204',
                particles = [ P.e__plus__, P.ta__minus__, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_129,(0,0):C.GC_1345})

V_1205 = Vertex(name = 'V_1205',
                particles = [ P.e__plus__, P.ta__minus__, P.vt__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_130,(0,0):C.GC_1354})

V_1206 = Vertex(name = 'V_1206',
                particles = [ P.e__plus__, P.ta__minus__, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_1714,(0,0):C.GC_1363})

V_1207 = Vertex(name = 'V_1207',
                particles = [ P.e__plus__, P.ta__minus__, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_137,(0,0):C.GC_1372})

V_1208 = Vertex(name = 'V_1208',
                particles = [ P.e__plus__, P.ta__minus__, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_144,(0,0):C.GC_1381})

V_1209 = Vertex(name = 'V_1209',
                particles = [ P.mu__plus__, P.ta__minus__, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_131,(0,0):C.GC_1310})

V_1210 = Vertex(name = 'V_1210',
                particles = [ P.mu__plus__, P.ta__minus__, P.vm__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_132,(0,0):C.GC_1319})

V_1211 = Vertex(name = 'V_1211',
                particles = [ P.mu__plus__, P.ta__minus__, P.vt__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_133,(0,0):C.GC_1328})

V_1212 = Vertex(name = 'V_1212',
                particles = [ P.mu__plus__, P.ta__minus__, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_134,(0,0):C.GC_1337})

V_1213 = Vertex(name = 'V_1213',
                particles = [ P.mu__plus__, P.ta__minus__, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_135,(0,0):C.GC_1346})

V_1214 = Vertex(name = 'V_1214',
                particles = [ P.mu__plus__, P.ta__minus__, P.vt__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_136,(0,0):C.GC_1355})

V_1215 = Vertex(name = 'V_1215',
                particles = [ P.mu__plus__, P.ta__minus__, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_137,(0,0):C.GC_1364})

V_1216 = Vertex(name = 'V_1216',
                particles = [ P.mu__plus__, P.ta__minus__, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_1715,(0,0):C.GC_1373})

V_1217 = Vertex(name = 'V_1217',
                particles = [ P.mu__plus__, P.ta__minus__, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_145,(0,0):C.GC_1382})

V_1218 = Vertex(name = 'V_1218',
                particles = [ P.ta__plus__, P.ta__minus__, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_138,(0,0):C.GC_1311})

V_1219 = Vertex(name = 'V_1219',
                particles = [ P.ta__plus__, P.ta__minus__, P.vm__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_139,(0,0):C.GC_1320})

V_1220 = Vertex(name = 'V_1220',
                particles = [ P.ta__plus__, P.ta__minus__, P.vt__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_140,(0,0):C.GC_1329})

V_1221 = Vertex(name = 'V_1221',
                particles = [ P.ta__plus__, P.ta__minus__, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_141,(0,0):C.GC_1338})

V_1222 = Vertex(name = 'V_1222',
                particles = [ P.ta__plus__, P.ta__minus__, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_142,(0,0):C.GC_1347})

V_1223 = Vertex(name = 'V_1223',
                particles = [ P.ta__plus__, P.ta__minus__, P.vt__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_143,(0,0):C.GC_1356})

V_1224 = Vertex(name = 'V_1224',
                particles = [ P.ta__plus__, P.ta__minus__, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_144,(0,0):C.GC_1365})

V_1225 = Vertex(name = 'V_1225',
                particles = [ P.ta__plus__, P.ta__minus__, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_145,(0,0):C.GC_1374})

V_1226 = Vertex(name = 'V_1226',
                particles = [ P.ta__plus__, P.ta__minus__, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_1716,(0,0):C.GC_1383})

V_1227 = Vertex(name = 'V_1227',
                particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_147,(0,0):C.GC_1719})

V_1228 = Vertex(name = 'V_1228',
                particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_165,(0,0):C.GC_1728})

V_1229 = Vertex(name = 'V_1229',
                particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_183,(0,0):C.GC_1737})

V_1230 = Vertex(name = 'V_1230',
                particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_201,(0,0):C.GC_1746})

V_1231 = Vertex(name = 'V_1231',
                particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_219,(0,0):C.GC_1755})

V_1232 = Vertex(name = 'V_1232',
                particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_237,(0,0):C.GC_1764})

V_1233 = Vertex(name = 'V_1233',
                particles = [ P.u__tilde__, P.u, P.ve__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_255,(0,0):C.GC_1773})

V_1234 = Vertex(name = 'V_1234',
                particles = [ P.u__tilde__, P.u, P.vm__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_273,(0,0):C.GC_1782})

V_1235 = Vertex(name = 'V_1235',
                particles = [ P.u__tilde__, P.u, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_291,(0,0):C.GC_1791})

V_1236 = Vertex(name = 'V_1236',
                particles = [ P.c__tilde__, P.u, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_149,(0,0):C.GC_1720})

V_1237 = Vertex(name = 'V_1237',
                particles = [ P.c__tilde__, P.u, P.vm__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_167,(0,0):C.GC_1729})

V_1238 = Vertex(name = 'V_1238',
                particles = [ P.c__tilde__, P.u, P.vt__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_185,(0,0):C.GC_1738})

V_1239 = Vertex(name = 'V_1239',
                particles = [ P.c__tilde__, P.u, P.ve__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_203,(0,0):C.GC_1747})

V_1240 = Vertex(name = 'V_1240',
                particles = [ P.c__tilde__, P.u, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_221,(0,0):C.GC_1756})

V_1241 = Vertex(name = 'V_1241',
                particles = [ P.c__tilde__, P.u, P.vt__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_239,(0,0):C.GC_1765})

V_1242 = Vertex(name = 'V_1242',
                particles = [ P.c__tilde__, P.u, P.ve__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_257,(0,0):C.GC_1774})

V_1243 = Vertex(name = 'V_1243',
                particles = [ P.c__tilde__, P.u, P.vm__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_275,(0,0):C.GC_1783})

V_1244 = Vertex(name = 'V_1244',
                particles = [ P.c__tilde__, P.u, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_293,(0,0):C.GC_1792})

V_1245 = Vertex(name = 'V_1245',
                particles = [ P.t__tilde__, P.u, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_151,(0,0):C.GC_1721})

V_1246 = Vertex(name = 'V_1246',
                particles = [ P.t__tilde__, P.u, P.vm__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_169,(0,0):C.GC_1730})

V_1247 = Vertex(name = 'V_1247',
                particles = [ P.t__tilde__, P.u, P.vt__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_187,(0,0):C.GC_1739})

V_1248 = Vertex(name = 'V_1248',
                particles = [ P.t__tilde__, P.u, P.ve__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_205,(0,0):C.GC_1748})

V_1249 = Vertex(name = 'V_1249',
                particles = [ P.t__tilde__, P.u, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_223,(0,0):C.GC_1757})

V_1250 = Vertex(name = 'V_1250',
                particles = [ P.t__tilde__, P.u, P.vt__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_241,(0,0):C.GC_1766})

V_1251 = Vertex(name = 'V_1251',
                particles = [ P.t__tilde__, P.u, P.ve__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_259,(0,0):C.GC_1775})

V_1252 = Vertex(name = 'V_1252',
                particles = [ P.t__tilde__, P.u, P.vm__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_277,(0,0):C.GC_1784})

V_1253 = Vertex(name = 'V_1253',
                particles = [ P.t__tilde__, P.u, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_295,(0,0):C.GC_1793})

V_1254 = Vertex(name = 'V_1254',
                particles = [ P.u__tilde__, P.c, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_153,(0,0):C.GC_1722})

V_1255 = Vertex(name = 'V_1255',
                particles = [ P.u__tilde__, P.c, P.vm__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_171,(0,0):C.GC_1731})

V_1256 = Vertex(name = 'V_1256',
                particles = [ P.u__tilde__, P.c, P.vt__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_189,(0,0):C.GC_1740})

V_1257 = Vertex(name = 'V_1257',
                particles = [ P.u__tilde__, P.c, P.ve__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_207,(0,0):C.GC_1749})

V_1258 = Vertex(name = 'V_1258',
                particles = [ P.u__tilde__, P.c, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_225,(0,0):C.GC_1758})

V_1259 = Vertex(name = 'V_1259',
                particles = [ P.u__tilde__, P.c, P.vt__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_243,(0,0):C.GC_1767})

V_1260 = Vertex(name = 'V_1260',
                particles = [ P.u__tilde__, P.c, P.ve__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_261,(0,0):C.GC_1776})

V_1261 = Vertex(name = 'V_1261',
                particles = [ P.u__tilde__, P.c, P.vm__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_279,(0,0):C.GC_1785})

V_1262 = Vertex(name = 'V_1262',
                particles = [ P.u__tilde__, P.c, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_297,(0,0):C.GC_1794})

V_1263 = Vertex(name = 'V_1263',
                particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_155,(0,0):C.GC_1723})

V_1264 = Vertex(name = 'V_1264',
                particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_173,(0,0):C.GC_1732})

V_1265 = Vertex(name = 'V_1265',
                particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_191,(0,0):C.GC_1741})

V_1266 = Vertex(name = 'V_1266',
                particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_209,(0,0):C.GC_1750})

V_1267 = Vertex(name = 'V_1267',
                particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_227,(0,0):C.GC_1759})

V_1268 = Vertex(name = 'V_1268',
                particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_245,(0,0):C.GC_1768})

V_1269 = Vertex(name = 'V_1269',
                particles = [ P.c__tilde__, P.c, P.ve__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_263,(0,0):C.GC_1777})

V_1270 = Vertex(name = 'V_1270',
                particles = [ P.c__tilde__, P.c, P.vm__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_281,(0,0):C.GC_1786})

V_1271 = Vertex(name = 'V_1271',
                particles = [ P.c__tilde__, P.c, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_299,(0,0):C.GC_1795})

V_1272 = Vertex(name = 'V_1272',
                particles = [ P.t__tilde__, P.c, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_157,(0,0):C.GC_1724})

V_1273 = Vertex(name = 'V_1273',
                particles = [ P.t__tilde__, P.c, P.vm__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_175,(0,0):C.GC_1733})

V_1274 = Vertex(name = 'V_1274',
                particles = [ P.t__tilde__, P.c, P.vt__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_193,(0,0):C.GC_1742})

V_1275 = Vertex(name = 'V_1275',
                particles = [ P.t__tilde__, P.c, P.ve__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_211,(0,0):C.GC_1751})

V_1276 = Vertex(name = 'V_1276',
                particles = [ P.t__tilde__, P.c, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_229,(0,0):C.GC_1760})

V_1277 = Vertex(name = 'V_1277',
                particles = [ P.t__tilde__, P.c, P.vt__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_247,(0,0):C.GC_1769})

V_1278 = Vertex(name = 'V_1278',
                particles = [ P.t__tilde__, P.c, P.ve__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_265,(0,0):C.GC_1778})

V_1279 = Vertex(name = 'V_1279',
                particles = [ P.t__tilde__, P.c, P.vm__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_283,(0,0):C.GC_1787})

V_1280 = Vertex(name = 'V_1280',
                particles = [ P.t__tilde__, P.c, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_301,(0,0):C.GC_1796})

V_1281 = Vertex(name = 'V_1281',
                particles = [ P.u__tilde__, P.t, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_159,(0,0):C.GC_1725})

V_1282 = Vertex(name = 'V_1282',
                particles = [ P.u__tilde__, P.t, P.vm__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_177,(0,0):C.GC_1734})

V_1283 = Vertex(name = 'V_1283',
                particles = [ P.u__tilde__, P.t, P.vt__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_195,(0,0):C.GC_1743})

V_1284 = Vertex(name = 'V_1284',
                particles = [ P.u__tilde__, P.t, P.ve__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_213,(0,0):C.GC_1752})

V_1285 = Vertex(name = 'V_1285',
                particles = [ P.u__tilde__, P.t, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_231,(0,0):C.GC_1761})

V_1286 = Vertex(name = 'V_1286',
                particles = [ P.u__tilde__, P.t, P.vt__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_249,(0,0):C.GC_1770})

V_1287 = Vertex(name = 'V_1287',
                particles = [ P.u__tilde__, P.t, P.ve__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_267,(0,0):C.GC_1779})

V_1288 = Vertex(name = 'V_1288',
                particles = [ P.u__tilde__, P.t, P.vm__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_285,(0,0):C.GC_1788})

V_1289 = Vertex(name = 'V_1289',
                particles = [ P.u__tilde__, P.t, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_303,(0,0):C.GC_1797})

V_1290 = Vertex(name = 'V_1290',
                particles = [ P.c__tilde__, P.t, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_161,(0,0):C.GC_1726})

V_1291 = Vertex(name = 'V_1291',
                particles = [ P.c__tilde__, P.t, P.vm__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_179,(0,0):C.GC_1735})

V_1292 = Vertex(name = 'V_1292',
                particles = [ P.c__tilde__, P.t, P.vt__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_197,(0,0):C.GC_1744})

V_1293 = Vertex(name = 'V_1293',
                particles = [ P.c__tilde__, P.t, P.ve__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_215,(0,0):C.GC_1753})

V_1294 = Vertex(name = 'V_1294',
                particles = [ P.c__tilde__, P.t, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_233,(0,0):C.GC_1762})

V_1295 = Vertex(name = 'V_1295',
                particles = [ P.c__tilde__, P.t, P.vt__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_251,(0,0):C.GC_1771})

V_1296 = Vertex(name = 'V_1296',
                particles = [ P.c__tilde__, P.t, P.ve__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_269,(0,0):C.GC_1780})

V_1297 = Vertex(name = 'V_1297',
                particles = [ P.c__tilde__, P.t, P.vm__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_287,(0,0):C.GC_1789})

V_1298 = Vertex(name = 'V_1298',
                particles = [ P.c__tilde__, P.t, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF3, L.FFFF5 ],
                couplings = {(0,2):C.GC_1718,(0,1):C.GC_1717,(0,0):C.GC_1798})

V_1299 = Vertex(name = 'V_1299',
                particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_163,(0,0):C.GC_1727})

V_1300 = Vertex(name = 'V_1300',
                particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_181,(0,0):C.GC_1736})

V_1301 = Vertex(name = 'V_1301',
                particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_199,(0,0):C.GC_1745})

V_1302 = Vertex(name = 'V_1302',
                particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_217,(0,0):C.GC_1754})

V_1303 = Vertex(name = 'V_1303',
                particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_235,(0,0):C.GC_1763})

V_1304 = Vertex(name = 'V_1304',
                particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_253,(0,0):C.GC_1772})

V_1305 = Vertex(name = 'V_1305',
                particles = [ P.t__tilde__, P.t, P.ve__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_271,(0,0):C.GC_1781})

V_1306 = Vertex(name = 'V_1306',
                particles = [ P.t__tilde__, P.t, P.vm__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_289,(0,0):C.GC_1790})

V_1307 = Vertex(name = 'V_1307',
                particles = [ P.t__tilde__, P.t, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_306,(0,0):C.GC_1799})

V_1308 = Vertex(name = 'V_1308',
                particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_469,(0,0):C.GC_1222})

V_1309 = Vertex(name = 'V_1309',
                particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_471,(0,0):C.GC_1231})

V_1310 = Vertex(name = 'V_1310',
                particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_473,(0,0):C.GC_1240})

V_1311 = Vertex(name = 'V_1311',
                particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_475,(0,0):C.GC_1249})

V_1312 = Vertex(name = 'V_1312',
                particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_477,(0,0):C.GC_1258})

V_1313 = Vertex(name = 'V_1313',
                particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF3, L.FFFF5 ],
                couplings = {(0,2):C.GC_3225,(0,1):C.GC_3224,(0,0):C.GC_1267})

V_1314 = Vertex(name = 'V_1314',
                particles = [ P.d__tilde__, P.d, P.ve__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_480,(0,0):C.GC_1276})

V_1315 = Vertex(name = 'V_1315',
                particles = [ P.d__tilde__, P.d, P.vm__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_482,(0,0):C.GC_1285})

V_1316 = Vertex(name = 'V_1316',
                particles = [ P.d__tilde__, P.d, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_484,(0,0):C.GC_1294})

V_1317 = Vertex(name = 'V_1317',
                particles = [ P.s__tilde__, P.d, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_486,(0,0):C.GC_1223})

V_1318 = Vertex(name = 'V_1318',
                particles = [ P.s__tilde__, P.d, P.vm__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_488,(0,0):C.GC_1232})

V_1319 = Vertex(name = 'V_1319',
                particles = [ P.s__tilde__, P.d, P.vt__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_490,(0,0):C.GC_1241})

V_1320 = Vertex(name = 'V_1320',
                particles = [ P.s__tilde__, P.d, P.ve__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_492,(0,0):C.GC_1250})

V_1321 = Vertex(name = 'V_1321',
                particles = [ P.s__tilde__, P.d, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_494,(0,0):C.GC_1259})

V_1322 = Vertex(name = 'V_1322',
                particles = [ P.s__tilde__, P.d, P.vt__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_496,(0,0):C.GC_1268})

V_1323 = Vertex(name = 'V_1323',
                particles = [ P.s__tilde__, P.d, P.ve__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_498,(0,0):C.GC_1277})

V_1324 = Vertex(name = 'V_1324',
                particles = [ P.s__tilde__, P.d, P.vm__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_500,(0,0):C.GC_1286})

V_1325 = Vertex(name = 'V_1325',
                particles = [ P.s__tilde__, P.d, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_502,(0,0):C.GC_1295})

V_1326 = Vertex(name = 'V_1326',
                particles = [ P.b__tilde__, P.d, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_504,(0,0):C.GC_1224})

V_1327 = Vertex(name = 'V_1327',
                particles = [ P.b__tilde__, P.d, P.vm__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_506,(0,0):C.GC_1233})

V_1328 = Vertex(name = 'V_1328',
                particles = [ P.b__tilde__, P.d, P.vt__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_508,(0,0):C.GC_1242})

V_1329 = Vertex(name = 'V_1329',
                particles = [ P.b__tilde__, P.d, P.ve__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_510,(0,0):C.GC_1251})

V_1330 = Vertex(name = 'V_1330',
                particles = [ P.b__tilde__, P.d, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_512,(0,0):C.GC_1260})

V_1331 = Vertex(name = 'V_1331',
                particles = [ P.b__tilde__, P.d, P.vt__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_514,(0,0):C.GC_1269})

V_1332 = Vertex(name = 'V_1332',
                particles = [ P.b__tilde__, P.d, P.ve__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_516,(0,0):C.GC_1278})

V_1333 = Vertex(name = 'V_1333',
                particles = [ P.b__tilde__, P.d, P.vm__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_518,(0,0):C.GC_1287})

V_1334 = Vertex(name = 'V_1334',
                particles = [ P.b__tilde__, P.d, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_520,(0,0):C.GC_1296})

V_1335 = Vertex(name = 'V_1335',
                particles = [ P.d__tilde__, P.s, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_522,(0,0):C.GC_1225})

V_1336 = Vertex(name = 'V_1336',
                particles = [ P.d__tilde__, P.s, P.vm__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_524,(0,0):C.GC_1234})

V_1337 = Vertex(name = 'V_1337',
                particles = [ P.d__tilde__, P.s, P.vt__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_526,(0,0):C.GC_1243})

V_1338 = Vertex(name = 'V_1338',
                particles = [ P.d__tilde__, P.s, P.ve__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_528,(0,0):C.GC_1252})

V_1339 = Vertex(name = 'V_1339',
                particles = [ P.d__tilde__, P.s, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_530,(0,0):C.GC_1261})

V_1340 = Vertex(name = 'V_1340',
                particles = [ P.d__tilde__, P.s, P.vt__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_532,(0,0):C.GC_1270})

V_1341 = Vertex(name = 'V_1341',
                particles = [ P.d__tilde__, P.s, P.ve__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_534,(0,0):C.GC_1279})

V_1342 = Vertex(name = 'V_1342',
                particles = [ P.d__tilde__, P.s, P.vm__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_536,(0,0):C.GC_1288})

V_1343 = Vertex(name = 'V_1343',
                particles = [ P.d__tilde__, P.s, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_538,(0,0):C.GC_1297})

V_1344 = Vertex(name = 'V_1344',
                particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_540,(0,0):C.GC_1226})

V_1345 = Vertex(name = 'V_1345',
                particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_542,(0,0):C.GC_1235})

V_1346 = Vertex(name = 'V_1346',
                particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_544,(0,0):C.GC_1244})

V_1347 = Vertex(name = 'V_1347',
                particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_546,(0,0):C.GC_1253})

V_1348 = Vertex(name = 'V_1348',
                particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_548,(0,0):C.GC_1262})

V_1349 = Vertex(name = 'V_1349',
                particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_550,(0,0):C.GC_1271})

V_1350 = Vertex(name = 'V_1350',
                particles = [ P.s__tilde__, P.s, P.ve__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_552,(0,0):C.GC_1280})

V_1351 = Vertex(name = 'V_1351',
                particles = [ P.s__tilde__, P.s, P.vm__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_554,(0,0):C.GC_1289})

V_1352 = Vertex(name = 'V_1352',
                particles = [ P.s__tilde__, P.s, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_556,(0,0):C.GC_1298})

V_1353 = Vertex(name = 'V_1353',
                particles = [ P.b__tilde__, P.s, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_558,(0,0):C.GC_1227})

V_1354 = Vertex(name = 'V_1354',
                particles = [ P.b__tilde__, P.s, P.vm__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_560,(0,0):C.GC_1236})

V_1355 = Vertex(name = 'V_1355',
                particles = [ P.b__tilde__, P.s, P.vt__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_562,(0,0):C.GC_1245})

V_1356 = Vertex(name = 'V_1356',
                particles = [ P.b__tilde__, P.s, P.ve__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_564,(0,0):C.GC_1254})

V_1357 = Vertex(name = 'V_1357',
                particles = [ P.b__tilde__, P.s, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_566,(0,0):C.GC_1263})

V_1358 = Vertex(name = 'V_1358',
                particles = [ P.b__tilde__, P.s, P.vt__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_568,(0,0):C.GC_1272})

V_1359 = Vertex(name = 'V_1359',
                particles = [ P.b__tilde__, P.s, P.ve__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_570,(0,0):C.GC_1281})

V_1360 = Vertex(name = 'V_1360',
                particles = [ P.b__tilde__, P.s, P.vm__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_572,(0,0):C.GC_1290})

V_1361 = Vertex(name = 'V_1361',
                particles = [ P.b__tilde__, P.s, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_574,(0,0):C.GC_1299})

V_1362 = Vertex(name = 'V_1362',
                particles = [ P.d__tilde__, P.b, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_576,(0,0):C.GC_1228})

V_1363 = Vertex(name = 'V_1363',
                particles = [ P.d__tilde__, P.b, P.vm__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_578,(0,0):C.GC_1237})

V_1364 = Vertex(name = 'V_1364',
                particles = [ P.d__tilde__, P.b, P.vt__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_580,(0,0):C.GC_1246})

V_1365 = Vertex(name = 'V_1365',
                particles = [ P.d__tilde__, P.b, P.ve__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_582,(0,0):C.GC_1255})

V_1366 = Vertex(name = 'V_1366',
                particles = [ P.d__tilde__, P.b, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_584,(0,0):C.GC_1264})

V_1367 = Vertex(name = 'V_1367',
                particles = [ P.d__tilde__, P.b, P.vt__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_586,(0,0):C.GC_1273})

V_1368 = Vertex(name = 'V_1368',
                particles = [ P.d__tilde__, P.b, P.ve__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_588,(0,0):C.GC_1282})

V_1369 = Vertex(name = 'V_1369',
                particles = [ P.d__tilde__, P.b, P.vm__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_590,(0,0):C.GC_1291})

V_1370 = Vertex(name = 'V_1370',
                particles = [ P.d__tilde__, P.b, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_592,(0,0):C.GC_1300})

V_1371 = Vertex(name = 'V_1371',
                particles = [ P.s__tilde__, P.b, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_594,(0,0):C.GC_1229})

V_1372 = Vertex(name = 'V_1372',
                particles = [ P.s__tilde__, P.b, P.vm__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_596,(0,0):C.GC_1238})

V_1373 = Vertex(name = 'V_1373',
                particles = [ P.s__tilde__, P.b, P.vt__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_598,(0,0):C.GC_1247})

V_1374 = Vertex(name = 'V_1374',
                particles = [ P.s__tilde__, P.b, P.ve__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_600,(0,0):C.GC_1256})

V_1375 = Vertex(name = 'V_1375',
                particles = [ P.s__tilde__, P.b, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_602,(0,0):C.GC_1265})

V_1376 = Vertex(name = 'V_1376',
                particles = [ P.s__tilde__, P.b, P.vt__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_604,(0,0):C.GC_1274})

V_1377 = Vertex(name = 'V_1377',
                particles = [ P.s__tilde__, P.b, P.ve__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_606,(0,0):C.GC_1283})

V_1378 = Vertex(name = 'V_1378',
                particles = [ P.s__tilde__, P.b, P.vm__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_608,(0,0):C.GC_1292})

V_1379 = Vertex(name = 'V_1379',
                particles = [ P.s__tilde__, P.b, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_610,(0,0):C.GC_1301})

V_1380 = Vertex(name = 'V_1380',
                particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_612,(0,0):C.GC_1230})

V_1381 = Vertex(name = 'V_1381',
                particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_614,(0,0):C.GC_1239})

V_1382 = Vertex(name = 'V_1382',
                particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.ve ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_616,(0,0):C.GC_1248})

V_1383 = Vertex(name = 'V_1383',
                particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_618,(0,0):C.GC_1257})

V_1384 = Vertex(name = 'V_1384',
                particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_620,(0,0):C.GC_1266})

V_1385 = Vertex(name = 'V_1385',
                particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vm ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_622,(0,0):C.GC_1275})

V_1386 = Vertex(name = 'V_1386',
                particles = [ P.b__tilde__, P.b, P.ve__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_624,(0,0):C.GC_1284})

V_1387 = Vertex(name = 'V_1387',
                particles = [ P.b__tilde__, P.b, P.vm__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_626,(0,0):C.GC_1293})

V_1388 = Vertex(name = 'V_1388',
                particles = [ P.b__tilde__, P.b, P.vt__tilde__, P.vt ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFFF15, L.FFFF5 ],
                couplings = {(0,1):C.GC_628,(0,0):C.GC_1302})

V_1389 = Vertex(name = 'V_1389',
                particles = [ P.ve__tilde__, P.ve, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_1708,(0,1):C.GC_1708})

V_1390 = Vertex(name = 'V_1390',
                particles = [ P.vm__tilde__, P.ve, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_110,(0,1):C.GC_110})

V_1391 = Vertex(name = 'V_1391',
                particles = [ P.vt__tilde__, P.ve, P.ve__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_111,(0,1):C.GC_111})

V_1392 = Vertex(name = 'V_1392',
                particles = [ P.ve__tilde__, P.ve, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_113,(0,1):C.GC_113})

V_1393 = Vertex(name = 'V_1393',
                particles = [ P.vm__tilde__, P.ve, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_116,(0,1):C.GC_114})

V_1394 = Vertex(name = 'V_1394',
                particles = [ P.vt__tilde__, P.ve, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_120,(0,1):C.GC_115})

V_1395 = Vertex(name = 'V_1395',
                particles = [ P.ve__tilde__, P.ve, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_125,(0,1):C.GC_125})

V_1396 = Vertex(name = 'V_1396',
                particles = [ P.vm__tilde__, P.ve, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_131,(0,1):C.GC_126})

V_1397 = Vertex(name = 'V_1397',
                particles = [ P.vt__tilde__, P.ve, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_138,(0,1):C.GC_127})

V_1398 = Vertex(name = 'V_1398',
                particles = [ P.vm__tilde__, P.ve, P.vm__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_1709,(0,1):C.GC_1709})

V_1399 = Vertex(name = 'V_1399',
                particles = [ P.vt__tilde__, P.ve, P.vm__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_112,(0,1):C.GC_112})

V_1400 = Vertex(name = 'V_1400',
                particles = [ P.vm__tilde__, P.ve, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_117,(0,1):C.GC_117})

V_1401 = Vertex(name = 'V_1401',
                particles = [ P.vt__tilde__, P.ve, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_121,(0,1):C.GC_118})

V_1402 = Vertex(name = 'V_1402',
                particles = [ P.vm__tilde__, P.ve, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_132,(0,1):C.GC_132})

V_1403 = Vertex(name = 'V_1403',
                particles = [ P.vt__tilde__, P.ve, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_139,(0,1):C.GC_133})

V_1404 = Vertex(name = 'V_1404',
                particles = [ P.vt__tilde__, P.ve, P.vt__tilde__, P.ve ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_1710,(0,1):C.GC_1710})

V_1405 = Vertex(name = 'V_1405',
                particles = [ P.vt__tilde__, P.ve, P.vt__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_122,(0,1):C.GC_122})

V_1406 = Vertex(name = 'V_1406',
                particles = [ P.vt__tilde__, P.ve, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_140,(0,1):C.GC_140})

V_1407 = Vertex(name = 'V_1407',
                particles = [ P.ve__tilde__, P.vm, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_1711,(0,1):C.GC_1711})

V_1408 = Vertex(name = 'V_1408',
                particles = [ P.vm__tilde__, P.vm, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_119,(0,1):C.GC_119})

V_1409 = Vertex(name = 'V_1409',
                particles = [ P.vt__tilde__, P.vm, P.ve__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_123,(0,1):C.GC_123})

V_1410 = Vertex(name = 'V_1410',
                particles = [ P.ve__tilde__, P.vm, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_128,(0,1):C.GC_128})

V_1411 = Vertex(name = 'V_1411',
                particles = [ P.vm__tilde__, P.vm, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_134,(0,1):C.GC_129})

V_1412 = Vertex(name = 'V_1412',
                particles = [ P.vt__tilde__, P.vm, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_141,(0,1):C.GC_130})

V_1413 = Vertex(name = 'V_1413',
                particles = [ P.vm__tilde__, P.vm, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_1712,(0,1):C.GC_1712})

V_1414 = Vertex(name = 'V_1414',
                particles = [ P.vt__tilde__, P.vm, P.vm__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_124,(0,1):C.GC_124})

V_1415 = Vertex(name = 'V_1415',
                particles = [ P.vm__tilde__, P.vm, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_135,(0,1):C.GC_135})

V_1416 = Vertex(name = 'V_1416',
                particles = [ P.vt__tilde__, P.vm, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_142,(0,1):C.GC_136})

V_1417 = Vertex(name = 'V_1417',
                particles = [ P.vt__tilde__, P.vm, P.vt__tilde__, P.vm ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_1713,(0,1):C.GC_1713})

V_1418 = Vertex(name = 'V_1418',
                particles = [ P.vt__tilde__, P.vm, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_143,(0,1):C.GC_143})

V_1419 = Vertex(name = 'V_1419',
                particles = [ P.ve__tilde__, P.vt, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_1714,(0,1):C.GC_1714})

V_1420 = Vertex(name = 'V_1420',
                particles = [ P.vm__tilde__, P.vt, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_137,(0,1):C.GC_137})

V_1421 = Vertex(name = 'V_1421',
                particles = [ P.vt__tilde__, P.vt, P.ve__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_144,(0,1):C.GC_144})

V_1422 = Vertex(name = 'V_1422',
                particles = [ P.vm__tilde__, P.vt, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_1715,(0,1):C.GC_1715})

V_1423 = Vertex(name = 'V_1423',
                particles = [ P.vt__tilde__, P.vt, P.vm__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_145,(0,1):C.GC_145})

V_1424 = Vertex(name = 'V_1424',
                particles = [ P.vt__tilde__, P.vt, P.vt__tilde__, P.vt ],
                color = [ '1' ],
                lorentz = [ L.FFFF4, L.FFFF5 ],
                couplings = {(0,0):C.GC_1716,(0,1):C.GC_1716})

V_1425 = Vertex(name = 'V_1425',
                particles = [ P.d__tilde__, P.d, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS4, L.FFVS9 ],
                couplings = {(0,0):C.GC_5320,(0,1):C.GC_1008})

V_1426 = Vertex(name = 'V_1426',
                particles = [ P.s__tilde__, P.d, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS4, L.FFVS9 ],
                couplings = {(0,0):C.GC_5332,(0,1):C.GC_1009})

V_1427 = Vertex(name = 'V_1427',
                particles = [ P.b__tilde__, P.d, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS4, L.FFVS9 ],
                couplings = {(0,0):C.GC_5344,(0,1):C.GC_1010})

V_1428 = Vertex(name = 'V_1428',
                particles = [ P.d__tilde__, P.s, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS4, L.FFVS9 ],
                couplings = {(0,0):C.GC_5324,(0,1):C.GC_1011})

V_1429 = Vertex(name = 'V_1429',
                particles = [ P.s__tilde__, P.s, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS4, L.FFVS9 ],
                couplings = {(0,0):C.GC_5336,(0,1):C.GC_1012})

V_1430 = Vertex(name = 'V_1430',
                particles = [ P.b__tilde__, P.s, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS4, L.FFVS9 ],
                couplings = {(0,0):C.GC_5348,(0,1):C.GC_1013})

V_1431 = Vertex(name = 'V_1431',
                particles = [ P.d__tilde__, P.b, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS4, L.FFVS9 ],
                couplings = {(0,0):C.GC_5328,(0,1):C.GC_1014})

V_1432 = Vertex(name = 'V_1432',
                particles = [ P.s__tilde__, P.b, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS4, L.FFVS9 ],
                couplings = {(0,0):C.GC_5340,(0,1):C.GC_1015})

V_1433 = Vertex(name = 'V_1433',
                particles = [ P.b__tilde__, P.b, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS4, L.FFVS9 ],
                couplings = {(0,0):C.GC_5352,(0,1):C.GC_1016})

V_1434 = Vertex(name = 'V_1434',
                particles = [ P.u__tilde__, P.u, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS4, L.FFVS9 ],
                couplings = {(0,0):C.GC_6103,(0,1):C.GC_2367})

V_1435 = Vertex(name = 'V_1435',
                particles = [ P.c__tilde__, P.u, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS4, L.FFVS9 ],
                couplings = {(0,0):C.GC_6115,(0,1):C.GC_2368})

V_1436 = Vertex(name = 'V_1436',
                particles = [ P.t__tilde__, P.u, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS4, L.FFVS9 ],
                couplings = {(0,0):C.GC_6127,(0,1):C.GC_2369})

V_1437 = Vertex(name = 'V_1437',
                particles = [ P.u__tilde__, P.c, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS4, L.FFVS9 ],
                couplings = {(0,0):C.GC_6107,(0,1):C.GC_2370})

V_1438 = Vertex(name = 'V_1438',
                particles = [ P.c__tilde__, P.c, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS4, L.FFVS9 ],
                couplings = {(0,0):C.GC_6119,(0,1):C.GC_2371})

V_1439 = Vertex(name = 'V_1439',
                particles = [ P.t__tilde__, P.c, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS4, L.FFVS9 ],
                couplings = {(0,0):C.GC_6131,(0,1):C.GC_2372})

V_1440 = Vertex(name = 'V_1440',
                particles = [ P.u__tilde__, P.t, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS4, L.FFVS9 ],
                couplings = {(0,0):C.GC_6111,(0,1):C.GC_2373})

V_1441 = Vertex(name = 'V_1441',
                particles = [ P.c__tilde__, P.t, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS4, L.FFVS9 ],
                couplings = {(0,0):C.GC_6123,(0,1):C.GC_2374})

V_1442 = Vertex(name = 'V_1442',
                particles = [ P.t__tilde__, P.t, P.g, P.H ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFVS4, L.FFVS9 ],
                couplings = {(0,0):C.GC_6135,(0,1):C.GC_2375})

V_1443 = Vertex(name = 'V_1443',
                particles = [ P.d__tilde__, P.d, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_5321,(0,1):C.GC_2397})

V_1444 = Vertex(name = 'V_1444',
                particles = [ P.s__tilde__, P.d, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_5333,(0,1):C.GC_2398})

V_1445 = Vertex(name = 'V_1445',
                particles = [ P.b__tilde__, P.d, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_5345,(0,1):C.GC_2399})

V_1446 = Vertex(name = 'V_1446',
                particles = [ P.d__tilde__, P.s, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_5325,(0,1):C.GC_2400})

V_1447 = Vertex(name = 'V_1447',
                particles = [ P.s__tilde__, P.s, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_5337,(0,1):C.GC_2401})

V_1448 = Vertex(name = 'V_1448',
                particles = [ P.b__tilde__, P.s, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_5349,(0,1):C.GC_2402})

V_1449 = Vertex(name = 'V_1449',
                particles = [ P.d__tilde__, P.b, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS2, L.FFVVS3 ],
                couplings = {(0,0):C.GC_5329,(0,1):C.GC_2403})

V_1450 = Vertex(name = 'V_1450',
                particles = [ P.s__tilde__, P.b, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_5341,(0,1):C.GC_2404})

V_1451 = Vertex(name = 'V_1451',
                particles = [ P.b__tilde__, P.b, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_5353,(0,1):C.GC_2405})

V_1452 = Vertex(name = 'V_1452',
                particles = [ P.d__tilde__, P.d, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_5323,(0,1):C.GC_4710})

V_1453 = Vertex(name = 'V_1453',
                particles = [ P.s__tilde__, P.d, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_5335,(0,1):C.GC_4711})

V_1454 = Vertex(name = 'V_1454',
                particles = [ P.b__tilde__, P.d, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_5347,(0,1):C.GC_4712})

V_1455 = Vertex(name = 'V_1455',
                particles = [ P.d__tilde__, P.s, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_5327,(0,1):C.GC_4713})

V_1456 = Vertex(name = 'V_1456',
                particles = [ P.s__tilde__, P.s, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_5339,(0,1):C.GC_4714})

V_1457 = Vertex(name = 'V_1457',
                particles = [ P.b__tilde__, P.s, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_5351,(0,1):C.GC_4715})

V_1458 = Vertex(name = 'V_1458',
                particles = [ P.d__tilde__, P.b, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_5331,(0,1):C.GC_4716})

V_1459 = Vertex(name = 'V_1459',
                particles = [ P.s__tilde__, P.b, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_5343,(0,1):C.GC_4717})

V_1460 = Vertex(name = 'V_1460',
                particles = [ P.b__tilde__, P.b, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_5355,(0,1):C.GC_4718})

V_1461 = Vertex(name = 'V_1461',
                particles = [ P.u__tilde__, P.u, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_6104,(0,1):C.GC_2411})

V_1462 = Vertex(name = 'V_1462',
                particles = [ P.c__tilde__, P.u, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_6116,(0,1):C.GC_2412})

V_1463 = Vertex(name = 'V_1463',
                particles = [ P.t__tilde__, P.u, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_6128,(0,1):C.GC_2413})

V_1464 = Vertex(name = 'V_1464',
                particles = [ P.u__tilde__, P.c, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_6108,(0,1):C.GC_2414})

V_1465 = Vertex(name = 'V_1465',
                particles = [ P.c__tilde__, P.c, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_6120,(0,1):C.GC_2415})

V_1466 = Vertex(name = 'V_1466',
                particles = [ P.t__tilde__, P.c, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_6132,(0,1):C.GC_2416})

V_1467 = Vertex(name = 'V_1467',
                particles = [ P.u__tilde__, P.t, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_6112,(0,1):C.GC_2417})

V_1468 = Vertex(name = 'V_1468',
                particles = [ P.c__tilde__, P.t, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_6124,(0,1):C.GC_2418})

V_1469 = Vertex(name = 'V_1469',
                particles = [ P.t__tilde__, P.t, P.g, P.g, P.H ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_6136,(0,1):C.GC_2419})

V_1470 = Vertex(name = 'V_1470',
                particles = [ P.u__tilde__, P.u, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_6106,(0,1):C.GC_4721})

V_1471 = Vertex(name = 'V_1471',
                particles = [ P.c__tilde__, P.u, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_6118,(0,1):C.GC_4722})

V_1472 = Vertex(name = 'V_1472',
                particles = [ P.t__tilde__, P.u, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_6130,(0,1):C.GC_4723})

V_1473 = Vertex(name = 'V_1473',
                particles = [ P.u__tilde__, P.c, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_6110,(0,1):C.GC_4724})

V_1474 = Vertex(name = 'V_1474',
                particles = [ P.c__tilde__, P.c, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_6122,(0,1):C.GC_4725})

V_1475 = Vertex(name = 'V_1475',
                particles = [ P.t__tilde__, P.c, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_6134,(0,1):C.GC_4726})

V_1476 = Vertex(name = 'V_1476',
                particles = [ P.u__tilde__, P.t, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_6114,(0,1):C.GC_4727})

V_1477 = Vertex(name = 'V_1477',
                particles = [ P.c__tilde__, P.t, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_6126,(0,1):C.GC_4728})

V_1478 = Vertex(name = 'V_1478',
                particles = [ P.t__tilde__, P.t, P.g, P.g ],
                color = [ 'f(-1,3,4)*T(-1,2,1)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_6138,(0,1):C.GC_4729})

V_1479 = Vertex(name = 'V_1479',
                particles = [ P.d__tilde__, P.u, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_4400,(0,1):C.GC_4409})

V_1480 = Vertex(name = 'V_1480',
                particles = [ P.s__tilde__, P.u, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_4401,(0,1):C.GC_4410})

V_1481 = Vertex(name = 'V_1481',
                particles = [ P.b__tilde__, P.u, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_4402,(0,1):C.GC_4411})

V_1482 = Vertex(name = 'V_1482',
                particles = [ P.d__tilde__, P.c, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_4403,(0,1):C.GC_4412})

V_1483 = Vertex(name = 'V_1483',
                particles = [ P.s__tilde__, P.c, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_4404,(0,1):C.GC_4413})

V_1484 = Vertex(name = 'V_1484',
                particles = [ P.b__tilde__, P.c, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_4405,(0,1):C.GC_4414})

V_1485 = Vertex(name = 'V_1485',
                particles = [ P.d__tilde__, P.t, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_4406,(0,1):C.GC_4415})

V_1486 = Vertex(name = 'V_1486',
                particles = [ P.s__tilde__, P.t, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_4407,(0,1):C.GC_4416})

V_1487 = Vertex(name = 'V_1487',
                particles = [ P.b__tilde__, P.t, P.a, P.W__minus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_4408,(0,1):C.GC_4417})

V_1488 = Vertex(name = 'V_1488',
                particles = [ P.d__tilde__, P.u, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4893,(0,1):C.GC_4902})

V_1489 = Vertex(name = 'V_1489',
                particles = [ P.s__tilde__, P.u, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4894,(0,1):C.GC_4903})

V_1490 = Vertex(name = 'V_1490',
                particles = [ P.b__tilde__, P.u, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4895,(0,1):C.GC_4904})

V_1491 = Vertex(name = 'V_1491',
                particles = [ P.d__tilde__, P.c, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4896,(0,1):C.GC_4905})

V_1492 = Vertex(name = 'V_1492',
                particles = [ P.s__tilde__, P.c, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4897,(0,1):C.GC_4906})

V_1493 = Vertex(name = 'V_1493',
                particles = [ P.b__tilde__, P.c, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4898,(0,1):C.GC_4907})

V_1494 = Vertex(name = 'V_1494',
                particles = [ P.d__tilde__, P.t, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4899,(0,1):C.GC_4908})

V_1495 = Vertex(name = 'V_1495',
                particles = [ P.s__tilde__, P.t, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4900,(0,1):C.GC_4909})

V_1496 = Vertex(name = 'V_1496',
                particles = [ P.b__tilde__, P.t, P.a, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4901,(0,1):C.GC_4910})

V_1497 = Vertex(name = 'V_1497',
                particles = [ P.u__tilde__, P.d, P.a, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_4418,(0,1):C.GC_4427})

V_1498 = Vertex(name = 'V_1498',
                particles = [ P.c__tilde__, P.d, P.a, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_4419,(0,1):C.GC_4428})

V_1499 = Vertex(name = 'V_1499',
                particles = [ P.t__tilde__, P.d, P.a, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_4420,(0,1):C.GC_4429})

V_1500 = Vertex(name = 'V_1500',
                particles = [ P.u__tilde__, P.s, P.a, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_4421,(0,1):C.GC_4430})

V_1501 = Vertex(name = 'V_1501',
                particles = [ P.c__tilde__, P.s, P.a, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_4422,(0,1):C.GC_4431})

V_1502 = Vertex(name = 'V_1502',
                particles = [ P.t__tilde__, P.s, P.a, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_4423,(0,1):C.GC_4432})

V_1503 = Vertex(name = 'V_1503',
                particles = [ P.u__tilde__, P.b, P.a, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_4424,(0,1):C.GC_4433})

V_1504 = Vertex(name = 'V_1504',
                particles = [ P.c__tilde__, P.b, P.a, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_4425,(0,1):C.GC_4434})

V_1505 = Vertex(name = 'V_1505',
                particles = [ P.t__tilde__, P.b, P.a, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_4426,(0,1):C.GC_4435})

V_1506 = Vertex(name = 'V_1506',
                particles = [ P.u__tilde__, P.d, P.a, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4911,(0,1):C.GC_4920})

V_1507 = Vertex(name = 'V_1507',
                particles = [ P.c__tilde__, P.d, P.a, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4912,(0,1):C.GC_4921})

V_1508 = Vertex(name = 'V_1508',
                particles = [ P.t__tilde__, P.d, P.a, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4913,(0,1):C.GC_4922})

V_1509 = Vertex(name = 'V_1509',
                particles = [ P.u__tilde__, P.s, P.a, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4914,(0,1):C.GC_4923})

V_1510 = Vertex(name = 'V_1510',
                particles = [ P.c__tilde__, P.s, P.a, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4915,(0,1):C.GC_4924})

V_1511 = Vertex(name = 'V_1511',
                particles = [ P.t__tilde__, P.s, P.a, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4916,(0,1):C.GC_4925})

V_1512 = Vertex(name = 'V_1512',
                particles = [ P.u__tilde__, P.b, P.a, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4917,(0,1):C.GC_4926})

V_1513 = Vertex(name = 'V_1513',
                particles = [ P.c__tilde__, P.b, P.a, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4918,(0,1):C.GC_4927})

V_1514 = Vertex(name = 'V_1514',
                particles = [ P.t__tilde__, P.b, P.a, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4919,(0,1):C.GC_4928})

V_1515 = Vertex(name = 'V_1515',
                particles = [ P.ve__tilde__, P.e__minus__, P.a, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1 ],
                couplings = {(0,0):C.GC_5486})

V_1516 = Vertex(name = 'V_1516',
                particles = [ P.vm__tilde__, P.e__minus__, P.a, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1 ],
                couplings = {(0,0):C.GC_5531})

V_1517 = Vertex(name = 'V_1517',
                particles = [ P.vt__tilde__, P.e__minus__, P.a, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1 ],
                couplings = {(0,0):C.GC_5576})

V_1518 = Vertex(name = 'V_1518',
                particles = [ P.ve__tilde__, P.mu__minus__, P.a, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1 ],
                couplings = {(0,0):C.GC_5501})

V_1519 = Vertex(name = 'V_1519',
                particles = [ P.vm__tilde__, P.mu__minus__, P.a, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1 ],
                couplings = {(0,0):C.GC_5546})

V_1520 = Vertex(name = 'V_1520',
                particles = [ P.vt__tilde__, P.mu__minus__, P.a, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1 ],
                couplings = {(0,0):C.GC_5591})

V_1521 = Vertex(name = 'V_1521',
                particles = [ P.ve__tilde__, P.ta__minus__, P.a, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1 ],
                couplings = {(0,0):C.GC_5516})

V_1522 = Vertex(name = 'V_1522',
                particles = [ P.vm__tilde__, P.ta__minus__, P.a, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1 ],
                couplings = {(0,0):C.GC_5561})

V_1523 = Vertex(name = 'V_1523',
                particles = [ P.vt__tilde__, P.ta__minus__, P.a, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1 ],
                couplings = {(0,0):C.GC_5606})

V_1524 = Vertex(name = 'V_1524',
                particles = [ P.ve__tilde__, P.e__minus__, P.a, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_5490})

V_1525 = Vertex(name = 'V_1525',
                particles = [ P.vm__tilde__, P.e__minus__, P.a, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_5535})

V_1526 = Vertex(name = 'V_1526',
                particles = [ P.vt__tilde__, P.e__minus__, P.a, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_5580})

V_1527 = Vertex(name = 'V_1527',
                particles = [ P.ve__tilde__, P.mu__minus__, P.a, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_5505})

V_1528 = Vertex(name = 'V_1528',
                particles = [ P.vm__tilde__, P.mu__minus__, P.a, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_5550})

V_1529 = Vertex(name = 'V_1529',
                particles = [ P.vt__tilde__, P.mu__minus__, P.a, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_5595})

V_1530 = Vertex(name = 'V_1530',
                particles = [ P.ve__tilde__, P.ta__minus__, P.a, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_5520})

V_1531 = Vertex(name = 'V_1531',
                particles = [ P.vm__tilde__, P.ta__minus__, P.a, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_5565})

V_1532 = Vertex(name = 'V_1532',
                particles = [ P.vt__tilde__, P.ta__minus__, P.a, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_5610})

V_1533 = Vertex(name = 'V_1533',
                particles = [ P.d__tilde__, P.d, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_5383,(0,1):C.GC_2429})

V_1534 = Vertex(name = 'V_1534',
                particles = [ P.s__tilde__, P.d, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_5407,(0,1):C.GC_2430})

V_1535 = Vertex(name = 'V_1535',
                particles = [ P.b__tilde__, P.d, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_5431,(0,1):C.GC_2431})

V_1536 = Vertex(name = 'V_1536',
                particles = [ P.d__tilde__, P.s, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_5391,(0,1):C.GC_2432})

V_1537 = Vertex(name = 'V_1537',
                particles = [ P.s__tilde__, P.s, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_5415,(0,1):C.GC_2433})

V_1538 = Vertex(name = 'V_1538',
                particles = [ P.b__tilde__, P.s, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_5439,(0,1):C.GC_2434})

V_1539 = Vertex(name = 'V_1539',
                particles = [ P.d__tilde__, P.b, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_5399,(0,1):C.GC_2435})

V_1540 = Vertex(name = 'V_1540',
                particles = [ P.s__tilde__, P.b, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_5423,(0,1):C.GC_2436})

V_1541 = Vertex(name = 'V_1541',
                particles = [ P.b__tilde__, P.b, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_5447,(0,1):C.GC_2437})

V_1542 = Vertex(name = 'V_1542',
                particles = [ P.d__tilde__, P.d, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_5384,(0,1):C.GC_4731})

V_1543 = Vertex(name = 'V_1543',
                particles = [ P.s__tilde__, P.d, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_5408,(0,1):C.GC_4732})

V_1544 = Vertex(name = 'V_1544',
                particles = [ P.b__tilde__, P.d, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_5432,(0,1):C.GC_4733})

V_1545 = Vertex(name = 'V_1545',
                particles = [ P.d__tilde__, P.s, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_5392,(0,1):C.GC_4734})

V_1546 = Vertex(name = 'V_1546',
                particles = [ P.s__tilde__, P.s, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_5416,(0,1):C.GC_4735})

V_1547 = Vertex(name = 'V_1547',
                particles = [ P.b__tilde__, P.s, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_5440,(0,1):C.GC_4736})

V_1548 = Vertex(name = 'V_1548',
                particles = [ P.d__tilde__, P.b, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_5400,(0,1):C.GC_4737})

V_1549 = Vertex(name = 'V_1549',
                particles = [ P.s__tilde__, P.b, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_5424,(0,1):C.GC_4738})

V_1550 = Vertex(name = 'V_1550',
                particles = [ P.b__tilde__, P.b, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_5448,(0,1):C.GC_4739})

V_1551 = Vertex(name = 'V_1551',
                particles = [ P.e__plus__, P.e__minus__, P.W__minus__, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_5484,(0,1):C.GC_2438})

V_1552 = Vertex(name = 'V_1552',
                particles = [ P.mu__plus__, P.e__minus__, P.W__minus__, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_5529,(0,1):C.GC_2439})

V_1553 = Vertex(name = 'V_1553',
                particles = [ P.ta__plus__, P.e__minus__, P.W__minus__, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_5574,(0,1):C.GC_2440})

V_1554 = Vertex(name = 'V_1554',
                particles = [ P.e__plus__, P.mu__minus__, P.W__minus__, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_5499,(0,1):C.GC_2441})

V_1555 = Vertex(name = 'V_1555',
                particles = [ P.mu__plus__, P.mu__minus__, P.W__minus__, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_5544,(0,1):C.GC_2442})

V_1556 = Vertex(name = 'V_1556',
                particles = [ P.ta__plus__, P.mu__minus__, P.W__minus__, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_5589,(0,1):C.GC_2443})

V_1557 = Vertex(name = 'V_1557',
                particles = [ P.e__plus__, P.ta__minus__, P.W__minus__, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_5514,(0,1):C.GC_2444})

V_1558 = Vertex(name = 'V_1558',
                particles = [ P.mu__plus__, P.ta__minus__, P.W__minus__, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_5559,(0,1):C.GC_2445})

V_1559 = Vertex(name = 'V_1559',
                particles = [ P.ta__plus__, P.ta__minus__, P.W__minus__, P.W__plus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_5604,(0,1):C.GC_2446})

V_1560 = Vertex(name = 'V_1560',
                particles = [ P.e__plus__, P.e__minus__, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_5488,(0,1):C.GC_4740})

V_1561 = Vertex(name = 'V_1561',
                particles = [ P.mu__plus__, P.e__minus__, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_5533,(0,1):C.GC_4741})

V_1562 = Vertex(name = 'V_1562',
                particles = [ P.ta__plus__, P.e__minus__, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_5578,(0,1):C.GC_4742})

V_1563 = Vertex(name = 'V_1563',
                particles = [ P.e__plus__, P.mu__minus__, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_5503,(0,1):C.GC_4743})

V_1564 = Vertex(name = 'V_1564',
                particles = [ P.mu__plus__, P.mu__minus__, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_5548,(0,1):C.GC_4744})

V_1565 = Vertex(name = 'V_1565',
                particles = [ P.ta__plus__, P.mu__minus__, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_5593,(0,1):C.GC_4745})

V_1566 = Vertex(name = 'V_1566',
                particles = [ P.e__plus__, P.ta__minus__, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_5518,(0,1):C.GC_4746})

V_1567 = Vertex(name = 'V_1567',
                particles = [ P.mu__plus__, P.ta__minus__, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_5563,(0,1):C.GC_4747})

V_1568 = Vertex(name = 'V_1568',
                particles = [ P.ta__plus__, P.ta__minus__, P.W__minus__, P.W__plus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_5608,(0,1):C.GC_4748})

V_1569 = Vertex(name = 'V_1569',
                particles = [ P.u__tilde__, P.u, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_6166,(0,1):C.GC_2462})

V_1570 = Vertex(name = 'V_1570',
                particles = [ P.c__tilde__, P.u, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_6190,(0,1):C.GC_2463})

V_1571 = Vertex(name = 'V_1571',
                particles = [ P.t__tilde__, P.u, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_6214,(0,1):C.GC_2464})

V_1572 = Vertex(name = 'V_1572',
                particles = [ P.u__tilde__, P.c, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_6174,(0,1):C.GC_2465})

V_1573 = Vertex(name = 'V_1573',
                particles = [ P.c__tilde__, P.c, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_6198,(0,1):C.GC_2466})

V_1574 = Vertex(name = 'V_1574',
                particles = [ P.t__tilde__, P.c, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_6222,(0,1):C.GC_2467})

V_1575 = Vertex(name = 'V_1575',
                particles = [ P.u__tilde__, P.t, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_6182,(0,1):C.GC_2468})

V_1576 = Vertex(name = 'V_1576',
                particles = [ P.c__tilde__, P.t, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_6206,(0,1):C.GC_2469})

V_1577 = Vertex(name = 'V_1577',
                particles = [ P.t__tilde__, P.t, P.W__minus__, P.W__plus__, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_6230,(0,1):C.GC_2470})

V_1578 = Vertex(name = 'V_1578',
                particles = [ P.u__tilde__, P.u, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_6167,(0,1):C.GC_4764})

V_1579 = Vertex(name = 'V_1579',
                particles = [ P.c__tilde__, P.u, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_6191,(0,1):C.GC_4765})

V_1580 = Vertex(name = 'V_1580',
                particles = [ P.t__tilde__, P.u, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_6215,(0,1):C.GC_4766})

V_1581 = Vertex(name = 'V_1581',
                particles = [ P.u__tilde__, P.c, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_6175,(0,1):C.GC_4767})

V_1582 = Vertex(name = 'V_1582',
                particles = [ P.c__tilde__, P.c, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_6199,(0,1):C.GC_4768})

V_1583 = Vertex(name = 'V_1583',
                particles = [ P.t__tilde__, P.c, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_6223,(0,1):C.GC_4769})

V_1584 = Vertex(name = 'V_1584',
                particles = [ P.u__tilde__, P.t, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_6183,(0,1):C.GC_4770})

V_1585 = Vertex(name = 'V_1585',
                particles = [ P.c__tilde__, P.t, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_6207,(0,1):C.GC_4771})

V_1586 = Vertex(name = 'V_1586',
                particles = [ P.t__tilde__, P.t, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_6231,(0,1):C.GC_4772})

V_1587 = Vertex(name = 'V_1587',
                particles = [ P.d__tilde__, P.u, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3722,(0,1):C.GC_3740})

V_1588 = Vertex(name = 'V_1588',
                particles = [ P.s__tilde__, P.u, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3724,(0,1):C.GC_3742})

V_1589 = Vertex(name = 'V_1589',
                particles = [ P.b__tilde__, P.u, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3726,(0,1):C.GC_3744})

V_1590 = Vertex(name = 'V_1590',
                particles = [ P.d__tilde__, P.c, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3728,(0,1):C.GC_3746})

V_1591 = Vertex(name = 'V_1591',
                particles = [ P.s__tilde__, P.c, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3730,(0,1):C.GC_3748})

V_1592 = Vertex(name = 'V_1592',
                particles = [ P.b__tilde__, P.c, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3732,(0,1):C.GC_3750})

V_1593 = Vertex(name = 'V_1593',
                particles = [ P.d__tilde__, P.t, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3734,(0,1):C.GC_3752})

V_1594 = Vertex(name = 'V_1594',
                particles = [ P.s__tilde__, P.t, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3736,(0,1):C.GC_3754})

V_1595 = Vertex(name = 'V_1595',
                particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3738,(0,1):C.GC_3756})

V_1596 = Vertex(name = 'V_1596',
                particles = [ P.d__tilde__, P.u, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4798,(0,1):C.GC_4816})

V_1597 = Vertex(name = 'V_1597',
                particles = [ P.s__tilde__, P.u, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4800,(0,1):C.GC_4818})

V_1598 = Vertex(name = 'V_1598',
                particles = [ P.b__tilde__, P.u, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4802,(0,1):C.GC_4820})

V_1599 = Vertex(name = 'V_1599',
                particles = [ P.d__tilde__, P.c, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4804,(0,1):C.GC_4822})

V_1600 = Vertex(name = 'V_1600',
                particles = [ P.s__tilde__, P.c, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4806,(0,1):C.GC_4824})

V_1601 = Vertex(name = 'V_1601',
                particles = [ P.b__tilde__, P.c, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4808,(0,1):C.GC_4826})

V_1602 = Vertex(name = 'V_1602',
                particles = [ P.d__tilde__, P.t, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4810,(0,1):C.GC_4828})

V_1603 = Vertex(name = 'V_1603',
                particles = [ P.s__tilde__, P.t, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4812,(0,1):C.GC_4830})

V_1604 = Vertex(name = 'V_1604',
                particles = [ P.b__tilde__, P.t, P.W__minus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4814,(0,1):C.GC_4832})

V_1605 = Vertex(name = 'V_1605',
                particles = [ P.u__tilde__, P.d, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3767,(0,1):C.GC_3785})

V_1606 = Vertex(name = 'V_1606',
                particles = [ P.c__tilde__, P.d, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3769,(0,1):C.GC_3787})

V_1607 = Vertex(name = 'V_1607',
                particles = [ P.t__tilde__, P.d, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3771,(0,1):C.GC_3789})

V_1608 = Vertex(name = 'V_1608',
                particles = [ P.u__tilde__, P.s, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3773,(0,1):C.GC_3791})

V_1609 = Vertex(name = 'V_1609',
                particles = [ P.c__tilde__, P.s, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3775,(0,1):C.GC_3793})

V_1610 = Vertex(name = 'V_1610',
                particles = [ P.t__tilde__, P.s, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3777,(0,1):C.GC_3795})

V_1611 = Vertex(name = 'V_1611',
                particles = [ P.u__tilde__, P.b, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3779,(0,1):C.GC_3797})

V_1612 = Vertex(name = 'V_1612',
                particles = [ P.c__tilde__, P.b, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3781,(0,1):C.GC_3799})

V_1613 = Vertex(name = 'V_1613',
                particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVVS1, L.FFVVS3 ],
                couplings = {(0,0):C.GC_3783,(0,1):C.GC_3801})

V_1614 = Vertex(name = 'V_1614',
                particles = [ P.u__tilde__, P.d, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4843,(0,1):C.GC_4861})

V_1615 = Vertex(name = 'V_1615',
                particles = [ P.c__tilde__, P.d, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4845,(0,1):C.GC_4863})

V_1616 = Vertex(name = 'V_1616',
                particles = [ P.t__tilde__, P.d, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4847,(0,1):C.GC_4865})

V_1617 = Vertex(name = 'V_1617',
                particles = [ P.u__tilde__, P.s, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4849,(0,1):C.GC_4867})

V_1618 = Vertex(name = 'V_1618',
                particles = [ P.c__tilde__, P.s, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4851,(0,1):C.GC_4869})

V_1619 = Vertex(name = 'V_1619',
                particles = [ P.t__tilde__, P.s, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4853,(0,1):C.GC_4871})

V_1620 = Vertex(name = 'V_1620',
                particles = [ P.u__tilde__, P.b, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4855,(0,1):C.GC_4873})

V_1621 = Vertex(name = 'V_1621',
                particles = [ P.c__tilde__, P.b, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4857,(0,1):C.GC_4875})

V_1622 = Vertex(name = 'V_1622',
                particles = [ P.t__tilde__, P.b, P.W__plus__, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFVV1, L.FFVV2 ],
                couplings = {(0,0):C.GC_4859,(0,1):C.GC_4877})

V_1623 = Vertex(name = 'V_1623',
                particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1 ],
                couplings = {(0,0):C.GC_5485})

V_1624 = Vertex(name = 'V_1624',
                particles = [ P.vm__tilde__, P.e__minus__, P.W__plus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1 ],
                couplings = {(0,0):C.GC_5530})

V_1625 = Vertex(name = 'V_1625',
                particles = [ P.vt__tilde__, P.e__minus__, P.W__plus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1 ],
                couplings = {(0,0):C.GC_5575})

V_1626 = Vertex(name = 'V_1626',
                particles = [ P.ve__tilde__, P.mu__minus__, P.W__plus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1 ],
                couplings = {(0,0):C.GC_5500})

V_1627 = Vertex(name = 'V_1627',
                particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1 ],
                couplings = {(0,0):C.GC_5545})

V_1628 = Vertex(name = 'V_1628',
                particles = [ P.vt__tilde__, P.mu__minus__, P.W__plus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1 ],
                couplings = {(0,0):C.GC_5590})

V_1629 = Vertex(name = 'V_1629',
                particles = [ P.ve__tilde__, P.ta__minus__, P.W__plus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1 ],
                couplings = {(0,0):C.GC_5515})

V_1630 = Vertex(name = 'V_1630',
                particles = [ P.vm__tilde__, P.ta__minus__, P.W__plus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1 ],
                couplings = {(0,0):C.GC_5560})

V_1631 = Vertex(name = 'V_1631',
                particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS1 ],
                couplings = {(0,0):C.GC_5605})

V_1632 = Vertex(name = 'V_1632',
                particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_5489})

V_1633 = Vertex(name = 'V_1633',
                particles = [ P.vm__tilde__, P.e__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_5534})

V_1634 = Vertex(name = 'V_1634',
                particles = [ P.vt__tilde__, P.e__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_5579})

V_1635 = Vertex(name = 'V_1635',
                particles = [ P.ve__tilde__, P.mu__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_5504})

V_1636 = Vertex(name = 'V_1636',
                particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_5549})

V_1637 = Vertex(name = 'V_1637',
                particles = [ P.vt__tilde__, P.mu__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_5594})

V_1638 = Vertex(name = 'V_1638',
                particles = [ P.ve__tilde__, P.ta__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_5519})

V_1639 = Vertex(name = 'V_1639',
                particles = [ P.vm__tilde__, P.ta__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_5564})

V_1640 = Vertex(name = 'V_1640',
                particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV1 ],
                couplings = {(0,0):C.GC_5609})

V_1641 = Vertex(name = 'V_1641',
                particles = [ P.e__plus__, P.ve, P.a, P.W__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_4379})

V_1642 = Vertex(name = 'V_1642',
                particles = [ P.mu__plus__, P.ve, P.a, P.W__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_4380})

V_1643 = Vertex(name = 'V_1643',
                particles = [ P.ta__plus__, P.ve, P.a, P.W__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_4381})

V_1644 = Vertex(name = 'V_1644',
                particles = [ P.e__plus__, P.vm, P.a, P.W__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_4382})

V_1645 = Vertex(name = 'V_1645',
                particles = [ P.mu__plus__, P.vm, P.a, P.W__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_4383})

V_1646 = Vertex(name = 'V_1646',
                particles = [ P.ta__plus__, P.vm, P.a, P.W__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_4384})

V_1647 = Vertex(name = 'V_1647',
                particles = [ P.e__plus__, P.vt, P.a, P.W__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_4385})

V_1648 = Vertex(name = 'V_1648',
                particles = [ P.mu__plus__, P.vt, P.a, P.W__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_4386})

V_1649 = Vertex(name = 'V_1649',
                particles = [ P.ta__plus__, P.vt, P.a, P.W__minus__, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_4387})

V_1650 = Vertex(name = 'V_1650',
                particles = [ P.e__plus__, P.ve, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_4879})

V_1651 = Vertex(name = 'V_1651',
                particles = [ P.mu__plus__, P.ve, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_4880})

V_1652 = Vertex(name = 'V_1652',
                particles = [ P.ta__plus__, P.ve, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_4881})

V_1653 = Vertex(name = 'V_1653',
                particles = [ P.e__plus__, P.vm, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_4882})

V_1654 = Vertex(name = 'V_1654',
                particles = [ P.mu__plus__, P.vm, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_4883})

V_1655 = Vertex(name = 'V_1655',
                particles = [ P.ta__plus__, P.vm, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_4884})

V_1656 = Vertex(name = 'V_1656',
                particles = [ P.e__plus__, P.vt, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_4885})

V_1657 = Vertex(name = 'V_1657',
                particles = [ P.mu__plus__, P.vt, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_4886})

V_1658 = Vertex(name = 'V_1658',
                particles = [ P.ta__plus__, P.vt, P.a, P.W__minus__ ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_4887})

V_1659 = Vertex(name = 'V_1659',
                particles = [ P.e__plus__, P.ve, P.W__minus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_2471})

V_1660 = Vertex(name = 'V_1660',
                particles = [ P.mu__plus__, P.ve, P.W__minus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_2472})

V_1661 = Vertex(name = 'V_1661',
                particles = [ P.ta__plus__, P.ve, P.W__minus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_2473})

V_1662 = Vertex(name = 'V_1662',
                particles = [ P.e__plus__, P.vm, P.W__minus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_2474})

V_1663 = Vertex(name = 'V_1663',
                particles = [ P.mu__plus__, P.vm, P.W__minus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_2475})

V_1664 = Vertex(name = 'V_1664',
                particles = [ P.ta__plus__, P.vm, P.W__minus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_2476})

V_1665 = Vertex(name = 'V_1665',
                particles = [ P.e__plus__, P.vt, P.W__minus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_2477})

V_1666 = Vertex(name = 'V_1666',
                particles = [ P.mu__plus__, P.vt, P.W__minus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_2478})

V_1667 = Vertex(name = 'V_1667',
                particles = [ P.ta__plus__, P.vt, P.W__minus__, P.Z, P.H ],
                color = [ '1' ],
                lorentz = [ L.FFVVS3 ],
                couplings = {(0,0):C.GC_2479})

V_1668 = Vertex(name = 'V_1668',
                particles = [ P.e__plus__, P.ve, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_4773})

V_1669 = Vertex(name = 'V_1669',
                particles = [ P.mu__plus__, P.ve, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_4774})

V_1670 = Vertex(name = 'V_1670',
                particles = [ P.ta__plus__, P.ve, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_4775})

V_1671 = Vertex(name = 'V_1671',
                particles = [ P.e__plus__, P.vm, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_4776})

V_1672 = Vertex(name = 'V_1672',
                particles = [ P.mu__plus__, P.vm, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_4777})

V_1673 = Vertex(name = 'V_1673',
                particles = [ P.ta__plus__, P.vm, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_4778})

V_1674 = Vertex(name = 'V_1674',
                particles = [ P.e__plus__, P.vt, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_4779})

V_1675 = Vertex(name = 'V_1675',
                particles = [ P.mu__plus__, P.vt, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_4780})

V_1676 = Vertex(name = 'V_1676',
                particles = [ P.ta__plus__, P.vt, P.W__minus__, P.Z ],
                color = [ '1' ],
                lorentz = [ L.FFVV2 ],
                couplings = {(0,0):C.GC_4781})

