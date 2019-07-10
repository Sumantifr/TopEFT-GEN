### summary
This directory contains EFT specific modifications and addons for cms-sw/genproductions which allow to prepare EFT gridpacks 

### instructions:  
 * execute setup_production.sh to checkout cms-sw/genproductions and merge dedicated EFT tools: 
 * make sure card files are under addons/cards/process_rwgt
 * for new processes that need a non-SM reference point (e.g. ctZ=ctZI=4), run e.g. 
```
    python make_customizecard.py --filename addons/cards/tWGamma_rwgt/tWGamma_rwgt_customizecards.dat --append --reference ctZ 4 ctZI 4 
```
 * to produce a reweight card  up to (for example) order 4 and for 6 EFT operators run
```
    python make_reweight_card.py --filename addons/cards/tWGamma_rwgt/tWGamma_rwgt_reweight_card.dat --reference ctZ 4 ctZI 4 --couplings 4 cpt 1 cpQM 1 ctZ 1 ctZI 1
```
 * run submit_madpack_ttbareft.sh to produce gridpacks 
   the script will copy card templates from  addons/cards/UFOMODEL_template and the corresponding UFO file in addons/models
   you can modify the copied cards according to your needs via sed in submit_madpack_ttbareft.sh
   afterwards jobs are submitted to lxplus condor 


