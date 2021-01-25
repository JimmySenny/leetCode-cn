#!/usr/bin/env  python3

import time
class Solution:
    #def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    def findRestaurant(self, list1, list2):
        # 哈希表 交叉遍历比较
        hashmap = {}
        for i,s1 in enumerate(list1):
            for j,s2 in enumerate(list2):
                if s1 == s2:
                    #print("i,j,i+j", i,j,i+j)
                    if hashmap.get(i+j) and s1 not in hashmap.get(i+j):
                        hashmap[i+j].append(list1[i])
                    else:
                        hashmap[i+j] = [list1[i]]
                    if 809 == i + j:
                        print("v", hashmap.get(i+j))
                    """
                    st = [list1[i]]
                    #print("i,j", i,j)
                    if i+j in hashmap.keys() and s1 not in hashmap.get(i+j):
                        st.append(hashmap.get(i+j))
                        hashmap[i+j] = st
                        pass
                    else:
                        hashmap.setdefault(i+j,st)
                    #print("st",st)
                    #print("v", hashmap.get(i+j))
                    """
        #minIndex = float("inf")
        minIndex = len(list1) + len(list2)
        for k in hashmap.keys():
            minIndex = min(minIndex, k)
        #print("minIndex", minIndex,hashmap.get(minIndex))
        return hashmap.get(minIndex)
    def findRestaurant2(self, list1, list2):
        # 哈希表 线性遍历比较
        # 第一次遍历，将list1的值和Index添加进字典；
        hashmaplist1 = {}
        for i,s1 in enumerate(list1):
            hashmaplist1[s1] = i
        # 第二次遍历，判断list2的值是否在字典中，
        # 如果在的话，更新最小Index，如果Index相等，增加答案。 
        res = []
        minIndex = float("inf")
        curIndex = 0
        for j,s2 in enumerate(list2):
            if s2 in hashmaplist1:
                curIndex = j + hashmaplist1[s2]
                if curIndex < minIndex:
                    minIndex = curIndex
                    res = [list2[j]]
                elif curIndex == minIndex:
                    res.append(list2[j])
        return res
    def findRestaurantForce(self, list1, list2):
        # 遍历sum(下标和)，并判断是否有字符串分别出现在list1和list2中,i,j
        # 且下标和为sum, i + j = sum, 0 < i < len1, 0 < j < len2 
        len1, len2 = len(list1), len(list2)
        res = []
        for sumIndex in range(len1+len2-1):
            for i in range(sumIndex):
                if (i<len1) and sumIndex-i<len2 and list1[i]==list2[sumIndex-i]:
                    res.append(list1[i])
            if res:
                break
            pass
        print(res)
        return res
                




