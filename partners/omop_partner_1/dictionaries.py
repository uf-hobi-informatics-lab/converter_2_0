                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                   
# ▓█████▄▓█████ ███▄ ▄███▓▒█████   ▄████ ██▀███  ▄▄▄      ██▓███  ██░ ██ ██▓▄████▄  
# ▒██▀ ██▓█   ▀▓██▒▀█▀ ██▒██▒  ██▒██▒ ▀█▓██ ▒ ██▒████▄   ▓██░  ██▓██░ ██▓██▒██▀ ▀█  
# ░██   █▒███  ▓██    ▓██▒██░  ██▒██░▄▄▄▓██ ░▄█ ▒██  ▀█▄ ▓██░ ██▓▒██▀▀██▒██▒▓█    ▄ 
# ░▓█▄   ▒▓█  ▄▒██    ▒██▒██   ██░▓█  ██▒██▀▀█▄ ░██▄▄▄▄██▒██▄█▓▒ ░▓█ ░██░██▒▓▓▄ ▄██▒
# ░▒████▓░▒████▒██▒   ░██░ ████▓▒░▒▓███▀░██▓ ▒██▒▓█   ▓██▒██▒ ░  ░▓█▒░██░██▒ ▓███▀ ░
#  ▒▒▓  ▒░░ ▒░ ░ ▒░   ░  ░ ▒░▒░▒░ ░▒   ▒░ ▒▓ ░▒▓░▒▒   ▓▒█▒▓▒░ ░  ░▒ ░░▒░░▓ ░ ░▒ ▒  ░
#  ░ ▒  ▒ ░ ░  ░  ░      ░ ░ ▒ ▒░  ░   ░  ░▒ ░ ▒░ ▒   ▒▒ ░▒ ░     ▒ ░▒░ ░▒ ░ ░  ▒   
#  ░ ░  ░   ░  ░      ░  ░ ░ ░ ▒ ░ ░   ░  ░░   ░  ░   ▒  ░░       ░  ░░ ░▒ ░       
                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                                                                                                                                                                                                              

demographic_sex_dict = {
            "0":"OT",
            "8507":"M",
            "8521":"OT",
            "8532":"F",
            "8570":"A",
            "F":"F",
            "FEMALE":"F",
            "M":"M",
            "MALE":"M",
            "OTHER":"OT", # GENDER UNKNOWN
            "PREFER NOT TO ANSWER":"NI", # GENDER UNSPECIFIED
            "SKIP":"NI", # GENDER UNSPECIFIED
            "AMBIGUOUS":"A",
            "UNKNOWN":"UN",
            "":"OT",
        }


demographic_sexual_orientation_dict = {
            "ASEXUAL":"AS",
            "BISEXUAL":"BI",
            "GAY":"GA",
            "LESBIAN":"LE",
            "QUEER":"QU",
            "LESBIAN, GAY OR HOMOSEXUAL":"HO",
            "QUESTIONING":"QS",
            "STRAIGHT":"ST",
            "SOMETHING ELSE":"SE",
            "MULTIPLE SEXUAL ORIENTATIONS":"MU",
            "DECLINE TO ANSWER":"DC",
            "":"NI",
            "UNKNOWN":"UN",
            "NO INFORMATION":"NI",

        } 



demographic_gender_identity_dict = {
            

            "MAN":"M",
            "WOMAN":"F",
            "TRANSGENDER MALE":"TM",
            "TRANS MAN":"TM",
            "FEMALE-TO-MALE":"TM",
            "TRANSGENDER FEMALE":"TF",
            "TRANS WOMAN":"TF",
            "MALE-TO-FEMALE":"TF",
            "GENDERQUEER":"GQ",
            "NON-BINARY":"GQ",
            "SOMETHING ELSE":"SE",
            "MULTIPLE GENDER CATEGORIES":"MU",
            "DECLINE TO ANSWER":"DC",
            "F":"F",
            "FEMALE":"F",
            "M":"M",
            "MALE":"M",
            "UNKNOWN":"UN",
            "NO INFORMATION":"NI",
            "":"NI",
        }


demographic_hispanic_dict = {
            "0":"OT",
            "H":"Y",
            "HISPANIC OR LATINO":"Y",
            "N":"N",
            "NOT HISPANIC OR LATINO":"N", 
            "1:NOT HISPANIC OR LATINO":"N", 
            "NON-HISPANIC OR LATINO":"N",
            "2:HISPANIC OR LATINO":"Y", 
            "PATIENT REFUSED":"NI",
            "UNKNOWN":"UN",
            "MISSING OR INVALID DATA FORMATION":"NI",
            "":"OT"    
        }


demographic_race_dict  = {

            "" : "OT",
            "WHITE" : "05",
            "AMERICAN INDIAN OR ALASKA NATIVE" : "01",
            "ASIAN" : "02",
            "BLACK OR AFRICAN AMERICAN" : "03",
            "AFRICAN AMERICAN OR BLACK" : "03",
            "African American  or Black" : "03",
            "AFRICAN AMERICAN  OR BLACK" : "03",
            "BLACK" : "03",
            "NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER" : "04",
            "ASIAN" : "02",
            "ASIAN" : "02",
            "UNKNOWN" : "UN",
            "PATIENT REFUSED" : "07",
            "PREFER NOT TO ANSWER" : "07",
            "SKIP" : "NI",
            "NOT RECORDED":"NI",
            "OTHER":"OT",
            "UNKNOWN RACIAL GROUP":"NI",
            "UNKNOWN, UNAVAILABLE OR UNREPORTED":"NI",
            "MULTIPLE":"06", 
            "MULTIRACIAL":"06",
            "MULTI-RACIAL":"06",
            "AMERICAN INDIAN OR ALASKAN NATIVE":"01",
            "AMERICAN INDIAN OR ALASKA NATIVE":"01",
            "AMERICAN INDIAN / ALASKA NATIVE":"01",
            "AMERICAN INDIAN":"01",
            "WHITE OR CAUCASIAN":"05",
            "AFRICAN AMERICAN  OR BLACK":"03",
            "CAUCASIAN OR WHITE":"05",
            "CAUCASIAN":"05",
        
        }   


demographic_biobank_flag_dict = {
            
            "":"N",
            "N":"N",
            
        } 



demographic_pat_pref_language_spoken_dict = {


            "AFAR":"AAR",
            "ABKHAZIAN":"ABK",
            "ACHINESE":"ACE",
            "ACOLI":"ACH",
            "ADANGME":"ADA",
            "ADYGHE; ADYGEI":"ADY",
            "AFRIKAANS":"AFR",
            "AINU":"AIN",
            "AKAN":"AKA",
            "ALEUT":"ALE",
            "SOUTHERN ALTAI":"ALT",
            "AMHARIC":"AMH",
            "ANGIKA":"ANP",
            "ARABIC":"ARA",
            "ARAGONESE":"ARG",
            "MAPUDUNGUN; MAPUCHE":"ARN",
            "ARAPAHO":"ARP",
            "ARAWAK":"ARW",
            "ASSAMESE":"ASM",
            "ASTURIAN; BABLE; LEONESE; ASTURLEONESE":"AST",
            "AVARIC":"AVA",
            "AWADHI":"AWA",
            "AYMARA":"AYM",
            "AZERBAIJANI":"AZE",
            "BASHKIR":"BAK",
            "BALUCHI":"BAL",
            "BAMBARA":"BAM",
            "BALINESE":"BAN",
            "BASA":"BAS",
            "BEJA; BEDAWIYET":"BEJ",
            "BELARUSIAN":"BEL",
            "BEMBA":"BEM",
            "BENGALI":"BEN",
            "BHOJPURI":"BHO",
            "BIKOL":"BIK",
            "BINI; EDO":"BIN",
            "BISLAMA":"BIS",
            "SIKSIKA":"BLA",
            "TIBETAN":"BOD",
            "BOSNIAN":"BOS",
            "BRAJ":"BRA",
            "BRETON":"BRE",
            "BURIAT":"BUA",
            "BUGINESE":"BUG",
            "BULGARIAN":"BUL",
            "BILIN; BLIN":"BYN",
            "CADDO":"CAD",
            "GALIBI CARIB":"CAR",
            "CATALAN; VALENCIAN":"CAT",
            "CEBUANO":"CEB",
            "CZECH":"CES",
            "CHAMORRO":"CHA",
            "CHECHEN":"CHE",
            "CHUUKESE":"CHK",
            "MARI":"CHM",
            "CHINOOK JARGON":"CHN",
            "CHOCTAW":"CHO",
            "CHIPEWYAN; DENE SULINE":"CHP",
            "CHEROKEE":"CHR",
            "CHUVASH":"CHV",
            "CHEYENNE":"CHY",
            "CORNISH":"COR",
            "CORSICAN":"COS",
            "CREE":"CRE",
            "CRIMEAN TATAR; CRIMEAN TURKISH":"CRH",
            "KASHUBIAN":"CSB",
            "WELSH":"CYM",
            "DAKOTA":"DAK",
            "DANISH":"DAN",
            "DARGWA":"DAR",
            "DELAWARE":"DEL",
            "SLAVE (ATHAPASCAN)":"DEN",
            "GERMAN":"DEU",
            "DOGRIB":"DGR",
            "DINKA":"DIN",
            "DHIVEHI; DHIVEHI; MALDIVIAN":"DIV",
            "DOGRI":"DOI",
            "LOWER SORBIAN":"DSB",
            "DUALA":"DUA",
            "DYULA":"DYU",
            "DZONGKHA":"DZO",
            "EFIK":"EFI",
            "EKAJUK":"EKA",
            "MODERN GREEK (1453‚ÄÌ)":"ELL",
            "ENGLISH":"ENG",
            "ESTONIAN":"EST",
            "BASQUE":"EUS",
            "EWE":"EWE",
            "EWONDO":"EWO",
            "FANG":"FAN",
            "FAROESE":"FAO",
            "PERSIAN":"FAS",
            "FANTI":"FAT",
            "FIJIAN":"FIJ",
            "FILIPINO; PILIPINO":"FIL",
            "FINNISH":"FIN",
            "FON":"FON",
            "FRENCH":"FRA",
            "NORTHERN FRISIAN":"FRR",
            "EASTERN FRISIAN":"FRS",
            "WESTERN FRISIAN":"FRY",
            "FULAH":"FUL",
            "FRIULIAN":"FUR",
            "GA":"GAA",
            "GAYO":"GAY",
            "GBAYA":"GBA",
            "GILBERTESE":"GIL",
            "GAELIC; SCOTTISH GAELIC":"GLA",
            "IRISH":"GLE",
            "GALICIAN":"GLG",
            "MANX":"GLV",
            "GONDI":"GON",
            "GORONTALO":"GOR",
            "GREBO":"GRB",
            "GUARANI":"GRN",
            "SWISS GERMAN; ALEMANNIC; ALSATIAN":"GSW",
            "GUJARATI":"GUJ",
            "GWICH ºIN":"GWI",
            "HAIDA":"HAI",
            "HAITIAN; HAITIAN CREOLE":"HAT",
            "HAUSA":"HAU",
            "HAWAIIAN":"HAW",
            "HEBREW":"HEB",
            "HERERO":"HER",
            "HILIGAYNON":"HIL",
            "HINDI":"HIN",
            "HMONG; MONG":"HMN",
            "HIRI MOTU":"HMO",
            "CROATIAN":"HRV",
            "UPPER SORBIAN":"HSB",
            "HUNGARIAN":"HUN",
            "HUPA":"HUP",
            "ARMENIAN":"HYE",
            "IBAN":"IBA",
            "IGBO":"IBO",
            "SICHUAN YI; NUOSU":"III",
            "INUKTITUT":"IKU",
            "ILOKO":"ILO",
            "INDONESIAN":"IND",
            "INGUSH":"INH",
            "INUPIAQ":"IPK",
            "ICELANDIC":"ISL",
            "ITALIAN":"ITA",
            "JAVANESE":"JAV",
            "JAPANESE":"JPN",
            "JUDEO-PERSIAN":"JPR",
            "JUDEO-ARABIC":"JRB",
            "KARA-KALPAK":"KAA",
            "KABYLE":"KAB",
            "KACHIN; JINGPHO":"KAC",
            "KALAALLISUT; GREENLANDIC":"KAL",
            "KAMBA":"KAM",
            "KANNADA":"KAN",
            "KASHMIRI":"KAS",
            "GEORGIAN":"KAT",
            "KANURI":"KAU",
            "KAZAKH":"KAZ",
            "KABARDIAN":"KBD",
            "KHASI":"KHA",
            "CENTRAL KHMER":"KHM",
            "KIKUYU; GIKUYU":"KIK",
            "KINYARWANDA":"KIN",
            "KIRGHIZ; KYRGYZ":"KIR",
            "KIMBUNDU":"KMB",
            "KONKANI":"KOK",
            "KOMI":"KOM",
            "KONGO":"KON",
            "KOREAN":"KOR",
            "KOSRAEAN":"KOS",
            "KPELLE":"KPE",
            "KARACHAY-BALKAR":"KRC",
            "KARELIAN":"KRL",
            "KURUKH":"KRU",
            "KUANYAMA; KWANYAMA":"KUA",
            "KUMYK":"KUM",
            "KURDISH":"KUR",
            "KUTENAI":"KUT",
            "LADINO":"LAD",
            "LAHNDA":"LAH",
            "LAMBA":"LAM",
            "LAO":"LAO",
            "LATVIAN":"LAV",
            "LEZGHIAN":"LEZ",
            "LIMBURGAN; LIMBURGER; LIMBURGISH":"LIM",
            "LINGALA":"LIN",
            "LITHUANIAN":"LIT",
            "MONGO":"LOL",
            "LOZI":"LOZ",
            "LUXEMBOURGISH; LETZEBURGESCH":"LTZ",
            "LUBA-LULUA":"LUA",
            "LUBA-KATANGA":"LUB",
            "GANDA":"LUG",
            "LUISENO":"LUI",
            "LUNDA":"LUN",
            "LUO (KENYA AND TANZANIA)":"LUO",
            "LUSHAI":"LUS",
            "MADURESE":"MAD",
            "MAGAHI":"MAG",
            "MARSHALLESE":"MAH",
            "MAITHILI":"MAI",
            "MAKASAR":"MAK",
            "MALAYALAM":"MAL",
            "MANDINGO":"MAN",
            "MARATHI":"MAR",
            "MASAI":"MAS",
            "MOKSHA":"MDF",
            "MANDAR":"MDR",
            "MENDE":"MEN",
            "MI'KMAQ; MICMAC":"MIC",
            "MINANGKABAU":"MIN",
            "MACEDONIAN":"MKD",
            "MALAGASY":"MLG",
            "MALTESE":"MLT",
            "MANCHU":"MNC",
            "MANIPURI":"MNI",
            "MOHAWK":"MOH",
            "MONGOLIAN":"MON",
            "MOSSI":"MOS",
            "MAORI":"MRI",
            "MALAY":"MSA",
            "CREEK":"MUS",
            "MIRANDESE":"MWL",
            "MARWARI":"MWR",
            "BURMESE":"MYA",
            "ERZYA":"MYV",
            "NEAPOLITAN":"NAP",
            "NAURU":"NAU",
            "NAVAJO; NAVAHO":"NAV",
            "SOUTH NDEBELE":"NBL",
            "NORTH NDEBELE":"NDE",
            "NDONGA":"NDO",
            "LOW GERMAN; LOW SAXON":"NDS",
            "NEPALI":"NEP",
            "NEPAL BHASA; NEWARI":"NEW",
            "NIAS":"NIA",
            "NIUEAN":"NIU",
            "DUTCH; FLEMISH":"NLD",
            "NORWEGIAN NYNORSK":"NNO",
            "NORWEGIAN BOKM√•L":"NOB",
            "NOGAI":"NOG",
            "NORWEGIAN":"NOR",
            "N'KO":"NQO",
            "PEDI; SEPEDI; NORTHERN SOTHO":"NSO",
            "CHICHEWA; CHEWA; NYANJA":"NYA",
            "NYAMWEZI":"NYM",
            "NYANKOLE":"NYN",
            "NYORO":"NYO",
            "NZIMA":"NZI",
            "OCCITAN (POST 1500)":"OCI",
            "OJIBWA":"OJI",
            "ORIYA":"ORI",
            "OROMO":"ORM",
            "OSAGE":"OSA",
            "OSSETIAN; OSSETIC":"OSS",
            "PANGASINAN":"PAG",
            "PAMPANGA; KAPAMPANGAN":"PAM",
            "PANJABI; PUNJABI":"PAN",
            "PAPIAMENTO":"PAP",
            "PALAUAN":"PAU",
            "POLISH":"POL",
            "POHNPEIAN":"PON",
            "PORTUGUESE":"POR",
            "PUSHTO; PASHTO":"PUS",
            "QUECHUA":"QUE",
            "RAJASTHANI":"RAJ",
            "RAPANUI":"RAP",
            "RAROTONGAN; COOK ISLANDS MAORI":"RAR",
            "ROMANSH":"ROH",
            "ROMANY":"ROM",
            "ROMANIAN; MOLDAVIAN; MOLDOVAN":"RON",
            "RUNDI":"RUN",
            "AROMANIAN; ARUMANIAN; MACEDO-ROMANIAN":"RUP",
            "RUSSIAN":"RUS",
            "SANDAWE":"SAD",
            "SANGO":"SAG",
            "YAKUT":"SAH",
            "SASAK":"SAS",
            "SANTALI":"SAT",
            "SICILIAN":"SCN",
            "SCOTS":"SCO",
            "SELKUP":"SEL",
            "SHAN":"SHN",
            "SIDAMO":"SID",
            "SINHALA; SINHALESE":"SIN",
            "SLOVAK":"SLK",
            "SLOVENIAN":"SLV",
            "SOUTHERN SAMI":"SMA",
            "NORTHERN SAMI":"SME",
            "LULE SAMI":"SMJ",
            "INARI SAMI":"SMN",
            "SAMOAN":"SMO",
            "SKOLT SAMI":"SMS",
            "SHONA":"SNA",
            "SINDHI":"SND",
            "SONINKE":"SNK",
            "SOMALI":"SOM",
            "SOUTHERN SOTHO":"SOT",
            "SPANISH; CASTILIAN":"SPA",
            "SPANISH":"SPA",
            "ALBANIAN":"SQI",
            "SARDINIAN":"SRD",
            "SRANAN TONGO":"SRN",
            "SERBIAN":"SRP",
            "SERER":"SRR",
            "SWATI":"SSW",
            "SUKUMA":"SUK",
            "SUNDANESE":"SUN",
            "SUSU":"SUS",
            "SWAHILI":"SWA",
            "SWEDISH":"SWE",
            "SYRIAC":"SYR",
            "TAHITIAN":"TAH",
            "TAMIL":"TAM",
            "TATAR":"TAT",
            "TELUGU":"TEL",
            "TIMNE":"TEM",
            "TERENO":"TER",
            "TETUM":"TET",
            "TAJIK":"TGK",
            "TAGALOG":"TGL",
            "THAI":"THA",
            "TIGRE":"TIG",
            "TIGRINYA":"TIR",
            "TIV":"TIV",
            "TOKELAU":"TKL",
            "TLINGIT":"TLI",
            "TAMASHEK":"TMH",
            "TONGA (NYASA)":"TOG",
            "TONGA (TONGA ISLANDS)":"TON",
            "TOK PISIN":"TPI",
            "TSIMSHIAN":"TSI",
            "TSWANA":"TSN",
            "TSONGA":"TSO",
            "TURKMEN":"TUK",
            "TUMBUKA":"TUM",
            "TURKISH":"TUR",
            "TUVALUA":"TVL",
            "TWI":"TWI",
            "TUVINIAN":"TYV",
            "UDMURT":"UDM",
            "UIGHUR; UYGHUR":"UIG",
            "UKRAINIAN":"UKR",
            "UMBUNDU":"UMB",
            "URDU":"URD",
            "UZBEK":"UZB",
            "VAI":"VAI",
            "VENDA":"VEN",
            "VIETNAMESE":"VIE",
            "VOTIC":"VOT",
            "WOLAITTA; WOLAYTTA":"WAL",
            "WARAY":"WAR",
            "WASHO":"WAS",
            "WALLOON":"WLN",
            "WOLOF":"WOL",
            "KALMYK; OIRAT":"XAL",
            "XHOSA":"XHO",
            "YAO":"YAO",
            "YAPESE":"YAP",
            "YIDDISH":"YID",
            "YORUBA":"YOR",
            "ZAPOTEC":"ZAP",
            "ZENAGA":"ZEN",
            "STANDARD MOROCCAN TAMAZIGHT":"ZGH",
            "ZHUANG; CHUANG":"ZHA",
            "CHINESE":"ZHO",
            "CHINESE":"ZHO",
            "CHINESE":"ZHO",
            "ZULU":"ZUL",
            "ZUNI":"ZUN",
            "ZAZA; DIMILI; DIMLI; KIRDKI; KIRMANJKI; ZAZAKI":"ZZA",
            "NO INFORMATION":"NI",
            "UNKNOWN":"UN",
            "OTHER":"OT",
            "OTHER":"OT",


}

# ▓█████ ███▄    █ ▄████▄  ▒█████  █    ██ ███▄    █▄▄▄█████▓█████ ██▀███  
# ▓█   ▀ ██ ▀█   █▒██▀ ▀█ ▒██▒  ██▒██  ▓██▒██ ▀█   █▓  ██▒ ▓▓█   ▀▓██ ▒ ██▒
# ▒███  ▓██  ▀█ ██▒▓█    ▄▒██░  ██▓██  ▒██▓██  ▀█ ██▒ ▓██░ ▒▒███  ▓██ ░▄█ ▒
# ▒▓█  ▄▓██▒  ▐▌██▒▓▓▄ ▄██▒██   ██▓▓█  ░██▓██▒  ▐▌██░ ▓██▓ ░▒▓█  ▄▒██▀▀█▄  
# ░▒████▒██░   ▓██▒ ▓███▀ ░ ████▓▒▒▒█████▓▒██░   ▓██░ ▒██▒ ░░▒████░██▓ ▒██▒
# ░░ ▒░ ░ ▒░   ▒ ▒░ ░▒ ▒  ░ ▒░▒░▒░░▒▓▒ ▒ ▒░ ▒░   ▒ ▒  ▒ ░░  ░░ ▒░ ░ ▒▓ ░▒▓░
#  ░ ░  ░ ░░   ░ ▒░ ░  ▒    ░ ▒ ▒░░░▒░ ░ ░░ ░░   ░ ▒░   ░    ░ ░  ░ ░▒ ░ ▒░
#    ░     ░   ░ ░░       ░ ░ ░ ▒  ░░░ ░ ░   ░   ░ ░  ░        ░    ░░   ░ 
#    ░  ░        ░░ ░         ░ ░    ░             ░           ░  ░  ░     
#                 ░                                                        

encounter_enc_type_dict ={

            ""           : "OT", # Other 
            "EMERGENCY ROOM AND INPATIENT" : "EI", # Emergency Department Admit to Inpatient Hospital Stay
            "INPATIENT"                    : "IP", # Inpatient Hospital Stay
            "EMERGENCY ROOM"               : "ED", # Emergency Department
            "OUTPATIENT"                   : "AV", # Outpatient Visit - Non Physician
            "INPATIENT VISIT"              : "IP", # Inpatient Hospital Stay
            "OUTPATIENT VISIT"             : "AV", # Outpatient Visit - Non Physician
            "OFFICE VISIT"                 : "AV", # Outpatient Visit - Non Physician
            "TELEHEALTH"                   : "TH", # Telehealth
            "OBSERVATION VISIT"            : "OS", # 
            "LABORATORY VISIT"             : "OA", # 
            "REHABILITATION VISIT"         : "IS", # 
            "EMERGENCY ROOM VISIT"         : "ED", # Emergency Department
            "LABORATORY"                   : "OA", # Laboratory Visit
            "INTENSIVE CARE"               : "IP", # Intensive Care
            "PHARMACY"                     : "OA", # Pharmacy visit
            "HOME"                         : "OA", # Home Visit
            "OFFICE"                       : "AV", # Office Visit
            "AMBULANCE"                    : "ED", # Ambulatory Visit
            "REHABILITATION"               : "IS", # Rehabilitation Visit
            "LONG TERM CARE"               : "IS", # Long Term Care Visit
            "UNKNOWN"                      : "UN", # Unknown
            "OTHER"                        : "OT", # Other
            "NO INFORMATION"               : "NI", # No information 

}

 




encounter_drg_type_dict = {
    1:"01",
    2:"02",
    "01":"01",
    "02":"02",
}


encounter_discharge_disposition_dict = {

            "44814649":"OT", #Other
            "44814653":"UN", #Unknown
            "44814650":"NI",# No information
            "4216643":"E",  # Expired
            "4161979":"A", #Alive
            "44814685":"A",# Discharged alive omop
            "44814686":"E", # Expired
            "":"NI",
            "ALIVE":"A", #Alive
            "EXPIRED":"A", #Alive
        }


encounter_discharge_status_dict = {

            "44814670" : "AF", #	Adult foster home
            "44814671" : "AL", #	Assisted living facility
            "44814672" : "AV", #	Ambulatory visit
            "44814673" : "ED", #	Emergency department
            "44814674" : "HH", #	Home health
            "44814675" : "HO", #	Home / self care
            "44814676" : "HS", #	Hospice
            "44814677" : "IP", #	Other acute inpatient hospital
            "44814678" : "NH", #	Nursing home (includes ICF)
            "44814679" : "RH", #	Rehabilitation facility
            "44814680" : "RS", #	Residential facility
            "44814681" : "SN", #	Skilled nursing facility
            "44814650" :"NI" , #	No information
            "44814653" :"UN" , #	Unknown
            "44814649" :"OT" , #	Other
            "0"        :"OT" , #	Other
            ""         :"OT" , #	OT

            "6:Rehab Facility"              : "RH", #	
            "6:Home-Health Care Svc"        : "HH", #	
            "3:Skilled Nursing Facility"    : "SN", #	
            "1:Home or Self Care"           : "HO", #	
            "7:Left Against Medical Advice" : "OT", #	
            "HOME / SELF CARE"              : "HO", #
            "OTHER"                         : "OT", #
            "REHABILITATION FACILITY"       : "RH", #
            "NURSING HOME (INCLUDES ICF)"   : "NH", #
            "OTHER ACUTE INPATIENT HOSPITAL": "IP", #
            "HOME HEALTH"                   : "HH", #
            "AMBULATORY VISIT"              : "", #
            "HOME OR SELF CARE"             : "HO", #
            "SKILLED NURSING FACILITY"      : "SN", #
            "HOSPICE/HOME"                  : "HS", #

             }


