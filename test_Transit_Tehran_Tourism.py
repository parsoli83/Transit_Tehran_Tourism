from Transit_Tehran_Tourism import *


def test_trip_metro():
    assert trip_metro([["Tehran Grand Bazaar", "Khayyam", 1]]) == [
        ["Tehran Grand Bazaar", "Khayyam", 2]
    ]
    assert trip_metro(
        [["Tehran Grand Bazaar", "Khayyam", 1], ["Azadi Tower", "Meydan-e Azadi", 4]]
    ) == [
        ["Tehran Grand Bazaar", "Khayyam", "Darvazeh Dolat"],
        ["Azadi Tower", "Meydan-e Azadi", 2],
    ]
    assert trip_metro(
        [
            ["Tehran Grand Bazaar", "Khayyam", 1],
            ["Azadi Tower", "Meydan-e Azadi", 4],
            ["Milad Tower", "Milad Tower", 7],
        ]
    ) == [
        ["Tehran Grand Bazaar", "Khayyam", "Darvazeh Dolat"],
        ["Azadi Tower", "Meydan-e Azadi", "Towhid"],
        ["Milad Tower", "Milad Tower", 2],
    ]


def test_metro():
    assert metro(["Khayyam", 1], ["Meydan-e Azadi", 4]) == "Darvazeh Dolat"
    assert metro(["Meydan-e Azadi", 4], ["Milad Tower", 7]) == "Towhid"
    assert metro(["Milad Tower", 7], ["Panzdah-e Khordad", 1]) == "Mohammadieh"


def test_catalog_ascii():
    assert (
        catalog_ascii(
            [
                ["Tehran Grand Bazaar", "Khayyam", "Darvazeh Dolat"],
                ["Azadi Tower", "Meydan-e Azadi", "Towhid"],
                ["Milad Tower", "Milad Tower", "Mohammadieh"],
                ["Moslem Restaurant", "Panzdah-e Khordad", 0],
                ["Golestan Palace", "Panzdah-e Khordad", 2],
            ]
        )
        == 0
    )
    assert (
        catalog_ascii(
            [
                ["Tehran Grand Bazaar", "Khayyam", "Darvazeh Dolat"],
                ["Azadi Tower", "Meydan-e Azadi", "Towhid"],
                ["Milad Tower", "Milad Tower", "Mohammadieh"],
                ["Moslem Restaurant", "Panzdah-e Khordad", 2],
            ]
        )
        == 0
    )
    assert (
        catalog_ascii(
            [
                ["Tehran Grand Bazaar", "Khayyam", "Darvazeh Dolat"],
                ["Azadi Tower", "Meydan-e Azadi", 2],
            ]
        )
        == 0
    )


def test_catalog_text():
    assert (
        catalog_text(
            [
                ["Tehran Grand Bazaar", "Khayyam", "Darvazeh Dolat"],
                ["Azadi Tower", "Meydan-e Azadi", "Towhid"],
                ["Milad Tower", "Milad Tower", "Mohammadieh"],
                ["Moslem Restaurant", "Panzdah-e Khordad", 0],
                ["Golestan Palace", "Panzdah-e Khordad", 2],
            ]
        )
        == 0
    )
    assert (
        catalog_text(
            [
                ["Tehran Grand Bazaar", "Khayyam", "Darvazeh Dolat"],
                ["Azadi Tower", "Meydan-e Azadi", "Towhid"],
                ["Milad Tower", "Milad Tower", "Mohammadieh"],
                ["Moslem Restaurant", "Panzdah-e Khordad", 2],
            ]
        )
        == 0
    )
    assert (
        catalog_text(
            [
                ["Tehran Grand Bazaar", "Khayyam", "Darvazeh Dolat"],
                ["Azadi Tower", "Meydan-e Azadi", 2],
            ]
        )
        == 0
    )
