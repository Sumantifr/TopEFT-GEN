# This file was automatically created by FeynRules 2.3.27
# Mathematica version: 9.0 for Mac OS X x86 (64-bit) (November 20, 2012)
# Date: Sun 20 Aug 2017 21:26:04


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '2*ee**2*complex(0,1)',
                order = {'QED':2})

GC_7 = Coupling(name = 'GC_7',
                value = '-ee**2/(2.*cw)',
                order = {'QED':2})

GC_8 = Coupling(name = 'GC_8',
                value = '(ee**2*complex(0,1))/(2.*cw)',
                order = {'QED':2})

GC_9 = Coupling(name = 'GC_9',
                value = 'ee**2/(2.*cw)',
                order = {'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '-G',
                 order = {'QCD':1})

GC_11 = Coupling(name = 'GC_11',
                 value = 'complex(0,1)*G',
                 order = {'QCD':1})

GC_12 = Coupling(name = 'GC_12',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_13 = Coupling(name = 'GC_13',
                 value = '-2*complex(0,1)*lam',
                 order = {'QED':2})

GC_14 = Coupling(name = 'GC_14',
                 value = '-4*complex(0,1)*lam',
                 order = {'QED':2})

GC_15 = Coupling(name = 'GC_15',
                 value = '-6*complex(0,1)*lam',
                 order = {'QED':2})

GC_16 = Coupling(name = 'GC_16',
                 value = '(-4*cblSI1)/Lambda**2 - (4*cblS1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '-(cblSI1/Lambda**2) - (cblS1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '-(cblSI1/Lambda**2) + (cblS1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_19 = Coupling(name = 'GC_19',
                 value = 'cblSI1/Lambda**2 - (cblS1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_20 = Coupling(name = 'GC_20',
                 value = 'cblSI1/Lambda**2 + (cblS1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '(4*cblSI1)/Lambda**2 - (4*cblS1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '(-4*cblSI2)/Lambda**2 - (4*cblS2*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_23 = Coupling(name = 'GC_23',
                 value = '-(cblSI2/Lambda**2) - (cblS2*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '-(cblSI2/Lambda**2) + (cblS2*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_25 = Coupling(name = 'GC_25',
                 value = 'cblSI2/Lambda**2 - (cblS2*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_26 = Coupling(name = 'GC_26',
                 value = 'cblSI2/Lambda**2 + (cblS2*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '(4*cblSI2)/Lambda**2 - (4*cblS2*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '-(cbWI/Lambda**2) + (cbW*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_29 = Coupling(name = 'GC_29',
                 value = 'cbWI/Lambda**2 - (cbW*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_30 = Coupling(name = 'GC_30',
                 value = 'cbWI/Lambda**2 + (cbW*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '(2*cQl31*complex(0,1))/Lambda**2 + (cQlM1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '(2*cQl32*complex(0,1))/Lambda**2 + (cQlM2*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '(cQq11*complex(0,1))/Lambda**2 - (cQq13*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '(cQq11*complex(0,1))/Lambda**2 + (cQq13*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '(cQQ1*complex(0,1))/Lambda**2 + (cQQ8*complex(0,1))/(3.*Lambda**2)',
                 order = {'DIM6':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '(cQq81*complex(0,1))/Lambda**2 - (cQq83*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '(cQq81*complex(0,1))/Lambda**2 + (cQq83*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_38 = Coupling(name = 'GC_38',
                 value = 'ctlSI1/Lambda**2 - (4*ctlTI1)/Lambda**2 + (ctlS1*complex(0,1))/Lambda**2 - (4*ctlT1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_39 = Coupling(name = 'GC_39',
                 value = 'ctlSI1/Lambda**2 - (4*ctlTI1)/Lambda**2 - (ctlS1*complex(0,1))/Lambda**2 + (4*ctlT1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '-(ctlTI1/Lambda**2) - (ctlT1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '-(ctlTI1/Lambda**2) + (ctlT1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_42 = Coupling(name = 'GC_42',
                 value = 'ctlTI1/Lambda**2 - (ctlT1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_43 = Coupling(name = 'GC_43',
                 value = 'ctlTI1/Lambda**2 + (ctlT1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '-(ctlSI1/Lambda**2) + (4*ctlTI1)/Lambda**2 + (ctlS1*complex(0,1))/Lambda**2 - (4*ctlT1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '-(ctlSI1/Lambda**2) + (4*ctlTI1)/Lambda**2 - (ctlS1*complex(0,1))/Lambda**2 + (4*ctlT1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_46 = Coupling(name = 'GC_46',
                 value = 'ctlSI2/Lambda**2 - (4*ctlTI2)/Lambda**2 + (ctlS2*complex(0,1))/Lambda**2 - (4*ctlT2*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_47 = Coupling(name = 'GC_47',
                 value = 'ctlSI2/Lambda**2 - (4*ctlTI2)/Lambda**2 - (ctlS2*complex(0,1))/Lambda**2 + (4*ctlT2*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '-(ctlTI2/Lambda**2) - (ctlT2*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '-(ctlTI2/Lambda**2) + (ctlT2*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_50 = Coupling(name = 'GC_50',
                 value = 'ctlTI2/Lambda**2 - (ctlT2*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_51 = Coupling(name = 'GC_51',
                 value = 'ctlTI2/Lambda**2 + (ctlT2*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '-(ctlSI2/Lambda**2) + (4*ctlTI2)/Lambda**2 + (ctlS2*complex(0,1))/Lambda**2 - (4*ctlT2*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '-(ctlSI2/Lambda**2) + (4*ctlTI2)/Lambda**2 - (ctlS2*complex(0,1))/Lambda**2 + (4*ctlT2*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_54 = Coupling(name = 'GC_54',
                 value = '-(ctWI/Lambda**2) - (ctW*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '-(ctWI/Lambda**2) + (ctW*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_56 = Coupling(name = 'GC_56',
                 value = 'ctWI/Lambda**2 + (ctW*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '-(ctZI/(Lambda**2*cmath.sqrt(2))) - (ctZ*complex(0,1))/(Lambda**2*cmath.sqrt(2))',
                 order = {'DIM6':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '-(ctZI/(Lambda**2*cmath.sqrt(2))) + (ctZ*complex(0,1))/(Lambda**2*cmath.sqrt(2))',
                 order = {'DIM6':1})

GC_59 = Coupling(name = 'GC_59',
                 value = 'ctZI/(Lambda**2*cmath.sqrt(2)) - (ctZ*complex(0,1))/(Lambda**2*cmath.sqrt(2))',
                 order = {'DIM6':1})

GC_60 = Coupling(name = 'GC_60',
                 value = 'ctZI/(Lambda**2*cmath.sqrt(2)) + (ctZ*complex(0,1))/(Lambda**2*cmath.sqrt(2))',
                 order = {'DIM6':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '-((cbWI*cw)/(Lambda**2*cmath.sqrt(2))) - (cbW*cw*complex(0,1))/(Lambda**2*cmath.sqrt(2))',
                 order = {'DIM6':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '-((cbWI*cw)/(Lambda**2*cmath.sqrt(2))) + (cbW*cw*complex(0,1))/(Lambda**2*cmath.sqrt(2))',
                 order = {'DIM6':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '(cbWI*cw)/(Lambda**2*cmath.sqrt(2)) - (cbW*cw*complex(0,1))/(Lambda**2*cmath.sqrt(2))',
                 order = {'DIM6':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '(cbWI*cw)/(Lambda**2*cmath.sqrt(2)) + (cbW*cw*complex(0,1))/(Lambda**2*cmath.sqrt(2))',
                 order = {'DIM6':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '-((cblS1*complex(0,1))/Lambda**2)',
                 order = {'DIM6':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '(cblS1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_67 = Coupling(name = 'GC_67',
                 value = 'cblSI1/Lambda**2',
                 order = {'DIM6':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '(cQb1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '(cQb8*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '(cQd1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '(cQd8*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '(cQe1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '(cQe2*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '(2*cQl31*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '(2*cQl32*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '(cQlM1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_77 = Coupling(name = 'GC_77',
                 value = '(cQlM2*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_78 = Coupling(name = 'GC_78',
                 value = '(cQQ1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_79 = Coupling(name = 'GC_79',
                 value = '(2*cQq13*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '-(cQQ8*complex(0,1))/(6.*Lambda**2)',
                 order = {'DIM6':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '(cQQ8*complex(0,1))/(2.*Lambda**2)',
                 order = {'DIM6':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '(cQq81*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '-((cQq83*complex(0,1))/Lambda**2)',
                 order = {'DIM6':1})

GC_84 = Coupling(name = 'GC_84',
                 value = '(2*cQq83*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '(cQt1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_86 = Coupling(name = 'GC_86',
                 value = '(cQt8*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '(cQu1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_88 = Coupling(name = 'GC_88',
                 value = '(cQu8*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '(ctb1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_90 = Coupling(name = 'GC_90',
                 value = '(ctb8*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '(ctd1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_92 = Coupling(name = 'GC_92',
                 value = '(ctd8*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_93 = Coupling(name = 'GC_93',
                 value = '(cte1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_94 = Coupling(name = 'GC_94',
                 value = '(cte2*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

#GC_95 = Coupling(name = 'GC_95',
#                 value = '(ctG*complex(0,1))/(Lambda**2*cmath.sqrt(2))',
#                 order = {'DIM6':1})
#
#GC_96 = Coupling(name = 'GC_96',
#                 value = 'ctGI/(Lambda**2*cmath.sqrt(2))',
#                 order = {'DIM6':1})
GC_95 = Coupling(name = 'GC_95',
                 value = '(ctG*G*complex(0,1))/(Lambda**2*cmath.sqrt(2))',
                 order = {'DIM6':1, 'QCD':1})
GC_96 = Coupling(name = 'GC_96',
                 value = 'ctGI*G/(Lambda**2*cmath.sqrt(2))',
                 order = {'DIM6':1, 'QCD':1})
GC_97 = Coupling(name = 'GC_97',
                 value = '(ctl1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_98 = Coupling(name = 'GC_98',
                 value = '(ctl2*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '(ctq1*complex(0,1))/Lambda**2',
                 order = {'DIM6':1})

GC_100 = Coupling(name = 'GC_100',
                  value = '(ctq8*complex(0,1))/Lambda**2',
                  order = {'DIM6':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '(2*ctt1*complex(0,1))/Lambda**2',
                  order = {'DIM6':1})

GC_102 = Coupling(name = 'GC_102',
                  value = '(ctu1*complex(0,1))/Lambda**2',
                  order = {'DIM6':1})

GC_103 = Coupling(name = 'GC_103',
                  value = '(ctu8*complex(0,1))/Lambda**2',
                  order = {'DIM6':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '-(ee**2*complex(0,1)) + (ee**2*complex(0,1))/sw**2',
                  order = {'QED':2})

GC_105 = Coupling(name = 'GC_105',
                  value = 'ctWI/(Lambda**2*sw*cmath.sqrt(2)) - (ctZI*cw)/(Lambda**2*sw*cmath.sqrt(2)) + (ctW*complex(0,1))/(Lambda**2*sw*cmath.sqrt(2)) - (ctZ*cw*complex(0,1))/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'DIM6':1})

GC_106 = Coupling(name = 'GC_106',
                  value = 'ctWI/(Lambda**2*sw*cmath.sqrt(2)) - (ctZI*cw)/(Lambda**2*sw*cmath.sqrt(2)) - (ctW*complex(0,1))/(Lambda**2*sw*cmath.sqrt(2)) + (ctZ*cw*complex(0,1))/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'DIM6':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '-(ctWI/(Lambda**2*sw*cmath.sqrt(2))) + (ctZI*cw)/(Lambda**2*sw*cmath.sqrt(2)) + (ctW*complex(0,1))/(Lambda**2*sw*cmath.sqrt(2)) - (ctZ*cw*complex(0,1))/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'DIM6':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '-(ctWI/(Lambda**2*sw*cmath.sqrt(2))) + (ctZI*cw)/(Lambda**2*sw*cmath.sqrt(2)) - (ctW*complex(0,1))/(Lambda**2*sw*cmath.sqrt(2)) + (ctZ*cw*complex(0,1))/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'DIM6':1})

GC_109 = Coupling(name = 'GC_109',
                  value = '(ee**2*complex(0,1))/(2.*sw**2)',
                  order = {'QED':2})

GC_110 = Coupling(name = 'GC_110',
                  value = '-((ee**2*complex(0,1))/sw**2)',
                  order = {'QED':2})

GC_111 = Coupling(name = 'GC_111',
                  value = '-ee/(2.*sw)',
                  order = {'QED':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '-(ee*complex(0,1))/(2.*sw)',
                  order = {'QED':1})

GC_113 = Coupling(name = 'GC_113',
                  value = '(ee*complex(0,1))/(2.*sw)',
                  order = {'QED':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_115 = Coupling(name = 'GC_115',
                  value = '-((cw*ee*complex(0,1))/sw)',
                  order = {'QED':1})

GC_116 = Coupling(name = 'GC_116',
                  value = '(cw*ee*complex(0,1))/sw',
                  order = {'QED':1})

GC_117 = Coupling(name = 'GC_117',
                  value = '-ee**2/(2.*sw)',
                  order = {'QED':2})

GC_118 = Coupling(name = 'GC_118',
                  value = '-(ee**2*complex(0,1))/(2.*sw)',
                  order = {'QED':2})

GC_119 = Coupling(name = 'GC_119',
                  value = 'ee**2/(2.*sw)',
                  order = {'QED':2})

GC_120 = Coupling(name = 'GC_120',
                  value = '(-2*cw*ee**2*complex(0,1))/sw',
                  order = {'QED':2})

GC_121 = Coupling(name = 'GC_121',
                  value = '(ee*complex(0,1)*sw)/(3.*cw)',
                  order = {'QED':1})

GC_122 = Coupling(name = 'GC_122',
                  value = '(-2*ee*complex(0,1)*sw)/(3.*cw)',
                  order = {'QED':1})

GC_123 = Coupling(name = 'GC_123',
                  value = '(ee*complex(0,1)*sw)/cw',
                  order = {'QED':1})

GC_124 = Coupling(name = 'GC_124',
                  value = '-((cbW*complex(0,1)*sw)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'DIM6':1})

GC_125 = Coupling(name = 'GC_125',
                  value = '-((cbWI*sw)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'DIM6':1})

GC_126 = Coupling(name = 'GC_126',
                  value = '-(cw*ee)/(2.*sw) - (ee*sw)/(2.*cw)',
                  order = {'QED':1})

GC_127 = Coupling(name = 'GC_127',
                  value = '-(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                  order = {'QED':1})

GC_128 = Coupling(name = 'GC_128',
                  value = '(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                  order = {'QED':1})

GC_129 = Coupling(name = 'GC_129',
                  value = '-(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_131 = Coupling(name = 'GC_131',
                  value = '(cw*ee**2*complex(0,1))/sw - (ee**2*complex(0,1)*sw)/cw',
                  order = {'QED':2})

GC_132 = Coupling(name = 'GC_132',
                  value = '(ee**2*complex(0,1))/2. + (ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_133 = Coupling(name = 'GC_133',
                  value = '(-3*ee**2*complex(0,1))/2. + (ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_134 = Coupling(name = 'GC_134',
                  value = '-(ee**2*vev)/(2.*cw)',
                  order = {'QED':1})

GC_135 = Coupling(name = 'GC_135',
                  value = '(ee**2*vev)/(2.*cw)',
                  order = {'QED':1})

GC_136 = Coupling(name = 'GC_136',
                  value = '-2*complex(0,1)*lam*vev',
                  order = {'QED':1})

GC_137 = Coupling(name = 'GC_137',
                  value = '-6*complex(0,1)*lam*vev',
                  order = {'QED':1})

GC_138 = Coupling(name = 'GC_138',
                  value = '(ctG*G*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'DIM6':1, 'QCD':1,'QED':-1})

GC_139 = Coupling(name = 'GC_139',
                  value = '(ctGI*G*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'DIM6':1, 'QCD':1,'QED':-1})

#GC_138 = Coupling(name = 'GC_138',
#                  value = '(ctG*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2))',
#                  order = {'DIM6':1,'QED':-1})
#
#GC_139 = Coupling(name = 'GC_139',
#                  value = '(ctGI*vev)/(Lambda**2*cmath.sqrt(2))',
#                  order = {'DIM6':1,'QED':-1})
#
GC_140 = Coupling(name = 'GC_140',
                  value = '(3*ctp*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'DIM6':1,'QED':-1})

GC_141 = Coupling(name = 'GC_141',
                  value = '(3*ctpI*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'DIM6':1,'QED':-1})

GC_142 = Coupling(name = 'GC_142',
                  value = '-((ctW*complex(0,1)*vev)/Lambda**2)',
                  order = {'DIM6':1,'QED':-1})

GC_143 = Coupling(name = 'GC_143',
                  value = '-((ctWI*vev)/Lambda**2)',
                  order = {'DIM6':1,'QED':-1})

#GC_144 = Coupling(name = 'GC_144',
#                  value = '-((ctG*G*vev)/(Lambda**2*cmath.sqrt(2)))',
#                  order = {'DIM6':1,'QCD':1,'QED':-1})
#
#GC_145 = Coupling(name = 'GC_145',
#                  value = '(ctGI*complex(0,1)*G*vev)/(Lambda**2*cmath.sqrt(2))',
#                  order = {'DIM6':1,'QCD':1,'QED':-1})

GC_144 = Coupling(name = 'GC_144',
                  value = '-((ctG*G*G*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'DIM6':1, 'QCD':2,'QED':-1})
GC_145 = Coupling(name = 'GC_145',
                  value = '(ctGI*G*complex(0,1)*G*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'DIM6':1, 'QCD':2,'QED':-1})

GC_146 = Coupling(name = 'GC_146',
                  value = '-(ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_147 = Coupling(name = 'GC_147',
                  value = '-(ee**2*complex(0,1)*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_148 = Coupling(name = 'GC_148',
                  value = '(ee**2*complex(0,1)*vev)/(2.*sw**2)',
                  order = {'QED':1})

GC_149 = Coupling(name = 'GC_149',
                  value = '(ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_150 = Coupling(name = 'GC_150',
                  value = '-(ee**2*vev)/(2.*sw)',
                  order = {'QED':1})

GC_151 = Coupling(name = 'GC_151',
                  value = '(ee**2*vev)/(2.*sw)',
                  order = {'QED':1})

GC_152 = Coupling(name = 'GC_152',
                  value = '-((cbW*ee*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'DIM6':1})

GC_153 = Coupling(name = 'GC_153',
                  value = '-((cbWI*ee*vev)/(Lambda**2*sw*cmath.sqrt(2)))',
                  order = {'DIM6':1})

GC_154 = Coupling(name = 'GC_154',
                  value = '(cpQ3*ee*complex(0,1)*vev*cmath.sqrt(2))/(Lambda**2*sw)',
                  order = {'DIM6':1})

GC_155 = Coupling(name = 'GC_155',
                  value = '(ctW*ee*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'DIM6':1})

GC_156 = Coupling(name = 'GC_156',
                  value = '(ctWI*ee*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'DIM6':1})

GC_157 = Coupling(name = 'GC_157',
                  value = '-((cbW*complex(0,1)*sw*vev)/(Lambda**2*cmath.sqrt(2)))',
                  order = {'DIM6':1,'QED':-1})

GC_158 = Coupling(name = 'GC_158',
                  value = '(cbWI*sw*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'DIM6':1,'QED':-1})

GC_159 = Coupling(name = 'GC_159',
                  value = '(ctp*complex(0,1)*vev**2)/(Lambda**2*cmath.sqrt(2))',
                  order = {'DIM6':1,'QED':-2})

GC_160 = Coupling(name = 'GC_160',
                  value = '(ctpI*vev**2)/(Lambda**2*cmath.sqrt(2))',
                  order = {'DIM6':1,'QED':-2})

GC_161 = Coupling(name = 'GC_161',
                  value = '(cpQ3*ee*complex(0,1)*vev**2)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'DIM6':1,'QED':-1})

GC_162 = Coupling(name = 'GC_162',
                  value = '-((cbWI*vev)/Lambda**2) + (cbW*complex(0,1)*vev)/Lambda**2',
                  order = {'DIM6':1,'QED':-1})

GC_163 = Coupling(name = 'GC_163',
                  value = '(cbWI*vev)/Lambda**2 - (cbW*complex(0,1)*vev)/Lambda**2',
                  order = {'DIM6':1,'QED':-1})

GC_164 = Coupling(name = 'GC_164',
                  value = '(cbWI*vev)/Lambda**2 + (cbW*complex(0,1)*vev)/Lambda**2',
                  order = {'DIM6':1,'QED':-1})

GC_165 = Coupling(name = 'GC_165',
                  value = '-((ctWI*vev)/Lambda**2) + (ctW*complex(0,1)*vev)/Lambda**2',
                  order = {'DIM6':1,'QED':-1})

GC_166 = Coupling(name = 'GC_166',
                  value = '(ctWI*vev)/Lambda**2 + (ctW*complex(0,1)*vev)/Lambda**2',
                  order = {'DIM6':1,'QED':-1})

GC_167 = Coupling(name = 'GC_167',
                  value = '-((ctZI*vev)/(Lambda**2*cmath.sqrt(2))) - (ctZ*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'DIM6':1,'QED':-1})

GC_168 = Coupling(name = 'GC_168',
                  value = '-((ctZI*vev)/(Lambda**2*cmath.sqrt(2))) + (ctZ*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'DIM6':1,'QED':-1})

GC_169 = Coupling(name = 'GC_169',
                  value = '(ctZI*vev)/(Lambda**2*cmath.sqrt(2)) - (ctZ*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'DIM6':1,'QED':-1})

GC_170 = Coupling(name = 'GC_170',
                  value = '(ctZI*vev)/(Lambda**2*cmath.sqrt(2)) + (ctZ*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'DIM6':1,'QED':-1})

GC_171 = Coupling(name = 'GC_171',
                  value = '-((cbWI*cw*vev)/(Lambda**2*cmath.sqrt(2))) - (cbW*cw*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'DIM6':1,'QED':-1})

GC_172 = Coupling(name = 'GC_172',
                  value = '-((cbWI*cw*vev)/(Lambda**2*cmath.sqrt(2))) + (cbW*cw*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'DIM6':1,'QED':-1})

GC_173 = Coupling(name = 'GC_173',
                  value = '(cbWI*cw*vev)/(Lambda**2*cmath.sqrt(2)) - (cbW*cw*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'DIM6':1,'QED':-1})

GC_174 = Coupling(name = 'GC_174',
                  value = '(cbWI*cw*vev)/(Lambda**2*cmath.sqrt(2)) + (cbW*cw*complex(0,1)*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'DIM6':1,'QED':-1})

GC_175 = Coupling(name = 'GC_175',
                  value = '-((cbWI*ee*vev)/Lambda**2) - (cbW*ee*complex(0,1)*vev)/Lambda**2',
                  order = {'DIM6':1})

GC_176 = Coupling(name = 'GC_176',
                  value = '-((cbWI*ee*vev)/Lambda**2) + (cbW*ee*complex(0,1)*vev)/Lambda**2',
                  order = {'DIM6':1})

GC_177 = Coupling(name = 'GC_177',
                  value = '(ctWI*ee*vev)/Lambda**2 - (ctW*ee*complex(0,1)*vev)/Lambda**2',
                  order = {'DIM6':1})

GC_178 = Coupling(name = 'GC_178',
                  value = '(ctWI*ee*vev)/Lambda**2 + (ctW*ee*complex(0,1)*vev)/Lambda**2',
                  order = {'DIM6':1})

GC_179 = Coupling(name = 'GC_179',
                  value = '-(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_180 = Coupling(name = 'GC_180',
                  value = '(ee**2*vev)/(4.*cw) - (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_181 = Coupling(name = 'GC_181',
                  value = '-(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_182 = Coupling(name = 'GC_182',
                  value = '(ee**2*vev)/(4.*cw) + (cw*ee**2*vev)/(4.*sw**2)',
                  order = {'QED':1})

GC_183 = Coupling(name = 'GC_183',
                  value = '(ctWI*vev)/(Lambda**2*sw*cmath.sqrt(2)) - (ctZI*cw*vev)/(Lambda**2*sw*cmath.sqrt(2)) + (ctW*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2)) - (ctZ*cw*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'DIM6':1,'QED':-1})

GC_184 = Coupling(name = 'GC_184',
                  value = '(ctWI*vev)/(Lambda**2*sw*cmath.sqrt(2)) - (ctZI*cw*vev)/(Lambda**2*sw*cmath.sqrt(2)) - (ctW*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2)) + (ctZ*cw*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'DIM6':1,'QED':-1})

GC_185 = Coupling(name = 'GC_185',
                  value = '-((ctWI*vev)/(Lambda**2*sw*cmath.sqrt(2))) + (ctZI*cw*vev)/(Lambda**2*sw*cmath.sqrt(2)) + (ctW*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2)) - (ctZ*cw*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'DIM6':1,'QED':-1})

GC_186 = Coupling(name = 'GC_186',
                  value = '-((ctWI*vev)/(Lambda**2*sw*cmath.sqrt(2))) + (ctZI*cw*vev)/(Lambda**2*sw*cmath.sqrt(2)) - (ctW*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2)) + (ctZ*cw*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'DIM6':1,'QED':-1})

GC_187 = Coupling(name = 'GC_187',
                  value = '-((cptbI*ee*vev)/(Lambda**2*sw*cmath.sqrt(2))) - (cptb*ee*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'DIM6':1})

GC_188 = Coupling(name = 'GC_188',
                  value = '(cptbI*ee*vev)/(Lambda**2*sw*cmath.sqrt(2)) - (cptb*ee*complex(0,1)*vev)/(Lambda**2*sw*cmath.sqrt(2))',
                  order = {'DIM6':1})

GC_189 = Coupling(name = 'GC_189',
                  value = '(cbWI*cw*ee*vev)/(Lambda**2*sw) - (cbW*cw*ee*complex(0,1)*vev)/(Lambda**2*sw)',
                  order = {'DIM6':1})

GC_190 = Coupling(name = 'GC_190',
                  value = '(cbWI*cw*ee*vev)/(Lambda**2*sw) + (cbW*cw*ee*complex(0,1)*vev)/(Lambda**2*sw)',
                  order = {'DIM6':1})

GC_191 = Coupling(name = 'GC_191',
                  value = '-((ctWI*cw*ee*vev)/(Lambda**2*sw)) - (ctW*cw*ee*complex(0,1)*vev)/(Lambda**2*sw)',
                  order = {'DIM6':1})

GC_192 = Coupling(name = 'GC_192',
                  value = '-((ctWI*cw*ee*vev)/(Lambda**2*sw)) + (ctW*cw*ee*complex(0,1)*vev)/(Lambda**2*sw)',
                  order = {'DIM6':1})

GC_193 = Coupling(name = 'GC_193',
                  value = '-((cbWI*sw*vev)/(Lambda**2*cmath.sqrt(2))) - (cbW*complex(0,1)*sw*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'DIM6':1,'QED':-1})

GC_194 = Coupling(name = 'GC_194',
                  value = '-((cbWI*sw*vev)/(Lambda**2*cmath.sqrt(2))) + (cbW*complex(0,1)*sw*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'DIM6':1,'QED':-1})

GC_195 = Coupling(name = 'GC_195',
                  value = '(cbWI*sw*vev)/(Lambda**2*cmath.sqrt(2)) + (cbW*complex(0,1)*sw*vev)/(Lambda**2*cmath.sqrt(2))',
                  order = {'DIM6':1,'QED':-1})

GC_196 = Coupling(name = 'GC_196',
                  value = '-((cpb*cw*ee*complex(0,1)*vev)/(Lambda**2*sw)) - (cpb*ee*complex(0,1)*sw*vev)/(cw*Lambda**2)',
                  order = {'DIM6':1})

GC_197 = Coupling(name = 'GC_197',
                  value = '-((cpQM*cw*ee*complex(0,1)*vev)/(Lambda**2*sw)) - (cpQM*ee*complex(0,1)*sw*vev)/(cw*Lambda**2)',
                  order = {'DIM6':1})

GC_198 = Coupling(name = 'GC_198',
                  value = '(-2*cpQ3*cw*ee*complex(0,1)*vev)/(Lambda**2*sw) - (cpQM*cw*ee*complex(0,1)*vev)/(Lambda**2*sw) - (2*cpQ3*ee*complex(0,1)*sw*vev)/(cw*Lambda**2) - (cpQM*ee*complex(0,1)*sw*vev)/(cw*Lambda**2)',
                  order = {'DIM6':1})

GC_199 = Coupling(name = 'GC_199',
                  value = '-((cpt*cw*ee*complex(0,1)*vev)/(Lambda**2*sw)) - (cpt*ee*complex(0,1)*sw*vev)/(cw*Lambda**2)',
                  order = {'DIM6':1})

GC_200 = Coupling(name = 'GC_200',
                  value = '-(ee**2*complex(0,1)*vev)/4. - (ee**2*complex(0,1)*vev)/(4.*sw**2) - (ee**2*complex(0,1)*sw**2*vev)/(4.*cw**2)',
                  order = {'QED':1})

GC_201 = Coupling(name = 'GC_201',
                  value = '(ee**2*complex(0,1)*vev)/2. + (ee**2*complex(0,1)*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                  order = {'QED':1})

GC_202 = Coupling(name = 'GC_202',
                  value = '-(cptbI*ee*vev**2)/(2.*Lambda**2*sw*cmath.sqrt(2)) - (cptb*ee*complex(0,1)*vev**2)/(2.*Lambda**2*sw*cmath.sqrt(2))',
                  order = {'DIM6':1,'QED':-1})

GC_203 = Coupling(name = 'GC_203',
                  value = '(cptbI*ee*vev**2)/(2.*Lambda**2*sw*cmath.sqrt(2)) - (cptb*ee*complex(0,1)*vev**2)/(2.*Lambda**2*sw*cmath.sqrt(2))',
                  order = {'DIM6':1,'QED':-1})

GC_204 = Coupling(name = 'GC_204',
                  value = '-(cpb*cw*ee*complex(0,1)*vev**2)/(2.*Lambda**2*sw) - (cpb*ee*complex(0,1)*sw*vev**2)/(2.*cw*Lambda**2)',
                  order = {'DIM6':1,'QED':-1})

GC_205 = Coupling(name = 'GC_205',
                  value = '-(cpQM*cw*ee*complex(0,1)*vev**2)/(2.*Lambda**2*sw) - (cpQM*ee*complex(0,1)*sw*vev**2)/(2.*cw*Lambda**2)',
                  order = {'DIM6':1,'QED':-1})

GC_206 = Coupling(name = 'GC_206',
                  value = '-((cpQ3*cw*ee*complex(0,1)*vev**2)/(Lambda**2*sw)) - (cpQM*cw*ee*complex(0,1)*vev**2)/(2.*Lambda**2*sw) - (cpQ3*ee*complex(0,1)*sw*vev**2)/(cw*Lambda**2) - (cpQM*ee*complex(0,1)*sw*vev**2)/(2.*cw*Lambda**2)',
                  order = {'DIM6':1,'QED':-1})

GC_207 = Coupling(name = 'GC_207',
                  value = '-(cpt*cw*ee*complex(0,1)*vev**2)/(2.*Lambda**2*sw) - (cpt*ee*complex(0,1)*sw*vev**2)/(2.*cw*Lambda**2)',
                  order = {'DIM6':1,'QED':-1})

GC_208 = Coupling(name = 'GC_208',
                  value = '-yb',
                  order = {'QED':1})

GC_209 = Coupling(name = 'GC_209',
                  value = 'yb',
                  order = {'QED':1})

GC_210 = Coupling(name = 'GC_210',
                  value = '-(yb/cmath.sqrt(2))',
                  order = {'QED':1})

GC_211 = Coupling(name = 'GC_211',
                  value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_212 = Coupling(name = 'GC_212',
                  value = 'yb/cmath.sqrt(2)',
                  order = {'QED':1})

GC_213 = Coupling(name = 'GC_213',
                  value = '-yt',
                  order = {'QED':1})

GC_214 = Coupling(name = 'GC_214',
                  value = 'yt',
                  order = {'QED':1})

GC_215 = Coupling(name = 'GC_215',
                  value = '-(yt/cmath.sqrt(2))',
                  order = {'QED':1})

GC_216 = Coupling(name = 'GC_216',
                  value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_217 = Coupling(name = 'GC_217',
                  value = 'yt/cmath.sqrt(2)',
                  order = {'QED':1})

GC_218 = Coupling(name = 'GC_218',
                  value = '-ytau',
                  order = {'QED':1})

GC_219 = Coupling(name = 'GC_219',
                  value = 'ytau',
                  order = {'QED':1})

GC_220 = Coupling(name = 'GC_220',
                  value = '-(ytau/cmath.sqrt(2))',
                  order = {'QED':1})

GC_221 = Coupling(name = 'GC_221',
                  value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_222 = Coupling(name = 'GC_222',
                  value = 'ytau/cmath.sqrt(2)',
                  order = {'QED':1})