encounter_admitting_source_dict = {
            "44814670" : "AF", #	Adult foster home
            "44814671" : "AL", #	Assisted living facility
            "44814672" : "AV", #	Ambulatory visit
            "44814673" : "ED", #	Emergency department
            "44814674" : "HH", #	Home health
            "44814675" : "HO", #	Home / self care
            "44814676" : "HS", #	Hospice
            "44814677" : "IP", #	Other acute inpatient hospital
            "44814678" : "NH", #	Nursing home (includes ICF)
            "44814679" : "RH", #	Rehabilitation facility
            "44814680" : "RS", #	Residential facility
            "44814681" : "SN", #	Skilled nursing facility
            "44814650" :"NI" , #	No information
            "44814653" :"UN" , #	Unknown
            "44814649" :"OT" , #	Other
            "0"        :"OT" , #	Other
            ""         :"OT" , #	OT

            "Rehab Facility"              : "RH", #	
            "Home-Health Care Svc"        : "HH", #	
            "Skilled Nursing Facility"    : "SN", #	
            "Home or Self Care"           : "HO", #	
            "Left Against Medical Advice" : "OT", #	
            "HOME / SELF CARE"              : "HO", #
            "OTHER"                         : "OT", #
            "REHABILITATION FACILITY"       : "RH", #
            "NURSING HOME (INCLUDES ICF)"   : "NH", #
            "OTHER ACUTE INPATIENT HOSPITAL": "IP", #
            "HOME HEALTH"                   : "HH", #
            "AMBULATORY VISIT"              : "AV", #
            




        }


encounter_payer_type_primary_dict= {

        "MEDICARE":"1",
        "MEDICAID":"2",
        "OTHER GOVERNMENT (FEDERAL/STATE/LOCAL) (EXCLUDING DEPARTMENT OF CORRECTIONS)":"3",
        "DEPARTMENTS OF CORRECTIONS":"4",
        "PRIVATE HEALTH INSURANCE":"5",
        "BLUE CROSS/BLUE SHIELD":"6",
        "BCBS BLUE SELECT NETWORK PPO":"6",
        "MANAGED CARE UNSPECIFIED (TO BE USED ONLY IF ONE CAN'T DISTINGUISH PUBLIC FROM PRIVATE)":"7",
        "NO PAYMENT FROM AN ORGANIZATION/AGENCY/PROGRAM/PRIVATE PAYER LISTED":"8",
        "MISCELLANEOUS/OTHER":"9",
        "MEDICARE (MANAGED CARE)":"11",
        "MEDICARE (NON-MANAGED CARE)":"12",
        "MEDICARE HOSPICE":"13",
        "DUAL ELIGIBILITY MEDICARE/MEDICAID ORGANIZATION":"14",
        "MEDICARE OTHER":"19",
        "MEDICARE - OTHER":"19",
        "MEDICAID (MANAGED CARE)":"21",
        "MEDICAID (NON-MANAGED CARE PLAN)":"22",
        "MEDICAID/SCHIP":"23",
        "MEDICAID/SCHIP":"23",
        "MEDICAID/SCHIP":"23",
        "MEDICAID/SCHIP":"23",
        "MEDICAID APPLICANT":"24",
        "MEDICAID - OUT OF STATE":"25",
        "MEDICAID LONG TERM CARE":"26",
        "MEDICAID OTHER":"29",
        "DEPARTMENT OF DEFENSE":"31",
        "DEPARTMENT OF VETERANS AFFAIRS":"32",
        "INDIAN HEALTH SERVICE OR TRIBE":"33",
        "HRSA PROGRAM":"34",
        "BLACK LUNG":"35",
        "STATE GOVERNMENT":"36",
        "LOCAL GOVERNMENT":"37",
        "OTHER GOVERNMENT (FEDERAL STATE LOCAL NOT SPECIFIED)":"38",
        "OTHER FEDERAL":"39",
        "CORRECTIONS FEDERAL":"41",
        "CORRECTIONS STATE":"42",
        "CORRECTIONS LOCAL":"43",
        "CORRECTIONS UNKNOWN LEVEL":"44",
        "MANAGED CARE (PRIVATE)":"51",
        "PRIVATE HEALTH INSURANCE - INDEMNITY":"52",
        "MANAGED CARE (PRIVATE) OR PRIVATE HEALTH INSURANCE (INDEMNITY) NOT OTHERWISE SPECIFIED":"53",
        "ORGANIZED DELIVERY SYSTEM":"54",
        "SMALL EMPLOYER PURCHASING GROUP":"55",
        "SPECIALIZED STAND ALONE PLAN":"56",
        "BC MANAGED CARE":"61",
        "BC INSURANCE INDEMNITY":"62",
        "HMO":"71",
        "PPO":"72",
        "POS":"73",
        "OTHER MANAGED CARE":"79",
        "SELF-PAY":"81",
        "NO CHARGE":"82",
        "REFUSAL TO PAY/BAD DEBT":"83",
        "HILL BURTON FREE CARE":"84",
        "RESEARCH/DONOR":"85",
        "NO PAYMENT OTHER":"89",
        "FOREIGN NATIONAL":"91",
        "OTHER (NON-GOVERNMENT)":"92",
        "DISABILITY INSURANCE":"93",
        "LONG-TERM CARE INSURANCE":"94",
        "WORKER'S COMPENSATION":"95",
        "AUTO INSURANCE (INCLUDES NO FAULT)":"96",
        "LEGAL LIABILITY / LIABILITY INSURANCE":"97",
        "OTHER SPECIFIED BUT NOT OTHERWISE CLASSIFIABLE (INCLUDES HOSPICE - UNSPECIFIED PLAN)":"98",
        "NO TYPOLOGY CODE AVAILABLE FOR PAYMENT SOURCE":"99",
        "MEDICARE HMO":"111",
        "MEDICARE PPO":"112",
        "MEDICARE POS":"113",
        "MEDICARE MANAGED CARE OTHER":"119",
        "MEDICARE FFS":"121",
        "MEDICARE DRUG BENEFIT":"122",
        "MEDICARE MEDICAL SAVINGS ACCOUNT (MSA)":"123",
        "MEDICARE NON-MANAGED CARE OTHER":"129",
        "MEDICARE PHARMACY BENEFIT MANAGER":"191",
        "MEDICAID HMO":"211",
        "MEDICAID PPO":"212",
        "MEDICAID PCCM (PRIMARY CARE CASE MANAGEMENT)":"213",
        "MEDICAID MANAGED CARE OTHER":"219",
        "MEDICAID PHARMACY BENEFIT MANAGER":"291",
        "MEDICAID - DENTAL":"299",
        "TRICARE (CHAMPUS)":"311",
        "MILITARY TREATMENT FACILITY":"312",
        "DENTAL --STAND ALONE":"313",
        "VETERAN CARE--CARE PROVIDED TO VETERANS":"321",
        "NON-VETERAN CARE":"322",
        "INDIAN HEALTH SERVICE REGULAR":"331",
        "INDIAN HEALTH SERVICE CONTRACT":"332",
        "INDIAN HEALTH SERVICE - MANAGED CARE":"333",
        "INDIAN TRIBE - SPONSORED COVERAGE":"334",
        "TITLE V (MCH BLOCK GRANT)":"341",
        "MIGRANT HEALTH PROGRAM":"342",
        "RYAN WHITE ACT":"343",
        "OTHER":"349",
        "STATE SCHIP PROGRAM (CODES FOR INDIVIDUAL STATES)":"361",
        "SPECIFIC STATE PROGRAMS (LIST/ LOCAL CODE)":"362",
        "STATE NOT OTHERWISE SPECIFIED (OTHER STATE)":"369",
        "LOCAL - MANAGED CARE":"371",
        "FFS/INDEMNITY":"372",
        "LOCAL NOT OTHERWISE SPECIFIED (OTHER LOCAL COUNTY)":"379",
        "FEDERAL STATE LOCAL NOT SPECIFIED MANAGED CARE":"381",
        "FEDERAL STATE LOCAL NOT SPECIFIED - FFS":"382",
        "FEDERAL STATE LOCAL NOT SPECIFIED - OTHER":"389",
        "FEDERAL EMPLOYEE HEALTH PLAN USE WHEN KNOWN.":"391",
        "COMMERCIAL MANAGED CARE - HMO":"511",
        "COMMERCIAL MANAGED CARE - PPO":"512",
        "COMMERCIAL MANAGED CARE - POS":"513",
        "EXCLUSIVE PROVIDER ORGANIZATION":"514",
        "GATEKEEPER PPO (GPPO)":"515",
        "COMMERCIAL MANAGED CARE - PHARMACY BENEFIT MANAGER":"516",
        "COMMERCIAL MANAGED CARE - DENTAL":"517",
        "MANAGED CARE OTHER (NON HMO)":"519",
        "COMMERCIAL INDEMNITY":"521",
        "SELF-INSURED (ERISA) ADMINISTRATIVE SERVICES ONLY (ASO) PLAN":"522",
        "MEDICARE SUPPLEMENTAL POLICY (AS SECOND PAYER)":"523",
        "INDEMNITY INSURANCE - DENTAL":"524",
        "PRIVATE HEALTH INSURANCEOTHER COMMERCIAL INDEMNITY":"529",
        "DENTAL":"561",
        "VISION OTHER PRIVATE INSURANCE":"562",
        "BC MANAGED CARE HMO":"611",
        "BC MANAGED CARE PPO":"612",
        "BLUE CROSS MANAGED CARE - PREFERRED PROVIDER ORGANIZATION (PPO)":"612",
        "BC MANAGED CARE POS":"613",
        "BC MANAGED CARE - DENTAL":"614",
        "BC MANAGED CARE OTHER":"619",
        "BC INDEMNITY":"621",
        "BC SELF-INSURED (ERISA) ADMINISTRATIVE SERVICES ONLY (ASO)PLAN":"622",
        "BC MEDICARE SUPPLEMENTAL PLAN":"623",
        "BLUE CROSS MEDICARE SUPPLEMENTAL PLAN":"623",
        "BC INDEMNITY - DENTAL":"629",
        "CHARITY":"821",
        "PROFESSIONAL COURTESY":"822",
        "RESEARCH/CLINICAL TRIAL":"823",
        "WORKER'S COMP HMO":"951",
        "WORKER'S COMP FEE-FOR-SERVICE":"953",
        "WORKERS COMP OTHER MANAGED CARE":"954",
        "WORKER'S COMP OTHER UNSPECIFIED":"959",
        "TRICARE PRIMEHMO":"3111",
        "TRICARE EXTRAPPO":"3112",
        "TRICARE STANDARD - FEE FOR SERVICE":"3113",
        "TRICARE FOR LIFE--MEDICARE SUPPLEMENT":"3114",
        "TRICARE RESERVE SELECT":"3115",
        "UNIFORMED SERVICES FAMILY HEALTH PLAN (USFHP) -- HMO":"3116",
        "DEPARTMENT OF DEFENSE - (OTHER)":"3119",
        "ENROLLED PRIMEHMO":"3121",
        "NON-ENROLLED SPACE AVAILABLE":"3122",
        "TRICARE FOR LIFE (TFL)":"3123",
        "DIRECT CARE--CARE PROVIDED IN VA FACILITIES":"3211",
        "INDIRECT CARE--CARE PROVIDED OUTSIDE VA FACILITIES":"3212",
        "CIVILIAN HEALTH AND MEDICAL PROGRAM FOR THE VA (CHAMPVA)":"3221",
        "SPINA BIFIDA HEALTH CARE PROGRAM (SB)":"3222",
        "CHILDREN OF WOMEN VIETNAM VETERANS (CWVV)":"3223",
        "OTHER NON-VETERAN CARE":"3229",
        "HMO":"3711",
        "PPO":"3712",
        "POS":"3713",
        "FEDERAL STATE LOCAL NOT SPECIFIED - HMO":"3811",
        "FEDERAL STATE LOCAL NOT SPECIFIED - PPO":"3812",
        "FEDERAL STATE LOCAL NOT SPECIFIED - POS":"3813",
        "FEDERAL STATE LOCAL NOT SPECIFIED - NOT SPECIFIED MANAGED CARE":"3819",
        "UNAVAILABLE / NO PAYER SPECIFIED / BLANK":"9999",
        "FEE BASIS":"32121",
        "FOREIGN FEE/FOREIGN MEDICAL PROGRAM (FMP)":"32122",
        "CONTRACT NURSING HOME/COMMUNITY NURSING HOME":"32123",
        "STATE VETERANS HOME":"32124",
        "SHARING AGREEMENTS":"32125",
        "OTHER FEDERAL AGENCY":"32126",
        "DENTAL CARE":"32127",
        "VISION CARE":"32128",
    
}




encounter_payer_type_secondary_dict= {

        "MEDICARE":"1",
        "MEDICAID":"2",
        "OTHER GOVERNMENT (FEDERAL/STATE/LOCAL) (EXCLUDING DEPARTMENT OF CORRECTIONS)":"3",
        "DEPARTMENTS OF CORRECTIONS":"4",
        "PRIVATE HEALTH INSURANCE":"5",
        "BLUE CROSS/BLUE SHIELD":"6",
        "BCBS BLUE SELECT NETWORK PPO":"6",
        "MANAGED CARE UNSPECIFIED (TO BE USED ONLY IF ONE CAN'T DISTINGUISH PUBLIC FROM PRIVATE)":"7",
        "NO PAYMENT FROM AN ORGANIZATION/AGENCY/PROGRAM/PRIVATE PAYER LISTED":"8",
        "MISCELLANEOUS/OTHER":"9",
        "MEDICARE (MANAGED CARE)":"11",
        "MEDICARE (NON-MANAGED CARE)":"12",
        "MEDICARE HOSPICE":"13",
        "DUAL ELIGIBILITY MEDICARE/MEDICAID ORGANIZATION":"14",
        "MEDICARE OTHER":"19",
        "MEDICARE - OTHER":"19",
        "MEDICAID (MANAGED CARE)":"21",
        "MEDICAID (NON-MANAGED CARE PLAN)":"22",
        "MEDICAID/SCHIP":"23",
        "MEDICAID/SCHIP":"23",
        "MEDICAID/SCHIP":"23",
        "MEDICAID/SCHIP":"23",
        "MEDICAID APPLICANT":"24",
        "MEDICAID - OUT OF STATE":"25",
        "MEDICAID LONG TERM CARE":"26",
        "MEDICAID OTHER":"29",
        "DEPARTMENT OF DEFENSE":"31",
        "DEPARTMENT OF VETERANS AFFAIRS":"32",
        "INDIAN HEALTH SERVICE OR TRIBE":"33",
        "HRSA PROGRAM":"34",
        "BLACK LUNG":"35",
        "STATE GOVERNMENT":"36",
        "LOCAL GOVERNMENT":"37",
        "OTHER GOVERNMENT (FEDERAL STATE LOCAL NOT SPECIFIED)":"38",
        "OTHER FEDERAL":"39",
        "CORRECTIONS FEDERAL":"41",
        "CORRECTIONS STATE":"42",
        "CORRECTIONS LOCAL":"43",
        "CORRECTIONS UNKNOWN LEVEL":"44",
        "MANAGED CARE (PRIVATE)":"51",
        "PRIVATE HEALTH INSURANCE - INDEMNITY":"52",
        "MANAGED CARE (PRIVATE) OR PRIVATE HEALTH INSURANCE (INDEMNITY) NOT OTHERWISE SPECIFIED":"53",
        "ORGANIZED DELIVERY SYSTEM":"54",
        "SMALL EMPLOYER PURCHASING GROUP":"55",
        "SPECIALIZED STAND ALONE PLAN":"56",
        "BC MANAGED CARE":"61",
        "BC INSURANCE INDEMNITY":"62",
        "HMO":"71",
        "PPO":"72",
        "POS":"73",
        "OTHER MANAGED CARE":"79",
        "SELF-PAY":"81",
        "NO CHARGE":"82",
        "REFUSAL TO PAY/BAD DEBT":"83",
        "HILL BURTON FREE CARE":"84",
        "RESEARCH/DONOR":"85",
        "NO PAYMENT OTHER":"89",
        "FOREIGN NATIONAL":"91",
        "OTHER (NON-GOVERNMENT)":"92",
        "DISABILITY INSURANCE":"93",
        "LONG-TERM CARE INSURANCE":"94",
        "WORKER'S COMPENSATION":"95",
        "AUTO INSURANCE (INCLUDES NO FAULT)":"96",
        "LEGAL LIABILITY / LIABILITY INSURANCE":"97",
        "OTHER SPECIFIED BUT NOT OTHERWISE CLASSIFIABLE (INCLUDES HOSPICE - UNSPECIFIED PLAN)":"98",
        "NO TYPOLOGY CODE AVAILABLE FOR PAYMENT SOURCE":"99",
        "MEDICARE HMO":"111",
        "MEDICARE PPO":"112",
        "MEDICARE POS":"113",
        "MEDICARE MANAGED CARE OTHER":"119",
        "MEDICARE FFS":"121",
        "MEDICARE DRUG BENEFIT":"122",
        "MEDICARE MEDICAL SAVINGS ACCOUNT (MSA)":"123",
        "MEDICARE NON-MANAGED CARE OTHER":"129",
        "MEDICARE PHARMACY BENEFIT MANAGER":"191",
        "MEDICAID HMO":"211",
        "MEDICAID PPO":"212",
        "MEDICAID PCCM (PRIMARY CARE CASE MANAGEMENT)":"213",
        "MEDICAID MANAGED CARE OTHER":"219",
        "MEDICAID PHARMACY BENEFIT MANAGER":"291",
        "MEDICAID - DENTAL":"299",
        "TRICARE (CHAMPUS)":"311",
        "MILITARY TREATMENT FACILITY":"312",
        "DENTAL --STAND ALONE":"313",
        "VETERAN CARE--CARE PROVIDED TO VETERANS":"321",
        "NON-VETERAN CARE":"322",
        "INDIAN HEALTH SERVICE REGULAR":"331",
        "INDIAN HEALTH SERVICE CONTRACT":"332",
        "INDIAN HEALTH SERVICE - MANAGED CARE":"333",
        "INDIAN TRIBE - SPONSORED COVERAGE":"334",
        "TITLE V (MCH BLOCK GRANT)":"341",
        "MIGRANT HEALTH PROGRAM":"342",
        "RYAN WHITE ACT":"343",
        "OTHER":"349",
        "STATE SCHIP PROGRAM (CODES FOR INDIVIDUAL STATES)":"361",
        "SPECIFIC STATE PROGRAMS (LIST/ LOCAL CODE)":"362",
        "STATE NOT OTHERWISE SPECIFIED (OTHER STATE)":"369",
        "LOCAL - MANAGED CARE":"371",
        "FFS/INDEMNITY":"372",
        "LOCAL NOT OTHERWISE SPECIFIED (OTHER LOCAL COUNTY)":"379",
        "FEDERAL STATE LOCAL NOT SPECIFIED MANAGED CARE":"381",
        "FEDERAL STATE LOCAL NOT SPECIFIED - FFS":"382",
        "FEDERAL STATE LOCAL NOT SPECIFIED - OTHER":"389",
        "FEDERAL EMPLOYEE HEALTH PLAN USE WHEN KNOWN.":"391",
        "COMMERCIAL MANAGED CARE - HMO":"511",
        "COMMERCIAL MANAGED CARE - PPO":"512",
        "COMMERCIAL MANAGED CARE - POS":"513",
        "EXCLUSIVE PROVIDER ORGANIZATION":"514",
        "GATEKEEPER PPO (GPPO)":"515",
        "COMMERCIAL MANAGED CARE - PHARMACY BENEFIT MANAGER":"516",
        "COMMERCIAL MANAGED CARE - DENTAL":"517",
        "MANAGED CARE OTHER (NON HMO)":"519",
        "COMMERCIAL INDEMNITY":"521",
        "SELF-INSURED (ERISA) ADMINISTRATIVE SERVICES ONLY (ASO) PLAN":"522",
        "MEDICARE SUPPLEMENTAL POLICY (AS SECOND PAYER)":"523",
        "INDEMNITY INSURANCE - DENTAL":"524",
        "PRIVATE HEALTH INSURANCEOTHER COMMERCIAL INDEMNITY":"529",
        "DENTAL":"561",
        "VISION OTHER PRIVATE INSURANCE":"562",
        "BC MANAGED CARE HMO":"611",
        "BC MANAGED CARE PPO":"612",
        "BLUE CROSS MANAGED CARE - PREFERRED PROVIDER ORGANIZATION (PPO)":"612",
        "BC MANAGED CARE POS":"613",
        "BC MANAGED CARE - DENTAL":"614",
        "BC MANAGED CARE OTHER":"619",
        "BC INDEMNITY":"621",
        "BC SELF-INSURED (ERISA) ADMINISTRATIVE SERVICES ONLY (ASO)PLAN":"622",
        "BC MEDICARE SUPPLEMENTAL PLAN":"623",
        "BLUE CROSS MEDICARE SUPPLEMENTAL PLAN":"623",
        "BC INDEMNITY - DENTAL":"629",
        "CHARITY":"821",
        "PROFESSIONAL COURTESY":"822",
        "RESEARCH/CLINICAL TRIAL":"823",
        "WORKER'S COMP HMO":"951",
        "WORKER'S COMP FEE-FOR-SERVICE":"953",
        "WORKERS COMP OTHER MANAGED CARE":"954",
        "WORKER'S COMP OTHER UNSPECIFIED":"959",
        "TRICARE PRIMEHMO":"3111",
        "TRICARE EXTRAPPO":"3112",
        "TRICARE STANDARD - FEE FOR SERVICE":"3113",
        "TRICARE FOR LIFE--MEDICARE SUPPLEMENT":"3114",
        "TRICARE RESERVE SELECT":"3115",
        "UNIFORMED SERVICES FAMILY HEALTH PLAN (USFHP) -- HMO":"3116",
        "DEPARTMENT OF DEFENSE - (OTHER)":"3119",
        "ENROLLED PRIMEHMO":"3121",
        "NON-ENROLLED SPACE AVAILABLE":"3122",
        "TRICARE FOR LIFE (TFL)":"3123",
        "DIRECT CARE--CARE PROVIDED IN VA FACILITIES":"3211",
        "INDIRECT CARE--CARE PROVIDED OUTSIDE VA FACILITIES":"3212",
        "CIVILIAN HEALTH AND MEDICAL PROGRAM FOR THE VA (CHAMPVA)":"3221",
        "SPINA BIFIDA HEALTH CARE PROGRAM (SB)":"3222",
        "CHILDREN OF WOMEN VIETNAM VETERANS (CWVV)":"3223",
        "OTHER NON-VETERAN CARE":"3229",
        "HMO":"3711",
        "PPO":"3712",
        "POS":"3713",
        "FEDERAL STATE LOCAL NOT SPECIFIED - HMO":"3811",
        "FEDERAL STATE LOCAL NOT SPECIFIED - PPO":"3812",
        "FEDERAL STATE LOCAL NOT SPECIFIED - POS":"3813",
        "FEDERAL STATE LOCAL NOT SPECIFIED - NOT SPECIFIED MANAGED CARE":"3819",
        "UNAVAILABLE / NO PAYER SPECIFIED / BLANK":"9999",
        "FEE BASIS":"32121",
        "FOREIGN FEE/FOREIGN MEDICAL PROGRAM (FMP)":"32122",
        "CONTRACT NURSING HOME/COMMUNITY NURSING HOME":"32123",
        "STATE VETERANS HOME":"32124",
        "SHARING AGREEMENTS":"32125",
        "OTHER FEDERAL AGENCY":"32126",
        "DENTAL CARE":"32127",
        "VISION CARE":"32128",
    
}



