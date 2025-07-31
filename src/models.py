from dataclasses import dataclass

@dataclass
class AgriProduct:
    TransDate: str
    TcType: str
    CropCode: str
    CropName: str
    MarketCode: str
    MarketName: str
    Upper_Price: float
    Middle_Price: float
    Lower_Price: float
    Avg_Price: float
    Trans_Quantity: float
