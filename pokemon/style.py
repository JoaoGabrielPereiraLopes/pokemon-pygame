class Style:
    def __init__(self, weak=str, strong=str) -> None:
        self.weak = weak
        self.strong = strong
    
    def GetWeak(self) -> str:
        return self.weak
    
    def GetStrong(self) -> str:
        return self.strong