encounter_facility_type_dict = {


        "INPATIENT HOSPITAL":"",
        "OFFICE":"",
        "ON CAMPUS - OUTPATIENT HOSPITAL":"",
        "AMBULATORY SURGICAL CENTER":"",
        "URGENT CARE FACILITY":"",



            "ADULT_DAY_CARE_CENTER"	 : 	"ADULT_DAY_CARE_CENTER"	,
        "AMBULANCE_BASED_CARE"	 : 	"AMBULANCE_BASED_CARE"	,
        "AMBULANCE_BASED_CARE"	 : 	"AMBULANCE_BASED_CARE"	,
        "AMBULATORY_CARE_SITE_OTHER_"	 : 	"AMBULATORY_CARE_SITE_OTHER_"	,
        "AMBULATORY_SURGERY_CENTER"	 : 	"AMBULATORY_SURGERY_CENTER"	,
        "CARE_OF_THE_ELDERLY_DAY_HOSPITAL"	 : 	"CARE_OF_THE_ELDERLY_DAY_HOSPITAL"	,
        "CHILD_DAY_CARE_CENTER"	 : 	"CHILD_DAY_CARE_CENTER"	,
        "CONTAINED_CASUALTY_SETTING"	 : 	"CONTAINED_CASUALTY_SETTING"	,
        "DIALYSIS_UNIT_HOSPITAL"	 : 	"DIALYSIS_UNIT_HOSPITAL"	,
        "ELDERLY_ASSESSMENT_CLINIC"	 : 	"ELDERLY_ASSESSMENT_CLINIC"	,
        "EMERGENCY_DEPARTMENT_HOSPITAL"	 : 	"EMERGENCY_DEPARTMENT_HOSPITAL"	,
        "EMERGENCY_DEPARTMENT_HOSPITAL"	 : 	"EMERGENCY_DEPARTMENT_HOSPITAL"	,
        "FEE_FOR_SERVICE_PRIVATE_PHYSICIANS_GROUP_OFFICE"	 : 	"FEE_FOR_SERVICE_PRIVATE_PHYSICIANS_GROUP_OFFICE"	,
        "FREE_STANDING_AMBULATORY_SURGERY_FACILITY"	 : 	"FREE_STANDING_AMBULATORY_SURGERY_FACILITY"	,
        "FREE_STANDING_BIRTHING_CENTER"	 : 	"FREE_STANDING_BIRTHING_CENTER"	,
        "FREE_STANDING_GERIATRIC_HEALTH_CENTER"	 : 	"FREE_STANDING_GERIATRIC_HEALTH_CENTER"	,
        "FREE_STANDING_LABORATORY_FACILITY"	 : 	"FREE_STANDING_LABORATORY_FACILITY"	,
        "FREE_STANDING_MENTAL_HEALTH_CENTER"	 : 	"FREE_STANDING_MENTAL_HEALTH_CENTER"	,
        "FREE_STANDING_RADIOLOGY_FACILITY"	 : 	"FREE_STANDING_RADIOLOGY_FACILITY"	,
        "HEALTH_ENCOUNTER_SITE_NOT_LISTED"	 : 	"HEALTH_ENCOUNTER_SITE_NOT_LISTED"	,
        "HEALTH_MAINTENANCE_ORGANIZATION"	 : 	"HEALTH_MAINTENANCE_ORGANIZATION"	,
        "HELICOPTER_BASED_CARE"	 : 	"HELICOPTER_BASED_CARE"	,
        "HOSPICE_FACILITY"	 : 	"HOSPICE_FACILITY"	,
        "HOSPITAL_BASED_OUTPATIENT_CLINIC_OR_DEPARTMENT_OTHER"	 : 	"HOSPITAL_BASED_OUTPATIENT_CLINIC_OR_DEPARTMENT_OTHER"	,
        "HOSPITAL_CHILDRENS"	 : 	"HOSPITAL_CHILDRENS"	,
        "HOSPITAL_COMMUNITY"	 : 	"HOSPITAL_COMMUNITY"	,
        "HOSPITAL_GOVERNMENT"	 : 	"HOSPITAL_GOVERNMENT"	,
        "HOSPITAL_LONG_TERM_CARE"	 : 	"HOSPITAL_LONG_TERM_CARE"	,
        "HOSPITAL_MILITARY_FIELD"	 : 	"HOSPITAL_MILITARY_FIELD"	,
        "HOSPITAL_PRISON"	 : 	"HOSPITAL_PRISON"	,
        "HOSPITAL_PSYCHIATRIC"	 : 	"HOSPITAL_PSYCHIATRIC"	,
        "HOSPITAL_REHABILITATION"	 : 	"HOSPITAL_REHABILITATION"	,
        "HOSPITAL_TRAUMA_CENTER"	 : 	"HOSPITAL_TRAUMA_CENTER"	,
        "HOSPITAL_VETERANS_ADMINISTRATION"	 : 	"HOSPITAL_VETERANS_ADMINISTRATION"	,
        "HOSPITAL_AMBULATORY_SURGERY_FACILITY"	 : 	"HOSPITAL_AMBULATORY_SURGERY_FACILITY"	,
        "HOSPITAL_BIRTHING_CENTER"	 : 	"HOSPITAL_BIRTHING_CENTER"	,
        "HOSPITAL_OUTPATIENT_DENTAL_CLINIC"	 : 	"HOSPITAL_OUTPATIENT_DENTAL_CLINIC"	,
        "HOSPITAL_OUTPATIENT_DERMATOLOGY_CLINIC"	 : 	"HOSPITAL_OUTPATIENT_DERMATOLOGY_CLINIC"	,
        "HOSPITAL_OUTPATIENT_ENDOCRINOLOGY_CLINIC"	 : 	"HOSPITAL_OUTPATIENT_ENDOCRINOLOGY_CLINIC"	,
        "HOSPITAL_OUTPATIENT_FAMILY_MEDICINE_CLINIC"	 : 	"HOSPITAL_OUTPATIENT_FAMILY_MEDICINE_CLINIC"	,
        "HOSPITAL_OUTPATIENT_GASTROENTEROLOGY_CLINIC"	 : 	"HOSPITAL_OUTPATIENT_GASTROENTEROLOGY_CLINIC"	,
        "HOSPITAL_OUTPATIENT_GASTROENTEROLOGY_CLINIC"	 : 	"HOSPITAL_OUTPATIENT_GASTROENTEROLOGY_CLINIC"	,
        "HOSPITAL_OUTPATIENT_GENERAL_SURGERY_CLINIC"	 : 	"HOSPITAL_OUTPATIENT_GENERAL_SURGERY_CLINIC"	,
        "HOSPITAL_OUTPATIENT_GERIATRIC_HEALTH_CENTER"	 : 	"HOSPITAL_OUTPATIENT_GERIATRIC_HEALTH_CENTER"	,
        "HOSPITAL_OUTPATIENT_HEMATOLOGY_CLINIC"	 : 	"HOSPITAL_OUTPATIENT_HEMATOLOGY_CLINIC"	,
        "HOSPITAL_OUTPATIENT_INFECTIOUS_DISEASE_CLINIC"	 : 	"HOSPITAL_OUTPATIENT_INFECTIOUS_DISEASE_CLINIC"	,
        "HOSPITAL_OUTPATIENT_MENTAL_HEALTH_CENTER"	 : 	"HOSPITAL_OUTPATIENT_MENTAL_HEALTH_CENTER"	,
        "HOSPITAL_OUTPATIENT_NEUROLOGY_CLINIC"	 : 	"HOSPITAL_OUTPATIENT_NEUROLOGY_CLINIC"	,
        "HOSPITAL_OUTPATIENT_ONCOLOGY_CLINIC"	 : 	"HOSPITAL_OUTPATIENT_ONCOLOGY_CLINIC"	,
        "HOSPITAL_OUTPATIENT_ONCOLOGY_CLINIC"	 : 	"HOSPITAL_OUTPATIENT_ONCOLOGY_CLINIC"	,
        "HOSPITAL_OUTPATIENT_ONCOLOGY_CLINIC"	 : 	"HOSPITAL_OUTPATIENT_ONCOLOGY_CLINIC"	,
        "HOSPITAL_OUTPATIENT_OPHTHALMOLOGY_CLINIC"	 : 	"HOSPITAL_OUTPATIENT_OPHTHALMOLOGY_CLINIC"	,
        "HOSPITAL_OUTPATIENT_ORTHOPEDICS_CLINIC"	 : 	"HOSPITAL_OUTPATIENT_ORTHOPEDICS_CLINIC"	,
        "HOSPITAL_OUTPATIENT_PAIN_CLINIC"	 : 	"HOSPITAL_OUTPATIENT_PAIN_CLINIC"	,
        "HOSPITAL_OUTPATIENT_PEDIATRIC_CLINIC"	 : 	"HOSPITAL_OUTPATIENT_PEDIATRIC_CLINIC"	,
        "HOSPITAL_OUTPATIENT_PERIPHERAL_VASCULAR_CLINIC"	 : 	"HOSPITAL_OUTPATIENT_PERIPHERAL_VASCULAR_CLINIC"	,
        "HOSPITAL_OUTPATIENT_REHABILITATION_CLINIC"	 : 	"HOSPITAL_OUTPATIENT_REHABILITATION_CLINIC"	,
        "HOSPITAL_OUTPATIENT_REHABILITATION_CLINIC"	 : 	"HOSPITAL_OUTPATIENT_REHABILITATION_CLINIC"	,
        "HOSPITAL_OUTPATIENT_REHABILITATION_CLINIC"	 : 	"HOSPITAL_OUTPATIENT_REHABILITATION_CLINIC"	,
        "HOSPITAL_OUTPATIENT_REHABILITATION_CLINIC"	 : 	"HOSPITAL_OUTPATIENT_REHABILITATION_CLINIC"	,
        "HOSPITAL_OUTPATIENT_REHABILITATION_CLINIC"	 : 	"HOSPITAL_OUTPATIENT_REHABILITATION_CLINIC"	,
        "HOSPITAL_OUTPATIENT_RESPIRATORY_DISEASE_CLINIC"	 : 	"HOSPITAL_OUTPATIENT_RESPIRATORY_DISEASE_CLINIC"	,
        "HOSPITAL_OUTPATIENT_RHEUMATOLOGY_CLINIC"	 : 	"HOSPITAL_OUTPATIENT_RHEUMATOLOGY_CLINIC"	,
        "HOSPITAL_OUTPATIENT_UROLOGY_CLINIC"	 : 	"HOSPITAL_OUTPATIENT_UROLOGY_CLINIC"	,
        "HOSPITAL_RADIOLOGY_FACILITY"	 : 	"HOSPITAL_RADIOLOGY_FACILITY"	,
        "HOSPITAL_RADIOLOGY_FACILITY"	 : 	"HOSPITAL_RADIOLOGY_FACILITY"	,
        "HOSPITAL_RADIOLOGY_FACILITY"	 : 	"HOSPITAL_RADIOLOGY_FACILITY"	,
        "HOSPITAL_RADIOLOGY_FACILITY"	 : 	"HOSPITAL_RADIOLOGY_FACILITY"	,
        "HOSPITAL_RADIOLOGY_FACILITY"	 : 	"HOSPITAL_RADIOLOGY_FACILITY"	,
        "HOSPITAL_SHIP"	 : 	"HOSPITAL_SHIP"	,
        "INDEPENDENT_AMBULATORY_CARE_PROVIDER_SITE_OTHER"	 : 	"INDEPENDENT_AMBULATORY_CARE_PROVIDER_SITE_OTHER"	,
        "LOCAL_COMMUNITY_HEALTH_CENTER"	 : 	"LOCAL_COMMUNITY_HEALTH_CENTER"	,
        "NURSING_HOME"	 : 	"NURSING_HOME"	,
        "PRIVATE_PHYSICIANS_GROUP_OFFICE"	 : 	"PRIVATE_PHYSICIANS_GROUP_OFFICE"	,
        "PRIVATE_RESIDENTIAL_HOME"	 : 	"PRIVATE_RESIDENTIAL_HOME"	,
        "PSYCHOGERIATRIC_DAY_HOSPITAL"	 : 	"PSYCHOGERIATRIC_DAY_HOSPITAL"	,
        "RESIDENTIAL_INSTITUTION"	 : 	"RESIDENTIAL_INSTITUTION"	,
        "RESIDENTIAL_SCHOOL_INFIRMARY"	 : 	"RESIDENTIAL_SCHOOL_INFIRMARY"	,
        "RURAL_HEALTH_CENTER"	 : 	"RURAL_HEALTH_CENTER"	,
        "SEXUALLY_TRANSMITTED_DISEASE_HEALTH_CENTER"	 : 	"SEXUALLY_TRANSMITTED_DISEASE_HEALTH_CENTER"	,
        "SKILLED_NURSING_FACILITY"	 : 	"SKILLED_NURSING_FACILITY"	,
        "SOLO_PRACTICE_PRIVATE_OFFICE"	 : 	"SOLO_PRACTICE_PRIVATE_OFFICE"	,
        "SPORTS_FACILITY"	 : 	"SPORTS_FACILITY"	,
        "SUBSTANCE_ABUSE_TREATMENT_CENTER"	 : 	"SUBSTANCE_ABUSE_TREATMENT_CENTER"	,
        "TRAVELERS_AID_CLINIC"	 : 	"TRAVELERS_AID_CLINIC"	,
        "VACCINATION_CLINIC"	 : 	"VACCINATION_CLINIC"	,
        "WALK_IN_CLINIC"	 : 	"WALK_IN_CLINIC"	,


        "NI"	 : 	"NI"	,
        "UN"	 : 	"UN"	,
        "OT"	 : 	"OT"	,
        ""       :  "OT"    ,

}


# ▓█████ ███▄    █ ██▀███  ▒█████  ██▓    ██▓    ███▄ ▄███▓█████ ███▄    █▄▄▄█████▓
# ▓█   ▀ ██ ▀█   █▓██ ▒ ██▒██▒  ██▓██▒   ▓██▒   ▓██▒▀█▀ ██▓█   ▀ ██ ▀█   █▓  ██▒ ▓▒
# ▒███  ▓██  ▀█ ██▓██ ░▄█ ▒██░  ██▒██░   ▒██░   ▓██    ▓██▒███  ▓██  ▀█ ██▒ ▓██░ ▒░
# ▒▓█  ▄▓██▒  ▐▌██▒██▀▀█▄ ▒██   ██▒██░   ▒██░   ▒██    ▒██▒▓█  ▄▓██▒  ▐▌██░ ▓██▓ ░ 
# ░▒████▒██░   ▓██░██▓ ▒██░ ████▓▒░██████░██████▒██▒   ░██░▒████▒██░   ▓██░ ▒██▒ ░ 
# ░░ ▒░ ░ ▒░   ▒ ▒░ ▒▓ ░▒▓░ ▒░▒░▒░░ ▒░▓  ░ ▒░▓  ░ ▒░   ░  ░░ ▒░ ░ ▒░   ▒ ▒  ▒ ░░   
#  ░ ░  ░ ░░   ░ ▒░ ░▒ ░ ▒░ ░ ▒ ▒░░ ░ ▒  ░ ░ ▒  ░  ░      ░░ ░  ░ ░░   ░ ▒░   ░    
#    ░     ░   ░ ░  ░░   ░░ ░ ░ ▒   ░ ░    ░ ░  ░      ░     ░     ░   ░ ░  ░      
#    ░  ░        ░   ░        ░ ░     ░  ░   ░  ░      ░     ░  ░        ░         
                                                                                 

enrollment_chart_dict = {

            "YES":"Y",
            "NO" :"N",


}



enrollment_enr_basis_dict = {


        "MEDICAL INSURANCE COVERAGE"                 :"I",
        "OUTPATIENT PRESCRIPTION DRUG COVERAGE"      :"D",
        "GEOGRAPHY"                                  :"G",
        "ALGORITHMIC"                                :"A",
        "ENCOUNTER BASE"                             :"E",
        "ENCOUNTER-BASED"                            :"E",

    
}

# ▓█████▄▓█████▄▄▄    ▄▄▄█████▓██░ ██ 
# ▒██▀ ██▓█   ▒████▄  ▓  ██▒ ▓▓██░ ██▒
# ░██   █▒███ ▒██  ▀█▄▒ ▓██░ ▒▒██▀▀██░
# ░▓█▄   ▒▓█  ░██▄▄▄▄█░ ▓██▓ ░░▓█ ░██ 
# ░▒████▓░▒████▓█   ▓██▒▒██▒ ░░▓█▒░██▓
#  ▒▒▓  ▒░░ ▒░ ▒▒   ▓▒█░▒ ░░   ▒ ░░▒░▒
#  ░ ▒  ▒ ░ ░  ░▒   ▒▒ ░  ░    ▒ ░▒░ ░
#  ░ ░  ░   ░   ░   ▒   ░      ░  ░░ ░
#    ░      ░  ░    ░  ░       ░  ░  ░
#  ░                                  


death_death_date_impute_dict = {

                
                "NOT IMPUTE":"N", # Not imputed
                "BOTH MONTH AND DAY IMPUTED":"B", # Both month and day imputed    
                "OTHER":"OT", # Other
                "":"OT", # Other
                "OT":"OT", # Other

}


death_death_source_dict = {

"L":"L",
"":""


}


death_death_match_confidence_dict = {

"":""


}

#  ▄████▄  ▒█████  ███▄    █▓█████▄ ██▄▄▄█████▓██▓▒█████  ███▄    █ 
# ▒██▀ ▀█ ▒██▒  ██▒██ ▀█   █▒██▀ ██▓██▓  ██▒ ▓▓██▒██▒  ██▒██ ▀█   █ 
# ▒▓█    ▄▒██░  ██▓██  ▀█ ██░██   █▒██▒ ▓██░ ▒▒██▒██░  ██▓██  ▀█ ██▒
# ▒▓▓▄ ▄██▒██   ██▓██▒  ▐▌██░▓█▄   ░██░ ▓██▓ ░░██▒██   ██▓██▒  ▐▌██▒
# ▒ ▓███▀ ░ ████▓▒▒██░   ▓██░▒████▓░██░ ▒██▒ ░░██░ ████▓▒▒██░   ▓██░
# ░ ░▒ ▒  ░ ▒░▒░▒░░ ▒░   ▒ ▒ ▒▒▓  ▒░▓   ▒ ░░  ░▓ ░ ▒░▒░▒░░ ▒░   ▒ ▒ 
#   ░  ▒    ░ ▒ ▒░░ ░░   ░ ▒░░ ▒  ▒ ▒ ░   ░    ▒ ░ ░ ▒ ▒░░ ░░   ░ ▒░
# ░       ░ ░ ░ ▒    ░   ░ ░ ░ ░  ░ ▒ ░ ░      ▒ ░ ░ ░ ▒    ░   ░ ░ 
# ░ ░         ░ ░          ░   ░    ░          ░     ░ ░          ░ 
# ░                          ░                                      



condition_condition_status_dict = {

    "AC":"AC",
    "RS":"RS",

}


condition_condition_type_dict = {

    "ICD9CM":"09",
    "ICD9":"09",
    "ICD-9-CM":"09",
    "ICD10":"10",
    "ICD10CM":"10",
    "ICD-10-CM":"10",
    "ICD11CM":"11",
    "ICD-11-CM":"11",
    "HUMAN PHENOTYPE ONTOLOGY":"HP",
    "ALGORITHMIC":"AG",
    "SNOMED":"SM",
    "": "NI"

}


condition_condition_source_dict = {

"HC":"HC"

}

# ▓█████▄ ██▓▄▄▄       ▄████ ███▄    █ ▒█████   ██████ ██▓ ██████ 
# ▒██▀ ██▓██▒████▄    ██▒ ▀█▒██ ▀█   █▒██▒  ██▒██    ▒▓██▒██    ▒ 
# ░██   █▒██▒██  ▀█▄ ▒██░▄▄▄▓██  ▀█ ██▒██░  ██░ ▓██▄  ▒██░ ▓██▄   
# ░▓█▄   ░██░██▄▄▄▄██░▓█  ██▓██▒  ▐▌██▒██   ██░ ▒   ██░██░ ▒   ██▒
# ░▒████▓░██░▓█   ▓██░▒▓███▀▒██░   ▓██░ ████▓▒▒██████▒░██▒██████▒▒
#  ▒▒▓  ▒░▓  ▒▒   ▓▒█░░▒   ▒░ ▒░   ▒ ▒░ ▒░▒░▒░▒ ▒▓▒ ▒ ░▓ ▒ ▒▓▒ ▒ ░
#  ░ ▒  ▒ ▒ ░ ▒   ▒▒ ░ ░   ░░ ░░   ░ ▒░ ░ ▒ ▒░░ ░▒  ░ ░▒ ░ ░▒  ░ ░
#  ░ ░  ░ ▒ ░ ░   ▒  ░ ░   ░   ░   ░ ░░ ░ ░ ▒ ░  ░  ░  ▒ ░  ░  ░  
#    ░    ░       ░  ░     ░         ░    ░ ░       ░  ░       ░  
#  ░                                                              


diagnosis_enc_type_dict = {

            ""           : "OT", # Other 
            "EMERGENCY ROOM AND INPATIENT" : "EI", # Emergency Department Admit to Inpatient Hospital Stay
            "INPATIENT"                    : "IP", # Inpatient Hospital Stay
            "EMERGENCY ROOM"               : "ED", # Emergency Department
            "OUTPATIENT"                   : "AV", # Outpatient Visit - Non Physician
            "INPATIENT VISIT"              : "IP", # Inpatient Hospital Stay
            "OUTPATIENT VISIT"             : "AV", # Outpatient Visit - Non Physician
            "OFFICE VISIT"                 : "AV", # Outpatient Visit - Non Physician
            "TELEHEALTH"                   : "TH", # Telehealth
            "OBSERVATION VISIT"            : "OS", # 
            "LABORATORY VISIT"             : "OA", # 
            "REHABILITATION VISIT"         : "IS", # 
            "EMERGENCY ROOM VISIT"         : "ED", # Emergency Department
            "LABORATORY"                   : "OA", # Laboratory Visit
            "INTENSIVE CARE"               : "IP", # Intensive Care
            "PHARMACY"                     : "OA", # Pharmacy visit
            "HOME"                         : "OA", # Home Visit
            "OFFICE"                       : "AV", # Office Visit
            "AMBULANCE"                    : "ED", # Ambulatory Visit
            "REHABILITATION"               : "IS", # Rehabilitation Visit
            "LONG TERM CARE"               : "IS", # Long Term Care Visit
            "UNKNOWN"                      : "UN", # Unknown
            "OTHER"                        : "OT", # Other
            "NO INFORMATION"               : "NI", # No information 

}




diagnosis_dx_type_dict = {

    "ICD9CM":"09",
    "ICD9":"09",
    "ICD-9-CM":"09",
    "ICD10":"10",
    "ICD10CM":"10",
    "ICD-10-CM":"10",
    "ICD11CM":"11",
    "ICD-11-CM":"11",
    "HUMAN PHENOTYPE ONTOLOGY":"HP",
    "ALGORITHMIC":"AG",
    "SNOMED":"SM",
    "": "NI"

}


diagnosis_dx_source_dict = {

            
            "FINAL DIAGNOISIS":"FI", # Final
            "FINAL":"FI",
            "ADMITTING":"AD",
            "DISCHARGE":"DI",
            "INTERIM":"IN",
            "":"NI", # Other
}


diagnosis_dx_origin_dict = {

    "OD":"OD",

}

diagnosis_pdx_dict = {



             "":"NI", # NO INFORMATION
            "SECONDARY CONDITION":"S", # SECONDARY
            "PRIMARY CONDITION":"P", # PRINCIPAL
            "BILLING DIAGNOSIS^SECONDARY":"S", # SECONDARY
            "BILLING DIAGNOSIS^PRIMARY":"P", # PRINCIPAL
}

diagnosis_dx_poa_dict = {

        "NO INFORMATION": "NI",
        "":"NI",
        "DIAGNOSIS PRESENT":"Y",
        "DIAGNOSIS NOT PRESENT":"N",
        "INSUFFICIENT DOCUMENTATION":"U",
        "CLINICALLY UNDETERMINED":"W",
        "UNREPORTED / NOT USED":"1",


}

#  ██▓███  ██▀███  ▒█████  ▄████▄ ▓█████▓█████▄ █    ██ ██▀███ ▓█████  ██████ 
# ▓██░  ██▓██ ▒ ██▒██▒  ██▒██▀ ▀█ ▓█   ▀▒██▀ ██▌██  ▓██▓██ ▒ ██▓█   ▀▒██    ▒ 
# ▓██░ ██▓▓██ ░▄█ ▒██░  ██▒▓█    ▄▒███  ░██   █▓██  ▒██▓██ ░▄█ ▒███  ░ ▓██▄   
# ▒██▄█▓▒ ▒██▀▀█▄ ▒██   ██▒▓▓▄ ▄██▒▓█  ▄░▓█▄   ▓▓█  ░██▒██▀▀█▄ ▒▓█  ▄  ▒   ██▒
# ▒██▒ ░  ░██▓ ▒██░ ████▓▒▒ ▓███▀ ░▒████░▒████▓▒▒█████▓░██▓ ▒██░▒████▒██████▒▒
# ▒▓▒░ ░  ░ ▒▓ ░▒▓░ ▒░▒░▒░░ ░▒ ▒  ░░ ▒░ ░▒▒▓  ▒░▒▓▒ ▒ ▒░ ▒▓ ░▒▓░░ ▒░ ▒ ▒▓▒ ▒ ░
# ░▒ ░      ░▒ ░ ▒░ ░ ▒ ▒░  ░  ▒   ░ ░  ░░ ▒  ▒░░▒░ ░ ░  ░▒ ░ ▒░░ ░  ░ ░▒  ░ ░
# ░░        ░░   ░░ ░ ░ ▒ ░          ░   ░ ░  ░ ░░░ ░ ░  ░░   ░   ░  ░  ░  ░  
#            ░        ░ ░ ░ ░        ░  ░  ░      ░       ░       ░  ░     ░  
#                         ░              ░                                    

procedures_enc_type_dict = {

            ""                             : "OT", # Other 
            "EMERGENCY ROOM AND INPATIENT" : "EI", # Emergency Department Admit to Inpatient Hospital Stay
            "INPATIENT"                    : "IP", # Inpatient Hospital Stay
            "EMERGENCY ROOM"               : "ED", # Emergency Department
            "OUTPATIENT"                   : "AV", # Outpatient Visit - Non Physician
            "INPATIENT VISIT"              : "IP", # Inpatient Hospital Stay
            "OUTPATIENT VISIT"             : "AV", # Outpatient Visit - Non Physician
            "OFFICE VISIT"                 : "AV", # Outpatient Visit - Non Physician
            "TELEHEALTH"                   : "TH", # Telehealth
            "OBSERVATION VISIT"            : "OS", # 
            "LABORATORY VISIT"             : "OA", # 
            "REHABILITATION VISIT"         : "IS", # 
            "EMERGENCY ROOM VISIT"         : "ED", # Emergency Department
            "LABORATORY"                   : "OA", # Laboratory Visit
            "INTENSIVE CARE"               : "IP", # Intensive Care
            "PHARMACY"                     : "OA", # Pharmacy visit
            "HOME"                         : "OA", # Home Visit
            "OFFICE"                       : "AV", # Office Visit
            "AMBULANCE"                    : "ED", # Ambulatory Visit
            "REHABILITATION"               : "IS", # Rehabilitation Visit
            "LONG TERM CARE"               : "IS", # Long Term Care Visit
            "UNKNOWN"                      : "UN", # Unknown
            "OTHER"                        : "OT", # Other
            "NO INFORMATION"               : "NI", # No information 
}


procedures_px_type_dict = {

    "ICD9CM":"09",
    "ICD9":"09",
    "ICD-9-CM":"09",
    "ICD10":"10",
    "ICD10CM":"10",
    "ICD-10-CM":"10",
    "ICD10PCS":"10",
    "ICD11CM":"11",
    "ICD-11-CM":"11",
    "LOINC":"LC",
    "NDC":"ND",
    "CPT4":"CH",
    "HCPCS":"CH",
    "NDC":"CH",
    "REVENUE":"RE",
    "SNOMED":"SM",
    "": "NI"

}


procedures_px_source_dict = {

    "OD":"OD",

}


procedures_ppx_dict = {



             "":"NI", # NO INFORMATION
            "SECONDARY CONDITION":"S", # SECONDARY
            "PRIMARY CONDITION":"P", # PRINCIPAL
            "BILLING DIAGNOSIS^SECONDARY":"S", # SECONDARY
            "BILLING DIAGNOSIS^PRIMARY":"P", # PRINCIPAL
}

#  ██▓███  ██▀███  ▒█████  ██▒   █▓██▓█████▄▓█████ ██▀███  
# ▓██░  ██▓██ ▒ ██▒██▒  ██▓██░   █▓██▒██▀ ██▓█   ▀▓██ ▒ ██▒
# ▓██░ ██▓▓██ ░▄█ ▒██░  ██▒▓██  █▒▒██░██   █▒███  ▓██ ░▄█ ▒
# ▒██▄█▓▒ ▒██▀▀█▄ ▒██   ██░ ▒██ █░░██░▓█▄   ▒▓█  ▄▒██▀▀█▄  
# ▒██▒ ░  ░██▓ ▒██░ ████▓▒░  ▒▀█░ ░██░▒████▓░▒████░██▓ ▒██▒
# ▒▓▒░ ░  ░ ▒▓ ░▒▓░ ▒░▒░▒░   ░ ▐░ ░▓  ▒▒▓  ▒░░ ▒░ ░ ▒▓ ░▒▓░
# ░▒ ░      ░▒ ░ ▒░ ░ ▒ ▒░   ░ ░░  ▒ ░░ ▒  ▒ ░ ░  ░ ░▒ ░ ▒░
# ░░        ░░   ░░ ░ ░ ▒      ░░  ▒ ░░ ░  ░   ░    ░░   ░ 
#            ░        ░ ░       ░  ░    ░      ░  ░  ░     
#                              ░      ░                    


