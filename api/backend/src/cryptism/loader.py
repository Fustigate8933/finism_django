from toml import load

ROOT_PATH = 'C:\\Users\\ianch\\Desktop\\Programming\\python\\django\\finism\\api\\backend\\src\\cryptism'

def toml(local_path: str) -> dict:
    filepath = '/'.join((
        ROOT_PATH,
        local_path
    ))
    return load(filepath)
