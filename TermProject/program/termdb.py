class TUser:
    def __init__(self, T_id=None, T_word=None, T_name=None):
        self.T_id=T_id
        self.T_word=T_word
        self.T_name=T_name
    
    def __str__(self):
        return 'T_id: '+self.T_id+'T_word: '+self.T_word+'T_name: '+self.T_name
    
    
class Shard_DB:
    def __init__(self,  SD_ID=None, SD_user_ID=None, SD_Date=None, SD_Cost=None,SD_Memo=None,SD_Goal=None,SD_how=None):
        self.SD_ID=SD_ID
        self.SD_user_ID=SD_user_ID
        self.SD_Date=SD_Date
        self.SD_Cost=SD_Cost
        self.SD_Memo=SD_Memo
        self.SD_Goal=SD_Goal
        self.SD_how=SD_how
                
def __str__(self):
        return 'SD_ID: '+self.SD_ID+'SD_user_ID: '+self.SD_user_ID+'SD_Date: '+self.SD_Date+'SD_Cost: '+self.SD_Cost+'SD_Memo: '+self.SD_Memo+'SD_Goal: '+self.SD_Goal+'SD_how: '+self.SD_how
    
    
class Income:
    def __init__(self, Inc_ID=None, Inc_Date=None, Inc_Cost=None, Inc_Clog=None, Inc_Memo=None, T_id=None):
        self.Inc_ID=Inc_ID
        self.Inc_Date=Inc_Date
        self.Inc_Cost=Inc_Cost
        self.Inc_Clog=Inc_Clog
        self.Inc_Memo=Inc_Memo
        self.T_id=T_id
    
    def __str__(self):
        return 'Inc_ID: '+self.Inc_ID+'Inc_Date: '+self.Inc_Date+'Inc_Cost: '+self.Inc_Cost+'Inc_Clog: '+self.Inc_Clog+'Inc_Memo: '+self.Inc_Memo+'T_id: '+self.T_id
    
class Outcome:
    def __init__(self, Out_ID=None, Out_Date=None, Out_Cost=None, Out_People=None, Out_Memo=None, T_id=None):
        self.Out_ID=Out_ID
        self.Out_Date=Out_Date
        self.Out_Cost=Out_Cost
        self.Out_People=Out_People
        self.Out_Memo=Out_Memo
        self.T_id=T_id
    
    def __str__(self):
        return 'Out_ID: '+self.Out_ID+'Out_Date: '+self.Out_Date+'Out_Cost: '+self.Out_Cost+'Out_People: '+self.Out_People+'Out_Memo: '+self.Out_Memo+'T_id: '+self.T_id
    
class Memo:
    def __init__(self, memo_ID=None, Minc_ID=None, Mout_ID=None, me_date=None, me_Memo=None, T_id=None):
        self.memo_ID=memo_ID
        self.Minc_ID=Minc_ID
        self.Mout_ID=Mout_ID
        self.me_date=me_date
        self.me_Memo=me_Memo
        self.T_id=T_id
    
    def __str__(self):
        return 'memo_ID: '+self.memo_ID+'Minc_ID: '+self.Minc_ID+'Mout_ID: '+self.Mout_ID+'me_date: '+self.me_date+'me_Memo: '+self.me_Memo+'T_id: '+self.T_id
    

