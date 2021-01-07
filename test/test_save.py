
import underpot 
from pathlib import Path
from unittest import TestCase
from tempfile import TemporaryDirectory

class TestSave (TestCase):
  
  def test_save (self):
    plain = b"my secret!"
    with TemporaryDirectory() as tempdir:
      path = Path(tempdir).joinpath("example")
      underpot.save(path, plain)
      loaded = underpot.load(path)
      self.assertEqual(loaded, plain)
  
  def test_save_empty (self):
    plain = b""
    with TemporaryDirectory() as tempdir:
      path = Path(tempdir).joinpath("example")
      underpot.save(path, plain)
      loaded = underpot.load(path)
      self.assertEqual(loaded, plain)
