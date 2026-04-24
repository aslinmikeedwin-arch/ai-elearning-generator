import openpyxl

def fix_storyboard(input_file, output_file):
    wb = openpyxl.load_workbook(input_file)
    ws = wb.active

    for row in ws.iter_rows(min_row=1):
        title_cell = row[0]
        if title_cell.value and title_cell.value not in ['title', None]:
            audio_cell = row[1]
            ost_cell   = row[2]
            title = str(title_cell.value).strip().lower()
            is_cyu = "check your understanding" in title

            if is_cyu:
                ost_cell.value   = audio_cell.value
                audio_cell.value = "-"
            else:
                old_audio        = audio_cell.value
                old_ost          = ost_cell.value
                audio_cell.value = old_ost
                ost_cell.value   = old_audio

    wb.save(output_file)
    print(f"✅ Saved: {output_file}")

if __name__ == "__main__":
    fix_storyboard("storyboard_script.xlsx", "storyboard_script_final.xlsx")
