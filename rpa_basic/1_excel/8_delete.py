from openpyxl import load_workbook
wb = load_workbook("sample1.xlsx")
ws = wb.active

# ws.delete_rows(8) # 8번째 줄에있는 데이터삭제
# ws.delete_rows(8, 3) # 8번째 줄부터 3줄 데이터삭제

# wb.save("sample_delete_row.xlsx")

ws.delete_cols(2) # 2번째 열에있는 데이터 삭제
# wb.save("sample_delete_col.xlsx")
