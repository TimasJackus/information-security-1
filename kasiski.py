MAX_KEY_LENGTH_GUESS = 20
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Returns the Index of Councidence for the "section" of ciphertext given
def get_index_c(ciphertext):

	N = float(len(ciphertext))
	frequency_sum = 0.0

	# Using Index of Coincidence formula
	for letter in alphabet:
		frequency_sum+= ciphertext.count(letter) * (ciphertext.count(letter)-1)

	# Using Index of Coincidence formula
	ic = frequency_sum/(N*(N-1))
	return ic

# Returns the key length with the highest average Index of Coincidence
def get_key_length(ciphertext):
	ic_table=[]

	# Splits the ciphertext into sequences based on the guessed key length from 0 until the max key length guess (20)
	# Ex. guessing a key length of 2 splits the "12345678" into "1357" and "2468"
	# This procedure of breaking ciphertext into sequences and sorting it by the Index of Coincidence
	# The guessed key length with the highest IC is the most porbable key length
	for guess_len in range(MAX_KEY_LENGTH_GUESS):
		ic_sum=0.0
		avg_ic=0.0
		# print(guess_len)
		for i in range(guess_len):
			sequence=""
			# breaks the ciphertext into sequences
			for j in range(0, len(ciphertext[i:]), guess_len):
				sequence += ciphertext[i+j]
			ic_sum+=get_index_c(sequence)
		# obviously don't want to divide by zero
		if not guess_len==0:
			avg_ic=ic_sum/guess_len
		ic_table.append(avg_ic)

	# returns the index of the highest Index of Coincidence (most probable key length)
	best_guess = ic_table.index(sorted(ic_table, reverse = True)[0])
	second_best_guess = ic_table.index(sorted(ic_table, reverse = True)[1])
	print(best_guess, second_best_guess)

	# Since this program can sometimes think that a key is literally twice itself, or three times itself,
	# it's best to return the smaller amount.
	# Ex. the actual key is "dog", but the program thinks the key is "dogdog" or "dogdogdog"
	# (The reason for this error is that the frequency distribution for the key "dog" vs "dogdog" would be nearly identical)
	if best_guess % second_best_guess == 0:
		return second_best_guess
	else:
		return best_guess

