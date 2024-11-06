
libname tmp1 '//apporto.com/dfs/SEA/Users/yso1_sea/Desktop/Finance Class/Data';
run;

data a1; set tmp1.r_all;
gvkey2=gvkey*1;
nyear=year(datadate);
if not missing(nyear);
if not missing(gvkey2);
proc sort nodupkey; by gvkey2 nyear;run;


/* ******************** */
/*Create Tax Burden on Foreign Income*/
/* ******************** */

data a2; set a1;
if missing(pifo) then pifo =0;
if missing(txfo) then txfo =0;
if not missing(at);
if not missing(che);
keep gvkey2 nyear pifo txfo at che;run;

data a3; set a2;
us_tax = pifo*0.35;
tax_b=0;
if (at-che) ne 0;
if us_tax < txfo then tax_b=0;
if us_tax >= txfo then tax_b=(us_tax-txfo)*100/(at-che);
if tax_b ne ".";run;

data a4; set a3;
keep gvkey2 nyear tax_b;
proc means;run;

data tmp1.m_tax; set a4;run;
