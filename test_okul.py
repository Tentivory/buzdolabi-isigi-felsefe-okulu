import okul


def test_tez_sabit():
    a = okul.tez_uret("peynir arkada", 7)
    b = okul.tez_uret("peynir arkada", 7)
    assert a == b
    assert "TEZ #" in a


def test_kapi_kapali_grev():
    metin = okul.kapi_durumu(False)
    assert "GREV" in metin.upper() or "grev" in metin


def test_muhur_bos_degil():
    assert okul.muhur_coz(okul._ENVANTER)
