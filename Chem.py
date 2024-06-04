CHEM_LINE = {
    'FEP-171 3mPa*s': ['PCAR', 'PCARB'],
    'FEP-171 6mPa*s': ['8K'],
    'MES EP500JE 1.9X': ['P53', 'P53B', 'P53C'],
    'SEBP-9012': ['P37', 'P37B'],
    'OEBR-CAP130T4': ['P23'],
    'MES EP561JE-1.9cp': ['P81'],
    'SEBP-602F': ['P94', 'P94B'],
    'E2 STACK AL9412-302': ['BARC'],
    'SEBN-306F': ['N19', 'N19B'],

    'EMX-7306': ['ACT12', 'ACT13', 'C21', 'C21B'],
    'EMX-7310': ['ACT11', 'ACT14', 'C14', 'C14B'],

    'PL9200A-319': ['SG1', 'SG1B'],
    'HM9825U-302.6': ['SARC', 'SARCB'],
    'MES EP900JB-1V2cP': ['P87', 'P87B'],
    'SEBN-1702': ['N23', 'N23B'],
}

CHEM_LINE = {v: k for k, li in CHEM_LINE.items() for v in li}

line = input("Which line are you changing: ")
line = line.upper()

if line in CHEM_LINE:
    line_index = (list(CHEM_LINE).index(line))
    CHEM_NAME = list(CHEM_LINE.values())[line_index]


class CHEM_Change:

    def __init__(self):
        self.TOOL = input('Which tool are you changing: ').upper()
        self.num_of_lines = int(input('How many lines are you changing?: '))
        self.EXP_DATE = input('Input the expiration date: ')
        self.WIINGS_num = input('Copy and paste the WIINGS order #: ')
        self.BUDDY_name = input('Input your buddy name: ').upper()
        self.BATCH = input('Input the batch number: ').upper()
        self.LEVEL_TYPE = input('What was the level of the bottle you changed?: ').upper()

    def prompt_script(self):

        if self.TOOL == 'ACT01' or self.TOOL == 'CCT01' or self.TOOL == 'CCT02':

            BOTTLE_FROM_WARMING_SHELF = input("Time bottle was placed on warming shelf: ")

            print(
                f"{line} REPLACED {self.LEVEL_TYPE} BOTTLE WITH BOTTLE FROM WARMING SHELF \n"
                f"\n"
                f"BOTTLE FROM WARMING SHELF: {BOTTLE_FROM_WARMING_SHELF} \n"
                f"\n"
                f"{CHEM_NAME} \n"
                f"BATCH: {self.BATCH} \n"
                f"EXP DATE: {self.EXP_DATE} \n"
                f"WIINGS: {self.WIINGS_num} \n"
                f"BUDDY: {self.BUDDY_name} \n"
                f"\n"
                f"KT"
            )

        elif self.TOOL == 'RCT03' or self.TOOL == 'RCT05' or self.TOOL == 'GCT01' or self.TOOL == 'GCT02':
            print(
                f"{self.TOOL}-{line} REPLACED {self.LEVEL_TYPE} BOTTLE WITH BOTTLE FROM FRIDGE \n"
                f"\n"
                f"{CHEM_NAME} \n"
                f"BATCH: {self.BATCH} \n"
                f"EXP DATE: {self.EXP_DATE} \n"
                f"WIINGS: {self.WIINGS_num} \n"
                f"BUDDY: {self.BUDDY_name} \n"
                f"\n"
                f"KT"
            )


def main():
    tester = CHEM_Change()
    tester.prompt_script()


if __name__ == '__main__':
    main()
