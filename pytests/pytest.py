import pytest

def test_upper():
    assert 'foo'.upper() == 'FOO'

def test_isupper():
    assert 'FOO'.isupper() == True
    assert 'Foo'.isupper() == False

def test_split():
    s = 'hello world'
    print(s)
    assert s.split() == ['hello', 'world']
    with pytest.raises(TypeError):
        s.split(2)