def main():
    s = Solution()

    """
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
    list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
    timeStamp1 = time.time()
    print(s.findRestaurant(list1,list2))
    timeStamp2 = time.time()
    print(timeStamp2-timeStamp1)
    """

    list1 = ["tt","ymlmxswzgfjgwrwky","m","sptlmcdijdsywqlkyaeborjerjgspr","pfsbenffrarsleywfigzjeg","cy","mzrzpqzpcmznthjtldoxixvr","ighiqrknopkufowwf","q","zfkkxbbbjmonswpuoydwsrp","pxcunqlu","kxyitdrbnkngbdidm","eidmpivxzlnjhy","aiochdomqqto","pppxnyvwqmxhekdoheopipt","gruaoodyqclmztxwqfvxcdiftqcmv","ezrbsqwxbl","qhtlpdmwjiwvshy","dlcualtjzitrm","lttzxyppzqsddnleyhrrwtr","olbcoxoe","dzwhbfpl","snwgqh","moenxwpxgeizwmufgkyhi","unqmbftbgvoyfstobeulvvmvlpee","abyle","tezdwinrsimiuciyznjuwlctxbd","rpgah","ruhbpsxisdbwbvjpuezllajdp","vqwwhrzcqcccijccwikcbdyywzf","rvwooywwwx","boqqs","gerqdhe","dglhczubhmheo","cflekpdqfmziof","ryhxeq","tzrkhpwcrvkvqleobdapwmbhbh","fgdfvpdo","liqksnspsbyfaw","kmbxchexjfbycaxrvpnxp","rdijvcrelhcc","jaqccc","sbjwli","shnmyyqvmugsqus","itiruoigrsxxcxkuzaegq","uowrlaosvjmfaiojlweyfvlhx","uaehrbdowsxhelsfpxmzz","im","cbt","mifmzxpbqdgfol","ttpf","x","yjfwkjzgqftbocqgzeehey","uxxuevlbosj","uhhghualhayhdyoaznsrvesgs","fohviowvodtbq","hwyhfiqkzlyovepiwkzhfwlrywza","hbnodwnukxncktihnl","axcqwbnsrhkybglggetxm","ighymdmvytynnkz","eagbltmrydioadrqatpykeh","kopriuq","klujzrrblyonoubyzkblp","lzpfeyeulppuhscgbhtlmgpq","lphswbpeimsxhgi","hfrkvs","ttcwsjadcdfyrxolvzeqxwkqdsynnr","fgjpjnppqlevugjbvftlvibwot","hyhuerngb","dkzwxkymsongsxdmofvlxg","lmpzzmznsdhc","mwvgmzmyxfwitdgmkf","iffrmao","ndgkcizbkvumzmzlxqzulufnk","ufvlrkufwzdbsmtp","ckqqqsqgjodjwuesljkptryjcvjkds","kgnuabcrcshxihlhzl","gndwjnpyh","kuonak","nbaqu","dmkxnxzmureedlnchvezafxyr","zlpbf","uuf","ipjlhkdqecqpluljgywtbtxfdo","hwkzehtdigrgyzblniwattix","jbfjbqeydufnjndtbkl","plimghfsewdodaymlx","kunuvkb","hlmm","raqrtgesxygacsmtoddxjqdeknkg","epcgiqvvctrpfrhytp","hubvsfxtquipnyfmm","jbbprjsksrtbguockujlttymqzxpdb","bpejstdjdknpvayyfhdda","lfeepxgaftg","ljilplbiunur","qxjxxswcjhgs","gnqkog","uuwvicikcbktan","rxkbrqqh","ttjegqr","flotflku","hbygsyrxlurojfavyez","hzyooxmpmpznvnbvnkdzfqs","biexiddklhyxax","nrhyqpefhmi","kvawxecueveec","cincvqvpuxfnxi","ucyxyt","ajeudmewgsqu","ibojejvcfgpbjfdwbyelwwpyn","euqxdmin","ljdulbzcymlivlftemeo","l","uamnqpaksqyzpkla","nqmpmnqgypsmhuudospfnwuv","ugeoewxqc","uarqpvoucbygszdhmprvlyy","ltjpmoal","jfzgcntikvmij","umgpgp","lkuteqaztfuxy","nngrj","brwdoswsxtfdncudilixmzofe","h","aojeds","edgobnpjzybqpa","odwnasfykr","gpshguadkjeklryqtduekmxd","qrpyqadebkuzzofhkvqbfwhpugp","ozssgeyddyjoolwulodcerkk","hxmogniktdprfvtbrwozkwupud","xazalitftocoo","sidakvzftpidoozvemb","hlknbwig","zijqituuyckvmpdizmghdl","rzzawwlrfttlsvpkmeopvw","sgdfirsnbphen","nkeyroehfvwfiteepgvzjyevry","pczpoajmlhvkkmawkbpalsmvvvm","yeaxuyjyrxtrsfrvlwc","a","jcdwooajlrdswuxhyivepcqigs","uixegudsskgndlehkxgslrr","otgyzbuxrjlhoujf","lxtlftfvk","skgfasgfqlilnkqisaxmvhkwdhnt","xduopjsuzrlsabgxapzeuld","dzsndweobhzcakrueevdg","aklibpzclbpxlqfauxevsnp","tqdrovqozuul","es","xsmhrisrkjmb","s","qxm","tiyaczwh","cxkfyrxupgwztwtfequztu","ouxtsutdlt","vtzf","hpbuztstzffkqlmlelulfodsj","saiobwffifhjekxnortkxsogkgce","pbmrd","hdyzraajvfbnzvwggjvxpqzxb","tfvllzrgoqgticq","jbodoxiqetkknul","hqqumsnbcawjmfbcwprjzod","qihtkg","dztilrjzzhwmmlybfpmegrxnefhu","xymwezglkhk","fluupktpkkqomozjbtebccjaxoogx","gahnnjgqcuhhrkbhraenlplss","himzsnjhxhxaersjleptlehia","lsfgbkwguheafpaxffhfxbpr","qktnvhyqzrfekbcgknpndoethl","se","xvoitdqnxslptrzbbbgvvond","govqvxxqkvgq","knxnrmqxzgzxrxbmvjijmegmqs","fsgeiqyzkotqwovwmsgoufkom","mtmxmvemslsoikkpforhecawjpthbs","iqapcatbmjv","wrjbfwkerzwg","tfnzkpzqjeveuzynauprcqtsuyafz","ukethqmdefjny","ifuidehgebxfnjww","dbptzbbzisaripjffjllwygwpzrxjf","xpzboyyugirhzemuyczhwm","hhqxqffxxfv","hgoesyvhlqgrzzkbmkx","cifvkapnwhlwge","wzhicdsciqcsn","zxmieefjwihlw","xtxazeffclcexzmeaycjjmajshv","xqkrqiowhqtmvktkzw","sdcjazwkoaxzvfibezuobaapzxt","mfnxfzjfkhhsg","ezzemdjhnsfi","vqosfqzswjb","kvdeqxesnbfhjbxuweyy","frugxsadoonqjt","zbswentubjugaaazjopvorij","jbyqcqtulsgrev","mcmlolerusdcswu","joqlzhffhwt","tzbubujkseyfkyngmyxoggwjqfyx","dnhhkdkchtvedfvvqhvcyomraih","rgvqedd","rgcwuyvxcedojsqsvguq","piyi","ogiuntjpfsvaahppvbmvblmg","elmawzkeisceowvgqu","hnkekswifkp","fjlhveplzxjkboerra","qobibsgjpzeo","kzvzcmylggozqyuhdv","qgdygmxmhndsnfasrequy","cfikawuztjfgbjq","iytaamorcwdvsvbopaoibgimwdgoq","jazjsenkuhwxyadoj","hzfdtbkltppxifzaqd","ngwrwbitnizquzubcmbqnty","rsfkpeucjvcvsyzdxqovfe","xexp","zbmfnskvsprfkmnlceyhwnmmleqr","ayhndlmoncvz","bzlqiynizzxmalbwcqjjllrplkv","vwaxdwgyocqxcbeiragiujyz","qkgbyibl","smygecysrkctzdaxrnoujhe","wkmmafwgtuqax","ovnxkpueoll","ikbobzuxwqtqiysopsp","toefaqhryjvufau","wcknyykbdgdqfoiyxwykkjgfmmgeup","ijqjcftcefcvsobsnywb","zzipzeaupqnsuugxicjojthg","ancbmeoklxzocevj","cqthrpqqkoffarsvl","ypdccysrhavpemcfw","hcaegubchzymfiymhrx","dlttlinurazlzzohstawpzrm","zijxdvyeryowylzemzpxmmi","ysxoyobphudyfz","oigzvomuntci","xategdafpthfyimy","eqvozcnrrtwivsxulpthgqgo","icgnxvf","prygvdkn","vrlipcacfsbqpdorzcetfdifg","izkoaumsaxykmmxrmqkailci","tkukbvzyqmingifrsagroqlskc","xqbewkuapzsbxkmij","cbqhxfyddsljmejqlrkpnsywpo","wpatkadvzgkuzdex","ovbqoeyowayrgyzyghyzjh","zxhqqmlbwuwpmipheqdk","agdwzefqjefqxjqqnkgnzkarovbtsy","jqkyy","trwxntdkqugaszdrhlliuxwtdsdte","ovxyhvtuln","fepdap","loyolizemdjbjtswrmevpwx","ggsifyfxlcmczbbsews","keydevouytrexndpxgjeklro","zikcykvdegerdxrpludstkdedgpvka","rgcfeqtnurfissqbzrvnozsvglgouo","eppxarvxswjngpgaoqimpwbnn","zroawyqqjsen","wiedrwfuhku","uwunzghrwfmubaiskqkgdpof","cwzyawjshlkamlrfepgahy","wxkqsbgbybxiundraolkidmq","rjoiqdyqcjpgmmkdhwzejjnbhszcce","irppitpnfeaupwovgmqilhxvdnhx","yyuptiwveukajjqy","nviswxjohavescjh","vuxujjgrnu","vvnllmcnhumomimsgcapoalroesjv","kxkmdhubufprfcaqiesgeskpk","qzsbqpkhdwxlujevptcuybxudzp","wjvvhpvhzrwskfqjawuxrsbqiqhugq","mmmmgivtylfha","xnfyfhqfnaysweif","lftckbrjqgugrtyyekabfpgf","gzfkwfkugdlohilycwgitmrbjx","huzlsrzvxuvuatuoohtcmijkc","lhjqhozpjqamxkkeyyrefmfyvso","sekitazbmshnzwsvsbiucrm","mxqxrhurfwzttcvohjmuxqarex","upxlcmivftjaowwozghzstlvciblwa","zjkkyugzmbtldazxdtsugsx","kjampmqrbbadf","wupxdaex","mfzizdcrhejnfntemslpmpbrv","mlcjbhsovogdhrddwmege","ftjbkbwwbmqhidftjow","lplvmrrspw","cnpadyfbsrscwyjnszlmapnjlv","hjojmzaaanwgl","yxhxgsinachceuhtdcmy","pxwllxjvcqepoqlccb","uuicetphghvkyeuerlipqlkmg","yyotfcpvitma","txzinypknlytydalfuqftkxot","aeqebtbstp","fsmuvbntbdyr","lpvawbrntrwzaxospvvepcvvdsn","hgehk","pbfmvhlxauzuwkipau","bvksdpuahbraombxpodjayaj","fhiljxxefqvjxpinukhxcohkda","xvzafbijvagqtwvzywqlvzdw","mdkwgbuawwzyquwegq","eyju","yubtvxrurykefarjnbz","uscrnqvolsjwbruo","kxnbmeusrvrmeihlcfhbfmzlc","qtjopibbhwfgvbseemlyahizea","yztuaagcvuoolimkjvxwatvp","hnsriqceqhxszer","vfkmxiewgzfxejabo","bvmpabbjscjyvqbrijdmnvwcp","hmbowfjzsuebtwdyzuzzkxqetipfre","xwguauoyuyukrsogmk","kwbmcubzosg","hzrcbftnoeqzdujzphanrmm","ub","dejdxtjgmwoiqtrhwoqiqa","ntridmgeuzhb","vkkhroagkeewav","owfqaovcjpvpqnpgrcgofbpcp","shwmezsrmrkygfbsmloajs","fiknafypwglwc","utqghqkavkuwlewcy","limeivcruynrkfcq","hwfrtdkgsihtrevob","lfuqmyrahzqkksqcjes","ztdtghnsgoerwp","qxtpbzjikguzoeiwbtb","zkgbhfxcoqisxvynu","awlkxp","nuvioxoftodogtkaailbpdptsatg","vlrrafhtzqss","hrvqewtxvljnvqbcwg","syvijkrallqrpgsopka","olajgsznpe","ryqgfxhdxsshfykugurhlbd","kqmvsexjvvnhnlpl","eohzhcpmhuvllout","ywspqowuqlcyunbqlimwngfxelfz","qmtjjhghsvbkkmxqkzufyxfpzzujf","yuzglufiwpsgtmqjoupzul","twndfgfjzhnrgiouciaa","crftcllsqkaxarsgpchaetgswujela","lrxlwodfshltzquorts","vjsjmoiwxcxtdq","uvvjnpuooevtcdz","cqxwconuyujrogmolju","zovzxzkqejjlhacuazaordmagpglun","txyfcikkpjjjusiuvrtagsuf","htysagzjgvjlizvonlqt","mxfkeckppjywrzfyuimcyem","ezisrxdvwexzzgnx","chebkaevvrgggqyhfujstzgiwzxrsu","kwxheyqmeiiq","tpgwfccafzbzbhrstnhlwaevaa","cxdgrxpoo","jzxlhlvmptbtxwwsppomorghhuy","ygvfcgsvakzaaalxcjqlgblcsigy","psrljsjdwuhqoazmvkirjgrppmurem","ksbpjxizdlodonhfbvss","raowzggriibccpte","kesiryhpas","ptsprvmhntujnwoseyavujzfc","uppoeskbbeawahzu","wzuxduheaffxl","jmqomtmksfajjtzbfrrsg","xcuewwbbhjqhktwy","zvjkoufzudabvvfmqygevutsi","alsfnvjualdffcsciabpzjlfsh","bftkbxnvpy","takwmclgdtuqpxbxpfgydxyopgkpnk","qxmfsobbzybrx","yvj","qipaehcfof","bvsaoqqecsiktxrfqmcr","gzrvh","thgcmqndebjwroeztebctmdkxgll","kyvmufripmexmhgl","ttxepmhwbgbzypmuybyeaaoqwqka","jfosgwsoqynnewzydiz","vpqinqlylpiqxlvaxirmxpyahdew","tnfnoaqpcyfybsxywkiioo","ndclpgzajmsibmz","xjqwkayccpfstqglebkhdk","vhdadutwcmhyugtjljlnbgtjh","hitimcysgpsxs","yzvizqequnckaynxhsocusuji","vxpxemgnvkdtopmgcqq","zvmopohgcavuskhpyorghggwfze","oxuyylozmnuqhdrnyiwlqvi","mwohrfmpfstsghjazakuzf","anfoesoelmfsjxraatwztrzeuvh","ypfykmezswsqdf","oabrzjdvxrjgcolklajadgdujzshdi","sfssrgjdgtfmcgrxifmvust"]
    list2 = ["lukgfhvzphndszxuu","wjuvgbvhiktyqsacjtyj","jeodsxoelkczggbbtvxbtlp","gtthhcfvmzjamnkxmlkf","mggnscyymkzbhhl","kbxbjcvlndl","elqovvhvbsmz","qknyqioavygbvzvynlct","ejhqwqnakghnhot","pshmnjewjfywtznpk","biq","jigmfclthonqp","fbubljitauzrgpxsegytyklzdo","yrrvueuvz","lemzr","d","wwmiomcgornpnjvu","ottyflggzfmtcouvdxusiphlqabejv","rcpyogdx","khleqhbaj","fqdcfoqra","omzllqjowxovptsxvhmpt","ekqvfygk","bacujeberpw","nguieyrtcxjyslvtdlrrsseertfs","fzniocjpzuuxnwwkaotseddjdhvqy","vpnzccwjgatsi","ndzprgzwfdpfdbteaiushwqs","hyhkvavecqfxjyq","nwykqd","tivvjiree","qrttqwagqimmtuenqsbhdotil","gttdfyflksyvdofzycaiir","wazmep","xsobmxe","kvqmwhrsvpqvjcughiirovb","nirpnokripyakcyhcbcsxi","nswfgvjbzqkixsfphpd","jod","pngc","qe","fydsrxrofhzralfrdssgjxzpmeu","tbkbvnhbelozqdasqibgecxagfeap","rywrxli","xusssllpjgvf","bakkzqmrvrwjlwtupzrsiwbhnlfw","cjrayjfslfnuq","w","rkdbqqsgpcjmwikfeynqtbdyir","erniwixhftjpigfgqe","tvrqdgvvxl","dvzdfoaqbvrhdkasoc","uay","uegcvwmgtxmdrqjm","ixtifakiluvz","xlwcgdyyrawlhjfnsjekh","bvhvizthdfoxxfakngygm","onxkskxkrkxevesdemncaphmao","gwzbfavhxkahqedofzmxthfys","juiq","qpxnaaiygn","xskikotkrtcmfrkzipcg","ixpadfrugophitf","meqilsxqwwdxsbdxhwuykhgee","svjnqdl","ghibpasmxygfnb","xrum","hqvjygbysqhmuliejnfhrvdksvj","mxuefhqsrre","hfwbgbziuaxfqwglihpxinlzonwslw","qxfgsgwvapshtvhujksaphbzaj","glavu","gclqhjfywelsamicqfprgmep","wiuay","aqpyysoktbvdfyy","szi","ezkrpbzxtqkugqv","yesofvitaddedgzqlhkf","psyjtsftxbohwieemuqyqcmxmqbkoi","lcqtickcvpbzskrtjrgmbxcn","ooupjfmxtzzghhpbtfhdrnzwbay","igryxtyxrsciiteyykpwsejzkoudls","ngdxa","pgghiszypqlsqapw","juyb","hdypcofnn","ltmiloashemqqyxrrmrfigxtz","ngjjqgokcgxaysi","jgqddgfqtesfmijlnmt","dgkprzspgmxncfrimiv","eusookwietituirowwtwbfdrpcfkj","jwerlwszrqjco","eiephnrdeqrzmmsiz","yxmqw","jeixuxwksrgattabh","bzqbpgtuysksrgljopibyk","hfixtzswlpzmcauiwhki","zvxjsmkcryfafhyrjoeymwg","rxyzkxczdgxubheounure","bomoysvocabceeauvobofltf","fiwozzuztcmtxnj","ndsgskwqjwqgwghrfrviqtvn","ql","wmsahdmviukfym","govxqung","ebajmltgtpj","rczedbgzfwztbrpyhuzscziwq","zjfcoggrvzjt","jrbcqxnoxlxdtkhevfihgbsc","pzzuucthxysonvwdclxi","pxufhfjteuhnzw","dwrfvtcotfefapujit","tleqbkhvvmkjwghke","rgyqabklalhefdywyuwn","lhftqpquxefzwgyuz","zieoxszmgn","mcj","ivfrpdoyqcmxya","xxtphbtf","gzjvbqogsuqvdjuewi","qpyemyekea","hxgrxkcmuajbnbmnnesnxfiba","mr","ahptxezuyxig","bipxskuuydjguuvqpouoclcxg","erqiejjtcwrgtdvmpmr","ovur","pmpphe","t","swdeosuwqeynspzdqzadmtopejocg","hcnarsjqc","vijzmkbdzu","k","nzbretavyrrby","lfcknoeld","cmdpmvasomwasfgfjyitqjr","vwfmsbh","nzrqtdm","wbhhtmtuiyqrr","drfwehgbc","toniqxic","wrvikxgymuekjufrmfpttxzhu","beiompq","tqhazkkobqo","qmrbnhrbprhlbtqotofgps","mdesjgnktbguginwmfz","ifbzpvykgswhnpaarecwmzcp","joiwkuqzevkqzekmcvynekvdvnfe","dagsoucuafxxbwkucctmrl","yoll","cty","ircleszyobxrwlfljyuwjgmxrcror","pkidfteoxwseosmoox","pumn","qrlr","nmyijjdvygqarjejdkan","akvuxbobyikzdpbylmt","ahpzluyihm","vjyaytwmlepxxpsyf","ycnubuqxcuaixwpnwatyeltiscl","fvbcykmjpvbjm","tqdweyhamvrr","bcjtmymzuafhrzzhdwx","xiamvhcbeti","ahillprlywqazflvnolvzapsywnr","ggwbjytfhvpbfwdfyjuticzpl","jlda","hkmcmyfjlzkxvsvbojkhtrzunoonqx","rxkzvmsyqggzulc","vvotkltcrcxqdtajgdyyucos","zf","svikkvfzneghmd","uudrvnhsowhfyqleckc","rhrtdaqovhodvherzvl","jert","jbkpsxfhtz","tpntjtrpmdixizyufnar","ozmhcdagffcuatcfwvexkhvmxx","ixxtfevrgzdzazazmdtcnxs","ilmuwlgufseopcsalajopfktdag","ic","quldbzqkv","zzznxpueqvbzqjbsdryvvxevvpgqgm","kkyahaqwtchrhzxsjpz","zurhwpuwohlrkgtglrwdrjp","ilpavqasaihfxovifhrgw","wycees","egqdvriwqvfgo","jxqrjruibvnwu","yvg","okkfan","vofywesozpcbicdvjfkarblyvamgwp","xzcdfhaqbybbeiqithdpfbpyxaomnp","fgkixdogvpuomdpcmdwc","uqptskmgjzaupsmuhchqbkgsunv","awrmmnbvfrr","ogjedtdgzkguuwwvlek","tjaievlh","atewfh","hzzycyabbivqwzyzoflgkkvmsjntgi","valzywfbipdkoinudoygrkggvrqpta","gerrltdkyhovccinxrzddakg","gxcvqacdicoyluultv","abvwdprt","pcvyxdndhxhkpkgvzqligv","ibdifhzewvxe","bemh","vceqlinqehb","pcxnm","tzgtjxzcvcmkyafyi","gzeoncreoxxhihgi","vfrcz","zfvqqzenzlpvfnvjiebeksp","eggiiguelerjrjqnldwlqynce","idzbrqfumsxzh","oiigypiajdumxd","quultahiwjjjhglnhjfvsn","umvpjkvsbqafvos","hwxzoqfuivmx","lopdgvqraroalxmtgo","mkqwrozeasy","fvtgthauirejp","adrishxrrakbymujyhybukaksqako","cpyaxrgxzqzd","kpkjmczgkrncoiaseujblttcapafi","qxqqledvinyldkexjrlhuc","qvedperkfbihclqnktptbfqnvispyg","iddfyoqvfrmaebcznesd","dufrqlwxnsstamgykxgopothviqbmi","eaudalgibns","wdvhbmnjwlmdzakyagbpyudbd","cebqiuefwcmyxogudfvrhsko","qitoxttm","weqzatuzixwtcilieiwrgpu","pkgzgjitnnyenxsriobgoclqm","pvdsx","gjjhym","vrlsqnavivjezfbmlasvnfppae","ay","yviqhkt","eaafmgkmvehkpo","rqkgidjsiat","jmwwonyxicnayxursry","zakskyquxrs","czbnvcmpfsfbxjczuigrsz","frnproerfhikhiimkzoxarpipowl","tuaqqboxivgvbvztog","kmhonsugrnvwkdmqqinqbehn","uwebakbvouyzoqvfqna","tlahsqopgqgvyhiymvxvmdsfw","fytrazlfbbffwkkunuemkcxyeqalbv","ldwqxohm","mlgsbjrfsgwlgujwqjbw","wgyvdxitdl","boaavxt","vsscmtnvdvwweud","guzorktskrtmfxuopcbmyatz","u","hslzvtmmx","mllspvqablhntgubd","jqckujv","wegvncc","jlwitntwvwpmyiyyrahhvnu","jlgjmxworiow","gfyspy","zvfkwlbpqmnrcgflc","peeta","ykcingdx","sbdxynjnkbwxaajyponvzkzon","xjbzqvhruuqyrxr","ltcvztsmxwgqrxymgc","ydjnaonwjkbvsiysefcyrqgjqbeph","dbhvwypiw","ubsvfdzzvpjmhlujo","kghexntvcnc","smxmpovd","htlmxuzwmemyeprtuihuyehrl","tifpshkyyfz","qkejdvjgcocpfsmjhmpevae","mnnwxtvnzbymek","aatlygcyknnxmezcotqttfzxftntek","ijalnzmkcdyfsiwwggmbezxmsjpz","sz","etcxvxyvbpysnxlgimssijehcfv","fctzcrbxbindlvsbruqwtxjo","uwqba","nzta","gf","qvlafropazglytfissukgcprgc","syarjfzpefvdiyo","kegczncp","kapqgczkzohtjtvlezxlyi","ygvqbbcoawhuhkqiwrdmz","wctukgtfvrnwxmusarashgpteuz","slzkazpagckwdenpsglymvsmuz","yzjsvarsktamgohtntrpp","pmwj","hdgbzbok","apocjag","qgmqnstukjspervoox","cmyqiqdfvfhakrsruekfl","vqsfzhuvbmlbze","pbxavkqhongpasfhox","zjvdphpzzve","lobjkzrmugrvcmk","gjcoyoqwqdk","wcgiufzldphwkduukjdquveib","rneympfghwjsvzaw","icqmvnwdjtwjkv","kmri","zlmjztyfnicepnvkoulswa","tgkfhgp","ebghxamukquf","ymbhojhcssco","ekpclqdyouhdya","fwrs","likho","jrobastcxnel","xahgsfzkeyenuts","gtsqdzrqqgnsijasieeiehvg","qrixocsoihedmvpf","xpjqllxvrhwrhflxd","pefblawfoaczmuvgbo","kablo","cuarcbazoi","wbhenigtfzelyfrngh","hisbgots","imdqvob","znemsneyrobbdlvnafbmdtcv","jrwkkzpgtnqrd","mwljadohvyeazfnhjvx","zozkxjuaopfszzk","ptdrnzuddcuorqbqzwrlvngsmkap","rh","qafjyvoju","xuqtxdnavhnbsxzuiqcvxrlhkr","putvgvsqtfrbcl","ibgyjqjqgvghyfgvdjahzxukjlbvzv","matunkznewjrqowokqfpiyacqrxq","ibuiacqcojcvyqspcztbjmabdqw","wgowwulnglkzxeyy","igcmvomnzi","fpxlf","ywulwfkppwozgvhtct","cvfnuibyxdaqejycrfjly","ghmbdaqjhtgiecitqooxuclezx","vw","dijxyd","spt","vhinhtuzrpbjitemoskoukojfj","jxhqmihjq","fvjpz","wincnzcdumff","kgr","kxlqwxvqvbteq","kbimhfetqhocthhyams","fiaqbuhxrziynkzvznjuupiqy","ewxqumcwvxlghwohgycq","gxhkpikkstucheihxrfgmpxgri","wwcguoabznntaeke","pwe","cizmywkpzlrittzfwrsvtoomgxwni","odvkhtrfwrpzibkidzaqdcbbbused","g","wjagjzezootium","dmzoxtguccjox","pbu","vtqpkjrplhxihlvfkncaxi","wfdvejqimfvunjldttwtzbyms","mgsbvdxvzbxehetrcdvv","xotzopcdlddwmdxdeg","mxzcvxneiroyoecyfko","y","n","eocl","beszsqsfemgtfipgjvgvwye","wofzxpqucxabywfjdivcpxz","yrkziunj","saqhgomhjmltbsxltgeoracriv","hndclklsstpbmvtyecbo","gfbuprwnoksbsknfub","znaylpg","psjavbogafyeuea","oaxyr","vcsxbzri","plyxswhlypxurgwm","hfxrgtzkfonwfohcqcdcwqxpqxox","lnroixczynpsssqdurfsqxfhjnt","auaxgmnnfrnrhypfz","mnsggibecipmolkr","vjyeiukhfaigpv","pptiwqfqpamapm","lizbmxovptpcmwymjtwakqxrnpodoq","ymsdqqvzolrcws","bzblrbnawn","lgmmlyrbtbkofufestjrieasux","iqhyjqifyx","bwagxaajhcsqrtdcwjfbvowzkqcry","qwsfph","kwqlkioucosaqwovcxevycprn","mmeltnktryvpormcqrfm","cwddqobkbewjeiothaycvfsxgg","stzavalphrqmmgyl","knkihawunfobepvbug","ryowgmfufm","gntleif","txffoidzwhhogimirfnwcow","osercemuzinmuqujcth","gacisrdkkesnygwmxefzbkglqkein","jta","ktiisxakxjsgssyznblffrlorvj","nndnt","uzbfaxkocqwklzanucy","zqynbaau","zeghjpjdsyzijnrhlrrtzapcc","cgrqqtellrfdu","dddjtluxrzvabqymawohkghe","ngjfjby","yfyvozzsb","kqxvqeejjwozaexonylweffewhydy","mixphl","paqzkfhurempgpimesfzzedplnubt","isnbtigafwuj","isngrmeivpnvyfnolemaplrhifiei","kafihqwvcnlqyhn","gnyjyzwukvyxpxbixviy","fn","xysybsszrqvjfot","pcnidiakpmrsfd","iirbiviewrldvebcoikcczayls","zazveqgjurxrciqcaib","mlzjzntjtotxa","gjunjqfywj","sdartmbugpieahhcwbbfpnbnlhdkvy","hbfujhfk","xbliovle","jdlvqwk","pcricqvtulqqfmcghyydtdfibmo","wgtgtcnfganbjwob","tgmnyyjdvejhk","ymyahklayyfronpsbpjxchg","jamlgxdijfcqanvvrcclffwsppmkbb","laiqoanffmeoslxjgzbfacwuajsipl","oaxzvr","wzgwavmkt","waj","avudil","lyehwatmyk","vwfd","fysob","hbshtjopwjnurzfyrrrmmkiy","xommcvvbwlaj","kvpcxysgnlgivshhpfmqpiaqkqb","qc","drmhelcxcg","pnffvnwrhnlhunewteppbqjol","lazmsyclqa","icnjnuvqgmprgwc","ndacfbv","xdtugscgjbnfuwxogtnbhxwjz","ewjxhnmp","gujmuzzbvsgzejw","evqrklcxgxdqkisvfgakhkmkoik","qwj","azzgsuttjj","ympdvitsczwdhxylusdhbivocikw","sxkygzfdohpqdmybnjpqvjr","eqwynrvlqh","aqunhvdbcudwbduuflahia","ljdslqaivfzhczbf","zxxvwcdlszfjphldhrfvblpakj","hv","xlirwzok","wk","otsyjxubiobajcfnh","vwve","kuhgxpmahrtzreknawgdfctodo","dlf","ujhml","ps","bdcraaqaaxusvnkrrrxplzudbl","vloqkeqznietcxtkcmj","qahxofzboem","xwqemizptcavrd","trd","qxqnmljjzlq","uvxzdyiuld","aptwscecfjzsvuk","jhhsgldmicsoboogdjrjbsxofmc","be","airdvhjssgbymc","jrabmvtbfxtxgocrrmgaazakwxv","uieawxkhkfjhfkzkfche","hdeedhdmaak","vuioh","rfiffadb","tzbwcxxwnabqgrasfg","noeahrjqbcculkrosvazd","qjckctqhasjykliaibeazx","wbogcpjp","crvxbznrvggnooioim","uzkwbdccovdtzpxgtyqjo","wqpgfblpdrttja","omyggchtnicqi","lmjgaahecand","yb","udjghqivyqzei","wvdnxeg","exjjkgdzgdp","znbqzxcyvtokkibmizwm","zsdigazu","gokorkmrncdm","bjllahmwmyzltxikaiiegrdpkps","jqbntbubwsyydc","kqrnhhsblsfuuadgelid","nbwonvyfftxlxifwq","atoxozzrviyafxfgzlkpucig","afrhhitwqomffbfmskfszur","yoakflecltptt","yxremwixkukmiwxq","uarcmh","yxmauxoddlathty","mcbrvfmwwcl","yqpdtekk","xigfajgp","aebjspyjzoytzwetdohjuylpams","nmpehaeouawcsidbkpbroispabpyqf","ytrimxnoihfafpsq","jxdrejppbgpvolfocboqcfvbkr","apkxbvq","kmgpjsbzgottvhmplmzbmtxsofdhtt","mthntbkqfedysvvgmitakeke","dvq","qmdlgxstkirameaoh","stcvmuuwv","xufoxmwckynqcphlkiv","nxegbfphvwvbtjjipsdt","pgmeiusqkyywdploaulobinsyy","imkgclqsygxsjcpwmfj","eeikcgkwxsrrzddocdbfgnjwhvb","qjthnfiiiujwh","nwrqjxgdmezankluvrj","gynxnfyjyukpmguydp","oogbdnrppt","vyxfrjyjeccwzl","omht","fsoma","uyvarmohopfpnsdkvbkvzy","mvz","ixyxcjy","tazhtiqiyxzbetdqqsqbtgh","bb","ky","wolkk","gxvhphjfr","etswuhhwobt","lbogmbrapntwdpxqzoqvthvorjh","lazqcjc","frsbm","higxphnvzpiqdzxtialuwfxxyx","wthpyqlpvybirkaozeweudkpiakt","hehsuxgviatzq","ofgycixomi","by","zgwfiycyxrrhisbzkijn","atlozwagevmcuclisovnxwhnlooqa","oabrzjdvxrjgcolklajadgdujzshdi","ypfykmezswsqdf","anfoesoelmfsjxraatwztrzeuvh","mwohrfmpfstsghjazakuzf","oxuyylozmnuqhdrnyiwlqvi","zvmopohgcavuskhpyorghggwfze","vxpxemgnvkdtopmgcqq","yzvizqequnckaynxhsocusuji","hitimcysgpsxs","vhdadutwcmhyugtjljlnbgtjh","ox","ukhpqmsp","tnfnoaqpcyfybsxywkiioo","vpqinqlylpiqxlvaxirmxpyahdew","jfosgwsoqynnewzydiz","ttxepmhwbgbzypmuybyeaaoqwqka","kyvmufripmexmhgl","thgcmqndebjwroeztebctmdkxgll","f","wsjrwnviiwbiltjyfweynqrqlhahdw","swrosmbskrormwnttirfnkh","cglaboshwlqunxhzdvcnrffrcnbinz","qxmfsobbzybrx","takwmclgdtuqpxbxpfgydxyopgkpnk","bftkbxnvpy","alsfnvjualdffcsciabpzjlfsh","zvjkoufzudabvvfmqygevutsi","qucbscbd","jmqomtmksfajjtzbfrrsg","wzuxduheaffxl","ssfymbzikhtrboqt","ptsprvmhntujnwoseyavujzfc","kesiryhpas","raowzggriibccpte","ksbpjxizdlodonhfbvss","psrljsjdwuhqoazmvkirjgrppmurem","ygvfcgsvakzaaalxcjqlgblcsigy","jzxlhlvmptbtxwwsppomorghhuy","oguezmqs","tpgwfccafzbzbhrstnhlwaevaa","kwxheyqmeiiq","chebkaevvrgggqyhfujstzgiwzxrsu","ezisrxdvwexzzgnx","mxfkeckppjywrzfyuimcyem","htysagzjgvjlizvonlqt","pc","zovzxzkqejjlhacuazaordmagpglun","yq","uvvjnpuooevtcdz","vjsjmoiwxcxtdq","lrxlwodfshltzquorts","crftcllsqkaxarsgpchaetgswujela","qvqbbhiocufckmeyyvr","yuzglufiwpsgtmqjoupzul","qmtjjhghsvbkkmxqkzufyxfpzzujf","ywspqowuqlcyunbqlimwngfxelfz","eohzhcpmhuvllout","kqmvsexjvvnhnlpl","ryqgfxhdxsshfykugurhlbd","olajgsznpe","jyxoaphhwgcbracqcqapqlagyqcjc","hrvqewtxvljnvqbcwg","vlrrafhtzqss","nuvioxoftodogtkaailbpdptsatg","hikvdszdonstggpwxtxwikpztevt","zkgbhfxcoqisxvynu","qxtpbzjikguzoeiwbtb","ztdtghnsgoerwp","wrrbnaueyniz","hwfrtdkgsihtrevob","limeivcruynrkfcq","utqghqkavkuwlewcy","fiknafypwglwc","shwmezsrmrkygfbsmloajs","owfqaovcjpvpqnpgrcgofbpcp","vkkhroagkeewav","ntridmgeuzhb","holwvhekup","waswwrdqxqdtzwfmm","hzrcbftnoeqzdujzphanrmm","kwbmcubzosg","xwguauoyuyukrsogmk","hmbowfjzsuebtwdyzuzzkxqetipfre","bvmpabbjscjyvqbrijdmnvwcp","vfkmxiewgzfxejabo","hnsriqceqhxszer","yztuaagcvuoolimkjvxwatvp","qtjopibbhwfgvbseemlyahizea","kxnbmeusrvrmeihlcfhbfmzlc","omjrvgtvlofaiufh","dvtaoqeacaaluskqqdhmuerjcyw","ttupgfb","mdkwgbuawwzyquwegq","xvzafbijvagqtwvzywqlvzdw","fhiljxxefqvjxpinukhxcohkda","bvksdpuahbraombxpodjayaj","pbfmvhlxauzuwkipau","pgxfnkbdgoztsaiexhugenlmz","zkxumizvzthjhqhiiyepfdhlimp","zmgd","aeqebtbstp","txzinypknlytydalfuqftkxot","yyotfcpvitma","uuicetphghvkyeuerlipqlkmg","pxwllxjvcqepoqlccb","uzsgdqvhfplpqrgrvicaxvkdhl","hjojmzaaanwgl","cnpadyfbsrscwyjnszlmapnjlv","lplvmrrspw","ftjbkbwwbmqhidftjow","mlcjbhsovogdhrddwmege","mfzizdcrhejnfntemslpmpbrv","iremxjh","nbogprsrilrmmsvcbwkwwobm","zjkkyugzmbtldazxdtsugsx","msfqrt","yfqexgfzzsz","sekitazbmshnzwsvsbiucrm","lhjqhozpjqamxkkeyyrefmfyvso","iigexfrelxlrkjckm","gzfkwfkugdlohilycwgitmrbjx","xa","xnfyfhqfnaysweif","qqrarmwasaibdcbeuswczzdmby","wjvvhpvhzrwskfqjawuxrsbqiqhugq","qzsbqpkhdwxlujevptcuybxudzp","kxkmdhubufprfcaqiesgeskpk","vvnllmcnhumomimsgcapoalroesjv","vuxujjgrnu","nviswxjohavescjh","yyuptiwveukajjqy","irppitpnfeaupwovgmqilhxvdnhx","ymontwijzcphsmpu","wxkqsbgbybxiundraolkidmq","cwzyawjshlkamlrfepgahy","uwunzghrwfmubaiskqkgdpof","wiedrwfuhku","zroawyqqjsen","eppxarvxswjngpgaoqimpwbnn","rgcfeqtnurfissqbzrvnozsvglgouo","zikcykvdegerdxrpludstkdedgpvka","keydevouytrexndpxgjeklro","ggsifyfxlcmczbbsews","loyolizemdjbjtswrmevpwx","lrkjarkkpo","ovxyhvtuln","trwxntdkqugaszdrhlliuxwtdsdte","xevtugwckxonclsqbbcgopz","agdwzefqjefqxjqqnkgnzkarovbtsy","zxhqqmlbwuwpmipheqdk","ovbqoeyowayrgyzyghyzjh","zdtdckehtsjrlvmaaafzykedesjw","nwlwgqnhktrdsolrywfpdhihyomcv","xqbewkuapzsbxkmij","tkukbvzyqmingifrsagroqlskc","cyy","vrlipcacfsbqpdorzcetfdifg","tmyeqibcdzebutginflfoagydhfs","wkexxrzhouquvchnplvtrocnxxaile","eqvozcnrrtwivsxulpthgqgo","xategdafpthfyimy","oigzvomuntci","ysxoyobphudyfz","zijxdvyeryowylzemzpxmmi","dlttlinurazlzzohstawpzrm","hcaegubchzymfiymhrx","ypdccysrhavpemcfw","cqthrpqqkoffarsvl","ancbmeoklxzocevj","zzipzeaupqnsuugxicjojthg","ijqjcftcefcvsobsnywb","wcknyykbdgdqfoiyxwykkjgfmmgeup","toefaqhryjvufau","ikbobzuxwqtqiysopsp","ovnxkpueoll","wkmmafwgtuqax","smygecysrkctzdaxrnoujhe","bthllqwgjhggvfqeriyh","vwaxdwgyocqxcbeiragiujyz","bzlqiynizzxmalbwcqjjllrplkv","aapifnzvepzobki","zbmfnskvsprfkmnlceyhwnmmleqr","quohumjpf","rsfkpeucjvcvsyzdxqovfe","ngwrwbitnizquzubcmbqnty","hzfdtbkltppxifzaqd","jazjsenkuhwxyadoj","iytaamorcwdvsvbopaoibgimwdgoq","cfikawuztjfgbjq","qgdygmxmhndsnfasrequy","kzvzcmylggozqyuhdv","qobibsgjpzeo","fjlhveplzxjkboerra","hnkekswifkp","elmawzkeisceowvgqu","ogiuntjpfsvaahppvbmvblmg","ctqdbxmkcgmfcyitoekmu","rgcwuyvxcedojsqsvguq","mwemijadtwkwunlztgmulocyrgj","dnhhkdkchtvedfvvqhvcyomraih","tzbubujkseyfkyngmyxoggwjqfyx","joqlzhffhwt","mcmlolerusdcswu","jbyqcqtulsgrev","zbswentubjugaaazjopvorij","frugxsadoonqjt","kvdeqxesnbfhjbxuweyy","vqosfqzswjb","ezzemdjhnsfi","mfnxfzjfkhhsg","sdcjazwkoaxzvfibezuobaapzxt","xqkrqiowhqtmvktkzw","xtxazeffclcexzmeaycjjmajshv","zxmieefjwihlw","wzhicdsciqcsn","njhka","hgoesyvhlqgrzzkbmkx","hhqxqffxxfv","npndzhkyctu","dbptzbbzisaripjffjllwygwpzrxjf","ccdagum","ukethqmdefjny","tfnzkpzqjeveuzynauprcqtsuyafz","wrjbfwkerzwg","iqapcatbmjv","mtmxmvemslsoikkpforhecawjpthbs","fsgeiqyzkotqwovwmsgoufkom","knxnrmqxzgzxrxbmvjijmegmqs","govqvxxqkvgq","xvoitdqnxslptrzbbbgvvond","fqotzrbknkunufganocgvddcpg","qktnvhyqzrfekbcgknpndoethl","lsfgbkwguheafpaxffhfxbpr","himzsnjhxhxaersjleptlehia","gahnnjgqcuhhrkbhraenlplss","fluupktpkkqomozjbtebccjaxoogx","gyhywm","dztilrjzzhwmmlybfpmegrxnefhu","rjmcgz","hqqumsnbcawjmfbcwprjzod","jbodoxiqetkknul","tfvllzrgoqgticq"]

    timeStamp1 = time.time()
    print(s.findRestaurant(list1,list2))
    timeStamp2 = time.time()
    print(s.findRestaurant2(list1,list2))
    timeStamp3 = time.time()
    print(s.findRestaurantForce(list1,list2))
    timeStamp4 = time.time()
    print(timeStamp2-timeStamp1)
    print(timeStamp3-timeStamp2)
    print(timeStamp4-timeStamp3)

if __name__ == '__main__':
    main()