provider_provider_sex_dict = {
            "0":"OT",
            "8507":"M",
            "8521":"OT",
            "8532":"F",
            "8570":"A",
            "F":"F",
            "FEMALE":"F",
            "M":"M",
            "MALE":"M",
            "OTHER":"OT", # GENDER UNKNOWN
            "PREFER NOT TO ANSWER":"NI", # GENDER UNSPECIFIED
            "SKIP":"NI", # GENDER UNSPECIFIED
            "AMBIGUOUS":"A",
            "UNKNOWN":"UN",
            "":"OT",
        }
        

provider_provider_npi_flag_dict = {

    "Y":"Y",
    "N":"N",
}



provider_provider_specialty_primary_dict = {
             "ACUPUNCTURIST":"171100000X",
            "ADULT COMPANION":"372600000X",
            "ADVANCED PRACTICE DENTAL THERAPIST":"125K00000X",
            "ADVANCED PRACTICE MIDWIFE":"367A00000X",
            "AIR CARRIER ":"344800000X",
            "ALLERGY & IMMUNOLOGY ":"207K00000X",
            "ALLERGY & IMMUNOLOGY ALLERGY":"207KA0200X",
            "ALLERGY & IMMUNOLOGY CLINICAL & LABORATORY IMMUNOLOGY":"207KI0005X",
            "ALZHEIMER CENTER (DEMENTIA CENTER) ":"311500000X",
            "AMBULANCE ":"341600000X",
            "AMBULANCE AIR TRANSPORT":"3416A0800X",
            "AMBULANCE LAND TRANSPORT":"3416L0300X",
            "AMBULANCE WATER TRANSPORT":"3416S0300X",
            "ANAPLASTOLOGIST ":"229N00000X",
            "ANESTHESIOLOGIST ASSISTANT ":"367H00000X",
            "ANESTHESIOLOGY ":"207L00000X",
            "ANESTHESIOLOGY ADDICTION MEDICINE":"207LA0401X",
            "ANESTHESIOLOGY CRITICAL CARE MEDICINE":"207LC0200X",
            "ANESTHESIOLOGY HOSPICE AND PALLIATIVE MEDICINE":"207LH0002X",
            "ANESTHESIOLOGY PAIN MEDICINE":"207LP2900X",
            "ANESTHESIOLOGY PEDIATRIC ANESTHESIOLOGY":"207LP3000X",
            "ART THERAPIST ":"221700000X",
            "ASSISTANT BEHAVIOR ANALYST ":"106E00000X",
            "ASSISTANT PODIATRIC ":"211D00000X",
            "ASSISTED LIVING FACILITY ":"310400000X",
            "ASSISTED LIVING FACILITY ASSISTED LIVING BEHAVIORAL DISTURBANCES":"3104A0630X",
            "ASSISTED LIVING FACILITY ASSISTED LIVING MENTAL ILLNESS":"3104A0625X",
            "AUDIOLOGIST ":"231H00000X",
            "AUDIOLOGIST ASSISTIVE TECHNOLOGY PRACTITIONER":"231HA2400X",
            "AUDIOLOGIST ASSISTIVE TECHNOLOGY SUPPLIER":"231HA2500X",
            "AUDIOLOGIST-HEARING AID FITTER ":"237600000X",
            "BEHAVIOR TECHNICIAN ":"106S00000X",
            "BEHAVIORAL ANALYST ":"103K00000X",
            "BLOOD BANK ":"331L00000X",
            "BUS ":"347B00000X",
            "CASE MANAGEMENT ":"251B00000X",
            "CASE MANAGER/CARE COORDINATOR ":"171M00000X",
            "CHIROPRACTOR ":"111N00000X",
            "CHIROPRACTOR INDEPENDENT MEDICAL EXAMINER":"111NI0013X",
            "CHIROPRACTOR INTERNIST":"111NI0900X",
            "CHIROPRACTOR NEUROLOGY":"111NN0400X",
            "CHIROPRACTOR NUTRITION":"111NN1001X",
            "CHIROPRACTOR OCCUPATIONAL HEALTH":"111NX0100X",
            "CHIROPRACTOR ORTHOPEDIC":"111NX0800X",
            "CHIROPRACTOR PEDIATRIC CHIROPRACTOR":"111NP0017X",
            "CHIROPRACTOR RADIOLOGY":"111NR0200X",
            "CHIROPRACTOR REHABILITATION":"111NR0400X",
            "CHIROPRACTOR SPORTS PHYSICIAN":"111NS0005X",
            "CHIROPRACTOR THERMOGRAPHY":"111NT0100X",
            "CHORE PROVIDER ":"372500000X",
            "CHRISTIAN SCIENCE FACILITY ":"317400000X",
            "CHRISTIAN SCIENCE SANITORIUM ":"287300000X",
            "CHRONIC DISEASE HOSPITAL ":"281P00000X",
            "CHRONIC DISEASE HOSPITAL CHILDREN":"281PC2000X",
            "CLINIC/CENTER ":"261Q00000X",
            "CLINIC/CENTER ADOLESCENT AND CHILDREN MENTAL HEALTH":"261QM0855X",
            "CLINIC/CENTER ADULT DAY CARE":"261QA0600X",
            "CLINIC/CENTER ADULT MENTAL HEALTH":"261QM0850X",
            "CLINIC/CENTER AMBULATORY FAMILY PLANNING FACILITY":"261QA0005X",
            "CLINIC/CENTER AMBULATORY FERTILITY FACILITY":"261QA0006X",
            "CLINIC/CENTER AMBULATORY SURGICAL":"261QA1903X",
            "CLINIC/CENTER AMPUTEE":"261QA0900X",
            "CLINIC/CENTER AUGMENTATIVE COMMUNICATION":"261QA3000X",
            "CLINIC/CENTER BIRTHING":"261QB0400X",
            "CLINIC/CENTER COMMUNITY HEALTH":"261QC1500X",
            "CLINIC/CENTER CORPORATE HEALTH":"261QC1800X",
            "CLINIC/CENTER CRITICAL ACCESS HOSPITAL":"261QC0050X",
            "CLINIC/CENTER DENTAL":"261QD0000X",
            "CLINIC/CENTER DEVELOPMENTAL DISABILITIES":"261QD1600X",
            "CLINIC/CENTER EMERGENCY CARE":"261QE0002X",
            "CLINIC/CENTER END-STAGE RENAL DISEASE (ESRD) TREATMENT":"261QE0700X",
            "CLINIC/CENTER ENDOSCOPY":"261QE0800X",
            "CLINIC/CENTER FAMILY PLANNING NON-SURGICAL":"261QF0050X",
            "CLINIC/CENTER FEDERALLY QUALIFIED HEALTH CENTER (FQHC)":"261QF0400X",
            "CLINIC/CENTER GENETICS":"261QG0250X",
            "CLINIC/CENTER HEALTH SERVICE":"261QH0100X",
            "CLINIC/CENTER HEARING AND SPEECH":"261QH0700X",
            "CLINIC/CENTER INFUSION THERAPY":"261QI0500X",
            "CLINIC/CENTER LITHOTRIPSY":"261QL0400X",
            "CLINIC/CENTER MAGNETIC RESONANCE IMAGING (MRI)":"261QM1200X",
            "CLINIC/CENTER MEDICAL SPECIALTY":"261QM2500X",
            "CLINIC/CENTER MEDICALLY FRAGILE INTANTS AND CHILDREN DAY CARE":"261QM3000X",
            "CLINIC/CENTER MENTAL HEALTH (INCLUDING COMMUNITY MENTAL HEALTH CENTER)":"261QM0801X",
            "CLINIC/CENTER METHADONE CLINIC":"261QM2800X",
            "CLINIC/CENTER MIGRANT HEALTH":"261QM1000X",
            "CLINIC/CENTER MILITARY AMBULATORY PROCEDURE VISITS OPERATIONAL (TRANSPORTABLE)":"261QM1103X",
            "CLINIC/CENTER MILITARY AND U.S. COAST GUARD AMBULATORY PROCEDURE":"261QM1101X",
            "CLINIC/CENTER MILITARY OUTPATIENT OPERATIONAL (TRANSPORTABLE) COMPONENT":"261QM1102X",
            "CLINIC/CENTER MILITARY/U.S. COAST GUARD OUTPATIENT":"261QM1100X",
            "CLINIC/CENTER MULTI-SPECIALTY":"261QM1300X",
            "CLINIC/CENTER OCCUPATIONAL MEDICINE":"261QX0100X",
            "CLINIC/CENTER ONCOLOGY":"261QX0200X",
            "CLINIC/CENTER ONCOLOGY RADIATION":"261QX0203X",
            "CLINIC/CENTER OPHTHALMOLOGIC SURGERY":"261QS0132X",
            "CLINIC/CENTER ORAL AND MAXILLOFACIAL SURGERY":"261QS0112X",
            "CLINIC/CENTER PAIN":"261QP3300X",
            "CLINIC/CENTER PHYSICAL THERAPY":"261QP2000X",
            "CLINIC/CENTER PODIATRIC":"261QP1100X",
            "CLINIC/CENTER PRIMARY CARE":"261QP2300X",
            "CLINIC/CENTER PRISON HEALTH":"261QP2400X",
            "CLINIC/CENTER PUBLIC HEALTH FEDERAL":"261QP0904X",
            "CLINIC/CENTER PUBLIC HEALTH STATE OR LOCAL":"261QP0905X",
            "CLINIC/CENTER RADIOLOGY":"261QR0200X",
            "CLINIC/CENTER RADIOLOGY MAMMOGRAPHY":"261QR0206X",
            "CLINIC/CENTER RADIOLOGY MOBILE":"261QR0208X",
            "CLINIC/CENTER RADIOLOGY MOBILE MAMMOGRAPHY":"261QR0207X",
            "CLINIC/CENTER RECOVERY CARE":"261QR0800X",
            "CLINIC/CENTER REHABILITATION":"261QR0400X",
            "CLINIC/CENTER REHABILITATION CARDIAC FACILITIES":"261QR0404X",
            "CLINIC/CENTER REHABILITATION COMPREHENSIVE OUTPATIENT REHABILITATION FACILITY (CORF)":"261QR0401X",
            "CLINIC/CENTER REHABILITATION SUBSTANCE USE DISORDER":"261QR0405X",
            "CLINIC/CENTER RESEARCH":"261QR1100X",
            "CLINIC/CENTER RURAL HEALTH":"261QR1300X",
            "CLINIC/CENTER SLEEP DISORDER DIAGNOSTIC":"261QS1200X",
            "CLINIC/CENTER STUDENT HEALTH":"261QS1000X",
            "CLINIC/CENTER URGENT CARE":"261QU0200X",
            "CLINIC/CENTER VA":"261QV0200X",
            "CLINICAL ETHICIST ":"174V00000X",
            "CLINICAL EXERCISE PHYSIOLOGIST ":"224Y00000X",
            "CLINICAL MEDICAL LABORATORY ":"291U00000X",
            "CLINICAL NEUROPSYCHOLOGIST ":"103G00000X",
            "CLINICAL NEUROPSYCHOLOGIST CLINICAL":"103GC0700X",
            "CLINICAL NURSE SPECIALIST ":"364S00000X",
            "CLINICAL NURSE SPECIALIST ACUTE CARE":"364SA2100X",
            "CLINICAL NURSE SPECIALIST ADULT HEALTH":"364SA2200X",
            "CLINICAL NURSE SPECIALIST CHRONIC CARE":"364SC2300X",
            "CLINICAL NURSE SPECIALIST COMMUNITY HEALTH/PUBLIC HEALTH":"364SC1501X",
            "CLINICAL NURSE SPECIALIST CRITICAL CARE MEDICINE":"364SC0200X",
            "CLINICAL NURSE SPECIALIST EMERGENCY":"364SE0003X",
            "CLINICAL NURSE SPECIALIST ETHICS":"364SE1400X",
            "CLINICAL NURSE SPECIALIST FAMILY HEALTH":"364SF0001X",
            "CLINICAL NURSE SPECIALIST GERONTOLOGY":"364SG0600X",
            "CLINICAL NURSE SPECIALIST HOLISTIC":"364SH1100X",
            "CLINICAL NURSE SPECIALIST HOME HEALTH":"364SH0200X",
            "CLINICAL NURSE SPECIALIST INFORMATICS":"364SI0800X",
            "CLINICAL NURSE SPECIALIST LONG-TERM CARE":"364SL0600X",
            "CLINICAL NURSE SPECIALIST MEDICAL-SURGICAL":"364SM0705X",
            "CLINICAL NURSE SPECIALIST NEONATAL":"364SN0000X",
            "CLINICAL NURSE SPECIALIST NEUROSCIENCE":"364SN0800X",
            "CLINICAL NURSE SPECIALIST OCCUPATIONAL HEALTH":"364SX0106X",
            "CLINICAL NURSE SPECIALIST ONCOLOGY":"364SX0200X",
            "CLINICAL NURSE SPECIALIST ONCOLOGY PEDIATRICS":"364SX0204X",
            "CLINICAL NURSE SPECIALIST PEDIATRICS":"364SP0200X",
            "CLINICAL NURSE SPECIALIST PERINATAL":"364SP1700X",
            "CLINICAL NURSE SPECIALIST PERIOPERATIVE":"364SP2800X",
            "CLINICAL NURSE SPECIALIST PSYCH/MENTAL HEALTH":"364SP0808X",
            "CLINICAL NURSE SPECIALIST PSYCH/MENTAL HEALTH ADULT":"364SP0809X",
            "CLINICAL NURSE SPECIALIST PSYCH/MENTAL HEALTH CHILD & ADOLESCENT":"364SP0807X",
            "CLINICAL NURSE SPECIALIST PSYCH/MENTAL HEALTH CHILD & FAMILY":"364SP0810X",
            "CLINICAL NURSE SPECIALIST PSYCH/MENTAL HEALTH CHRONICALLY ILL":"364SP0811X",
            "CLINICAL NURSE SPECIALIST PSYCH/MENTAL HEALTH COMMUNITY":"364SP0812X",
            "CLINICAL NURSE SPECIALIST PSYCH/MENTAL HEALTH GEROPSYCHIATRIC":"364SP0813X",
            "CLINICAL NURSE SPECIALIST REHABILITATION":"364SR0400X",
            "CLINICAL NURSE SPECIALIST SCHOOL":"364SS0200X",
            "CLINICAL NURSE SPECIALIST TRANSPLANTATION":"364ST0500X",
            "CLINICAL NURSE SPECIALIST WOMEN'S HEALTH":"364SW0102X",
            "CLINICAL PHARMACOLOGY ":"208U00000X",
            "COLON & RECTAL SURGERY ":"208C00000X",
            "COMMUNITY BASED RESIDENTIAL TREATMENT FACILITY MENTAL ILLNESS ":"320800000X",
            "COMMUNITY BASED RESIDENTIAL TREATMENT MENTAL RETARDATION AND/OR DEVELOPMENTAL DISABILITIES ":"320900000X",
            "COMMUNITY HEALTH WORKER ":"172V00000X",
            "COMMUNITY/BEHAVIORAL HEALTH ":"251S00000X",
            "CONTRACTOR ":"171W00000X",
            "CONTRACTOR HOME MODIFICATIONS":"171WH0202X",
            "CONTRACTOR VEHICLE MODIFICATIONS":"171WV0202X",
            "COUNSELOR":"101Y00000X",
            "COUNSELOR ADDICTION SUBSTANCE USE DISORDER":"101YA0400X",
            "COUNSELOR MENTAL HEALTH":"101YM0800X",
            "COUNSELOR PASTORAL":"101YP1600X",
            "COUNSELOR PROFESSIONAL":"101YP2500X",
            "COUNSELOR SCHOOL":"101YS0200X",
            "CUSTODIAL CARE FACILITY ":"311Z00000X",
            "CUSTODIAL CARE FACILITY ADULT CARE HOME":"311ZA0620X",
            "DANCE THERAPIST ":"225600000X",
            "DAY TRAINING DEVELOPMENTALLY DISABLED SERVICES ":"251C00000X",
            "DAY TRAINING/HABILITATION SPECIALIST ":"373H00000X",
            "DENTAL ASSISTANT ":"126800000X",
            "DENTAL HYGIENIST ":"124Q00000X",
            "DENTAL LABORATORY ":"292200000X",
            "DENTAL LABORATORY TECHNICIAN ":"126900000X",
            "DENTAL THERAPIST ":"125J00000X",
            "DENTIST ":"122300000X",
            "DENTIST DENTAL PUBLIC HEALTH":"1223D0001X",
            "DENTIST DENTIST ANESTHESIOLOGIST":"1223D0004X",
            "DENTIST ENDODONTICS":"1223E0200X",
            "DENTIST GENERAL PRACTICE":"1223G0001X",
            "DENTIST ORAL AND MAXILLOFACIAL PATHOLOGY":"1223P0106X",
            "DENTIST ORAL AND MAXILLOFACIAL RADIOLOGY":"1223X0008X",
            "DENTIST ORAL AND MAXILLOFACIAL SURGERY":"1223S0112X",
            "DENTIST ORTHODONTICS AND DENTOFACIAL ORTHOPEDICS":"1223X0400X",
            "DENTIST PEDIATRIC DENTISTRY":"1223P0221X",
            "DENTIST PERIODONTICS":"1223P0300X",
            "DENTIST PROSTHODONTICS":"1223P0700X",
            "DENTURIST ":"122400000X",
            "DEPARTMENT OF VETERANS AFFAIRS (VA) PHARMACY ":"332100000X",
            "DERMATOLOGY ":"207N00000X",
            "DERMATOLOGY CLINICAL & LABORATORY DERMATOLOGICAL IMMUNOLOGY":"207NI0002X",
            "DERMATOLOGY DERMATOPATHOLOGY":"207ND0900X",
            "DERMATOLOGY MOHS-MICROGRAPHIC SURGERY":"207ND0101X",
            "DERMATOLOGY PEDIATRIC DERMATOLOGY":"207NP0225X",
            "DERMATOLOGY PROCEDURAL DERMATOLOGY":"207NS0135X",
            "DEVELOPMENTAL THERAPIST ":"222Q00000X",
            "DIETARY MANAGER ":"132700000X",
            "DIETETIC TECHNICIAN REGISTERED ":"136A00000X",
            "DIETITIAN REGISTERED ":"133V00000X",
            "DIETITIAN REGISTERED NUTRITION METABOLIC":"133VN1006X",
            "DIETITIAN REGISTERED NUTRITION PEDIATRIC":"133VN1004X",
            "DIETITIAN REGISTERED NUTRITION RENAL":"133VN1005X",
            "DOULA ":"374J00000X",
            "DRIVER ":"172A00000X",
            "DURABLE MEDICAL EQUIPMENT & MEDICAL SUPPLIES ":"332B00000X",
            "DURABLE MEDICAL EQUIPMENT & MEDICAL SUPPLIES CUSTOMIZED EQUIPMENT":"332BC3200X",
            "DURABLE MEDICAL EQUIPMENT & MEDICAL SUPPLIES DIALYSIS EQUIPMENT & SUPPLIES":"332BD1200X",
            "DURABLE MEDICAL EQUIPMENT & MEDICAL SUPPLIES NURSING FACILITY SUPPLIES":"332BN1400X",
            "DURABLE MEDICAL EQUIPMENT & MEDICAL SUPPLIES OXYGEN EQUIPMENT & SUPPLIES":"332BX2000X",
            "DURABLE MEDICAL EQUIPMENT & MEDICAL SUPPLIES PARENTERAL & ENTERAL NUTRITION":"332BP3500X",
            "EARLY INTERVENTION PROVIDER AGENCY ":"252Y00000X",
            "ELECTRODIAGNOSTIC MEDICINE ":"204R00000X",
            "EMERGENCY MEDICAL TECHNICIAN BASIC ":"146N00000X",
            "EMERGENCY MEDICAL TECHNICIAN INTERMEDIATE ":"146M00000X",
            "EMERGENCY MEDICAL TECHNICIAN PARAMEDIC ":"146L00000X",
            "EMERGENCY MEDICINE ":"207P00000X",
            "EMERGENCY MEDICINE EMERGENCY MEDICAL SERVICES":"207PE0004X",
            "EMERGENCY MEDICINE HOSPICE AND PALLIATIVE MEDICINE":"207PH0002X",
            "EMERGENCY MEDICINE MEDICAL TOXICOLOGY":"207PT0002X",
            "EMERGENCY MEDICINE PEDIATRIC EMERGENCY MEDICINE":"207PP0204X",
            "EMERGENCY MEDICINE SPORTS MEDICINE":"207PS0010X",
            "EMERGENCY MEDICINE UNDERSEA AND HYPERBARIC MEDICINE":"207PE0005X",
            "EMERGENCY RESPONSE SYSTEM COMPANIES ":"333300000X",
            "EPILEPSY UNIT ":"273100000X",
            "EXCLUSIVE PROVIDER ORGANIZATION ":"302F00000X",
            "EYE BANK ":"332G00000X",
            "EYEWEAR SUPPLIER (EQUIPMENT NOT THE SERVICE) ":"332H00000X",
            "FAMILY MEDICINE ":"207Q00000X",
            "FAMILY MEDICINE ADDICTION MEDICINE":"207QA0401X",
            "FAMILY MEDICINE ADOLESCENT MEDICINE":"207QA0000X",
            "FAMILY MEDICINE ADULT MEDICINE":"207QA0505X",
            "FAMILY MEDICINE GERIATRIC MEDICINE":"207QG0300X",
            "FAMILY MEDICINE HOSPICE AND PALLIATIVE MEDICINE":"207QH0002X",
            "FAMILY MEDICINE OBESITY MEDICINE":"207QB0002X",
            "FAMILY MEDICINE SLEEP MEDICINE":"207QS1201X",
            "FAMILY MEDICINE SPORTS MEDICINE":"207QS0010X",
            "FOSTER CARE AGENCY ":"253J00000X",
            "FUNERAL DIRECTOR ":"176P00000X",
            "GENERAL ACUTE CARE HOSPITAL ":"282N00000X",
            "GENERAL ACUTE CARE HOSPITAL CHILDREN":"282NC2000X",
            "GENERAL ACUTE CARE HOSPITAL CRITICAL ACCESS":"282NC0060X",
            "GENERAL ACUTE CARE HOSPITAL RURAL":"282NR1301X",
            "GENERAL ACUTE CARE HOSPITAL WOMEN":"282NW0100X",
            "GENERAL PRACTICE ":"208D00000X",
            "GENETIC COUNSELOR MS ":"170300000X",
            "HEALTH EDUCATOR ":"174H00000X",
            "HEALTH MAINTENANCE ORGANIZATION ":"302R00000X",
            "HEARING  AID EQUIPMENT ":"332S00000X",
            "HEARING INSTRUMENT SPECIALIST ":"237700000X",
            "HOME DELIVERED MEALS ":"332U00000X",
            "HOME HEALTH ":"251E00000X",
            "HOME HEALTH AIDE ":"374U00000X",
            "HOME INFUSION ":"251F00000X",
            "HOMEMAKER ":"376J00000X",
            "HOMEOPATH ":"175L00000X",
            "HOSPICE CARE COMMUNITY BASED ":"251G00000X",
            "HOSPICE INPATIENT ":"315D00000X",
            "HOSPITALIST ":"208M00000X",
            "IN HOME SUPPORTIVE CARE ":"253Z00000X",
            "INDEPENDENT MEDICAL EXAMINER ":"202C00000X",
            "INDIAN HEALTH SERVICE/TRIBAL/URBAN INDIAN HEALTH (I/T/U) PHARMACY ":"332800000X",
            "INTERMEDIATE CARE FACILITY MENTAL ILLNESS ":"310500000X",
            "INTERMEDIATE CARE FACILITY MENTALLY RETARDED ":"315P00000X",
            "INTERNAL MEDICINE ":"207R00000X",
            "INTERNAL MEDICINE ADDICTION MEDICINE":"207RA0401X",
            "INTERNAL MEDICINE ADOLESCENT MEDICINE":"207RA0000X",
            "INTERNAL MEDICINE ADVANCED HEART FAILURE AND TRANSPLANT CARDIOLOGY":"207RA0001X",
            "INTERNAL MEDICINE ALLERGY & IMMUNOLOGY":"207RA0201X",
            "INTERNAL MEDICINE CARDIOVASCULAR DISEASE":"207RC0000X",
            "INTERNAL MEDICINE CLINICAL & LABORATORY IMMUNOLOGY":"207RI0001X",
            "INTERNAL MEDICINE CLINICAL CARDIAC ELECTROPHYSIOLOGY":"207RC0001X",
            "INTERNAL MEDICINE CRITICAL CARE MEDICINE":"207RC0200X",
            "INTERNAL MEDICINE ENDOCRINOLOGY DIABETES & METABOLISM":"207RE0101X",
            "INTERNAL MEDICINE GASTROENTEROLOGY":"207RG0100X",
            "INTERNAL MEDICINE GERIATRIC MEDICINE":"207RG0300X",
            "INTERNAL MEDICINE HEMATOLOGY":"207RH0000X",
            "INTERNAL MEDICINE HEMATOLOGY & ONCOLOGY":"207RH0003X",
            "INTERNAL MEDICINE HEPATOLOGY":"207RI0008X",
            "INTERNAL MEDICINE HOSPICE AND PALLIATIVE MEDICINE":"207RH0002X",
            "INTERNAL MEDICINE HYPERTENSION SPECIALIST":"207RH0005X",
            "INTERNAL MEDICINE INFECTIOUS DISEASE":"207RI0200X",
            "INTERNAL MEDICINE INTERVENTIONAL CARDIOLOGY":"207RI0011X",
            "INTERNAL MEDICINE MAGNETIC RESONANCE IMAGING (MRI)":"207RM1200X",
            "INTERNAL MEDICINE MEDICAL ONCOLOGY":"207RX0202X",
            "INTERNAL MEDICINE NEPHROLOGY":"207RN0300X",
            "INTERNAL MEDICINE OBESITY MEDICINE":"207RB0002X",
            "INTERNAL MEDICINE PULMONARY DISEASE":"207RP1001X",
            "INTERNAL MEDICINE RHEUMATOLOGY":"207RR0500X",
            "INTERNAL MEDICINE SLEEP MEDICINE":"207RS0012X",
            "INTERNAL MEDICINE SPORTS MEDICINE":"207RS0010X",
            "INTERNAL MEDICINE TRANSPLANT HEPATOLOGY":"207RT0003X",
            "INTERPRETER ":"171R00000X",
            "KINESIOTHERAPIST ":"226300000X",
            "LACTATION CONSULTANT NON-RN ":"174N00000X",
            "LEGAL MEDICINE ":"173000000X",
            "LEGAL MEDICINE ":"209800000X",
            "LICENSED PRACTICAL NURSE ":"164W00000X",
            "LICENSED PSYCHIATRIC TECHNICIAN ":"167G00000X",
            "LICENSED VOCATIONAL NURSE ":"164X00000X",
            "LOCAL EDUCATION AGENCY (LEA) ":"251300000X",
            "LODGING ":"177F00000X",
            "LONG TERM CARE HOSPITAL ":"282E00000X",
            "MARRIAGE & FAMILY THERAPIST ":"106H00000X",
            "MASSAGE THERAPIST ":"225700000X",
            "MASTECTOMY FITTER ":"224900000X",
            "MEALS ":"174200000X",
            "MECHANOTHERAPIST ":"172M00000X",
            "MEDICAL FOODS SUPPLIER ":"335G00000X",
            "MEDICAL GENETICS CLINICAL BIOCHEMICAL GENETICS":"207SG0202X",
            "MEDICAL GENETICS CLINICAL CYTOGENETIC":"207SC0300X",
            "MEDICAL GENETICS CLINICAL GENETICS (M.D.)":"207SG0201X",
            "MEDICAL GENETICS CLINICAL MOLECULAR GENETICS":"207SG0203X",
            "MEDICAL GENETICS MOLECULAR GENETIC PATHOLOGY":"207SM0001X",
            "MEDICAL GENETICS PH.D. MEDICAL GENETICS":"207SG0205X",
            "MEDICAL GENETICS PH.D. MEDICAL GENETICS ":"170100000X",
            "MEDICARE DEFINED SWING BED UNIT ":"275N00000X",
            "MIDWIFE ":"176B00000X",
            "MIDWIFE LAY ":"175M00000X",
            "MILITARY CLINICAL MEDICAL LABORATORY ":"291900000X",
            "MILITARY HEALTH CARE PROVIDER ":"171000000X",
            "MILITARY HEALTH CARE PROVIDER INDEPENDENT DUTY CORPSMAN":"1710I1002X",
            "MILITARY HEALTH CARE PROVIDER INDEPENDENT DUTY MEDICAL TECHNICIANS":"1710I1003X",
            "MILITARY HOSPITAL ":"286500000X",
            "MILITARY HOSPITAL COMMUNITY HEALTH":"2865C1500X",
            "MILITARY HOSPITAL MILITARY GENERAL ACUTE CARE HOSPITAL":"2865M2000X",
            "MILITARY HOSPITAL MILITARY GENERAL ACUTE CARE HOSPITAL. OPERATIONAL (TRANSPORTABLE)":"2865X1600X",
            "MILITARY/U.S. COAST GUARD PHARMACY ":"332000000X",
            "MILITARY/U.S. COAST GUARD TRANSPORT ":"341800000X",
            "MILITARY/U.S. COAST GUARD TRANSPORT MILITARY OR U.S. COAST GUARD AMBULANCE AIR TRANSPORT":"3418M1120X",
            "MILITARY/U.S. COAST GUARD TRANSPORT MILITARY OR U.S. COAST GUARD AMBULANCE GROUND TRANSPORT":"3418M1110X",
            "MILITARY/U.S. COAST GUARD TRANSPORT MILITARY OR U.S. COAST GUARD AMBULANCE WATER TRANSPORT":"3418M1130X",
            "MULTI-SPECIALTY ":"193200000X",
            "MUSIC THERAPIST ":"225A00000X",
            "NAPRAPATH ":"172P00000X",
            "NATUROPATH ":"175F00000X",
            "NEUROLOGICAL SURGERY ":"207T00000X",
            "NEUROMUSCULOSKELETAL MEDICINE & OMM ":"204D00000X",
            "NEUROMUSCULOSKELETAL MEDICINE SPORTS MEDICINE ":"204C00000X",
            "NO INFORMATION":"NI",
            "NON-EMERGENCY MEDICAL TRANSPORT (VAN) ":"343900000X",
            "NON-PHARMACY DISPENSING SITE ":"332900000X",
            "NUCLEAR MEDICINE ":"207U00000X",
            "NUCLEAR MEDICINE IN VIVO & IN VITRO NUCLEAR MEDICINE":"207UN0903X",
            "NUCLEAR MEDICINE NUCLEAR CARDIOLOGY":"207UN0901X",
            "NUCLEAR MEDICINE NUCLEAR IMAGING & THERAPY":"207UN0902X",
            "NURSE ANESTHETIST CERTIFIED REGISTERED ":"367500000X",
            "NURSE PRACTITIONER ":"363L00000X",
            "NURSE PRACTITIONER ACUTE CARE":"363LA2100X",
            "NURSE PRACTITIONER ADULT HEALTH":"363LA2200X",
            "NURSE PRACTITIONER COMMUNITY HEALTH":"363LC1500X",
            "NURSE PRACTITIONER CRITICAL CARE MEDICINE":"363LC0200X",
            "NURSE PRACTITIONER FAMILY":"363LF0000X",
            "NURSE PRACTITIONER GERONTOLOGY":"363LG0600X",
            "NURSE PRACTITIONER NEONATAL":"363LN0000X",
            "NURSE PRACTITIONER NEONATAL CRITICAL CARE":"363LN0005X",
            "NURSE PRACTITIONER OBSTETRICS & GYNECOLOGY":"363LX0001X",
            "NURSE PRACTITIONER OBSTETRICS & GYNECOLOGY":"363LX0001X",
            "NURSE PRACTITIONER OCCUPATIONAL HEALTH":"363LX0106X",
            "NURSE PRACTITIONER PEDIATRICS":"363LP0200X",
            "NURSE PRACTITIONER PEDIATRICS CRITICAL CARE":"363LP0222X",
            "NURSE PRACTITIONER PERINATAL":"363LP1700X",
            "NURSE PRACTITIONER PRIMARY CARE":"363LP2300X",
            "NURSE PRACTITIONER PSYCH/MENTAL HEALTH":"363LP0808X",
            "NURSE PRACTITIONER SCHOOL":"363LS0200X",
            "NURSE PRACTITIONER WOMEN'S HEALTH":"363LW0102X",
            "NURSE'S AIDE ":"376K00000X",
            "NURSING CARE ":"251J00000X",
            "NURSING FACILITY/INTERMEDIATE CARE FACILITY ":"313M00000X",
            "NURSING HOME ADMINISTRATOR ":"376G00000X",
            "NUTRITIONIST ":"133N00000X",
            "NUTRITIONIST NUTRITION EDUCATION":"133NN1002X",
            "OBSTETRICS & GYNECOLOGY ":"207V00000X",
            "OBSTETRICS & GYNECOLOGY ":"207V00000X",
            "OBSTETRICS & GYNECOLOGY CRITICAL CARE MEDICINE":"207VC0200X",
            "OBSTETRICS & GYNECOLOGY FEMALE PELVIC MEDICINE AND RECONSTRUCTIVE SURGERY":"207VF0040X",
            "OBSTETRICS & GYNECOLOGY GYNECOLOGIC ONCOLOGY":"207VX0201X",
            "OBSTETRICS & GYNECOLOGY GYNECOLOGY":"207VG0400X",
            "OBSTETRICS & GYNECOLOGY HOSPICE AND PALLIATIVE MEDICINE":"207VH0002X",
            "OBSTETRICS & GYNECOLOGY MATERNAL & FETAL MEDICINE":"207VM0101X",
            "OBSTETRICS & GYNECOLOGY OBESITY MEDICINE":"207VB0002X",
            "OBSTETRICS & GYNECOLOGY OBSTETRICS":"207VX0000X",
            "OBSTETRICS & GYNECOLOGY REPRODUCTIVE ENDOCRINOLOGY":"207VE0102X",
            "OCCUPATIONAL THERAPIST":"225X00000X",
            "OCCUPATIONAL THERAPIST DRIVING AND COMMUNITY MOBILITY":"225XR0403X",
            "OCCUPATIONAL THERAPIST ENVIRONMENTAL MODIFICATION":"225XE0001X",
            "OCCUPATIONAL THERAPIST ERGONOMICS":"225XE1200X",
            "OCCUPATIONAL THERAPIST FEEDING EATING & SWALLOWING":"225XF0002X",
            "OCCUPATIONAL THERAPIST GERONTOLOGY":"225XG0600X",
            "OCCUPATIONAL THERAPIST HAND":"225XH1200X",
            "OCCUPATIONAL THERAPIST HUMAN FACTORS":"225XH1300X",
            "OCCUPATIONAL THERAPIST LOW VISION":"225XL0004X",
            "OCCUPATIONAL THERAPIST MENTAL HEALTH":"225XM0800X",
            "OCCUPATIONAL THERAPIST NEUROREHABILITATION":"225XN1300X",
            "OCCUPATIONAL THERAPIST PEDIATRICS":"225XP0200X",
            "OCCUPATIONAL THERAPIST PHYSICAL REHABILITATION":"225XP0019X",
            "OCCUPATIONAL THERAPY ASSISTANT ":"224Z00000X",
            "OCCUPATIONAL THERAPY ASSISTANT DRIVING AND COMMUNITY MOBILITY":"224ZR0403X",
            "OCCUPATIONAL THERAPY ASSISTANT ENVIRONMENTAL MODIFICATION":"224ZE0001X",
            "OCCUPATIONAL THERAPY ASSISTANT FEEDING EATING & SWALLOWING":"224ZF0002X",
            "OCCUPATIONAL THERAPY ASSISTANT LOW VISION":"224ZL0004X",
            "OPHTHALMOLOGY ":"207W00000X",
            "OPHTHALMOLOGY GLAUCOMA SPECIALIST":"207WX0009X",
            "OPHTHALMOLOGY NEURO-OPHTHALMOLOGY":"207WX0109X",
            "OPHTHALMOLOGY OPHTHALMIC PLASTIC AND RECONSTRUCTIVE SURGERY":"207WX0200X",
            "OPHTHALMOLOGY PEDIATRIC OPHTHALMOLOGY AND STRABISMUS SPECIALIST":"207WX0110X",
            "OPHTHALMOLOGY RETINA SPECIALIST":"207WX0107X",
            "OPHTHALMOLOGY UVEITIS AND OCULAR INFLAMMATORY DISEASE":"207WX0108X",
            "OPTOMETRIST ":"152W00000X",
            "OPTOMETRIST CORNEAL AND CONTACT MANAGEMENT":"152WC0802X",
            "OPTOMETRIST LOW VISION REHABILITATION":"152WL0500X",
            "OPTOMETRIST OCCUPATIONAL VISION":"152WX0102X",
            "OPTOMETRIST PEDIATRICS":"152WP0200X",
            "OPTOMETRIST SPORTS VISION":"152WS0006X",
            "OPTOMETRIST VISION THERAPY":"152WV0400X",
            "ORAL & MAXILLOFACIAL SURGERY ":"204E00000X",
            "ORAL MEDICINIST ":"125Q00000X",
            "ORGAN PROCUREMENT ORGANIZATION ":"335U00000X",
            "ORTHOPAEDIC SURGERY ":"207X00000X",
            "ORTHOPAEDIC SURGERY ADULT RECONSTRUCTIVE ORTHOPAEDIC SURGERY":"207XS0114X",
            "ORTHOPAEDIC SURGERY FOOT AND ANKLE SURGERY":"207XX0004X",
            "ORTHOPAEDIC SURGERY HAND SURGERY":"207XS0106X",
            "ORTHOPAEDIC SURGERY ORTHOPAEDIC SURGERY OF THE SPINE":"207XS0117X",
            "ORTHOPAEDIC SURGERY ORTHOPAEDIC TRAUMA":"207XX0801X",
            "ORTHOPAEDIC SURGERY PEDIATRIC ORTHOPAEDIC SURGERY":"207XP3100X",
            "ORTHOPAEDIC SURGERY SPORTS MEDICINE":"207XX0005X",
            "ORTHOTIC FITTER ":"225000000X",
            "ORTHOTIST ":"222Z00000X",
            "OTHER":"OT",
            "OTOLARYNGOLOGY ":"207Y00000X",
            "OTOLARYNGOLOGY FACIAL PLASTIC SURGERY":"207YS0123X",
            "OTOLARYNGOLOGY OTOLARYNGIC ALLERGY":"207YX0602X",
            "OTOLARYNGOLOGY OTOLARYNGOLOGY/FACIAL PLASTIC SURGERY":"207YX0905X",
            "OTOLARYNGOLOGY OTOLOGY & NEUROTOLOGY":"207YX0901X",
            "OTOLARYNGOLOGY PEDIATRIC OTOLARYNGOLOGY":"207YP0228X",
            "OTOLARYNGOLOGY PLASTIC SURGERY WITHIN THE HEAD & NECK":"207YX0007X",
            "OTOLARYNGOLOGY & HEAD & NECK SURGERY":"207YX0007X",
            "OTOLARYNGOLOGY SLEEP MEDICINE":"207YS0012X",
            "PACE PROVIDER ORGANIZATION ":"251T00000X",
            "PAIN MEDICINE INTERVENTIONAL PAIN MEDICINE":"208VP0014X",
            "PAIN MEDICINE PAIN MEDICINE":"208VP0000X",
            "PATHOLOGY ANATOMIC PATHOLOGY":"207ZP0101X",
            "PATHOLOGY ANATOMIC PATHOLOGY & CLINICAL PATHOLOGY":"207ZP0102X",
            "PATHOLOGY BLOOD BANKING & TRANSFUSION MEDICINE":"207ZB0001X",
            "PATHOLOGY CHEMICAL PATHOLOGY":"207ZP0104X",
            "PATHOLOGY CLINICAL INFORMATICS":"207ZC0008X",
            "PATHOLOGY CLINICAL LABORATORY DIRECTOR NON-PHYSICIAN":"247ZC0005X",
            "PATHOLOGY CLINICAL PATHOLOGY":"207ZC0006X",
            "PATHOLOGY CLINICAL PATHOLOGY/LABORATORY MEDICINE":"207ZP0105X",
            "PATHOLOGY CYTOPATHOLOGY":"207ZC0500X",
            "PATHOLOGY DERMATOPATHOLOGY":"207ZD0900X",
            "PATHOLOGY FORENSIC PATHOLOGY":"207ZF0201X",
            "PATHOLOGY HEMATOLOGY":"207ZH0000X",
            "PATHOLOGY IMMUNOPATHOLOGY":"207ZI0100X",
            "PATHOLOGY MEDICAL MICROBIOLOGY":"207ZM0300X",
            "PATHOLOGY MOLECULAR GENETIC PATHOLOGY":"207ZP0007X",
            "PATHOLOGY NEUROPATHOLOGY":"207ZN0500X",
            "PATHOLOGY PEDIATRIC PATHOLOGY":"207ZP0213X",
            "PEDIATRICS ":"208000000X",
            "PEDIATRICS ADOLESCENT MEDICINE":"2080A0000X",
            "PEDIATRICS CHILD ABUSE PEDIATRICS":"2080C0008X",
            "PEDIATRICS CLINICAL & LABORATORY IMMUNOLOGY":"2080I0007X",
            "PEDIATRICS DEVELOPMENTAL ÔØΩÔØΩÔØΩÔØΩÔØΩÔØΩ BEHAVIORAL PEDIATRICS":"2080P0006X",
            "PEDIATRICS HOSPICE AND PALLIATIVE MEDICINE":"2080H0002X",
            "PEDIATRICS MEDICAL TOXICOLOGY":"2080T0002X",
            "PEDIATRICS NEONATAL-PERINATAL MEDICINE":"2080N0001X",
            "PEDIATRICS NEURODEVELOPMENTAL DISABILITIES":"2080P0008X",
            "PEDIATRICS OBESITY MEDICINE":"2080B0002X",
            "PEDIATRICS PEDIATRIC ALLERGY/IMMUNOLOGY":"2080P0201X",
            "PEDIATRICS PEDIATRIC CARDIOLOGY":"2080P0202X",
            "PEDIATRICS PEDIATRIC CRITICAL CARE MEDICINE":"2080P0203X",
            "PEDIATRICS PEDIATRIC EMERGENCY MEDICINE":"2080P0204X",
            "PEDIATRICS PEDIATRIC ENDOCRINOLOGY":"2080P0205X",
            "PEDIATRICS PEDIATRIC GASTROENTEROLOGY":"2080P0206X",
            "PEDIATRICS PEDIATRIC HEMATOLOGY-ONCOLOGY":"2080P0207X",
            "PEDIATRICS PEDIATRIC INFECTIOUS DISEASES":"2080P0208X",
            "PEDIATRICS PEDIATRIC NEPHROLOGY":"2080P0210X",
            "PEDIATRICS PEDIATRIC PULMONOLOGY":"2080P0214X",
            "PEDIATRICS PEDIATRIC RHEUMATOLOGY":"2080P0216X",
            "PEDIATRICS PEDIATRIC TRANSPLANT HEPATOLOGY":"2080T0004X",
            "PEDIATRICS SLEEP MEDICINE":"2080S0012X",
            "PEDIATRICS SPORTS MEDICINE":"2080S0010X",
            "PEDORTHIST ":"224L00000X",
            "PEER SPECIALIST ":"175T00000X",
            "PERFUSIONIST ":"242T00000X",
            "PERSONAL EMERGENCY RESPONSE ATTENDANT ":"146D00000X",
            "PHARMACIST ":"183500000X",
            "PHARMACIST AMBULATORY CARE":"1835P2201X",
            "PHARMACIST CRITICAL CARE":"1835C0205X",
            "PHARMACIST GENERAL PRACTICE":"1835G0000X",
            "PHARMACIST GERIATRIC":"1835G0303X",
            "PHARMACIST NUCLEAR":"1835N0905X",
            "PHARMACIST NUTRITION SUPPORT":"1835N1003X",
            "PHARMACIST ONCOLOGY":"1835X0200X",
            "PHARMACIST PEDIATRICS":"1835P0200X",
            "PHARMACIST PHARMACIST CLINICIAN (PHC)/ CLINICAL PHARMACY SPECIALIST":"1835P0018X",
            "PHARMACIST PHARMACOTHERAPY":"1835P1200X",
            "PHARMACIST PSYCHIATRIC":"1835P1300X",
            "PHARMACY ":"333600000X",
            "PHARMACY CLINIC PHARMACY":"3336C0002X",
            "PHARMACY COMMUNITY/RETAIL PHARMACY":"3336C0003X",
            "PHARMACY COMPOUNDING PHARMACY":"3336C0004X",
            "PHARMACY HOME INFUSION THERAPY PHARMACY":"3336H0001X",
            "PHARMACY INSTITUTIONAL PHARMACY":"3336I0012X",
            "PHARMACY LONG TERM CARE PHARMACY":"3336L0003X",
            "PHARMACY MAIL ORDER PHARMACY":"3336M0002X",
            "PHARMACY MANAGED CARE ORGANIZATION PHARMACY":"3336M0003X",
            "PHARMACY NUCLEAR PHARMACY":"3336N0007X",
            "PHARMACY SPECIALTY PHARMACY":"3336S0011X",
            "PHARMACY TECHNICIAN ":"183700000X",
            "PHLEBOLOGY ":"202K00000X",
            "PHYSICAL MEDICINE & REHABILITATION ":"208100000X",
            "PHYSICAL MEDICINE & REHABILITATION BRAIN INJURY MEDICINE":"2081P0301X",
            "PHYSICAL MEDICINE & REHABILITATION HOSPICE AND PALLIATIVE MEDICINE":"2081H0002X",
            "PHYSICAL MEDICINE & REHABILITATION NEUROMUSCULAR MEDICINE":"2081N0008X",
            "PHYSICAL MEDICINE & REHABILITATION PAIN MEDICINE":"2081P2900X",
            "PHYSICAL MEDICINE & REHABILITATION PEDIATRIC REHABILITATION MEDICINE":"2081P0010X",
            "PHYSICAL MEDICINE & REHABILITATION SPINAL CORD INJURY MEDICINE":"2081P0004X",
            "PHYSICAL MEDICINE & REHABILITATION SPORTS MEDICINE":"2081S0010X",
            "PHYSICAL THERAPIST ":"225100000X",
            "PHYSICAL THERAPIST CARDIOPULMONARY":"2251C2600X",
            "PHYSICAL THERAPIST ELECTROPHYSIOLOGY CLINICAL":"2251E1300X",
            "PHYSICAL THERAPIST ERGONOMICS":"2251E1200X",
            "PHYSICAL THERAPIST GERIATRICS":"2251G0304X",
            "PHYSICAL THERAPIST HAND":"2251H1200X",
            "PHYSICAL THERAPIST HUMAN FACTORS":"2251H1300X",
            "PHYSICAL THERAPIST NEUROLOGY":"2251N0400X",
            "PHYSICAL THERAPIST ORTHOPEDIC":"2251X0800X",
            "PHYSICAL THERAPIST PEDIATRICS":"2251P0200X",
            "PHYSICAL THERAPIST SPORTS":"2251S0007X",
            "PHYSICAL THERAPY ASSISTANT ":"225200000X",
            "PHYSICIAN ASSISTANT ":"363A00000X",
            "PHYSICIAN ASSISTANT MEDICAL":"363AM0700X",
            "PHYSICIAN ASSISTANT SURGICAL TECHNOLOGIST":"363AS0400X",
            "PHYSIOLOGICAL LABORATORY ":"293D00000X",
            "PLASTIC SURGERY PLASTIC SURGERY WITHIN THE HEAD AND NECK":"2082S0099X",
            "PLASTIC SURGERY SURGERY OF THE HAND":"2082S0105X",
            "PODIATRIST ":"213E00000X",
            "PODIATRIST FOOT & ANKLE SURGERY":"213ES0103X",
            "PODIATRIST FOOT SURGERY":"213ES0131X",
            "PODIATRIST GENERAL PRACTICE":"213EG0000X",
            "PODIATRIST PRIMARY PODIATRIC MEDICINE":"213EP1101X",
            "PODIATRIST PUBLIC MEDICINE":"213EP0504X",
            "PODIATRIST RADIOLOGY":"213ER0200X",
            "PODIATRIST SPORTS MEDICINE":"213ES0000X",
            "POETRY THERAPIST ":"102X00000X",
            "POINT OF SERVICE ":"305S00000X",
            "PORTABLE X-RAY AND/OR OTHER PORTABLE DIAGNOSTIC IMAGING SUPPLIER ":"335V00000X",
            "PREFERRED PROVIDER ORGANIZATION ":"305R00000X",
            "PREVENTION PROFESSIONAL ":"405300000X",
            "PREVENTIVE MEDICINE AEROSPACE MEDICINE":"2083A0100X",
            "PREVENTIVE MEDICINE CLINICAL INFORMATICS":"2083C0008X",
            "PREVENTIVE MEDICINE MEDICAL TOXICOLOGY":"2083T0002X",
            "PREVENTIVE MEDICINE OBESITY MEDICINE":"2083B0002X",
            "PREVENTIVE MEDICINE OCCUPATIONAL MEDICINE":"2083X0100X",
            "PREVENTIVE MEDICINE PREVENTIVE MEDICINE/OCCUPATIONAL ENVIRONMENTAL MEDICINE":"2083P0500X",
            "PREVENTIVE MEDICINE PUBLIC HEALTH & GENERAL PREVENTIVE MEDICINE":"2083P0901X",
            "PREVENTIVE MEDICINE SPORTS MEDICINE":"2083S0010X",
            "PREVENTIVE MEDICINE UNDERSEA AND HYPERBARIC MEDICINE":"2083P0011X",
            "PRIVATE VEHICLE ":"347C00000X",
            "PROSTHETIC/ORTHOTIC SUPPLIER ":"335E00000X",
            "PROSTHETIST ":"224P00000X",
            "PSYCHIATRIC HOSPITAL ":"283Q00000X",
            "PSYCHIATRIC RESIDENTIAL TREATMENT FACILITY ":"323P00000X",
            "PSYCHIATRIC UNIT ":"273R00000X",
            "PSYCHIATRY & NEUROLOGY ADDICTION MEDICINE":"2084A0401X",
            "PSYCHIATRY & NEUROLOGY ADDICTION PSYCHIATRY":"2084P0802X",
            "PSYCHIATRY & NEUROLOGY BEHAVIORAL NEUROLOGY & NEUROPSYCHIATRY":"2084B0040X",
            "PSYCHIATRY & NEUROLOGY BRAIN INJURY MEDICINE":"2084P0301X",
            "PSYCHIATRY & NEUROLOGY CHILD & ADOLESCENT PSYCHIATRY":"2084P0804X",
            "PSYCHIATRY & NEUROLOGY CLINICAL NEUROPHYSIOLOGY":"2084N0600X",
            "PSYCHIATRY & NEUROLOGY DIAGNOSTIC NEUROIMAGING":"2084D0003X",
            "PSYCHIATRY & NEUROLOGY FORENSIC PSYCHIATRY":"2084F0202X",
            "PSYCHIATRY & NEUROLOGY GERIATRIC PSYCHIATRY":"2084P0805X",
            "PSYCHIATRY & NEUROLOGY HOSPICE AND PALLIATIVE MEDICINE":"2084H0002X",
            "PSYCHIATRY & NEUROLOGY NEUROCRITICAL CARE":"2084A2900X",
            "PSYCHIATRY & NEUROLOGY NEURODEVELOPMENTAL DISABILITIES":"2084P0005X",
            "PSYCHIATRY & NEUROLOGY NEUROLOGY":"2084N0400X",
            "PSYCHIATRY & NEUROLOGY NEUROLOGY WITH SPECIAL QUALIFICATIONS IN CHILD NEUROLOGY":"2084N0402X",
            "PSYCHIATRY & NEUROLOGY NEUROMUSCULAR MEDICINE":"2084N0008X",
            "PSYCHIATRY & NEUROLOGY OBESITY MEDICINE":"2084B0002X",
            "PSYCHIATRY & NEUROLOGY PAIN MEDICINE":"2084P2900X",
            "PSYCHIATRY & NEUROLOGY PSYCHIATRY":"2084P0800X",
            "PSYCHIATRY & NEUROLOGY PSYCHOSOMATIC MEDICINE":"2084P0015X",
            "PSYCHIATRY & NEUROLOGY SLEEP MEDICINE":"2084S0012X",
            "PSYCHIATRY & NEUROLOGY SPORTS MEDICINE":"2084S0010X",
            "PSYCHIATRY & NEUROLOGY VASCULAR NEUROLOGY":"2084V0102X",
            "PSYCHOANALYST ":"102L00000X",
            "PSYCHOLOGIST ":"103T00000X",
            "PSYCHOLOGIST ADDICTION (SUBSTANCE USE DISORDER)":"103TA0400X",
            "PSYCHOLOGIST ADULT DEVELOPMENT & AGING":"103TA0700X",
            "PSYCHOLOGIST CLINICAL":"103TC0700X",
            "PSYCHOLOGIST CLINICAL CHILD & ADOLESCENT":"103TC2200X",
            "PSYCHOLOGIST COGNITIVE & BEHAVIORAL":"103TB0200X",
            "PSYCHOLOGIST COUNSELING":"103TC1900X",
            "PSYCHOLOGIST EDUCATIONAL":"103TE1000X",
            "PSYCHOLOGIST EXERCISE & SPORTS":"103TE1100X",
            "PSYCHOLOGIST FAMILY":"103TF0000X",
            "PSYCHOLOGIST FORENSIC":"103TF0200X",
            "PSYCHOLOGIST GROUP PSYCHOTHERAPY":"103TP2701X",
            "PSYCHOLOGIST HEALTH":"103TH0004X",
            "PSYCHOLOGIST HEALTH SERVICE":"103TH0100X",
            "PSYCHOLOGIST MEN & MASCULINITY":"103TM1700X",
            "PSYCHOLOGIST MENTAL RETARDATION & DEVELOPMENTAL DISABILITIES":"103TM1800X",
            "PSYCHOLOGIST PRESCRIBING (MEDICAL)":"103TP0016X",
            "PSYCHOLOGIST PSYCHOANALYSIS":"103TP0814X",
            "PSYCHOLOGIST PSYCHOTHERAPY":"103TP2700X",
            "PSYCHOLOGIST REHABILITATION":"103TR0400X",
            "PSYCHOLOGIST SCHOOL":"103TS0200X",
            "PSYCHOLOGIST WOMEN":"103TW0100X",
            "PUBLIC HEALTH OR WELFARE ":"251K00000X",
            "PULMONARY FUNCTION TECHNOLOGIST ":"225B00000X",
            "RADIOLOGIC TECHNOLOGIST ":"247100000X",
            "RADIOLOGIC TECHNOLOGIST BONE DENSITOMETRY":"2471B0102X",
            "RADIOLOGIC TECHNOLOGIST CARDIAC-INTERVENTIONAL TECHNOLOGY":"2471C1106X",
            "RADIOLOGIC TECHNOLOGIST CARDIOVASCULAR-INTERVENTIONAL TECHNOLOGY":"2471C1101X",
            "RADIOLOGIC TECHNOLOGIST COMPUTED TOMOGRAPHY":"2471C3401X",
            "RADIOLOGIC TECHNOLOGIST MAGNETIC RESONANCE IMAGING":"2471M1202X",
            "RADIOLOGIC TECHNOLOGIST MAMMOGRAPHY":"2471M2300X",
            "RADIOLOGIC TECHNOLOGIST NUCLEAR MEDICINE TECHNOLOGY":"2471N0900X",
            "RADIOLOGIC TECHNOLOGIST QUALITY MANAGEMENT":"2471Q0001X",
            "RADIOLOGIC TECHNOLOGIST RADIATION THERAPY":"2471R0002X",
            "RADIOLOGIC TECHNOLOGIST RADIOGRAPHY":"2471C3402X",
            "RADIOLOGIC TECHNOLOGIST SONOGRAPHY":"2471S1302X",
            "RADIOLOGIC TECHNOLOGIST VASCULAR SONOGRAPHY":"2471V0105X",
            "RADIOLOGIC TECHNOLOGIST VASCULAR-INTERVENTIONAL TECHNOLOGY":"2471V0106X",
            "RADIOLOGY BODY IMAGING":"2085B0100X",
            "RADIOLOGY DIAGNOSTIC NEUROIMAGING":"2085D0003X",
            "RADIOLOGY DIAGNOSTIC RADIOLOGY":"2085R0202X",
            "RADIOLOGY DIAGNOSTIC ULTRASOUND":"2085U0001X",
            "RADIOLOGY HOSPICE AND PALLIATIVE MEDICINE":"2085H0002X",
            "RADIOLOGY NEURORADIOLOGY":"2085N0700X",
            "RADIOLOGY NUCLEAR RADIOLOGY":"2085N0904X",
            "RADIOLOGY PEDIATRIC RADIOLOGY":"2085P0229X",
            "RADIOLOGY PRACTITIONER ASSISTANT ":"243U00000X",
            "RADIOLOGY RADIATION ONCOLOGY":"2085R0001X",
            "RADIOLOGY RADIOLOGICAL PHYSICS":"2085R0205X",
            "RADIOLOGY THERAPEUTIC RADIOLOGY":"2085R0203X",
            "RADIOLOGY VASCULAR & INTERVENTIONAL RADIOLOGY":"2085R0204X",
            "RECREATION THERAPIST ":"225800000X",
            "RECREATIONAL THERAPIST ASSISTANT ":"226000000X",
            "REFLEXOLOGIST ":"173C00000X",
            "REGISTERED NURSE ":"163W00000X",
            "REGISTERED NURSE ADDICTION (SUBSTANCE USE DISORDER)":"163WA0400X",
            "REGISTERED NURSE ADMINISTRATOR":"163WA2000X",
            "REGISTERED NURSE AMBULATORY CARE":"163WP2201X",
            "REGISTERED NURSE CARDIAC REHABILITATION":"163WC3500X",
            "REGISTERED NURSE CASE MANAGEMENT":"163WC0400X",
            "REGISTERED NURSE COLLEGE HEALTH":"163WC1400X",
            "REGISTERED NURSE COMMUNITY HEALTH":"163WC1500X",
            "REGISTERED NURSE CONTINENCE CARE":"163WC2100X",
            "REGISTERED NURSE CONTINUING EDUCATION/STAFF DEVELOPMENT":"163WC1600X",
            "REGISTERED NURSE CRITICAL CARE MEDICINE":"163WC0200X",
            "REGISTERED NURSE DIABETES EDUCATOR":"163WD0400X",
            "REGISTERED NURSE DIALYSIS PERITONEAL":"163WD1100X",
            "REGISTERED NURSE EMERGENCY":"163WE0003X",
            "REGISTERED NURSE ENTEROSTOMAL THERAPY":"163WE0900X",
            "REGISTERED NURSE FLIGHT":"163WF0300X",
            "REGISTERED NURSE GASTROENTEROLOGY":"163WG0100X",
            "REGISTERED NURSE GENERAL PRACTICE":"163WG0000X",
            "REGISTERED NURSE GERONTOLOGY":"163WG0600X",
            "REGISTERED NURSE HEMODIALYSIS":"163WH0500X",
            "REGISTERED NURSE HOME HEALTH":"163WH0200X",
            "REGISTERED NURSE HOSPICE":"163WH1000X",
            "REGISTERED NURSE INFECTION CONTROL":"163WI0600X",
            "REGISTERED NURSE INFUSION THERAPY":"163WI0500X",
            "REGISTERED NURSE LACTATION CONSULTANT":"163WL0100X",
            "REGISTERED NURSE MATERNAL NEWBORN":"163WM0102X",
            "REGISTERED NURSE MEDICAL-SURGICAL":"163WM0705X",
            "REGISTERED NURSE NEONATAL INTENSIVE CARE":"163WN0002X",
            "REGISTERED NURSE NEONATAL LOW-RISK":"163WN0003X",
            "REGISTERED NURSE NEPHROLOGY":"163WN0300X",
            "REGISTERED NURSE NEUROSCIENCE":"163WN0800X",
            "REGISTERED NURSE NURSE MASSAGE THERAPIST (NMT)":"163WM1400X",
            "REGISTERED NURSE NUTRITION SUPPORT":"163WN1003X",
            "REGISTERED NURSE OBSTETRIC HIGH-RISK":"163WX0002X",
            "REGISTERED NURSE OBSTETRIC INPATIENT":"163WX0003X",
            "REGISTERED NURSE OCCUPATIONAL HEALTH":"163WX0106X",
            "REGISTERED NURSE ONCOLOGY":"163WX0200X",
            "REGISTERED NURSE OPHTHALMIC":"163WX1100X",
            "REGISTERED NURSE ORTHOPEDIC":"163WX0800X",
            "REGISTERED NURSE OSTOMY CARE":"163WX1500X",
            "REGISTERED NURSE OTORHINOLARYNGOLOGY & HEAD-NECK":"163WX0601X",
            "REGISTERED NURSE PAIN MANAGEMENT":"163WP0000X",
            "REGISTERED NURSE PEDIATRIC ONCOLOGY":"163WP0218X",
            "REGISTERED NURSE PEDIATRICS":"163WP0200X",
            "REGISTERED NURSE PERINATAL":"163WP1700X",
            "REGISTERED NURSE PLASTIC SURGERY":"163WS0121X",
            "REGISTERED NURSE PSYCH/MENTAL HEALTH":"163WP0808X",
            "REGISTERED NURSE PSYCH/MENTAL HEALTH ADULT":"163WP0809X",
            "REGISTERED NURSE PSYCH/MENTAL HEALTH CHILD & ADOLESCENT":"163WP0807X",
            "REGISTERED NURSE REGISTERED NURSE FIRST ASSISTANT":"163WR0006X",
            "REGISTERED NURSE REHABILITATION":"163WR0400X",
            "REGISTERED NURSE REPRODUCTIVE ENDOCRINOLOGY/INFERTILITY":"163WR1000X",
            "REGISTERED NURSE SCHOOL":"163WS0200X",
            "REGISTERED NURSE UROLOGY":"163WU0100X",
            "REGISTERED NURSE WOMEN'S HEALTH CARE AMBULATORY":"163WW0101X",
            "REGISTERED NURSE WOUND CARE":"163WW0000X",
            "REHABILITATION COUNSELOR ":"225C00000X",
            "REHABILITATION COUNSELOR ASSISTIVE TECHNOLOGY PRACTITIONER":"225CA2400X",
            "REHABILITATION COUNSELOR ASSISTIVE TECHNOLOGY SUPPLIER":"225CA2500X",
            "REHABILITATION COUNSELOR ORIENTATION AND MOBILITY TRAINING PROVIDER":"225CX0006X",
            "REHABILITATION HOSPITAL ":"283X00000X",
            "REHABILITATION HOSPITAL CHILDREN":"283XC2000X",
            "REHABILITATION PRACTITIONER ":"225400000X",
            "REHABILITATION UNIT ":"273Y00000X",
            "REHABILITATION SUBSTANCE USE DISORDER UNIT ":"276400000X",
            "RELIGIOUS NONMEDICAL HEALTH CARE INSTITUTION ":"282J00000X",
            "RELIGIOUS NONMEDICAL NURSING PERSONNEL ":"374T00000X",
            "RELIGIOUS NONMEDICAL PRACTITIONER ":"374K00000X",
            "RESIDENTIAL TREATMENT FACILITY EMOTIONALLY DISTURBED CHILDREN ":"322D00000X",
            "RESIDENTIAL TREATMENT FACILITY MENTAL RETARDATION AND/OR DEVELOPMENTAL DISABILITIES ":"320600000X",
            "RESIDENTIAL TREATMENT FACILITY PHYSICAL DISABILITIES ":"320700000X",
            "RESPIRATORY THERAPIST CERTIFIED ":"227800000X",
            "RESPIRATORY THERAPIST CERTIFIED CRITICAL CARE":"2278C0205X",
            "RESPIRATORY THERAPIST CERTIFIED EDUCATIONAL":"2278E1000X",
            "RESPIRATORY THERAPIST CERTIFIED EMERGENCY CARE":"2278E0002X",
            "RESPIRATORY THERAPIST CERTIFIED GENERAL CARE":"2278G1100X",
            "RESPIRATORY THERAPIST CERTIFIED GERIATRIC CARE":"2278G0305X",
            "RESPIRATORY THERAPIST CERTIFIED HOME HEALTH":"2278H0200X",
            "RESPIRATORY THERAPIST CERTIFIED NEONATAL/PEDIATRICS":"2278P3900X",
            "RESPIRATORY THERAPIST CERTIFIED PALLIATIVE/HOSPICE":"2278P3800X",
            "RESPIRATORY THERAPIST CERTIFIED PATIENT TRANSPORT":"2278P4000X",
            "RESPIRATORY THERAPIST CERTIFIED PULMONARY DIAGNOSTICS":"2278P1004X",
            "RESPIRATORY THERAPIST CERTIFIED PULMONARY FUNCTION TECHNOLOGIST":"2278P1006X",
            "RESPIRATORY THERAPIST CERTIFIED PULMONARY REHABILITATION":"2278P1005X",
            "RESPIRATORY THERAPIST CERTIFIED SNF/SUBACUTE CARE":"2278S1500X",
            "RESPIRATORY THERAPIST REGISTERED ":"227900000X",
            "RESPIRATORY THERAPIST REGISTERED CRITICAL CARE":"2279C0205X",
            "RESPIRATORY THERAPIST REGISTERED EDUCATIONAL":"2279E1000X",
            "RESPIRATORY THERAPIST REGISTERED EMERGENCY CARE":"2279E0002X",
            "RESPIRATORY THERAPIST REGISTERED GENERAL CARE":"2279G1100X",
            "RESPIRATORY THERAPIST REGISTERED GERIATRIC CARE":"2279G0305X",
            "RESPIRATORY THERAPIST REGISTERED HOME HEALTH":"2279H0200X",
            "RESPIRATORY THERAPIST REGISTERED NEONATAL/PEDIATRICS":"2279P3900X",
            "RESPIRATORY THERAPIST REGISTERED PALLIATIVE/HOSPICE":"2279P3800X",
            "RESPIRATORY THERAPIST REGISTERED PATIENT TRANSPORT":"2279P4000X",
            "RESPIRATORY THERAPIST REGISTERED PULMONARY DIAGNOSTICS":"2279P1004X",
            "RESPIRATORY THERAPIST REGISTERED PULMONARY FUNCTION TECHNOLOGIST":"2279P1006X",
            "RESPIRATORY THERAPIST REGISTERED PULMONARY REHABILITATION":"2279P1005X",
            "RESPIRATORY THERAPIST REGISTERED SNF/SUBACUTE CARE":"2279S1500X",
            "RESPITE CARE ":"385H00000X",
            "RESPITE CARE RESPITE CARE CAMP":"385HR2050X",
            "RESPITE CARE RESPITE CARE MENTAL ILLNESS CHILD":"385HR2055X",
            "RESPITE CARE RESPITE CARE MENTAL RETARDATION AND/OR DEVELOPMENTAL DISABILITIES CHILD":"385HR2060X",
            "RESPITE CARE RESPITE CARE PHYSICAL DISABILITIES CHILD":"385HR2065X",
            "SECURED MEDICAL TRANSPORT (VAN) ":"343800000X",
            "SINGLE SPECIALTY ":"193400000X",
            "SKILLED NURSING FACILITY ":"314000000X",
            "SKILLED NURSING FACILITY NURSING CARE PEDIATRIC":"3140N1450X",
            "SLEEP SPECIALIST PHD ":"173F00000X",
            "SOCIAL WORKER ":"104100000X",
            "SOCIAL WORKER CLINICAL":"1041C0700X",
            "SOCIAL WORKER SCHOOL":"1041S0200X",
            "SPEC/TECH CARDIOVASCULAR ":"246X00000X",
            "SPEC/TECH CARDIOVASCULAR CARDIOVASCULAR INVASIVE SPECIALIST":"246XC2901X",
            "SPEC/TECH CARDIOVASCULAR SONOGRAPHY":"246XS1301X",
            "SPEC/TECH CARDIOVASCULAR VASCULAR SPECIALIST":"246XC2903X",
            "SPEC/TECH HEALTH INFO ":"246Y00000X",
            "SPEC/TECH HEALTH INFO CODING SPECIALIST HOSPITAL BASED":"246YC3301X",
            "SPEC/TECH HEALTH INFO CODING SPECIALIST PHYSICIAN OFFICE BASED":"246YC3302X",
            "SPEC/TECH HEALTH INFO REGISTERED RECORD ADMINISTRATOR":"246YR1600X",
            "SPEC/TECH PATHOLOGY ":"246Q00000X",
            "SPEC/TECH PATHOLOGY BLOOD BANKING":"246QB0000X",
            "SPEC/TECH PATHOLOGY CHEMISTRY":"246QC1000X",
            "SPEC/TECH PATHOLOGY CYTOTECHNOLOGY":"246QC2700X",
            "SPEC/TECH PATHOLOGY HEMAPHERESIS PRACTITIONER":"246QH0401X",
            "SPEC/TECH PATHOLOGY HEMATOLOGY":"246QH0000X",
            "SPEC/TECH PATHOLOGY HISTOLOGY":"246QH0600X",
            "SPEC/TECH PATHOLOGY IMMUNOLOGY":"246QI0000X",
            "SPEC/TECH PATHOLOGY LABORATORY MANAGEMENT":"246QL0900X",
            "SPEC/TECH PATHOLOGY LABORATORY MANAGEMENT DIPLOMATE":"246QL0901X",
            "SPEC/TECH PATHOLOGY MEDICAL TECHNOLOGIST":"246QM0706X",
            "SPEC/TECH PATHOLOGY MICROBIOLOGY":"246QM0900X",
            "SPECIAL HOSPITAL ":"284300000X",
            "SPECIALIST ":"174400000X",
            "SPECIALIST GRAPHICS DESIGNER":"1744G0900X",
            "SPECIALIST PROSTHETICS CASE MANAGEMENT":"1744P3200X",
            "SPECIALIST RESEARCH DATA ABSTRACTER/CODER":"1744R1103X",
            "SPECIALIST RESEARCH STUDY":"1744R1102X",
            "SPECIALIST/TECHNOLOGIST ":"225500000X",
            "SPECIALIST/TECHNOLOGIST ":"235500000X",
            "SPECIALIST/TECHNOLOGIST ATHLETIC TRAINER":"2255A2300X",
            "SPECIALIST/TECHNOLOGIST AUDIOLOGY ASSISTANT":"2355A2700X",
            "SPECIALIST/TECHNOLOGIST REHABILITATION BLIND":"2255R0406X",
            "SPECIALIST/TECHNOLOGIST SPEECH-LANGUAGE ASSISTANT":"2355S0801X",
            "SPECIALIST/TECHNOLOGIST OTHER ":"246Z00000X",
            "SPECIALIST/TECHNOLOGIST OTHER ART MEDICAL":"246ZA2600X",
            "SPECIALIST/TECHNOLOGIST OTHER BIOCHEMIST":"246ZB0500X",
            "SPECIALIST/TECHNOLOGIST OTHER BIOMEDICAL ENGINEERING":"246ZB0301X",
            "SPECIALIST/TECHNOLOGIST OTHER BIOMEDICAL PHOTOGRAPHER":"246ZB0302X",
            "SPECIALIST/TECHNOLOGIST OTHER BIOSTATISTICIAN":"246ZB0600X",
            "SPECIALIST/TECHNOLOGIST OTHER EEG":"246ZE0500X",
            "SPECIALIST/TECHNOLOGIST OTHER ELECTRONEURODIAGNOSTIC":"246ZE0600X",
            "SPECIALIST/TECHNOLOGIST OTHER GENETICIST MEDICAL (PHD)":"246ZG1000X",
            "SPECIALIST/TECHNOLOGIST OTHER GRAPHICS METHODS":"246ZG0701X",
            "SPECIALIST/TECHNOLOGIST OTHER ILLUSTRATION MEDICAL":"246ZI1000X",
            "SPECIALIST/TECHNOLOGIST OTHER NEPHROLOGY":"246ZN0300X",
            "SPECIALIST/TECHNOLOGIST OTHER ORTHOPEDIC ASSISTANT":"246ZX2200X",
            "SPECIALIST/TECHNOLOGIST OTHER SURGICAL ASSISTANT":"246ZC0007X",
            "SPECIALIST/TECHNOLOGIST OTHER SURGICAL TECHNOLOGIST":"246ZS0410X",
            "SPEECH-LANGUAGE PATHOLOGIST ":"235Z00000X",
            "STUDENT IN AN ORGANIZED HEALTH CARE EDUCATION/TRAINING PROGRAM ":"390200000X",
            "SUBSTANCE ABUSE REHABILITATION FACILITY ":"324500000X",
            "SUBSTANCE ABUSE REHABILITATION FACILITY SUBSTANCE ABUSE TREATMENT CHILDREN":"3245S0500X",
            "SUPPORTS BROKERAGE ":"251X00000X",
            "SURGERY ":"208600000X",
            "SURGERY HOSPICE AND PALLIATIVE MEDICINE":"2086H0002X",
            "SURGERY PEDIATRIC SURGERY":"2086S0120X",
            "SURGERY PLASTIC AND RECONSTRUCTIVE SURGERY":"2086S0122X",
            "SURGERY SURGERY OF THE HAND":"2086S0105X",
            "SURGERY SURGICAL CRITICAL CARE":"2086S0102X",
            "SURGERY SURGICAL ONCOLOGY":"2086X0206X",
            "SURGERY TRAUMA SURGERY":"2086S0127X",
            "SURGERY VASCULAR SURGERY":"2086S0129X",
            "TAXI ":"344600000X",
            "TECHNICIAN ":"374700000X",
            "TECHNICIAN ATTENDANT CARE PROVIDER":"3747A0650X",
            "TECHNICIAN PERSONAL CARE ATTENDANT":"3747P1801X",
            "TECHNICIAN CARDIOLOGY ":"246W00000X",
            "TECHNICIAN HEALTH INFORMATION ":"247000000X",
            "TECHNICIAN HEALTH INFORMATION ASSISTANT RECORD TECHNICIAN":"2470A2800X",
            "TECHNICIAN OTHER ":"247200000X",
            "TECHNICIAN OTHER BIOMEDICAL ENGINEERING":"2472B0301X",
            "TECHNICIAN OTHER DARKROOM":"2472D0500X",
            "TECHNICIAN OTHER EEG":"2472E0500X",
            "TECHNICIAN OTHER RENAL DIALYSIS":"2472R0900X",
            "TECHNICIAN OTHER VETERINARY":"2472V0600X",
            "TECHNICIAN PATHOLOGY ":"246R00000X",
            "TECHNICIAN PATHOLOGY HISTOLOGY":"246RH0600X",
            "TECHNICIAN PATHOLOGY MEDICAL LABORATORY":"246RM2200X",
            "TECHNICIAN PATHOLOGY PHLEBOTOMY":"246RP1900X",
            "TECHNICIAN/TECHNOLOGIST ":"156F00000X",
            "TECHNICIAN/TECHNOLOGIST CONTACT LENS":"156FC0800X",
            "TECHNICIAN/TECHNOLOGIST CONTACT LENS FITTER":"156FC0801X",
            "TECHNICIAN/TECHNOLOGIST OCULARIST":"156FX1700X",
            "TECHNICIAN/TECHNOLOGIST OPHTHALMIC":"156FX1100X",
            "TECHNICIAN/TECHNOLOGIST OPHTHALMIC ASSISTANT":"156FX1101X",
            "TECHNICIAN/TECHNOLOGIST OPTICIAN":"156FX1800X",
            "TECHNICIAN/TECHNOLOGIST OPTOMETRIC ASSISTANT":"156FX1201X",
            "TECHNICIAN/TECHNOLOGIST OPTOMETRIC TECHNICIAN":"156FX1202X",
            "TECHNICIAN/TECHNOLOGIST ORTHOPTIST":"156FX1900X",
            "THORACIC SURGERY (CARDIOTHORACIC VASCULAR SURGERY) ":"208G00000X",
            "TRAIN ":"347D00000X",
            "TRANSPLANT SURGERY ":"204F00000X",
            "TRANSPORTATION BROKER ":"347E00000X",
            "UNKNOWN":"UN",
            "UROLOGY ":"208800000X",
            "UROLOGY ":"208800000X",
            "UROLOGY FEMALE PELVIC MEDICINE AND RECONSTRUCTIVE SURGERY":"2088F0040X",
            "UROLOGY PEDIATRIC UROLOGY":"2088P0231X",
            "VETERINARIAN ":"174M00000X",
            "VETERINARIAN MEDICAL RESEARCH":"174MM1900X",
            "VOLUNTARY OR CHARITABLE ":"251V00000X",
            "HEMATOLOGY":"246QH0000X",
            "CARDIOLOGY":"246W00000X",
            "GASTROENTEROLOGY":"207RG0100X",
            "NEUROLOGY":"2084D0003X",
            "AUDIOLOGY":"2355A2700X",
            "ENDOCRINOLOGY, DIABETES & METABOLISM":"207RE0101X",
            "OTOLARYNGOLOGY & HEAD & NECK SURGERY":"207YX0007X",
            "INTERNAL MEDICINE":"207R00000X",
            "DERMATOLOGY":"207N00000X",
            "OPHTHALMOLOGY":"207W00000X",
        
        

        }

