class Config:
    Username = None
    User_id = None
    Search = None
    Geo = None
    Location = False
    Near = None
    Lang = None
    Output = None
    Elasticsearch = None
    Timedelta = None
    Year = None
    Since = None
    Until = None
    Fruit = False
    Verified = False
    Store_csv = False
    Store_json = False
    Custom = False
    Show_hashtags = False
    Limit = None
    Count = None
    Stats = False
    hostname = None #mysql
    Database = None
    DB_user = None #mysql
    DB_pwd = None  #mysql
    To = None
    All = None
    Debug = False
    Format = None
    Essid = ""
    Profile = False
    Followers = False
    Following = False
    Favorites = False
    TwitterSearch = False
    User_full = False
    Profile_full = False
    Store_object = False
    Store_pandas = False
    Pandas_type = None
    Pandas = False
    Search_name = "-" #for identify a records in mysql with the search it provides from.  it cannot be null for DB requirements. a tweet must be in several search so the PK are tweet ID and search_name
    Index_tweets = "twint"
    Index_follow = "twintGraph"
    Index_users = "twintUser"