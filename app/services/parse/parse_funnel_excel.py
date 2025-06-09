import pandas as pd
import os


from app.schema import RegionAgeRecord


def _get_mnt_data_path(filename: str) -> str:
    """
    取得 mnt/data 資料夾下的檔案路徑
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, "..", "mnt", "data", filename)


def parse_funnel_excel(filename: str) -> dict[str, list[RegionAgeRecord]]:
    """
    讀取 Excel 中各年度資料，並依年度分組回傳
    """
    xls_path = _get_mnt_data_path(filename=filename)

    records_by_year: dict[str, list[RegionAgeRecord]] = {}
    xls = pd.ExcelFile(xls_path, engine="openpyxl")

    for sheet in xls.sheet_names:
        df = pd.read_excel(xls_path, sheet_name=sheet, header=None, engine="openpyxl")
        # 偵測 header row
        header_row = df.apply(
            lambda r: any("區域別" in str(c) for c in r)
            and any("性別" in str(c) for c in r)
            and any("總" in str(c) for c in r),
            axis=1,
        ).idxmax()
        # 讀取資料
        df = pd.read_excel(
            xls_path, sheet_name=sheet, header=header_row, engine="openpyxl"
        )
        df.columns = df.columns.astype(str).str.replace("\n", "").str.strip()
        df = df.rename(
            columns={
                df.columns[0]: "Area",
                df.columns[1]: "Sex",
                df.columns[2]: "Total",
            }
        )
        # 過濾
        df = df[df["Sex"].isin(["男", "女"])]
        df = df[df["Area"] != "總　　計"]
        df["Area"] = df["Area"].ffill()
        df = df[df["Area"].notna() & (df["Area"].str.strip() != "")]
        df["Year"] = sheet
        age_cols = [c for c in df.columns if c not in ["Area", "Sex", "Total", "Year"]]
        df["Total"] = pd.to_numeric(df["Total"], errors="coerce").fillna(0).astype(int)
        for c in age_cols:
            df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0).astype(int)

        # 建立模型清單
        recs: list[RegionAgeRecord] = []
        for _, row in df.iterrows():
            age_data = {c: row[c] for c in age_cols}
            rec = RegionAgeRecord(
                area=row["Area"],
                sex=row["Sex"],
                year=sheet,
                total=row["Total"],
                age_groups=age_data,
            )
            recs.append(rec)
        records_by_year[sheet] = recs

    return records_by_year


if __name__ == "__main__":
    # 執行並印出前3筆
    records_by_year = parse_funnel_excel()
    # 只印出第一個年度的前三筆資料
    for year, records in records_by_year.items():
        for rec in records[:3]:
            print(rec)
        break
