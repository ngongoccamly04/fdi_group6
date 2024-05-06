# -*- coding: utf-8 -*-
"""fdi_group6"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# FILE 1: FDI THEO CÁC NƯỚC
# 1. Đọc và làm sạch dữ liệu
df1 = pd.read_csv("./mfdi_country_partners_en.csv")
df1.fillna(0, inplace=True) # Thay thế NaN bằng 0
df1.replace('-', np.nan, inplace=True)  # Chuyển đổi '-' thành NaN
df1.replace(',', '', regex=True, inplace=True)
df1.replace('\\s+', '', regex=True, inplace=True)  # Xóa các khoảng trắng

# Chuyển đổi các cột thành dạng số
df1['Number of new projects']=pd.to_numeric(df1['Number of new projects'], errors='coerce')
df1['Adjusted project number']=pd.to_numeric(df1['Adjusted project number'], errors='coerce')
df1['Newly registered capital (million USD)']=pd.to_numeric(df1['Newly registered capital (million USD)'], errors='coerce')
df1['Adjusted capital (million USD)']=pd.to_numeric(df1['Adjusted capital (million USD)'], errors='coerce')

# 2. Phân tích mô tả
# Tổng số dự án mới và điều chỉnh theo từng năm
total_projects = df1.groupby('Year')[['Number of new projects', 'Adjusted project number']].sum().reset_index()
# Tổng vốn đầu tư theo từng năm
total_capital = df1.groupby('Year')[['Newly registered capital (million USD)', 'Adjusted capital (million USD)']].sum().reset_index()
# Tính tổng vốn đầu tư
df1['Total Capital (Million USD)'] = df1['Newly registered capital (million USD)'] + df1['Adjusted capital (million USD)']
# Nhóm dữ liệu theo quốc gia và tính tổng vốn đầu tư
total_capital_by_country = df1.groupby('Country')['Total Capital (Million USD)'].sum().reset_index()
# Lấy top 10 quốc gia đầu tư lớn nhất
top_10_country = total_capital_by_country.nlargest(10, 'Total Capital (Million USD)')
# Sắp xếp dữ liệu từ lớn nhất đến nhỏ nhất
top_10_country = top_10_country.sort_values(by='Total Capital (Million USD)', ascending=True)

# 3. Trực quan hóa dữ liệu

def project_year():
    # Biểu đồ tổng các dự án từ 2015-2022
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(10, 6))
    bar_width = 0.4
    positions = np.arange(len(total_projects))
    plt.bar(positions - bar_width/2, total_projects['Number of new projects'], width=bar_width, color='blue', label='New Projects')
    plt.bar(positions + bar_width/2, total_projects['Adjusted project number'], width=bar_width, color='green', label='Adjusted Projects')
    plt.xlabel('Year')
    plt.ylabel('Total Number of Projects')
    plt.title('Total Number of New and Adjusted Projects by Year')
    plt.xticks(positions, total_projects['Year'])
    plt.legend()
    plt.savefig('chart1.png')
    plt.show()

def capital_year():
    # Biểu đồ tổng vốn cho các dự án từ 2015-2022
    plt.figure(figsize=(15, 6))
    bar_width = 0.35
    positions = np.arange(len(total_projects))
    plt.bar(positions - bar_width/2, total_capital['Newly registered capital (million USD)'], width=bar_width, color='red', label='New Capital')
    plt.bar(positions + bar_width/2, total_capital['Adjusted capital (million USD)'], width=bar_width, color='blue', label='Adjusted Capital')
    plt.xlabel('Year')
    plt.ylabel('Total Capital (Million USD)')
    plt.title('Total Newly Registered and Adjusted Capital by Year')
    plt.xticks(positions, total_capital['Year'])
    plt.legend()
    plt.savefig('chart2.png')
    plt.show()

def Top_10():
    # Biểu đồ cho top 10 quốc gia có fdi cao ở VN 2015-2022
    plt.figure(figsize=(15, 10))
    plt.barh(top_10_country['Country'], top_10_country['Total Capital (Million USD)'], color='b')
    plt.xlabel('Total Capital (Million USD)')
    plt.ylabel('Country')
    plt.title('Top 10 Countries Investing in Vietnam from 2015 to 2022')
    plt.savefig('chart3.png')
    plt.show()


###################################################################

# FILE 2: FDI THEO CÁC NGÀNH
#đọc dữ liệu
csv_path=("./mfdi_industry_en.csv")
df2=pd.read_csv(csv_path)
#làm sạch dữ liệu
df2.fillna(0,inplace=True)
df2.replace('-',np.nan,inplace= True)
df2.replace(',', '', regex=True, inplace=True)
def project_industry():
    #SỐ DỰ ÁN MỚI VÀ DỰ ÁN ĐIỀU CHỈNH
    #chuyển dữ liệu sang dạng số
    df2['Number of new projects']=pd.to_numeric(df2['Number of new projects'], errors='coerce')
    df2['Adjusted project number']=pd.to_numeric(df2['Adjusted project number'], errors='coerce')
    #tổng các dự án mới và thay đổi tính theo theo ngành
    Total_newP = df2.groupby('Industry')['Number of new projects'].sum()
    Total_adjP = df2.groupby('Industry')['Adjusted project number'].sum()
    #vẽ đồ thị
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(10,7))
    bar_width=0.35
    positions = np.arange(len(Total_newP))
    plt.yticks(positions, Total_newP.index)
    plt.barh(positions+bar_width/2, Total_newP.values,bar_width, label='Number of New Projects',color='blue')
    plt.barh(positions-bar_width/2, Total_adjP.values,bar_width, label='Adjusted project number',color='green')
    plt.xlabel('Total Number of Projects')
    plt.ylabel('Industry')
    plt.title('Total Number of New and Adjusted Projects by Industry from 2015 to 2022')
    plt.legend()
    plt.tight_layout()
    plt.savefig('chart4.png')
    plt.show()

def capital_industry():
    #SỐ VỐN CHO DỰ ÁN MỚI VÀ DỰ ÁN ĐIỀU CHỈNH
    #chuyển dữ liệu sang dạng số
    df2['Newly registered capital (million USD)']=pd.to_numeric(df2['Newly registered capital (million USD)'], errors='coerce')
    df2['Adjusted capital (million USD)']=pd.to_numeric(df2['Adjusted capital (million USD)'], errors='coerce')
    #tổng vốn cho các dự án mới và thay đổi tính theo theo ngành
    Total_newC = df2.groupby('Industry')['Newly registered capital (million USD)'].sum()
    Total_adjC = df2.groupby('Industry')['Adjusted capital (million USD)'].sum()

    #vẽ đồ thị
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(10,7))
    bar_width=0.4
    positions = np.arange(len(Total_newC))
    plt.yticks(positions, Total_newC.index)
    plt.barh(positions+bar_width/2, Total_newC.values,bar_width, label='Number of New Projects',color='red')
    plt.barh(positions-bar_width/2, Total_adjC.values,bar_width, label='Adjusted project number',color='blue')
    plt.xlabel('Total Number capital')
    plt.ylabel('Industry')
    plt.title('Total Number of Newly registered and Adjusted Capital by Industry from 2015 to 2022')
    plt.legend()
    plt.tight_layout()
    plt.savefig('chart5.png')
    plt.show()

def main():
    while True:
        print("Choose a number to display the chart:")
        print("1. Total Number of New and Adjusted Projects by Year")
        print("2.Total Newly Registered and Adjusted Capital by Year")
        print("3. Top 10 Countries Investing in Vietnam from 2015 to 2022")
        print("4. Total Number of New and Adjusted Projects by Industry from 2015 to 2022")
        print("5. Total Number of Newly registered and Adjusted Capital by Industry from 2015 to 2022")
        print("0. Exit")


        choice = int(input("Enter your number: "))

        if choice == 0:
            print("Exiting.")
            break
        elif choice == 1:
            project_year()
        elif choice == 2:
           capital_year()
        elif choice == 3:
            Top_10()
        elif choice == 4:
            project_industry()
        elif choice == 5:
            capital_industry()
        else:
            print("Invalid choise! Choose again.")

main()