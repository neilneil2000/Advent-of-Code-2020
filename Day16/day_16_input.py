RULES = {
    "departure location": "25-863 or 882-957",
    "departure station": "50-673 or 690-972",
    "departure platform": "25-312 or 321-959",
    "departure track": "48-337 or 358-971",
    "departure date": "31-458 or 476-957",
    "departure time": "32-800 or 821-973",
    "arrival location": "34-502 or 528-951",
    "arrival station": "30-650 or 662-957",
    "arrival platform": "50-148 or 160-966",
    "arrival track": "27-572 or 587-969",
    "class": "46-893 or 913-964",
    "duration": "36-161 or 179-962",
    "price": "38-294 or 311-965",
    "route": "26-391 or 397-962",
    "row": "28-111 or 122-967",
    "seat": "48-65 or 84-973",
    "train": "33-827 or 839-960",
    "type": "47-436 or 454-959",
    "wagon": "45-136 or 147-959",
    "zone": "36-252 or 275-957",
}

YOUR_TICKET = (
    "179,101,223,107,127,211,191,61,199,193,181,131,89,109,197,59,227,53,103,97"
)

NEARBY_TICKETS = """797,604,555,482,170,789,928,930,331,605,402,720,924,743,852,61,213,713,540,51
88,569,789,136,693,294,749,717,503,294,740,696,849,415,703,716,383,693,557,136
174,778,823,850,587,714,282,181,483,148,288,616,741,105,643,594,367,602,857,379
131,554,492,542,553,329,201,825,887,203,591,200,395,778,947,179,539,565,696,845
862,845,550,641,289,16,632,86,637,672,205,647,733,593,490,480,949,551,762,931
764,749,417,705,919,944,158,928,937,564,943,130,427,387,161,885,755,98,282,401
179,311,600,126,884,427,362,821,478,208,641,591,358,53,549,750,146,569,160,735
213,223,623,192,569,562,208,281,631,717,206,528,402,899,764,52,242,477,943,488
456,794,533,243,228,94,671,316,852,107,797,824,945,538,335,129,725,738,321,362
481,637,210,727,885,672,62,936,417,229,189,553,947,234,936,938,886,206,15,497
234,792,64,209,232,587,626,109,225,390,884,126,743,253,312,323,480,482,783,229
390,784,182,943,616,617,628,760,921,718,796,388,824,97,737,455,704,904,883,839
607,275,749,203,721,109,500,559,563,648,606,796,540,291,489,102,543,396,778,642
201,110,535,401,700,763,632,940,102,238,949,55,889,194,488,102,655,499,247,358
942,321,132,368,668,891,550,545,786,219,730,665,646,489,839,906,892,794,774,207
781,400,946,531,189,280,294,408,286,360,650,949,179,828,773,940,389,363,642,421
361,64,486,883,709,518,824,405,629,226,800,916,90,748,841,386,670,789,552,547
549,358,206,935,718,290,237,781,382,599,826,629,645,670,127,738,377,980,425,206
241,891,148,791,147,698,499,345,57,890,916,846,588,478,92,598,536,426,736,727
534,57,92,4,249,594,741,941,183,131,824,235,199,884,785,494,561,714,92,946
60,902,596,491,97,627,107,287,944,226,858,91,892,642,548,790,699,860,110,278
104,925,217,924,57,942,662,664,243,366,826,53,402,275,607,936,736,412,918,395
184,403,793,530,21,556,491,821,491,432,358,851,758,845,555,535,733,925,557,188
890,369,387,96,709,164,379,225,737,795,124,62,884,855,252,744,278,401,211,845
849,283,186,919,231,55,244,291,693,765,57,496,705,342,291,553,291,617,557,283
771,785,941,386,752,891,496,636,454,184,726,840,886,755,539,509,483,638,748,799
435,703,596,849,818,398,364,702,136,712,128,428,127,547,405,237,612,240,694,589
742,290,839,428,16,916,615,741,199,736,720,790,212,240,609,547,708,530,55,241
788,89,862,372,641,916,213,102,709,98,913,714,884,868,486,789,609,694,855,620
710,567,63,842,646,270,136,916,125,928,383,561,425,709,363,188,187,634,331,383
446,915,501,336,719,429,647,147,195,285,615,332,922,277,377,209,212,860,92,206
280,433,572,771,622,243,485,335,244,311,613,280,412,184,796,481,384,774,884,681
101,930,11,130,496,739,882,853,494,385,275,630,645,772,420,769,747,240,550,792
147,557,824,136,322,824,694,781,337,53,758,789,754,633,103,81,541,189,767,185
412,226,539,733,592,766,772,185,940,601,861,643,784,682,596,722,196,636,924,85
643,719,365,747,718,571,359,379,853,376,596,644,363,632,109,764,941,63,765,349
321,781,565,54,62,791,737,744,382,774,921,800,704,73,483,931,50,323,857,939
242,823,777,100,217,717,800,126,923,94,398,733,322,239,85,316,224,58,602,732
502,366,785,283,462,714,147,558,202,389,539,848,491,842,599,456,649,692,225,717
848,534,516,568,563,882,179,638,597,362,529,862,416,696,545,327,532,916,552,860
133,729,378,236,615,770,559,171,614,98,641,929,708,367,235,935,594,776,734,182
610,887,488,846,400,374,429,993,179,87,920,764,230,699,229,278,545,845,532,382
774,283,371,714,654,239,568,147,122,131,54,859,430,407,107,457,562,367,537,286
729,759,882,363,429,323,184,195,240,561,365,931,628,543,369,625,368,655,91,639
104,775,549,244,852,367,216,925,191,608,377,724,641,648,282,214,440,65,430,647
368,61,620,614,631,418,991,535,535,400,107,434,795,364,400,230,542,334,290,423
754,240,291,863,841,381,488,136,60,717,769,284,749,167,235,204,186,500,239,109
697,55,134,201,365,422,463,602,863,186,546,671,541,65,124,556,191,56,502,248
933,76,427,564,854,415,630,746,946,134,418,623,847,645,232,187,425,762,501,766
337,12,746,825,934,321,280,919,762,886,212,493,382,671,743,629,407,739,417,188
59,401,126,491,98,439,488,334,107,209,789,768,283,606,700,417,101,708,799,920
64,226,105,403,214,379,266,88,636,148,748,529,481,777,224,288,430,845,366,544
748,18,97,333,180,284,494,111,823,456,567,538,423,700,280,796,189,213,362,104
347,498,625,406,926,795,212,554,376,667,203,477,378,208,419,379,665,250,857,700
130,716,913,430,336,80,733,728,194,603,569,204,888,913,131,387,64,95,326,276
325,108,713,388,747,432,724,456,690,758,672,131,330,409,202,356,547,553,623,293
204,379,630,312,525,938,399,482,939,938,202,666,55,376,210,554,212,378,224,560
565,94,499,398,499,762,232,216,936,183,940,753,244,670,789,729,979,891,529,931
227,740,751,367,614,892,643,106,201,397,186,789,192,839,729,285,381,111,260,751
601,667,715,180,721,857,557,109,282,570,557,710,189,95,565,540,267,784,638,571
762,947,84,240,154,839,405,941,386,220,774,362,763,851,326,742,244,708,885,662
938,431,700,250,210,637,313,662,822,840,544,566,607,787,217,426,556,429,111,489
100,491,854,330,378,536,206,773,8,542,845,947,333,409,646,398,662,764,496,947
86,412,945,478,182,190,919,419,594,840,384,241,932,661,691,379,185,639,692,198
124,431,823,477,131,224,137,212,546,948,755,779,213,569,488,718,729,946,235,388
5,50,183,858,825,528,457,407,92,793,709,786,101,206,125,536,414,397,127,797
377,543,598,913,435,638,328,655,478,722,735,600,62,376,699,948,928,329,207,856
284,750,671,405,763,770,368,728,60,670,790,941,508,709,887,241,753,86,940,791
394,631,795,602,490,486,148,418,329,194,796,419,629,133,251,237,377,383,458,603
948,132,129,787,699,499,479,3,863,57,822,404,719,99,420,190,57,399,671,288
630,480,148,539,709,103,197,631,398,614,696,242,622,275,754,869,649,232,326,882
563,434,626,287,712,609,610,662,362,325,96,228,388,500,525,863,436,497,185,730
927,423,97,388,259,374,713,180,932,721,52,948,949,90,133,936,724,483,233,556
855,780,662,638,240,290,703,321,658,482,843,406,458,593,547,290,127,753,572,235
58,390,666,744,790,110,715,519,639,85,554,430,939,698,95,367,548,742,229,784
892,219,185,52,634,189,819,224,291,622,855,632,761,740,551,380,936,590,669,719
398,497,58,430,848,281,275,851,667,529,222,925,542,456,290,395,125,478,591,236
548,184,722,719,433,667,597,887,56,51,770,479,992,545,913,857,949,932,559,202
251,571,614,285,947,937,240,130,421,5,636,732,841,535,404,428,927,696,736,788
605,605,557,588,841,420,160,839,458,755,723,825,362,294,378,399,758,778,896,851
734,478,673,360,773,656,237,722,593,918,249,292,147,707,767,182,427,191,614,587
488,406,572,128,324,229,703,528,123,54,731,773,749,517,857,216,693,705,841,602
924,613,366,727,184,406,945,718,737,329,291,717,87,221,907,779,842,54,99,698
919,496,381,414,895,189,669,376,386,359,769,540,386,712,668,107,742,400,885,795
382,235,768,455,369,699,854,748,51,426,457,766,935,495,209,327,290,519,411,379
854,932,398,255,724,495,53,388,419,741,401,233,560,821,371,502,668,485,538,850
110,892,771,774,931,931,590,691,69,431,641,211,633,604,370,94,64,619,543,692
377,565,481,408,607,393,891,729,367,186,293,278,362,195,861,738,244,245,889,913
934,624,598,378,329,128,726,134,202,99,495,496,917,533,363,223,540,436,98,114
783,389,199,664,386,539,758,662,187,360,913,747,427,444,325,202,917,365,635,749
103,489,147,929,103,371,733,397,324,126,713,391,624,717,200,691,985,483,617,239
499,407,408,390,856,549,215,52,534,537,454,548,891,722,201,131,359,562,920,507
147,613,734,572,596,725,562,279,797,937,397,673,843,392,200,862,435,98,534,840
707,783,752,920,276,931,489,487,444,61,758,637,949,571,535,776,695,672,96,612
758,494,179,415,790,748,328,808,794,699,549,786,65,456,760,930,949,335,717,56
781,312,148,491,849,528,662,708,915,608,530,705,160,810,287,202,434,722,205,823
316,103,770,129,231,85,378,65,333,457,604,431,487,436,730,413,131,436,415,758
668,770,842,406,745,244,368,590,824,218,243,286,598,236,860,411,771,922,825,981
847,699,478,638,52,108,63,589,608,237,275,781,772,398,743,147,473,431,53,714
939,719,697,291,394,927,715,110,280,478,644,246,628,824,846,188,845,198,369,361
589,758,856,942,364,102,887,398,95,220,413,388,327,195,288,482,848,979,500,375
750,923,532,509,728,632,416,541,86,94,723,767,843,758,328,399,790,86,856,229
334,175,251,599,99,773,129,276,859,649,537,778,885,914,920,939,248,862,399,388
499,411,92,401,368,597,386,212,609,458,52,929,755,88,890,719,168,251,329,532
667,788,731,445,542,669,412,779,859,668,690,359,766,291,210,784,379,54,193,862
597,214,311,56,939,735,699,94,393,398,720,720,457,245,782,572,289,235,666,379
132,630,482,212,408,544,822,106,195,725,425,221,225,933,756,704,878,604,288,855
873,370,190,397,752,125,726,782,924,637,787,95,777,929,751,550,534,646,398,856
385,927,713,673,289,222,645,423,235,591,398,543,723,632,757,703,720,778,95,157
926,779,724,793,639,434,592,232,93,215,211,665,402,102,562,480,364,713,452,570
591,444,725,205,669,281,625,597,190,547,379,291,565,743,794,614,287,790,407,639
328,725,368,594,290,311,763,875,933,721,390,633,56,110,755,594,939,744,398,390
63,193,326,775,249,562,600,377,853,24,650,543,645,275,488,235,588,776,335,764
599,723,936,542,232,787,696,232,93,632,330,759,249,709,195,739,276,862,518,778
592,777,566,920,343,608,827,206,735,201,533,275,199,54,824,281,915,913,332,712
292,742,202,319,697,363,106,740,360,639,424,597,161,587,608,479,615,724,850,665
649,392,731,231,433,496,535,528,558,380,285,60,61,533,824,489,372,940,422,84
758,405,892,328,571,935,406,771,398,673,721,129,551,425,203,749,806,364,416,720
701,397,278,96,629,846,209,949,487,529,884,776,617,423,288,802,89,102,936,327
630,88,730,736,629,797,748,0,768,552,454,247,927,754,843,492,562,282,415,740
374,844,939,147,4,744,595,567,89,728,399,863,276,50,623,709,669,632,861,359
668,375,495,897,737,822,769,84,764,431,389,567,237,430,533,455,454,913,728,602
737,529,275,287,424,716,378,885,199,633,987,667,134,230,596,645,107,590,542,401
161,129,534,937,833,647,429,764,937,643,242,790,767,750,228,208,709,849,636,571
275,693,888,870,247,753,490,709,727,587,671,101,379,245,852,134,293,797,220,160
661,571,742,592,630,432,221,230,208,922,221,477,766,918,322,923,922,421,191,236
102,109,630,647,920,531,731,384,821,239,487,231,703,921,931,996,603,57,60,98
559,840,763,289,749,901,222,131,481,88,724,696,336,726,594,198,432,382,857,695
888,700,943,161,249,601,985,530,643,495,792,496,485,621,107,719,606,85,160,947
89,377,911,423,702,234,454,373,827,88,91,191,750,775,759,635,236,551,550,782
363,628,398,861,777,914,428,241,821,640,588,225,428,318,597,327,183,134,672,629
593,386,180,702,129,777,761,696,58,928,636,325,854,891,286,724,767,892,409,144
978,236,61,916,623,534,752,217,190,603,489,364,529,369,760,530,703,122,606,489
413,477,609,654,457,490,105,88,380,569,337,293,89,626,725,248,332,400,412,772
312,323,134,105,454,941,181,554,643,928,282,706,183,403,400,275,689,361,930,555
229,93,544,486,534,321,931,444,759,646,621,223,823,131,568,665,286,335,611,455
842,599,929,764,787,641,200,886,593,601,483,94,418,336,761,205,95,668,333,171
858,386,200,781,331,595,235,312,424,858,615,226,731,786,530,174,186,944,615,723
714,623,205,415,622,373,385,247,721,492,861,890,926,232,720,60,313,886,705,593
88,203,184,74,591,756,778,737,827,587,402,424,796,96,918,755,696,201,389,853
123,792,104,594,789,544,545,771,797,406,90,697,442,913,613,890,724,54,246,251
774,794,930,126,706,742,275,612,614,766,418,848,653,777,109,414,103,753,490,436
742,647,229,528,483,933,659,528,386,590,488,211,501,719,401,429,719,601,634,498
726,86,487,623,456,596,550,572,539,481,243,556,245,530,384,784,599,715,180,262
224,618,482,162,776,554,638,417,708,337,561,195,765,764,631,123,696,691,725,478
282,407,538,856,941,397,235,598,248,160,620,334,488,52,740,858,572,381,67,369
245,110,923,763,454,544,770,87,366,429,191,531,738,634,229,429,551,278,322,874
250,533,127,248,679,664,90,208,774,290,751,335,737,246,546,821,215,383,433,131
361,528,938,404,250,885,241,368,604,329,520,857,741,789,823,763,604,91,793,611
288,278,938,772,412,424,695,765,609,886,712,246,795,120,786,211,128,196,759,886
370,200,720,932,366,713,541,109,240,240,183,633,537,18,708,789,249,663,246,774
136,852,745,600,69,610,365,233,888,481,647,383,488,714,853,289,387,90,693,564
941,13,768,915,324,358,335,223,547,62,368,639,561,328,488,615,738,436,745,602
330,650,245,287,548,711,757,555,231,590,282,903,700,787,787,373,732,698,726,87
773,281,588,127,85,938,369,571,282,331,134,976,535,275,494,93,852,413,366,716
562,192,935,101,196,365,396,457,718,637,760,741,281,773,886,701,500,493,412,670
532,88,633,223,85,740,488,858,232,796,217,623,930,459,501,97,924,924,672,372
709,608,608,191,619,160,758,425,755,948,290,931,73,649,924,537,428,883,200,826
738,89,242,845,286,483,713,550,854,791,129,403,568,388,128,410,14,935,638,571
910,673,476,534,790,935,723,726,567,250,433,104,692,381,413,942,799,547,617,727
401,935,490,241,769,868,692,600,330,293,333,919,884,594,948,732,501,241,136,196
928,627,726,924,412,377,332,187,61,711,361,209,631,774,292,921,509,568,720,572
231,386,222,690,700,781,645,732,701,229,923,943,927,860,722,986,533,186,822,690
233,199,756,396,242,800,481,941,252,206,702,947,790,287,292,539,436,280,423,532
592,436,528,190,196,411,911,564,863,361,537,489,844,134,610,641,781,762,536,532
843,769,496,859,182,372,165,93,774,855,489,568,384,705,373,502,493,947,400,611
626,641,395,844,234,400,561,593,648,330,633,646,184,605,411,94,218,106,589,920
791,771,204,217,640,430,337,478,111,0,669,612,282,537,598,948,932,530,211,212
796,494,215,992,331,224,724,710,208,788,405,707,480,649,59,691,335,772,105,792
615,193,335,193,223,148,535,360,798,532,786,671,335,292,488,675,559,948,863,719
662,53,789,52,102,638,886,761,728,545,887,742,331,858,596,851,498,729,759,79
458,125,607,885,871,778,335,363,326,495,776,240,889,545,430,197,181,148,376,332
433,655,794,843,863,211,708,182,784,863,493,617,572,918,620,731,593,237,368,885
289,648,65,226,701,778,932,226,364,92,975,389,704,232,758,492,937,863,892,631
612,565,109,723,482,594,340,281,333,381,545,722,374,57,499,421,698,782,919,941
201,201,230,708,480,540,389,221,937,626,945,590,502,839,191,231,197,797,988,543
944,65,50,129,931,773,275,285,906,615,329,232,378,56,621,614,484,613,107,389
186,332,130,88,633,725,101,233,485,640,713,979,481,326,740,599,89,194,127,477
800,93,754,863,554,562,406,224,931,649,189,536,191,279,98,259,477,714,424,846
103,181,432,648,439,331,430,196,591,692,209,764,92,227,200,700,693,539,567,889
730,381,553,841,184,548,209,227,457,571,127,125,550,926,366,528,717,745,316,633
645,431,213,562,614,403,552,479,329,55,180,702,176,542,594,391,542,716,208,323
801,287,94,936,421,490,665,857,857,192,205,913,373,672,863,939,62,646,886,737
223,331,283,787,839,402,381,774,843,721,388,281,101,223,128,312,634,236,165,235
730,750,533,751,531,669,289,237,851,65,762,851,247,649,737,549,587,794,392,827
126,238,210,841,986,218,793,730,425,800,192,276,614,378,619,422,690,376,87,62
230,591,408,554,608,411,915,666,567,987,477,218,673,411,693,290,647,857,211,124
436,477,748,205,414,607,509,92,589,859,943,361,423,382,291,777,478,762,560,789
432,490,431,637,85,945,878,219,368,762,596,208,554,534,643,857,735,605,721,694
274,405,698,716,213,701,718,488,426,414,380,743,226,289,221,826,748,457,501,948
946,359,913,185,311,697,278,456,588,280,908,863,662,855,572,628,97,643,779,326
84,617,403,539,886,214,23,241,798,419,197,888,946,384,773,739,491,90,542,226
723,275,722,403,228,593,220,495,246,599,556,196,902,212,729,627,477,847,733,696
609,199,91,334,316,200,491,825,718,421,927,605,218,638,230,710,707,218,643,132
282,558,791,793,215,609,787,382,293,758,566,283,564,730,421,328,195,893,326,585
595,275,766,422,733,284,221,485,539,409,569,694,278,914,629,469,929,132,850,705
823,548,380,782,458,843,438,929,85,775,741,199,249,539,550,663,946,761,107,126
63,273,777,778,918,605,215,276,380,857,857,132,327,853,608,568,764,637,634,292
600,100,122,787,363,160,941,205,885,228,943,85,122,537,542,363,544,66,597,616
218,377,626,418,785,935,557,367,548,933,856,631,605,128,750,822,847,326,337,468
640,524,100,592,415,436,331,111,205,662,703,51,884,496,612,642,486,823,662,889
423,854,401,21,619,321,110,757,533,616,622,929,202,492,768,424,885,195,55,843
411,3,839,539,850,893,244,202,646,620,784,50,248,283,498,940,426,771,931,560
436,483,784,23,204,189,730,758,641,634,624,294,710,235,219,821,627,710,204,329
529,941,129,209,200,782,603,797,407,215,670,200,415,670,124,774,894,312,278,636
225,241,827,486,733,949,882,198,249,669,671,487,977,59,938,333,293,388,249,668
678,948,748,623,882,483,57,918,823,203,480,626,104,566,370,765,207,103,781,481
732,827,884,725,778,55,363,528,85,196,544,791,364,696,932,591,493,530,785,911
510,745,785,795,733,848,638,741,237,410,231,192,927,532,742,614,717,949,369,921
77,743,723,99,528,605,620,771,85,826,649,696,434,640,477,211,844,135,888,890
399,278,642,698,140,698,53,763,501,362,752,384,821,888,594,324,433,598,731,723
608,821,740,104,363,416,78,148,889,416,615,552,776,858,862,824,128,540,712,718
391,697,647,433,560,228,383,600,636,856,369,602,250,490,539,485,396,665,787,416
213,946,604,716,944,668,456,456,891,333,329,665,186,144,621,403,715,292,495,598
665,187,552,596,194,949,365,530,847,641,193,364,398,482,694,616,783,105,980,541
713,863,62,693,379,851,499,650,770,226,701,668,946,732,606,553,769,389,249,831
663,738,776,756,672,416,863,290,620,111,690,147,122,891,200,226,491,397,359,320
148,216,928,799,774,199,535,975,103,610,914,621,430,286,746,127,844,479,741,703
200,477,668,861,723,848,363,922,592,622,369,691,535,743,284,659,945,603,282,747
762,645,413,782,636,791,212,722,369,990,92,102,708,633,54,666,589,181,181,111
782,105,699,212,592,96,136,725,365,856,779,136,705,416,134,499,998,501,240,636
458,363,375,944,192,885,883,224,282,611,635,456,292,630,592,193,546,408,597,657
384,726,700,591,366,371,195,549,105,946,610,18,412,633,621,934,429,434,629,825
91,735,57,854,432,623,161,277,136,551,364,599,545,700,422,444,826,436,130,561
619,777,780,368,249,86,391,590,545,363,985,373,709,87,933,332,627,388,603,404
89,324,725,778,491,799,242,766,763,229,490,891,455,568,788,329,427,553,796,447
774,225,413,208,859,629,97,396,496,204,728,861,108,334,552,398,384,711,533,606
795,122,89,233,370,587,371,722,937,737,230,324,325,482,857,551,72,193,718,182
498,7,537,405,423,921,715,934,487,761,424,609,704,454,609,742,374,287,54,641
496,666,704,732,358,593,374,311,664,400,104,629,697,632,186,246,338,761,628,592
618,199,363,925,189,183,530,910,179,277,535,562,434,889,712,861,761,124,219,202
570,59,937,809,326,724,693,397,727,294,65,942,610,132,595,850,860,891,774,721
108,282,325,624,636,798,921,261,433,286,919,127,621,52,293,417,63,707,133,949
135,570,68,457,715,596,237,87,95,587,434,555,597,400,551,919,434,610,602,704
841,128,489,936,434,891,939,563,418,10,605,708,325,613,385,757,430,289,767,401
668,251,938,4,726,698,281,105,537,367,84,719,720,914,737,750,213,745,220,798
760,947,610,102,839,107,685,407,641,233,759,849,105,645,703,641,754,223,757,325
616,436,540,386,97,726,672,83,736,237,478,601,605,595,593,58,566,229,730,572
409,941,455,136,792,104,238,600,822,747,671,707,185,155,913,61,423,637,604,827
613,779,219,698,759,134,161,224,84,204,66,564,697,375,386,336,405,795,591,321
926,435,539,124,499,328,224,242,549,914,613,381,86,500,860,102,891,410,664,808
202,821,748,399,65,313,277,108,384,634,534,709,59,863,416,607,227,501,211,853
540,610,430,949,104,928,160,501,247,290,949,839,426,768,227,705,714,228,655,50"""
