# patch_h5py.py
import h5py
orig_getitem = h5py._hl.attrs.AttributeManager.__getitem__
def patched_getitem(self, key):
    out = orig_getitem(self, key)
    if isinstance(out, bytes):
        return out.decode('utf8')
    return out
h5py._hl.attrs.AttributeManager.__getitem__ = patched_getitem
print(">>> h5py monkey patch for __getitem__ applied!")