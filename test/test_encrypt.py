
from unittest import TestCase
import underpot 

class TestEncrypt (TestCase):
  
  def test_encrypt (self):
    plain = b"your secret!"    
    encrypted = underpot.encrypt(plain)
    decrypted = underpot.decrypt(encrypted)
    self.assertEqual(decrypted, plain)