#  ██▓   ▄▄▄      ▄▄▄▄       ██▀███ ▓█████  ██████ █    ██ ██▓ ▄▄▄█████▓    ▄████▄  ███▄ ▄███▓
# ▓██▒  ▒████▄   ▓█████▄    ▓██ ▒ ██▓█   ▀▒██    ▒ ██  ▓██▓██▒ ▓  ██▒ ▓▒   ▒██▀ ▀█ ▓██▒▀█▀ ██▒
# ▒██░  ▒██  ▀█▄ ▒██▒ ▄██   ▓██ ░▄█ ▒███  ░ ▓██▄  ▓██  ▒██▒██░ ▒ ▓██░ ▒░   ▒▓█    ▄▓██    ▓██░
# ▒██░  ░██▄▄▄▄██▒██░█▀     ▒██▀▀█▄ ▒▓█  ▄  ▒   ██▓▓█  ░██▒██░ ░ ▓██▓ ░    ▒▓▓▄ ▄██▒██    ▒██ 
# ░██████▓█   ▓██░▓█  ▀█▓   ░██▓ ▒██░▒████▒██████▒▒▒█████▓░██████▒██▒ ░    ▒ ▓███▀ ▒██▒   ░██▒
# ░ ▒░▓  ▒▒   ▓▒█░▒▓███▀▒   ░ ▒▓ ░▒▓░░ ▒░ ▒ ▒▓▒ ▒ ░▒▓▒ ▒ ▒░ ▒░▓  ▒ ░░      ░ ░▒ ▒  ░ ▒░   ░  ░
# ░ ░ ▒  ░▒   ▒▒ ▒░▒   ░      ░▒ ░ ▒░░ ░  ░ ░▒  ░ ░░▒░ ░ ░░ ░ ▒  ░ ░         ░  ▒  ░  ░      ░
#   ░ ░   ░   ▒   ░    ░      ░░   ░   ░  ░  ░  ░  ░░░ ░ ░  ░ ░  ░         ░       ░      ░   
#     ░  ░    ░  ░░            ░       ░  ░     ░    ░        ░  ░         ░ ░            ░   
#                      ░                                                   ░                  

