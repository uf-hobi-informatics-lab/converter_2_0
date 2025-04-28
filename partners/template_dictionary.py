 # Template file for building partner specific dictionaries
 # Must contain a dictionary for every column even if there is no mapping taking place
 # i.e. if you are not mapping race there still needs to be a dictionary 
 #  demographic_race_dict : {
 #  '':''
 #  }
 # See line 144 for example
 # Mappings may also be to and from the same value, see line 166 for example                                                                                                                                                                                                                                  
 # Dictionaries will be named table_column_dict
 # column is the full cdm name of the column

# To create the dictionary mappings for any table and column (result_unit as example):
#  SELECT concat('"',replace(replace(RAW_UNIT, '}', '\}'), '{', '\{') collate SQL_Latin1_General_CP1_CS_AS,'":"', replace(replace(RESULT_UNIT, '}', '\}'), '{', '\{'),'",')
#   FROM [CHAR_USF].[dbo].[lab_result_cm] group by  RAW_UNIT, RESULT_UNIT order by count(*) desc




# ▓█████▄▓█████ ███▄ ▄███▓▒█████   ▄████ ██▀███  ▄▄▄      ██▓███  ██░ ██ ██▓▄████▄  
# ▒██▀ ██▓█   ▀▓██▒▀█▀ ██▒██▒  ██▒██▒ ▀█▓██ ▒ ██▒████▄   ▓██░  ██▓██░ ██▓██▒██▀ ▀█  
# ░██   █▒███  ▓██    ▓██▒██░  ██▒██░▄▄▄▓██ ░▄█ ▒██  ▀█▄ ▓██░ ██▓▒██▀▀██▒██▒▓█    ▄ 
# ░▓█▄   ▒▓█  ▄▒██    ▒██▒██   ██░▓█  ██▒██▀▀█▄ ░██▄▄▄▄██▒██▄█▓▒ ░▓█ ░██░██▒▓▓▄ ▄██▒
# ░▒████▓░▒████▒██▒   ░██░ ████▓▒░▒▓███▀░██▓ ▒██▒▓█   ▓██▒██▒ ░  ░▓█▒░██░██▒ ▓███▀ ░
#  ▒▒▓  ▒░░ ▒░ ░ ▒░   ░  ░ ▒░▒░▒░ ░▒   ▒░ ▒▓ ░▒▓░▒▒   ▓▒█▒▓▒░ ░  ░▒ ░░▒░░▓ ░ ░▒ ▒  ░
#  ░ ▒  ▒ ░ ░  ░  ░      ░ ░ ▒ ▒░  ░   ░  ░▒ ░ ▒░ ▒   ▒▒ ░▒ ░     ▒ ░▒░ ░▒ ░ ░  ▒   
#  ░ ░  ░   ░  ░      ░  ░ ░ ░ ▒ ░ ░   ░  ░░   ░  ░   ▒  ░░       ░  ░░ ░▒ ░       
                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                                                                                                                                                                                                              

demographic_sex_dict = { # the key is what we receive from the partner, value is the CDM 
            "0":"OT", # receive 0 from partner map to OT
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
            
            "":"OT", # we receive nothing from partner map to OT
            
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

}


