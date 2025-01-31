# -*-coding:utf-8-*-
# @ auth ivan
# @ time 2021-02-09
# @ goal 105.Test_LevenshteinDistance,

import Levenshtein

s1, s2 = "ABCD", "ACE"
print(
	Levenshtein.distance(s1, s2), 	
	Levenshtein.distance(s2, s1),
	Levenshtein.editops(s1, s2),
	Levenshtein.ratio(s1, s2), 
	Levenshtein.jaro(s1, s2),
	Levenshtein.jaro_winkler(s1, s2)
)

# s1, s2 = "广东省广州市番禺区luoxi海bin花园A座1房", "广州洛溪海滨花园A座1房"

