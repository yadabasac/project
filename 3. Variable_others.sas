/*I. Cash Estimation Equation*/

/*libname tmp1 '/home/u63644257/Data';*/
libname tmp1 '//apporto.com/dfs/SEA/Users/yso1_sea/Desktop/Finance Class/Data';
run;

data a1; set tmp1.r_all;
gvkey2=gvkey*1;
nyear=year(datadate);
if not missing(nyear);
if not missing(gvkey2);
proc sort nodupkey; by gvkey2 nyear;run;

/* ******************** */
/*0. Create Cash*/
/* ******************** */

data a2; set a1;
if not missing(at);
if not missing(che);
keep gvkey2 nyear at che; run;

data a3; set a2;
if (at-che)=0 then delete;
che2=che/(at-che);
if che2 ne ".";run;

data a4; set a3;
keep gvkey2 nyear che2;
proc means; run;

data tmp1.m_che2; set a4;run;



/* ******************** */
/*1. Create Firm Size*/
/* ******************** */

data a2; set a1;
if not missing(at);
keep gvkey2 nyear at;run;

data a3; set a2;
if at ne 0;
size=log(at);
if size ne ".";run;

data a4; set a3;
keep gvkey2 nyear size;
proc means; run;

data tmp1.m_size; set a4;run;




/* ******************** */
/*2. Create Net Working Capital*/
/* ******************** */

data a2; set a1;
if not missing(act);
if not missing(lct);
if not missing(at);
if not missing(che);
keep gvkey2 nyear act lct at che;run;

data a3; set a2;
if (at-che) ne 0;
nwc=(act-lct-che)/(at-che);
if nwc ne ".";run;

data a4; set a3;
keep gvkey2 nyear nwc;
proc means;run;

data tmp1.m_nwc; set a4;run;

/* ******************** */
/*3. Create Capital Expenditures*/
/* ******************** */

data a2; set a1;
if not missing(capx);
if not missing(che);
if not missing(at);
keep gvkey2 nyear capx at che;run;


data a3; set a2;
if (at-che) ne 0;
capx2=capx/(at-che);
if capx2 ne ".";run;

data a4; set a3;
keep gvkey2 nyear capx2;
proc means; run;

data tmp1.m_capx; set a4;run;

/* ******************** */
/*4. Create Industry Sigma/Cash Flow*/
/* ******************** */


/* ******************** */
/*5. Create Research and Development*/
/* ******************** */

data a2; set a1;
if missing(xrd) then xrd = 0;
keep gvkey2 nyear xrd at;run;

data a3; set a2;
if at ne 0;
xrd2=xrd/at;
if xrd2 ne ".";run;

data a4; set a3;
keep gvkey2 nyear xrd2;
proc means; run;

data tmp1.m_xrd; set a4;run;


/* ******************** */
/*6. Create Dividend Dummy*/
/* ******************** */

data a2; set a1;
if missing(dvc) then dvc=0;
keep gvkey2 nyear dvc;
proc sort; by gvkey2 nyear;run;

data a3; set a2;
by gvkey2;
first = first.gvkey2; 
prev_dvc= lag(dvc);
if first = 1 then prev_dvc = 0;
run;

data a4; set a3;
if missing(prev_dvc) then prev_dvc =0;
dvc2 = 0;
if prev_dvc > 0 then dvc2 = 1;
if prev_dvc <= 0 then dvc2 = 0;
keep gvkey2 nyear dvc2;
proc means;run;

data tmp1.m_dividend; set a4;run;

/* ******************** */
/*7. Create sales growth */
/* ******************** */

data a2; set a1;
if not missing(sale);
keep gvkey2 sale nyear ;
proc sort; by gvkey2 nyear;run;

data a3; set a2;
by gvkey2;
first = first.gvkey2; 
prev_sale= lag(sale);
if first = 1 then prev_sale = 0;
run;

data a4; set a3;
if prev_sale ne '.';
if prev_sale ne 0;
salesgrowth = (sale-prev_sale)/prev_sale;
if salesgrowth ne '.';
keep gvkey2 nyear salesgrowth;
proc means; run;

data tmp1.m_salesgrowth; set a4;run;

/* ******************** */
/*8. Create Cash From Operation */
/* ******************** */

data a2; set a1;
if not missing(oancf);
if not missing(che);
if not missing(at);
keep gvkey2 nyear oancf at che;
proc means; run;

/*proc print data=a2(obs=100);run;*/

data a3; set a2;
if (at-che) ne 0;
cashop=oancf/(at-che);
if cashop ne ".";run;

data a4; set a3;
keep gvkey2 nyear cashop;
proc means; run;

data tmp1.m_cashop; set a4;run;

/* ******************** */
/*10. Create Tax Burden on Foreign Income*/
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
