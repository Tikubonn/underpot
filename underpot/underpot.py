
from .cipher import encrypt, decrypt
from .utility import generate_envbase_hash, generate_envbase_hash_string 
from pathlib import Path

def hashed_path (filename: Path) -> Path:
  path = Path(filename)
  return path.with_name(
    generate_envbase_hash_string(
      path.name.encode("utf-8")
    ))

def generate_hash_by_path (path: Path) -> bytes:
  return generate_envbase_hash(
    path.absolute().as_posix().encode("utf-8"))

def save (filename: Path, data: bytes):
  path = hashed_path(filename)
  encryptkey = generate_hash_by_path(filename)
  with open(path, "wb") as file:
    file.write(
      encrypt(
        data,
        encryptkey = encryptkey
      ))

def load (filename: Path) -> bytes:
  path = hashed_path(filename)
  encryptkey = generate_hash_by_path(filename)
  with open(path, "rb") as file:
    return decrypt(
      file.read(),
      encryptkey = encryptkey
    )