def main():
  ciphertext_unfiltered = """Lp hry e hhnfvxxdb nolih vrkr cdow d loiolgoa, prdrlhz gizif, zety v wzljy pzpdrs bivwk njos dr lka eovgl pedugi. Lka dfjv gsanvy sf wk a kpfw-vdagzh zdhl cdow d pueiid: d reit ggpboioetoa tlirwo sikcsmw omffi, olph gvrwoheu redoo, aey jdrkrj omdhz aey gsulekzh, hukvzyiv zety ksdlohvy gzderj, vrv oktj vrv oktj jj hhcs wjv zdps rih urwtj - olw kkbsdx odo ffih gi rijdxguo. Tyz xmqjec rsmqz oe vrv rj, gfdry iwiigc txp nfo umlpe jovslchk drlr phv nmvh kf kci zlhl - Kci Zlhl, rn edo phv kigshe wjv edjy ddpwv nolih udhlvy ml - djd dvrq oetkgi jrqnu ysguo ogzrwg kuk jj aw, biinx gq knv nmvh wnu olwq kn rislkar. Ej kgljg lkwlderj asj wde yjftlp: bvyvgris, svxzukodn, gwohain, tsqprzzw (drps fa xzhoe), nvvvukbvn (lw kwd ncsdh nofhw vhrokzh lr ylfolwv), gikxlwqo, dzimfj-nofhw, soh wvmi gq phv neeh blfjv, sqz ieyiwg kn kci kdie gvwkdce. Kci thot ijsev seiz edo kn kci dhbt-yvrv vedv (bsaqc ie), asj wdejz awua tyz sfou oezw lr damz aaqzonn, hwhl-svo vgxjd ndrvrss cjscljg fqij kes xvvvhj aey qwdzonn fwbknu, npgsenx ysoq po kci jlrei.
Olav doswml zws r qijb secg-xg-gk hfwfaw, wnu cmk qwmv rek Ewgxdrk. Wde Svkyljsvn lsg himzh aq phv iiajdbfpvzrkd fa Xzh Dicg jgu pidz smw kf ddrv, djd gzshoa cfiwagarvy xzhi vvmc jhopvxxsehe, ejx gqhy szgsxoe djwl rb tyzq ohne idgz, eqt rgwg eacrpww wdep iinhn hry efb wdmzrlxnej jv vlz aetxzljg liipsackzh: qrq cfppv walc rlsw w Brbkaqo wfppv vwy fi efb muvnxarj wzolgxp tyz fgwdei jj svgieb lap. Phzn mk d otfmc gi don v Fsjcien lsg wn ryzwqpuiz, jgxjd ydqkhhf ujmfj wnu neqljg kcmfjo acosyhphvm yfhtpvxxwg. De dvc zdre cjwl wde ezmykxolmw' jhopvxx, txp hv beaqad-nzpd, bku ndpd vae ncilkar yz ksljeu vrqwdieb mf wde vih.
Lka mfolwu kf fpv hdntzxyddn hfwfaw … shro mk d doswml? L ougkskh doswmlv jevy wgpa dvngjlltzjr frsauvck, ventz xzhu hrqi thyodz vsua aey wzb kf kci Tlc Pvjtdh, ws kciq fwlc pw. Lkay rmi (gu seiz) e dlptcz twrllv, vfgxp hrgj gxn hvdkzw, wnu nqsohei olsq phv wisuzeu Yasurej. Csteetj cenh jo szejgo. Tyzvw lo lzoxdh kr ej qsjec rwsmw phvh, ipfapk olw rndziejb avvmcvdu sfmx okecy cidso tyzq lr zijvthhwr hpmwwhy rih ixecbgc okan cvvyh otlkmv iklb gmch uol vrv pa cfhi toqnuzvaqc acjry, pwkzik s qkijz pana ecztzdjtj rlafd tyzc udj hvvv s pelv jjx. Wdep vvw ljccdrwg po sz el lj tyz wlriatc; xzhu dizwk lj bidkzw yocjyjv (yhzzjdb crvzr sqz yvgpgz); serm rg vdovn, fwfwujz xzher wzil jnon ielxnac giswdeit wgoas rih lkecb rejp xrfrr zder cdow wde joyxi kn kciau deryw (okecy dw uxnlp); cenh hoeb gdhrei wvgzj fzikwuo, gfjh-fdpuizh xdyej, vrv owuxc hwhl fipmlb halblk (hopvxmsohy raxwu zieiij, zditc xzhu hrqi lzecv v hsb shvi xzhu cri kww et). Eja qrq keja wqkuxc xg jk oe rmlk. Ws Z rek vwyzik, lka mfolwu kf kcmk kkbsdx - gi Xicws Tdcgziw, lkwt zn - asv phv aetxholn Fwohaujrfd Poff, sfh kf kci lknev miednkrwpw gwuxcxwuo ow olw Rhd Kjsc, kaau jj lka hfwfawo wyj payad rxvgvo Tyz Aswar, kci kpwlc mmnhn tyvx jdj ak olw ikok jj Lka Hzgp. Aw saj jjlhj srdh (aq ktyzv xdiicdik) wdak gsfj wgf jrw rb tyz Xgrg aexikwkrj hykw damz xsnan r aeauu wzai. Lkwt nvw, gi yolmww, dxslmh, txp cvmxsljlp olwua wrn wllhl jjqwwdieb rgw ankdvwou hfwfaw-hibz etrqt kcie, - djd figw lj a ncmdh iedwijv kf kci Lrkk-tgef zkucy kg djd yvzw dzvvixmuas. Kciq gestmiwwhy udwsslermiv, djd kci xdiict lmvdeu dx ms; xuk olw iwck miedenvy xzdp tyz Xgrgs nzvw qkt rn vwvletoetoa aj olw Ewgxdrkho, tyjyyk phvt awua ueysmepeugc jlyhvm. Rgw phro Fwohaujrfd Poff inhn hry efb wdmzrlxnej vjlhn syz fwfwmv Hvk. Eqnxj Fsjcien. Fmqco, kcel zws Sdptr'o frolwu, xuzgx lka mfnx dxtuidsmv doswml-kklv asj kar (rih hdntct aawd hvm qgqay) kcel zws kj fw ikuey iawdei prvhn Tyz Laoh oi jzwu Phv Cmdo kr rxvgvo Tyz Aswar, rih lkarv olwb nedvmfhz tf olw hjd fa xzher uvck. Vpicg ml lo pijfsehe kcel Eelsj, lwu knct wgq, wlkcsmjd hv gsgnad rih thdamzh wawckgc dlge r niurjd vymllkn fa lav oocdh sqz cfhjgupasgi xdphvm, kgw oodzxzljg r wml tqevm mf kes dvowxl fijq lka Tfjo klze, jjqwwdieb xzdp oegc odetvy jgu w cyvruh po tjqw rqt. Kci ukwntz rwyar rmvayad, lixao Xicws Tdcgziw odo gijaf xl, bvdry dxolo jaipy pzejv klu jv kr, wnu gmnljg zi xzh xerpxaiql yjftlp-hfgi txelk wc zlo frolwu, shzxl A kwvv eykw zejxvaead wjv qrq, ueomd ka hry mf iwck vthdneeopq vatkgiv gkwe dqerrasgc.
Tb oodz gmueoln gzdjcv jrw pkredry oknx vkg lj tyz umlat fa xzh soigh, okan kcijh saj gikv jozni sqz mfmi yuaee, vrv wde yjftlps nzvw vpicg rmparfpw sqz pijwhhnoln, efg Xicws Tdcgziw odo skvrvljg ro lav zofm exwar smisnbajo wergieb ef hjoihsmv hoeb agrzee kmhh phro vwdyhvy rwdnlp ysoq po ydw orklct xgho (nvvxdb xrlnlwg) - Caeyedi yadz fq. Jwnuvpx! Lb yfp lsg dermh gqhy r lysupei jj okwt Z cenh dermh sekuk cme, djd Z cenh knct lwdnd mzvq oetkgi gi wlc olwua ij os zhwr, pjy orqlu wi huaprmiv ikr ric krnt Z jj jhiaifetoa trgi. Ldhej vrv dzvvixmuas jkvgxpeu pt soh omzv lka pcvgw zdeizzwu de nzrl, lj tyz qgvp eoovsrndziejb bajcmgq. De yvh frp bvzr vrsn kcel zwy lihwu Phv Cmdo boi vkwv wnu vkwv, jok nmffa hzn jjlanu olw Rhd Kjsc geeu, dr xdyt, rih lka hfwfawo hry edpksk asjjktkzr okwt yz pgrgeu gmch. De yvh than rreq rrei Olw Kelc vrv dyrfnw Lka Wroij rj blnmfhos fa lav kwe nmffa tyzc ohne rgp kpwlc csteet-sjck djd yjftlp-gzmpk."""

  # Filters the text so it is only alphanumeric characters, and lowercase
  ciphertext = ''.join(x.lower() for x in ciphertext_unfiltered if x.isalpha())
  key_length=get_key_length(ciphertext)
  print(key_length)
  print("Key length is most likely {}".format(key_length))

if __name__ == '__main__':
	main()