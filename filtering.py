# Nama          : Ridho Fariha
# NIM           : 227056014
# Matakuliah    : Pemrograman untuk data science dan kecerdasan buatan


import pandas as pd


class Filtering:

    def selected_column(self, df):
        new_df = pd.DataFrame()
        new_df['name'] = df['Player']
        new_df['age'] = df['Age']
        new_df['nationality'] = df['Nation']
        new_df['born_year'] = df['Born']
        new_df['squad'] = df['Squad']

        return new_df

    def replace_zero_values(self, df):
        df['Nation'] = df['Nation'].replace(['0'], 'ESP')
        df['Age'] = df['Age'].replace([0], 20)
        df['Born'] = df['Born'].replace([0], 2002)

        return df

    def result(self, csv):
        df = pd.read_csv(csv, sep=";", encoding="latin-1")

        # pd.set_option('display.max_rows', None)
        # pd.set_option('display.max_columns', None)

        self.replace_zero_values(df)

        return self.selected_column(df)
