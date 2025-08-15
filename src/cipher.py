"""def xor_cipher(text, key):
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))

password = "+'oqEDDw,K<yA8Tys0]7Yct5+~y4ngLz86K<)`,h4'-U,Q|)r$\$,Yjh;6l]VgLP4PZ1Gm]jgra|GYH%Yq4xj?#{:qT9}m"I;(M2G~jmJG#,^t1oT{lh$V#\Kp^5V3zvj3ki:gR%J7W*hDS{F#P{)7p3V{9Qp:2<}nS+]I>XHLWfA&Sv-gzqJ/~Z*:C}ZeSv:>L{}zoK}BJ>QlNoa{@+/Or2{>*{x=e,u'`IjF!8&42h9|rb$n11ha>~)_Ka3"PPQflPfH2eIvCDHmhPR1to#*F%72=o+3I's1{1L>:zCU?x1DuV@{pe(LRetVP&Ed]JJS&xsj\JOh+?=3c7za/7SRBi#8V%m2_b"Eluj}<t*+M($[2%Pk|=kb{2hkRw@2&ArP:I+D^MpYg`*PXh0h5xF)osj',P#U3Z=It]M']g<U$;?8*\Ot6&aHyyjfEyn[b8Qc2N-~$4IYKJ)qvp[Wr2[t3L/?lVWvY^u?)S8"a9PB3tL6E$*hpi[zPj;U37*xR*tU'Qw^%h}{[WGdcCP+djSQr?F^"Be)Kl%A5!|V1xREEy-&pYbD2&V&|&Oz;H#n58*,Zpj_)|S+39SwOOmQg*~T3&4#+"2,\fOx/aVv^sQfe,w&z2`q+'I1g/IOR\~F*EOt6~r6gy#>yN~E&352-X|;/;'rx^(PR1e}(B928]6"F:@b8B{U5C=PQ$o4xQW@['zkrB6<i;0{laaZ@BScR>mK@~s$_vP{L/B:!;Kuk=Ex:n&ol~S.uew|<HOEXglo"LE/Z&hh@%/I9hU*is\&I;gn5f_8r0C{[1\piy6KF\4herc"^%r;fOU]np3Fcx0TAX3I2gSR[1md[iR?NPf:(CJue%_0?6IEC@Y.3%|UyfhBrY1k)3d^XzP<6Iwf<|u@D(XEc]kJ\-EixX'wO}r`0(N*d($##G+SP<S=mmBBU9+7av-BxHXT$+'HlPp5J)weIG4~.XX"U?S8dUUZJECX\9FKkE"rO5$kLguuwoyuAw"
key = "*hD}b96~K#Q0J9zK7Q]_/?Z&4\|UV5nvxR7>cM4C_.=([PWhW*A!n@kyee,-uj(1+E+PSVJfeDk{{G4rBFGejTF!F=t`S-rzIk,2FM$1@l^d2e6)Qmu&bXn[UftYAo-4Jm)\g=jcBO(U^uRHj^PYrT@9i-lf/E_2rcDglvI-;T"3h[eUq"r7,(BqB&DqzfAJYx?~sGi<:%R7[xsgoKQ?`/{3m/c"GjK*?6bq^3'(bMugBHl[8CNqruamh]K>O"&,1mt9n<T5g$}0M~woj#L>?XKuOHTCeS`"]C3E-;Ktq1HpC.p><cvrIYwR-p19r'sF-M<<zq1t}_rFk[Gp~g-r#%^(R;)0]u2??Y\E-j]AR;*3"-I>vl~gvNvH_-1"KTOJ?n;GgV&irj_0[zHiLuhM72x0`lab1.[_R8;vY>%x#FFwp*GB\.q[!3f]9NuaK.(7o^p{@{*L2A65-w`7o]*ax/Te'ni%)\)W`TFldRlJ^Sq"Z"sp?Gvp+@`1;(+7#A44is4tP}Qt^KL5^bq5h"thD2?%mJa(QZ'},FxHmmwUUmtK)?U$Y3O-DwQ^{r*fXNvA~O6H[ulb'9bqz&?}-Nu#[ts#'W!-`Yhx]3>fHFP%_Zv0)mUP\dM,FE1'4!JosMR~_R32IwA*F4Y`XWS)2lMtp_[iN+<K<?,uqbMeHjD>2@?rC3O6-mycXQyjuOEe~Je[|+?t|<4c(zBit+w'tP2yxPMU+)Ul)"~TUxm%>g1(|7*MQ!5B#JK$CJx+)t9^ad1SQBYB=<U>m<gO8dH^l\a1HluS6}Z|t0%oUk(3T':7r0D-L,|[9N'GT'H@!+y/CGL%Dty[{?5EL<b;qH\i5zoCJb4|r|]SDiOA\Fr((Y%|P3b3lQ/*jX`ebXw[2Fqyb2t{H(&maeR.sao%~{;H5*(N0E:$KkzTOq4(&izIP1}K9Cc"Rt~gdKVR+]i_*GkM+FIMDr`IFP-6c^1lUjkagjM;~]v]zsw$'a}DG`dnG{2!"
ciphered = xor_cipher(password, key)
print([ord(c) for c in ciphered])  # store this list in Custom Instructions
"""

import secrets
import string

# Use all printable ASCII characters for maximum complexity
characters = string.ascii_letters + string.digits + string.punctuation

# Generate a 1000-character password
password = ''.join(secrets.choice(characters) for _ in range(1000))

# Generate a 1000-character secret key
secret_key = ''.join(secrets.choice(characters) for _ in range(1000))

print("Password:", password)
print("Secret Key:", secret_key)
