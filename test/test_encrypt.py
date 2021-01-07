
import underpot 
from unittest import TestCase

class TestEncrypt (TestCase):
  
  def test_encrypt (self):
    plain = b"your secret!"    
    encrypted = underpot.encrypt(plain)
    decrypted = underpot.decrypt(encrypted)
    self.assertEqual(decrypted, plain)
  
  def test_encrypt_empty (self):
    plain = b""
    encrypted = underpot.encrypt(plain)
    decrypted = underpot.decrypt(encrypted)
    self.assertEqual(decrypted, plain)
