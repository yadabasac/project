libname tmp1 '\\apporto.com\dfs\SEA\Users\yso1_sea\Desktop\Finance Class\Data';
run;

/*Exclude companies with stock prices less than 2$*/
/*Exclude utilities and financial companies*/
data a0; set tmp1.m_cashestimation_outliers;
if not missing(che);
if at>0;
if sale>0;
if not missing(seq);
if prcc_c >=2;
if sic2 ne 40;
if sic2 ne 41;
if sic2 ne 42;
if sic2 ne 44;
if sic2 ne 45;
if sic2 ne 46;
if sic2 ne 47;
if sic2 ne 48;
if sic2 ne 49;
if sic2 ne 60;
if sic2 ne 61;
if sic2 ne 62;
if sic2 ne 63;
if sic2 ne 64;
if sic2 ne 65;
if sic2 ne 67;
drop sic2 che at sale seq prcc_c;
proc means; run;

proc corr; var che2 size nwc capx2 sigmacash xrd2 dvc2 salesgrowth cashop
firmage tax_b dma; run;

proc reg; model che2=size nwc capx2 sigmacash xrd2 dvc2 salesgrowth cashop firmage 
tax_b dma y1988 y1989 y1990 y1991 y1992 y1993 y1994 y1995 y1996 y1997 y1998 y1999
y2000 y2001 y2002 y2003 y2004 y2005 y2006 y2007 y2008 y2009
y2010 y2011 y2012 y2013 y2014 y2015 y2016 y2017 y2018 y2019
y2020  nsic2 nsic7 nsic8 nsic9 nsic10 nsic12 nsic13
nsic14 nsic15 nsic16 nsic17 nsic20 nsic21 nsic22 nsic23 nsic24
nsic25 nsic26 nsic27 nsic28 nsic29 nsic30 nsic31 nsic32 nsic33
nsic34 nsic35 nsic36 nsic37 nsic38 nsic39 nsic50 nsic51 nsic52
nsic53 nsic54 nsic55 nsic56 nsic57 nsic58 nsic59 nsic70 nsic72 nsic73 nsic75
nsic76 nsic78 nsic79 nsic80 nsic81 nsic82 nsic83 nsic86 nsic87
nsic89 nsic99; run;




