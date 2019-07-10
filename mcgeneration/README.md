### Summary
This directory contains EFT specific modifications and addons for cms-sw/genproductions which allow to prepare EFT gridpacks 

### Setup 
To run the gridpack generation using condor, a cms_connect account incl. registration is needed.
To sign up to cms_connect use the guide: http://connect.uscms.org/signup

Once the registration is complete, connect to the server, change to the working directory and get a voms certificate:
```
ssh username@login.uscms.org
cd /local-scratch/username/
voms-proxy-init -voms cms -valid 192:00
```
Details can be found here: https://ci-connect.atlassian.net/wiki/spaces/CMS/pages/6783080/CMS+Connect+Quickstart

### Set up TopEFT repository and genproductions 
```
    git clone https://github.com/cms-analysis/TopEFT.git
    cd TopEFT/mcgeneration
```

###  Add a new process or modifying EFT settings
For a new process, add a directory to addons/cards/CARDNAME containing a run card (CARDNAME_run_card.dat) and a process card (CARDNAME_proc_card.dat).
Create a customize card with the EFT reference point using make_customizecard.py (example given in make_customizecard.sh). Use --append if a customize card with e.g. mass settings already exists.
```
python make_customizecard.py --filename addons/cards/CARDNAME/CARDNAME_customizecards.dat --append --referencepoint ctZ 4 ctZI 4
```
Create a reweight card with the EFT parameters (of order ORDER) and the same reference point using make_reweight_card.py (example given in make_reweight_card.sh).
```
python make_reweight_card.py --overwrite --filename addons/cards/CARDNAME/CARDNAME_reweight_card.dat --referencepoint ctZ 4 ctZI 4 --couplings ORDER cpt 1 cpQM 1 ctZ 1 ctZI 1
```

You may want to add the addons/cards/CARDNAME to the repository and commit to cms-analysis/TopEFT but it is not required in the following.

### Create gridpacks
First, set up the production environment
```
    source setup_production.sh  
```
The command takes you to the production environment.
Then, submit gridpacks locally with
```
    ./submit_madpack_local.sh CARDNAME1 CARDNAME2 ...
```
or via cmsconnect
```
    nohup ./submit_madpack_cmsconnect.sh CARDNAME > CARDNAME.debug 2>&1 &
```

