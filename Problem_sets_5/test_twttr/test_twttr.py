from twttr import shorten

def test_shorten():
    assert shorten("word") == "wrd"
    assert shorten("Twitter") == "Twttr"
    assert shorten("AEIOUaeiou") == ""
    assert shorten("123!") == "123!"
    assert shorten("Hello, World!") == "Hll, Wrld!"