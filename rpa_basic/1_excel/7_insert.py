from openpyxl import load_workbook
wb = load_workbook("sample1.xlsx")
ws = wb.active

# ws.insert_rows(8) # 8번째 줄 위치에 행추가
# ws.insert_rows(8,5) # 8번째 줄 위치에 5줄 추가

# ws.insert_cols(2) # B번째 줄 위치에 열추가
ws.insert_cols(2,3) # B번째 줄 위치에 3열추가

wb.save("sample_insert_rows.xlsx")