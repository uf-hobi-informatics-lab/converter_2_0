import pandas as pd



pconrnet_cdm_location = "/app/common/cdm/"
pcornet_cdm_file_name = "pcornet_cdm_v61.csv"


pcornet_cdm_file_path = pconrnet_cdm_location + pcornet_cdm_file_name
pcornet_cdm_data = pd.read_csv(pcornet_cdm_file_path)


class PcornetCDM:


    

       


###################################################################################################################################
# This function will return the list of fields from the PCORnet CDM based on the passed table name
###################################################################################################################################

   
   

    @classmethod
    def get_cdm_table_fields_list(cls, table_name):


            filter_column = "TABLE_NAME"  # Replace with the actual filter column name
            filter_value = table_name   # Replace with the desired filter value
            filtered_rows = pcornet_cdm_data[pcornet_cdm_data[filter_column] == filter_value.upper()]
            print(filtered_rows)
            field_name = 'FIELD_NAME'


            table_fields_list = filtered_rows[field_name].tolist()
            print(table_fields_list)
            return table_fields_list












