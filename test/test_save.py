
from unittest import TestCase
from tempfile import TemporaryDirectory
from pathlib import Path
import underpot 

class TestSave (TestCase):
  
  def test_save (self):
    with TemporaryDirectory() as tempdir:
      path = Path(tempdir).joinpath("my-secret")
      plain = b"my secret!"
      underpot.save(path, plain)
      loaded = underpot.load(path)
      self.assertEqual(loaded, plain)
