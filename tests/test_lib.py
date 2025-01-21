from wordz.libwordz import compte_mots


def test_compte_mots():
    counts = compte_mots(["Fluoxyniobate de potassium, et oxyde de cérium"])
    assert counts["Fluoxyniobate"] == 1
    assert counts["de"] == 2
    assert counts["uranium"] == 0
    assert counts[","] == 0
    assert counts["potassium,"] == 0
