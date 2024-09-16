import os
import shutil
import logging
import sys

# ANSI escape sequences for color output
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
RESET = '\033[0m'

# Logging configuration for better output formatting
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)

def create_partner_directory(partner_path):
    logging.info(f"{CYAN}Step 1: Creating partner directories...{RESET}")
    
    if not os.path.exists(partner_path):
        os.makedirs(partner_path)
        os.makedirs(os.path.join(partner_path, 'formatting_scripts'))
        os.makedirs(os.path.join(partner_path, 'data'))
        os.makedirs(os.path.join(partner_path, 'custom_fixes'))
        os.makedirs(os.path.join(partner_path, 'fixer_scripts'))
        logging.info(f"{GREEN}Partner directory structure created successfully at: {partner_path}{RESET}\n")
    else:
        logging.warning(f"{YELLOW}The path already exists! Skipping directory creation.{RESET}\n")

def pull_from_template(cdm_format, dictionary_selection, partner_path):
    logging.info(f"{CYAN}Step 2: Pulling template files for the selected CDM format...{RESET}")

    if cdm_format == '1':
        source = os.path.join(os.getcwd(), 'partners', 'pcornet_partner_1')
        logging.info(f"{BLUE}Selected CDM format: PCORnet{RESET}")
    elif cdm_format == '2':
        source = os.path.join(os.getcwd(), 'partners', 'omop_partner_1')
        logging.info(f"{BLUE}Selected CDM format: OMOP{RESET}")

    logging.info(f"{CYAN}Copying fixer scripts...{RESET}")
    files = os.listdir(os.path.join(source, 'fixer_scripts'))
    for file in files:
        file_path = os.path.join(source, 'fixer_scripts', file)
        if os.path.isfile(file_path):
            shutil.copy(file_path, os.path.join(partner_path, 'fixer_scripts'))
    logging.info(f"{GREEN}Fixer scripts copied successfully.{RESET}\n")

    logging.info(f"{CYAN}Copying formatting scripts...{RESET}")
    files = os.listdir(os.path.join(source, 'formatting_scripts'))
    for file in files:
        file_path = os.path.join(source, 'formatting_scripts', file)
        if os.path.isfile(file_path):
            shutil.copy(file_path, os.path.join(partner_path, 'formatting_scripts'))
    logging.info(f"{GREEN}Formatting scripts copied successfully.{RESET}\n")

    if dictionary_selection == '1':
        shutil.copy(os.path.join(source, 'dictionaries.py'), partner_path)
        logging.info(f"{GREEN}Existing dictionary copied successfully.{RESET}\n")
    elif dictionary_selection == '2':
        shutil.copy(os.path.join(os.getcwd(), 'new_partner_setup', 'dictionaries.py'), partner_path)
        logging.info(f"{GREEN}New dictionary setup initiated.{RESET}\n")

def update_formatter_fixer_files(partner, partner_path):
    logging.info(f"{CYAN}Step 3: Updating formatting and fixer scripts with the partner name...{RESET}")

    files = os.listdir(os.path.join(partner_path, 'formatting_scripts'))
    for file_name in files:
        file_path = os.path.join(partner_path, 'formatting_scripts', file_name)
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        with open(file_path, 'w') as file:
            for line in lines:
                if line.strip() == "partner_name = 'omop_partner_1'":
                    file.write(f"partner_name = '{partner}'\n")
                elif line.strip() == "partner_name = 'pcornet_partner_1'":
                    file.write(f"partner_name = '{partner}'\n")
                else:
                    file.write(line)

    files = os.listdir(os.path.join(partner_path, 'fixer_scripts'))
    for file_name in files:
        file_path = os.path.join(partner_path, 'fixer_scripts', file_name)
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        with open(file_path, 'w') as file:
            for line in lines:
                if line.strip() == "partner_name = 'omop_partner_1'":
                    file.write(f"partner_name = '{partner}'\n")
                elif line.strip() == "partner_name = 'pcornet_partner_1'":
                    file.write(f"partner_name = '{partner}'\n")
                else:
                    file.write(line)

    logging.info(f"{GREEN}Partner name '{partner}' updated successfully in scripts.{RESET}\n")

def update_settings(partner):
    logging.info(f"{CYAN}Step 4: Updating settings.py with the new partner...{RESET}")
    
    settings_file = os.path.join(os.getcwd(), 'common', 'settings.py')

    with open(settings_file, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.strip().startswith('partners_list = ['):
            for j in range(i + 1, len(lines)):
                if ']' in lines[j]:
                    lines.insert(j, f'                 "{partner}",\n')
                    break
            break

    with open(settings_file, 'w') as file:
        file.writelines(lines)

    logging.info(f"{GREEN}Partner '{partner}' added to settings.py successfully.{RESET}\n")

def update_commonFunctions(partner):
    logging.info(f"{CYAN}Step 5: Updating commonFunctions.py with the new partner encryption value...{RESET}")

    common_functions_file = os.path.join(os.getcwd(), 'common', 'commonFunctions.py')

    with open(common_functions_file, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.strip().startswith('partner_encryption_value_dict = {'):
            for j in range(i + 1, len(lines)):
                if '}' in lines[j]:
                    lines.insert(j, f"                        '{partner}' : '{partner}',\n")
                    break
            break

    with open(common_functions_file, 'w') as file:
        file.writelines(lines)

    logging.info(f"{GREEN}Partner '{partner}' encryption value added to commonFunctions.py successfully.{RESET}\n")

def main():
    ascii_text = f"""{MAGENTA}
    **************************************
    *           Welcome to Ovid          *
    **************************************
    {RESET}
    """
    print(ascii_text)

    partner = input('What is the name of your partner? ').lower()
    cdm_format = input(f"""{CYAN}Which CDM is your source data in?\n
        1. PCORnet
        2. OMOP\n{RESET}""")
    
    while cdm_format not in ['1', '2']:
        logging.warning(f"{RED}\nInvalid input! Please select 1 or 2{RESET}")
        cdm_format = input(f"""{CYAN}Which CDM is your source data in?\n
        1. PCORnet
        2. OMOP\n{RESET}""")

    dictionary_selection = input(f"""{CYAN}How would you like to create your dictionary?\n
        1. Copy from existing dictionary
        2. Create new dictionary\n{RESET}""")

    while dictionary_selection not in ['1', '2']:
        logging.warning(f"{RED}\nInvalid input! Please select 1 or 2{RESET}")
        dictionary_selection = input(f"""{CYAN}How would you like to create your dictionary?\n
        1. Copy from existing dictionary (Recommended)
        2. Create new dictionary\n{RESET}""")
    
    print('\n')

    partner = partner.lower()
    partner_path = os.path.join(os.getcwd(), 'partners', partner)

    create_partner_directory(partner_path)
    pull_from_template(cdm_format, dictionary_selection, partner_path)
    update_formatter_fixer_files(partner, partner_path)
    update_settings(partner)
    update_commonFunctions(partner)

    logging.info(f"{GREEN}\nAll steps completed successfully!{RESET}")

if __name__ == '__main__':
    main()
