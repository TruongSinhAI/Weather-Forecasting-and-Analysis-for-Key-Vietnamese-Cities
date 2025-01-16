from datetime import datetime

from down.down import DownloadData

dataDownload = DownloadData(
    location=["Hanoi", "DaNang", "HoChiMinh"],
    start_date="2000-01-01",
    end_date=datetime.today().__str__()
)
dataDownload.check_and_update_data()