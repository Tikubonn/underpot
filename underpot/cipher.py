
from .utility import generate_envbase_hash 
from Cryptodome.Cipher import AES
from io import BytesIO
import uuid 

def default_encrypt_key ():
  return generate_envbase_hash(
    uuid.getnode().to_bytes(8, "little"))

def encrypt (data: bytes, *, encryptkey: bytes = default_encrypt_key()) -> bytes:

  """
  encrypt the binary object.
  this routine get auto generated key that made of hardware information.
  it is more secure than hard coding.
  """

  aes = AES.new(encryptkey, AES.MODE_EAX)
  with BytesIO() as buffer:
    text, tag = aes.encrypt_and_digest(data)
    buffer.write(aes.nonce)
    buffer.write(tag)
    buffer.write(text)
    return buffer.getvalue()

def decrypt (data: bytes, *, encryptkey: bytes = default_encrypt_key()) -> bytes:

  """
  decrypt the binary object.
  this routine get auto generated key that made of hardware information.
  it is more secure than hard coding.
  """

  with BytesIO(data) as buffer:
    nonce = buffer.read(16)
    tag = buffer.read(16)
    text = buffer.read()
    aes = AES.new(encryptkey, AES.MODE_EAX, nonce)
    return aes.decrypt_and_verify(text, tag)
