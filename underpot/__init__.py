
import os 
import uuid 
import base64
import hashlib 
from io import BytesIO
from pathlib import Path 
from Cryptodome.Cipher import AES

def generate_stretched_hash (source: bytes, *, algorithm, stretching_count: int) -> bytes:
  digest = source
  for i in range(stretching_count):
    digest = algorithm(digest).digest()
  return digest

def get_envbase_hash (*, algorithm, stretching_count: int) -> bytes:
  digest1 = generate_stretched_hash(uuid.getnode().to_bytes(8, "little"), algorithm=algorithm, stretching_count=stretching_count)
  digest2 = generate_stretched_hash(os.getlogin().encode("utf-8"), algorithm=algorithm, stretching_count=stretching_count)
  return generate_stretched_hash(digest1 + digest2, algorithm=algorithm, stretching_count=stretching_count)

def generate_envbase_hash (source: bytes, *, algorithm, stretching_count: int) -> bytes:
  salt = get_envbase_hash(algorithm=algorithm, stretching_count=stretching_count)
  return generate_stretched_hash(salt + source, algorithm=algorithm, stretching_count=stretching_count)

def encrypt (data: bytes, *, algorithm=hashlib.sha256, stretching_count: int=256, encrypt_key=None) -> bytes:

  """
  encrypt plain text without require cipher key.
  this function make cipher key temporally from machine-identifier and username.
  """

  if encrypt_key is None:
    encrypt_key = get_envbase_hash(algorithm=algorithm, stretching_count=stretching_count)
  aes = AES.new(encrypt_key, AES.MODE_EAX)
  with BytesIO() as buffer:
    text, tag = aes.encrypt_and_digest(data)
    buffer.write(aes.nonce)
    buffer.write(tag)
    buffer.write(text)
    return buffer.getvalue()

def decrypt (data: bytes, *, algorithm=hashlib.sha256, stretching_count: int=256, encrypt_key=None) -> bytes:

  """
  decrypt cipher text that encrypted by `encrypt` function.
  this function make cipher key temporally from machine-identifier and username.
  """

  if encrypt_key is None:
    encrypt_key = get_envbase_hash(algorithm=algorithm, stretching_count=stretching_count)
  with BytesIO(data) as buffer:
    nonce = buffer.read(16)
    tag = buffer.read(16)
    text = buffer.read()
    aes = AES.new(encrypt_key, AES.MODE_EAX, nonce)
    return aes.decrypt_and_verify(text, tag)

def generate_hash_by_path (path: Path, *, algorithm, stretching_count: int) -> bytes:
  p = Path(path)
  return generate_envbase_hash(p.as_posix().encode("utf-8"), algorithm=algorithm, stretching_count=stretching_count)

def get_hashed_path (path: Path, *, algorithm=hashlib.sha256, stretching_count: int=256) -> bytes:

  """
  obfuscate a filename.
  I recommend this function, if you want to hide from anybody guess a file information from file-name.
  """

  p = Path(path)
  return p.with_name(base64.urlsafe_b64encode(generate_hash_by_path(p, algorithm=algorithm, stretching_count=stretching_count)).decode("ascii"))

def save (path: Path, data: bytes, *, algorithm=hashlib.sha256, stretching_count: int=256) -> None:

  """
  encrypt binary data without cipher key then save it into the file.
  this function make cipher key temporally from machine-identifier, username and path.
  """

  encrypt_key = generate_hash_by_path(path, algorithm=algorithm, stretching_count=stretching_count)
  with open(path, "wb") as stream:
    stream.write(encrypt(data, encrypt_key=encrypt_key))

def load (path: Path, *, algorithm=hashlib.sha256, stretching_count: int=256):

  """
  load encrypted file and decrypt it without cipher key.
  this function make cipher key temporally from machine-identifier, username and path.
  """

  encrypt_key = generate_hash_by_path(path, algorithm=algorithm, stretching_count=stretching_count)
  with open(path, "rb") as stream:
    return decrypt(stream.read(), encrypt_key=encrypt_key)
