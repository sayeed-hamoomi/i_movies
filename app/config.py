from pydantic_settings import BaseSettings,SettingsConfigDict

class Setting(BaseSettings):

    
    database_name:str
    database_user:str
    database_password:str
    database_host:str
    database_port:str
    secret_key:str
    algorithm:str
    access_expire_minutes:int


    model_config = SettingsConfigDict(validate_default=False,env_file=".env")

settings=Setting()


