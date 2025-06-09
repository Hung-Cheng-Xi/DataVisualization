# 台灣人口變遷與高齡化趨勢

## 專案描述
這個專案是一個基於 Dash 和 Plotly 的數據可視化應用，專注於展示台灣的人口變遷與高齡化趨勢。應用提供了三種主要的可視化圖表：台灣高齡人口地圖、人口金字塔，以及出生死亡線圖。

## 功能

### 1. 台灣高齡人口地圖
- 以地圖形式展示台灣各縣市的高齡人口比率
- 可選擇民國 103、108 和 113 年數據
- 提供連續色階和分級顏色兩種展示模式

### 2. 人口金字塔
- 以金字塔圖表展示台灣人口年齡與性別分布
- 可切換民國 103、108 和 113 年資料

### 3. 出生死亡線圖
- 以折線圖展示民國 103 年至 113 年間台灣的出生人數、死亡人數及自然增減趨勢

## 專案架構
```
app/
  ├── chart/           # 各種圖表生成函數
  │   ├── funnel.py    # 人口金字塔圖表
  │   ├── line.py      # 出生死亡線圖
  │   └── map.py       # 高齡人口地圖
  ├── mnt/             # 資料檔案目錄
  │   └── data/        # 原始資料檔案
  ├── pages/           # Dash 頁面組件
  │   ├── funnel.py    # 人口金字塔頁面
  │   ├── line.py      # 出生死亡線圖頁面
  │   └── map.py       # 高齡人口地圖頁面
  ├── schema/          # 資料模型定義
  │   ├── funnel_record.py
  │   ├── life_line_record.py
  │   ├── map_area_record.py
  │   └── region_age_record.py
  ├── services/        # 資料處理服務
  │   ├── calculate/   # 資料計算邏輯
  │   ├── parse/       # 資料解析邏輯
  │   ├── get_funnel_data.py
  │   ├── get_line_data.py
  │   └── get_map_data.py
  └── until/           # 共用工具函數
main.py                # 應用程式主入口
```

## 使用技術與套件
- **Dash**: 用於建立網頁應用介面
- **Plotly**: 用於生成互動式圖表
- **Pandas**: 用於數據處理與分析
- **GeoPandas**: 用於地理空間數據處理
- **Openpyxl**: 用於讀取 Excel 檔案
- **Pydantic**: 用於資料驗證與模型定義

## 環境設置與運行

### 使用 uv 設置虛擬環境
```bash
# 安裝 uv (如果尚未安裝)
pip install uv

# 創建虛擬環境
uv venv

# 啟動虛擬環境
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 安裝依賴
uv pip install -r uv.lock
# 或者
uv pip sync
```

### 運行應用
```bash
python main.py
```

應用將會在 http://0.0.0.0:8000 上運行，可通過瀏覽器訪問。

## 資料來源
專案使用了多個資料檔案，包括：
- 三年人數統計.xlsx: 包含人口金字塔分析所需的年齡性別數據
- 人口比率.xlsx: 包含高齡人口地圖所需的比率數據
- twCounty2010.geo.json: 台灣縣市地理資訊檔案

## 系統需求
- Python 3.12 或更高版本