death_death_source_dict = { # example of no mapping being done but dictionary is present

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



condition_condition_status_dict = { # Mappings may be to itself but is still needed

    "AC":"AC",
    "RS":"RS",

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



# To create the units mappings from lab_result:
#  SELECT concat('"',replace(replace(RAW_UNIT, '}', '\}'), '{', '\{') collate SQL_Latin1_General_CP1_CS_AS,'":"', replace(replace(RESULT_UNIT, '}', '\}'), '{', '\{'),'",')
#   FROM [CHAR_USF].[dbo].[lab_result_cm] group by  RAW_UNIT, RESULT_UNIT order by count(*) desc


lab_result_cm_result_unit_dict = {
"%":"%",
"MG/DL":"mg/dL",
"":"",
"MEQ/L":"meq/L",
"g/dL":"g/dL",
"fL":"fL",
"ML/MIN/1.73 M2":"mL/min/\{1.73_m2\}",
"U/L":"U/L",
"10*3/uL":"10*3/uL",
"GM/DL":"g/dL",
"PG":"pg",
"MMOL/L":"mmol/L",
"10*6/uL":"10*6/uL",
"NG/ML":"ng/mL",
"SEC":"s",
"MM HG":"mm[Hg]",
"IU/L":"[IU]/L",
"K/UL":"10*3/uL",
"cells/uL":"\{cells\}/uL",
"(calc)":"",
"x10E3/uL":"10*3/uL",
"M/UL":"10*6/uL",
"/HPF":"/[HPF]",
"MG%":"",
"Thousand/uL":"10*3/uL",
"mg/dL (calc)":"mg/dL",
"pg/mL":"pg/mL",
"mL/min/1.73m2":"mL/min/\{1.73_m2\}",
"Million/uL":"10*6/uL",
"g/dL (calc)":"g/dL",
"uIU/mL":"u[IU]/mL",
"Leu/uL":"",
"ng/dL":"ng/dL",
"mL/min/1.73":"mL/min/\{1.73_m2\}",
"\\% of total Hgb":"%\{Hb\}",
"x10E6/uL":"10*6/uL",
"mcg/dL":"ug/dL",
"mIU/L":"m[IU]/L",
"MG/L":"mg/L",
"UG/ML":"ug/mL",
"/LPF":"/[LPF]",
"ug/dL":"ug/dL",
"MM/HR":"mm/h",
"ratio":"\{ratio\}",
"IU/mL":"[IU]/mL",
"umol/L":"umol/L",
"mg/L FEU":"",
"AI":"",
"/100 WBCS":"/100\{WBCs\}",
"RH GROUP":"",
"BLOOD TYPE":"",
"kU/L":"kU/L",
"MIU/ML":"",
"mg/g creat":"mg/g\{creat\}",
"mcg/mg creat":"ug/mg\{creat\}",
"U/mL":"U/mL",
"mIU/mL":"m[IU]/mL",
"mcg/dL (calc)":"ug/dL",
"MOS/KG":"mosm/kg",
"MCG/MG CR":"ug/mg\{creat\}",
"s/co ratio":"s/\{control\}",
"mm/h":"mm/h",
"index":"",
"/uL":"/uL",
"mmol/mol creat":"mmol/mol\{creat\}",
"MOSM/KG":"mosm/kg",
"UG/ML FEU":"ug/mL",
"mcg/mL":"ug/mL",
"ratio units":"\{ratio\}",
"Score":"",
"QUAL":"",
"nmol/L":"nmol/L",
"UNITS":"",
"mcg/L":"ug/L",
"U":"U",
"MOSMO/KG":"",
"K/-¦L":"",
"HRS":"h",
"mL":"mL",
"Index":"\{index\}",
"HR":"h",
"AU/mL":"",
"copies/mL":"\{copies\}/mL",
"mcg/24 h":"ng/(24.h)",
"titer":"\{titer\}",
"mcg/g":"ug/g",
"/MM3":"/mL",
"SI":"",
"Units":"[IU]",
"ML/24 HRS":"mL/(24.h)",
"SMU":"",
"SGU":"",
"SAU":"",
"\\% baseline":"%\{baseline\}",
"TITRE":"\{titer\}",
"ML/MIN":"mL/min",
"% (calc)":"%",
"mg/24 h":"mg/(24.h)",
"g":"g",
"ng/mL/h":"ng/mL/h",
"g/24 h":"g/(24.h)",
"FEU ug/mL":"ug/mL",
"U/g Hgb":"U/g\{Hb\}",
"Log copies/mL":"\{Log_copies\}/mL",
"nmol/hr/mL RBC":"",
"%\{Activity\}":"%\{activity\}",
"ug/L":"ug/L",
"% Inhibition":"%\{inhibition\}",
"yr":"",
"GM/24H":"",
"% normal":"%\{normal\}",
"% ACTIVITY":"%\{activity\}",
"mcg/g creat":"ug/g\{creat\}",
"ng/mL RBC":"ng/mL\{RBCs\}",
"APL":"",
"mg/day":"mg/d",
"nmol/mL":"nmol/mL",
"Log IU/mL":"\{Log_IU\}/mL",
"mg/24 hr":"mg/(24.h)",
"EU/ml":"",
"calc":"",
"AU":"[AU]",
"GPL U/mL":"",
"MPL U/mL":"",
"U/g Hb":"U/g\{Hb\}",
"Log cps/mL":"\{Log_copies\}/mL",
"ug/g":"ug/g",
"mcg/g cr":"ug/g\{creat\}",
"pmol/L":"pmol/L",
"10^3/mL":"10*3/mL",
"GPI IgG units":"",
"10^6/-¦L":"",
"mcg/mL FEU":"",
"GPI IgM units":"",
"mEq/day":"",
"YEARS":"",
"/100 WBC":"/100\{WBCs\}",
"log10copy/mL":"\{Log_copies\}/mL",
"APL U/mL":"",
"mg/mg creat":"",
"APL-U/mL":"",
"MG/24H":"mg/(24.h)",
"GPI IgA units":"",
"L/day":"",
"mmol/day":"",
"ng/mL/hr":"",
"ISR":"",
"HOURS":"",
"uU/mL":"uU/mL",
"Unit":"",
"mmol/g creat":"",
"umol/g Cr":"",
"MPS":"",
"GPS":"",
"Net CPM":"",
"mg/dL Adult":"",
"ug Elast./g":"",
"ug/24 hr":"",
"MEQ/24HR":"",
"log10 IU/mL":"\{Log_IU\}/mL",
"ng/L":"ng/L",
"mOsmol/kg":"",
"rel to H2O":"",
"mm":"mm",
"\\% binding inhib":"",
"LU30":"",
"\\% inhibit":"",
"\\% activity":"",
"X 100":"",
"pmol/8x 10E8":"",
"nm":"nm",
"JDF units":"",
"mg":"mg",
"Mill/uL":"10*6/uL",
"MG/24HR":"",
"mmol/24 h":"",
"ug/g creat":"",
"pH units":"[pH]",
"RU/mL":"",
"ug/mg Creat":"",
"mg/g Cr":"",
"CU":"",
"h":"h",
"/100":"/100",
"BRBIO1":"",
"Index Value":"\{index_val\}",
"%mean normal":"",
"mmol/24 hr":"",
"FIAX TITRE":"",
"U / 2 HR":"",
"FIU":"",
"x10-3/uL":"",
"Million/mL":"",
"mL/24 h":"",
"MG/GM":"",
"ug FEU/mL":"",
"REFERENCE RANGE":"",
"nmol/h/mg Hb":"",
"ppb":"",
"\\% eos":"",
"\\% of inhibition":"",
"10":"",
"BTU":"",
"x10 3/uL":"",
"BU":"",
"th/uL":"10*3/uL",
"IV":"",
"mL/24 hr":"",
"not reported":"",
"MEQ/24H":"",
"MoM":"",
"g/L":"g/dL",
"mEq/24 hr":"",
"EU":"",
"nmol/min/mL":"nmol/min/mL",
"mmol/mol Cr":"",
"\\% binding inhibition":"",
"mcg Eq/mL":"",
"mOsm":"",
"GM/24HR":"",
"SECONDS":"s",
"mlU/mL":"m[IU]/mL",
"g/24 hr":"g/(24.h)",
"rel.saline":"",
"g/dl *calc*":"",
"nM BCE/mM Cr":"",
"mcg/24hr":"",
"% Release":"",
"nmol BCE":"",
"mg/g":"mg/g",
"log10IU/mL":"\{Log_IU\}/mL",
"\\% by wt":"",
"Bethesda":"",
"ug Eq/mL":"",
"nmol/hr/mg prt":"",
"x10^3/UL":"",
"x10-6/uL":"",
"umol/24 h":"",
"Units/mL":"",
"pg/dL":"pg/dL",
"U/g":"U/g",
"K/uL":"",
"EIA units":"",
"%Hb":"",
"UperL":"",
"BU/mL":"",
"mcg/g Cr":"",
"INDEX":"%\{index\}",
"\\% binding":"",
"10S6/uL":"",
"umol/mmol cr":"",
"min":"min",
"MM3":"",
"ML/MIN/1.7":"mL/min/\{1.73_m2\}",
"10S3/uL":"",
"mgperdL":"",
"x10 6/uL":"",
"log10 copy/mL":"",
"APS Units":"\{APS'U\}",
"10^6/mm3":"",
"mcmol/L":"",
"CBU/mL":"",
"mcg/min":"ug/min",
"mcg/g Hb":"",
"OD":"",
"U/g creat":"",
"BEU":"",
"%TOTAL HGB":"",
"cal":"cal",
"10^3/uL":"10*3/uL",
"clac":"",
"mcg/mg":"ug/mg",
"EU/dL":"",
"MM6":"",
"mcg/24H":"",
"%Saturation":"",
"mg/24hr":"mg/(24.h)",
"th/-¦L":"",
"mL/mn/1.73m2":"mL/min/\{1.73_m2\}",
"nM BCE/mM creat":"nmol\{BCE\}/mmol\{creat\}",
"G units":"",
"nmol/h/mg":"",
"mcg/mL Eq":"",
"LogIU/mL":"\{Log_IU\}/mL",
"mcg/g Creat":"",
"10^9/c":"",
"OD ratio":"",
"pmol/mL":"pmol/mL",
"32":"",
"particles/uL":"",
"IU":"",
"uM":"",
"g/dL(calc)":"g/dL",

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

lds_address_history_address_use_dict ={
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


obs_clin_result_qual_dict = {

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

obs_gen_result_qual_dict = {

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


obs_gen_result_modifier_dict = {

            "<=":"LE",
            ">=":"GE",
            "<":"LT",
            "=":"EQ",
            ">":"GT",
            "":"NI",

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