lab_result_cm_specimen_source_dict = {

            "2143-6"	 :	"SER_PLAS"	,
            "11558-4"	 :	"BLD"	,
            "6136-6"	 :	"SER"	,
            "5778-6"	 :	"URINE"	,
            "2157-6"	 :	"SER_PLAS"	,
            "3150-0"	 :	"INHL_GAS"	,
            "2823-3"	 :	"SER_PLAS"	,
            "4576-5"	 :	"BLD"	,
            "5799-2"	 :	"URINE"	,
            "779-9"	 :	"BLD"	,
            "26484-6"	 :	"BLD"	,
            "19113-0"	 :	"SER_PLAS"	,
            "630-4"	 :	"URINE"	,
            "2028-9"	 :	"SER_PLAS"	,
            "702-1"	 :	"BLD"	,
            "32623-1"	 :	"BLD"	,
            "18481-2"	 :	"THRT"	,
            "6301-6"	 :	"PPP"	,
            "600-7"	 :	"BLD"	,
            "11556-8"	 :	"BLD"	,
            "41276-7"	 :	"BLD"	,
            "1994-3"	 :	"BLD"	,
            "6273-7"	 :	"SER"	,
            "6106-9"	 :	"SER"	,
            "3255-7"	 :	"PPP"	,
            "3107-0"	 :	"URINE"	,
            "11555-0"	 :	"BLD"	,
            "6768-6"	 :	"SER_PLAS"	,
            "2085-9"	 :	"SER_PLAS"	,
            "789-8"	 :	"BLD"	,
            "30934-4"	 :	"SER_PLAS"	,
            "20563-3"	 :	"BLD"	,
            "11253-2"	 :	"BLD"	,
            "26450-7"	 :	"BLD"	,
            "16362-6"	 :	"PLAS"	,
            "3024-7"	 :	"SER_PLAS"	,
            "1975-2"	 :	"SER_PLAS"	,
            "2089-1"	 :	"SER_PLAS"	,
            "26455-6"	 :	"BODY_FLD"	,
            "59408-5"	 :	"BLDA"	,
            "1742-6"	 :	"SER_PLAS"	,
            "2502-3"	 :	"SER_PLAS"	,
            "1920-8"	 :	"SER_PLAS"	,
            "5804-0"	 :	"URINE"	,
            "26474-7"	 :	"BLD"	,
            "26466-3"	 :	"BODY_FLD"	,
            "5902-2"	 :	"PPP"	,
            "26486-1"	 :	"CSF"	,
            "11557-6"	 :	"BLD"	,
            "26485-3"	 :	"BLD"	,
            "2336-6"	 :	"SER"	,
            "718-7"	 :	"BLD"	,
            "1798-8"	 :	"SER_PLAS"	,
            "1963-8"	 :	"SER"	,
            "26499-4"	 :	"BLD"	,
            "26479-6"	 :	"CSF"	,
            "2500-7"	 :	"SER_PLAS"	,
            "20570-8"	 :	"BLD"	,
            "10501-5"	 :	"SER_PLAS"	,
            "785-6"	 :	"RBC"	,
            "2947-0"	 :	"BLD"	,
            "1751-7"	 :	"SER_PLAS"	,
            "2340-8"	 :	"BLD"	,
            "2324-2"	 :	"SER_PLAS"	,
            "2951-2"	 :	"SER_PLAS"	,
            "2276-4"	 :	"SER_PLAS"	,
            "5797-6"	 :	"URINE"	,
            "4625-0"	 :	"BLD"	,
            "19123-9"	 :	"SER_PLAS"	,
            "728-6"	 :	"BLD"	,
            "33051-4"	 :	"URINE"	,
            "786-4"	 :	"RBC"	,
            "3094-0"	 :	"SER_PLAS"	,
            "43396-1"	 :	"SER_PLAS"	,
            "6718-1"	 :	"SER"	,
            "5770-3"	 :	"URINE"	,
            "3016-3"	 :	"SER_PLAS"	,
            "4546-8"	 :	"BLD"	,
            "26464-8"	 :	"BLD"	,
            "2880-3"	 :	"CSF"	,
            "4548-4"	 :	"BLD"	,
            "3084-1"	 :	"SER_PLAS"	,
            "10839-9"	 :	"SER_PLAS"	,
            "19048-8"	 :	"BLD"	,
            "26478-8"	 :	"BLD"	,
            "20564-1"	 :	"BLD"	,
            "47277-9"	 :	"BLDCO"	,
            "2345-7"	 :	"SER_PLAS"	,
            "2465-3"	 :	"SER_PLAS"	,
            "5803-2"	 :	"URINE"	,
            "2965-2"	 :	"URINE"	,
            "34728-6"	 :	"BLD"	,
            "30428-7"	 :	"RBC"	,
            "30180-4"	 :	"BLD"	,
            "2091-7"	 :	"SER_PLAS"	,
            "5802-4"	 :	"URINE"	,
            "31208-2"	 :	"XXX"	,
            "26444-0"	 :	"BLD"	,
            "30341-2"	 :	"BLD"	,
            "6050-9"	 :	"SER"	,
            "6019-4"	 :	"SER"	,
            "2692-2"	 :	"SER_PLAS"	,
            "10378-8"	 :	"BLD"	,
            "27298-9"	 :	"URINE"	,
            "2342-4"	 :	"CSF"	,
            "6206-7"	 :	"SER"	,
            "30384-2"	 :	"RBC"	,
            "2075-0"	 :	"SER_PLAS"	,
            "17849-1"	 :	"BLD"	,
            "2458-8"	 :	"SER_PLAS"	,
            "26515-7"	 :	"BLD"	,
            "30385-9"	 :	"RBC"	,
            "5792-7"	 :	"URINE"	,
            "2160-0"	 :	"SER_PLAS"	,
            "14959-1"	 :	"URINE"	,
            "38256-4"	 :	"BODY_FLD"	,
            "17861-6"	 :	"SER_PLAS"	,
            "2093-3"	 :	"SER_PLAS"	,
            "26449-9"	 :	"BLD"	,
            "1968-7"	 :	"SER_PLAS"	,
            "8310-5"	 :	"^PATIENT"	,
            "1971-1"	 :	"SER_PLAS"	,
            "2571-8"	 :	"SER_PLAS"	,
            "11282-1"	 :	"BLD"	,
            "2885-2"	 :	"SER_PLAS"	,
            "15152-2"	 :	"SER_PLAS"	,
}


