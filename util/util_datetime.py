from datetime import datetime
def convert_datetime_str(dt:datetime)->str:
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def convert_str_datetime(format:str)->datetime:
    return datetime.strptime(format, "%d-%m-%Y")