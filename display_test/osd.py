# -*- coding: utf-8 -*-
'''

'''
import acoular
import pylab as plt
import numpy as np
from numpy import pi, cos, sin, zeros, sqrt, round, int
import pdb


a[  0] = 0x00
a[  1] = 0x00
a[  2] = 0x00
a[  3] = 0x00
a[  4] = 0x00
a[  5] = 0x00
a[  6] = 0x00
a[  7] = 0x00
a[  8] = 0x00
a[  9] = 0x00
a[ 10] = 0x00
a[ 11] = 0x00
a[ 12] = 0x00
a[ 13] = 0x00
a[ 14] = 0x00
a[ 15] = 0x00
a[ 16] = 0x00
a[ 17] = 0x00
a[ 18] = 0x00
a[ 19] = 0x00
a[ 20] = 0x00
a[ 21] = 0x00
a[ 22] = 0x00
a[ 23] = 0x00
a[ 24] = 0x00
a[ 25] = 0x00
a[ 26] = 0x00
a[ 27] = 0x00
a[ 28] = 0x00
a[ 29] = 0x00
a[ 30] = 0x00
a[ 31] = 0x00
a[ 32] = 0x00
a[ 33] = 0x00
a[ 34] = 0x00
a[ 35] = 0x00
a[ 36] = 0x00
a[ 37] = 0x00
a[ 38] = 0x00
a[ 39] = 0x00
a[ 40] = 0x00
a[ 41] = 0x00
a[ 42] = 0x00
a[ 43] = 0x00
a[ 44] = 0x00
a[ 45] = 0x00
a[ 46] = 0x00
a[ 47] = 0x04
a[ 48] = 0x00
a[ 49] = 0x00
a[ 50] = 0x00
a[ 51] = 0x00
a[ 52] = 0x00
a[ 53] = 0x00
a[ 54] = 0x00
a[ 55] = 0x00
a[ 56] = 0x00
a[ 57] = 0x00
a[ 58] = 0x00
a[ 59] = 0x00
a[ 60] = 0x00
a[ 61] = 0x00
a[ 62] = 0x00
a[ 63] = 0x00
a[ 64] = 0x00
a[ 65] = 0x1C
a[ 66] = 0x38
a[ 67] = 0x00
a[ 68] = 0x00
a[ 69] = 0x00
a[ 70] = 0x00
a[ 71] = 0x03
a[ 72] = 0x00
a[ 73] = 0x00
a[ 74] = 0x00
a[ 75] = 0x00
a[ 76] = 0x00
a[ 77] = 0x00
a[ 78] = 0x00
a[ 79] = 0x00
a[ 80] = 0x00
a[ 81] = 0x00
a[ 82] = 0x00
a[ 83] = 0x0C
a[ 84] = 0x38
a[ 85] = 0x00
a[ 86] = 0x00
a[ 87] = 0xE6
a[ 88] = 0xFF
a[ 89] = 0x07
a[ 90] = 0x80
a[ 91] = 0x01
a[ 92] = 0x00
a[ 93] = 0x00
a[ 94] = 0x00
a[ 95] = 0x00
a[ 96] = 0x00
a[ 97] = 0x00
a[ 98] = 0x00
a[ 99] = 0x00
a[100] = 0x00
a[101] = 0x0C
a[102] = 0x18
a[103] = 0x08
a[104] = 0xFC
a[105] = 0x0F
a[106] = 0x01
a[107] = 0x03
a[108] = 0xC0
a[109] = 0x01
a[110] = 0x7E
a[111] = 0x00
a[112] = 0xF8
a[113] = 0x1F
a[114] = 0x0F
a[115] = 0xFC
a[116] = 0x3E
a[117] = 0x7E
a[118] = 0x00
a[119] = 0x0C
a[120] = 0x18
a[121] = 0x1C
a[122] = 0x00
a[123] = 0x06
a[124] = 0x82
a[125] = 0x01
a[126] = 0xC0
a[127] = 0x01
a[128] = 0x18
a[129] = 0x00
a[130] = 0x80
a[131] = 0x01
a[132] = 0x1C
a[133] = 0x10
a[134] = 0x1C
a[135] = 0x18
a[136] = 0xFC
a[137] = 0xFF
a[138] = 0xFF
a[139] = 0x3F
a[140] = 0x30
a[141] = 0x06
a[142] = 0xC6
a[143] = 0x00
a[144] = 0xC0
a[145] = 0x01
a[146] = 0x18
a[147] = 0x00
a[148] = 0x80
a[149] = 0x01
a[150] = 0x1C
a[151] = 0x10
a[152] = 0x18
a[153] = 0x08
a[154] = 0x00
a[155] = 0x0C
a[156] = 0x18
a[157] = 0x00
a[158] = 0x30
a[159] = 0x06
a[160] = 0xEC
a[161] = 0x00
a[162] = 0xC0
a[163] = 0x03
a[164] = 0x18
a[165] = 0x00
a[166] = 0x80
a[167] = 0x01
a[168] = 0x3C
a[169] = 0x10
a[170] = 0x18
a[171] = 0x0C
a[172] = 0x00
a[173] = 0x0C
a[174] = 0x18
a[175] = 0x00
a[176] = 0x10
a[177] = 0x06
a[178] = 0x78
a[179] = 0x00
a[180] = 0x60
a[181] = 0x03
a[182] = 0x18
a[183] = 0x00
a[184] = 0x80
a[185] = 0x01
a[186] = 0x34
a[187] = 0x10
a[188] = 0x30
a[189] = 0x04
a[190] = 0x00
a[191] = 0x0C
a[192] = 0x18
a[193] = 0x00
a[194] = 0x18
a[195] = 0x02
a[196] = 0x38
a[197] = 0x00
a[198] = 0x20
a[199] = 0x03
a[200] = 0x18
a[201] = 0x00
a[202] = 0x80
a[203] = 0x01
a[204] = 0x74
a[205] = 0x10
a[206] = 0x30
a[207] = 0x06
a[208] = 0x00
a[209] = 0x04
a[210] = 0x08
a[211] = 0x00
a[212] = 0x18
a[213] = 0x03
a[214] = 0xFC
a[215] = 0x00
a[216] = 0x20
a[217] = 0x03
a[218] = 0x18
a[219] = 0x00
a[220] = 0x80
a[221] = 0x01
a[222] = 0x64
a[223] = 0x10
a[224] = 0x60
a[225] = 0x02
a[226] = 0x00
a[227] = 0x60
a[228] = 0x00
a[229] = 0x00
a[230] = 0x18
a[231] = 0x03
a[232] = 0xC6
a[233] = 0x03
a[234] = 0x20
a[235] = 0x03
a[236] = 0x18
a[237] = 0x00
a[238] = 0x80
a[239] = 0x01
a[240] = 0xE4
a[241] = 0x10
a[242] = 0x60
a[243] = 0x03
a[244] = 0x00
a[245] = 0xC0
a[246] = 0x00
a[247] = 0x00
a[248] = 0x18
a[249] = 0x83
a[250] = 0x01
a[251] = 0x3F
a[252] = 0x30
a[253] = 0x06
a[254] = 0x18
a[255] = 0x00
a[256] = 0x80
a[257] = 0x01
a[258] = 0xC4
a[259] = 0x10
a[260] = 0xC0
a[261] = 0x01
a[262] = 0x00
a[263] = 0x82
a[264] = 0x03
a[265] = 0x00
a[266] = 0x18
a[267] = 0x63
a[268] = 0x38
a[269] = 0x0C
a[270] = 0x10
a[271] = 0x06
a[272] = 0x18
a[273] = 0x00
a[274] = 0x80
a[275] = 0x01
a[276] = 0xC4
a[277] = 0x11
a[278] = 0xC0
a[279] = 0x01
a[280] = 0x00
a[281] = 0x8E
a[282] = 0x03
a[283] = 0x00
a[284] = 0x18
a[285] = 0x13
a[286] = 0x18
a[287] = 0x00
a[288] = 0x10
a[289] = 0x06
a[290] = 0x18
a[291] = 0x00
a[292] = 0x80
a[293] = 0x01
a[294] = 0x84
a[295] = 0x11
a[296] = 0x80
a[297] = 0x01
a[298] = 0x20
a[299] = 0x06
a[300] = 0x07
a[301] = 0x00
a[302] = 0x1C
a[303] = 0x0B
a[304] = 0x18
a[305] = 0x00
a[306] = 0x18
a[307] = 0x06
a[308] = 0x18
a[309] = 0x00
a[310] = 0x80
a[311] = 0x01
a[312] = 0x84
a[313] = 0x13
a[314] = 0xC0
a[315] = 0x01
a[316] = 0x20
a[317] = 0x06
a[318] = 0x03
a[319] = 0x03
a[320] = 0xFC
a[321] = 0x1F
a[322] = 0x18
a[323] = 0x07
a[324] = 0xF8
a[325] = 0x0F
a[326] = 0x18
a[327] = 0x00
a[328] = 0x80
a[329] = 0x01
a[330] = 0x04
a[331] = 0x17
a[332] = 0xC0
a[333] = 0x03
a[334] = 0x20
a[335] = 0x06
a[336] = 0x00
a[337] = 0x06
a[338] = 0x00
a[339] = 0xCC
a[340] = 0xFF
a[341] = 0x0F
a[342] = 0x08
a[343] = 0x0C
a[344] = 0x18
a[345] = 0x00
a[346] = 0x80
a[347] = 0x01
a[348] = 0x04
a[349] = 0x17
a[350] = 0x60
a[351] = 0x03
a[352] = 0x30
a[353] = 0x06
a[354] = 0x00
a[355] = 0x0C
a[356] = 0x00
a[357] = 0x0C
a[358] = 0x18
a[359] = 0x00
a[360] = 0x08
a[361] = 0x0C
a[362] = 0x18
a[363] = 0x00
a[364] = 0x80
a[365] = 0x01
a[366] = 0x04
a[367] = 0x1E
a[368] = 0x20
a[369] = 0x06
a[370] = 0x30
a[371] = 0x06
a[372] = 0x00
a[373] = 0x1C
a[374] = 0x00
a[375] = 0x0E
a[376] = 0x18
a[377] = 0x00
a[378] = 0x0C
a[379] = 0x0C
a[380] = 0x18
a[381] = 0x00
a[382] = 0x80
a[383] = 0x01
a[384] = 0x04
a[385] = 0x1C
a[386] = 0x30
a[387] = 0x06
a[388] = 0x38
a[389] = 0x06
a[390] = 0x00
a[391] = 0x18
a[392] = 0xC0
a[393] = 0x0D
a[394] = 0x18
a[395] = 0x08
a[396] = 0x0C
a[397] = 0x1C
a[398] = 0x18
a[399] = 0x40
a[400] = 0x80
a[401] = 0x01
a[402] = 0x04
a[403] = 0x1C
a[404] = 0x10
a[405] = 0x0C
a[406] = 0x38
a[407] = 0x06
a[408] = 0x00
a[409] = 0x18
a[410] = 0x3C
a[411] = 0x0C
a[412] = 0x18
a[413] = 0x1C
a[414] = 0x04
a[415] = 0x18
a[416] = 0x18
a[417] = 0x20
a[418] = 0x80
a[419] = 0x01
a[420] = 0x04
a[421] = 0x18
a[422] = 0x18
a[423] = 0x0C
a[424] = 0x1C
a[425] = 0x06
a[426] = 0x00
a[427] = 0x18
a[428] = 0x0E
a[429] = 0xFC
a[430] = 0xFF
a[431] = 0x3F
a[432] = 0x04
a[433] = 0x18
a[434] = 0x18
a[435] = 0x20
a[436] = 0x80
a[437] = 0x01
a[438] = 0x04
a[439] = 0x18
a[440] = 0x08
a[441] = 0x1C
a[442] = 0x00
a[443] = 0x06
a[444] = 0x80
a[445] = 0x00
a[446] = 0x04
a[447] = 0x04
a[448] = 0x18
a[449] = 0x00
a[450] = 0x06
a[451] = 0x18
a[452] = 0x18
a[453] = 0x38
a[454] = 0x80
a[455] = 0x01
a[456] = 0x04
a[457] = 0x10
a[458] = 0x0C
a[459] = 0x18
a[460] = 0x00
a[461] = 0x06
a[462] = 0xC0
a[463] = 0x00
a[464] = 0x00
a[465] = 0x06
a[466] = 0x18
a[467] = 0x00
a[468] = 0x1F
a[469] = 0x7C
a[470] = 0xFE
a[471] = 0x3F
a[472] = 0xF8
a[473] = 0x1F
a[474] = 0x1F
a[475] = 0x10
a[476] = 0x1F
a[477] = 0x7E
a[478] = 0x00
a[479] = 0x0E
a[480] = 0xC0
a[481] = 0x01
a[482] = 0x00
a[483] = 0x06
a[484] = 0x18
a[485] = 0x00
a[486] = 0x00
a[487] = 0x00
a[488] = 0x00
a[489] = 0x00
a[490] = 0x00
a[491] = 0x00
a[492] = 0x00
a[493] = 0x00
a[494] = 0x00
a[495] = 0x00
a[496] = 0x00
a[497] = 0xFC
a[498] = 0xFF
a[499] = 0x00
a[500] = 0x70
a[501] = 0x07
a[502] = 0x18
a[503] = 0x00
a[504] = 0x00
a[505] = 0x00
a[506] = 0x00
a[507] = 0x00
a[508] = 0x00
a[509] = 0x00
a[510] = 0x00
a[511] = 0x00
a[512] = 0x00
a[513] = 0x00
a[514] = 0x00
a[515] = 0x00
a[516] = 0x00
a[517] = 0x00
a[518] = 0xC0
a[519] = 0x03
a[520] = 0x18
a[521] = 0x00
a[522] = 0x00
a[523] = 0x00
a[524] = 0x00
a[525] = 0x00
a[526] = 0x00
a[527] = 0x00
a[528] = 0x00
a[529] = 0x00
a[530] = 0x00
a[531] = 0x00
a[532] = 0x00
a[533] = 0x00
a[534] = 0x00
a[535] = 0x00
a[536] = 0x80
a[537] = 0x01
a[538] = 0x18
a[539] = 0x00
a[540] = 0x00
a[541] = 0x00
a[542] = 0x00
a[543] = 0x00
a[544] = 0x00
a[545] = 0x00
a[546] = 0x00
a[547] = 0x00
a[548] = 0x00
a[549] = 0x00
a[550] = 0x00
a[551] = 0x00
a[552] = 0x00
a[553] = 0x00
a[554] = 0x00
a[555] = 0x00
a[556] = 0x18
a[557] = 0x00
a[558] = 0x00
a[559] = 0x00
a[560] = 0x00
a[561] = 0x00
a[562] = 0x00
a[563] = 0x00
a[564] = 0x00
a[565] = 0x00
a[566] = 0x00
a[567] = 0x00
a[568] = 0x00
a[569] = 0x00
a[570] = 0x00
a[571] = 0x00
a[572] = 0x00
a[573] = 0x00
a[574] = 0x00
a[575] = 0x00

for x in range(0, 576, 1):
    b0 = a[x] & 0x01
    b1 = a[x] & 0x02
    b2 = a[x] & 0x04
    b3 = a[x] & 0x08
    b4 = a[x] & 0x10
    b5 = a[x] & 0x20
    b6 = a[x] & 0x40
    b7 = a[x] & 0x80

