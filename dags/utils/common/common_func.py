def get_sftp():
    print("get_sftp!!!!!!!!!!")

def register(**kwargs):
    name=kwargs['name'] or ''
    sex=kwargs['sex'] or ''
    country=kwargs['country'] or ''
    city=kwargs['city'] or ''
    print(f'{name}, {sex}, {country}, {city} 입니다')
