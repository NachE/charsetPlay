#!/usr/bin/env python

##############################################################################
#
#    CharsetPlay
#    Copyright (C) 2013 Juan Antonio Nache <ja@nache.net>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
############################################################################

# References and DOC used for this code:
#
# https://www.iana.org/assignments/character-sets/character-sets.xhtml
#
# Also, alias dictionary is the result of print alias dict from chalias.py

import sys

alias={'cp1258': 'windows-1258', 'utf8': 'UTF-8', 'chinese': 'GB2312', 'x-mac-ce': 'x-mac-ce', 'cp-866': 'IBM866', 'iso-10646': 'UTF-16BE', 'x-cp1257': 'windows-1257', 'latin6': 'ISO-8859-10', 'x-mac-farsi': 'x-mac-farsi', 'gb_2312-80': 'GB2312', 'iso88598': 'ISO-8859-8', 'iso_8859-15': 'ISO-8859-15', 'koi8': 'KOI8-R', 'x-mac-ukrainian': 'x-mac-cyrillic', 'utf-16le': 'UTF-16LE', 'csibm857': 'IBM857', 'csibm855': 'IBM855', 'utf-16': 'UTF-16', 'iso-8859-8i': 'ISO-8859-8-I', 'csibm850': 'IBM850', 'csibm866': 'IBM866', 'cseucpkdfmtjapanese': 'EUC-JP', 'csiso103t618bit': 'T.61-8bit', 'shift-jis': 'Shift_JIS', 'l4': 'ISO-8859-4', 'x-mac-arabic': 'x-mac-arabic', 'asmo-708': 'ISO-8859-6', 'iso885915': 'ISO-8859-15', 'csiso88598i': 'ISO-8859-8-I', 'x-mac-romanian': 'x-mac-romanian', 'csiso88598e': 'ISO-8859-8-E', 'euc-kr': 'EUC-KR', 'ksc5601': 'EUC-KR', 'iso-2022-jp-2': 'ISO-2022-JP', 'cp1257': 'windows-1257', 'ibm-864': 'IBM864', 'iso88595': 'ISO-8859-5', 'windows-936': 'gbk', 'csibm862': 'IBM862', 'tis620': 'TIS-620', 'x-viet-tcvn5712': 'x-viet-tcvn5712', 'iso_8859-7:1987': 'ISO-8859-7', 'iso8859-11': 'ISO-8859-11', 'us-ascii': 'us-ascii', 'iso8859-10': 'ISO-8859-10', 'armscii-8': 'armscii-8', 'iso885913': 'ISO-8859-13', 'iso_8859-8:1988': 'ISO-8859-8', 'csunicodelatin1': 'UTF-16BE', 'viscii': 'VISCII', 'cp1256': 'windows-1256', 'csiso88596i': 'ISO-8859-6-I', 'ibm857': 'IBM857', 'csisolatinarabic': 'ISO-8859-6', 'ibm855': 'IBM855', 'l5': 'ISO-8859-9', 'ansi_x3.4-1968': 'us-ascii', 'ibm852': 'IBM852', 'ibm850': 'IBM850', 'cp1254': 'windows-1254', 'iso-ir-138': 'ISO-8859-8', 'csunicode': 'UTF-16BE', 'iso885910': 'ISO-8859-10', 'csksc56011987': 'EUC-KR', 'csiso2022jp2': 'ISO-2022-JP', '862': 'IBM862', 'x-mac-turkish': 'x-mac-turkish', 'sjis': 'Shift_JIS', 'gbk': 'gbk', 'cp932': 'Shift_JIS', 'iso-10646-ucs-2': 'UTF-16BE', '5601': 'EUC-KR', 'unicode-2-0-utf-7': 'UTF-7', 'csisolatin1': 'ISO-8859-1', 'csisolatin2': 'ISO-8859-2', 'iso-ir-111': 'ISO-IR-111', 'csisolatin4': 'ISO-8859-4', 'csisolatin5': 'ISO-8859-9', 'csisolatin6': 'ISO-8859-10', 'zh_tw-euc': 'x-euc-tw', 'l6': 'ISO-8859-10', 'csiso2022kr': 'ISO-2022-KR', '866': 'IBM866', 'x-mac-devanagari': 'x-mac-devanagari', 'cns11643': 'x-euc-tw', 'csiso111ecmacyrillic': 'ISO-IR-111', 'csibm864': 'IBM864', 'x-sjis': 'Shift_JIS', 'ibm819': 'ISO-8859-1', 'korean': 'EUC-KR', 'iso-2022-jp': 'ISO-2022-JP', 'x-user-defined': 'x-user-defined', 'utf-16be': 'UTF-16BE', 'iso885914': 'ISO-8859-14', 'x-mac-croatian': 'x-mac-croatian', 'ecma-114': 'ISO-8859-6', 'cn-big5': 'Big5', 'l2': 'ISO-8859-2', 'csunicodeascii': 'UTF-16BE', 'ecma-118': 'ISO-8859-7', 'cskoi8r': 'KOI8-R', 'x-mac-hebrew': 'x-mac-hebrew', 'l3': 'ISO-8859-3', 'ecma-cyrillic': 'ISO-IR-111', 'x-cp1251': 'windows-1251', 'iso-10646-j-1': 'UTF-16BE', 'csiso58gb231280': 'GB2312', 'l1': 'ISO-8859-1', 'cp862': 'IBM862', 'iso-ir-109': 'ISO-8859-3', 'x-viet-vps': 'x-viet-vps', 'unicode-1-1-utf-7': 'UTF-7', 'x-unicode-2-0-utf-7': 'UTF-7', 'x-gbk': 'gbk', 'x-euc-jp': 'EUC-JP', 'iso-ir-101': 'ISO-8859-2', 'iso-ir-100': 'ISO-8859-1', 'iso-ir-103': 'T.61-8bit', 'x-imap4-modified-utf7': 'x-imap4-modified-utf7', 'csibm852': 'IBM852', 'x-euc-tw': 'x-euc-tw', 'iso8859-2': 'ISO-8859-2', 'iso8859-1': 'ISO-8859-1', 'iso8859-7': 'ISO-8859-7', 'iso8859-6': 'ISO-8859-6', 'iso8859-5': 'ISO-8859-5', 'iso8859-4': 'ISO-8859-4', 'koi8-u': 'KOI8-U', 'iso8859-9': 'ISO-8859-9', 'iso8859-8': 'ISO-8859-8', 'gb2312': 'GB2312', 'koi8-r': 'KOI8-R', 'ms_kanji': 'Shift_JIS', 'cp850': 'IBM850', 'shift_jis': 'Shift_JIS', 'iso_8859-2:1987': 'ISO-8859-2', 'cp855': 'IBM855', 'csshiftjis': 'Shift_JIS', '646': 'us-ascii', 'cp1251': 'windows-1251', 'l9': 'ISO-8859-15', 'windows-949': 'EUC-KR', 'macintosh': 'macintosh', 'dos-874': 'windows-874', 'csisolatinhebrew': 'ISO-8859-8', 'iso88599': 'ISO-8859-9', 'x-x-big5': 'Big5', 'cp1253': 'windows-1253', 'iso88593': 'ISO-8859-3', 'iso88592': 'ISO-8859-2', 'iso88591': 'ISO-8859-1', 'iso-8859-10': 'ISO-8859-10', 'iso88597': 'ISO-8859-7', 'iso_8859-7': 'ISO-8859-7', 'logical': 'ISO-8859-8-I', 'iso88594': 'ISO-8859-4', 'csgb2312': 'GB2312', 'csisolatin3': 'ISO-8859-3', 'x-mac-roman': 'macintosh', 'iso-10646-unicode-latin1': 'UTF-16BE', 'cp819': 'ISO-8859-1', 'elot_928': 'ISO-8859-7', 'iso-2022-cn': 'ISO-2022-CN', 'iso-2022-kr': 'ISO-2022-KR', 'koi': 'KOI8-R', '855': 'IBM855', '857': 'IBM857', '850': 'IBM850', 'latin4': 'ISO-8859-4', '852': 'IBM852', 'gb_2312': 'GB2312', 'iso_8859-3:1988': 'ISO-8859-3', 'iso_8859-9:1989': 'ISO-8859-9', 'x-johab': 'x-johab', 'csmacintosh': 'macintosh', 'x-iso-10646-ucs-2-le': 'UTF-16LE', 'ibm874': 'windows-874', 'iso_8859-1:1987': 'ISO-8859-1', 'csunicode11utf7': 'UTF-7', 'x-cp1256': 'windows-1256', 'iso8859-3': 'ISO-8859-3', 'x-cp1254': 'windows-1254', 'x-cp1255': 'windows-1255', 'x-cp1252': 'windows-1252', 'x-cp1253': 'windows-1253', 'x-mac-cyrillic': 'x-mac-cyrillic', 'iso_8859-6:1987': 'ISO-8859-6', 'ibm866': 'IBM866', 'ibm864': 'IBM864', 'ibm862': 'IBM862', 'greek8': 'ISO-8859-7', 'x-cp1258': 'windows-1258', 'visual': 'ISO-8859-8', 'iso-ir-127': 'ISO-8859-6', 'iso-ir-126': 'ISO-8859-7', 'windows-1258': 'windows-1258', 'windows-1256': 'windows-1256', 'windows-1257': 'windows-1257', 'windows-1254': 'windows-1254', 'windows-1255': 'windows-1255', 'windows-1252': 'windows-1252', 'windows-1253': 'windows-1253', 'windows-1250': 'windows-1250', 'windows-1251': 'windows-1251', 'iso_8859-5:1988': 'ISO-8859-5', 'csunicode11': 'UTF-16BE', 'ks_c_5601-1987': 'EUC-KR', 'csviscii': 'VISCII', '864': 'IBM864', 'csiso88596e': 'ISO-8859-6-E', 'ks_c_5601-1989': 'EUC-KR', 'iso_8859-4:1988': 'ISO-8859-4', 'big5': 'Big5', 'iso-2022-cn-ext': 'ISO-2022-CN', 'x-mac-greek': 'x-mac-greek', 'unicode-1-1-utf-8': 'UTF-8', 'zh_tw-big5': 'Big5', 'windows-31j': 'Shift_JIS', 'iso_8859-5': 'ISO-8859-5', 'iso_8859-4': 'ISO-8859-4', 'gb18030': 'gb18030', 'iso_8859-6': 'ISO-8859-6', 'iso_8859-1': 'ISO-8859-1', 'iso_8859-3': 'ISO-8859-3', 'iso_8859-2': 'ISO-8859-2', 'tis-620': 'TIS-620', 'zh_cn.euc': 'GB2312', 'euc-jp': 'EUC-JP', 'hebrew': 'ISO-8859-8', 'iso_8859-9': 'ISO-8859-9', 'iso_8859-8': 'ISO-8859-8', 'iso-ir-157': 'ISO-8859-10', 't.61-8bit': 'T.61-8bit', 't.61': 'T.61-8bit', 'hz-gb-2312': 'HZ-GB-2312', 'ksc_5601': 'EUC-KR', 'arabic': 'ISO-8859-6', 'ascii': 'us-ascii', 'iso-ir-110': 'ISO-8859-4', 'cp866': 'IBM866', 'iso-ir-144': 'ISO-8859-5', 'x-iso-10646-ucs-2-be': 'UTF-16BE', 'iso88596': 'ISO-8859-6', 'x-cp1250': 'windows-1250', 'iso-8859-9': 'ISO-8859-9', 'iso-8859-8': 'ISO-8859-8', 'iso-8859-7': 'ISO-8859-7', 'iso-8859-6': 'ISO-8859-6', 'iso-8859-5': 'ISO-8859-5', 'iso-8859-4': 'ISO-8859-4', 'iso-8859-3': 'ISO-8859-3', 'iso-8859-2': 'ISO-8859-2', 'iso-8859-1': 'ISO-8859-1', 'big5-hkscs': 'Big5-HKSCS', 'cp852': 'IBM852', 'x-mac-gujarati': 'x-mac-gujarati', 'utf-8': 'UTF-8', 'iso8859-13': 'ISO-8859-13', 'utf-7': 'UTF-7', 'latin1': 'ISO-8859-1', 'cp864': 'IBM864', 'iso885912': 'ISO-8859-12', 'iso8859-15': 'ISO-8859-15', 'iso8859-14': 'ISO-8859-14', 'windows-874': 'windows-874', 'cp857': 'IBM857', 'csisolatingreek': 'ISO-8859-7', 'sun_eu_greek': 'ISO-8859-7', 'iso885911': 'ISO-8859-11', 'csisolatincyrillic': 'ISO-8859-5', 'cp1255': 'windows-1255', 'iso-8859-16': 'ISO-8859-16', 'iso-8859-15': 'ISO-8859-15', 'iso-8859-14': 'ISO-8859-14', 'iso-8859-13': 'ISO-8859-13', 'cp1250': 'windows-1250', 'iso-8859-11': 'ISO-8859-11', 'iso-8859-8-e': 'ISO-8859-8-E', 'iso-8859-8-i': 'ISO-8859-8-I', 'iso-ir-149': 'EUC-KR', 'iso-ir-148': 'ISO-8859-9', 'csiso2022jp': 'ISO-2022-JP', 'x-mac-icelandic': 'x-mac-icelandic', 'latin5': 'ISO-8859-9', 'mac': 'macintosh', 'csbig5': 'Big5', 'iso-8859-6-e': 'ISO-8859-6-E', 'latin2': 'ISO-8859-2', 'latin3': 'ISO-8859-3', 'csisolatin9': 'ISO-8859-15', 'iso-8859-6-i': 'ISO-8859-6-I', 'cyrillic': 'ISO-8859-5', 'iso-ir-58': 'GB2312', 'iso-10646-ucs-basic': 'UTF-16BE', 'x-mac-gurmukhi': 'x-mac-gurmukhi', 'koi8_r': 'KOI8-R', 'greek': 'ISO-8859-7', 'cseuckr': 'EUC-KR', 'ansi-1251': 'windows-1251', 'cp1252': 'windows-1252'}

RAW=1
UTF8=0

def get_table(charset,mode=RAW):
	r = []
	for x in range(0,256):
		try:
			if mode == RAW:
				r.append( ('%c' % x).encode(charset, errors='strict') )
			elif mode == UTF8:
				r.append( ('%c' % x).decode(charset, errors='strict') )
		except UnicodeDecodeError, e:
			r.append( None )
		except UnicodeEncodeError, e:
			r.append( None )
		except LookupError, e:
			r.append( None )
	if len(r) > 0:
		return r
	else:
		return None

def print_table(charset, mode=RAW):
	table = get_table(charset, mode)
	i=0
	for value in table:
		try:
			if mode == RAW:
				sys.stdout.write(' '+str(i)+':')
				sys.stdout.write(value)
			elif mode == UTF8:
				sys.stdout.write(' '+str(i)+':')
				sys.stdout.write(value.encode('utf8', errors='ignore'))
		except AttributeError:
			pass
		i=i+1

def get_all(mode=RAW):
	r = []
	for key, value in alias.iteritems():
		r.extend(get_table(value, mode))
	return r

def print_all(mode=RAW):
	for key, value in alias.iteritems():
		print ("\n\n***** %s ******" % value)
		print_table(value, mode)

