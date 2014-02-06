#!/usr/bin/env python
#
# Extracted and modified from:
# https://mxr.mozilla.org/mozilla-central/source/intl/locale/src/charsetalias.properties
# Wich have this license:

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# This Original Code has been modified by IBM Corporation.
# Modifications made by IBM described herein are
# Copyright (c) International Business Machines
# Corporation, 1999
#
# Modifications to Mozilla code or documentation
# identified per MPL Section 3.3
#
# Date         Modified by     Description of modification
# 12/09/1999   IBM Corp.       Support for IBM codepages - 850,852,855,857,862,864
#
# Rule of this file:
# 1. key should always be in lower case ascii so we can do case insensitive
#    comparison in the code faster.
# 2. value should be the one used in unicode converter
#
# 3. If the charset is not used for document charset, but font charset
#    (e.g. XLFD charset- such as JIS x0201, JIS x0208), don't put here
#

alias={}
alias['ascii']='us-ascii'
alias['us-ascii']='us-ascii'
alias['ansi_x3.4-1968']='us-ascii'
alias['646']='us-ascii'
alias['iso-8859-1']='ISO-8859-1'
alias['iso-8859-2']='ISO-8859-2'
alias['iso-8859-3']='ISO-8859-3'
alias['iso-8859-4']='ISO-8859-4'
alias['iso-8859-5']='ISO-8859-5'
alias['iso-8859-6']='ISO-8859-6'
alias['iso-8859-6-i']='ISO-8859-6-I'
alias['iso-8859-6-e']='ISO-8859-6-E'
alias['iso-8859-7']='ISO-8859-7'
alias['iso-8859-8']='ISO-8859-8'
alias['iso-8859-8-i']='ISO-8859-8-I'
alias['iso-8859-8-e']='ISO-8859-8-E'
alias['iso-8859-9']='ISO-8859-9'
alias['iso-8859-10']='ISO-8859-10'
alias['iso-8859-11']='ISO-8859-11'
alias['iso-8859-13']='ISO-8859-13'
alias['iso-8859-14']='ISO-8859-14'
alias['iso-8859-15']='ISO-8859-15'
alias['iso-8859-16']='ISO-8859-16'
alias['iso-ir-111']='ISO-IR-111'
alias['iso-2022-cn']='ISO-2022-CN'
alias['iso-2022-cn-ext']='ISO-2022-CN'
alias['iso-2022-kr']='ISO-2022-KR'
alias['iso-2022-jp']='ISO-2022-JP'
alias['utf-16be']='UTF-16BE'
alias['utf-16le']='UTF-16LE'
alias['utf-16']='UTF-16'
alias['windows-1250']='windows-1250'
alias['windows-1251']='windows-1251'
alias['windows-1252']='windows-1252'
alias['windows-1253']='windows-1253'
alias['windows-1254']='windows-1254'
alias['windows-1255']='windows-1255'
alias['windows-1256']='windows-1256'
alias['windows-1257']='windows-1257'
alias['windows-1258']='windows-1258'
alias['ibm866']='IBM866'
alias['ibm850']='IBM850'
alias['ibm852']='IBM852'
alias['ibm855']='IBM855'
alias['ibm857']='IBM857'
alias['ibm862']='IBM862'
alias['ibm864']='IBM864'
alias['utf-8']='UTF-8'
alias['utf-7']='UTF-7'
alias['shift_jis']='Shift_JIS'
alias['big5']='Big5'
alias['euc-jp']='EUC-JP'
alias['euc-kr']='EUC-KR'
alias['gb2312']='GB2312'
alias['gb18030']='gb18030'
alias['viscii']='VISCII'
alias['koi8-r']='KOI8-R'
alias['koi8_r']='KOI8-R'
alias['cskoi8r']='KOI8-R'
alias['koi']='KOI8-R'
alias['koi8']='KOI8-R'
alias['koi8-u']='KOI8-U'
alias['tis-620']='TIS-620'
alias['t.61-8bit']='T.61-8bit'
alias['hz-gb-2312']='HZ-GB-2312'
alias['big5-hkscs']='Big5-HKSCS'
alias['gbk']='gbk'
alias['cns11643']='x-euc-tw'
#
# Netscape private ...
#
alias['x-imap4-modified-utf7']='x-imap4-modified-utf7'
alias['x-euc-tw']='x-euc-tw'
alias['x-mac-ce']='x-mac-ce'
alias['x-mac-turkish']='x-mac-turkish'
alias['x-mac-greek']='x-mac-greek'
alias['x-mac-icelandic']='x-mac-icelandic'
alias['x-mac-croatian']='x-mac-croatian'
alias['x-mac-romanian']='x-mac-romanian'
alias['x-mac-cyrillic']='x-mac-cyrillic'
alias['x-mac-ukrainian']='x-mac-cyrillic'
alias['x-mac-hebrew']='x-mac-hebrew'
alias['x-mac-arabic']='x-mac-arabic'
alias['x-mac-farsi']='x-mac-farsi'
alias['x-mac-devanagari']='x-mac-devanagari'
alias['x-mac-gujarati']='x-mac-gujarati'
alias['x-mac-gurmukhi']='x-mac-gurmukhi'
alias['armscii-8']='armscii-8'
alias['x-viet-tcvn5712']='x-viet-tcvn5712'
alias['x-viet-vps']='x-viet-vps'
alias['iso-10646-ucs-2']='UTF-16BE'
alias['x-iso-10646-ucs-2-be']='UTF-16BE'
alias['x-iso-10646-ucs-2-le']='UTF-16LE'
alias['x-user-defined']='x-user-defined'
alias['x-johab']='x-johab'
#
# Aliases for ISO-8859-1
#
alias['latin1']='ISO-8859-1'
alias['iso_8859-1']='ISO-8859-1'
alias['iso8859-1']='ISO-8859-1'
alias['iso8859-2']='ISO-8859-2'
alias['iso8859-3']='ISO-8859-3'
alias['iso8859-4']='ISO-8859-4'
alias['iso8859-5']='ISO-8859-5'
alias['iso8859-6']='ISO-8859-6'
alias['iso8859-7']='ISO-8859-7'
alias['iso8859-8']='ISO-8859-8'
alias['iso8859-9']='ISO-8859-9'
alias['iso8859-10']='ISO-8859-10'
alias['iso8859-11']='ISO-8859-11'
alias['iso8859-13']='ISO-8859-13'
alias['iso8859-14']='ISO-8859-14'
alias['iso8859-15']='ISO-8859-15'
alias['iso_8859-1:1987']='ISO-8859-1'
alias['iso-ir-100']='ISO-8859-1'
alias['l1']='ISO-8859-1'
alias['ibm819']='ISO-8859-1'
alias['cp819']='ISO-8859-1'
alias['csisolatin1']='ISO-8859-1'
#
# Aliases for ISO-8859-2
#
alias['latin2']='ISO-8859-2'
alias['iso_8859-2']='ISO-8859-2'
alias['iso_8859-2:1987']='ISO-8859-2'
alias['iso-ir-101']='ISO-8859-2'
alias['l2']='ISO-8859-2'
alias['csisolatin2']='ISO-8859-2'
#
# Aliases for ISO-8859-3
#
alias['latin3']='ISO-8859-3'
alias['iso_8859-3']='ISO-8859-3'
alias['iso_8859-3:1988']='ISO-8859-3'
alias['iso-ir-109']='ISO-8859-3'
alias['l3']='ISO-8859-3'
alias['csisolatin3']='ISO-8859-3'
#
# Aliases for ISO-8859-4
#
alias['latin4']='ISO-8859-4'
alias['iso_8859-4']='ISO-8859-4'
alias['iso_8859-4:1988']='ISO-8859-4'
alias['iso-ir-110']='ISO-8859-4'
alias['l4']='ISO-8859-4'
alias['csisolatin4']='ISO-8859-4'
#
# Aliases for ISO-8859-5
#
alias['cyrillic']='ISO-8859-5'
alias['iso_8859-5']='ISO-8859-5'
alias['iso_8859-5:1988']='ISO-8859-5'
alias['iso-ir-144']='ISO-8859-5'
alias['csisolatincyrillic']='ISO-8859-5'
#
# Aliases for ISO-8859-6
#
alias['arabic']='ISO-8859-6'
alias['iso_8859-6']='ISO-8859-6'
alias['iso_8859-6:1987']='ISO-8859-6'
alias['iso-ir-127']='ISO-8859-6'
alias['ecma-114']='ISO-8859-6'
alias['asmo-708']='ISO-8859-6'
alias['csisolatinarabic']='ISO-8859-6'
#
# Aliases for ISO-8859-6-I
#
alias['csiso88596i']='ISO-8859-6-I'
#
# Aliases for ISO-8859-6-E
#
alias['csiso88596e']='ISO-8859-6-E'
#
# Aliases for ISO-8859-7
#
alias['greek']='ISO-8859-7'
alias['greek8']='ISO-8859-7'
alias['sun_eu_greek']='ISO-8859-7'
alias['iso_8859-7']='ISO-8859-7'
alias['iso_8859-7:1987']='ISO-8859-7'
alias['iso-ir-126']='ISO-8859-7'
alias['elot_928']='ISO-8859-7'
alias['ecma-118']='ISO-8859-7'
alias['csisolatingreek']='ISO-8859-7'
#
# Aliases for ISO-8859-8
#
alias['hebrew']='ISO-8859-8'
alias['iso_8859-8']='ISO-8859-8'
alias['visual']='ISO-8859-8'
alias['iso_8859-8:1988']='ISO-8859-8'
alias['iso-ir-138']='ISO-8859-8'
alias['csisolatinhebrew']='ISO-8859-8'
#
# Aliases for ISO-8859-8-I
#
alias['csiso88598i']='ISO-8859-8-I'
alias['iso-8859-8i']='ISO-8859-8-I'
alias['logical']='ISO-8859-8-I'
#
# Aliases for ISO-8859-8-E
#
alias['csiso88598e']='ISO-8859-8-E'
#
# Aliases for ISO-8859-9
#
alias['latin5']='ISO-8859-9'
alias['iso_8859-9']='ISO-8859-9'
alias['iso_8859-9:1989']='ISO-8859-9'
alias['iso-ir-148']='ISO-8859-9'
alias['l5']='ISO-8859-9'
alias['csisolatin5']='ISO-8859-9'
#
# Aliases for UTF-8
#
alias['unicode-1-1-utf-8']='UTF-8'
# nl_langinfo(CODESET) in HP/UX returns 'utf8' under UTF-8 locales
alias['utf8']='UTF-8'
#
# Aliases for Shift_JIS
#
alias['x-sjis']='Shift_JIS'
alias['shift-jis']='Shift_JIS'
alias['ms_kanji']='Shift_JIS'
alias['csshiftjis']='Shift_JIS'
alias['windows-31j']='Shift_JIS'
alias['cp932']='Shift_JIS'
alias['sjis']='Shift_JIS'
#
# Aliases for EUC_JP
#
alias['cseucpkdfmtjapanese']='EUC-JP'
alias['x-euc-jp']='EUC-JP'
#
# Aliases for ISO-2022-JP
#
alias['csiso2022jp']='ISO-2022-JP'
# The following are really not aliases ISO-2022-JP, but sharing the same decoder'
alias['iso-2022-jp-2']='ISO-2022-JP'
alias['csiso2022jp2']='ISO-2022-JP'
#
# Aliases for Big5
#
alias['csbig5']='Big5'
alias['cn-big5']='Big5'
# x-x-big5 is not really a alias for Big5, add it only for MS FrontPage
alias['x-x-big5']='Big5'
# Sun Solaris
alias['zh_tw-big5']='Big5'
#
# Aliases for EUC-KR
#
alias['cseuckr']='EUC-KR'
alias['ks_c_5601-1987']='EUC-KR'
alias['iso-ir-149']='EUC-KR'
alias['ks_c_5601-1989']='EUC-KR'
alias['ksc_5601']='EUC-KR'
alias['ksc5601']='EUC-KR'
alias['korean']='EUC-KR'
alias['csksc56011987']='EUC-KR'
alias['5601']='EUC-KR'
alias['windows-949']='EUC-KR'
#
# Aliases for GB2312
#
# The following are really not aliases GB2312, add them only for MS FrontPage
alias['gb_2312-80']='GB2312'
alias['iso-ir-58']='GB2312'
alias['chinese']='GB2312'
alias['csiso58gb231280']='GB2312'
alias['csgb2312']='GB2312'
alias['zh_cn.euc']='GB2312'
# Sun Solaris
alias['gb_2312']='GB2312'
#
# Aliases for windows-125x
#
alias['x-cp1250']='windows-1250'
alias['x-cp1251']='windows-1251'
alias['x-cp1252']='windows-1252'
alias['x-cp1253']='windows-1253'
alias['x-cp1254']='windows-1254'
alias['x-cp1255']='windows-1255'
alias['x-cp1256']='windows-1256'
alias['x-cp1257']='windows-1257'
alias['x-cp1258']='windows-1258'
#
# Aliases for windows-874
#
alias['windows-874']='windows-874'
alias['ibm874']='windows-874'
alias['dos-874']='windows-874'
#
# Aliases for macintosh
#
alias['macintosh']='macintosh'
alias['x-mac-roman']='macintosh'
alias['mac']='macintosh'
alias['csmacintosh']='macintosh'
#
# Aliases for IBM866
#
alias['cp866']='IBM866'
alias['cp-866']='IBM866'
alias['866']='IBM866'
alias['csibm866']='IBM866'
#
# Aliases for IBM850
#
alias['cp850']='IBM850'
alias['850']='IBM850'
alias['csibm850']='IBM850'
#
# Aliases for IBM852
#
alias['cp852']='IBM852'
alias['852']='IBM852'
alias['csibm852']='IBM852'
#
# Aliases for IBM855
#
alias['cp855']='IBM855'
alias['855']='IBM855'
alias['csibm855']='IBM855'
#
# Aliases for IBM857
#
alias['cp857']='IBM857'
alias['857']='IBM857'
alias['csibm857']='IBM857'
#
# Aliases for IBM862
#
alias['cp862']='IBM862'
alias['862']='IBM862'
alias['csibm862']='IBM862'
#
# Aliases for IBM864
#
alias['cp864']='IBM864'
alias['864']='IBM864'
alias['csibm864']='IBM864'
alias['ibm-864']='IBM864'
#
# Aliases for T.61-8bit
#
alias['t.61']='T.61-8bit'
alias['iso-ir-103']='T.61-8bit'
alias['csiso103t618bit']='T.61-8bit'
#
# Aliases for UTF-7
#
alias['x-unicode-2-0-utf-7']='UTF-7'
alias['unicode-2-0-utf-7']='UTF-7'
alias['unicode-1-1-utf-7']='UTF-7'
alias['csunicode11utf7']='UTF-7'
#
# Aliases for ISO-10646-UCS-2
#
alias['csunicode']='UTF-16BE'
alias['csunicode11']='UTF-16BE'
alias['iso-10646-ucs-basic']='UTF-16BE'
alias['csunicodeascii']='UTF-16BE'
alias['iso-10646-unicode-latin1']='UTF-16BE'
alias['csunicodelatin1']='UTF-16BE'
alias['iso-10646']='UTF-16BE'
alias['iso-10646-j-1']='UTF-16BE'
#
# Aliases for ISO-8859-10
#
alias['latin6']='ISO-8859-10'
alias['iso-ir-157']='ISO-8859-10'
alias['l6']='ISO-8859-10'
# Currently .properties cannot handle : in key
#alias['iso_8859-10:1992']='ISO-8859-10'
alias['csisolatin6']='ISO-8859-10'
#
# Aliases for ISO-8859-15
#
alias['iso_8859-15']='ISO-8859-15'
alias['csisolatin9']='ISO-8859-15'
alias['l9']='ISO-8859-15'
#
# Aliases for ISO-IR-111
#
alias['ecma-cyrillic']='ISO-IR-111'
alias['csiso111ecmacyrillic']='ISO-IR-111'
#
# Aliases for ISO-2022-KR
#
alias['csiso2022kr']='ISO-2022-KR'
#
# Aliases for VISCII
#
alias['csviscii']='VISCII'
#
# Aliases for x-euc-tw
#
alias['zh_tw-euc']='x-euc-tw'
#
# Following names appears in unix nl_langinfo(CODESET)
# They can be compiled as platform specific if necessary
# DONT put things here if it does not look generic enough (like hp15CN)
#
alias['iso88591']='ISO-8859-1'
alias['iso88592']='ISO-8859-2'
alias['iso88593']='ISO-8859-3'
alias['iso88594']='ISO-8859-4'
alias['iso88595']='ISO-8859-5'
alias['iso88596']='ISO-8859-6'
alias['iso88597']='ISO-8859-7'
alias['iso88598']='ISO-8859-8'
alias['iso88599']='ISO-8859-9'
alias['iso885910']='ISO-8859-10'
alias['iso885911']='ISO-8859-11'
alias['iso885912']='ISO-8859-12'
alias['iso885913']='ISO-8859-13'
alias['iso885914']='ISO-8859-14'
alias['iso885915']='ISO-8859-15'
#
alias['tis620']='TIS-620'
#
alias['cp1250']='windows-1250'
alias['cp1251']='windows-1251'
alias['cp1252']='windows-1252'
alias['cp1253']='windows-1253'
alias['cp1254']='windows-1254'
alias['cp1255']='windows-1255'
alias['cp1256']='windows-1256'
alias['cp1257']='windows-1257'
alias['cp1258']='windows-1258'

alias['x-gbk']='gbk'
alias['windows-936']='gbk'
alias['ansi-1251']='windows-1251'