lab_result_cm_lab_result_source_dict = {

    "OD":"OD",

}



lab_result_cm_priority_dict = {

    "EXPEDITE"      :"E",
    "ROUTINE"       :"R",
    "STAT"          :"S",
    "NO INFORMATION":"NI",
    "UNKNOWN"       :"UN",
    "OTHER"         :"OT",
    ""              :"NI",
    
}


lab_result_cm_result_loc_dict = {

    "L":"L",
    "P":"P",
}


lab_result_cm_lab_px_type_dict = {

    "ICD9CM":"09",
    "ICD9":"09",
    "ICD-9-CM":"09",
    "ICD10":"10",
    "ICD10CM":"10",
    "ICD-10-CM":"10",
    "ICD11CM":"11",
    "ICD-11-CM":"11",
    "HUMAN PHENOTYPE ONTOLOGY":"HP",
    "ALGORITHMIC":"AG",
    "SNOMED":"SM",
    "": "NI"

}


lab_result_cm_result_qual_dict = {

        ""	        :	"OT"	, #	Other    
        "DETECTED"   :  "DETECTED",
        "NOT DETECTED" : "NOT DETECTED",
        "POSITIVE"	    :	"POSITIVE"	, #	Positive
        "NEGATIVE"   	:	"NEGATIVE"	, #	Negative
        "BORDERLINE"	:	"BORDERLINE"	, #	Borderline normal
        "HIGH"	        :	"HIGH"	, #	High
        "LOW"	        :	"LOW"	, #	Low
        "NORMAL"	    :	"NORMAL"	, #	Normal range
        "ABNORMAL"	    :	"ABNORMAL"	, #	Abnormal presence of
        "UNDETERMINED"	:	"UNDETERMINED"	, #	Undetermined
        "NO INFROMATION":	"NI"	, #	No information
        "UNKNOWN"	    :	"UN"	, #	Unknown
        "OTHER"	        :	"OT"	, #	Other

}


lab_result_cm_result_modifier_dict = {

            "=":"EQ",#   EQUAL
            "EQ":"EQ",#   EQUAL
            ">=":"GE",#   Greater than or equal to
            ">":"GT",#   Greater than
            "<":"LT",#   Less than
            "<=":"LE",#   Less than or equal to
            "GE":"GE",#   Other
            "LT":"LT",#   Unkown
            "LE":"LE",#   No Information
            "0":"OT",#   Other
            "":"OT",#   Other

}



lab_result_cm_norm_modifier_low_dict = {

            "=":"EQ",#   EQUAL
            "EQ":"EQ",#   EQUAL
            ">=":"GE",#   Greater than or equal to
            ">":"GT",#   Greater than
            "<":"OT",#   Less than
            "<=":"OT",#   Less than or equal to
            "GE":"GE",#   Other
            "LT":"OT",#   Unkown
            "LE":"OT",#   No Information
            "0":"OT",#   Other
            "":"OT",#   Other

}


lab_result_cm_norm_modifier_high_dict = {

            "=":"EQ",#   EQUAL
            "EQ":"EQ",#   EQUAL
            ">=":"OT",#   Greater than or equal to
            ">":"OT",#   Greater than
            "<":"LT",#   Less than
            "<=":"LE",#   Less than or equal to
            "GE":"OT",#   Other
            "LT":"LT",#   Unkown
            "LE":"LE",#   No Information
            "0":"OT",#   Other
            "":"OT",#   Other

}




lab_result_cm_abn_ind_dict = {

    "ABNORMAL":"AB",
    "ABNORMALLY HIGH":"AH",
    "ABNORMALLY LOW":"AL",
    "CRITICALLY HIGH":"CH",
    "CRITICALLY LOW":"CL",
    "CRITICAL":"CR",
    "INCONCLUSIVE":"IN",
    "NORMAL":"NL",
    "NO INFORMATION":"NI",
    "UNKNOWN":"UN",
    "OTHER":"OT",
    "":"NI",
}




lab_result_cm_result_unit_dict = {
            "mg/dL":"mg/dL",
            "%":"%",
            "":"",
            "mMol/L":"mmol/L",
            "10^3/cmm":"mL",
            "gm/dL":"g/dL",
            "fL":"fL",
            "Units/L":"U/L",
            "mL/min/1.73 m2":"mL/min/{1.73_m2}",
            "10^6/cmm":"L",
            "pg":"pg",
            "mmHg":"mm[Hg]",
            "mEq/L-Historical":"meq/L",
            "mEq/L":"meq/L",
            "second(s)":"s",
            "/HPF":"/[HPF]",
            "g/dL-Historical":"g/dL",
            "ng/mL":"ng/mL",
            "VOL_%":"%{vol}",
            "pg/mL":"pg/mL",
            "Sec-Historical":"",
            "mcg/dL":"ug/dL",
            "/LPF":"/[LPF]",
            "mg/L":"mg/L",
            "mInt-unit(s)/mL":"m[IU]/L",
            "ng/dL":"ng/dL",
            "unit(s)/mL":"U/mL",
            "mcg/mL":"ug/mL",
            "mcIntUnits/mL":"u[IU]/mL",
            "/100_WBC":"/100{WBCs}",
            "10^3":"10*3",
            "/cmm":"/mm3",
            "mm/hr":"mm/h",
            "IntUnits/mL":"[IU]/mL",
            "unit(s)":"U",
            "minute(s)":"min",
            "ng/mL DDU":"",
            "copies/mL":"{copies}/mL",
            "mcMol/L":"umol/L",
            "mEq/mL":"meq/mL",
            "degree":"deg",
            "mm":"mm",
            "mg/24H":"mg/(24.h)",
            "mOsm/kg H2O":"mosm/kg",
            "titer":"{titer}",
            "hr":"h",
            "ratio":"{ratio}",
            "L":"L",
            "nMol/L":"nmol/L",
            "Int-unit(s)/L":"[IU]",
            "mOS/kG":"mosm/kg",
            "ISR":"{ISR}",
            "Index":"",
            "mOsm/kg":"mosm/kg",
            "GPL-Units/mL":"",
            "MPL-Units/mL":"",
            "nMol/mL":"nmol/mL",
            "kIntUnits/L":"m[IU]/L",
            "unit(s)/liter":"U/L",
            "L-Historical":"L",
            "mcg/min":"ug/min",
            "m":"",
            "mmol/day":"mmol/(24.h)",
            "mcg/gm":"ug/g",
            "AU/mL":"",
            "mL/min":"mL/min",
            "mEq/24H-Historical":"meq/(24.h)",
            "BG":"",
            "gm":"g",
            "mg":"mg",
            "mEq/24 hr":"meq/(24.h)",
            "mIU/mL":"",
            "log10":"",
            "mg/day":"mg/d",
            "EUunits/mL":"",
            "mL/day":"mL/(24.h)",
            "mGycm2":"",
            "mEq/day":"meq/(24.h)",
            "mcg/L":"ug/L",
            "RU/mL":"",
            "score":"{score}",
            "CU":"",
            "mOs/24hr":"",
            "Units/mL-Historical":"[IU]/mL",
            "pg/dL":"",
            "mcMole/L":"umol/L",
            "mOsm/24hr":"",
            "ga":"",
            "mg/mL":"mg/mL",
            "D":"",
            "unit(s)/hr":"U/h",
            "Units/24H":"[IU]/(24.h)",




}


#  ██▓   ▓█████▄  ██████     ▄▄▄     ▓█████▄▓█████▄ ██▀███ ▓█████  ██████  ██████     ██░ ██ ██▓ ██████▄▄▄█████▓▒█████  ██▀███▓██   ██▓
# ▓██▒   ▒██▀ ██▒██    ▒    ▒████▄   ▒██▀ ██▒██▀ ██▓██ ▒ ██▓█   ▀▒██    ▒▒██    ▒    ▓██░ ██▓██▒██    ▒▓  ██▒ ▓▒██▒  ██▓██ ▒ ██▒██  ██▒
# ▒██░   ░██   █░ ▓██▄      ▒██  ▀█▄ ░██   █░██   █▓██ ░▄█ ▒███  ░ ▓██▄  ░ ▓██▄      ▒██▀▀██▒██░ ▓██▄  ▒ ▓██░ ▒▒██░  ██▓██ ░▄█ ▒▒██ ██░
# ▒██░   ░▓█▄   ▌ ▒   ██▒   ░██▄▄▄▄██░▓█▄   ░▓█▄   ▒██▀▀█▄ ▒▓█  ▄  ▒   ██▒ ▒   ██▒   ░▓█ ░██░██░ ▒   ██░ ▓██▓ ░▒██   ██▒██▀▀█▄  ░ ▐██▓░
# ░██████░▒████▓▒██████▒▒    ▓█   ▓██░▒████▓░▒████▓░██▓ ▒██░▒████▒██████▒▒██████▒▒   ░▓█▒░██░██▒██████▒▒ ▒██▒ ░░ ████▓▒░██▓ ▒██▒░ ██▒▓░
# ░ ▒░▓  ░▒▒▓  ▒▒ ▒▓▒ ▒ ░    ▒▒   ▓▒█░▒▒▓  ▒ ▒▒▓  ▒░ ▒▓ ░▒▓░░ ▒░ ▒ ▒▓▒ ▒ ▒ ▒▓▒ ▒ ░    ▒ ░░▒░░▓ ▒ ▒▓▒ ▒ ░ ▒ ░░  ░ ▒░▒░▒░░ ▒▓ ░▒▓░ ██▒▒▒ 
# ░ ░ ▒  ░░ ▒  ▒░ ░▒  ░ ░     ▒   ▒▒ ░░ ▒  ▒ ░ ▒  ▒  ░▒ ░ ▒░░ ░  ░ ░▒  ░ ░ ░▒  ░ ░    ▒ ░▒░ ░▒ ░ ░▒  ░ ░   ░     ░ ▒ ▒░  ░▒ ░ ▒▓██ ░▒░ 
#   ░ ░   ░ ░  ░░  ░  ░       ░   ▒   ░ ░  ░ ░ ░  ░  ░░   ░   ░  ░  ░  ░ ░  ░  ░      ░  ░░ ░▒ ░  ░  ░   ░     ░ ░ ░ ▒   ░░   ░▒ ▒ ░░  
#     ░  ░  ░         ░           ░  ░  ░      ░      ░       ░  ░     ░       ░      ░  ░  ░░       ░             ░ ░    ░    ░ ░     
#         ░                           ░      ░                                                                                 ░ ░     

lds_address_hx_address_use_dict ={
    "HO":"HO",
    "WO":"WO",
    "TP":"TP",
    "OL":"OL",
    "NI":"NI",
    "UN":"UN",
    "OT":"OT",
    "":"NI",
    "HOME":"HO",
    "WORK":"WO",
    "TEMP":"TP",
    "OLD/INCORRECT":"OL",
    "NO INFORMATION":"NI",
    "UNKNOWN":"UN",
    "OT":"OTHER",



}

lds_address_hx_address_preferred_dict = {

    "Y":"Y",
    "N":"N"
}


lds_address_hx_address_type_dict = {


    "NO INFORMATION":"NI",
    "UNKNOWN":"UN",
    "OT":"OTHER",
    "":"NI",
    "NI":"NI",
    "UN":"UN",
    "OT":"OT",
    "PO":"PO",
    "POSTAL":"PO",
    "PH":"PH",
    "PHYSICAL":"PH",
    "BO":"BO",
    "BOTH":"BO",



}

#  ███▄ ▄███▓█████▓█████▄     ▄▄▄     ▓█████▄ ███▄ ▄███▓██▓███▄    █ 
# ▓██▒▀█▀ ██▓█   ▀▒██▀ ██▌   ▒████▄   ▒██▀ ██▓██▒▀█▀ ██▓██▒██ ▀█   █ 
# ▓██    ▓██▒███  ░██   █▌   ▒██  ▀█▄ ░██   █▓██    ▓██▒██▓██  ▀█ ██▒
# ▒██    ▒██▒▓█  ▄░▓█▄   ▌   ░██▄▄▄▄██░▓█▄   ▒██    ▒██░██▓██▒  ▐▌██▒
# ▒██▒   ░██░▒████░▒████▓     ▓█   ▓██░▒████▓▒██▒   ░██░██▒██░   ▓██░
# ░ ▒░   ░  ░░ ▒░ ░▒▒▓  ▒     ▒▒   ▓▒█░▒▒▓  ▒░ ▒░   ░  ░▓ ░ ▒░   ▒ ▒ 
# ░  ░      ░░ ░  ░░ ▒  ▒      ▒   ▒▒ ░░ ▒  ▒░  ░      ░▒ ░ ░░   ░ ▒░
# ░      ░     ░   ░ ░  ░      ░   ▒   ░ ░  ░░      ░   ▒ ░  ░   ░ ░ 
#        ░     ░  ░  ░             ░  ░  ░          ░   ░          ░ 
#                  ░                   ░                             

med_admin_medadmin_type_dict = {

            'RXNORM': "RX",
            "NDC"   : "ND",
            "NO INFORMATION":"NI", # 
            "UNKNOWN":"UN", # 
            "OTHER":"OT", # 
            "":'OT',
}


med_admin_medadmin_dose_admin_unit_dict = {

            "mg":"mg",
            "":"OT",
            "gm":"OT",
            "unit(s)":"OT",
            "mcg":"ug",
            "mEq":"meq",
            "mMol":"OT",
            "int-unit(s)":"OT",
            "mcg/hr":"ug/h",
            "mg/mL":"mg/mL",
            "mil-unit(s)":"OT",
            "mg/m2":"mg/m2",
            "mg/day":"ug/d",
            "mg/kg":"mg/kg",
            "mg/hr":"OT",
            "mL":"mL",
            "unit(s)/kg":"OT",
            "mil-int-unit(s)":"OT",
            "mcg/kg/min":"ug/kg/min",
            "unit(s)/mL":"OT",
            "mCi":"",
            "mcg/mL":"OT",
            "EA":"OT",
            "mcg/kg":"ug/kg",
            "gm/day":"OT",
            "mcg/puff":"OT",
            "int-unit(s)/day":"OT",
            "mg/dL":"mg/dL",
            "gm/mL":"OT",
            "mEq/mL":"meq/mL",
            "mg/kg/min":"mg/kg/min",
            "mEq/kg":"meq/kg",
            "mcg/day":"OT",
            "mL/kg/hr":"mL/kg/h",
            "unit(s)/m2":"OT",
            "mcg/min":"ug/min",
            "mcg/kg/hr":"ug/kg/h",
            "mg/kg/hr":"mg/kg/h",
            "unit(s)/hr":"OT",
            "mMol/kg":"OT",
            "mg/gm":"OT",
            "ng/kg/min":"ng/kg/min",
            "mg/m2/day":"",
            "gm/kg":"OT",
            "int-unit(s)/kg":"OT",
            "mg/kg/dose":"OT",
            "mEq/hr":"meq/h",
            "ng":"ng",
            "gm/m2":"",
            "tab(s)":"OT",
            "mEq/kg/hr":"meq/kg/h",
            "-gm/kg(TPN)":"OT",
            "int-unit(s)/m2":"OT",
            "AUC Carboplatin":"OT",
            "cap(s)":"OT",
            "kg":"kg",
            "tuberc-unit(s)":"OT",
            "th-unit(s)":"OT",
            "mg/min":"mg/min",
            "mL/kg":"mL/kg",
            "mEq/L":"meq/L",
            "mEq/day":"meq/d",
            "mcg/L":"OT",
            "gm/dL":"OT",
            "mg/kg/day":"ug/kg/d",
            "gm/hr":"",
            "th-int-unit(s)":"OT",
            "mcg/dL":"OT",
            "unit(s)/liter":"OT",
            "mcg/kg/day":"ug/kg/d",
            "unit(s)/min":"OT",
            "inch(es)":"OT",
            "Int-unit(s)/L":"OT",
            "mcg/kg/dose":"OT",
            "mcg/m2":"OT",
            "int-unit(s)/liter":"OT",
            "gm/kg/dose":"OT",
            "-mcg/kg(TPN)":"OT",
            "-unit(s)/mL_(TPN)":"OT",
            "vial(s)":"OT",
            "mEq/liter":"OT",
            "patch(es)":"OT",
            "mil-unit(s)/gm":"OT",
            "ng/mL":"ng/mL",
            "unit(s)/kg/day":"OT",
            "packet(s)":"OT",
            "mEq/kg/dose":"OT",
            "unit(s)/kg/hr":"OT",
            "millionunits/m2":"OT",








}


med_admin_medadmin_route_dict = {

           "ORAL" : "ORAL",
           "INTRAVENOUS" : "INTRAVENOUS",
           "SUBCUTANEOUS" : "SUBCUTANEOUS",       
           "TOPICAL" : "TOPICAL",
           "NASAL" : "NASAL",
           "RECTAL" : "RECTAL",
           "INTRAOCULAR" : "INTRAOCULAR",
           "URETHRAL" : "URETHRAL",
           "INTRATHECAL" : "INTRATHECAL",
           "":"OT"

}


med_admin_medadmin_source_dict = {


    "OD":"OD"
}

#  ██▓███  ██▀███ ▓█████  ██████ ▄████▄  ██▀███  ██▓▄▄▄▄   ██▓███▄    █  ▄████ 
# ▓██░  ██▓██ ▒ ██▓█   ▀▒██    ▒▒██▀ ▀█ ▓██ ▒ ██▓██▓█████▄▓██▒██ ▀█   █ ██▒ ▀█▒
# ▓██░ ██▓▓██ ░▄█ ▒███  ░ ▓██▄  ▒▓█    ▄▓██ ░▄█ ▒██▒██▒ ▄█▒██▓██  ▀█ ██▒██░▄▄▄░
# ▒██▄█▓▒ ▒██▀▀█▄ ▒▓█  ▄  ▒   ██▒▓▓▄ ▄██▒██▀▀█▄ ░██▒██░█▀ ░██▓██▒  ▐▌██░▓█  ██▓
# ▒██▒ ░  ░██▓ ▒██░▒████▒██████▒▒ ▓███▀ ░██▓ ▒██░██░▓█  ▀█░██▒██░   ▓██░▒▓███▀▒
# ▒▓▒░ ░  ░ ▒▓ ░▒▓░░ ▒░ ▒ ▒▓▒ ▒ ░ ░▒ ▒  ░ ▒▓ ░▒▓░▓ ░▒▓███▀░▓ ░ ▒░   ▒ ▒ ░▒   ▒ 
# ░▒ ░      ░▒ ░ ▒░░ ░  ░ ░▒  ░ ░ ░  ▒    ░▒ ░ ▒░▒ ▒░▒   ░ ▒ ░ ░░   ░ ▒░ ░   ░ 
# ░░        ░░   ░   ░  ░  ░  ░ ░         ░░   ░ ▒ ░░    ░ ▒ ░  ░   ░ ░░ ░   ░ 
#            ░       ░  ░     ░ ░ ░        ░     ░  ░      ░          ░      ░ 
#                               ░                        ░                     


prescribing_rx_dose_ordered_unit_dict = {
            "mg":"mg",
            "":"OT",
            "mcg":"ug",
            "gm":"OT",
            "unit(s)":"OT",
            "mEq":"meq",
            "int-unit(s)":"OT",
            "mL":"mL",
            "mg/mL":"mg/mL",
            "mcg/hr":"ug/h",
            "mg/day":"ug/d",
            "mg/kg":"mg/kg",
            "mil-unit(s)":"OT",
            "unit(s)/kg":"OT",
            "mCi":"",
            "mg/m2":"mg/m2",
            "mcg/kg/min":"ug/kg/min",
            "ng/kg/min":"ng/kg/min",
            "mcg/kg":"ug/kg",
            "mg/hr":"OT",
            "mil-int-unit(s)":"OT",
            "mg/dL":"mg/dL",
            "mcg/mL":"OT",
            "unit(s)/mL":"OT",
            "gm/mL":"OT",
            "mEq/mL":"",
            "mL/kg/hr":"mL/kg/h",
            "mcg/m2":"OT",
            "gm/dL":"OT",
            "mg/kg/day":"ug/kg/d",
            "mcg/puff":"OT",
            "unit(s)/kg/hr":"OT",
            "mL/kg":"mL/kg",
            "ng/mL":"ng/mL",
            "mEq/L":"",
            "mL/mL":"",
            "unit(s)/hr":"OT",
            "mEq/kg/hr":"",





}


