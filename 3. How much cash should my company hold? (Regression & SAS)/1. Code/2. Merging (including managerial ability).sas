
libname tmp1 '\\apporto.com\dfs\SEA\Users\yso1_sea\Desktop\Finance Class\Data';
run;

/* ******************** */
/*Merging Data*/
/* ******************** */

data a0; set tmp1.m_che2;
proc sort nodupkey; by gvkey2 nyear;
proc means; run;

data a1; set tmp1.m_size;
proc sort nodupkey; by gvkey2 nyear;
proc means; run;

data a2; set tmp1.m_nwc;
proc sort nodupkey; by gvkey2 nyear;
proc means; run;

data a3; set tmp1.m_capx;
proc sort nodupkey; by gvkey2 nyear;
proc means; run;

data a4; set tmp1.m_ind_sig;
proc sort nodupkey; by gvkey2 nyear;
proc means; run;

data a5; set tmp1.m_xrd;
proc sort nodupkey; by gvkey2 nyear;
proc means; run;

data a6; set tmp1.m_dividend;
proc sort nodupkey; by gvkey2 nyear;
proc means; run;

data a7; set tmp1.m_salesgrowth;
proc sort nodupkey; by gvkey2 nyear;
proc means; run;

data a8; set tmp1.m_cashop;
proc sort nodupkey; by gvkey2 nyear;
proc means; run;

data a9; set tmp1.m_firmage;
proc sort nodupkey; by gvkey2 nyear;
proc means; run;

data a10; set tmp1.m_tax;
proc sort nodupkey; by gvkey2 nyear;
proc means; run;

data a11; set tmp1.r_managerialability;
proc sort nodupkey; by gvkey2 nyear;
proc means; run;

data a12; set tmp1.m_stockprice;
proc sort nodupkey; by gvkey2 nyear;
proc means; run;

data a13;
merge a0 a1 a2 a3 a4 a5 a6 a7 a8 a9 a10 a11 a12;
by gvkey2 nyear;
proc means; run;

data tmp1.m_cashestimation_merge; set a13;run;
