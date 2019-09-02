
import uuid 
import platform
import hashlib
import base64
import os 

def generate_stretched_hash (source: bytes, *, algorithm = hashlib.sha256, itercount: int = 8):
  digest = source
  for n in range(itercount):
    digest = algorithm(digest).digest()
  return digest

def generate_envbase_pepper (algorithm = hashlib.sha256, itercount: int = 8):
  # avoid confliction by machine
  digest1 = generate_stretched_hash(
    uuid.getnode().to_bytes(8, "little"),
    algorithm = algorithm,
    itercount = itercount
  )
  # avoid confliction by user
  digest2 = generate_stretched_hash(
    os.getlogin().encode("utf-8"),
    algorithm = algorithm,
    itercount = itercount
  )
  return digest1 + digest2

def generate_envbase_hash (source: bytes, *, algorithm = hashlib.sha256, itercount: int = 8):
  digest = b""
  digest += generate_envbase_pepper(
    algorithm = algorithm,
    itercount = itercount
  )
  digest += source
  for n in range(itercount):
    digest = algorithm(digest).digest()
  return digest

def generate_envbase_hash_string (source: bytes, *, algorithm = hashlib.sha256, itercount: int = 8):
  return base64.urlsafe_b64encode(
    generate_envbase_hash(
      source,
      algorithm = algorithm,
      itercount = itercount
    )).decode("ascii")
