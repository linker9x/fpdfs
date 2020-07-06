import pandas as pd

global df_earnings, df_positions, df_departments, df_payroll


def clean_earnings_df():
    df_2012 = pd.read_csv('./raw/Earnings_History_2012_2016.csv')
    df_2017 = pd.read_csv('./raw/Earnings_History_2017.csv')
    df_2012.columns = map(str.lower, df_2012.columns)
    df_2017.columns = map(str.lower, df_2017.columns)

    df_full = pd.concat([df_2012, df_2017])
    df_full.drop(['checknumber', 'pay_period', 'activitydate', 'fid'], axis=1, inplace=True)

    df_full['name'] = df_full['lastname'] + ', ' + df_full['firstname']

    df_full.to_csv('./cleaned_data/earnings.csv', index=False)

    return df_full


def clean_positions_df():
    df = pd.read_csv('./raw/All_Positions_List_Public.csv')
    df.drop(['START_DATE', 'END_DATE', 'FROZEN', 'SUPERVISORY', 'FID'], axis=1, inplace=True)

    df.columns = map(str.lower, df.columns)
    df.to_csv('./cleaned_data/positions.csv', index=False)
    return df


def clean_departments_df():
    df = pd.read_csv('./raw/Payroll_HomeDepartments_Public.csv')
    df.drop(['INFO_TYPE', 'FID'], axis=1, inplace=True)
    df.columns = map(str.lower, df.columns)

    df.to_csv('./cleaned_data/departments.csv', index=False)
    return df


def clean_payroll_df():
    df = pd.read_csv('./raw/PayrollHourTypes_Public.csv')
    df.drop(['Hour_Action_Code', 'Base_Hours', 'Hour_Class', 'Affordable_Care_Subject', 'FID'], axis=1, inplace=True)

    df.columns = map(str.lower, df.columns)
    df.to_csv('./cleaned_data/payroll.csv', index=False)
    return df


if __name__ == "__main__":
    df_earnings = clean_earnings_df()
    df_positions = clean_positions_df()
    df_departments = clean_departments_df()
    df_payroll = clean_payroll_df()

    df_combined = result = pd.merge(df_earnings, df_payroll, on='hourtype')
    df_combined[df_combined['pay_multiplier'] == 1.5].to_csv('look.csv', index=False)
    print(df_combined['hourtype'])
    headers = {'amount': 'amount', 'hours': 'hours', 'rate': 'avg_rate'}
    df_earnings = df_earnings.groupby(['name', 'fiscal_year']).agg({'amount': 'sum', 'hours': 'sum', 'rate': 'mean'}).rename(columns=headers)