prescribing_rx_dose_form_dict = {
        "":"",
}

prescribing_rx_prn_flag_dict = {

        "N":"N",
        "Y":"Y",
        "AS NEEDED":"Y",
        "":"",

}


prescribing_rx_route_dict = {

           "ORAL" : "ORAL",
           "INTRAVENOUS" : "INTRAVENOUS",
           "SUBCUTANEOUS" : "SUBCUTANEOUS",       
           "TOPICAL" : "TOPICAL",
           "NASAL" : "NASAL",
           "RECTAL" : "RECTAL",
           "INTRAOCULAR" : "INTRAOCULAR",
           "URETHRAL" : "URETHRAL",
           "INTRATHECAL" : "INTRATHECAL",
           "":"OT"

}

prescribing_rx_basis_dict = {

        "PRESCRIPTION WRITTEN":"01",
        "PRESCRIPTION":"01",
        "HOME-MED":"01",   
        "PRESCRIPTION DISPENSED IN PHARMACY":"01",   
        "PHYSICIAN ADMINISTERED DRUG (IDENTIFIED FROM EHR ORDER)":"02",   
        "":"NI",

}

prescribing_rx_source_dict = {

    "OD":"OD"
}




prescribing_rx_frequency_dict = {
 "30000000|2384745045":"OT",
        "30000000|2337377229":"OT",
        "30000000|2200324447":"02",
        "30000000|1782899353":"01",
        "30000000|1782897725":"01",
        "30000000|1769639975":"OT",
        "30000000|1612254461":"01",
        "30000000|1612252939":"01",
        "30000000|1566974993":"OT",
        "30000000|1478944991":"03",
        "30000000|1373794521":"OT",
        "30000000|1041929101":"02",
        "30000000|1025624759":"01",
        "30000000|952028145":"02",
        "30000000|901526265":"OT",
        "30000000|892104019":"OT",
        "30000000|786310639":"OT",
        "30000000|534644379":"02",
        "30000000|534642345":"02",
        "30000000|521122297":"01",
        "30000000|521122090":"OT",
        "30000000|460403157":"01",
        "30000000|458671896":"01",
        "30000000|341209969":"02",
        "30000000|330841481":"OT",
        "30000000|325420592":"NI",
        "30000000|325420587":"NI",
        "30000000|303942368":"OT",
        "30000000|267017365":"02",
        "30000000|267017153":"04",
        "30000000|247812999":"OT",
        "30000000|247626071":"02",
        "30000000|246984487":"OT",
        "30000000|246984286":"OT",
        "30000000|246907619":"03",
        "30000000|246907463":"OT",
        "30000000|246907223":"OT",
        "30000000|241148818":"OT",
        "30000000|223763882":"OT",
        "30000000|223763851":"OT",
        "30000000|223763813":"OT",
        "30000000|209363662":"OT",
        "30000000|196300645":"OT",
        "30000000|194065426":"02",
        "30000000|194048166":"02",
        "30000000|194045301":"02",
        "30000000|182654240":"02",
        "30000000|142861689":"03",
        "30000000|132240170":"OT",
        "30000000|111554602":"01",
        "30000000|111553448":"OT",
        "30000000|111553096":"OT",
        "30000000|104043242":"01",
        "30000000|98058860":"OT",
        "30000000|80343996":"02",
        "30000000|76745074":"02",
        "30000000|76705140":"02",
        "30000000|76691886":"02",
        "30000000|76676658":"02",
        "30000000|76659652":"OT",
        "30000000|76528337":"OT",
        "30000000|76527304":"03",
        "30000000|76526594":"02",
        "30000000|76514603":"03",
        "30000000|76503975":"02",
        "30000000|76481254":"02",
        "30000000|76470153":"02",
        "30000000|76462335":"02",
        "30000000|76447970":"OT",
        "30000000|76066964":"OT",
        "30000000|67992426":"OT",
        "30000000|67990308":"OT",
        "30000000|66730794":"OT",
        "30000000|66730511":"OT",
        "30000000|56285230":"OT",
        "30000000|52504016":"01",
        "30000000|52246700":"OT",
        "30000000|45115896":"OT",
        "30000000|41450413":"OT",
        "30000000|40159516":"OT",
        "30000000|37803653":"OT",
        "30000000|34308538":"OT",
        "30000000|33913613":"01",
        "30000000|33765164":"OT",
        "30000000|33478031":"OT",
        "30000000|31547963":"OT",
        "30000000|31542598":"OT",
        "30000000|29746172":"OT",
        "30000000|29614907":"OT",
        "30000000|25646401":"OT",
        "30000000|25646242":"OT",
        "30000000|24975052":"01",
        "30000000|24139065":"OT",
        "30000000|8196848":"OT",
        "30000000|8196598":"OT",
        "30000000|8195311":"OT",
        "30000000|8194909":"OT",
        "30000000|6806576":"OT",
        "30000000|6501903":"OT",
        "30000000|5813223":"02",
        "30000000|5813214":"03",
        "30000000|5813200":"03",
        "30000000|5813178":"02",
        "30000000|5813154":"04",
        "30000000|5813116":"04",
        "30000000|5813063":"OT",
        "30000000|5652604":"OT",
        "30000000|5652601":"OT",
        "30000000|5652600":"OT",
        "30000000|5652597":"OT",
        "30000000|5652596":"OT",
        "30000000|5652594":"OT",
        "30000000|5652590":"OT",
        "30000000|5652587":"OT",
        "30000000|5652580":"OT",
        "30000000|3850663":"OT",
        "30000000|3697312":"OT",
        "30000000|3592248":"OT",
        "30000000|3542964":"OT",
        "30000000|3530020":"OT",
        "30000000|3530019":"OT",
        "30000000|3530018":"OT",
        "30000000|3530017":"OT",
        "30000000|3530016":"OT",
        "30000000|3517054":"OT",
        "30000000|3517051":"OT",
        "30000000|3517049":"OT",
        "30000000|3517048":"OT",
        "30000000|3517047":"OT",
        "30000000|3517043":"OT",
        "30000000|3517042":"OT",
        "30000000|3517037":"OT",
        "30000000|3517035":"OT",
        "30000000|3517031":"OT",
        "30000000|3517027":"OT",
        "30000000|3517007":"OT",
        "30000000|3517005":"OT",
        "30000000|3517003":"OT",
        "30000000|3517000":"OT",
        "30000000|3516994":"OT",
        "30000000|3516990":"OT",
        "30000000|3516988":"OT",
        "30000000|3516980":"OT",
        "30000000|3516954":"OT",
        "30000000|3498418":"OT",
        "30000000|3498417":"OT",
        "30000000|3498414":"OT",
        "30000000|3498413":"OT",
        "30000000|3498412":"OT",
        "30000000|3498411":"OT",
        "30000000|3498410":"OT",
        "30000000|3498407":"OT",
        "30000000|3498402":"OT",
        "30000000|3498401":"OT",
        "30000000|3498400":"OT",
        "30000000|3498399":"OT",
        "30000000|3496990":"OT",
        "30000000|3496989":"OT",
        "30000000|3496988":"OT",
        "30000000|3496987":"OT",
        "30000000|3496986":"OT",
        "30000000|3496983":"OT",
        "30000000|3496982":"OT",
        "30000000|3496977":"OT",
        "30000000|3496976":"OT",
        "30000000|3496270":"OT",
        "30000000|3496252":"OT",
        "30000000|3496251":"OT",
        "30000000|3496250":"OT",
        "30000000|3496235":"OT",
        "30000000|3496234":"OT",
        "30000000|3496233":"OT",
        "30000000|3495482":"OT",
        "30000000|3495457":"02",
        "30000000|3495456":"01",
        "30000000|3495446":"01",
        "30000000|3495441":"OT",
        "30000000|3495428":"02",
        "30000000|3495413":"OT",
        "30000000|3494365":"OT",
        "30000000|3494359":"OT",
        "30000000|3494349":"OT",
        "30000000|3494343":"OT",
        "30000000|3494335":"OT",
        "30000000|3494326":"OT",
        "30000000|3494303":"OT",
        "30000000|3494298":"OT",
        "30000000|3494286":"OT",
        "30000000|3494277":"OT",
        "30000000|3494266":"OT",
        "30000000|3494261":"OT",
        "30000000|3494256":"OT",
        "30000000|3494249":"OT",
        "30000000|3494241":"OT",
        "30000000|3494235":"OT",
        "30000000|3494188":"OT",
        "30000000|3494171":"OT",
        "30000000|3494169":"OT",
        "30000000|3494163":"OT",
        "30000000|3494152":"OT",
        "30000000|3494037":"OT",
        "30000000|3494010":"OT",
        "30000000|3491470":"OT",
        "30000000|3491463":"OT",
        "30000000|3491457":"OT",
        "30000000|3491453":"OT",
        "30000000|3491388":"OT",
        "30000000|3491383":"OT",
        "30000000|3491373":"OT",
        "30000000|3486584":"OT",
        "30000000|3486578":"OT",
        "30000000|3486577":"OT",
        "30000000|3486576":"OT",
        "30000000|3486566":"OT",
        "30000000|3486563":"OT",
        "30000000|3486562":"OT",
        "30000000|3486561":"OT",
        "30000000|3486559":"OT",
        "30000000|3486365":"OT",
        "30000000|3486359":"OT",
        "30000000|3486313":"OT",
        "30000000|3472275":"OT",
        "30000000|3421384":"OT",
        "30000000|3421070":"03",
        "30000000|3405120":"02",
        "30000000|3405100":"OT",
        "30000000|3405095":"OT",
        "30000000|3405091":"OT",
        "30000000|3405084":"OT",
        "30000000|3404897":"OT",
        "30000000|3404873":"OT",
        "30000000|3404864":"OT",
        "30000000|3404856":"OT",
        "30000000|3404851":"OT",
        "30000000|3404843":"OT",
        "30000000|3404835":"OT",
        "30000000|3404827":"OT",
        "30000000|3404774":"02",
        "30000000|3404632":"OT",
        "30000000|3404600":"OT",
        "30000000|3404561":"04",
        "30000000|3404547":"OT",
        "30000000|3404526":"OT",
        "30000000|3404524":"01",
        "30000000|3404523":"OT",
        "30000000|3404456":"OT",
        "30000000|3404446":"OT",
        "30000000|3404435":"OT",
        "30000000|3404431":"OT",
        "30000000|3404424":"OT",
        "30000000|3404412":"OT",
        "30000000|3403776":"01",
        "30000000|3403630":"OT",
        "30000000|3402233":"02",
        "30000000|3402176":"01",
        "30000000|3344931":"OT",
        "30000000|3268237":"OT",
        "30000000|3268234":"03",
        "30000000|3268184":"OT",
        "30000000|3268183":"02",
        "30000000|3268182":"OT",
        "30000000|3268170":"03",
        "30000000|3267697":"02",
        "30000000|3267485":"02",
        "30000000|3267479":"01",
        "30000000|3267407":"OT",
        "30000000|3267406":"OT",
        "30000000|3267405":"OT",
        "30000000|3267404":"02",
        "30000000|3267032":"OT",
        "30000000|3267031":"09",
        "30000000|3267030":"02",
        "30000000|3263822":"01",
        "30000000|3263821":"01",
        "30000000|3260744":"OT",
        "30000000|3260694":"01",
        "30000000|3260629":"01",
        "30000000|3260626":"01",
        "30000000|3260614":"08",
        "30000000|3254051":"OT",
        "30000000|3254050":"OT",
        "30000000|3254049":"OT",
        "30000000|3254046":"OT",
        "30000000|3254045":"OT",
        "30000000|3254044":"OT",
        "30000000|3254043":"OT",
        "30000000|3254041":"2",
        "30000000|3254029":"2",
        "30000000|3253890":"OT",
        "30000000|3253888":"OT",
        "30000000|3245964":"01",
        "30000000|3245893":"07",
        "30000000|3239159":"OT",
        "30000000|3239147":"02",
        "30000000|3239144":"OT",
        "30000000|3238978":"04",
        "30000000|3194727":"07",
        "30000000|696617":"OT",
        "30000000|696616":"OT",
        "30000000|696615":"OT",
        "30000000|696614":"OT",
        "30000000|696613":"OT",
        "30000000|696612":"OT",
        "30000000|696611":"OT",
        "30000000|696610":"OT",
        "30000000|696609":"OT",
        "30000000|696608":"02",
        "30000000|696607":"03",
        "30000000|696606":"04",
        "30000000|696605":"04",
        "30000000|696604":"OT",
        "30000000|696603":"OT",
        "30000000|696602":"01",
        "30000000|696601":"OT",
        "30000000|696600":"OT",
        "30000000|696599":"OT",
        "30000000|696598":"OT",
        "30000000|696597":"OT",
        "30000000|696596":"OT",
        "30000000|696595":"OT",
        "30000000|696594":"OT",
        "30000000|696593":"OT",
        "30000000|696592":"OT",
        "30000000|696591":"OT",
        "30000000|696590":"OT",
        "30000000|696589":"OT",
        "30000000|696588":"OT",
        "30000000|696587":"OT",
        "30000000|696586":"OT",
        "30000000|696585":"OT",
        "30000000|696584":"OT",
        "30000000|696583":"OT",
        "30000000|696582":"OT",
        "30000000|696581":"OT",
        "30000000|696580":"OT",
        "30000000|696579":"OT",
        "30000000|696578":"OT",
        "30000000|696577":"OT",
        "30000000|696576":"OT",
        "30000000|696575":"OT",
        "30000000|696574":"OT",
        "30000000|696573":"OT",
        "30000000|696572":"OT",
        "30000000|696571":"OT",
        "30000000|696570":"OT",
        "30000000|696569":"OT",
        "30000000|696568":"OT",
        "30000000|696567":"OT",
        "30000000|696566":"OT",
        "30000000|696565":"OT",
        "30000000|696564":"03",
        "30000000|696563":"03",
        "30000000|696562":"OT",
        "30000000|696561":"04",
        "30000000|696560":"01",
        "30000000|696559":"01",
        "30000000|696558":"01",
        "30000000|696557":"01",
        "30000000|696556":"OT",
        "30000000|696555":"03",
        "30000000|696554":"OT",
        "30000000|696553":"04",
        "30000000|696552":"OT",
        "30000000|696551":"OT",
        "30000000|696550":"OT",
        "30000000|696549":"OT",
        "30000000|696548":"OT",
        "30000000|696547":"OT",
        "30000000|696546":"OT",
        "30000000|696545":"OT",
        "30000000|696544":"OT",
        "30000000|696543":"OT",
        "30000000|696542":"OT",
        "30000000|696541":"OT",
        "30000000|696540":"01",
        "30000000|696539":"OT",
        "30000000|696538":"OT",
        "30000000|696537":"OT",
        "30000000|696536":"02",
        "30000000|696535":"OT",
        "30000000|696534":"OT",
        "30000000|696533":"2",
        "30000000|696532":"2",
        "30000000|696531":"OT",
        "30000000|696530":"01",
        "30000000|696529":"03",
        "30000000|696528":"02",
        "30000000|673994":"OT",
        "30000000|29":"OT",
        "30000000|18675958":"OT",
        "30000000|18432":"OT",
        "30000000|18676218":"OT",
        "30000000|46":"OT",
        "30000000|34":"OT",
        "30000000|47":"OT",
        "30000000|24":"OT",
        "30000000|20104":"OT",
        "30000000|18249":"OT",
        "30000000|142111":"OT",
        "30000000|48":"OT",
        "30000000|18675949":"OT",
        "30000000|18676967":"OT",
        "30000000|18905855":"OT",
        "30000000|18677493":"OT",
        "30000000|18676770":"OT",
        "30000000|18676172":"OT",
        "30000000|18675808":"OT",
        "30000000|18675714":"OT",
        "30000000|18675913":"OT",
        "30000000|19069224":"OT",
        "30000000|19069126":"OT",
        "30000000|18677438":"OT",
        "30000000|11560":"OT",
        "30000000|18676798":"OT",
        "30000000|18675716":"OT",
        "30000000|19069127":"OT",
        "30000000|32130":"OT",
        "30000000|40":"OT",
        "30000000|18677569":"OT",
        "30000000|19072577":"OT",
        "30000000|18675947":"OT",
        "30000000|18675768":"OT",
        "30000000|18410":"OT",
        "30000000|18677458":"OT",
        "30000000|18677486":"OT",
        "30000000|18677486":"OT",
        "30000000|18985815":"OT",
        "30000000|18985815":"OT",
        "30000000|12226":"OT",
        "30000000|":"NI",
        "0":"OT",
        "EVERY 24 HOURS' THEN '01": "1",
        "EVERY 12 HOURS' ,'EVERY 12 HOURS RT','EVERY 12 HOURS SCHEDULED'": "2",
        "3 TIMES DAILY": "3",
        "4 TIMES DAILY RT' ,'4 TIMES DAILY WITH MEALS AND NIGHTLY','4 TIMES DAILY PRN": "4",
        "EVERY MORNING": "5",
        "EVERY AFTERNOON": "6",
        "2 TIMES DAILY BEFORE MEALS','2 TIMES DAILY BEFORE MEALS PRN','2 TIMES DAILY BEFORE MEALS','3 TIMES DAILY BEFORE MEALS": "7",
        "2 TIMES DAILY AFTER MEALS PRN','2 TIMES DAILY AFTER MEALS','3 TIMES DAILY AFTER MEALS": "8",
        "EVERY EVENING": "10",
        "ONCE": "11",
        "*UNKNOWN,*UNSPECIFIED": "UN",
        "CUSTOM,*NOT APPLICABLE": "OT",

}




#  ▒█████  ▄▄▄▄    ██████     ▄████▄  ██▓    ██▓███▄    █ 
# ▒██▒  ██▓█████▄▒██    ▒    ▒██▀ ▀█ ▓██▒   ▓██▒██ ▀█   █ 
# ▒██░  ██▒██▒ ▄█░ ▓██▄      ▒▓█    ▄▒██░   ▒██▓██  ▀█ ██▒
# ▒██   ██▒██░█▀   ▒   ██▒   ▒▓▓▄ ▄██▒██░   ░██▓██▒  ▐▌██▒
# ░ ████▓▒░▓█  ▀█▒██████▒▒   ▒ ▓███▀ ░██████░██▒██░   ▓██░
# ░ ▒░▒░▒░░▒▓███▀▒ ▒▓▒ ▒ ░   ░ ░▒ ▒  ░ ▒░▓  ░▓ ░ ▒░   ▒ ▒ 
#   ░ ▒ ▒░▒░▒   ░░ ░▒  ░ ░     ░  ▒  ░ ░ ▒  ░▒ ░ ░░   ░ ▒░
# ░ ░ ░ ▒  ░    ░░  ░  ░     ░         ░ ░   ▒ ░  ░   ░ ░ 
#     ░ ░  ░           ░     ░ ░         ░  ░░          ░ 
#               ░            ░                            

obs_clin_obsclin_type_dict = {


    "LC":"LC",
    "SM":"SM",
    "LOINC":"LC",
    "SNOMED":"SM",
    "": "NI"
}


obs_clin_obsclin_result_qual_dict = {

                "ABNORMAL": "ABNORMAL",
                "BORDERLINE": "BORDERLINE",
                "ELEVATED": "ELEVATED",
                "HIGH": "HIGH",
                "LOW": "LOW",
                "NEGATIVE": "NEGATIVE",
                "NI": "NI",
                "NORMAL": "NORMAL",
                "OT": "OT",
                "POSITIVE": "POSITIVE",
                "UN": "UN",
                "UNDETECTABLE": "UNDETECTABLE",
                "UNDETERMINED": "UNDETERMINED",

}

obs_clin_obsclin_result_modifier_dict = {
            "<=":"LE",
            ">=":"GE",
            "<":"LT",
            "=":"EQ",
            ">":"GT",
            "":"NI",

}







obs_clin_obsclin_result_unit_dict = {
        "":"",
        "%":"%",
        "":"[lb_av]",
        "BPM":"",
        "lbs":"[lb_av]",
        "mm":"mm",
        "CM":"cm",
        "KG":"kg",
        "WEEKS":"wk",
        " infant nasal":"",
        "in":"",
        "Lb":"",
        " FI":"",
        "17":"",
        "18":"",
        " TRAUMATIZ":"",




}

obs_clin_obsclin_source_dict = {
            "NLP DERIVED"                  :"DR" ,
            "INFERRED FROM CLAIM"          :"CL" ,
            "OBSERVATION FROM MEASUREMENT" :"DR" ,
            "PROBLEM LIST FROM EHR"        :"DR" ,
            "LAB OBSERVATION NUMERIC RESULT" :"DR" ,
            "LAB OBSERVATION TEXT"         :"DR" ,
            "LAB OBSERVATION CONCEPT CODE RESULT" :"" ,
            "OBSERVATION RECORDED FROM EHR" :"DR" ,
            "OBSERVATION RECORDED FROM EHR WITH TEXT RESULT" :"DR" ,
            "CHIEF COMPLAINT"              :"OT" ,
            "REFERRAL RECORD"              :"OT",
            "HRA OBSERVATION NUMERIC RESULT" :"DR" ,
            "HRA OBSERVATION TEXT"         :"DR" ,
            "PATIENT REPORTED"             :"OT" ,
            "OBSERVATION RECORDED FROM A SURVEY" :"OT" ,
  

}



obs_clin_obsclin_abn_ind_dict = {

"":"",
}


#  ▒█████  ▄▄▄▄    ██████      ▄████▓█████ ███▄    █ 
# ▒██▒  ██▓█████▄▒██    ▒     ██▒ ▀█▓█   ▀ ██ ▀█   █ 
# ▒██░  ██▒██▒ ▄█░ ▓██▄      ▒██░▄▄▄▒███  ▓██  ▀█ ██▒
# ▒██   ██▒██░█▀   ▒   ██▒   ░▓█  ██▒▓█  ▄▓██▒  ▐▌██▒
# ░ ████▓▒░▓█  ▀█▒██████▒▒   ░▒▓███▀░▒████▒██░   ▓██░
# ░ ▒░▒░▒░░▒▓███▀▒ ▒▓▒ ▒ ░    ░▒   ▒░░ ▒░ ░ ▒░   ▒ ▒ 
#   ░ ▒ ▒░▒░▒   ░░ ░▒  ░ ░     ░   ░ ░ ░  ░ ░░   ░ ▒░
# ░ ░ ░ ▒  ░    ░░  ░  ░     ░ ░   ░   ░     ░   ░ ░ 
#     ░ ░  ░           ░           ░   ░  ░        ░ 
#               ░                                    

obs_gen_obsgen_type_dict = {

    "LC":"LC",
    "SM":"SM",
    "LOINC":"LC",
    "SNOMED":"SM",
    "": "NI"
}

obs_gen_obsgen_result_qual_dict = {

                "ABNORMAL": "ABNORMAL",
                "BORDERLINE": "BORDERLINE",
                "ELEVATED": "ELEVATED",
                "HIGH": "HIGH",
                "LOW": "LOW",
                "NEGATIVE": "NEGATIVE",
                "NI": "NI",
                "NORMAL": "NORMAL",
                "OT": "OT",
                "POSITIVE": "POSITIVE",
                "UN": "UN",
                "UNDETECTABLE": "UNDETECTABLE",
                "UNDETERMINED": "UNDETERMINED",
}


obs_gen_obsgen_result_modifier_dict = {

            "<=":"LE",
            ">=":"GE",
            "<":"LT",
            "=":"EQ",
            ">":"GT",
            "":"NI",

}

obs_gen_obsgen_result_unit_dict = {

       "":"",
        "%":"%",
        "":"[lb_av]",
        "BPM":"",
        "lbs":"[lb_av]",
        "mm":"mm",
        "CM":"cm",
        "KG":"kg",
        "WEEKS":"wk",
        " infant nasal":"",
        "in":"",
        "Lb":"",
        " FI":"",
        "17":"",
        "18":"",
        " TRAUMATIZ":"",

}

obs_gen_obsgen_source_dict = {

            "NLP DERIVED"                  :"DR" ,
            "INFERRED FROM CLAIM"          :"CL" ,
            "OBSERVATION FROM MEASUREMENT" :"DR" ,
            "PROBLEM LIST FROM EHR"        :"DR" ,
            "LAB OBSERVATION NUMERIC RESULT" :"DR" ,
            "LAB OBSERVATION TEXT"         :"DR" ,
            "LAB OBSERVATION CONCEPT CODE RESULT" :"" ,
            "OBSERVATION RECORDED FROM EHR" :"DR" ,
            "OBSERVATION RECORDED FROM EHR WITH TEXT RESULT" :"DR" ,
            "CHIEF COMPLAINT"              :"OT" ,
            "REFERRAL RECORD"              :"OT",
            "HRA OBSERVATION NUMERIC RESULT" :"DR" ,
            "HRA OBSERVATION TEXT"         :"DR" ,
            "PATIENT REPORTED"             :"OT" ,
            "OBSERVATION RECORDED FROM A SURVEY" :"OT" ,
  

}

obs_gen_obsgen_abn_ind_dict = {

"":"",
}


#  ██▒   █▓██▄▄▄█████▓▄▄▄      ██▓    
# ▓██░   █▓██▓  ██▒ ▓▒████▄   ▓██▒    
#  ▓██  █▒▒██▒ ▓██░ ▒▒██  ▀█▄ ▒██░    
#   ▒██ █░░██░ ▓██▓ ░░██▄▄▄▄██▒██░    
#    ▒▀█░ ░██░ ▒██▒ ░ ▓█   ▓██░██████▒
#    ░ ▐░ ░▓   ▒ ░░   ▒▒   ▓▒█░ ▒░▓  ░
#    ░ ░░  ▒ ░   ░     ▒   ▒▒ ░ ░ ▒  ░
#      ░░  ▒ ░ ░       ░   ▒    ░ ░   
#       ░  ░               ░  ░   ░  ░
#      ░                              


vital_bp_position_dict ={
    "":"",
}
vital_vital_source_dict ={
    "":"",
}
vital_smoking_dict ={
    "":"",
}
vital_tobacco_dict ={
    "":"",
}
vital_tobacco_type_dict ={
    "":"",
}