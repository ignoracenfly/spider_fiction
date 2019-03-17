#!/usr/bin/python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import requests
import random
import time
from config_old import header

def register(phone):
	url = 'http://api.valuedbit.tech/api/center/register'
	r = random.randint(0,100)
	data = {}
	if(r>=95):
		data={'orion-source':'', 'source':'', 'app_id':'10001'}
	elif(r>=90):
		data={'orion-source':'h5', 'source':'3', 'app_id':'10001'}
	elif(r>40):
		data={'orion-source':'ios', 'source':'1', 'app_id':'10000'}
	else:
		data={'orion-source':'android', 'source':'2', 'app_id':'10000'}
	data['account'] = phone
	data['password'] = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz!@1234567890', 8))
	data['code'] = '079999'

	r = requests.post(url, data = data, headers = header[random.randint(0,4)])
	print(r.text)

if __name__=="__main__":
	phone1 = [13430403880, 15202027772, 13511972216, 18826132053, 13249898762, 18928969460, 18941013958, 13751008506, 13768838509, 13696824420, 13699888941, 18648840416, 13631401758, 13560237781, 13715144460, 13751093475, 13043429180, 18665301168, 13268739069, 13729115877, 17603085757, 18771638860, 15212656655, 15118066069, 15507559401, 13711508885, 13055088244, 18316626256, 13597500844, 13410059538, 13647578061, 13528826750, 15220283784, 13622285627, 13798526367, 13640918433, 13530247454, 15013625913, 15889678112, 13682521706, 18682168764, 13316459993, 18192001667, 13022223513, 15546162277, 15602382158, 13927426334, 13480739308, 18341944101, 18126520062, 13535477778, 13510001475, 15986693342, 13798591222, 13524422651, 13510664563, 13541996834, 18664919610, 15820709542, 13088858169, 13751046362, 18823346393, 18617047282, 13186255444, 18283162762, 13359219380, 15918676834, 13632589784, 15249169080, 13713805182, 13185945670, 15875522185, 13421375386, 13365720368, 13925241661, 13088880086, 13760157210, 13088068579, 17688609559, 15034793684, 15889293009, 13590135337, 15889777703, 18123937948, 18520711252, 18665302940, 18823876817, 13533456042, 15929441237, 17722618860, 15814637617, 13981458291, 18584116365, 13914221054, 13127212291, 15091282849, 15986792226, 15678860906, 15309346626, 18566688227]
	phone2 = [18011890681, 13821714758, 15078818840, 18219410105, 13699852920, 18872965738, 18681557023, 13714381071, 13632466285, 13189743319, 18617161373, 13643147254, 18616632063, 18820104213, 15013808041, 17688766729, 18899812949, 13417408456, 15814575392, 13913550458, 13705065277, 13538259875, 15112608784, 18513218724, 13688810717, 15915513533, 15989448591, 15013413567, 13570467915, 18316350236, 13686471105, 18148749876, 13631570680, 18820999309, 13430655189, 15816880856, 13956688910, 13404046942, 13410998674, 13913750191, 13682578455, 13448354391, 18620389548, 18320337704, 13528772889, 17666591996, 15919772087, 15914058169, 18818770510, 18312686185, 13265321701, 13822290319, 13127812497, 15013478360, 13928444713, 13265579996, 18127077760, 13809773002, 18038052145, 13928421519, 15118104927, 17755610141, 15118162718, 13643777617, 13711028133, 18995034353, 18320946690, 15618377478, 13411865545, 13613012311, 13418967316, 13798266971, 13641419689, 13242082586, 13461122619, 13660315235, 15115130309, 18565605512, 13669885703, 13513193202, 15625532774, 13723761530, 13410112110, 18377001850, 13246761596, 18370801195, 15012968591, 13240145969, 15307111196, 17774757728, 15919716779, 15013418818, 13530221586, 13750561011, 13927525300, 15889938020, 15817106392, 15224923345, 13421807301, 13728741271, 18680360349, 13825707163, 13924016687, 13590160330, 13266845668, 13655206363, 13299001353, 13487023069, 13446135037, 13149931280, 13247548968, 15521216396, 13670293720, 13580006363, 15018471471, 17321285551, 15014109910, 18177653425, 13530121312, 15899771277, 15817443579, 13058170616, 18302091632, 13602634629, 13510065726, 15378824937, 18392115098, 18924586623, 13560731981, 13824384083, 18676740272, 15817470153, 17666136955, 17322041962, 13715335742, 13977191151, 15087531547, 13144829770, 18820789509, 15818593048, 13631400304, 15889782660, 13670009157, 17603080640, 13922258753, 15827230331, 13058071908, 15989434930, 18028797939, 18033066156, 15112431008, 13649815022, 18503001550, 13137557931, 15013575204, 18718546667, 18675560626, 13828448798, 13113952618, 17688973851, 13410690500, 18664313267, 13428928082, 13798524855, 13380042110, 13686892583, 13319945924, 15133607761, 13050992538, 17817773217, 15188411112, 15521411220, 13923476345, 15019492504, 13802564450, 13530950819, 18620301478, 15820208083, 13544041219, 15055925284, 18011766047, 13501531660, 18309210607, 13003766768, 13528893100, 13713712652, 15177325950, 13103121998, 18820606026, 15999532775, 13119559126, 13332822652, 13622317669, 13635461181, 15811843182, 15818649805, 13535144246, 13723591166, 15302670406, 13534356442, 18819283274, 18188625059, 13510194381, 15818502414, 13410513936, 13528858910, 13798270113, 13430457517, 13833384373, 13612948492, 13168771825, 13760248327, 13725058854, 13265693217, 13428961513, 15317790057, 17722518026, 18575171823, 13823558492, 13889345727, 18098912597, 18665367538, 15889667236, 17688773354, 18520898839, 18102599250, 17009019407, 13416989967, 15919851744, 17688161669, 13647113147, 13802703855, 13691745253, 13554769024, 15899852832, 13686835292, 15872349690, 13530524470, 18577810818, 15110036730, 15876544874, 18813577456, 15815829906, 13778815377, 18565672991, 18062593330, 13148884891, 15024010541, 18617068313, 15004660112, 15323800676, 13215687645, 18820794016, 15919853069, 13430360653, 15820786475, 15521287653, 13639586527, 18682366785, 15913135041, 13503048735, 13602530637, 13691753692, 15766086018, 18779257084, 15712028831, 15817266707, 13510565923, 13450357154, 13619096752, 13751819610, 13349879138, 18950581963, 13827625018, 15814608984, 17828027882, 13430210627, 15112261339, 13590444461, 13826178070, 17749795478, 13537605953, 18620375091, 18826086852, 18289767660, 17688981994, 18688619857, 13049330574, 13422933361, 17602301444, 13691079999, 13766709644, 17681677331, 13510161023, 13510802662, 15019434508, 13128972253, 13612850203, 13532882508, 18281567673, 13227287266, 18318158288, 18500208069, 18684982657, 13798757572, 18267588886, 18312530725, 18519897986, 18923723757, 17666106217, 13760190750, 13922248853, 14718284623, 13530658001, 18934878507, 13728925404, 13692890621, 13510972559, 18822830872, 13510185916, 15189350443, 18520698844, 15915495282, 15692002494, 13411000656, 13242955267, 15817302637, 13172458085, 18676762329, 18926033146, 13754990859, 13686495871, 13049333915, 13500057252, 15989450781, 13826966190, 13602580929, 13622893364, 13684967305, 13691761596, 17688718124, 15155665705, 17688736168, 13039663102, 18617186691, 13530983581, 13976950945, 13351439083, 15603340731, 13596329153, 15919955921, 13430674043, 13539007528, 13690265061, 13215166323, 18898720575, 15817311904, 18665061093, 15521506860, 13902432770, 17691191308, 13688869610, 18688786646, 15692007693, 18569432757, 13632578656, 13875500606, 13977137498, 13926515040, 13116075693, 13119597545, 18819189815, 13392188999, 13534146453, 15013652986, 18682142861, 18570148283, 13544274161, 13662692873, 13028442123, 18123848554, 18397833581, 17603054262, 13828805327, 17665278058, 18703426090, 13237614401, 15149759530, 18820292810, 17687736027, 15167835795, 15022836130, 17688735254, 13077213977, 13269209693, 18123741479, 15817395095, 13410734840, 17607612576, 15057948909, 18818779707, 18176756218, 13714390742, 13714688389, 13824309377, 15330268163, 18337058333, 13145984080, 18697184564, 15899896382, 15012621848, 17676166530, 15017842110, 13144813874, 15907622855, 18026361488, 18777845892, 18320807870, 13657348315, 13715126186, 13733286175, 18948784588, 15112399602, 13418305975, 15999573584, 18820844505, 17097245588, 18206608401, 13265393483, 13590220809, 13690999314, 13925003062, 13533128659, 13242433262, 15885503582, 13802438012, 18126133392, 15818634439, 15815570926, 13180800236, 13922821308, 15977980047, 13715179766, 18689223663, 13798229810, 13438219388, 15521133592, 13352807777, 18620355397, 13797159585, 15919785041, 15101031846, 13560239456, 15119338802, 17688741048, 15061071540, 13724249209, 13143609090, 13537643246, 13708259712, 13826531235, 15179284794, 18306913461, 13438810964, 15813717069, 15361654327, 13670080310, 13726243119, 13631590960, 13106812887, 13634735795, 15994816349, 13510909252, 18814181568, 13760714281, 18680380746, 15155516085, 18502002009, 15919849072, 13683990400, 13975622528, 15889313245, 17520480023, 15281211112, 15992413490, 13767624722, 15573871628, 15002706858, 15602321163, 18302997049, 13348302039, 13760141627, 15627551238, 15521098484, 13662491453, 18569454517, 13418652622, 13922726200, 18301575631, 13656559398, 18938067199, 13823678301, 15622362283, 18666287436, 18617181298, 15875525752, 13798286469, 13418662824, 13980357208, 18813460876, 15986610262, 17097232075, 13909252112, 13632252018, 13332666024, 15999550460, 13430543242, 13543308252, 18319782446, 13163750802, 13486373263, 13594086535, 15322270602, 15975142032, 18600580738, 18616839999, 13839123665, 15818690853, 13671882848, 13751903563, 18138436660, 13723766140, 13656609722, 15899888059, 15196153196, 13510340010, 15889775783, 18664384029, 13249850058, 18028794094, 13824529784, 13667084725, 18607272180, 17722617950, 15715176390, 13430407702, 15878911025, 18588765193, 18566632268, 18666974641, 13629091703, 13768248782, 13450442427, 13612942939, 13715116829, 13692162522, 13662654414, 18218360646, 13928738310, 18565698962, 15012646263, 17722487814, 13178596573, 13172772761, 15512456555, 13302950049, 17620714544, 13426913210, 13498613486, 13602580494, 13929529636, 13674035511, 15522579395, 13416389857, 18688828941, 18575691836, 13537714839, 13316909755, 18268028048, 13244807991, 13751086603, 13560482499, 13570570576, 15019237913, 13484861666, 13413155150, 13709692782, 13691650552, 13724308245, 13927492114, 18902446112, 13417343778, 13423769952, 18312345370, 13865564736, 17666127757, 13317854819, 18680308780, 15018756634, 18588280614]
	phone = [15361566509, 15542392029, 13590207500, 13825922270, 13544422821, 13531367600, 13714269622, 13760448278, 18681507996, 13637242759, 15603018541, 13358273133, 13715501342, 18620355090, 18674536698, 13751090544, 13543337629, 15625269505, 13631575692, 13266784810, 13578646391, 15237111191, 15367683287, 13682659350, 18211558683, 13560751893, 15889137146, 15736775677, 13794808673, 13543298459, 13825779586, 15817216468, 18664588021, 13538068587, 15009456399, 13611075246, 13603002358, 13493961468, 13461809065, 13005420382, 13924599531, 13713550756, 13711524566, 18922141913, 18824225281, 15625017674, 13418494293, 13827449709, 13530416309, 18566653795, 18702606919, 13692164008, 17691040478, 18646463020, 13682439910, 13100895651, 15015109193, 13715079493, 13537806807, 15975570883, 15915409897, 15811801946, 13591461312, 13534143654, 17688830741, 15521026469, 13969054459, 15099927428, 13760635354, 13410139218, 13825201596, 15814032667, 13528735011, 18420386925, 18576400617, 13928853025, 13247336227, 18823844149, 13600395956, 13902264631, 15997360242, 13713853741, 13266533966, 13715025303, 18312536350, 18813867263, 18838903897, 13620205336, 17042205791, 13452360520, 13794530042, 15057969479, 13794458203, 18818587686, 15994771882, 13478694366, 13543465294, 15994945981, 15797708275, 13035602407, 15917454123, 13480634573, 13926552733, 18588261485, 13919833552, 15818627621, 13670162820, 13623075762, 13512738730, 13794849338, 15818821498, 17727524095, 18718562319, 15507515268, 13530003043, 13823599583, 18575393281, 13266579764, 18674634746, 18565789383, 13691980083, 15562596293, 13725535385, 17612092555, 15820284981, 13076995685, 15051882728, 15989245278, 13926411857, 13714759390, 13072285519, 13530138558, 13714762557, 18680302161, 13534445447, 18520818368, 13510143900, 13723729377, 13637906638, 18770873133, 18575549965, 13424177255, 13570929269, 18689462556, 18777456270, 18520867371, 13631673065, 13686843892, 15820451196, 13759768598, 15219496747, 17301936429, 18566297667, 13480117996, 15016649187, 13480301696, 13528846939, 17520607631, 13530972721, 17820211607, 13798291104, 18038048570, 13926581453, 13424203413, 13570866405, 18680664984, 15889356255, 15066828688, 13066188907, 15014002497, 18520869828, 13434487328, 15920535832, 17765291245, 15715802832, 13530976749, 13428934821, 18566658649, 13119896520, 15217559358, 13544033862, 15820228300, 15800285051, 18688736043, 13626669263, 13031911693, 15775696981, 18665986317, 13682683901, 13418716543, 13955051035, 13824349545, 15820752800, 15914174008, 13681356559, 17071636057, 18608683173, 15999627128, 15529001231, 13418519155]
	i = 1
	while i<=600:
		register(phone[i-1])
		i += 1
		time.sleep(random.randint(1,3))