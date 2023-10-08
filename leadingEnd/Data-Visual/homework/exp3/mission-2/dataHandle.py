import openpyxl
from datetime import datetime
from datetime import timedelta
# import xml.etree.ElementTree as ET 
import json
def dataHandle(sheet, useless_row, useless_col):
    '''
    删除工作表中无用的行和列
    sheet:工作表

    '''
    sheet.delete_cols(useless_col)
    sheet.delete_rows(useless_row)
    return sheet


def get_province(sheet, col):
    '''
    获得表中所有的省份名，并返回{省份：确诊人数}的字典
    col:省份所在列
    '''
    mySet = set()
    data_require = sheet[col]
    for cell in data_require:
        value = cell.value
        mySet.add(value)
    province_dict = {item: 0 for item in mySet}
    return province_dict


def get_confirmed_cases(sheet, province_dict, begin_date,end_date):
    '''
    获取某一天的确诊人数
    province_dict:{省份：确诊人数}字典，在此基础上生成结果字典
    begin_date:统计这一天的确诊人数
    end_date:工作表中的最大日期,begin_date不能超过end_date
    '''
    # print(len(data_dict))
    result_dict = province_dict.copy()
    # print(len(result_dict))
    rawdata = []
    flag = 0  # 获取到数据的省份数量
    # 获得截止到给定日期各省的累计确诊，如果该日数据丢失，则寻找之前最接近这一天的数据
    while 1:
        for row in sheet.iter_rows(values_only=True):
            if row[6] == begin_date:
                rawdata.append(row)

        for i in rawdata:
            if result_dict[i[0]] == 0:
                result_dict[i[0]] += i[2]
                flag = flag + 1
        if flag == len(result_dict): # 获取到所有省份的数据
            return result_dict
        elif begin_date == end_date:
            return result_dict
        elif begin_date < end_date:
            begin_date = begin_date + timedelta(days=1)


# 获取到每一天各省的确诊人数
def get_confirmed_cases_everyDay(sheet, begin_date_tuple, end_date_tuple):
    '''
    begin_date_tuple:初始日期
    end_date_tuple:结束日期
    
    '''
    # 时间数据转换
    date = datetime(*begin_date_tuple)
    end_date = datetime(*end_date_tuple)
    # 获得省份字典
    province_dict = get_province(sheet)
    # print(len(province_dict))
    # 结果字典
    data_dict_everyDay = {}


    while 1:
        # 获得某一天的确诊人数
        data_dict = get_confirmed_cases(sheet, province_dict, date, end_date)
        data_dict_everyDay[date] = data_dict

        # 时间迭代
        date = date + timedelta(days=1)
        if date > end_date:
            return data_dict_everyDay

if __name__ == "__main__":
    # 导入工作簿
    workbook = openpyxl.load_workbook('exp3/mission-2/CityData.xlsx')
    # 导入工作表
    sheet = workbook.worksheets[0]
    # print(workbook.active)
    # 数据处理
    # 去掉无关项
    row = 1
    col = 1
    sheet = dataHandle(sheet, row, col)
    try:
        result_dict = get_confirmed_cases_everyDay(
            sheet, (2020, 1, 24), (2020, 4, 18))
    except MemoryError as ME:
        print("内存耗尽", ME)

    print("data handled successfully")


    # 保存为JSON文件
    json_dict = {}
    for key, value  in result_dict.items():
        new_key = key.strftime('%Y-%m-%d') 
        json_dict[new_key] = value
    with open("exp3/mission-2/data_dict.json", 'w', encoding='utf-8') as file:
        json.dump(json_dict, file, ensure_ascii=False)

    # 保存为xml
    #  xml_dict = {}
    # for key, value  in result_dict.items():
    #     new_key = key.strftime('%Y-%m-%d') 
    #     xml_dict[new_key] = value
    # root = ET.Element('confirmed')  
    # for key, value in xml_dict.items():  
    #     element = ET.SubElement(root, key)  
    #     element.text = str(value)

    # tree = ET.ElementTree(root)  

    # tree.write('exp3/mission-2/confirmed.xml', encoding='utf-8', xml_declaration=True)
