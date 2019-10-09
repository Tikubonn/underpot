
from .cipher import encrypt, decrypt
from .utility import generate_envbase_hash, generate_envbase_hash_string 
from pathlib import Path

def generate_hash_by_path (path: Path) -> bytes:
  return generate_envbase_hash(
    path.absolute().as_posix().encode("utf-8"))

def get_hashed_path (path: Path) -> Path:
  pa = Path(path)
  return pa.with_name(
    generate_envbase_hash_string(
      pa.name.encode("utf-8")
    ))

def save (path: Path, data: bytes, *, use_hashed_path: bool=False):
  if use_hashed_path:
    path = get_hashed_path(path)
  encryptkey = generate_hash_by_path(path)
  with open(path, "wb") as file:
    file.write(
      encrypt(
        data,
        encryptkey = encryptkey
      ))

def load (path: Path, *, use_hashed_path: bool=False) -> bytes:
  if use_hashed_path:
    path = get_hashed_path(path)
  encryptkey = generate_hash_by_path(path)
  with open(path, "rb") as file:
    return decrypt(
      file.read(),
      encryptkey = encryptkey
    )
